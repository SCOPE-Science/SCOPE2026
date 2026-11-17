from collections import defaultdict
STEPS=(1,9,10,13,15,17,20)

def relation_vectors(S=STEPS):
 S=tuple(sorted(S));ix={x:i for i,x in enumerate(S)}; groups=defaultdict(list)
 for i,a in enumerate(S):
  for j in range(i,len(S)):
   b=S[j]; groups[a+b].append((a,b))
 rel=[]
 for sm, pairs in groups.items():
  if sm in ix:
   a,b=pairs[0];vec=[0]*len(S)
   for t,c in ((a,1),(b,1),(sm,-1)):vec[ix[t]]+=c
   rel.append(vec)
  a,b=pairs[0]
  for c,d in pairs[1:]:
   vec=[0]*len(S)
   for t,z in ((a,1),(b,1),(c,-1),(d,-1)):vec[ix[t]]+=z
   rel.append(vec)
 return rel

def sparse_columns(n,S=STEPS):
 S=tuple(sorted(S)); assert n>2*max(S)
 # Identify 1-cycles with edges except spanning tree (0,1),(1,2),..,(n-2,n-1)
 ix={(x,s):i for i,(x,s) in enumerate((x,s) for x in range(n) for s in S if (s!=1 or x==n-1))}
 groups=defaultdict(list)
 for x in range(n):
  for a in S:
   for b in S:
    groups[(x,a+b)].append((a,b))
 cols=[]
 for (x,sm),pairs in groups.items():
  def boundary(part):
   d=defaultdict(int)
   for c,a,b in part:
    for edge,v in (((x,a),1),(((x+a)%n,b),1)):
     if edge in ix:d[ix[edge]]+=c*v
    if sm in S and (x,sm) in ix:d[ix[(x,sm)]]-=c
   return {j:v for j,v in d.items() if v}
  if sm in S:
   cols.extend(boundary([(1,a,b)]) for a,b in pairs)
  else:
   a,b=pairs[0]
   cols.extend(boundary([(1,c,d),(-1,a,b)]) for c,d in pairs[1:])
 return len(ix),cols

def sparse_rank(cols,p):
 piv={}
 for col in cols:
  v={i:c%p for i,c in col.items() if c%p}
  while v:
   i=min(v)
   if i not in piv:
    inv=pow(v[i],-1,p)
    piv[i]={j:(t*inv)%p for j,t in v.items()}
    break
   scale=v[i]; rr=piv[i]
   for j,t in rr.items():
    z=(v.get(j,0)-scale*t)%p
    if z: v[j]=z
    else: v.pop(j,None)
 return len(piv)

def determinant(M):
    n=len(M)
    if n==1:return M[0][0]
    a=[list(map(int,row)) for row in M]
    sign=1;prev=1
    for k in range(n-1):
        if not a[k][k]:
            j=next((j for j in range(k+1,n) if a[j][k]),None)
            if j is None:return 0
            a[k],a[j]=a[j],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator%prev==0
                a[i][j]=numerator//prev
        for i in range(k+1,n):a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]

if __name__=='__main__':
    import math
    R=relation_vectors()
    assert len(R)==6
    assert all(sum(x*s for x,s in zip(row,STEPS))==0 for row in R)
    # The 6x6 cofactor minors certify all nonzero Smith factors.
    minors=[determinant([[x for i,x in enumerate(row) if i!=j] for row in R]) for j in range(7)]
    assert minors[0]!=0 and math.gcd(*minors)==2
    assert all(sum(row[i]*(i==4) for i in range(7))%2==0 for row in R)
    u=[-15,0,0,0,1,0,0]
    # Exact integral certificate for 2u in the row lattice:
    coeff=(-21,-9,3,-7,-6,-1)
    assert [sum(coeff[i]*R[i][j] for i in range(6)) for j in range(7)]==[2*v for v in u]
    print('steps',STEPS)
    print('relation_rows',len(R),'maximal_minors',tuple(minors),'gcd',math.gcd(*minors))
    print('integral_group','Z plus Z/2; torsion u=E15-15E1; twice u certificate passed')
    for n in (41,43):
        nc,cols=sparse_columns(n); r2=sparse_rank(cols,2);r101=sparse_rank(cols,101)
        assert nc-r2==2 and nc-r101==1
        print('modulus',n,'cycle_rank',nc,'boundary_columns',len(cols),'rank_F2',r2,'rank_F101',r101,'betti_mod2',nc-r2,'betti_mod101',nc-r101)
    print('ALL CHECKS PASS')
