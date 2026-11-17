"""Exact rational tangent-line counts for the plane-filling pencil and its dual quartic.
Pure Python 3; no external dependencies. All operations are exact integer/modular.
"""
from collections import Counter


def points(p):
    return [(0,0,1)]+[(0,1,z) for z in range(p)]+[(1,y,z) for y in range(p) for z in range(p)]


def norm(a,p):
    for x in a:
        if x%p:
            inv=pow(x%p,-1,p)
            return tuple(z*inv%p for z in a)
    raise AssertionError('zero tangent vector')


def f_rootfree(p,k):
    return all((pow(x,7,p)+k*pow(x,3,p)-1)%p for x in range(p))


def gauss(P,k,p):
    x,y,z=P
    q1=x*x%p; q2=y*y%p; q3=(z*z+k*x*x)%p
    return norm((z*q3-y*q1,x*q1-z*q2,y*q2-x*q3),p)


def h_value(l,k,p):
    a,b,c=l
    return (a**3*b+b**3*c+a*c**3+k*(b**4+a*b*c*c))%p


def line_count(l,pts,k,p):
    a,b,c=l
    return sum(1 for P in pts if (a*P[0]+b*P[1]+c*P[2])%p==0 and gauss(P,k,p)==l)


def run():
    tested=0
    for p in (3,5,7,11,13,17,19,23,29):
        pts=points(p);N=p*p+p+1
        assert len(pts)==N and len(set(pts))==N
        for k in range(p):
            if not f_rootfree(p,k):
                continue
            raw=Counter(gauss(P,k,p) for P in pts)
            assert sum(raw.values())==N
            assert max(raw.values())<=2
            n1=sum(h_value(l,k,p)==0 for l in pts)
            n2=(N-n1)//2
            assert (N-n1)%2==0
            assert Counter(raw.values())==Counter({1:n1,2:n2})
            assert len(raw)==n1+n2
            # A separate check uses the line/point incidences rather than the Gauss-fiber counts.
            if p<=17:
                for l in pts:
                    cnt=line_count(l,pts,k,p)
                    assert cnt==raw[l]
                    assert (cnt==1)==(h_value(l,k,p)==0)
            if p in (3,5,7,11,29):
                print('p=%s k=%s unique=%s double=%s uncovered=%s' %(p,k,n1,n2,n2))
            tested+=1
    print('VERIFY_TANGENT_SPECTRUM_OK',tested)

if __name__=='__main__':run()
