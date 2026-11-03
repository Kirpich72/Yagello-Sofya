#task1
def outed(meet, boss):
    s = 0
    n = 0
    for i, j in meet.items():
        s += j
        n += 1
    srznach = s/n
    if srznach <= 5:
        return 'Get Out Now!'
    else:
        return 'Nice Work Champ!'
#task2

#task3
def make_readable(seconds):
    return(f'{(seconds//3600):02d}:{(seconds%3600//60):02d}:{(seconds%60):02d}')
