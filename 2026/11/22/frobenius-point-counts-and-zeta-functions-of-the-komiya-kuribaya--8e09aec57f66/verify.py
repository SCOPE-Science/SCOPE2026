from kkcore import *
from contextlib import redirect_stdout
import io

def signperm(ei,er):
 def ss(v):return(v[0],ei*v[1],er*v[2],ei*er*v[3])
 def conjug(l):return tuple(ss(c) for c in l)
 def cross(a,b):
  return(sub(mul(a[1],b[2]),mul(a[2],b[1])),sub(mul(a[2],b[0]),mul(a[0],b[2])),sub(mul(a[0],b[1]),mul(a[1],b[0])))
 sp=[]
 for l in L:
  lc=conjug(l)
  v=[j for j,t in enumerate(L) if cross(lc,t)==(Z,Z,Z)]
  assert len(v)==1, (lc,v)
  sp.append(v[0]);
 assert sorted(sp)==list(range(28)) and all(sp[sp[i]]==i for i in range(28))
 return sp

def frob(p):
 ei=1 if pow(p-1,(p-1)//2,p)==1 else -1
 er=1 if pow(5,(p-1)//2,p)==1 else -1
 perm=signperm(ei,er)
 with redirect_stdout(io.StringIO()):Ps=modfield(p)
 pp={frozenset(perm[k] for k in S) for S in Ps}
 assert pp==Ps
 fixed=Counter(map(len,(S for S in Ps if frozenset(perm[k] for k in S)==S)))
 tot=Counter(map(len,Ps))
 # rational line counts and special point counts
 nline=sum(i==j for i,j in enumerate(perm))
 special=dict(sorted(fixed.items()))
 return (ei,er),nline,dict(sorted(tot.items())),special
if __name__=='__main__':
 for p in [7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,101,109,127]:
  print(p,frob(p))

def points_formula(p):
 ei=1 if pow(p-1,(p-1)//2,p)==1 else -1
 er=1 if pow(5,(p-1)//2,p)==1 else -1
 perm=signperm(ei,er)
 with redirect_stdout(io.StringIO()):Ps=modfield(p)
 fixed=[S for S in Ps if frozenset(perm[k] for k in S)==S]
 corr=sum(1-sum(perm[k]==k for k in S) for S in fixed)
 lin=sum(i==j for i,j in enumerate(perm))
 allcorr=28-sum((len(S)-1) for S in Ps)
 return lin,corr,28,allcorr,Counter((len(S),sum(perm[k]==k for k in S)) for S in fixed)
if __name__=='__main__':
 for p in [7,11,13,17,19,23,29,31,41,61,101,109]:
  print('NUMBERS',p,points_formula(p))

# Exact finite certificate for all good characteristics, plus samples for each
# Galois-sign pattern. Norm support proves the generic cases are uniform.
if __name__ == '__main__':
 EXPECT={
 7:((4,-3),{2:252,3:24,4:9}, {4:9}),
 13:((16,-87),{2:288,3:12,4:9},{2:48,3:12,4:9}),
 29:((28,-327),{2:252,3:24,4:9},{2:252,3:24,4:9}),
 41:((28,-327),{2:252,3:24,4:9},{2:252,3:24,4:9}),
 61:((28,-339),{2:288,3:12,4:9},{2:288,3:12,4:9}),
 101:((28,-327),{2:252,3:24,4:9},{2:252,3:24,4:9}),
 109:((28,-339),{2:288,3:12,4:9},{2:288,3:12,4:9}),
 11:((4,-3),{2:324,4:9},{4:9}),
 17:((16,-99),{2:324,4:9},{2:84,4:9}),
 23:((4,-3),{2:324,4:9},{4:9}),
 89:((28,-351),{2:324,4:9},{2:324,4:9}),
 }
 assert set(norms)=={2,3,5,7,13,29,41,61,101,109},norms
 assert len(base)==333 and Counter(map(len,base))=={2:324,4:9}
 for p,(lc,allc,fixc) in EXPECT.items():
  typ,nr,total,fx=frob(p)
  nl,b,_,a,_=points_formula(p)
  assert (nl,b)==lc, (p,nl,b,lc)
  assert total==allc and fx==fixc,(p,total,allc,fx,fixc)
  assert a==28-sum((k-1)*v for k,v in allc.items())
 assert len(D)==3276 and sum(v==Z for v in D.values())==36
 print('KK_BITANGENT_ZETA_ALL_PRIME_CLASSES_OK')
