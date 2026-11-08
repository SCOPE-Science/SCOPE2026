"""Exact rational checks of finite Fourier-idempotent local factorizations.

Run: python check_exact.py
The proof for infinite torsion groups is analytic, not finite enumeration.
"""
from fractions import Fraction as Q

checks=0

def insist(statement):
    global checks
    assert statement
    checks+=1

def plus(a,b): return [x+y for x,y in zip(a,b)]
def minus(a,b): return [x-y for x,y in zip(a,b)]
def scale(c,a): return [c*x for x in a]
def norm(a): return sum(abs(x) for x in a)

def conv(a,b):
    n=len(a)
    return [sum(a[j]*b[k^j] for j in range(n)) for k in range(n)]

def walsh(a):
    n=len(a)
    return [sum(a[j]*(-1 if ((j & k).bit_count()%2) else 1) for j in range(n)) for k in range(n)]

def iwalsh(a): return scale(Q(1,len(a)),walsh(a))

def ee(k,r,d):
    n=1<<d
    return [Q((-1 if ((g&k).bit_count()%2) else 1),1<<r) if g<(1<<r) else Q(0) for g in range(n)]

def unit(d): return [Q(1)]+[Q(0)]*((1<<d)-1)

for d in range(1,6):
    for r in range(1,d+1):
        es=[ee(k,r,d) for k in range(1<<r)]
        e_sum=[sum(e[g] for e in es) for g in range(1<<d)]
        insist(e_sum==unit(d))
        for k in range(1<<r):
            insist(norm(es[k])==1)
            for l in range(1<<r):
                insist(conv(es[k],es[l]) == (es[k] if k==l else [Q(0)]*(1<<d)))
        m=1<<r
        # Coefficient classes include simultaneous spectral zeros and no simultaneous zeros.
        for case in range(6):
            aa=[Q(0 if (k+case)%3==0 else (-1 if k%2 else 2)) for k in range(m)]
            bb=[Q(0 if (2*k+case)%4==0 else (1 if k%2 else -2)) for k in range(m)]
            a=[sum(aa[k]*es[k][g] for k in range(m)) for g in range(1<<d)]
            b=[sum(bb[k]*es[k][g] for k in range(m)) for g in range(1<<d)]
            delta=Q(1,1<<24)
            root=Q(1,1<<12)
            h=scale(delta,unit(d))
            xa=[Q(0)]*(1<<d); yb=[Q(0)]*(1<<d)
            for k in range(m):
                hk=conv(es[k],h)
                if aa[k]:
                    xk=scale(aa[k],es[k]); yk=plus(scale(bb[k],es[k]),scale(1/aa[k],hk))
                elif bb[k]:
                    xk=scale(1/bb[k],hk); yk=scale(bb[k],es[k])
                else:
                    xk=scale(root,es[k]); yk=scale(1/root,hk)
                xa=plus(xa,xk); yb=plus(yb,yk)
            insist(conv(xa,yb)==plus(conv(a,b),h))
            insist(norm(minus(xa,a))<=m*(delta+root))
            insist(norm(minus(yb,b))<=m*(delta+root))
            insist((not any(aa[k]==0 and bb[k]==0 for k in range(m))) or delta<=root*root)

        # One finite-spectrum factor, other an arbitrary element of the larger subgroup.
        if d>r:
            a=[sum(Q(k%3-1)*es[k][g] for k in range(m)) for g in range(1<<d)]
            b=[Q(((5*g+3*d)%11)-5,1<<d) for g in range(1<<d)]
            hh=scale(Q(1,1<<90), unit(d))
            xx=[Q(0)]*(1<<d); yy=[Q(0)]*(1<<d)
            for k in range(m):
                ak=Q(k%3-1)
                bk=conv(es[k],b); hk=conv(es[k],hh)
                if ak:
                    xk=scale(ak,es[k]); yk=plus(bk,scale(1/ak,hk))
                else:
                    # Small rational shift avoids all finitely many spectral zeros.
                    v=None
                    for j in range(12,35):
                        shift=Q(1,1<<j)
                        candidate=plus(bk,scale(shift,es[k]))
                        freqs=walsh(candidate)
                        if all(freqs[t] for t in range(1<<d) if (t % m)==k):
                            v=candidate;break
                    insist(v is not None)
                    ff=walsh(v)
                    inv=iwalsh([1/ff[t] if (t % m)==k else Q(0) for t in range(1<<d)])
                    insist(conv(v,inv)==es[k])
                    xk=conv(hk,inv); yk=v
                xx=plus(xx,xk); yy=plus(yy,yk)
            insist(conv(xx,yy)==plus(conv(a,b),hh))
            insist(norm(minus(xx,a))<Q(1,8))
            insist(norm(minus(yy,b))<Q(1,8))

print('FINITE_SUPPORT_LOCAL_OPENNESS_EXACT_OK',checks)

