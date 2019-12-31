from random import randint
import random
from math import * 
import matplotlib.pyplot as plt
from copy import copy

class Point:

	def __init__(self,x,y):
		self.point=(x,y)

	def getX(self):
		return self.point[0]

	def getY(self):
		return self.point[1]

	def getXY(self):
		return self.point

	def __str__(self):
		tmp="(x,y):({},{})".format(self.getX(),self.getY())
		return tmp

	def __eq__(self,others):
		if self.getX()==others.getX() and self.getY()==others.getY():
			return True
		else:
			return False

class Cluster:

	def __init__(self):
		self.listePoint=[]
		self.Calculecentre()

	def getliste(self):
		return self.listePoint

	def getCentre(self):
		return self.centre

	def append(self,p):
		self.listePoint.append(p)
		self.Calculecentre()

	def __str__(self):
		tmp0=""
		for i in self.getliste():
			tmp0+=str(i.getXY())+" "
		tmp="la liste est : {}\nle Centre {}".format(tmp0,self.getCentre())
		return tmp

	def Calculecentre(self):
		x=0
		y=0
		for i in self.listePoint:
			x+=i.getX()

		for j in self.listePoint:
			y+=j.getY()

		if len(self.listePoint)!=0:
			x=x/len(self.listePoint)
			y=y/len(self.listePoint)
			self.centre=Point(x,y)
		else:
			self.centre=Point(0,0)


class Partie:

	def __init__(self,nbrCluster,nbrPoint):
		self.creeListePoint(nbrPoint)
		self.creeLesClusters(nbrCluster)

	def creeListePoint(self,nbrPoint):
		self.listeDesPoints=[]
		li1=random.sample(range(100),nbrPoint)
		li2=copy(li1)
		random.shuffle(li2)
		print("1er",li1)
		print("2er",li2)
		for i in range(nbrPoint):
			"""
			x1=randint(0,5)
			y1=randint(0,5)
			x=randint(8,10)
			y=randint(8,10)
			"""
			
			self.listeDesPoints.append(Point(li1[i],li2[i]))
			#self.listeDesPoints.append(Point(x1,y1))
	def nettoyage(self):
		n=1
		for i in self.getLesPoints():
			for j in self.getLesPoints()[n:len(self.getLesPoints())]:
				if i==j:
					print(i)
					print(j)
					self.getLesPoints().remove(i)
				n+=1

	def creeLesClusters(self,nbrCluster):
		self.listeDesClusters=[]
		for i in range(nbrCluster):
			x=Cluster()
			self.listeDesClusters.append(x)

	def initClusters(self):
		for i in self.listeDesPoints:
			self.getLesClusters()[0].append(i)


	def getLesPoints(self):
		return self.listeDesPoints

	def getLesClusters(self):
		return self.listeDesClusters

	def distanceEucl(self,g,p):
		x=sqrt(   (g.getX()-p.getX())**2  + (g.getY()-p.getY())**2  )
		return x

	def test(self):
		d=self.distanceEucl(self.getLesClusters()[0].getCentre(),self.getLesClusters()[0].getliste()[0])
		return d

	def run(self):
		print(self.__str__())
		c=True
		while c==True:
			for i in self.getLesClusters():
				
				c=False
				#print("c:",i.getCentre())
				c1=True
				while c1==True:
					
					c1=False
					for k in i.getliste():
						x=float('inf')
						ind=0
						for j in self.getLesClusters():
							print(self.getLesClusters().index(j))
							d=self.distanceEucl(k,j.getCentre())
							if d<x:
								x=d
								indice=ind
							ind+=1
						print(k.getXY()," go to ", indice)
						#print("hna",type(self.getLesClusters()[indice]))
						if x!=float('inf') and k not in self.getLesClusters()[indice].getliste() :
							#print("incie",indice)

							self.getLesClusters()[indice].append(k)
							self.getLesClusters()[indice].Calculecentre()
							i.getliste().remove(k)
							i.Calculecentre()
							print(self.__str__())
							c=True
							c1=True
	def afficher(self):
		lix=[]
		liy=[]
		lix1=[]
		liy1=[]
		ind=1
		li=["x","o","*","+","s","_","|"]
		plt.subplot(2,1,1)
		for j in self.getLesClusters():
			for i in j.getliste():
				lix1.append(i.getX())
				liy1.append(i.getY())

		plt.scatter(lix1,liy1,s=15,c="#000000")
		plt.title("** Agrandir ou réduire la fenêtre pour mieux visualiser **\n\nFigure avant clustering")

		plt.subplot(2,1,2)
		for j in self.getLesClusters():
			for i in j.getliste():
				lix.append(i.getX())
				liy.append(i.getY())
			#plt.subplot(2,1,1)
			if lix!=[] and liy!=[]:
				x=randint(100000,999999)
				x="#"+str(x)+""
				y="Cluster "+str(ind)
				ind+=1
				plt.scatter(lix,liy,  c=x,s=50, label=y,marker=li[0])
				li.remove(li[0])
			lix=[]
			liy=[]
		
		plt.legend(bbox_to_anchor=(1.12, 1.05))
		plt.title("Figure après clustering")
		plt.show()


				 

				

	def __str__(self):
		kk=1
		tmp0=""
		for i in self.getLesPoints():
			tmp0+=str(i.getXY())+" "
		tmp0+="\n----------------------------------------------------"
		tmp1=""
		for j in self.getLesClusters():
			tmp2=""
			for k in j.getliste() :
				tmp2+=str(k.getXY())+" "
			tmp1+="- cluster "+str(kk)+" ["+tmp2+"]"+str(j.getCentre().getXY())+"\n"
			kk+=1

		tmp="-liste des Points crée {}\n-liste des Clusters \n{}".format(tmp0,tmp1)
		return tmp




#p1=Point(1,2)
#p2=Point(2,3)
#print(p1)
#print(p2)
#c1=Cluster()
#c1.append(p1)
#c1.append(p2)
#print(c1)
par=Partie(7,40)
#print(par)
par.initClusters()
#print(par)
par.run()
#print(par.test())
print(par)
par.afficher()

















