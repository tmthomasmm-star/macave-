#!/usr/bin/env python3
"""Download pinned offline OCR resources with SHA-256 integrity checks."""
from pathlib import Path
import gzip,hashlib,io,json,tarfile,urllib.request
ROOT=Path(__file__).resolve().parents[1]
def prepare():
 target=ROOT/'app/assets/ocr';target.mkdir(parents=True,exist_ok=True)
 dependencies=json.loads((ROOT/'ocr-dependencies.json').read_text())
 resources={
 'tesseract.tgz':{'package/dist/tesseract.min.js':'tesseract.min.js','package/dist/worker.min.js':'worker.min.js'},
 'core.tgz':{'package/tesseract-core-lstm.wasm.js':'tesseract-core-lstm.wasm.js','package/tesseract-core-lstm.wasm':'tesseract-core-lstm.wasm'}
 }
 for name,url,sha in dependencies:
  expected=list(resources.get(name,{}).values()) if name in resources else ['fra.traineddata']
  if all((target/n).is_file() for n in expected):continue
  data=urllib.request.urlopen(url,timeout=90).read()
  if hashlib.sha256(data).hexdigest()!=sha:raise RuntimeError('Integrity check failed: '+name)
  if name.endswith('.tgz'):
   with tarfile.open(fileobj=io.BytesIO(data),mode='r:gz') as archive:
    for source,dest in resources[name].items():
     member=archive.extractfile(source)
     if member is None:raise RuntimeError('Missing resource: '+source)
     (target/dest).write_bytes(member.read())
  else:(target/'fra.traineddata').write_bytes(gzip.decompress(data))
 print('Offline OCR resources ready.')
if __name__=='__main__':prepare()
