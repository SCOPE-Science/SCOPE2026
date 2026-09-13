"""Script X: correct high-block probe: columns (fixed INPUT k, mass over outputs j).
Column k=0 is trivially e_0 (volume preservation). Take k=(1,0,0): mass spread over j?
And ROW masses for high-stable j (fixed output j, over inputs k in box): the D-block
row norm = sqrt(sum_{|k|>K}|M[j,k]|^2)."""
import numpy as np, math
Amat=np.array([[2.,1.,0.],[1.,2.,1.],[0.,1.,1.]])
a,b=0.03,0.02
def f(y):
    z=np.stack([y[...,0]+a*np.sin(2*np.pi*y[...,1]),y[...,1]+b*np.sin(2*np.pi*y[...,2]),y[...,2]],axis=-1)%1
    return (z@Amat.T)%1
K=2; N=24
modes=[(i,j,k) for i in range(-4,5) for j in range(-4,5) for k in range(-4,5)]
Jarr=np.array(modes,float)
g=np.linspace(0,1,N,endpoint=False)
X,Y,Z=np.meshgrid(g,g,g,indexing='ij'); grid=np.stack([X,Y,Z],axis=-1); Fy=f(grid)
def col(k, radius=4):
    G=np.exp(2j*np.pi*(np.einsum('...d,d->...',grid,np.array(k,float))[...,None]-np.einsum('...d,md->...m',Fy,Jarr)))
    return np.array([G[...,j].mean() for j in range(len(modes))])
for k in [(1,0,0),(0,1,0),(1,1,1)]:
    c=np.abs(col(k))
    o=np.argsort(-c)
    out=np.array([max(abs(mm) for mm in m) for m in modes])>2
    print(f"input k={k}: top outputs:",[(modes[i],round(float(c[i]),3)) for i in o[:6]]," col mass outside box2:",round(float(np.sqrt((c[out]**2).sum())),4))
# rows for high outputs
M4=np.zeros((len(modes),len(modes)),complex)
KK=[m for m in modes if max(abs(mm) for mm in m)<=2]
idx={m:i for i,m in enumerate(modes)}
for k in KK:
    M4[:,idx[k]]=col(k)
for j in [(3,0,0),(0,3,0),(0,0,3),(4,1,0),(3,3,0)]:
    r=np.abs(M4[idx[j],:])
    print(f"output j={j}: row mass inside box2 = {r.sum():.4f}, max entry {r.max():.4f}")
