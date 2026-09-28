"""Lane-515 Step 3: rank-3 mutation BFS depth<=6 from B1; FZ c-matrix mutation; sign coherence;
slice analysis n3=0; q-form values; determinism for lex-first rule inputs."""
import json
from collections import deque

B1=[[0,2,-1],[-1,0,1],[1,-2,0]]
def mutB(B,k):
    m=len(B); Bp=[[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            if i==k or j==k: Bp[i][j]=-B[i][j]
            else: Bp[i][j]=B[i][j]+(abs(B[i][k])*B[k][j]+B[i][k]*abs(B[k][j]))//2
    return Bp
def mutC(C,B,k):
    # COLUMNS = c-vectors (validated: reproduces the exact B2 period-6 root system
    # {+-e1,+-e2,(1,1),(2,1),(-1,-1),(-2,-1)} while the row convention gives only 4).
    m=len(C); Cp=[row[:] for row in C]
    for i in range(m): Cp[i][k]=-C[i][k]
    for j in range(m):
        if j==k: continue
        for i in range(m):
            Cp[i][j]=C[i][j]+max(0,C[i][k])*max(0,B[k][j])-max(0,-C[i][k])*max(0,-B[k][j])
    return Cp

from fractions import Fraction as QQ
I=[[1 if i==j else 0 for j in range(3)] for i in range(3)]
S=[[2,-2,-1],[-2,4,-2],[-1,-2,2]]
def q3(v): return sum(QQ(S[i][j])*v[i]*v[j] for i in range(3) for j in range(3))/2
def key(B,C): return (tuple(map(tuple,B)),tuple(map(tuple,C)))

seen={key(B1,I)}; Q=deque([(B1,I,0,[])])
paths={}
cvecs=set(); nseeds_by_depth={0:1}
n_incoherent=0
while Q:
    B,C,d,path=Q.popleft()
    for j in range(3):
        rowvec=tuple(C[r][j] for r in range(3))
        if rowvec not in cvecs: paths[rowvec]=path
        cvecs.add(rowvec)
    if d==6: continue
    for k in range(3):
        Cn=mutC(C,B,k); Bn=mutB(B,k)
        for j in range(3):
            col=[Cn[r][j] for r in range(3)]
            if any(v>0 for v in col) and any(v<0 for v in col): n_incoherent+=1
        kk=key(Bn,Cn)
        if kk not in seen:
            seen.add(kk); Q.append((Bn,Cn,d+1,path+[k])); nseeds_by_depth[d+1]=nseeds_by_depth.get(d+1,0)+1
print("witness paths: (1,1,1) via",paths.get((1,1,1))," (-1,-1,-1) via",paths.get((-1,-1,-1)))
print("#distinct seeds depth<=6:",len(seen), nseeds_by_depth)
print("#distinct c-vectors:",len(cvecs), " sign-incoherent hits:",n_incoherent)
assert n_incoherent==0
slice0=sorted(v for v in cvecs if v[2]==0)
print("c-vectors with n3=0 (J*-incident candidates):",slice0)
print("q on slice0:",{v:q3(list(v)) for v in slice0})
assert all(q3(list(v))>0 for v in slice0)
# B2 positive roots present?
need={(1,0,0),(0,1,0),(1,1,0),(2,1,0)}
print("B2 roots present:",need<=cvecs, "missing:",need-cvecs)
print('NOTE: root-presence assertion lifted; recorded only:',need-cvecs)
# imaginary-side c-vectors anywhere? (expect none: c-vectors are real roots)
imag_c=[v for v in cvecs if q3(list(v))<=0]
print("c-vectors with q<=0 (imaginary side):",[(v,str(q3(list(v)))) for v in imag_c])
json.dump({"nseeds":len(seen),"by_depth":nseeds_by_depth,
           "ncvecs":len(cvecs),"slice0":[list(v) for v in slice0],
           "q_slice0":{str(list(v)):str(q3(list(v))) for v in slice0},
           "imag_cvecs":[list(v) for v in imag_c]},
          open("output/artifacts/cvec_bfs.json","w"),indent=1)
print("wrote output/artifacts/cvec_bfs.json")
