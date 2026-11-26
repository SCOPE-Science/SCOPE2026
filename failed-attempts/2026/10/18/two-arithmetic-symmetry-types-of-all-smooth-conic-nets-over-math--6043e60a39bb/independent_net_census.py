"""Independent vectorized enumeration of three-spaces of ternary quadratics over GF(5)."""
import numpy as np, itertools, hashlib
p=5
allnets=[]
seen_count=0
params=[(1,a,b) for a in range(5) for b in range(5)]+[(0,1,b) for b in range(5)]+[(0,0,1)]
for piv in itertools.combinations(range(6),3):
    slots=[(i,j) for i in range(3) for j in range(6) if j>piv[i] and j not in piv]
    size=5**len(slots)
    for lo in range(0,size,40000):
        n=min(size-lo,40000)
        rows=np.zeros((n,3,6),dtype=np.int16)
        for i,k in enumerate(piv): rows[:,i,k]=1
        enc=np.arange(lo,lo+n,dtype=np.int64)
        for i,j in slots:
            rows[:,i,j]=enc%5
            enc//=5
        ok=np.ones(n,dtype=bool)
        for u,v,w in params:
            a=(u*rows[:,0,:]+v*rows[:,1,:]+w*rows[:,2,:])%5
            A,B,C,D,E,F=a.T
            # determinant of full doubled symmetric coefficient matrix, expanded as 3x3 determinant
            t1=(2*A)%5; t2=(2*B)%5; t3=(2*C)%5
            determinant=(t1*t2*t3 + 2*D*E*F - t1*F*F - t2*E*E - t3*D*D)%5
            ok &= determinant!=0
            if not ok.any():break
        allnets.extend(map(bytes,rows[ok].astype(np.uint8).reshape((-1,18))))
        seen_count+=n
assert seen_count==2558556,(seen_count)
saved=open(str(__import__('pathlib').Path(__file__).resolve().parent / 'conic_nets_q5.bin'),'rb').read()
recs=set(saved[i:i+18] for i in range(0,len(saved),18))
assert len(allnets)==8000 and len(set(allnets))==8000
assert set(allnets)==recs
print('TOTAL 3-spaces',seen_count)
print('ALL-SMOOTH nets',len(allnets))
print('C++/numpy sets agree',True)
print('Canonical net records SHA256',hashlib.sha256(b''.join(sorted(recs))).hexdigest())
