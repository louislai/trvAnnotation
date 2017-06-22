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
        # The path where the dataset is located
        self.imagePath = ""
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
        # Warn before saving that you are overwriting files.
        self.showSaveWarning = False
        # Quick label enabled?
        self.quickLabel = True
        # Autosave?
        self.autoSave = True

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
        if self.imagePath:
            self.imagePath = os.path.normpath(self.imagePath)
            if not os.path.isdir(self.imagePath):
                self.imagePath = ""
        if self.labelPath:
            self.labelPath = os.path.normpath(self.labelPath)

        if self.correctionPath:
            self.correctionPath = os.path.normpath(self.correctionPath)

        if not os.path.isfile(self.currentFile):
            self.currentFile = ""

        if not os.path.isfile(self.currentLabelFile):
            self.currentLabelFile = ""

        if not os.path.isfile(self.currentCorrectionFile):
            self.currentCorrectionFile = ""


    # Save to given filename (using pickle)
    def save(self, filename):
        with open(filename, 'w') as f:
            f.write(json.dumps(self.__dict__, default=lambda o: o.__dict__, sort_keys=True, indent=4))