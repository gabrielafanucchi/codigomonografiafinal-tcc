import cv2   
print( cv2.__version__ )
import matplotlib.pyplot as plt
import numpy as np
import os

directory = 'd6\D'
directory2 = 'Testes1\Teste-'
directory4 = 'Testes2\Teste'
acertos=0
resultados2 = [2,2,5,1,3,2,3,3,6,4,1,3,6,4,1,3,6,4,
3,6,4,1,2,2,5,3,2,4,6,2,1,5,6,2,1,5,4,2,3,5,4,2,3,
5,4,2,3,5,3,2,4,5,3,1,6,6,3,5,6,4,1,5,6,3,1,4,6,5,
1,2,6,3,3,3,3,1,4,1,5,4,5,1,5,6,5,1,4,5,1,2,4,5,3,
6,2,6,4,1,5,6]
resultados = [5,1,3,2,6,3,1,3,2,4,6,3,5,2,3,4,6,5,
3,4,2,4,6,2,5,3,6,5,4,2,3,2,6,5,4,2,1,2,4,5,6,3,2,
1,4,6,3,5,3,1,5,3,1,5,1,4,5,4,1,5,1,5,6,3,1,5,2,1,
2,1,3,1,5,1,6,2,1,2,4,2,1,4,1,5,4,1,5,1,4,5,2,6,5,
2,6,2,4,5,4,6]
leitura =[]
erro =[]

def read (dir1,dir2):
    img = cv2.imread(dir1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(dir2, cv2.IMREAD_GRAYSCALE)

    sift = cv2.SIFT_create(5000)

    keypoints, des1 = sift.detectAndCompute(img, None)
    keypoints2, des2 = sift.detectAndCompute(img2, None)




    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1,des2, k=2)

    

    good = []
    for m,n in matches:
        if m.distance < 0.75*n.distance:
            good.append([m])
    #img3 = cv2.drawMatchesKnn(img,keypoints,img2,keypoints2,
            #good[:20],None,flags=2)
    #cv2.imshow("Image", img3)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    return(len(good))

#print(resultados[0])

#read('Testes1\Teste-1.jpeg','d6\D4.jpeg')

ret = 0
max = ""
i=1
while i<(101): 
    fil= directory2 + str(i) + ".jpeg"
    
    ret = 0
    max = ""
    print(fil)
    j=1
    while j<=6:
        directory3=directory+str(j)
        for filename in os.listdir(directory3):
            #print(filename)
            f = os.path.join(directory3, filename)
            
            if os.path.isfile(f):
                #print(f)
                r = read(f,fil)    
                #print(r)
                if r>ret:
                    ret = r
                    max = f[4]
        j+=1
    i+=1
    
    if ret != 0:
        #print(max)
        #print(resultados[i-2])
        leitura.append(int(max))
        
        if str(resultados[i-2]) == max:
            print("entrou")
            acertos=acertos+1
        else: 
            erro.append(i-1)
i=1
while i<(101): 
    fil= directory4 + str(i) + ".jpeg"
    
    ret = 0
    max = ""
    print(fil)
    j=1
    while j<=6:
        directory3=directory+str(j)
        for filename in os.listdir(directory3):
            #print(filename)
            f = os.path.join(directory3, filename)
            if os.path.isfile(f):
                #print(f)
                r = read(f,fil)    
                #print(r)
                if r>ret:
                    ret = r
                    max = f[4]
        j+=1
    i+=1
    
    if ret != 0:
        #print(max)
        #print(resultados[i-2])
        leitura.append(int(max))
        
        if str(resultados2[i-2]) == max:
            print("entrou")
            acertos=acertos+1
        else: 
            erro.append(i-1)
                    
print(acertos)
print(int(len(resultados))+int(len((resultados2))))
precisao=acertos/(int(len(resultados))+int(len(resultados2)))
print(precisao)
print(erro)
print(leitura)
