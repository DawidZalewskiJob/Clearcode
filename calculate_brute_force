from itertools import combinations #standard library

def calculate(usb_size, memes): #brute force method

# ---------------------------INITIALIZATION----------------------------
    usb_size_mb = usb_size * 1024
    meme_amount = len(memes)
    meme_list_numbers = (list(range(0,meme_amount)))
    best_price = 0
    best_meme_order_list = []
    best_meme_order_names = set()

# ---------------------------ALGORITHM----------------------------
    for i in range (1,meme_amount+1):   #creating combinations without repetition from i colection of all memes
        combinationss = combinations(meme_list_numbers, i) #note that combinations is already key word, that why i use "combinationss"

        for j in list(combinationss):  #The combinations has j invidual lists of memes
            weight = 0
            value = 0
            meme_order = []

            for k in list(j):   #Checking invidual k elements from j  list of memes
                meme_order.append(k)
                weight = memes[k][1] + weight
                if weight <= usb_size_mb:     #checking if the current sequence of memes fit on pendrive
                    value = memes[k][2] + value

                    if best_price < value:   #Saving best value and order
                        best_price = value
                        best_meme_order_list = meme_order[::]


    for i in best_meme_order_list:   #adding to set names of memes
        best_meme_order_names.add(memes[i][0])

    return(best_price,best_meme_order_names)
