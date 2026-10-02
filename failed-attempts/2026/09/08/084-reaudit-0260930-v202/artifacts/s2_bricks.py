import random, json, itertools
def enddim(a,b,M,order=2):
    # M: list of 3 matrices bxa over GF(p); unknowns X (axa), Y (bxb): YA_k = A_k X
    p=order; n=a*a+b*b; import copy
    rows=[]
    for k in range(3):
        A=M[k]
        for i in range(b):
            for j in range(a):
                r=[0]*n
                # (YA)_ij=sum_l Y_il A_lj ; (AX)_ij=sum_m A_im X_mj
                for l in range(b):
                    if A[l][j]: r[i*b+l]^=A[l][j]  # Y coef (xor since GF2, but A entries 0/1)
                for m in range(a):
                    if A[i][m]: r[b*b+m*a+j]^=A[i][m]
                rows.append(r)
    # nullspace dim over GF2
    M2=[r[:] for r in rows]; piv=0; where=[-1]*n
    R=len(M2)
    for c in range(n):
        f=None
        for i in range(piv,R):
            if M2[i][c]: f=i;break
        if f is None: continue
        M2[piv],M2[f]=M2[f],M2[piv]; where[c]=piv
        for i in range(R):
            if i!=piv and M2[i][c]:
                for j in range(c,n): M2[i][j]^=M2[piv][j]
        piv+=1
    return n-piv
def randrep(a,b,rng):
    return [[[rng.randint(0,1) for _ in range(a)] for _ in range(b)] for _ in range(3)]
def findbrick(a,b,trials,rng):
    best=(9,None)
    for _ in range(trials):
        M=randrep(a,b,rng)
        d=enddim(a,b,M)
        if d<best[0]: best=(d,M)
        if d==1: return 1,M
    return best
rng=random.Random(251)
out={}
L=[(2,2),(2,3),(3,3),(3,4),(4,4),(2,4)]
tri={'(2, 2)':400,'(2, 3)':800}
for d in L:
    a,b=d; t=600 if max(a,b)<=3 else 300
    if str(d) in ['(2, 2)','(2, 3)']: t={'(2, 2)':200,'(2, 3)':400}[str(d)]
    dd,M=findbrick(a,b,t,rng)
    out[str(d)]={'enddim':dd,'brick':(dd==1),'M':M}
    print(d,'enddim',dd)
json.dump(out,open('output/artifacts/s2_bricks.json','w'))
