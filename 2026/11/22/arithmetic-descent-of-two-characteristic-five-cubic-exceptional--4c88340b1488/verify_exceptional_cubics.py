"""Exact F_5/F_25 cubic-surface computations (requires SymPy).

F_25=F_5[s]/(s^2-2), stored as integers a+5b, 0<=a,b<5.
All line lists and intersection certificates are recomputed from equations.
"""
from itertools import combinations
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

def add(a,b): return ((a%5+b%5)%5)+5*((a//5+b//5)%5)
def mul(a,b):
 x,y=a%5,a//5;u,v=b%5,b//5
 return (x*u+2*y*v)%5+5*((x*v+y*u)%5)
T=[[mul(a,b) for b in range(25)] for a in range(25)]
A=[[add(a,b) for b in range(25)] for a in range(25)]
def neg(a): return T[4][a]
def sub(a,b): return A[a][neg(b)]
def frob(a):
 b=a
 for _ in range(4): b=T[b][a]
 return b

def rank4(rows):
 m=[list(row) for row in rows]; r=0
 for col in range(4):
  k=next((j for j in range(r,4) if m[j][col]),None)
  if k is None:continue
  m[r],m[k]=m[k],m[r]
  iv=next(z for z in range(1,25) if T[z][m[r][col]]==1)
  m[r]=[T[iv][u] for u in m[r]]
  for j in range(r+1,4):
   z=m[j][col]
   if z:m[j]=[sub(m[j][h],T[z][m[r][h]]) for h in range(4)]
  r+=1
  if r==4:break
 return r

def matrices(mode):
 out=[]
 for a in range(25):
  for b in range(25):
   for c in range(25):
    for d in range(25):
     a2=T[a][a];b2=T[b][b];c2=T[c][c];d2=T[d][d]
     if mode=='split':
      k0=sub(T[a][c2],T[a2][c]); k3=sub(T[b][d2],T[b2][d])
      if k0 or k3:continue
      k1=sub(A[T[b][c2]][T[2][T[a][T[c][d]]]],A[T[a2][d]][T[2][T[a][T[b][c]]]])
      k2=sub(A[T[a][d2]][T[2][T[b][T[c][d]]]],A[T[b2][c]][T[2][T[a][T[b][d]]]])
      if (k1,k2)!=(4,1):continue
     else:
      k0=sub(T[a][a2],T[2][T[a][c2]])
      k3=sub(T[b][b2],T[2][T[b][d2]])
      if k0!=1 or k3!=0:continue
      k1=sub(T[3][T[a2][b]],T[2][A[T[2][T[a][T[c][d]]]][T[b][c2]]])
      k2=sub(T[3][T[a][b2]],T[2][A[T[a][d2]][T[2][T[b][T[c][d]]]]])
      if (k1,k2)!=(0,3):continue
     if sub(T[a][d],T[b][c])==0:continue
     out.append((a,b,c,d))
 return out

def run(mode):
 sol=matrices(mode)
 assert len(sol)==18
 roots=[(0,1),(1,0),(1,1)] if mode=='split' else [(0,1),(5,1),(20,1)]
 lines=[]
 for (x,y) in roots:
  for (z,w) in roots: lines.append([(x,y,0,0),(0,0,z,w)])
 for (a,b,c,d) in sol: lines.append([(1,0,a,c),(0,1,b,d)])
 assert len(lines)==27
 G=Matrix(27,27,lambda i,j:-1 if i==j else int(rank4([*lines[i],*lines[j]])<4))
 assert G.rank()==7
 assert set(sum(int(G[i,j]==1) for j in range(27)) for i in range(27))=={10}
 perm=[]
 for v in lines:
  fv=[tuple(map(frob,row)) for row in v]
  ids=[i for i,w in enumerate(lines) if rank4([*fv,*w])==2]
  assert len(ids)==1
  perm.append(ids[0])
 assert all(perm[perm[i]]==i for i in range(27))
 fixed=sum(i==perm[i] for i in range(27))
 six=next(s for s in combinations(range(27),6) if all(G[i,j]==0 for i,j in combinations(s,2)))
 basis=next(list(six)+[j] for j in range(27) if j not in six and abs(G.extract(list(six)+[j],list(six)+[j]).det())==1)
 B=G.extract(basis,basis)
 C=Matrix.hstack(*[B.inv()*G.extract(basis,[perm[i]]) for i in basis])
 assert C*C==Matrix.eye(7) and C.T*B*C==B
 H=Matrix.hstack(*(C-Matrix.eye(7)).nullspace())
 # RREF kernel basis is integral and saturated if its free-entry columns form the identity.
 assert all(x.q==1 for x in H)
 free=[j for j in range(7) if (C-Matrix.eye(7)).rref()[1].count(j)==0]
 assert H.extract(free,list(range(H.cols)))==Matrix.eye(H.cols)
 K=H.T*B*H
 snf=tuple(abs(int(smith_normal_form(K,domain=ZZ)[i,i])) for i in range(K.rows))
 def count_five(f):
  counts=[sum(f(x,y)==v for x in range(5) for y in range(5)) for v in range(5)]
  return (sum(c*c for c in counts)-1)//4,counts
 if mode=='split': points,counts=count_five(lambda x,y:x*y*(y-x)%5)
 else:points,counts=count_five(lambda x,y:(x*x*x-2*x*y*y)%5)
 assert (fixed,H.cols,points)==({'split':(15,6,51),'nonsplit':(3,4,31)}[mode])
 assert abs(K.det())==({'split':2,'nonsplit':8}[mode])
 print(mode,'graph automorphisms',len(sol),'F5 graphs',sum(max(t)<5 for t in sol),'F5 line count',fixed,'Pic rank',H.cols,'Pic discriminant',K.det(),'SNF',snf,'points',points,'binary fibers',counts)
 print('line basis',basis,'Pic lattice Gram',K,'Frob characteristic',C.charpoly().as_expr())
 return mode,basis,C,H,K

if __name__=='__main__':
 for mode in ['split','nonsplit']:run(mode)
 print('All exact finite-field, line, Frobenius, and saturated-lattice checks passed.')
