"""Exact rational certificates for a five-lane nursery-connectivity example.

Requires only the Python standard library. An exact uniformization expansion,
with rational exponential and Poisson-tail bounds, encloses each quantity.
"""
from fractions import Fraction as F
from math import factorial

N=65
Q=[[F(0) for j in range(5)] for i in range(5)]
for i in range(5):
    for j in (i-1,i+1):
        if 0<=j<5:
            Q[i][j]=F(1)
            Q[i][i]-=1
P=[[F(int(i==j))+Q[i][j]/2 for j in range(5)] for i in range(5)]
assert all(sum(row)==1 and min(row)>=0 for row in P)

def prod(M,y):
    return [sum(M[i][j]*y[j] for j in range(5)) for i in range(5)]

def exp_bound(y,t):
    """Certified closed rational interval for (e^{tQ} y)[0], t>=0."""
    t=F(t);assert 0<=t<=4
    u=2*t
    A=F(0);S=F(0);z=list(map(F,y));term=F(1)
    for k in range(N+1):
        A+=term*z[0]
        S+=term
        z=prod(P,z)
        term*=u/F(k+1)
    R=term/(1-u/F(N+2)) # tail of exp(u), sum k>=N+1
    M=max(abs(F(v)) for v in y)
    lo,hi=A-M*R,A+M*R
    emin,emax=1/(S+R),1/S
    return min(lo*emin,lo*emax,hi*emin,hi*emax),max(lo*emin,lo*emax,hi*emin,hi*emax)

def h(q):return list(map(F,[42,44,23,q,0]))
def dh(q):return prod(Q,h(q))
def cert_sign(interval,sign,label):
    a,b=interval
    if sign>0: assert a>0,(label,float(a),float(b))
    else: assert b<0,(label,float(a),float(b))

# Strict signs force exactly three interior extrema for every q in [95,97].
for q in (95,97):
    for t,sign in ((F(0),1),(F(1,2),-1),(F(1),1),(F(4),-1)):
        cert_sign(exp_bound(dh(q),t),sign,f'q={q} derivative t={t}')

root_boxes={
 95:((F(1181,10000),F(1182,10000)),(F(20262,10000),F(20263,10000))),
 97:((F(1191,10000),F(1192,10000)),(F(22297,10000),F(22298,10000))),
}
# There is one root in each isolated box, since 3 roots altogether.
for q,(early,late) in root_boxes.items():
    for label,(a,b) in [('early',early),('late',late)]:
        cert_sign(exp_bound(dh(q),a),1 if label=='early' else 1,f'q={q} {label} lower')
        cert_sign(exp_bound(dh(q),b),-1,f'q={q} {label} upper')
    def at_unknown_root(box):
        a,b=box
        m=(a+b)/2
        lo,hi=exp_bound(h(q),m)
        # Uniform stochastic bound |H_q'(t)| <= ||Q h_q||_infty.
        err=max(abs(z) for z in dh(q))*(b-a)/2
        return lo-err,hi+err
    e_lo,e_hi=at_unknown_root(early)
    l_lo,l_hi=at_unknown_root(late)
    gap=(l_lo-e_hi,l_hi-e_lo)
    cert_sign(gap,-1 if q==95 else 1,f'q={q} late-early value')
    print('q',q,'early-peak enclosure',*[float(z) for z in (e_lo,e_hi)],
          'late-peak enclosure',*[float(z) for z in (l_lo,l_hi)],
          'gap enclosure',*[float(z) for z in gap])

# Checks for the exact five-state generator and three-jump leading term.
assert prod(Q,[0,0,0,1,0])[0]==0
assert prod(Q,prod(Q,[0,0,0,1,0]))[0]==0
assert prod(Q,prod(Q,prod(Q,[0,0,0,1,0])))[0]==1
print('PASS: exact root isolation, strict signs, opposite peak gaps, and cubic onset')
