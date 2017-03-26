'''
Created on Mar 15, 2017

@author: Utilizator
'''

class Console(object):
    '''
    classdocs
    '''


    def __init__(self, controller):
        '''
        Constructor
        '''
        self.__controller=controller
        self.__theWord=None
        self.__score=1
        
    def returnRandom(self):
        r= self.__controller.returnRandom()
        return r
    
    def readCommand(self):
        cmd = input("Your option is:")
        try:
            cmd=int(cmd)
        except Exception:
            raise Exception("Invalid input! Please type in again!")
        return cmd
    
    def validateCommand(self,cmd):
        if cmd<0 or cmd>1:
            raise Exception("Invalid option! Please type in again!")  
        
    def printMenu1(self):
        print("1. Start new game")        
        print("0. Exit")
        
    def printMenu2(self):
        print("1. Swap <word1><letter1>-<word2><letter2>")
        print("2. Undo") 
        print("0. Exit")
    def swap(self,word,cmd):
        cmd=cmd.split(" ")
        cmd=cmd[1]
        cmd.split("-")
        #print(cmd)
        try:
            word1=int(cmd[0])
            letter1=int(cmd[1])
            word2=int(cmd[3])
            letter2=int(cmd[4])    
        except IndexError:
            raise Exception("Command is not complete!")
        
        scrambledWord=self.__controller.swap(word,word1,letter1,word2,letter2)
        return scrambledWord
    def won(self,string1,string2):
        if string1==string2:
            return True
        return False
    def lose(self,score):
        if score==0:
            return True
        return False
    def undo(self,scrambled):
        scrambled=self.__controller.undo(scrambled)
        print(scrambled)
    def play(self):
        stop=False
        while True and not stop:
            self.printMenu1()
            cmd = self.readCommand()
            try:
                self.validateCommand(cmd)
            except Exception as ex:
                            print(ex)
            if cmd ==0:
                print("Bye! Thank you for using the app!")
                break                
            elif cmd == 1:  
                won = True
                r=self.returnRandom()   
                self.__theWord=r.get_string()      
                         
                self.__score=self.__controller.getScore(r)
                r=self.__controller.scramble(r)
                print("The scrambled word or sentence is:",r)
                print("Initial score:",self.__score)
                scrambled=r
                while True:                      
                    self.printMenu2()
                    cmd=self.readCommand()
                    if cmd == 0:
                        stop=True
                        print("Bye! Thank you for using the app!")
                        break
                    elif cmd==1:
                        try:
                            cmd=input()
                            scrambled=self.swap(scrambled,cmd)
                            print("The scrambled word or sentence is:",scrambled)
                            if self.won(scrambled,self.__theWord):
                                print("You won!")
                                stop=True
                                break                            
                            else:
                                self.__score-=1
                                if self.lose(self.__score):
                                    print("You lose!")
                                    stop=True
                                    break
                                print("Your score is:",self.__score)
                        except Exception as ex:
                            print(ex)
                    
                    elif cmd==2:
                        try:
                            scrambled=self.undo(scrambled)
                        except Exception as ex:
                            print(ex)
    
            
        