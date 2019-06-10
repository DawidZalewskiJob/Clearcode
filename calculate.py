def calculate(usb_size,memes):  #Dynamic programming solution

# ---------------------------INITIALIZATION----------------------------
    usb_size_mb = usb_size * 1024
    values = []
    weight = []
    memes_amount = len(memes)
    best_memes_order_names = set()
    best_memes_order_list = []
    avaible_weight = usb_size_mb

    for i in range(0,len(memes)):
        values.append(memes[i][2])
        weight.append(memes[i][1])

    #Creating a matrix with the length of memes and the width of (0,usb_size_mb) to alocate memory of
    #all previous steps

    #In each usb_size_mb step(step is 1) it store data about highest possible value of meme that can fit into.

    matrix = [[0 for i in range(usb_size_mb+1)] for i in range(memes_amount)]

# ---------------------------ALGORITHM----------------------------

    for current_mem in range (memes_amount):
        for matrix_weight_step in range(usb_size_mb+1):

            #if current mem doesn't fit into given weight of matrix then given heading
            #of matrix is replaced by old known memes weight (in that matrix weight step)

            if weight[current_mem] > matrix_weight_step:
                matrix[current_mem][matrix_weight_step] = matrix[current_mem-1][matrix_weight_step]
                continue
                
            #if current mem does fit into given heading of matrix then
            #choose higher value from: old meme value (in same step) OR
            #current meme that fit into heading of matrix AND previous mem with decreased
            #matrix weight step (as much as it took the place of the meme we put in)

            previous_value = matrix[current_mem-1][matrix_weight_step]
            nowa_opcja = values[current_mem] + matrix[current_mem-1][matrix_weight_step - weight[current_mem]]
            matrix[current_mem][matrix_weight_step] = max(previous_value,nowa_opcja)

    best_value = matrix[len(memes) - 1][usb_size_mb]
    remaining_value = best_value

    #decoding matrix to gain information about memes that was used to
    #build best solution

    for i in range((len(memes)-1), 0, -1):
        if remaining_value <= 0:
            break

        #if remaining value is not equal value from the right edge of matrix with height i
        #then it means current i memes was in the list of best value memes, then
        #correct remaing_value by subtracking used meme weight

        if remaining_value == matrix[i - 1][avaible_weight]:
            continue
        else:
            best_memes_order_list.append(i)
            remaining_value = remaining_value - values[i]
            avaible_weight = avaible_weight - weight[i]


    for i in best_memes_order_list:   #adding to set names of memes
        best_memes_order_names.add(memes[i][0])

    return(best_value,best_memes_order_names)
