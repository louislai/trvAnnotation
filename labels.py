#!/usr/bin/python
#
# Trv labels
#

from collections import namedtuple


#--------------------------------------------------------------------------------
# Definitions
#--------------------------------------------------------------------------------

# a label and all meta information
Label = namedtuple( 'Label' , [

    'name'        , # The identifier of this label, e.g. 'car', 'person', ... .
                    # We use them to uniquely name a class

    'id'          , # An integer ID that is associated with this label.

    'color'       , # The color of this label
    ] )


#--------------------------------------------------------------------------------
# A list of all labels
#--------------------------------------------------------------------------------

# Please adapt the train IDs as appropriate for you approach.
# Note that you might want to ignore labels with ID 255 during training.
# Further note that the current train IDs are only a suggestion. You can use whatever you like.
# Make sure to provide your results using the original IDs and not the training IDs.
# Note that many IDs are ignored in evaluation and thus you never need to predict these!

labels = [
    #       name                     id    color
    Label(  'background'            ,  0 ,  (  0,  0,  0)  ),
    Label(  'dense_trees'           ,  1 ,  ( 81,  0, 81)  ),
    Label(  'tree_farm'             ,  2 ,  (128, 64, 128) ),
    Label(  'flat_farm'             ,  3 ,  (244, 35, 232) ),
    Label(  'building'              ,  4 ,  (  0,  0, 142) ),
]

#--------------------------------------------------------------------------------
# Create dictionaries for a fast lookup
#--------------------------------------------------------------------------------

# name to label object
name2label      = { label.name    : label for label in labels           }
