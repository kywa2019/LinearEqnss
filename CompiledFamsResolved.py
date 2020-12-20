#code for generating maple inputs for confining symmetric triangle of BOTH family one and two
#author Kevin Wu
while True:

    print("\n-----------------------------------------------------------------------------------------------------\n"
    "Directions:\nPlease type numerical input directly w/o any extras.\nInput takes ALL sites counted individually from the triangle.\n\n")
    keyValue = int(input("What are the total number of sites?"))                        #allows inputter to choose triangle to generate output
    x = keyValue                                                                        #set input value for site_max()

    if ((x**(1/2))) % 3 == 1:
        def site_max(x):                                                                #generates total number of sites/traps for a given parallel triangle
            milk = 0
            while_count = 4
            triangle_num = (x**(1/2)-4)/3
            total_count = 4
            while milk < triangle_num:
                while_count += 3
                total_count += while_count
                milk += 1
            return total_count
        site_total = site_max(x)
    else:
        def site_max2(x):                                                              #generates total number of sites/traps for a given parallel triangle
            milk = 0
            while_count = 5
            triangle_num = (x**(1/2)-5)/3
            total_count = 6
            while milk < triangle_num:
                while_count += 3
                total_count += while_count
                milk += 1
            return total_count
        site_total = site_max2(x)


    traps = []
    def var_gen(site_total):                                                            #generates list of vars to be used in the maple input
        counter = 1
        for i in range(1, int(site_total) + 1):
            value = " x(" + str(counter) + ")"
            traps.append(value)
            counter += 1
        return str(",".join(traps))

    if ((x**(1/2))) % 3 == 1:
        def eqnss_full():                                                               #generates average and variable equations for maple input (doesn't contain x(T))
            def avg_fnc(site_total):                                                    #generates the average function using the site_total input
                #important code initializers
                lrg_count = 4                                                           #keeps track of total 6* needed in current iteration
                sml_countdown = 3                                                       #keeps track of total 3* needed in current iteration
                ff_sml = 3                                                              #small fractal constant 3*
                ff_lrg = 6                                                              #large fractal constant 6*
                var_iter = 3                                                            #current site to put into variable
                current_fam = 3                                                         #same thing as var_iter but used as separate comparator

                avg = ["3*x(" + str(1) + ")+", "6*x(" + str(2) + ")+"]                  #list with initial eqnss elements

                while current_fam < site_total:                                         #loops through to add new elements to var list

                    while sml_countdown > 0 and current_fam <= site_total:              #loops through to add small fractals with 3* pattern beginning
                        if current_fam < site_total:                                    #goes through all sites except last one, conditionalized for both pattern status and site total
                            piece = str(ff_sml) + "*x(" + str(var_iter) + ")+"
                            avg.append(piece)
                            var_iter += 1
                            sml_countdown -= 1
                            current_fam += 1
                        elif current_fam == site_total:                                 #only goes through last site to remove extra + sign
                            piece = str(ff_sml) + "*x(" + str(var_iter) + ")"
                            avg.append(piece)
                            var_iter += 1
                            sml_countdown -= 1
                            current_fam += 1
                    sml_countdown += 3                                                  #refreshes count to match small fractal pattern

                    lrg_countdown = lrg_count                                           #refreshes count to match lrg fractal pattern
                    while lrg_countdown > 0 and current_fam <= site_total:              #loops through to add large fractals with 6* pattern beginning
                        if current_fam < site_total:                                    #goes through all large sites except last one, conditionalized for both pattern status and site total
                            piece = str(ff_lrg) + "*x(" + str(var_iter) + ")+"
                            avg.append(piece)
                            var_iter += 1
                            lrg_countdown -= 1
                            current_fam += 1
                        elif current_fam == site_total:                                 #only goes through last site to get rid of extra + sign
                            piece = str(ff_lrg) + "*x(" + str(var_iter) + ")"
                            avg.append(piece)
                            var_iter += 1
                            lrg_countdown -= 1
                            current_fam += 1
                    lrg_count += 3                                                      #change lrg_count and countdown to match 6* pattern
                    # adds to overall count to match pattern
                average_eqnss = "".join(avg)
                print("eqnss:={x(T)=0, x(average)=("+str(average_eqnss)+")/"+str(int(keyValue)-1)+",")
            avg_fnc(site_total)

            #use len(site_paths)+1 as current-operating site indicator
            #len(site_paths) is technically the previous site since we have yet to finish building the current one
            site_paths = {1:[2,2,"T"],2:[1,3],3:[2,2,4],4:[3]}                          #dictionary with initial triangle elements

            def num_gen():                                                              #generates dictionary filled with site# (key) and a list of possible site paths (value)

                def actual_cons(x):                                                     #creates total number of cycles for script to iterate through
                    constant_1 = ((x**(1/2))//3) - 1                                    #subtract one since number of cycles actual must be accurate
                    return constant_1
                actual_cycle = int(actual_cons(x))


                def fam_cons(x):                                                        #creates empty-space predictor constant based off parent traingle
                    constant = x**(1/2)-(3*actual_cycle)
                    return constant
                group_cons = int(fam_cons(x))

                #list of initialized value for next
                true_table = []                                                         #created artificial error catcher
                oddity = 2                                                              #oddity value to be put-in
                store = 1                                                               #stores ending site from parent function to use on next iteration
                odditySwtch = 0                                                         #accounts for the pattern switch occuring every 2 cycles that changes oddity location from even to odd sites
                oddity_cntr = 0                                                         #counts total number of oddities
                oddity_total = 2                                                        #tracks totla number of oddities necessary to fulfill given cycle
                cycle_count = 0                                                         #counts number of cycles/iterations that have finished where n=49 is cycle 0 and n=100 is cycle 1
                if keyValue == 16:                                                      #conditionalized to fulfill n=16 triangle
                    return site_paths
                if keyValue > 16:                                                       #fulfills all other triangle
                    while cycle_count < actual_cycle:                                   #iterates until generating all site paths necessary

                        def getKeys(site_paths):                                        #returns all keys in the dictionary also known as sites/trap#s
                            return site_paths.keys()
                        keys = getKeys(site_paths)

                        if cycle_count == 0:                                            #artificial elements for mistakes catching
                            for i in site_paths:
                                true_table.append('False: ' + str(i))
                        if cycle_count > 0:
                            for i in range(store, int(len(keys) + 1)):
                                true_table.append('False: ' + str(i))

                        for i in range(store, int(len(keys) + 1)):                      #checks case of 3 total site_paths to make sure all empty spaces are filled
                            if len(site_paths[i]) == 3:
                                true_table[i - 1] = 'True: ' + str(i)
                            elif len(site_paths[i]) == 2:
                                value = i + group_cons                                  #checks case of 2 and 1 site_path(s) filling in Both values dependent on given cases
                                site_paths[i].append(value)
                                true_table[i - 1] = 'True: ' + str(i)
                            elif len(site_paths[i]) == 1:
                                value = i + group_cons
                                site_paths[i].append(value)
                                site_paths[i].append(value)
                                true_table[i - 1] = 'True: ' + str(i)


                        if cycle_count % 2 == 0 and odditySwtch % 2 == 0:               #conditionalizes oddity values and count for given environment
                            site_paths[len(site_paths) + 1] = [len(site_paths) + 2, len(site_paths) + 2]
                            #generates ending value pair
                        elif cycle_count % 2 == 1 and odditySwtch % 2 == 0:
                            oddity -= 1
                            site_paths[len(site_paths) + 1] = [oddity, len(site_paths) + 2, len(site_paths) + 2]
                            oddity += 2
                            oddity_cntr += 1

                        if cycle_count % 2 == 0 and odditySwtch % 2 == 1:               #conditionalizes oddity values and count for given environment
                            site_paths[len(site_paths) + 1] = [len(site_paths) + 2, len(site_paths) + 2]
                            #generates ending value pair
                        elif cycle_count % 2 == 1 and odditySwtch % 2 == 1:
                            oddity -= 1
                            site_paths[len(site_paths) + 1] = [oddity, len(site_paths) + 2, len(site_paths) + 2]
                            oddity += 2
                            oddity_cntr += 1

                        store = len(site_paths)                                         #refreshes store value for next cycle
                                                                                        #code to generate new numbers after filling past numbers begins
                        a_gen = 6 + 3*(cycle_count)                                     #keeps track of a-column number generation (see excel spread: Pattern Search)
                        b_gen = 5 + 3*(cycle_count)                                     #keeps trakc of b-column number generation

                        if cycle_count % 2 == 0:                                        #conditionales oddity counter based off current cycle since changes every cycle
                            oddity_cntr = 0                                             #some new cycles begin with oddity (3 paths) while others start without (two path)
                        if cycle_count % 2 == 1:
                            oddity_cntr = 1

                        while a_gen or b_gen > 0:                                       #iterates to generate new values
                            group_cur = []                                              #empty list to change and adapt to new site paths
                            if a_gen and b_gen > 0:
                                a_cur = len(site_paths)
                                b_cur = len(site_paths) + 2
                                group_cur.append(a_cur)
                                group_cur.append(b_cur)
                                fam_num = len(site_paths) + 1
                                if fam_num % 2 == 0 and oddity_cntr < oddity_total and odditySwtch % 2 == 0:
                                                                                        #accounts for empty spaces on x-column and oddity filter based on site(odd/even), total odditities, and current environment
                                    group_cur.append(oddity)
                                    oddity += 2
                                    oddity_cntr += 1
                                elif fam_num % 2 == 0 and oddity_total == oddity_cntr and odditySwtch % 2 == 0:
                                    group_cur.append(a_cur)

                                if fam_num % 2 == 1 and oddity_cntr < oddity_total and odditySwtch % 2 == 1:
                                                                                        #accounts for empty spaces on x-column and oddity filter based on site(odd/even), total odditities, and current environment
                                    group_cur.append(oddity)
                                    oddity += 2
                                    oddity_cntr += 1
                                elif fam_num % 2 == 1 and oddity_total == oddity_cntr and odditySwtch % 2 == 1:
                                    group_cur.append(a_cur)
                                group_cur.sort()
                                site_paths[len(site_paths) + 1] = group_cur             #sets new dictionary values with site as key and current site paths as a list value
                                a_gen -= 1
                                b_gen -= 1

                            else:
                                a_cur = len(site_paths)
                                group_cur.append(a_cur)
                                site_paths[len(site_paths) + 1] = group_cur
                                a_gen -= 1

                        if cycle_count % 2 == 0:                                        #conditionalizes oddity total necessary based off the current cycle environment
                            oddity_total += 2
                        if cycle_count % 2 == 1:
                            oddity_total += 1

                        group_cons += 3                                                 #refreshes group_cons to adapt to new children (future) iterations
                        cycle_count += 1
                        if cycle_count % 2 == 0:                                        #keeps track of changes in every two cycles so that environment is updated accurately
                            odditySwtch += 1

            num_gen()

            def eqnss_gen(site_total):                                                  #generates compilation of equations one by one
                i = 1                                                                   #iterator value to feed yield generator
                # change False to i < int(site_total+1) when wanting to use the function
                while i < int(site_total+1):
                    yield i
                    i += 1

            for i in eqnss_gen(site_total):                                             #iterates and calls on the function defined above
                length = len(site_paths[i])                                             #defines variable specifier
                if length == 3:                                                         #conditionalizes specific equations to generate one by one
                    value = "x("+str(i)+")=(1/3)*((x("+str(site_paths[i][0])+")+1)+(x("+str(site_paths[i][1])+")+1)+(x("+str(site_paths[i][2])+")+1)),"
                    print(value)
                elif length == 2:
                    value = "x("+str(i)+")=(1/2)*((x("+str(site_paths[i][0])+")+1)+(x("+str(site_paths[i][1])+")+1)),"
                    print(value)
                elif length == 1:
                    value = "x("+str(i)+")=(1)*((x("+str(site_paths[i][0])+")+1))}:\na:=solve(eqnss,b);"
                    print(value)

####transitiion for FamilyII code---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    elif ((x**(1/2))) % 3 == 2:
        def eqnss_full2():                                                              # generates average and variable equations for maple input (doesn't contain x(T))
            def avg_fnc2(site_total):                                                   # generates the average function using the site_total input
                                                                                        # important code initializers
                lrg_count = 5                                                           # keeps track of total 6* needed in current iteration
                sml_countdown = 3                                                       # keeps track of total 3* needed in current iteration
                ff_sml = 3                                                              # small fractal constant 3*
                ff_lrg = 6                                                              # large fractal constant 6*
                var_iter = 5                                                            # current site to put into variable
                current_fam = 5                                                         # same thing as var_iter but used as separate comparator

                avg = ["3*x(" + str(1) + ")+", "6*x(" + str(2) + ")+", "3*x(" + str(3) + ")+", "6*x(" + str(4) + ")+"]
                                                                                        # list with initial eqnss elements

                while current_fam < site_total:                                         # loops through to add new elements to var list

                    while sml_countdown > 0 and current_fam <= site_total:              # loops through to add small fractals with 3* pattern beginning
                        if current_fam < site_total:                                    # goes through all sites except last one, conditionalized for both pattern status and site total
                            piece = str(ff_sml) + "*x(" + str(var_iter) + ")+"
                            avg.append(piece)
                            var_iter += 1
                            sml_countdown -= 1
                            current_fam += 1
                        elif current_fam == site_total:                                 # only goes through last site to remove extra + sign
                            piece = str(ff_sml) + "*x(" + str(var_iter) + ")"
                            avg.append(piece)
                            var_iter += 1
                            sml_countdown -= 1
                            current_fam += 1
                    sml_countdown += 3                                                  # refreshes count to match small fractal pattern

                    lrg_countdown = lrg_count                                           # refreshes count to match lrg fractal pattern
                    while lrg_countdown > 0 and current_fam <= site_total:              # loops through to add large fractals with 6* pattern beginning
                        if current_fam < site_total:                                    # goes through all large sites except last one, conditionalized for both pattern status and site total
                            piece = str(ff_lrg) + "*x(" + str(var_iter) + ")+"
                            avg.append(piece)
                            var_iter += 1
                            lrg_countdown -= 1
                            current_fam += 1
                        elif current_fam == site_total:                                 # only goes through last site to get rid of extra + sign
                            piece = str(ff_lrg) + "*x(" + str(var_iter) + ")"
                            avg.append(piece)
                            var_iter += 1
                            lrg_countdown -= 1
                            current_fam += 1
                    lrg_count += 3                                                      # change lrg_count and countdown to match 6* pattern
                                                                                        # adds to overall count to match pattern
                average_eqnss = "".join(avg)
                print("eqnss:={x(T)=0, x(average)=(" + str(average_eqnss) + ")/" + str(int(keyValue) - 1) + ",")

            avg_fnc2(site_total)

            # use len(site_paths)+1 as current-operating site indicator
            # len(site_paths) is technically the previous site since we have yet to finish building the current one
            site_paths = {1: [2, 2, "T"], 2: [1, 3, 4], 3: [2, 2, 7], 4: [2, 5], 5: [4, 4, 6],
                          6: [5]}                                                       # dictionary with initial triangle elements

            def num_gen2():                                                             # generates dictionary filled with site# (key) and a list of possible site paths (value)

                def actual_cons2(x):                                                    # creates total number of cycles for script to iterate through
                    constant_1 = ((x ** (1 / 2)) // 3) - 1                              # subtract one since number of cycles actual must be accurate
                    return constant_1

                actual_cycle = int(actual_cons2(x))

                def fam_cons2(x):                                                       # creates empty-space predictor constant based off parent traingle
                    constant = x ** (1 / 2) - (3 * actual_cycle)
                    return constant

                group_cons = int(fam_cons2(x))

                # list of initialized value for next
                true_table = []                                                         # created artificial error catcher
                oddity = 4                                                              # oddity value to be put-in
                store = 1                                                               # stores ending site from parent function to use on next iteration
                odditySwtch = 0                                                         # accounts for the pattern switch occuring every 2 cycles that changes oddity location from even to odd sites
                oddity_cntr = 0                                                         # counts total number of oddities
                oddity_total = 3                                                        # tracks totla number of oddities necessary to fulfill given cycle
                cycle_count = 0                                                         # counts number of cycles/iterations that have finished where n=49 is cycle 0 and n=100 is cycle 1
                if keyValue == 25:                                                      # conditionalized to fulfill n=16 triangle
                    site_paths[3] = [2, 2]
                    return site_paths
                if keyValue > 25:                                                       # fulfills all other triangle
                    while cycle_count < actual_cycle:                                   # iterates until generating all site paths necessary

                        def getKeys(site_paths):                                        # returns all keys in the dictionary also known as sites/trap#s
                            return site_paths.keys()

                        keys = getKeys(site_paths)

                        if cycle_count == 0:                                            # artificial elements for mistakes catching
                            for i in site_paths:
                                true_table.append('False: ' + str(i))
                        if cycle_count > 0:
                            for i in range(store, int(len(keys) + 1)):
                                true_table.append('False: ' + str(i))

                        for i in range(store, int(len(keys) + 1)):                      # checks case of 3 total site_paths to make sure all empty spaces are filled
                            if len(site_paths[i]) == 3:
                                true_table[i - 1] = 'True: ' + str(i)
                            elif len(site_paths[i]) == 2:
                                value = i + group_cons                                  # checks case of 2 and 1 site_path(s) filling in Both values dependent on given cases
                                site_paths[i].append(value)
                                true_table[i - 1] = 'True: ' + str(i)
                            elif len(site_paths[i]) == 1:
                                value = i + group_cons
                                site_paths[i].append(value)
                                site_paths[i].append(value)
                                true_table[i - 1] = 'True: ' + str(i)

##here is where the big boy check really occurs, change oddity values
# check out number generation for sites RIGHT BEFORE ending values since it's an oddity===where to put ext4ra oddity switch
                        if cycle_count % 2 == 1 and odditySwtch % 2 == 0:               # conditionalizes oddity values and count for given environment
                            site_paths[len(site_paths) + 1] = [len(site_paths) + 2, len(site_paths) + 2]
                            # GENERATES ENDING VALUE PAIR
                        elif cycle_count % 2 == 0 and odditySwtch % 2 == 0 and cycle_count == 0:
                            oddity = 3
                            site_paths[len(site_paths) + 1] = [oddity, len(site_paths) + 2, len(site_paths) + 2]
                            oddity += 1
# oddity_cntr+=1 line removed
                            oddity_cntr += 1
                        elif cycle_count % 2 == 0 and odditySwtch % 2 == 0:
                            oddity -= 1
                            site_paths[len(site_paths) + 1] = [oddity, len(site_paths) + 2, len(site_paths) + 2]
                            oddity += 2
                            oddity_cntr += 1

                        if cycle_count % 2 == 1 and odditySwtch % 2 == 1:               # conditionalizes oddity values and count for given environment
                            site_paths[len(site_paths) + 1] = [len(site_paths) + 2, len(site_paths) + 2]
                            # GENERATES ENDING VALUE PAIR
                        elif cycle_count % 2 == 0 and odditySwtch % 2 == 1:
                            oddity -= 1
                            site_paths[len(site_paths) + 1] = [oddity, len(site_paths) + 2, len(site_paths) + 2]
                            oddity += 2
                            oddity_cntr += 1

                        store = len(site_paths)                                         # refreshes store value for next cycle
                                                                                        # code to generate new numbers after filling past numbers begins
                        a_gen = 7 + 3 * (
                            cycle_count)                                                # keeps track of a-column number generation (see excel spread: Pattern Search)
                        b_gen = 6 + 3 * (cycle_count)                                   # keeps track of b-column number generation

                        if cycle_count % 2 == 0:                                        # conditionales oddity counter based off current cycle since changes every cycle
                            oddity_cntr = 1                                             # some new cycles begin with oddity (3 paths) while others start without (two path)
                        else:
                            oddity_cntr = 0

                        while a_gen or b_gen > 0:                                       # iterates to generate new values
                            group_cur = []                                              # empty list to change and adapt to new site paths
                            if a_gen and b_gen > 0:
                                a_cur = len(site_paths)
                                b_cur = len(site_paths) + 2
                                group_cur.append(a_cur)
                                group_cur.append(b_cur)
                                fam_num = len(site_paths) + 1
                                if fam_num % 2 == 1 and oddity_cntr < oddity_total and odditySwtch % 2 == 0:
                                                                                        # accounts for empty spaces on x-column and oddity filter based on site(odd/even), total odditities, and current environment
                                    group_cur.append(oddity)
                                    oddity += 2
                                    oddity_cntr += 1
                                    # print(oddity)
                                    # print(oddity_total)
                                    # print(oddity_cntr)
                                elif fam_num % 2 == 1 and oddity_total == oddity_cntr and odditySwtch % 2 == 0:
                                    group_cur.append(a_cur)
                                    # print(oddity)
                                    # print(oddity_total)
                                    # print(oddity_cntr)
                                if fam_num % 2 == 0 and oddity_cntr < oddity_total and odditySwtch % 2 == 1:
                                                                                        # accounts for empty spaces on x-column and oddity filter based on site(odd/even), total odditities, and current environment
                                    group_cur.append(oddity)
                                    oddity += 2
                                    oddity_cntr += 1
                                    # print(oddity)
                                    # print(oddity_total)
                                    # print(oddity_cntr)

                                elif fam_num % 2 == 0 and oddity_total == oddity_cntr and odditySwtch % 2 == 1:
                                    # print(oddity)
                                    # print(oddity_total)
                                    # print(oddity_cntr)
                                    group_cur.append(a_cur)
                                group_cur.sort()
                                site_paths[len(
                                    site_paths) + 1] = group_cur                        # sets new dictionary values with site as key and current site paths as a list value
                                a_gen -= 1
                                b_gen -= 1

                            else:
                                a_cur = len(site_paths)
                                group_cur.append(a_cur)
                                site_paths[len(site_paths) + 1] = group_cur
                                a_gen -= 1
# might need to recheck this oddity change with Theo and vik's values
                        if odditySwtch % 2 == 0 and cycle_count % 2 == 0:               # conditionalizes oddity total necessary based off the current cycle environment
                            # print(str(oddity_total)+':HMM')
                            oddity_total += 1
                        elif odditySwtch % 2 == 0 and cycle_count % 2 == 1:
                            # print(str(oddity_total) + ':WHAT')
                            oddity_total += 2
                        if odditySwtch % 2 == 1 and cycle_count % 2 == 0:
                            # print(str(oddity_total) + ':HOW')
                            oddity_total += 1
                        elif odditySwtch % 2 == 1 and cycle_count % 2 == 1:
                            # print(str(oddity_total) + ':COW')
                            oddity_total += 2

                        group_cons += 3                                                 # refreshes group_cons to adapt to new children (future) iterations
                        cycle_count += 1
                        if cycle_count % 2 == 1:                                        # keeps track of changes in every two cycles so that environment is updated accurately
                            odditySwtch += 1

            num_gen2()

            def eqnss_gen2(site_total):                                                 # generates compilation of equations one by one
                i = 1                                                                   # iterator value to feed yield generator
                                                                                        # change False to i < int(site_total+1) when wanting to use the function
                while i < int(site_total + 1):
                    yield i
                    i += 1

            for i in eqnss_gen2(site_total):                                            # iterates and calls on the function defined above
                length = len(site_paths[i])                                             # defines variable specifier
                if length == 3:                                                         # conditionalizes specific equations to generate one by one
                    value = "x(" + str(i) + ")=(1/3)*((x(" + str(site_paths[i][0]) + ")+1)+(x(" + str(
                        site_paths[i][1]) + ")+1)+(x(" + str(site_paths[i][2]) + ")+1)),"
                    print(value)
                elif length == 2:
                    value = "x(" + str(i) + ")=(1/2)*((x(" + str(site_paths[i][0]) + ")+1)+(x(" + str(
                        site_paths[i][1]) + ")+1)),"
                    print(value)
                elif length == 1:
                    value = "x(" + str(i) + ")=(1)*((x(" + str(site_paths[i][0]) + ")+1))}:\na:=solve(eqnss,b);"
                    print(value)

    vars = var_gen(site_total)                                                      #creates variable for all vars except x(T) and x(average)
                                                                                    #sets all print notes and functions to create correct output final
    print("\n#note that you must personally input the carrots to indicate new blocks\n#each new block in output code is indicated with LARGE gaps\n#code for generating maple inputs for confining symmetric triangles in family one AND two")
    print("\nrestart:\n\n")
    print("with(linalg):\n\n")
    print("b:={x(T), x(average),"+vars+"}:\n\n")
    if ((x**(1/2))) % 3 == 1:
        eqnss_full()
    else:
        eqnss_full2()
    while True:
        answer = input("\n\nRun again? Type (y/n):")
        if answer in ('y', 'n'):
            break
        print("Invalid input.")
    if answer == 'y':
        continue
    else:
        print("\nTHANKS FOR USING!")
        while True:
            input("Please click close to exit")





