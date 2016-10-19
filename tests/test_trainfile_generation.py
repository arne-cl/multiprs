# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
from multiprs import corpustools
from lxml import etree
import re
import pytest
import os

# Path to directory with manually pos tagged exb files

tdata = os.path.abspath("./tdata/")
# Path to directory to exb files without pos tags 

# def tokenpos(trdata):
#     trfiles = {}
#     try:
#         for fn, t, p in trdata:
#             tp = []
#             for token in t:
#                 tkn = token[1].rstrip(' \t\n')
#                 for pos in p:
#                     if pos[1] == None:
#                         continue
#                     if token[0] == pos[0]:
#                         tp.append((token[0], tkn, pos[1].rstrip(' \t\n')))
#                         continue
#                 if tkn == u'.':
#                     tp.append((token[0], tkn, '.$'))
#                     continue
#                 elif tkn == u',':
#                     tp.append((token[0], tkn, ',$'))
#                     continue
#                 elif tkn == u';':
#                     tp.append((token[0], tkn, ';$'))
#                     continue
#                 elif tkn == u'?':
#                     tp.append((token[0], tkn, '?$'))
#                     continue
#                 elif tkn == u'!':
#                     tp.append((token[0], tkn, '!$'))
#                     continue
#                 elif tkn == u'• • •' or tkn == '• •' or tkn == '•':
#                     tp.append((token[0], tkn, 'PAUSE'))
#                     continue
#                 elif re.match('\(\(\d,\ds\)\)',tkn):
#                     tp.append((token[0], tkn, 'PAUSE'))
#                     continue
#
#             trfiles.update({fn: tp})
#     except TypeError:
#         print("tokenpos: none type reference")
#     return trfiles

#
# def tokenpos(trdata):
#     trfiles = {}
#     for fn, t, p in trdata:
#         tp = []
#
#         for token in t:
#             for pos in p:
#                 if token[0] == pos[0]:
#                     tp.append((token[0], token[1], pos[1]))
#         trfiles.update({fn: tp})
#
#     return trfiles
#
#
# def create_tagger_trainingfile(trainingsources, trainingfilepath, type='treetagger'):
#     """
#     creates a textfile conform to the train-tree-tagger input format
#     (verticalized token \t pos \n lines of a file)
#     param: traingsources: filepath to all .exb training files
#     param: trainingfilepath: path and filename of the text trainingfile
#     param: type: either treetagger or brill to determine the style of the trainingfile.
#     """
#     traindata_iterator = corpustools.ExmaTokenPOSIterator(trainingsources)
#     data = tokenpos(traindata_iterator)
#
#     with open(trainingfilepath,  "w") as tt_trainingfile:
#         for postuples_tier in data.itervalues():
#         # print("{}{}".format(postuple_tier, "\n"*2))
#             for postuple in postuples_tier:
#                 if type=='treetagger':
#                     line = "{}\t{}\t{}".format(postuple[1], postuple[2], u'\n')
#                 elif type=='brill':
#                     line = "{}|{}{}".format(postuple[1], postuple[2], u'\n')
#                 line8 = line.encode('UTF-8')
#                 try:
#                     tt_trainingfile.write(line8)
#                 except UnicodeEncodeError:
#                     print("unicode error in tuple {}".format(postuple))


def test_traindata():
    """
    this test runs to find non-parsed element-tiers in the exmaralda sources
    :return:
    """
    traindata_iterator = corpustools.make_tier_tuple_list(tdata)
    for fname, token, pos in traindata_iterator:
        assert fname != None
        assert token != None
        assert pos != None




def test_v_tupels():
    """
    Are all verbal tier tupels created without None values?
    :return:
    """
    traindata_iterator = corpustools.make_tier_tuple_list(tdata)
    tlist = [(fname, v_tupels, pos_tupels) for fname, v_tupels, pos_tupels in traindata_iterator]

    for fname, v_tupels, pos_tupels in tlist:

        assert len(v_tupels) > 1
        for tupel in v_tupels:
            timestamp = tupel[0]
            value = tupel[1]
            assert timestamp != None
            assert value != None



def test_pos_tupels():
    """
    Are all pos tier tupels created without None values?
    :return:
    """
    traindata_iterator = corpustools.make_tier_tuple_list(tdata)
    for fname, v_tupels, pos_tupels in traindata_iterator:

        assert len(pos_tupels) > 1
        for tupel in pos_tupels:
            timestamp = tupel[0]
            value = tupel[1]
            assert timestamp != None
            assert value != None

def test_tokenpos():
    trdata = corpustools.make_tier_tuple_list(tdata)
    trfiles = {}

    # check if trdata is iterable
    assert hasattr(trdata, '__iter__')
    counter = 0
    for fn, t, p in trdata:
        counter += 1
        tp = []

        for token in t:
            for pos in p:
                if token[0] == pos[0]:
                    tp.append((token[0], token[1], pos[1]))
        trfiles.update({fn: tp})

    assert len(trfiles) == counter



