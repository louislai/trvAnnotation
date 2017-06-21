import os
import json

# Helper class that contains the current configuration of the Gui
# This config is loaded when started and saved when leaving
class configuration:
    # Constructor
    def __init__(self):
        # The filename of the image we currently working on
        self.currentFile = ""
        # The filename of the labels we currently working on
        self.currentLabelFile = ""
        # The filename of the corrections we currently working on
        self.currentCorrectionFile = ""
        # The path where the Cityscapes dataset is located
        self.csPath = ""
        # The path of the images of the currently loaded city
        self.city = ""
        # The name of the currently loaded city
        self.cityName = ""
        # The type of the current annotations
        self.gtType = ""
        # The split, where the currently loaded city belongs to
        self.split = ""
        # The path of the labels. In this folder we expect a folder for each city
        # Within these city folders we expect the label with a filename matching
        # the images, except for the extension
        self.labelPath = ""
        # The path to store correction markings
        self.correctionPath = ""
        # The transparency of the labels over the image
        self.transp = 0.5
        # The zoom toggle
        self.zoom = False
        # The zoom factor
        self.zoomFactor = 1.0
        # The size of the zoom window. Currently there is no setter or getter for that
        self.zoomSize = 400 #px
        # The highlight toggle
        self.highlight = False
        # The highlight label
        self.highlightLabelSelection = ""
        # Screenshot file
        self.screenshotFilename = "%i"
        # Correction mode
        self.correctionMode = False
        # Warn before saving that you are overwriting files
        self.showSaveWarning = True

    # Load from given filename
    def load(self, filename):
        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                jsonText = f.read()
                jsonDict = json.loads(jsonText)
                for key in jsonDict:
                    if key in self.__dict__:
                        self.__dict__[key] = jsonDict[key]
        self.fixConsistency()

    # Make sure the config is consistent.
    # Automatically called after loading
    def fixConsistency(self):
        if self.currentFile:
            self.currentFile      = os.path.normpath(self.currentFile)
        if self.currentLabelFile:
            self.currentLabelFile = os.path.normpath(self.currentLabelFile)
        if self.currentCorrectionFile:
            self.currentCorrectionFile = os.path.normpath(self.currentCorrectionFile)
        if self.csPath:
            self.csPath = os.path.normpath(self.csPath)
            if not os.path.isdir(self.csPath):
                self.csPath = ""
        if self.city:
            self.city = os.path.normpath(self.city)
            if not os.path.isdir(self.city):
                self.city = ""
        if self.labelPath:
            self.labelPath = os.path.normpath(self.labelPath)

        if self.correctionPath:
            self.correctionPath = os.path.normpath(self.correctionPath)

        if self.city:
            self.cityName == os.path.basename(self.city)

        if not os.path.isfile(self.currentFile) or os.path.dirname(self.currentFile) != self.city:
            self.currentFile = ""

        if not os.path.isfile(self.currentLabelFile)                       or \
           not os.path.isdir( os.path.join(self.labelPath,self.cityName) ) or \
           os.path.dirname(self.currentLabelFile) != os.path.join(self.labelPath,self.cityName):
            self.currentLabelFile = ""

        if not os.path.isfile(self.currentCorrectionFile)                       or \
           not os.path.isdir( os.path.join(self.correctionPath,self.cityName) ) or \
           os.path.dirname(self.currentCorrectionFile) != os.path.join(self.correctionPath,self.cityName):
            self.currentCorrectionFile = ""


    # Save to given filename (using pickle)
    def save(self, filename):
        with open(filename, 'w') as f:
            f.write(json.dumps(self.__dict__, default=lambda o: o.__dict__, sort_keys=True, indent=4))