# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 20:45:10 2022

@author: Kris
"""

import rdflib
import shapely.wkt

g = rdflib.Graph()

#Make sure that this points to the correct file
g.parse('./ontology.ttl', format='ttl')


def get_coords_bin_1():

    knows_query = """
    PREFIX geos: <http://www.opengis.net/ont/geosparql#>
    PREFIX TRASH: <http://www.trashrobot.com/onto/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    select distinct ?s ?co where { 
        ?s rdfs:label "trashbin2" .
        ?s geos:hasCentroid ?g .
        ?g geos:asWKT	?co .
    } limit 1"""

    qres = g.query(knows_query)
    
    for row in qres:
        coords = row.co
    
    return (shapely.wkt.loads(coords).x, shapely.wkt.loads(coords).y)

def get_coords_bin_2():
    knows_query = """
    PREFIX geos: <http://www.opengis.net/ont/geosparql#>
    PREFIX TRASH: <http://www.trashrobot.com/onto/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    select distinct ?s ?co where { 
        ?s rdfs:label "trashbin8" .
        ?s geos:hasCentroid ?g .
        ?g geos:asWKT	?co .
    } limit 1"""

    qres = g.query(knows_query)
    
    for row in qres:
        coords = row.co
    
    return (shapely.wkt.loads(coords).x, shapely.wkt.loads(coords).y)

def get_volume_bin_1():
    knows_query = """
    PREFIX geos: <http://www.opengis.net/ont/geosparql#>
    PREFIX TRASH: <http://www.trashrobot.com/onto/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    select distinct ?s ?vol where { 
        ?s rdfs:label "trashbin3" .
        ?s geos:hasMetricVolume ?vol .
    } limit 1"""

    qres = g.query(knows_query)
    
    for row in qres:
        vol = row.vol
    
    return float(vol)

def get_volume_bin_2():
    knows_query = """
    PREFIX geos: <http://www.opengis.net/ont/geosparql#>
    PREFIX TRASH: <http://www.trashrobot.com/onto/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    select distinct ?s ?vol where { 
        ?s rdfs:label "trashbin8" .
        ?s geos:hasMetricVolume ?vol .
    } limit 1"""

    qres = g.query(knows_query)
    
    for row in qres:
        vol = row.vol
    
    return float(vol)

def get_coords_obj():
    knows_query = """
    PREFIX geos: <http://www.opengis.net/ont/geosparql#>
    PREFIX TRASH: <http://www.trashrobot.com/onto/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    select distinct ?s ?co where { 
        ?s rdfs:label "trashObject11" .
        ?s geos:hasGeometry ?g .
        ?g geos:asWKT	?co .
    } limit 1"""

    qres = g.query(knows_query)
    
    for row in qres:
        coords = row.co
    
    return (shapely.wkt.loads(coords).x, shapely.wkt.loads(coords).y)

def get_volume_obj():
    knows_query = """
    PREFIX geos: <http://www.opengis.net/ont/geosparql#>
    PREFIX TRASH: <http://www.trashrobot.com/onto/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    select distinct ?s ?vol where { 
        ?s rdfs:label "trashObject11" .
        ?s geos:hasMetricVolume ?vol .
    } limit 1"""

    qres = g.query(knows_query)
    
    for row in qres:
        vol = row.vol
    
    return float(vol)

def get_coords_bin_a():
    knows_query = """
    PREFIX geos: <http://www.opengis.net/ont/geosparql#>
    PREFIX TRASH: <http://www.trashrobot.com/onto/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    select distinct ?s ?co where { 
        ?s rdfs:label "trashbin3" .
        ?s geos:hasCentroid ?g .
        ?g geos:asWKT	?co .
    } limit 1"""

    qres = g.query(knows_query)
    
    for row in qres:
        coords = row.co
    
    return (shapely.wkt.loads(coords).x, shapely.wkt.loads(coords).y)

def get_uri_obj():
    knows_query = """
    PREFIX TRASH: <http://www.trashrobot.com/onto/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    select distinct ?s where { 
        ?s rdfs:label "trashObject11" .
    } limit 100"""

    qres = g.query(knows_query)
       
    for row in qres:
        uri = row.s
    
    return str(uri)

def get_uri_robot():
    knows_query = """
    PREFIX TRASH: <http://www.trashrobot.com/onto/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    select distinct ?s where { 
        ?s rdfs:label "VURobot" .
    } limit 1"""

    qres = g.query(knows_query)
       
    for row in qres:
        uri = row.s
    
    return str(uri)

def get_uri_b1():
    knows_query = """
    PREFIX TRASH: <http://www.trashrobot.com/onto/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    select distinct ?s where { 
        ?s rdfs:label "trashbin2" .
    } limit 100"""

    qres = g.query(knows_query)
       
    for row in qres:
        uri = row.s
    
    return str(uri)

def get_uri_b2():
    knows_query = """
    PREFIX TRASH: <http://www.trashrobot.com/onto/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    select distinct ?s where { 
        ?s rdfs:label "trashbin8" .
    } limit 100"""

    qres = g.query(knows_query)
       
    for row in qres:
        uri = row.s
    
    return str(uri)

def get_uri_ba():
    knows_query = """
    PREFIX TRASH: <http://www.trashrobot.com/onto/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    select distinct ?s where { 
        ?s rdfs:label "trashbin3" .
    } limit 100"""

    qres = g.query(knows_query)
       
    for row in qres:
        uri = row.s
    
    return str(uri)

#Coordinate functions
#print(get_coords_bin_1())
#print(get_coords_bin_2())
#print(get_coords_bin_a())
#print(get_coords_obj())

#URI functions
#print(type(get_uri_b1()))
#print(get_uri_b2())
#print(get_uri_ba())
#print(get_uri_obj())
#print(get_uri_robot())

#Volume functions
print(get_volume_bin_1())
print(get_volume_bin_2())
print(get_volume_obj())