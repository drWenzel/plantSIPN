
import graphviz as gv
import sys
import os

'''
   Nutzen in der LV Produkt als Problem-Tool Beispiel
   -> Lean-Canvas
'''


# ToDo: Abstracte Klasse draus machen
class sipnElement:
    """A simple example class"""

    def __init__(self):
        self.createSubgraphLayout()
        self.createNoteRepository()

    def createSubgraphLayout(self):
        return None

    def createNoteRepository(self):
        self.Nodes = {}

    def createSubGraph(self):
        try:
            self.addNodesToSubGraph()
        except:
            print("Unexpected error:", sys.exc_info()[0])

    def addNodesToSubGraph(self):
        for key, value in self.Nodes.iteritems():
            self.elementOfSipn.node(key, value)

    def getAndCreateSubGraph(self):
        self.createSubGraph()
        return self.elementOfSipn

    def getSubGraph(self):
        return self.elementOfSipn


# TRANSITIONEN
# ---------------------------------------------------------

class StandardTransition(sipnElement):
    def createSubgraphLayout(self):
        self.elementOfSipn = gv.Digraph('StdTrans')
        self.elementOfSipn.node_attr.update(shape="record", fixedsize="true", width="1.5")

    def addNode(self, transitionsName):
        label = str(transitionsName)
        self.Nodes[transitionsName] = label

class TimeTransition(sipnElement):
    '''Zeit'''

    def createSubgraphLayout(self):
        self.elementOfSipn = gv.Digraph('TimeTrans')
        self.elementOfSipn.node_attr.update(shape="record", fixedsize="true", width="1.5")

    def addNode(self, transitionsName, tranistionsZeit):
        label = "<f0> " + str(transitionsName) + " |<f1> t |<f2> - " + str(tranistionsZeit)
        self.Nodes[transitionsName] = label


class ClearTransiton(sipnElement):
    '''Loeschtransition'''

    def createSubgraphLayout(self):
        self.elementOfSipn = gv.Digraph('ClearTrans')
        self.elementOfSipn.node_attr.update(shape="record", fixedsize="true", width="1.5")

    def addNode(self, transitionsName, placesToBeCleared):
        label = "<f0> " + str(transitionsName) + " |<f1> x |<f2> " + str(placesToBeCleared)
        self.Nodes[transitionsName] = label

# Platze
# -----------------------------------------
class Place(sipnElement):
    ''' STD Platz'''

    def createSubgraphLayout(self):
        self.elementOfSipn = gv.Digraph('Places')
        self.elementOfSipn.node_attr.update(shape="circle", fixedsize="true", width="1.5")

    def addNode(self, placeName):
        label = str(placeName)
        self.Nodes[placeName] = label

class StartPlace(Place):
    ''' Startplatz'''

    def createSubgraphLayout(self):
        self.elementOfSipn = gv.Digraph('StartPlaces')
        self.elementOfSipn.node_attr.update(shape="doublecircle", fixedsize="true", width="1.5")

class InputPlace(Place):
    ''' Startplatz'''

    def createSubgraphLayout(self):
        self.elementOfSipn = gv.Digraph('InputPlaces')
        self.elementOfSipn.node_attr.update(penwidth = "0", shape = "record", fixedsize="true")

class OutputPlace(Place):
    ''' Startplatz'''

    def createSubgraphLayout(self):
        self.elementOfSipn = gv.Digraph('OutputPlaces')
        self.elementOfSipn.node_attr.update(penwidth="0", shape="record", fixedsize="true")

# Verknuepfungen
# ----------------------------------
class EdgesBetweenElements(sipnElement):
    '''Verknuepfungen zwischen Stellen und Trans'''

    def __init__(self):
        self.createSubgraphLayout()

    def createSubgraphLayout(self):
        self.elementOfSipn = gv.Digraph('Edges')

    def addStdEdge(self, EdgeStart, EdgeEnd,EdgeLable=""):
        self.elementOfSipn.edge(EdgeStart, EdgeEnd, label="", arrowhead="", style="")

    def addOutputEdge(self, EdgeStart, EdgeEnd,EdgeLable=""):
        self.elementOfSipn.edge(EdgeStart, EdgeEnd, label="", arrowhead="none", style="dotted")

    def addNotEdge(self, EdgeStart, EdgeEnd,EdgeLable=""):
        self.elementOfSipn.edge(EdgeStart, EdgeEnd, label="", arrowhead="odot", style="")

    def createSubGraph(self):
        return None

# SIPN
# ---------------------------------

class sipnNetwork:
    def __init__(self, nameAndPath="img\_temp"):
        self.sipnGraph = gv.Digraph(format='svg')
        self.stdTransition = StandardTransition()
        self.timeTransition = TimeTransition()
        self.clearTransitions = ClearTransiton()
        self.places = Place()
        self.startPlaces = StartPlace()
        self.input = InputPlace()
        self.output = OutputPlace()
        self.edges = EdgesBetweenElements()
        self.setSipnNameAndPath(nameAndPath)

    def setSipnNameAndPath(self,nameSipn):
        self.sipnNameAndPath = nameSipn

    def addStandardTransition(self, transistionName):
        self.stdTransition.addNode(transistionName)

    def addTimeTranistion(self,transistionName,transitionValue):
        self.timeTransition.addNode(transistionName,transitionValue)

    def addClearTransition(self,transitionName,transitionValue):
        self.clearTransitions.addNode(transitionName,transitionValue)

    def addStandardPlace(self,placeName):
        self.places.addNode(placeName)

    def addStartPlace(self,placeName):
        self.startPlaces.addNode(placeName)

    def addInput(self,inputName):
        self.input.addNode(inputName)

    def addOutput(self,outputName):
        self.output.addNode(outputName)

    def addStdEdge(self,EdgeStart,EdgeEnd):
        self.edges.addStdEdge(EdgeStart,EdgeEnd)

    def addOutputEdge(self, EdgeStart, EdgeEnd):
        self.edges.addOutputEdge(EdgeStart, EdgeEnd)

    def addNotEdge(self, EdgeStart, EdgeEnd):
        self.edges.addNotEdge(EdgeStart, EdgeEnd)

    def exportSipn(self, activatedView=True):
        self.buildSubGraphs()
        localPath = os.getcwd() + "/"
        print self.sipnGraph.source
        self.sipnGraph.render(str(localPath)+ str(self.sipnNameAndPath), view=activatedView)


    def buildSubGraphs(self):
        self.sipnGraph.subgraph(self.startPlaces.getAndCreateSubGraph())
        self.sipnGraph.subgraph(self.input.getAndCreateSubGraph())
        self.sipnGraph.subgraph(self.places.getAndCreateSubGraph())
        self.sipnGraph.subgraph(self.output.getAndCreateSubGraph())

        self.sipnGraph.subgraph(self.stdTransition.getAndCreateSubGraph())
        self.sipnGraph.subgraph(self.clearTransitions.getAndCreateSubGraph())
        self.sipnGraph.subgraph(self.timeTransition.getAndCreateSubGraph())

        self.sipnGraph.subgraph(self.edges.getAndCreateSubGraph())


    def setExportTypeToSvg(self):
        self.sipnGraph = gv.Digraph(format='svg')

    def setExportTypeToPng(self):
        self.sipnGraph = gv.Digraph(format='png')

