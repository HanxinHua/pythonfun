def main():
    p=add_two(3,5)
    subtract_two(2,1)
    q=multiply_two(3,p)
    print(q)

def add_two(v1,v2):
    """do something
    """
    p=v1+v2
    print(p)
    return p

def subtract_two(v1,v2):
    """do more
    """
    p=v1-v2
    print(p)

def multiply_two(v1,v2):
    """multiply two nums

    :param v1: num 1
    :param v2: num 2
    :returns: product num
    """
    p=v1*v2
    print(p)
    return p

if __name__=="__main__":

    """ __name__ is protected valuable
    """
    main()

