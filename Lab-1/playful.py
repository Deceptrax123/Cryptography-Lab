
def generate_digrams(word):
    word=word.replace(" ","")

    digrams=list()
    dig=""
    for c,letter in enumerate(word):
        dig+=letter
        if (c+1)%2==0:
            if dig[0]==dig[1]:
                dig=dig[0]+"x"
            digrams.append(dig)
            dig=""
    if len(word)%2!=0:
        digrams[-1]=digrams[-1][0]+"z"
    
    return digrams
    

def generate_matrix():
    pass 

def search():
    pass

if __name__=='__main__':
    word="hello world"
    k=generate_digrams(word)
    print(k)
