import itertools, sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

def basisH2(a):
    return list(itertools.combinations(range(1,a),3))

def coeffs(a,P,I):
    tet=(0,)+I; P=tuple(sorted(P)); others=[v for v in range(a) if v not in P];
    # coefficient at each triangle containing P in oriented boundary of [tet]
    c=[]
    for v in others:
      tri=tuple(sorted(P+(v,)))
      if not set(tri).issubset(tet): c.append(0);continue
      missing=list(set(tet)-set(tri))[0]
      j=tet.index(missing)
      sign=(-1)**j
      c.append(sign*(-1)**sum(tri[i]>tri[i+1] for i in range(len(tri)-1))) # sorted tri, sign orientation of boundary tet restricted; link extraction orientation of P, leftover v
      # If P not same as beginning of tri, factor permutation sign of (p,q,v) to tri
      arr=P+(v,); inv=sum(arr[i]>arr[j] for i in range(3) for j in range(i+1,3)); c[-1]*=(-1)**inv
    # 0-chains sum=0, represent by first len-1 coords (last determined)
    assert sum(c)==0,(a,P,I,c)
    return c[:-1]

def matrix(a,b, blocks):
    IA=basisH2(a);IB=basisH2(b)
    rows=[]
    for P,Q in blocks:
        AA=[coeffs(a,P,I) for I in IA];BB=[coeffs(b,Q,J) for J in IB]
        for i in range(a-3):
            for j in range(b-3):
                rows.append([AA[ii][i]*BB[jj][j] for ii in range(len(IA)) for jj in range(len(IB))])
    return s.Matrix(rows)
for a,b in [(4,4),(4,5),(4,6),(4,7),(5,5),(5,6),(5,7),(6,6),(6,7)]:
 for m in range(1,min(a,b)//2+1):
  blocks=[((2*i,2*i+1),(2*i,2*i+1)) for i in range(m)]
  M=matrix(a,b,blocks)
  if M.rows>60: continue
  rank=M.rank(); diag=[abs(int(x)) for x in smith_normal_form(M,domain=ZZ).diagonal() if x]
  print(a,b,m, 'rank',rank,'target',M.rows,'source',M.cols, 'torsion', [x for x in diag if x!=1],flush=True)
