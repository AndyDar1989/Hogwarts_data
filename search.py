def person_search(data_file, name):
    with open (data_file, 'r', encoding='utf_8') as data:
        data_list = data.readlines()
        length = len(data_list)
        for i in range(1, length):
            if name in data_list[i]:
                print (data_list[i])
                break
        else: 
            print('data not found')    
            
        
        
person_search('Hogwarts.csv', 'зоолог')        
        