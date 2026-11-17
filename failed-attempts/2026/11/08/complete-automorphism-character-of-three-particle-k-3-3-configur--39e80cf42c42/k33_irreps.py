from k33_classes import AUT,chi,classes
from fractions import Fraction
N=72
# S3 irreps: trivial, sign, standard
names=('1','sgn','std')
def cht(l,p):
 if l==0:return 1
 if l==1:return (-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
 return sum(p[i]==i for i in range(3))-1

def pair(p,q):return tuple(p[q[i]] for i in range(3))
characters={}
for l in range(3):
 for sn in (1,-1):
  def ch(gi,l=l,sn=sn):
   g,em,swap,p,q=AUT[gi]
   return cht(l,p)*cht(l,q) if swap==0 else sn*cht(l,pair(p,q))
  characters[f'({names[l]},{"+" if sn==1 else "-"})']=ch
for l in range(3):
 for m in range(l+1,3):
  def ch(gi,l=l,m=m):
   g,em,swap,p,q=AUT[gi]
   return 0 if swap else cht(l,p)*cht(m,q)+cht(m,p)*cht(l,q)
  characters[f'({names[l]},{names[m]})']=ch
for name,c in characters.items():
 print(name,'dim',c(0),'mult',[Fraction(sum(len(cl)*chi[i][j]*c(i) for i,cl in classes),72) for j in (1,2)])
for a,ca in characters.items():
 for b,cb in characters.items():
  ip=Fraction(sum(len(cl)*ca(i)*cb(i) for i,cl in classes),72)
  assert ip==(1 if a==b else 0),(a,b,ip)
print('all 9 irreps orthonormal')
