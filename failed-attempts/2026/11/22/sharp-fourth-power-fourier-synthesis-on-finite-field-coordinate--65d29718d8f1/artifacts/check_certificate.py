"""Independent finite-field character-table sanity checks for the exact analytic formula."""
import cmath, math

def run(q):
    # Test prime fields; the general field statement follows analytically.
    assert q in (2, 3, 5, 7, 11)
    t=(q-1)**(1/3)
    D=1+2*t
    a=(2+2*t-q)/D
    b=(1+t)/D
    f={(x,y):(a if x==0 and y==0 else b) for x in range(q) for y in range(q) if x==0 or y==0}
    out={}
    for xi in range(q):
        for eta in range(q):
            out[xi,eta]=sum(z*cmath.exp(-2j*math.pi*(xi*x+eta*y)/q) for (x,y),z in f.items())/q
    assert abs(out[0,0]-1)<1e-12
    x=a-2*b
    for (xi,eta),v in out.items():
        expect=1 if (xi,eta)==(0,0) else ((q+x)/(2*q) if xi==0 or eta==0 else x/q)
        assert abs(v-expect)<1e-11, (q,xi,eta,v,expect)
    actual=sum(abs(z)**4 for z in out.values())
    exact=1+(q-1)**2/D**3
    assert abs(actual-exact)<1e-9
    assert abs((q+x)**3+8*(q-1)*x**3)<1e-9
    # A nonsymmetric variation keeps the Fourier value at the origin fixed.
    p=(1,0); n=(0,0)
    for e in (0.05, -0.05, 0.2):
        f2=dict(f); f2[p]+=e; f2[n]-=e
        norm=0.
        for xi in range(q):
            for eta in range(q):
                v=sum(z*cmath.exp(-2j*math.pi*(xi*x+eta*y)/q) for (x,y),z in f2.items())/q
                norm+=abs(v)**4
        assert norm>actual+1e-9
    return q, round(actual,12), round((1/exact)**.25,12)

if __name__=='__main__':
    for q in (2,3,5,7,11): print(*run(q))
    print('PASS')
