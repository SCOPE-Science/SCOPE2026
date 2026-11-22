"""Independent exact-integer one-dimensional tail and saddlepoint diagnostics."""
from math import sqrt, pi

def tail(m):
    # Numerator of Pr[S_m <= -1] where each page gives increments
    # +1, 0, -1 with multiplicities 3, 1, 2 respectively.
    d = {0:1}
    for _ in range(m):
        new = {}
        for s,n in d.items():
            new[s+1] = new.get(s+1,0)+3*n
            new[s] = new.get(s,0)+n
            new[s-1] = new.get(s-1,0)+2*n
        d = new
    return sum(n for k,n in d.items() if k<=-1)/6**m

if __name__=='__main__':
    r=sqrt(2/3)
    rho=(1+2*sqrt(6))/6
    variance=2*sqrt(6)/(1+2*sqrt(6))
    c=r/(1-r)/sqrt(2*pi*variance)
    assert 0 < (2*r+r*r+2+r**(-2))/6 < rho < 1
    assert 0 < (2+2*sqrt(3))/6 < rho
    for m in (50,100,200,400):
        p=tail(m)
        scaled=p*sqrt(m)/(rho**m)
        print(m, f'{scaled:.12f}', f'limit={c:.12f}')
    assert abs(tail(400)*sqrt(400)/(rho**400)/c-1)<0.08
    print('LARGE_DEVIATION_DIAGNOSTIC_OK')
