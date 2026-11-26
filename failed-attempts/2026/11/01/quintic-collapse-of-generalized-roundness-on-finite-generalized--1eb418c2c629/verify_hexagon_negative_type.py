"""Exact symbolic and independent scalar verification of the generalized-hexagon metric theorem.
Only finite symbolic identities and sampled orders are checked; the all-order inequalities are proved in RESULT.md.
"""
import sympy as S
import mpmath as mp
q=S.symbols('q',positive=True); z=S.symbols('z')
b=[q+1,q,q,q,q,q,0]
c=[0,1,1,1,1,1,q+1]
P=[S.Integer(1),z]
for i in range(1,6):
    P.append(S.factor((z*P[i]-b[i-1]*P[i-1])/c[i+1]))
assert S.factor(P[6]-(z**6-(5*q+1)*z**4+(6*q*q+3*q)*z*z-q**3-q**2)/(q+1))==0
T=S.zeros(7)
for i in range(7):
    if i>0:T[i,i-1]=c[i]
    if i<6:T[i,i+1]=b[i]
assert S.simplify(T.charpoly(z).as_expr()-z*(z**2-3*q)*(z**2-q)*(z-q-1)*(z+q+1))==0
coeff=[S.factor(P[i].subs(z,-q-1)) for i in range(1,7)]
assert coeff==[-(q+1),q*(q+1),-q**2*(q+1),q**3*(q+1),-q**4*(q+1),q**5]
assert S.factor(sum(coeff))==-1
assert S.factor(sum(i*coeff[i-1] for i in range(1,7)))==(q-1)*(q*q-q+1)*(q*q+q+1)
for theta in [S.sqrt(3*q),-S.sqrt(3*q),S.sqrt(q),-S.sqrt(q),S.Integer(0)]:
    D=[S.factor(P[i].subs(z,-q-1)-P[i].subs(z,theta)) for i in range(1,7)]
    assert S.simplify(sum(D))==0
    H=[S.simplify(sum(D[j-1:])) for j in range(2,7)]
    for Q in [2,3,4,5,7,11,19]:
        h=list(map(lambda a:float(a.subs(q,Q)),H))
        # Two elementary adjacent-difference pairing certificates, except exactly two q=2 subcases.
        if Q==2 and theta==S.sqrt(q):
            assert h[2]+1.5*h[1] + h[4]+1.25*h[3]>0
        elif Q==2 and theta==0:
            assert h[0]==3 and h[1]==-6 and h[2]==6 and h[3]==-12 and h[4]==36
        else:
            assert h[0]>0 and h[2]+1.5*h[1]>0 and h[4]+1.25*h[3]>0,(theta,Q,h)
mp.mp.dps=75
out=[]
for Q in [2,3,4,5,7,11,19,41]:
    co=[mp.mpf(int(v.subs(q,Q))) for v in coeff]
    def f(t):
        return sum(co[i-1]*mp.power(i,t) for i in range(1,7))
    lo,hi=mp.mpf(0),mp.mpf(1)
    for _ in range(220):
        mid=(lo+hi)/2
        if f(mid)>0:hi=mid
        else:lo=mid
    rt=(lo+hi)/2
    assert abs(f(rt))<mp.mpf('1e-50')
    vals=[]
    for theta in [mp.sqrt(3*Q),-mp.sqrt(3*Q),mp.sqrt(Q),-mp.sqrt(Q),mp.mpf(0)]:
        vals1=[mp.mpf(str(S.N(v.subs({q:Q,z:theta}),70))) for v in P[1:]]
        vals.append(sum(vals1[i-1]*mp.power(i,rt) for i in range(1,7)))
    assert max(vals)<-mp.mpf('0.1'),(Q,vals)
    out.append((Q,mp.nstr(rt,18),mp.nstr(rt*Q**5,12),mp.nstr(max(vals),12)))
print('EXACT_OK seven spectral roots and distance-0..6 recurrence all q')
print('BOUNDS_CHECK_OK domination inequalities with q checks 2,3,4,5,7,11,19')
for row in out:print('ROOT_OK',*row)
print('HEXAGON_NEGATIVE_TYPE_CHECKS_OK')
