import itertools,sys
from collections import defaultdict

def rotate(c):return c[1],c[2],c[0]
def rot_sign(c):
 a,b,d=(len(x)-1 for x in c)
 return -1 if a*(b+d)%2 else 1

def sparse_sub(v,b,a,p):
 for j,x in b.items():
  z=(v.get(j,0)-a*x)%p
  if z:v[j]=z
  else:v.pop(j,None)

def rank_vectors(vecs,p=3):
 b={}
 for vec in vecs:
  v=vec.copy()
  while v:
   k=min(v); coeff=v[k]
   if k in b:sparse_sub(v,b[k],coeff,p)
   else:
    inv=pow(coeff,-1,p)
    b[k]={j:(x*inv)%p for j,x in v.items()}
    break
 return len(b)

def kernel_mod3(columns):
 piv={}; kernels=[]
 for i,orig in enumerate(columns):
  v={j:x%3 for j,x in orig.items() if x%3}
  rel={i:1}
  while v:
   k=min(v);coeff=v[k]
   if k in piv:
    w,r=piv[k];sparse_sub(v,w,coeff,3);sparse_sub(rel,r,coeff,3)
   else:
    inv=pow(coeff,-1,3)
    piv[k]=({j:(x*inv)%3 for j,x in v.items()},{j:(x*inv)%3 for j,x in rel.items()})
    break
  else:kernels.append(rel)
 return kernels,len(piv)

def full_top(n):
  cells=[]
  for assn in itertools.product([1,2,3],repeat=n):
   if 1 in assn and 2 in assn and 3 in assn:
    cells.append(tuple(tuple(i for i,x in enumerate(assn) if x==t) for t in [1,2,3]))
  cidx={c:i for i,c in enumerate(cells)}
  fidx={}
  cols=[]
  for c in cells:
   vec=defaultdict(int);off=0
   for k,A in enumerate(c):
    if len(A)>1:
     for z in range(len(A)):
      f=c[:k]+(A[:z]+A[z+1:],)+c[k+1:]
      if f not in fidx:fidx[f]=len(fidx)
      vec[fidx[f]]+=(-1)**(off+z)
    off+=len(A)-1
   cols.append(dict(vec))
  return cells,cidx,cols

def main(n):
 cells,idx,cols=full_top(n)
 basis,rnk=kernel_mod3(cols)
 assert len(basis)==2**n-3
 def T(vec):
  v=defaultdict(int)
  for j,c in vec.items():
   face=cells[j];t=idx[rotate(face)]
   v[t]+=c*rot_sign(face);v[j]-=c
  return {j:x%3 for j,x in v.items() if x%3}
 bT=[T(x) for x in basis]
 bT2=[T(x) for x in bT]
 r1=rank_vectors(bT);r2=rank_vectors(bT2)
 blocks=(len(basis)-2*r1+r2,r1-2*r2,r2)
 d=n-3
 expect=(1,0,(2**n-4)//3) if d%2 else (0,1,(2**n-5)//3)
 print('n',n,'top cells',len(cells),'top boundary rank',rnk,'homology dimension',len(basis),'(g-1) ranks',r1,r2,'Jordan blocks size 1,2,3',blocks,'expected',expect,flush=True)
 assert blocks==expect

if __name__=='__main__':
 for n in list(map(int,sys.argv[1:])) or [5,6]:main(n)
