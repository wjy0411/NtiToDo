def rreadls(ff=""):
    with open(ff,'r',encoding='utf-8') as rl:
        return(rl.readlines())
    
def rread(fn=""):
    with open(fn,'r',encoding='utf-8') as re:
        return(re.read())