"""Exact integer/rational checks for the star cosmological-polytope outer ellipsoid.

Only Python standard library is required. Mathematical proof is in RESULT.md.
"""
from fractions import Fraction as F
from math import prod, sqrt


def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),F(0))


def check(m):
    assert isinstance(m,int) and m >= 1
    D=2*m+1
    d=2*m
    def e(j):
        x=[F(0)]*D
        x[j]=F(1)
        return x
    def plus(*vs):
        return [sum((v[j] for v in vs),F(0)) for j in range(D)]
    def scale(s,v):
        return [s*x for x in v]
    h=e(0)
    S=plus(*(plus(e(i),e(m+i)) for i in range(1,m+1)))
    W=[plus(e(i),scale(-1,e(m+i))) for i in range(1,m+1)]
    U=[plus(e(i),e(m+i),scale(F(-1,m),S)) for i in range(1,m+1)]
    delta=plus(scale(-2,h),scale(F(1,m),S))
    assert dot(delta,delta)==F(4)+F(2,m)
    verts=[]
    for w in W:
        verts.extend([plus(h,w),plus(h,scale(-1,w))])
    for u in U:
        verts.append(plus(scale(-1,h),scale(F(1,m),S),u))
    assert len({tuple(v) for v in verts})==3*m
    assert all(sum(v)==1 and dot(v,v)==3 for v in verts)
    c=[F(1,D)]*D
    a=F(m+1,D); b=F(m,D)
    weights=[a/F(2*m)]*(2*m)+[b/F(m)]*m
    assert sum(weights)==1
    assert all(sum(weights[j]*verts[j][i] for j in range(3*m))==c[i] for i in range(D))
    lT=F(4*m*(m+1),D); lV=F(4*(m+1),D); lU=F(4*m,D)
    def inner(v):
        z=plus(v,scale(-1,c))
        t=dot(z,delta)**2/dot(delta,delta)
        v2=sum((dot(z,w)**2/F(2) for w in W),F(0))
        u2=dot(z,z)-t-v2
        return t/lT+v2/lV+(u2/lU if m>1 else F(0))
    assert all(inner(v)==1 for v in verts)
    cov=[[sum((weights[k]*(verts[k][i]-c[i])*(verts[k][j]-c[j]) for k in range(3*m)),F(0)) for j in range(D)] for i in range(D)]
    # Projector matrices (U vanishes at m=1).
    for i in range(D):
        for j in range(D):
            pt=delta[i]*delta[j]/dot(delta,delta)
            pv=sum((w[i]*w[j]/2 for w in W),F(0))
            pu=sum((u[i]*u[j]/2 for u in U),F(0))
            assert 2*m*cov[i][j]==lT*pt+lV*pv+lU*pu
    R2=F(3)-F(1,D)
    assert all(dot(plus(v,scale(-1,c)),plus(v,scale(-1,c)))==R2 for v in verts)
    return {'m':m,'vertices':len(verts),'dimension':d, 'semiaxes_squared':(lT,lU,lV), 'radius_squared':R2}

if __name__=='__main__':
    import sys
    bound=int(sys.argv[1]) if len(sys.argv)>1 else 10
    assert 1<=bound<=20
    for m in range(1,bound+1):
        result=check(m)
        print('m=%d points=%d dimension=%d eigenvalues=%s' % (result['m'],result['vertices'],result['dimension'],result['semiaxes_squared']))
    for m in (1,2,3,5,10,20,40,80):
        rho=sqrt(m+1)*(2*sqrt(m*(m+1))/(3*m+1))**m
        assert 0<rho<=1+1e-12
    print('STAR_COSMO_LOEWNER_PASS', 'orders=1..'+str(bound))
