package fr.macave.test;
import android.content.*;import android.database.*;import android.net.Uri;import android.os.*;import java.io.*;
public class PhotoProvider extends ContentProvider{
 public boolean onCreate(){return true;}private File file(Uri uri)throws FileNotFoundException{String n=uri.getLastPathSegment();if(n==null||!n.matches("[a-f0-9-]{36}\\.jpg"))throw new FileNotFoundException();File d=new File(getContext().getCacheDir(),"captures");d.mkdirs();return new File(d,n);}
 public ParcelFileDescriptor openFile(Uri u,String mode)throws FileNotFoundException{return ParcelFileDescriptor.open(file(u),mode.contains("w")?ParcelFileDescriptor.MODE_CREATE|ParcelFileDescriptor.MODE_TRUNCATE|ParcelFileDescriptor.MODE_READ_WRITE:ParcelFileDescriptor.MODE_READ_ONLY);}
 public String getType(Uri u){return "image/jpeg";}public Cursor query(Uri u,String[] projection,String selection,String[] args,String sort){try{File f=file(u);MatrixCursor c=new MatrixCursor(new String[]{"_display_name","_size"});c.addRow(new Object[]{f.getName(),f.length()});return c;}catch(Exception e){return null;}}public Uri insert(Uri u,ContentValues v){return null;}public int update(Uri u,ContentValues v,String s,String[] a){return 0;}public int delete(Uri u,String s,String[] a){return 0;}
}
