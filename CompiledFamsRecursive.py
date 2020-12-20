# adaptation of compiled fams resolved into a class format with recursive functions

# code for total number of sites
sites_total = int(input("What are the total number of sites?"))

class SiteNumber:
    def __init__(self, sites):
        self.sites = sites

    def site_count(self):
        if self.sites ** (1 / 2) % 3 == 1:
            counter = 0
            variable_counter = 4
            triangle_num = (self.sites ** (1 / 2) - 4) / 3
            cumulative_counter = 4
            while counter < triangle_num:
                variable_counter += 3
                cumulative_counter += variable_counter
                counter += 1
            return cumulative_counter

        else:
            counter = 0
            variable_counter = 5
            triangle_num = (self.sites ** (1 / 2) - 5) / 3
            cumulative_counter = 6
            while counter < triangle_num:
                variable_counter += 3
                cumulative_counter += variable_counter
                counter += 1
            return cumulative_counter

#created object
triangle_1 = SiteNumber(sites_total)
true_sites = triangle_1.site_count()

# TESTING CODE
#print(true_sites)

# code for average and variable equations for input
traps = []
def var_gen(site_total):
    # generates list of vars to be used in the maple input
    counter = 1
    for i in range(1, int(site_total) + 1):
        if i == 1:
            value = "x(" + str(counter) + ")"
            traps.append(value)
            counter += 1
        else:
            value = " x(" + str(counter) + ")"
            traps.append(value)
            counter += 1
    return str(",".join(traps))
site_list = var_gen(true_sites)


# TESTING CODE
#print(site_list)


class AverageEqnss:

    LRG_COUNT = 4
    SML_COUNTDOWN = 3
    FF_SML= 3
    FF_LRG = 6
    VAR_ITER = 3
    CURRENT_FAM = 3

    AVG = ["3*x(" + str(1) + ")+", "6*x(" + str(2) + ")+"]

    def __init__(self, totalvars):
        self.totalvars = totalvars

    def avg_gen(self):
        while self.CURRENT_FAM < self.totalvars:
            while self.SML_COUNTDOWN > 0 and self.CURRENT_FAM <= self.totalvars:
                if self.CURRENT_FAM < self.totalvars:
                    piece = str(self.FF_SML) + "*x(" + str(self.VAR_ITER) + ")+"
                    self.AVG.append(piece)
                    self.VAR_ITER += 1
                    self.SML_COUNTDOWN -= 1
                    self.CURRENT_FAM += 1
                elif self.CURRENT_FAM == self.totalvars:  # only goes through last site to remove extra + sign
                    piece = str(self.FF_SML) + "*x(" + str(self.VAR_ITER) + ")"
                    self.AVG.append(piece)
                    self.VAR_ITER += 1
                    self.SML_COUNTDOWN -= 1
                    self.CURRENT_FAM += 1
            self.SML_COUNTDOWN += 3

            lrg_countdown = self.LRG_COUNT  # refreshes count to match lrg fractal pattern
            while lrg_countdown > 0 and self.CURRENT_FAM <= self.totalvars:  # loops through to add large fractals with 6* pattern beginning
                if self.CURRENT_FAM < self.totalvars:  # goes through all large sites except last one, conditionalized for both pattern status and site total
                    piece = str(self.FF_LRG) + "*x(" + str(self.VAR_ITER) + ")+"
                    self.AVG.append(piece)
                    self.VAR_ITER += 1
                    lrg_countdown -= 1
                    self.CURRENT_FAM += 1
                elif self.CURRENT_FAM == self.totalvars:  # only goes through last site to get rid of extra + sign
                    piece = str(self.FF_LRG) + "*x(" + str(self.VAR_ITER) + ")"
                    self.AVG.append(piece)
                    self.VAR_ITER += 1
                    lrg_countdown -= 1
                    self.CURRENT_FAM += 1
            self.LRG_COUNT += 3  # change lrg_count and countdown to match 6* pattern
        return ("".join(self.AVG))

    def combine(self):
        print("eqnss:={x(T)=0, x(average)=("+str(self.avg_gen())+")/"+str(int(sites_total)-1)+",")

#created object
avgeqnss1 = AverageEqnss(true_sites)
avgeqnss1.combine()

class ColumnsInitializer:

    def __init__(self, sitestot, truesites):
        self.sitestot = sitestot
        self.truesites = truesites


the_initial = ColumnsInitializer(sites_total, true_sites)
#OBJECT VALUES
#print(int(the_initial.actual_cons()))


class Column1(ColumnsInitializer):
#odditymaxgenvars
    family_value = 7
    oddity_counter = 0
#odditygenvars
    oddityreg = 2
    oddityodd = 1
    oddity_comp = 3
    oddity_ender = 2
    oddity_entity= 7
    cycle_tracker = 0
    column_tracker1 = []
#Shared function vars
    oddity_value = 2
    oddity_max = 2


    def odditymaxgen(self):
        if self.oddity_counter == (int(sites_total**(1/2)//3) - 1):                          #MIGHT NEED TO CHECK MATH LOGIC ON THIS
            self.oddity_counter = 1
            return self.oddity_max
        else:
            self.oddity_max += self.family_value
            self.family_value += 3
            self.oddity_counter += 1
            self.odditymaxgen()

    def odditygen(self):
        if self.oddity_ender == self.oddity_max:
            return self.column_tracker1
        else:
            for i in range(0, self.oddity_comp):
                if self.oddity_ender == self.oddity_max:
                    break
                if self.oddity_counter < self.oddity_comp:
                    self.column_tracker1.append(self.oddity_value)
                    self.oddity_counter += 1
                    self.oddity_value += self.oddityreg
                else:
                    self.oddity_ender += self.oddity_entity
                    self.column_tracker1.append(self.oddity_ender)
                    self.oddity_entity += 3
                    self.cycle_tracker += 1
                    if self.cycle_tracker % 2 == 0:
                        self.oddity_comp += self.oddityodd
                        self.oddity_counter = 1
                    else:
                        self.oddity_value -= self.oddityodd
                        self.oddity_comp += self.oddityreg
                        self.oddity_counter = 1
            self.odditygen()

#OBJECT VALUES
the_first = Column1(sites_total, true_sites)
the_first.odditymaxgen()
the_first.odditygen()
print(the_first.column_tracker1)


class Column2(ColumnsInitializer):
    column_tracker2 = []
    gen_counter = true_sites
    gen_variable = int(sites_total**(1/2)) + 1
    def generation(self):
        if self.gen_counter == 4:
            return self.column_tracker2
        else:
            for i in range(1,self.gen_variable):
                if i == int(self.gen_variable - 1):
                    self.gen_counter += 1
                    #print(self.gen_counter)
                    self.column_tracker2.insert(0,self.gen_counter)
                    self.gen_counter -= 2
                else:
                    self.gen_counter -= 1
                    #print(self.gen_counter)
                    self.column_tracker2.insert(0, self.gen_counter)
            self.gen_variable -= 3
            self.generation()

#OBJECT VALUES
the_second = Column2(sites_total, true_sites)
the_second.generation()
print(the_second.column_tracker2)


class Column3(ColumnsInitializer):
    column_tracker3 = []
    gen_counter = true_sites
    gen_variable = int(sites_total ** (1 / 2)) + 1
    family_constant1 = 4 + 3 * int(((sites_total ** (1 / 2) // 3) - 2))
    family_constant2 = 3 + 3 * int(((sites_total ** (1 / 2) // 3) - 2))

    def generation(self):
        if self.gen_counter == 4:
            return self.column_tracker3
        else:
            for i in range(1, int(self.gen_variable)):
                if i == int(self.gen_variable - 1):
                    self.gen_counter += self.family_constant2
                    self.column_tracker3.insert(0, self.gen_counter)
                    self.gen_counter -= self.family_constant1
                    self.family_constant1 -= 3
                    self.family_constant2 -= 3
                else:
                    self.column_tracker3.insert(0, self.gen_counter)
                    self.gen_counter -= 1
            self.gen_variable -= 3
            self.generation()

#OBJECT VALUES
the_third = Column3(sites_total, true_sites)
the_third.generation()
print(the_third.column_tracker3)


class Column4(ColumnsInitializer):
#odditymaxgenvars
    family_value = 0
    site_number = 0
#odditygenvars
    column_tracker4 = []
    ODDITYREG = 2
    ODDITYODD = 1
    oddity_comp = 1
    oddity_ender = 2
    cycle_tracker = 0
    oddity_counter = 0
    site_num = 0
    family_constant3 = 0
#Shared function vars
    oddity_value = 6
    oddity_max = 2


    def odditymaxgen(self):
        for i in range(0, int((sites_total**(1/2)//3) - 1)):
            self.site_number += self.family_value
            if self.family_value == 0:
                self.family_value += 7
            else:
                self.family_value += 3
        self.oddity_max = the_third.column_tracker3[int(self.site_number)]


    def odditygen(self):
        if self.oddity_ender == self.oddity_max:
            return self.column_tracker4
        else:
            for i in range(0, self.oddity_comp):
                if self.oddity_ender == self.oddity_max:
                    break
                if self.oddity_counter < self.oddity_comp:
                    self.column_tracker4.append(self.oddity_value)
                    self.oddity_counter += 1
                    self.oddity_value += self.ODDITYREG
                else:
                    self.site_num += self.family_constant3
                    if self.family_constant3 == 0:
                        self.family_constant3 += 7
                    else:
                        self.family_constant3 += 3
                    self.oddity_ender = the_third.column_tracker3[int(self.site_num)]
                    self.column_tracker4.append(self.oddity_ender)
                    self.cycle_tracker += 1
                    if self.cycle_tracker % 2 == 0:
                        self.oddity_comp += self.ODDITYODD
                        self.oddity_counter = 0
                        self.oddity_value += 5
                    else:
                        self.oddity_value += 4
                        self.oddity_comp += self.ODDITYREG
                        self.oddity_counter = 0
            self.odditygen()

#OBJECT VALUES
the_fourth = Column4(sites_total, true_sites)
the_fourth.odditymaxgen()
the_fourth.odditygen()
print(the_fourth.column_tracker4)


#class NumsFullSelector(ColumnsInitializer):
    #pass
