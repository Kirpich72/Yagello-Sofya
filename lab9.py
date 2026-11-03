#variant 22
#task1. 7 level
def outed(meet, boss):
    if (sum(meet.values())+meet[boss])/(len(meet)) <= 5:
        return 'Get Out Now!'
    else:
        return 'Nice Work Champ!'
        
#task2. 6 level
def wave(people):
    spisok = []
    for i in range(len(people)):
        if people[i] == " ":
            continue
        else:  
            spisok.append(people[:i] + people[i].upper() + people[i+1:])
    return spisok
    
#task3. 5 level
def make_readable(seconds):
    return(f'{(seconds//3600):02d}:{(seconds%3600//60):02d}:{(seconds%60):02d}')
