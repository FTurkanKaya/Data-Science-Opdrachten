
#####################################################################
#####################################################################
##                           HUISWERK                              ##
#####################################################################
#####################################################################
# VRAAG 1 (Maak een virtuele omgeving met je eigen naam en installeer Python 3 tijdens het aanmaken.)
#############
# conda create -n FKaya  python=3

#VRAAG 2 (Activeer de aangemaakte omgeving.)
#############
# conda activate FKaya

#VRAAG 3 (Toon de lijst met geïnstalleerde pakketten.)
#############
# conda list

#VRAAG 4 (Installeer tegelijkertijd de nieuwste versie van Numpy en versie 1.2.1 van Pandas in de omgeving.)
#############
# conda install numpy pandas=1.2.1


#VRAAG 5 (Wat is de versie van de geïnstalleerde Numpy?)
#############
#  numpy-1.26.4

#VRAAG 6 (Upgrade Pandas. Wat is de nieuwe versie?)
#############
# conda update pandas
# conda list pandas  -->> pandas 2.2.3

#VRAAG 7 (Verwijder Numpy uit de omgeving.)
#############
# conda remove numpy

#VRAAG 8 ( Installeer de nieuwste versies van de Seaborn- en Matplotlib-bibliotheken tegelijkertijd.)
#############
# conda install seaborn matplotlib

#VRAAG 9 (Exporteer de pakketten in de virtuele omgeving met versie-informatie en bekijk het YAML-bestand.)
#############
# conda env export > environment.yml

#VRAAG 10 (Verwijder de aangemaakte omgeving (deactiveer de omgeving eerst).
#############
# conda deactivate
# conda env remove -n FKaya
# conda remove -n FKaya --all

