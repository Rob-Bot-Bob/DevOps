f = open('/mnt/c/Users/Yenny/Documents/DevOps/DevOps/Ex_Files_Python_Automation/Exercise Files/inputFile.txt','r')
passFile = open('/mnt/c/Users/Yenny/Documents/DevOps/DevOps/Ex_Files_Python_Automation/Exercise Files/passFile.txt','w')
failFile = open('/mnt/c/Users/Yenny/Documents/DevOps/DevOps/Ex_Files_Python_Automation/Exercise Files/failFile.txt','w')

count = 0 
for line in f:
    line_split = line.split() #line.split() separa los strings de acuerdo al parametro que pases si lo pasas vacio los separa por coma cada vez que encuentre un espacio o tambien por caracter que queiras quitar  en este caso los separa por comas
    if line_split[2] == 'P': #aqui verifica en la lista en la pocion 2 si es F o P y los imprime de acuerdo a cual es
        passFile.write(line)
    else:
        failFile.write(line)
f.close()
passFile.close()
failFile.close()
