from iron_worker import *

name ="FibWorker"
zip_name = "%s.zip" % name
zip_file = IronWorker.createZip(files=["fibonacci.py"], destination=zip_name, overwrite=True)
worker = IronWorker(config="config.ini")
res = worker.postCode(runFilename="fibonacci.py", name=name, zipFilename=zip_name)
print res
