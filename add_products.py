import csv
from numpy import product
from rdflib import *


def load_into_rdf():
    g = Graph()
    g.parse("expanded_ontology.ttl", format='ttl')

    g.namespace_manager.bind('TRASH', URIRef(
        'http://www.trashrobot.com/onto/'))

    TRASH = Namespace("http://www.trashrobot.com/onto/")

    with open("products - final.csv", newline='') as csvfile:
        product_reader = csv.reader(csvfile, delimiter=',')
        next(product_reader)
        for row in product_reader:
            # print(row)
            material = row[3]
            item = row[0].replace(" ", "")
            if material == 'organic':
                g.add((TRASH[item], RDF.type, TRASH.OrganicMaterial))
            elif material == "paper":
                g.add((TRASH[item], RDF.type, TRASH.PaperMaterial))
            elif material == "glass":
                g.add((TRASH[item], RDF.type, TRASH.GlassMaterial))
            elif material == "plastic":
                g.add((TRASH[item], RDF.type, TRASH.PlasticMaterial))
            elif material == "other":
                g.add((TRASH[item], RDF.type, TRASH.OtherMaterial))
            else:
                print(material)
                raise ValueError()

            g.add((TRASH[item], OWL.sameAs, URIRef(row[2])))

    g.serialize(destination="final_ontology.ttl")


load_into_rdf()
