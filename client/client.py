import qrl
import file2b64

print "Enter the file path of the file you would like to turn into a QR code!"
f=raw_input()
b64=file2b64.file2b64(f)
qrs=qrl.createQR(b64)
print "Enter a folder path in which you would like to save your QR codes."
folder=raw_input()
if folder[-1]!='/':
	folder+='/'

for qr in qrs:
	qr.save(open(folder+'out_'+str(qrs.index(qr))+'.png','w'))
print "It should be all saved! Happy scanning!"