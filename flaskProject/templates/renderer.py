

def parser(way:str):
    '''

    :param way: Путь
    :return: HTMLString
    '''
    with open(way, 'r') as fs:
        page = fs.readlines()
        fnl = str()
        '''итоговая страничка'''
        for l in page:
            fnl += l
        return fnl