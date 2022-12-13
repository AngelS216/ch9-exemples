import logging


def logging_exemple():
    #On modifie le niveau d'affichage (avec lelvel = loggine.DEBUG) et redirige la journalisation vers un fichier (avec filename = "./log.txt") 
    logging.basicConfig(level=logging.DEBUG, filename="./log.txt")

    logging.debug("debug logging test") # -> information détaillée, intéressante seulement lorsqu'on diagnostique un problème
    logging.info("info logging test") #-> pour confirmer que tout fct comme prévu
    logging.warning("warning logging test") # -> indique s'il y a qqch inattendu qui arrive ou qui arrivera
    logging.error("error logging test") # -> problème sérieux, program = incapable to execute the job
    logging.critical("critical logging test") # -> serious error; program can't continue to fct


if __name__ == "__main__":
    logging_exemple()

    x =5
    x+=1
    print(x)