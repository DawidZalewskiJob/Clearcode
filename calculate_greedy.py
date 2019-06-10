def sort(meme_list_numbers,values_per_unit,memes_value,memes_weight):    #bubble sorting

# ---------------------------SORTING----------------------------

    for i in range(0,len(meme_list_numbers)):
        j=len(meme_list_numbers)-1
        while j>i:  #Sorting from the largest to the smallest
            if values_per_unit[j] > values_per_unit[j-1]:
                tmp1 = values_per_unit[j]
                values_per_unit[j] = values_per_unit[j-1]
                values_per_unit[j-1] = tmp1

                #While sorting the values per unit it synchronizes
                #rest of the elements (value,weight,list)

                tmp2 = meme_list_numbers[j]
                meme_list_numbers[j] = meme_list_numbers[j-1]
                meme_list_numbers[j-1] = tmp2

                tmp3 = memes_value[j]
                memes_value[j] = memes_value[j-1]
                memes_value[j-1] = tmp3

                tmp4 = memes_weight[j]
                memes_weight[j] = memes_weight[j - 1]
                memes_weight[j - 1] = tmp4
            j-=1
    return meme_list_numbers,values_per_unit,memes_value,memes_weight

def calculate(usb_size, memes):  #greedy algorithm

# ---------------------------INITIALIZATION----------------------------

    usb_size_mb = usb_size * 1024
    number_of_memes = len(memes)
    meme_list_numbers = (list(range(0,number_of_memes)))
    memes_weight = []
    values_per_unit = []
    memes_value = []
    best_memes_order_names = set()
    value=0

    for i in range(0, len(meme_list_numbers)):
        memes_value.append(memes[i][2])
        memes_weight.append(memes[i][1])
        values_per_unit.append(memes_value[i] / memes_weight[i])

    least_mem_weight = min(memes_weight)

# ---------------------------ALGORITHM----------------------------

    sort(meme_list_numbers,values_per_unit,memes_value,memes_weight)

    for i in range(0,number_of_memes):  #Inserting to the final best memes list in sequence best value per unit
        if ( (usb_size_mb - memes_weight[i]) >= 0 ):
            usb_size_mb -= memes_weight[i]
            value += memes_value[i]

            best_memes_order_names.add(memes[meme_list_numbers[i]][0])
            if usb_size_mb < least_mem_weight:   #If the rest of weight is smaller then smallest memes return
                return (value, best_memes_order_names)

    return(value,best_memes_order_names)
