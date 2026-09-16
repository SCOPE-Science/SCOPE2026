import itertools, sys
sys.path.insert(0,'output/artifacts')
from collections import deque
sys.path.insert(0,'.')
import sim_pivotal2 as S

def build_rect(Lx,Ly):
    adj={}
    for i in range(Lx+1):
        for j in range(Ly+1):
            adj[('z',i,j)]=[]
    for i in range(Lx):
        for j in range(Ly):
            adj[('f',i,j)]=[]
    for i in range(Lx):
        for j in range(Ly):
            f=('f',i,j)
            for (ii,jj) in ((i,j),(i+1,j),(i,j+1),(i+1,j+1)):
                z=('z',ii,jj); adj[f].append(z); adj[z].append(f)
    for i in range(Lx+1):
        for j in range(Ly+1):
            z=('z',i,j)
            if i<Lx:
                w=('z',i+1,j); adj[z].append(w); adj[w].append(z)
            if j<Ly:
                w=('z',i,j+1); adj[z].append(w); adj[w].append(z)
    return adj

def has_cross_rect(Lx,Ly,adj,st):
    seen=set(); dq=deque()
    for j in range(Ly+1):
        z=('z',0,j)
        if st[z]: dq.append(z); seen.add(z)
    while dq:
        u=dq.popleft()
        if u[0]=='z' and u[1]==Lx: return True
        for w in adj[u]:
            if w not in seen and st[w]: seen.add(w); dq.append(w)
    return False

def exact_pair(Lx,Ly,qmode='q0'):
    adj=build_rect(Lx,Ly)
    zlist=[('z',i,j) for i in range(Lx+1) for j in range(Ly+1)]
    flist=[('f',i,j) for i in range(Lx) for j in range(Ly)]
    for ic in range(Lx-1):
        for jc in range(Ly):
            if (ic+jc)%2==0: break
        if (ic+jc)%2==0: break
    v=('f',ic,jc); vp=('f',ic+1,jc)
    tot=pv=pvp=0
    for bits in itertools.product([False,True],repeat=len(zlist)):
        st=dict(zip(zlist,bits))
        for (fi,fj) in ((f[1],f[2]) for f in flist):
            st[('f',fi,fj)] = (False if (fi+fj)%2==0 else True)
        tot+=1
        for (vv,tag) in ((v,0),(vp,1)):
            b=st[vv]
            st[vv]=True; c1=has_cross_rect(Lx,Ly,adj,st)
            st[vv]=False; c0=has_cross_rect(Lx,Ly,adj,st)
            st[vv]=b
            if c1!=c0:
                if tag==0: pv+=1
                else: pvp+=1
    return (Lx,Ly,ic,jc,pv/tot,pvp/tot,(pv-pvp)/tot)

if __name__=='__main__':
    import math
    for (Lx,Ly) in [(2,2),(3,2),(4,4),(4,2),(3,3)]:
        r=exact_pair(Lx,Ly)
        print(f"L={Lx}x{Ly} center=({r[2]},{r[3]}): PII={r[4]:.6f} PIII={r[5]:.6f} Delta={r[6]:+.6f} ratio={r[6]/(1/(Lx*Ly)):+.4f}",flush=True)
