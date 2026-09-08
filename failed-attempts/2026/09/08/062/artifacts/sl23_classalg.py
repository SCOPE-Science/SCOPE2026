"""S2: class multiplication constants + centralizer sizes for SL(2,3)."""
import json
MOD=3
def mat(a,b,c,d): return (a%3,b%3,c%3,d%3)
def mul(X,Y):
    a,b,c,d=X; e,f,g,h=Y
    return mat(a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h)
def mat_inv(X):
    a,b,c,d=X; return mat(d,-b,-c,a)
G=[mat(a,b,c,d) for a in range(3) for b in range(3) for c in range(3) for d in range(3) if (a*d-b*c)%3==1]
idx={g:i for i,g in enumerate(G)}
seen=[False]*24; classes=[]
for i,X in enumerate(G):
    if seen[i]: continue
    cl=set()
    for A in G:
        cl.add(idx[mul(mul(A,X),mat_inv(A))])
    for j in cl: seen[j]=True
    classes.append(sorted(cl))
classes.sort(key=len)
k=len(classes)
cls_of=[0]*24
for ci,c in enumerate(classes):
    for j in c: cls_of[j]=ci
sizes=[len(c) for c in classes]
# class multiplication constants c[i][j][kk]: (# of pairs (x in Ci,y in Cj) with xy in Ckk)/... store integer M[i][j][kk] = sum over x in Ci of #{y in Cj : xy in Ckk} for fixed rep? Standard: K_i K_j = sum c_ijk K_k with c integer.
reps=[c[0] for c in classes]
cconst={}
for i in range(k):
    for j in range(k):
        for kk in range(k):
            n=0
            x=G[reps[i]]
            for yj in classes[j]:
                if cls_of[idx[mul(x,G[yj])]]==kk: n+=1
            cconst[(i,j,kk)]=n
# verify associativity spot + identity class index
idx0=cls_of[idx[mat(1,0,0,1)]]
assert sizes[idx0]==1
print("sizes",sizes,"k",k,"idclass",idx0)
print("centralizer sizes:",[24//s for s in sizes])
json.dump({"sizes":sizes,"centralizers":[24//s for s in sizes],
           "cconst":{str(kk):v for kk,v in cconst.items()}},
          open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-192/output/artifacts/sl23_classalg.json","w"))
print("saved")
