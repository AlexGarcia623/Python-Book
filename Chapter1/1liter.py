file = '/Users/alexgarcia/Documents/GitHub/Python-Book/Chapter1/files/densities.dat'

file = open(file,'r')
contents = file.read()

lines = contents.split('\n')

names = []
dens  = []
for index in range(len(lines)):
    current_line_list = lines[index].split(' ')

    not_dens = current_line_list[:-1]
    name = ''
    for n in not_dens:
        if (len(n) > 0):
            if (len(name) > 0):
                name += ' ' +  n
            else:
                name += n

    names.append( name )
    dens.append( float(current_line_list[-1]) )

dic = { names[i]:dens[i] for i in range(len(names)) }

print('iron'      , dic['iron']      )
print('air'       , dic['air']       )
print('gasoline'  , dic['gasoline']  )
print('ice'       , dic['ice']       )
print('human body', dic['human body'])
print('silver'    , dic['silver']    )
print('platinium' , dic['platinium'] )