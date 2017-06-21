def enum(**enums):
    return type('Enum', (), enums)


class CorrectionBox:
    types = enum(TO_CORRECT=1, TO_REVIEW=2, RESOLVED=3, QUESTION=4)

    def __init__(self, rect=None, annotation=""):
        self.type = CorrectionBox.types.TO_CORRECT
        self.bbox = rect
        self.annotation = annotation
        self.selected = False

        return

    def get_colour(self):
        if self.type == CorrectionBox.types.TO_CORRECT:
            return QtGui.QColor(255, 0, 0)
        elif self.type == CorrectionBox.types.TO_REVIEW:
            return QtGui.QColor(255, 255, 0)
        elif self.type == CorrectionBox.types.RESOLVED:
            return QtGui.QColor(0, 255, 0)
        elif self.type == CorrectionBox.types.QUESTION:
            return QtGui.QColor(0, 0, 255)

    def select(self):
        if not self.selected:
            self.selected = True
        return

    def unselect(self):
        if self.selected:
            self.selected = False
        return

    # Read the information from the given object node in an XML file
    # The node must have the tag object and contain all expected fields
    def readFromXMLNode(self, correctionNode):
        if not correctionNode.tag == 'correction':
            return

        typeNode = correctionNode.find('type')
        self.type = int(typeNode.text)
        annotationNode = correctionNode.find('annotation')
        self.annotation = annotationNode.text
        bboxNode = correctionNode.find('bbox')
        x = float(bboxNode.find('x').text)
        y = float(bboxNode.find('y').text)
        width = float(bboxNode.find('width').text)
        height = float(bboxNode.find('height').text)
        self.bbox = QtCore.QRectF(x, y, width, height)

    # Append the information to a node of an XML file
    # Creates an object node with all children and appends to the given node
    # Usually the given node is the root
    def appendToXMLNode(self, node):

        # New object node
        correctionNode = ET.SubElement(node, 'correction')
        correctionNode.tail = "\n"
        correctionNode.text = "\n"

        # Name node
        typeNode = ET.SubElement(correctionNode, 'type')
        typeNode.tail = "\n"
        typeNode.text = str(int(self.type))

        # Deleted node
        annotationNode = ET.SubElement(correctionNode, 'annotation')
        annotationNode.tail = "\n"
        annotationNode.text = str(self.annotation)

        # Polygon node
        bboxNode = ET.SubElement(correctionNode, 'bbox')
        bboxNode.text = "\n"
        bboxNode.tail = "\n"

        xNode = ET.SubElement(bboxNode, 'x')
        xNode.tail = "\n"
        yNode = ET.SubElement(bboxNode, 'y')
        yNode.tail = "\n"
        xNode.text = str(int(round(self.bbox.x())))
        yNode.text = str(int(round(self.bbox.y())))
        wNode = ET.SubElement(bboxNode, 'width')
        wNode.tail = "\n"
        hNode = ET.SubElement(bboxNode, 'height')
        hNode.tail = "\n"
        wNode.text = str(int(round(self.bbox.width())))
        hNode.text = str(int(round(self.bbox.height())))
