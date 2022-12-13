def syntax_error(some_list):
    #Il manquait un : à la fin de some_list)

    return sorted(some_list)


def sem_error(x, y):
    #On ne peut pas assuré que les varibales sont de même type et qu'ils peuvent s'additioner
    return x + y


def logical_error(count):
    x = 0
    while count > 0:
        x += 1
        count = x
    #Boucle infini, count est tjs > 0 car x ne fait qu'augmenter de 1 à chaque exécution de ce boucle while
    return x


if __name__ == '__main__':
    syntax_error([3,2,1])
    
    sem_error(5, "test")
    logical_error(8)
