import cv2   
print( cv2.__version__ )
import matplotlib.pyplot as plt
import numpy as np
import os

directory = 'd6\D'
directory2 = 'BaseD6\Teste'
directory4 = 'Testes2\Teste'
acertos=0
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
while i<(1484): 
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
       

                    

print(len(leitura))
print(leitura)