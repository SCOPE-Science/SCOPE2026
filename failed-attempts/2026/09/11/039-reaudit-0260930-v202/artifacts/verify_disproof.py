"""Certify the TARGET disproof witness. Exact integer/rational arithmetic only (no floats)."""
from fractions import Fraction as Q

def mat_mul(A,B): return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
                          [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]
def mat_pow(A,k):
    R=[[1,0],[0,1]]
    for _ in range(k): R=mat_mul(R,A)
    return R
def tr(A): return A[0][0]+A[1][1]
def det(A): return A[0][0]*A[1][1]-A[0][1]*A[1][0]

A=[[1,1],[0,1]]     # sigma1
B=[[1,0],[-1,1]]    # sigma2
Ai=[[1,-1],[0,1]]; Bi=[[1,0],[1,1]]
# braid relation check
ABA=mat_mul(mat_mul(A,B),A); BAB=mat_mul(mat_mul(B,A),B)
assert ABA==BAB==[[0,1],[-1,0]], (ABA,BAB)
W=ABA  # image of Delta
W2=mat_mul(W,W)
assert W2==[[-1,0],[0,-1]], W2  # Delta^2 -> -I (central, in kernel of projectivization)
print("braid-relation OK; Delta^2 -> -I OK")

G=mat_mul(A,Bi)     # gamma = sigma1 sigma2^{-1}
assert tr(G)==3 and det(G)==1, G
Bs=mat_mul(G,W2)    # beta* = gamma Delta^2
assert tr(Bs)==-3 and det(Bs)==1, Bs
print("trace(gamma)=3 OK; trace(beta*)=-3 OK (|tr|=3>2 hyperbolic)")

# exponent sums (abelianization, conjugacy invariant)
e_gamma=1+(-1)            # 0
e_delta2=2*(1+1+1)        # 6
e_star=e_gamma+e_delta2   # 6
assert e_gamma==0 and e_star==6
print("exp(gamma)=0 OK; exp(beta*)=6 OK -> beta* not conjugate to any gamma^{+-k} (exp 0) OK")

# minimum bound: (3+sqrt5)/2 < 2.62  since sqrt5 < 2.24 (as 5 < 2.24^2 = 5.0176)
assert 5 < Q(224,100)**2
print("sqrt5<2.24 OK -> (3+sqrt5)/2 < 2.62 < 2.747 OK")

# quartic f(t)=t^4-3t^3-t^2+3t-1 at integers/rationals
def f(t): return t**4-3*t**3-t**2+3*t-1
def fp(t): return 4*t**3-9*t**2-2*t+3
assert f(Q(3))==-1 and f(Q(31,10))==Q(16691,10000), (f(Q(3)), f(Q(31,10)))
print("f(3)=-1 OK; f(3.1)=1.6691 OK -> largest-real-root candidate interval (3,3.1)")
# derivative lower bound: fp(t)-fp(3) = (t-3)(4t^2+3t+7) [exact polynomial identity],
# so fp(t) >= fp(3) = 24 > 0 for all t >= 3; hence f strictly increasing on [3,inf),
# so exactly one real root in (3,3.1) and it is the largest real root (all larger t have f>0).
assert fp(Q(3))==24
for t in [Q(3), Q(31,10), Q(4), Q(10)]:
    assert fp(t)-24 == (t-3)*(4*t*t+3*t+7), t
    assert fp(t) >= 24
print("fp(t)-24=(t-3)(4t^2+3t+7) OK; fp>=24 on {3,3.1,4,10} OK -> unique largest root in (3,3.1)")
# claimed approx 2.747 is not near any real root: f(2.747)<0 strictly (rational check)
t2747=Q(2747,1000)
print("f(2.747) =", float(f(t2747)), "(rational:", f(t2747), ") <0 OK" if f(t2747)<0 else "SIGN?")
assert f(t2747) < 0

# ---- Artin-action corroboration: Delta^2 acts by conjugation -> identical cyclic growth ----
def img(g,i,inv):
    a=abs(g); s=1 if g>0 else -1
    if not inv:
        if a==i: base=(i,i+1,-i)
        elif a==i+1: base=(i,)
        else: return (g,)
    else:
        if a==i: base=(i+1,)
        elif a==i+1: base=(-(i+1),i,i+1)
        else: return (g,)
    return base if s>0 else tuple(-x for x in reversed(base))
def apply_cyc(w,i,inv):
    out=[]
    for g in w:
        a=g if g>0 else -g
        out.extend(img(g,i,inv) if (a==i or a==i+1) else (g,))
    st=[]
    for g in out:
        if st and st[-1]==-g: st.pop()
        else: st.append(g)
    i0=0; j=len(st)
    while j-i0>=2 and st[i0]==-st[j-1]: i0+=1; j-=1
    return st[i0:j]
def ops(word):
    o=[]
    for (g,e) in word: o.extend([(g,e<0)]*abs(e))
    return o
D=[(1,1),(2,1),(1,1)]; Dm=[(1,-1),(2,-1),(1,-1)]
gamma=[(1,1),(2,-1)]; star=gamma+D+D
og=ops(gamma); os_=ops(star)
w1=[1,2]; w2=[1,2]
lg=[]; ls=[]
for _ in range(12):
    for (i,inv) in og: w1=apply_cyc(w1,i,inv)
    for (i,inv) in os_: w2=apply_cyc(w2,i,inv)
    lg.append(len(w1)); ls.append(len(w2))
assert lg==ls, (lg,ls)
print("cyclic-growth identical:", lg)
print("ALL_CHECKS_PASSED")
