"""High-precision finite checks for the near-right-angle witness; not an infinite proof."""
import itertools
import mpmath as mp
mp.mp.dps=70
T=mp.mpf('1e-35')
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def vertices(A,b):
    out=[]
    for c in itertools.combinations(range(len(A)),3):
        C=mp.matrix([A[i] for i in c]); z=mp.matrix([b[i] for i in c])
        if abs(mp.det(C))<mp.mpf('1e-55'):continue
        x=list(mp.lu_solve(C,z))
        if max(dot(a,x)-h for a,h in zip(A,b))>T:continue
        if not any(max(abs(x[j]-y[j]) for j in range(3))<T for y in out):out.append(x)
    return out
def run(M,R):
    t=mp.acos(-1/R)
    v=[[mp.cos(j*t),mp.sin(j*t),R**(j-M)] for j in range(M)]
    A=[[mp.mpf(0),mp.mpf(0),mp.mpf(-1)],*v[:3]]
    b=[mp.mpf(0),*(R**(j-M) for j in range(3))]
    for k in range(2,M):
        W=vertices(A,b)
        assert len(W)==2*k,(k,'vertices')
        act=[[abs(dot(a,w)-h)<T for w in W] for a,h in zip(A,b)]
        edges=[(i,j) for i,j in itertools.combinations(range(len(A)),2) if sum(act[i][s] and act[j][s] for s in range(len(W)))>=2]
        assert len(edges)==3*k,(k,'edges')
        obt=[(i,j) for i,j in edges if dot(A[i],A[j])>T]
        assert len(obt)==k-2 and all(i>0 and j-i==3 for i,j in obt),(k,'obtuse')
        if k<M-1:
            p=list(mp.lu_solve(mp.matrix(v[k-2:k+1]),mp.matrix(b[k-1:k+2])))
            assert any(max(abs(x[j]-p[j]) for j in range(3))<T for x in W)
            other=[x for x in W if max(abs(x[j]-p[j]) for j in range(3))>=T]
            hi=dot(v[k+1],p);lo=max(dot(v[k+1],x) for x in other)
            assert hi>lo
            A.append(v[k+1]);b.append((hi+lo)/2)
        print(f'R={float(R):.4f} F={k+2} V={len(W)} E={len(edges)} obtuse={len(obt)}')
if __name__=='__main__':
    run(9,mp.mpf(6)+mp.pi/10)
    run(7,mp.mpf(16)+mp.pi/10)
    print('PASS all high-precision finite witnesses')
