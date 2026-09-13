import numpy as np, time
p=7
A=np.array([0,0,1,5,3],dtype=np.int64)
B=np.array([0,0,0,2,1,1,6,2],dtype=np.int64)
N=7**6
idx=np.arange(N)
X6=np.zeros((N,7),dtype=np.int64)
tmp=idx.copy()
for j in range(6):
    X6[:,j]=tmp%7; tmp//=7
def run(x6):
    X6[:,6]=x6
    C=np.zeros((N,19),dtype=np.int64)
    for i in range(7):
        Xi=X6[:,i]
        for j in range(7):
            Xij=(Xi*X6[:,j])%p
            for l in range(7):
                C[:,i+j+l]=(C[:,i+j+l]+Xij*X6[:,l])%p
    L=np.zeros((N,19),dtype=np.int64)
    for i in range(5):
        if A[i]:
            for j in range(7):
                if i+j<=18: L[:,i+j]=(L[:,i+j]+int(A[i])*X6[:,j])%p
    for k in range(8):
        L[:,k]=(L[:,k]+int(B[k]))%p
    R=(C+L)%p
    r18=pow(x6,3,p)
    y9=[y for y in range(p) if (y*y)%p==r18][0]
    inv2y9=pow((2*y9)%p,-1,p)
    Y=np.zeros((N,10),dtype=np.int64); Y[:,9]=y9
    for k in range(17,8,-1):
        m=k-9
        known=np.zeros(N,dtype=np.int64)
        for i in range(10):
            j=k-i
            if j<0 or j>9: continue
            if i==9 and j==m: continue
            if j==9 and i==m: continue
            known=(known+Y[:,i]*Y[:,j])%p
        Y[:,m]=((R[:,k]-known)*inv2y9)%p
    ok=np.ones(N,dtype=bool)
    for k in range(9):
        s=np.zeros(N,dtype=np.int64)
        for i in range(10):
            j=k-i
            if j<0 or j>9: continue
            s=(s+Y[:,i]*Y[:,j])%p
        ok&=(s==R[:,k])
    return np.where(ok)[0], y9
t0=time.time()
for x6 in (1,2,4):
    ids,y9=run(x6)
    print("x6=",x6,"y9=",y9,"nsol=",len(ids),"t=",round(time.time()-t0,1),flush=True)
    for i in ids[:10]:
        print("  x=",tuple(X6[i]))
print("TOTAL t=",round(time.time()-t0,1))
