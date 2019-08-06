def progressBarprint(signstr,pos,rightstr = ' ',leftstr = ' ',lengh = 100,showPercentage = False):
    if (showPercentage == False):
        print('\r|',leftstr*(pos-1),signstr,rightstr*(lengh-pos),'|',end = ' ')
        if (pos == 100):
            print('complete')
    else:
        print('\r|',leftstr*(pos-1),signstr,rightstr*(lengh-pos),'|',str(pos)+'%',end = ' ')
        if (pos == 100):
            print('complete')
    return