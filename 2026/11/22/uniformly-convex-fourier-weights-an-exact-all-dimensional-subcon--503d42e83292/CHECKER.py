import numpy as np

def ratio(d,q,a,p,N,cap=24):
    # finite truncation: all k with each coordinate in [-cap,N+cap] for axial k1
    js=[np.arange(-cap,cap+1)]*(d-1)
    mesh=np.meshgrid(*js,indexing='ij')
    trans=sum(np.abs(j).astype(float)**q for j in mesh)
    val=0.
    for m in range(-cap,N+cap+1):
        r1=(abs(m)**q+trans)**(1/q)
        r2=(abs(N-m)**q+trans)**(1/q)
        ex=-a*(r1+r2-N)
        val+=np.sum(np.exp(ex)*((1+N)/((1+r1)*(1+r2)))**p)
    return float(val)
if __name__=='__main__':
    tests=[(2,2,1.5),(2,3,1.6666666667),(2,6,1.83333333),(3,3,2.3333333333)]
    for d,q,pc in tests:
        a=1.2
        N1,N2=(32,64) if d==2 else (12,24)
        cap=35 if d==2 else 16
        below=[ratio(d,q,a,pc-.4,N,cap) for N in [N1,N2]]
        critical=[ratio(d,q,a,pc,N,cap) for N in [N1,N2]]
        above=[ratio(d,q,a,pc+.4,N,cap) for N in [N1,N2]]
        print('d q pc',d,q,pc,'N',N1,N2,'below',below,'critical',critical,'above',above,flush=True)
        assert below[1] > below[0]*1.05
        assert critical[1]>critical[0]*1.02
        assert all(np.isfinite(x) and x>0 for x in below+critical+above)
    print('PASS general checker')
