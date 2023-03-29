


class game:
    def __init__(self):
        while True:
            print('''Welcome to our game
        1 : sentence No Duplicate
        2 : Name list count
        3 : divided By
        4 : to Exit
            ''')

            user_choise = int (input('Enter game number :'))
            if user_choise == 1:
                sentence = input('Enter sentence :')
                self.no_duplicate(sentence)
            elif user_choise == 2:
                names = eval (input('Enter names :'))
                self.names_count(names)
            elif user_choise == 3:
                first_number = int(input ('Enter number :'))
                secound_number = int(input ('Enter number :'))
                self.divided_by(first_number,secound_number)
            elif user_choise == 4:
                print ('Good bay...')
                return
            else :
                print ('Enter correct number !!')
            play_agin = input('Press any key to play agin , n for exit !')
            if play_agin == 'n':
                print ('God bay !')
                break
            

    def no_duplicate(self ,sentence):
        words = sentence.split(' ')
        new_words = []
        for w in words:
            if w in new_words:
                continue
            else:
                new_words.append(w)
        new_sentence = ' '.join(new_words)
        print(new_sentence)


    def names_count(self,names):
        count = []
        for n in names:
            count.append(len(n))
        print (count)

    def divided_by( self ,x,y):
        result = []
        for n in range(1,101):
            if n%x == 0 and n%y == 0:
                result.append(n)
        print (result)
g1 = game()


