#!/usr/bin/env python3
"""Direct finite checks for the R5 characteristic-five commutator theorem.

Uses the defining quandle product for exhaustive work over F5 and a
separate quadratic-character calculation for F25. Python 3, stdlib only.
"""
from itertools import product

P=5
ZERO=(0,)*5
ONE=(1,0,0,0,0)
T=(0,1,0,0,0)

def plus(a,b):return tuple((x+y)%5 for x,y in zip(a,b))
def neg(a):return tuple((-x)%5 for x in a)
def scale(a,c):return tuple(c*x%5 for x in a)
def mul(a,b):
    z=[0]*5
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):z[(i+j)%5]=(z[(i+j)%5]+ai*bj)%5
    return tuple(z)
def power(a,n):
    z=ONE
    for _ in range(n):z=mul(z,a)
    return z
def theta(a):
    z=[0]*5
    for i,v in enumerate(a):z[(3*i)%5]=(z[(3*i)%5]+v)%5
    return tuple(z)
def inv(a):
    z=[0]*5
    for i,v in enumerate(a):z[(-i)%5]=(z[(-i)%5]+v)%5
    return tuple(z)
def double(a):
    z=[0]*5
    for i,v in enumerate(a):z[(2*i)%5]=(z[(2*i)%5]+v)%5
    return tuple(z)
def bracket(a,b):
    # Arguments are transported coordinates x=inv(f), y=inv(g).
    f,g=inv(a),inv(b)
    return plus(mul(inv(f),double(g)),neg(mul(inv(g),double(f))))

def in_u(c,ubasis):
    z=ZERO
    for w,v in zip(c,ubasis):z=plus(z,scale(v,w))
    return z

def rank_mod5(vs):
    piv={}
    for v in vs:
        a=list(v)
        for i in sorted(piv):
            if a[i]:a=[(x-a[i]*y)%5 for x,y in zip(a,piv[i])]
        if any(a):
            j=next(i for i,x in enumerate(a) if x)
            a=[x*pow(a[j],-1,5)%5 for x in a]
            piv[j]=a
    return len(piv)

def main():
    s=plus(T,neg(ONE))
    # The projector to the 3-eigenspace of theta gives u=s+O(s^2).
    u=ZERO
    for j in range(4):
        tmp=s
        for _ in range(j):tmp=theta(tmp)
        u=plus(u,scale(tmp,(4*pow(pow(3,j,5),-1,5))%5))
    ubasis=[power(u,i) for i in range(5)]
    assert rank_mod5(ubasis)==5
    assert theta(u)==scale(u,3)
    assert power(u,5)==ZERO
    # Test the closed coefficient formula on 800 independent random inputs.
    import random
    random.seed(50311)
    for _ in range(800):
        x=[random.randrange(5) for i in range(5)]
        y=[random.randrange(5) for i in range(5)]
        xt=in_u(x,ubasis);yt=in_u(y,ubasis)
        raw=bracket(xt,yt)
        pred=[0,
              2*(x[0]*y[1]-x[1]*y[0])%5,
              3*(x[0]*y[2]-x[2]*y[0])%5,
              (x[0]*y[3]-x[3]*y[0]+x[1]*y[2]-x[2]*y[1])%5,
              (-x[1]*y[3]+x[3]*y[1])%5]
        assert raw==in_u(pred,ubasis), (x,y,raw,pred)
    # Exhaustively enumerate images of y -> [x,y] for each x in the
    # 4-dimensional effective input space. This is independent of discriminants.
    seen=set()
    ux=[in_u((1 if i==j else 0 for i in range(5)),ubasis) for j in range(4)]
    for x in product(range(5),repeat=4):
        xx=tuple(sum(x[i]*ux[i][j] for i in range(4))%5 for j in range(5))
        cols=[bracket(xx,ux[j]) for j in range(4)]
        sub={ZERO}
        for c in cols:
            sub={plus(v,scale(c,k)) for v in sub for k in range(5)}
        seen.update(sub)
    assert len(seen)==585,('image_count',len(seen))
    predicted=set()
    nonsquare=set(range(5))-{(a*a)%5 for a in range(5)}
    for a,b,c,d in product(range(5),repeat=4):
        delta=(c*c+3*b*d)%5
        if a !=0 or b==0 or delta not in nonsquare:
            predicted.add(in_u((0,a,b,c,d),ubasis))
    assert seen==predicted,('mismatch',len(seen^predicted))
    # Source's explicit length-2 witness, whose coefficient sum is zero.
    witness=(2,1,1,2,4)
    assert witness not in seen
    # Separately count discriminant nonsquares in F25 = F5[z]/(z^2-2).
    items=list(product(range(5),repeat=2))
    def fm(a,b):return ((a[0]*b[0]+2*a[1]*b[1])%5,(a[0]*b[1]+a[1]*b[0])%5)
    def fa(a,b):return ((a[0]+b[0])%5,(a[1]+b[1])%5)
    def fs(a,k):return (a[0]*k%5,a[1]*k%5)
    squares={fm(a,a) for a in items}
    assert len(squares)==13
    cnt=0
    for b in items[1:]:
        for c in items:
            for d in items:
                discriminant=fa(fm(c,c),fs(fm(b,d),3))
                if discriminant not in squares:cnt+=1
    assert cnt==7200,(cnt,7200)
    print('VERIFY_OK')
    print('u_t_basis =',u)
    print('F5_single_bracket_outputs =',len(seen))
    print('F5_length_two_outputs =',625-len(seen))
    print('F25_nonsquare_discriminant_outputs =',cnt)

if __name__=='__main__':main()
