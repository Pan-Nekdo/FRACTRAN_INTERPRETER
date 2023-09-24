def NSD(a: int, b: int):#Nejvetsi spolecny delitel za pomoci klasickeho Eukleidova algoritmu
    '''Najde nejvetsi spolecny delitel, a to za pomoci Eukleidova algoritmu'''
    while b != 0:
        a, b = b, a%b
    return a

class FRACTRAN:
    uvodni_zprava = 'FRACTRAN interpreter\nUse the command HELP to learn more.'
    napoveda = '\tFRACTRAN is esoteric language invented by the mathematician John Conway.\n\
\tA FRACTRAN program is an ordered list of positive fractions together with an initial positive integer input n. \
The program is run by updating the integer n as follows:\n\
\t1)\tfor the first fraction f in the list for which nf is an integer, replace n by nf\n\
\t2)\trepeat this rule until no fraction in the list produces an integer when multiplied by n, then halt.\n\
\tTo enter your program here simply type the initial value n followed by the program (the fractions) here separated by spaces. \
Note that the denominators of the fractions must be always present (even when the fraction is whole number\
 - write it as a/1).\n\
\tBecause very often interesting are not only the final values but even the values during the execution this interpreter prints them. \
The number of these numbers during the process is often very high (and sometimes the programs are intentionally \
designed to be infinite - for example the PRIMEGAME by the author J. Conway that produces prime numbers) so \
it would be hard to go through them when all would be printed (almost) at the same time, this interpreter prints \
only limited number of them and then asks whether it should continue. You can change this limit in SETTINGS or even \
choose not to have it at all. You can turn off the printing of the numbers during the process as well.\
\n\n\
\tThis interpreter furthermore has the following commands:\n\
\tHELP\t - to open this help.\n\
\tSETTINGS - to change settings of this interpreter\n\
\tEXIT\t - to leave this interpreter\n\n\
\tFinally this interpreter allows you to save programs and quickly access them using their name. To use them simply \
type the initial value followed by the name of the program. The following commands are used to save new ones, delete old ones \
and see which ones are currently saved (and can be used):\n\
\tSAVE\t - saves a new program (syntax: SAVE _NAME_ _FRACTIONS_)\n\
\tDEL\t - deletes a prorgam (syntax: DEL _NAME_)\n\
\tPROGRAMS - shows all currently saved programs'
    prompt = '-> '

    def __init__(self):
        self.programy = {
        'primegame': '17/91 78/85 19/51 23/38 29/33 77/29 95/23 77/19 1/17 11/13 13/11 15/2 1/7 55/1',
        'fibonaccigame': '17/65 133/34 17/19 23/17 2233/69 23/29 31/23 74/341 31/37 41/31 129/287 41/43 13/41 1/13 1/3'}
        self.tiskni = True #rozhoduje, zda se maji tisknout zlomky v prubehu
        self.interval = 500 # pocet zlomku pred vyzadanim potvrzeni o pokracovani
        self.sep = ' '

        print(self.uvodni_zprava)
        exit = False
        while not exit:
            vstup = input(self.prompt).strip().lower()
            exit = self.zpracuj_vstup(vstup)
    
    def zpracuj_vstup(self, vstup: str) -> bool: #Vysledny boolean urcuje, zda neslo o prikaz EXIT.
        vstup_cut = vstup.split()
        if len(vstup_cut) == 0: return False

        if vstup_cut[0] == 'help':
            print(self.napoveda)
        elif vstup_cut[0] == 'settings':
            self.nastaveni()
        elif vstup_cut[0] == 'exit':
            return True
        elif vstup_cut[0] == 'save':
            if len(vstup_cut) < 3:
                self.chyba()
                return False
            if vstup_cut[1] in self.programy:
                print('\tProgram with this name already exists. If you want to assing a new \
program to this name delete the old one using the command DEL.')
                return False
            for zlomek_t in vstup_cut[2:]:
                try:
                    c_t, j_t = zlomek_t.split(sep='/')
                except ValueError:
                    print('\tThe program you are trying to save is not valid.')
                    return False
                if c_t.isnumeric() and j_t.isnumeric():
                    if int(j_t) == 0:
                        print('\tThe program you are trying to save is not valid (denominator can\'t be 0).')
                    continue
                else:
                    print('\tThe program you are trying to save is not valid.')
                    return False
            self.programy[vstup_cut[1]] = ' '.join(vstup_cut[2:])
        elif vstup_cut[0] == 'del':
            if len(vstup_cut) == 1:
                self.chyba()
                return False
            if vstup_cut[1] in self.programy: del self.programy[vstup_cut[1]]
            else: print('\tProgram with this name did not exist.')
        elif vstup_cut[0] == 'programs':
            for name in self.programy:
                print(f'\t{name}:\t{self.programy[name]}')
        else:
            self.interpretuj(vstup)
        return False
    
    def chyba(self): #Chybova hlaska
        print('\tThis input is in wrong format. Type HELP to learn what is allowed.')
    
    def interpretuj(self, kod: str):
        try:
            if kod.split()[1].isalpha():
                if kod.split()[1] in self.programy:
                    kod = kod.split()[0] + ' ' + self.programy[kod.split()[1]]
                    print('Executing: ' + kod + '\n')
                else:
                    self.chyba()
                    return
            N_t, *zlomky_t = kod.split()
            N = int(N_t)
            zlomky = []
            for zlomek_t in zlomky_t:
                c_t, j_t = zlomek_t.split(sep='/')
                c, j = int(c_t), int(j_t)
                if j == 0:
                    print('\tThe denominator of a fraction can\'t be 0.')
                    return
                d = NSD(c,j)
                c, j = c//d, j//d
                zlomky.append((c, j))
            
            if self.interval == 0:
                while True:
                    if self.tiskni: print(N, end=self.sep)
                    for zlomek in zlomky:
                        if NSD(zlomek[1], N) == zlomek[1]:
                            N = zlomek[0]*N//zlomek[1]
                            break
                    else:
                        if self.tiskni: print()
                        print(N)
                        break
            else:
                opust = False
                while True:
                    for _ in range(self.interval):
                        if self.tiskni: print(N, end=self.sep)
                        for zlomek in zlomky:
                            if NSD(zlomek[1], N) == zlomek[1]:
                                N = zlomek[0]*N//zlomek[1]
                                break
                        else:
                            if self.tiskni: print()
                            print(N)
                            opust = True
                            break
                    if opust: break
                    else:
                        print()
                        vstup = input(f'\tThe number of steps exceeded the limit. Do you want to continue? (Y/N) \
(The current limit is {self.interval}. You can change it in settings.) ')
                        if vstup == 'Y' or vstup == 'y':
                            pass
                        else: break
        except (ValueError, IndexError):
            self.chyba()

    def nastaveni(self):
        print('\tUse the following commands:\n\tPROMPT "new_prompt"\
\n\t*The prompt string will be changed to new_prompt\n\t\
INTERVAL n\n\t*To change the number of numbers computed and printed (if turned on) before it will be required to continue computation. To turn off the confirmation use 0\
 (note that this can lead to infinite loops).\n\t\
PRINT ON/PRINT OFF\n\t*to turn on/off the printing of numbers during the computation.\n\t\
SEP "separator"\n\t*To change the string that separates printed numbers during computation. Use /n to print every number on a new line.\
\n\tCURRENT\n\t*shows the current and default settings.\n\n\tPress enter (without any input) to leave settings.')
        while (vstup:=input('SETTINGS: ').strip()) != '':
            vstup_raw = vstup
            vstup = vstup.lower()
            vstup_cut = vstup.split()
            if vstup_cut[0] == 'current':
                print(f'\tPROMPT:\t "{self.prompt}" (default "-> ")\n\t\
INTERVAL:{self.interval} (default 500)\n\tPRINT:\t {"ON" if self.tiskni else "OFF"} (default ON)\n\t\
SEP:\t "{self.sep}" (default " ")')
            elif vstup_cut[0] == 'prompt':
                v = vstup_raw[6:].strip()
                if len(v) < 2:
                    print('The prompt string must be inside quotation marks.')
                    continue
                if v[0] != '"' or v[-1] != '"':
                    print('The prompt string must be inside quotation marks.')
                else:
                    self.prompt = v[1:-1]
            elif vstup_cut[0] == 'interval':
                try:
                    self.interval = int(''.join(vstup_cut[1:]))
                except ValueError:
                    print('\tThe interval must be number.')
            elif vstup_cut[0] == 'print':
                if len(vstup_cut) != 2:
                    print('\tWrong input.')
                elif vstup_cut[1] == 'on':
                    self.tiskni = True
                elif vstup_cut[1] == 'off':
                    self.tiskni = False
                else:
                    print('\tWrong input.')
            elif vstup_cut[0] == 'sep':
                v = vstup_raw[3:].strip()
                if len(v) < 2:
                    print('\tThe separation string must be inside quotation marks.')
                    continue
                if v[0] != '"' or v[-1] != '"':
                    print('\tThe prompt string must be inside quotation marks.')
                else:
                    self.sep = v.replace('/n', '\n')[1:-1]
            else:
                print('\tWrong input.')




def main():
    FRACTRAN()

if __name__ == '__main__':
    main()