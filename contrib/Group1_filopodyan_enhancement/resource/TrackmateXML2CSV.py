# !/usr/bin/env python3
# coding: utf-8
# author : Tong LI (tongli.bioinfo@gmail.com)
# BSD 3 license
import os
import pandas as pd
import xml.etree.cElementTree as et
from os import path

def readXml(path):
    if not os.path.lexists(path):
        raise IOError("File does not exist %s" %path)
    return et.fromstring(open(path, mode="r", encoding="utf-8").read())

def dropConstantCols(df):
    for col in df.columns:
        if len(df[col].unique()) ==1:
            del df[col]

def getAllTracks(path):
    xml = readXml(path)
    #########get all tracks' data##################
    filteredTracks = list(xml.find("Model").find("FilteredTracks"))
    filteredTracks = [ft.get("TRACK_ID") for ft in filteredTracks]

    allTracks = list(xml.find("Model").find("AllTracks"))
    if len(allTracks)>0:
        listTracks = list()
        for track in allTracks:
            listTracks.append(dict((x,y)for x,y in track.items()))
        allTracksDf = pd.DataFrame(listTracks,index=filteredTracks)
        dropConstantCols(allTracksDf)
        return allTracksDf
    else:
        return pd.DataFrame()

def getAllEdges(path):
    xml = readXml(path)
    allTracks = list(xml.find("Model").find("AllTracks"))
    if len(allTracks)>0:
        #########get all edges' data (in each track)##################
        dictTrack_Edges = dict()
        for track in allTracks:
            listEdges = list()
            for edge in list(track):
                listEdges.append(dict((x,y)for x,y in edge.items()))
            dictTrack_Edges[int(track.get("TRACK_ID"))] = pd.DataFrame(listEdges)
        allEdgesDf = pd.concat(dictTrack_Edges,keys=dictTrack_Edges.keys())
        dropConstantCols(allEdgesDf)
        return allEdgesDf
    else:
        return pd.DataFrame()

def getAllSpots(path):
    xml = readXml(path)
    ##########get all spots in each frame#########################
    allSpots = list(xml.find("Model").find("AllSpots"))
    spotInFrames = dict()
    for frame in list(allSpots):
        spots = list()
        if len(list(frame))>0:
            for spot in list(frame):
                spots.append(dict((x,y)for x,y in spot.items()))
            spotsDf = pd.DataFrame(spots)
            # spotsDf.reset_index(spotsDf["FRAME"])
            spotInFrames[int(frame.get("frame"))] = spotsDf
    allSpotsDf = pd.concat(spotInFrames)
    dropConstantCols(allSpotsDf)
    return allSpotsDf

