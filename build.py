#!/usr/bin/env python3
"""Rebuild the TEST APK with Java 17+ (runtime sufficient), Python 3 and keytool."""
from pathlib import Path
import subprocess, urllib.request, zipfile, os
ROOT=Path(__file__).resolve().parent
os.chdir(ROOT)
from scripts.prepare_ocr import prepare
prepare()
TOOLS=ROOT/'tools'; TOOLS.mkdir(exist_ok=True)
def run(*args): subprocess.run([str(x) for x in args],check=True)
def download(name,url):
 p=TOOLS/name
 if not p.exists(): urllib.request.urlretrieve(url,p)
 return p
for name,url,check in [('build.zip','https://dl.google.com/android/repository/build-tools_r35_linux.zip','android-15/aapt'),('platform.zip','https://dl.google.com/android/repository/platform-35_r02.zip','android-35/android.jar')]:
 if not (TOOLS/'sdk'/check).exists():
  with zipfile.ZipFile(download(name,url)) as z:z.extractall(TOOLS/'sdk')
ecj=download('ecj.jar','https://repo.maven.apache.org/maven2/org/eclipse/jdt/ecj/3.33.0/ecj-3.33.0.jar')
bt=TOOLS/'sdk/android-15'; aj=TOOLS/'sdk/android-35/android.jar'
for p in ['aapt','zipalign']: (bt/p).chmod(0o755)
for p in ['build/classes','build/dex','out']:Path(p).mkdir(parents=True,exist_ok=True)
run('java','-jar',ecj,'-8','-encoding','UTF-8','-warn:none','-classpath',aj,'-d','build/classes',*Path('app/src').rglob('*.java'))
run(bt/'aapt','package','-f','-M','app/AndroidManifest.xml','-S','app/res','-A','app/assets','-I',aj,'-F','build/base.apk')
run('java','-cp',bt/'lib/d8.jar','com.android.tools.r8.D8','--min-api','26','--lib',aj,'--output','build/dex',*Path('build/classes').rglob('*.class'))
with zipfile.ZipFile('build/base.apk','a',compression=zipfile.ZIP_DEFLATED) as z:
 for f in Path('build/dex').glob('*.dex'):z.write(f,f.name)
run(bt/'zipalign','-f','4','build/base.apk','build/aligned.apk')
key=TOOLS/'test-signing.p12'
if not key.exists():run('keytool','-genkeypair','-keystore',key,'-storepass','macave-test-only','-keypass','macave-test-only','-alias','macave-test','-dname','CN=Ma Cave Test','-keyalg','RSA','-keysize','2048','-validity','10000','-noprompt')
run('java','-jar',bt/'lib/apksigner.jar','sign','--ks',key,'--ks-pass','pass:macave-test-only','--ks-key-alias','macave-test','--out','out/Ma-Cave-Test-0.1.apk','build/aligned.apk')
run('java','-jar',bt/'lib/apksigner.jar','verify','--verbose','out/Ma-Cave-Test-0.1.apk')
run(bt/'aapt','dump','badging','out/Ma-Cave-Test-0.1.apk')
print('APK: '+str(ROOT/'out/Ma-Cave-Test-0.1.apk'))
