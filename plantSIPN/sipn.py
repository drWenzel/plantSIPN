
import sipnDsl as sipn

mySipn = sipn.sipnDslService()

def main():
   print "SIPN structure created - ready to build SPIN"


def setSipnInput(sipnInput):
    mySipn.setDslInput(sipnInput)

def createSipnFromInput():
    mySipn.createSipnFromInput()

def exportCreatedSipn():
    mySipn.exportSipn()

def setExportTypeToSvg():
    mySipn.setExportTypeToSvg()

def setExportTypeToPng():
    mySipn.setExportTypeToPng()


if __name__ == "__main__":
    # execute only if run as a script
    main()
