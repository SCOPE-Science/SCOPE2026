"""Exact-rational checks of a symplectic polygon pair's dyadic return rules.

Run with Python 3.9+: python CHECK.py. Finite checks support, not replace, proof.
"""
from fractions import Fraction as F
S = [(F(0),F(0)),(F(4),F(0)),(F(4),F(4)),(F(0),F(4))]
R = [(F(6),F(5)),(F(8),F(1)),(F(12),F(-1)),(F(10),F(3))]

def diff(a,b): return (a[0]-b[0], a[1]-b[1])
def summ(a,b): return (a[0]+b[0], a[1]+b[1])
def mul(a,t): return (a[0]*t,a[1]*t)
def det(a,b): return a[0]*b[1]-a[1]*b[0]
def edge(P,i): return diff(P[(i+1)%4],P[i])
def point(P,i,u): return summ(P[i],mul(edge(P,i),u))
def param(P,i,z):
    d=edge(P,i); w=diff(z,P[i]); assert det(d,w)==0
    q=w[0]/d[0] if d[0] else w[1]/d[1]
    assert F(0)<q<F(1)
    return q

def advance(x,y,P,Q,i,j):
    # Chord through x is parallel to edge j of Q, and z belongs to P.
    d=edge(Q,j); hits=[]
    for k in range(4):
        e=edge(P,k); den=det(d,e)
        if not den:continue
        a=diff(P[k],x)
        tau=det(a,e)/den
        t=det(a,d)/den
        if 0<t<1 and tau!=0:hits.append((k,summ(x,mul(d,tau))))
    assert len(hits)==1,(P,Q,i,j,x,y,hits)
    k,z=hits[0]
    return y,z,Q,P,j,k

def run_initial(i,j,m,n):
    # Deliberately off dyadic cut values, in each exact dyadic cell.
    u=F(5,3*2**(m+1)); v=F(7,4*2**(n+1))
    assert F(1,2**(m+1))<u<F(1,2**m)
    assert F(1,2**(n+1))<v<F(1,2**n)
    s=u if not i%2 else 1-u
    t=v if not j%2 else 1-v
    x,y=point(S,i,s),point(R,j,t)
    expected=8*(m+n+(i+j)%2)+4
    start=(x,y)
    seq=[]
    P,Q=S,R;ii,jj=i,j
    for k in range(expected):
        if k%2==0:
            seq.append((x,y,ii,jj,P is S))
        x,y,P,Q,ii,jj=advance(x,y,P,Q,ii,jj)
        if (x,y)==start:
            assert k+1==expected,(i,j,m,n,k+1,expected)
            break
    else:raise AssertionError(('no return',i,j,m,n))
    return len(seq)

def check_two_step(i,j,m,n):
    u=F(5,3*2**(m+1));v=F(7,4*2**(n+1))
    x,y=point(S,i,u if not i%2 else 1-u),point(R,j,v if not j%2 else 1-v)
    x,y,P,Q,ii,jj=advance(x,y,S,R,i,j)
    x,y,P,Q,ii,jj=advance(x,y,P,Q,ii,jj)
    assert P is S and Q is R
    u2=param(S,ii,x);v2=param(R,jj,y)
    u2=u2 if ii%2==0 else 1-u2
    v2=v2 if jj%2==0 else 1-v2
    q=lambda a:(a+(-1 if a%2==0 else 1))%4
    h=lambda a:(a+2)%4
    if (i+j)%2==0:
        if m:
            ex=(q(i),q(j),2*u,v/2)
        elif n:
            ex=(h(i),q(j),F(3,2)-u,2*v)
        else:
            ex=(h(i),h(j),F(3,2)-u,F(3,2)-v)
    else:
        if n:
            ex=(q(i),q(j),u/2,2*v)
        else:
            ex=(q(i),h(j),u/2,F(3,2)-v)
    assert (ii,jj,u2,v2)==ex,((i,j,m,n),(ii,jj,u2,v2),ex)

if __name__=='__main__':
    tests=0
    for i in range(4):
        for j in range(4):
            for m in range(5):
                for n in range(5):
                    check_two_step(i,j,m,n)
                    run_initial(i,j,m,n)
                    tests+=2
    # Exact area weights: eight same-parity pairs have area 16, and eight mixed pairs 8.
    assert all(abs(det(edge(S,i),edge(R,j)))==(16 if (i+j)%2==0 else 8) for i in range(4) for j in range(4))
    # Formula for 0<=K<=24 and its exact remaining mass.
    for M in range(25):
        p=sum((F(2*k+1,3*2**(k+1)) for k in range(M+1)),F(0))
        tail=F(2*M+5,3*2**(M+1))
        assert p+tail==1
    print('PASS:',tests,'exact-rational branch and primitive-period checks; 16 area weights; 25 exact distribution tails')
