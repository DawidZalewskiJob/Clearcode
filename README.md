# Clearcode
                          MISSION CODENAME: 


              ,,  ,,                                                      
`7MMF'        db *MM                                  mm                  
  MM              MM                                  MM                  
  MM        `7MM  MM,dMMb.   .gP"Ya `7Mb,od8 .gP"Ya mmMMmm ,pW"Wq.`7Mb,od8
  MM          MM  MM    `Mb ,M'   Yb  MM' "',M'   Yb  MM  6W'   `Wb MM' "'
  MM      ,   MM  MM     M8 8M""""""  MM    8M""""""  MM  8M     M8 MM    
  MM     ,M   MM  MM.   ,M9 YM.    ,  MM    YM.    ,  MM  YA.   ,A9 MM    
.JMMmmmmMMM .JMML.P^YbmdP'   `Mbmmd'.JMML.   `Mbmmd'  `Mbmo`Ybmd9'.JMML.  
                                                                                    
                                                                


The request from xXxDankScavengerxXxx initially seemed simple to me, but after first tests for a larger pool of data it turned out that without expensive quantum computers there will be impossible to compute the best funny_cat_memes sets in live long time. Unfortunately, my client, even though he's a big smuggler, still can't afford to buy expensive quantum computer or even TraumaTeam™ package , so the possibility of detection by the cops wasn't an option. So I had to use some tricks to make my program run as fast as possible to avoid risk of getting busted.

The task was selecting such a set of memes, that their profit was as high as possible. Actually the problem was limited to the backpack problem 1/0. That why I proposed three methods for its solution differing in computational complexity and quality of results. However the best approach to the problem you can find in file “calculate.py”.

The first method from the "calculate_brute_force" file is a complete overview of the solutions. Using brute-force I perform here the combination without repeating for each possible variant. Then we remember only the variant with the highest profit. Its advantage is finding the best set. The downside is the very high computational complexity ( O( 2^n) ) which for the order of tens is beyond the capabilities of modern computers.

The second method from the "calculate_greedy" file is the approximation algorithm (greedy). It is simple in action: we create information about value per unit factor of each meme and sort it from the largest to the smallest (I chose the bubble algorithm, but we can chose even better). The advantage of this algorithm is lower computational complexity depending on the sorting algorithm (in my case n^2). The downside of  that solution is that it’s not ideal, and in comparison to the third method is much worse. This algorithm maybe more interesting if same memes could be in the best set more then once.

The third method from the "calculate" file is a dynamic algorithm. The basis of this algorithm is to create a matrix (array) that contain information about memes located in each step of the possible weight (maximum is pendrive size). The height of this array is the number of memes and the width is the number of steps from 0 to usb_size_mb (with the size of step equal to 1). If a given mem does not fit in a given step, it insert an old mem that is already inscribed in memory arrays. If mem does fit, it chose the larger value from the old mem, or the new one and old one decreased by matrix weight step (as much as it took the place of the meme we put in) . Its advantage is low computational complexity of the order of polynomials. The downside is a slightly difficult method of implementation in comparison to the rest algorithms.

Summarizing the above pros and cons of the three methods I chose that xXxDankScavengerxXxx should use the "calculate.py" program (lowest calculation time and high value of memes sets)
