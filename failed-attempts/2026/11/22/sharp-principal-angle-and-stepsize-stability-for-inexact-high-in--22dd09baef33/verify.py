"""Exact-rational checks for a sharp projector-angle stability theorem.

The infinite-dimensional quantifiers (arbitrary finite n, changing projectors,
all SPD metrics) are proved algebraically in the accompanying result. This
program checks symbolic specializations and both sides of the sharp boundary.
No network access or third-party packages are needed.
"""
from fractions import Fraction as F


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def tr(a):
    return [list(x) for x in zip(*a)]


def mul(a, b):
    bt = tr(b)
    return [[sum(x*y for x,y in zip(ar,bc)) for bc in bt] for ar in a]


def add(a,b):
    return [[x+y for x,y in zip(ar,br)] for ar,br in zip(a,b)]


def scale(a,c):
    return [[c*x for x in row] for row in a]


def sub(a,b):
    return add(a,scale(b,-1))


def diag(values):
    a = eye(len(values))
    for i,v in enumerate(values):
        a[i][i] = F(v)
    return a


def outer(v,w):
    return [[x*y for y in w] for x in v]


def all_principal_minors_nonnegative(a,strict=False):
    # Principal minors, not just leading minors, so this tests PSD.
    n=len(a)
    for mask in range(1,1<<n):
        inds=[i for i in range(n) if mask & (1<<i)]
        z=[[a[i][j] for j in inds] for i in inds]
        determinant=F(1)
        for i in range(len(inds)):
            for j in range(i+1,len(inds)):
                if z[j][i]:
                    z[i],z[j]=z[j],z[i]
                    determinant=-determinant
                    break
            else:
                # No lower pivot; either z[i][i] nonzero or this minor is zero.
                if z[i][i] == 0:
                    determinant=F(0)
                    break
            p=z[i][i]
            if p == 0:
                determinant=F(0)
                break
            determinant*=p
            for j in range(i+1,len(inds)):
                f=z[j][i]/p
                for k in range(i+1,len(inds)):
                    z[j][k]-=f*z[i][k]
                z[j][i]=F(0)
        if determinant<0 or (strict and determinant==0):
            return False
    return True


def test_case(pairs,root_d,step):
    # Block basis = [negative eigenaxes, positive eigenaxes].
    k=len(pairs); n=2*k
    p=diag([1]*k+[0]*k)
    q=[[F(0) for _ in range(n)] for _ in range(n)]
    for j,(c,s) in enumerate(pairs):
        assert c*c+s*s==1
        v=[F(0)]*n
        v[j]=c;v[k+j]=s
        q=add(q,outer(v,v))
    ident=eye(n)
    sign=sub(ident,scale(p,F(2)))
    reflector=sub(ident,scale(q,F(2)))
    u=mul(reflector,sign)
    lhs=scale(add(u,tr(u)),F(1,2))
    rhs=sub(ident,scale(mul(sub(p,q),sub(p,q)),F(2)))
    assert lhs==rhs,"Projector-reflection identity failed"
    cmin=min(c*c-s*s for c,s in pairs)
    assert cmin>0
    droot=diag(root_d)
    L=max(x*x for x in root_d)
    mu=min(x*x for x in root_d)
    assert step>0 and step*L<2*cmin
    C=mul(mul(droot,u),droot)
    t=sub(ident,scale(C,step))
    bound=F(1)-step*mu*(2*cmin-step*L)
    gap=sub(scale(ident,bound),mul(tr(t),t))
    assert all_principal_minors_nonnegative(gap),"Global contraction certificate failed"
    return cmin,L,mu,bound


def test_sharpness(c,s,L):
    ident=eye(2)
    p=diag([1,0]); v=[c,s];q=outer(v,v)
    u=mul(sub(ident,scale(q,2)),sub(ident,scale(p,2)))
    c2=c*c-s*s
    assert c*c+s*s==1
    assert scale(add(u,tr(u)),F(1,2))==scale(ident,c2)
    threshold=F(2)*c2/F(L)
    for h in [threshold,threshold+F(1,20)]:
        t=sub(ident,scale(u,h*L))
        gram=mul(tr(t),t)
        factor=F(1)-2*h*L*c2+(h*L)**2
        assert gram==scale(ident,factor)
        if h==threshold:
            assert factor==1
        else:
            assert factor>1
    return threshold


def main():
    pair1=(F(4,5),F(3,5))
    pair2=(F(12,13),F(5,13))
    cases=[([pair1],[1,2],F(1,10)),
           ([pair1,pair2],[1,2,3,4],F(1,40)),
           ([pair1,pair1,pair2],[1,2,3,4,5,6],F(1,100))]
    for pairs,roots,h in cases:
        c,L,mu,bound=test_case(pairs,roots,h)
        print('PASS exact n=%d k=%d; cos(2theta)=%s; L=%s; squared-bound=%s'%(2*len(pairs),len(pairs),c,L,bound))
    print('PASS exact boundary h* =',test_sharpness(*pair1,5))
    # At 45 degrees, an arbitrarily small positive step expands a norm.
    u=mul(sub(eye(2),scale([[F(1,2),F(1,2)],[F(1,2),F(1,2)]],2)),diag([-1,1]))
    h=F(1,100)
    t=sub(eye(2),scale(u,h))
    assert mul(tr(t),t)==scale(eye(2),F(1)+h*h)
    print('PASS 45-degree boundary expands at every positive step')

if __name__=='__main__':
    main()
