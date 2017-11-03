

import plantSIPN.sipn as mySipn

sipn_file = "test_sipn.txt"
f = open(sipn_file,'r')

mySipn.setSipnInput(f)
mySipn.createSipnFromInput()
mySipn.setExportTypeToPng()
mySipn.exportCreatedSipn()








