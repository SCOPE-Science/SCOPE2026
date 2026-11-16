"""Independent exact distance-polynomial proof of the Dyck sampling spectra.
Requires Python 3 and SymPy.
"""
from math import comb
from sympy import Matrix, Symbol, Poly, factor

def enumerate_words(i, height, ups, prefix):
    if i==8:
        if height==0 and ups==4:
            yield tuple(prefix)
        return
    if ups<4:
        yield from enumerate_words(i+1,height+1,ups+1,prefix+[1])
    if height>0:
        yield from enumerate_words(i+1,height-1,ups,prefix+[0])

W=sorted(enumerate_words(0,0,0,[]))
assert len(W)==14

def krawtchouk(k,d):
    return sum((-1)**j*comb(d,j)*comb(8-d,k-j)
        for j in range(max(0,k-8+d),min(k,d)+1))

def gram(deg):
    return Matrix([[sum(krawtchouk(k,sum(a!=b for a,b in zip(u,v))) for k in range(deg+1))
                    for v in W] for u in W])

z=Symbol('z')
poly2= z*(z-12)**3*(z-32)**3*(z-52)*(z-64)**3*(z**3-142*z**2+5576*z-58112)
poly3= (z-64)*(z-96)**3*(z-104)*(z**2-184*z+8192)**3*(z**3-294*z**2+28528*z-912896)
for degree,target,rank in [(2,poly2,13),(3,poly3,14)]:
    G=gram(degree)
    assert factor(G.charpoly(z).as_expr()-target)==0
    assert G.rank()==rank
    assert G==G.T
    assert sum(G[i,i] for i in range(14))==14*sum(comb(8,k) for k in range(degree+1))
# Rigorous real-root localization by rational sign tests and square-free degree.
for f, intervals in [(z**3-142*z**2+5576*z-58112,[(16,17),(41,42),(83,84)]),
                     (z**3-294*z**2+28528*z-912896,[(80,81),(99,100),(113,114)]),
                     (z**2-184*z+8192,[(75,76),(108,109)])]:
    pp=Poly(f,z)
    assert len(intervals)==pp.degree()
    assert all(pp.eval(a)*pp.eval(b)<0 for a,b in intervals)
print('DISTANCE_DYCK_WALSH_SPECTRA_PASS')
