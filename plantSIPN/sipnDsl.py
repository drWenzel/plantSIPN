from sipnnetwork import sipnNetwork


class sipnDslService():
    def __init__(self):
        self.sipn = sipnNetwork()

    def setDslInput(self, sipnData):
        self.dslInput = sipnData

    def setSipnName(self,sipnNameAndPath):
        self.sipn.setSipnNameAndPath(sipnNameAndPath)

    def createSipnFromInput(self):
        for line in self.dslInput:
            aLine = dslLine(line)
            aLine.deleteUnnesserayElements()
            if (aLine.isNotEmpty() or not aLine.isComment()):
                if (aLine.isTimeTranistion()):
                    lineValues = aLine.getTransitionValues()
                    self.sipn.addTimeTranistion(lineValues["Name"], lineValues["Values"])
                elif (aLine.isClearTransition()):
                    lineValues = aLine.getTransitionValues()
                    self.sipn.addClearTransition(lineValues["Name"], lineValues["Values"])
                elif (aLine.isStandardTranistion()):
                    lineValues = aLine.getTransitionName()
                    self.sipn.addStandardTransition(lineValues["Name"])
                elif (aLine.isStdStelle()):
                    lineValues = aLine.getStellenValues()
                    self.sipn.addStandardPlace(lineValues["Name"])
                elif (aLine.isStartStelle()):
                    lineValues = aLine.getStellenValues()
                    print lineValues
                    self.sipn.addStartPlace(lineValues["Name"])
                elif (aLine.isInput()):
                    lineValues = aLine.getStellenValues()
                    self.sipn.addInput(lineValues["Name"])
                elif (aLine.isOutput()):
                    lineValues = aLine.getStellenValues()
                    self.sipn.addOutput(lineValues["Name"])
                elif (aLine.isStdEdge()):
                    lineValues = aLine.getStdEdgeValues()
                    self.sipn.addStdEdge(lineValues["Source"],lineValues["Target"])
                elif (aLine.isNotEdge()):
                    lineValues = aLine.getNotEdgeValues()
                    self.sipn.addNotEdge(lineValues["Source"],lineValues["Target"])
                elif (aLine.isOutputEdge()):
                    lineValues = aLine.getOutputEdgeValues()
                    self.sipn.addOutputEdge(lineValues["Source"],lineValues["Target"])
                elif (aLine.isStartLine()):
                    lineValues = aLine.getGraphName()
                    self.sipn.setSipnNameAndPath(lineValues['Name'])

    def exportSipn(self,activatedView=True):
        self.sipn.exportSipn(activatedView)

    def setExportTypeToSvg(self):
        self.sipn.setExportTypeToSvg()

    def setExportTypeToPng(self):
        self.sipn.setExportTypeToPng()


class dslLine():
    def __init__(self, line):
        self.line = line
        self.addElementNameList()
        self.deleteUnnesserayElements()

    def addElementNameList(self, ElementList = {"input":"eingang", "output":"ausgang","stdTransiton":"transition", "tTransition":"timertransition", "cTransition":"loeschtransition", "stdStelle":"stelle", "startStelle":"startstelle", "start":"@sipnNetwork:start", "ende":"@sipnNetwork:end"}):
        self.ElementList = ElementList

    def isNotEmpty(self):
        return (len(self.line)>1)

    def deleteUnnesserayElements(self):
        self.line = self.line.replace(' ', '')
        self.line = self.line.replace('\n', '')

    def isStandardTranistion(self):
        if self.line.startswith(self.ElementList["stdTransiton"]):
            return True

    def isTimeTranistion(self):
        if self.line.startswith(self.ElementList["tTransition"]):
            return True

    def isClearTransition(self):
        if self.line.startswith(self.ElementList["cTransition"]):
            return True

    def isStdStelle(self):
        if self.line.startswith(self.ElementList["stdStelle"]):
            return True

    def isStartStelle(self):
        if self.line.startswith(self.ElementList["startStelle"]):
            return True

    def isStartLine(self):
        if self.line.startswith(self.ElementList["start"]):
            return True

    def isInput(self):
        if self.line.startswith(self.ElementList["input"]):
            return True

    def isOutput(self):
        if self.line.startswith(self.ElementList["output"]):
            return True


    def isEndLine(self):
        if self.line.startswith(self.ElementList["ende"]):
            return True


    def getStellenValues(self):
        lineValues = self.splitByDoppleDot()
        return {"Name":lineValues[1]}

    def getTransitionValues(self):
        lineValues = self.splitByDoppleDot()
        lineValues = lineValues[1]
        lineValues = lineValues.split('/')
        return {"Name":lineValues[0], "Values": lineValues[1]}

    def getTransitionName(self):
        lineValues = self.splitByDoppleDot()
        lineValues = lineValues[1]
        lineValues = lineValues.split('/')
        return {"Name":lineValues[0]}

    def getGraphName(self):
        lineValues = self.splitByDoppleDot()
        lineValues = lineValues[1]
        lineValues = lineValues.split('/')
        return {"Name": lineValues[1]}

    def getLine(self):
        return self.line

    def splitByDoppleDot(self):
        return self.line.split(':')

    def isStdEdge(self):
        return self.line.find('->') <> -1

    def isNotEdge(self):
        return self.line.find('-O') <> -1

    def isOutputEdge(self):
        return self.line.find('..') <> -1

    def isTestEdge(self):
        return self.line.find('-|') <> -1

    def isComment(self):
        return  self.line.startswith('//')

    def getStdEdgeValues(self):
        values = self.line.split('->')
        return {"Source":values[0], "Target":values[1]}

    def getNotEdgeValues(self):
        values = self.line.split('-O')
        return {"Source":values[0], "Target":values[1]}

    def getOutputEdgeValues(self):
        values = self.line.split('..')
        return {"Source":values[0], "Target":values[1]}

    def getTestEdgeValues(self):
        values = self.line.split('-|')
        return {"Source":values[0], "Target":values[1]}




