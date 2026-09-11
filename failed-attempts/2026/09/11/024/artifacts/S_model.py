"""Polycyclic model of S = (C8xC8xC4) : (C2xC2), pure stdlib+numpy."""
import numpy as np, itertools, time

# encode (i,j,k,a,b)
N=1024
def build_elems():
    E=[]
    for i in range(8):
        for j in range(8):
            for k in range(4):
                for a in range(2):
                    for b in range(2):
                        E.append((i,j,k,a,b))
    return np.array(E, dtype=np.int64)  # (1024,5)

E = build_elems()
index = {tuple(e):n for n,e in enumerate(map(tuple,E.tolist()))}

def act_on(i,j,k,a1,b1):
    # apply u^a1 v^b1 to (i,j,k)
    if b1:
        i = (5*i) % 8
        j = (-j) % 8
        # k unchanged
    if a1:
        i = (-i) % 8
        j = (3*j) % 8
        k = (-k) % 4
    return i,j,k

def mul_idx(n1,n2):
    i1,j1,k1,a1,b1 = E[n1]
    i2,j2,k2,a2,b2 = E[n2]
    ai,aj,ak = act_on(int(i2),int(j2),int(k2),int(a1),int(b1))
    i=(int(i1)+ai)%8; j=(int(j1)+aj)%8; k=(int(k1)+ak)%4
    a=(int(a1)+int(a2))%2; b=(int(b1)+int(b2))%2
    return index[(i,j,k,a,b)]

# vectorized mul table via loops (1024x1024 = 1M) using numpy where possible
def build_multable():
    # precompute action images for all 4 (a1,b1) on all elements' A-parts
    # act_table[(a1,b1), n] = (ai,aj,ak) of E[n] under (a1,b1)
    print("building multable...", flush=True)
    t0=time.time()
    MT = np.zeros((N,N), dtype=np.int32)
    # for speed, loop over n1 (1024) with vectorized inner loop over n2
    # precompute for each (a1,b1) the permuted A-coords arrays
    Aact = {}
    for a1 in (0,1):
        for b1 in (0,1):
            ai = np.zeros(N,dtype=np.int64); aj=np.zeros(N,dtype=np.int64); ak=np.zeros(N,dtype=np.int64)
            for n in range(N):
                i,j,k = int(E[n,0]),int(E[n,1]),int(E[n,2])
                x,y,z = act_on(i,j,k,a1,b1)
                ai[n]=x; aj[n]=y; ak[n]=z
            Aact[(a1,b1)]=(ai,aj,ak)
    # element lookup: build 5D index array idx[i,j,k,a,b]
    IDX = np.zeros((8,8,4,2,2),dtype=np.int32)
    for n,(i,j,k,a,b) in enumerate(E.tolist()):
        IDX[i,j,k,a,b]=n
    for n1 in range(N):
        i1,j1,k1,a1,b1 = (int(E[n1,0]),int(E[n1,1]),int(E[n1,2]),int(E[n1,3]),int(E[n1,4]))
        ai,aj,ak = Aact[(a1,b1)]
        ii = (i1+ai)%8; jj=(j1+aj)%8; kk=(k1+ak)%4
        aa = (a1+E[:,3])%2; bb=(b1+E[:,4])%2
        MT[n1,:] = IDX[ii,jj,kk,aa,bb]
    print(f"multable done in {time.time()-t0:.1f}s", flush=True)
    return MT

if __name__=="__main__":
    MT = build_multable()
    np.save("output/artifacts/multable.npy", MT)
    np.save("output/artifacts/elems.npy", E)
    print("saved", MT.shape)
