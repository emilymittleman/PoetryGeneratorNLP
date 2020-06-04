'''
    post processing
'''

def clean_up(poem=''):
    ''' Cleans the poem into a readable format '''
    #poem = poem.split(",")
    poem = ""
    uglyPoem = [(6, 'they'), (6, ' '), (6, 'wanted'), (6, ' '), (6, 'to'), (5, '\n'), (5, '~'), (5, 'and'), (5, ' '), (5, 'we'), (5, ' '), (5, 'had'), (5, ' '), (5, 'a'), (5, ' '), (5, 'little'), (5, ' '), (5, 'drum'), (5, ' '), (5, 'and'), (5, ' '), (4, '\n'), (4, '~'), (4, 'and'), (4, ' '), (4, 'we'), (4, ' '), (4, 'had'), (4, ' '), (4, 'a'), (4, ' '), (4, 'little'), (4, ' '), (4, 'drum'), (4, ' '), (4, 'and'), (3, '\n'), (3, '~'), (3, 'and'), (3, ' '), (3, 'we'), (3, ' '), (3, 'had'), (3, ' '), (3, 'a'), (3, ' '), (3, 'little'), (3, ' '), (3, 'drum'), (3, ' '), (3, 'and'), (3, ' '), (3, 'we'), (3, ' '), (3, 'had'), (3, ' '), (3, 'a'), (3, ' '), (3, 'little'), (3, ' '), (3, 'drum'), (2, '\n'), (2, '~'), (2, 'and'), (2, ' '), (2, 'we'), (2, ' '), (2, 'had'), (2, ' '), (2, 'a'), (2, ' '), (2, 'little'), (2, ' '), (2, 'drum'), (2, ' '), (2, 'and'), (2, ' '), (2, 'we'), (2, ' '), (2, 'had'), (2, ' '), (2, 'some'), (2, ' '), (2, 'drum'), (2, ' '), (2, 'and'), (2, ' '), (2, 'we'), (2, ' '), (2, 'had'), (2, ' '), (2, 'some'), (2, ' '), (2, 'frown'), (2, ' '), (2, 'and'), (2, ' '), (2, 'we'), (2, ' '), (2, 'had'), (2, ' '), (2, 'some'), (2, ' '), (2, 'frown'), (2, ' '), (2, 'and'), (2, ' '), (2, 'we'), (2, ' '), (2, 'had'), (2, ' '), (2, 'some'), (2, ' '), (2, 'frown'), (2, ' '), (2, 'and'), (2, ' '), (2, 'we'), (2, ' '), (2, 'had'), (2, ' '), (2, 'some'), (2, ' '), (2, 'frown'), (2, ' '), (2, 'and'), (2, ' '), (2, 'we'), (2, ' '), (2, 'had'), (2, ' '), (2, 'some'), (2, ' '), (2, 'frown'), (2, ' '), (2, 'and'), (2, ' '), (2, 'we'), (2, ' '), (2, 'had'), (2, ' '), (2, 'some'), (2, ' '), (2, 'frown'), (2, ' '), (2, 'and'), (2, ' '), (2, 'we'), (2, ' '), (2, 'had'), (2, ' '), (2, 'some'), (2, ' '), (2, 'frown'), (2, ' '), (2, 'and'), (2, ' '), (2, 'we'), (2, ' '), (2, 'had'), (2, ' '), (2, 'some'), (2, ' '), (2, 'frown'), (2, ' '), (2, 'and'), (2, ' ')]
    
    capitalize = False
    for pair in uglyPoem:
        word = pair[1]
        # item is either a word, punctuation, or ~ (which is the only case you have to process)
        if word == '~':
            #capitalize the NEXT word, so set capitalize to True
            capitalize = True
            continue
        else:
            # test if you have to capitalize the word or leave it
            if capitalize:
                word = word.capitalize()
                capitalize = False
            poem += word

    return poem

    

def main():
    '''
    uglyPoem = input("(q to quit)\nEnter the formatted poem which is a list of tuples: ")
    while(uglyPoem != "q"):
        poem = clean_up(uglyPoem)
    '''
    poem = clean_up()
    print(poem)

if __name__ == "__main__":
    main()


