"""Executable finite tests of the Bernstein--Kantorovich BV mixing formulas.
Requires only Python 3 standard library. The infinite-dimensional proof is in RESULT.md.
"""
from fractions import Fraction as Q
from math import comb

def transition(n):
    m=n+1
    out=[]
    for i in range(m):
        row=[]
        for j in range(m):
            v=Q(0)
            for k in range(n-j+1):
                p=j+k+1
                v+=Q(m*comb(n,j)*comb(n-j,k)*(-1)**k,p)*(Q(i+1,m)**p-Q(i,m)**p)
            row.append(v)
        out.append(row)
    return out

def dot(a,b):return sum((x*y for x,y in zip(a,b)),Q(0))
def mv(M,v):return [dot(row,v) for row in M]

def linear_solve(A,b):
    rows=[list(row)+[bi] for row,bi in zip(A,b)];m=len(rows)
    for k in range(m):
        p=next(i for i in range(k,m) if rows[i][k])
        rows[k],rows[p]=rows[p],rows[k]
        d=rows[k][k];rows[k]=[x/d for x in rows[k]]
        for i in range(m):
            if i==k:continue
            d=rows[i][k]
            if d:rows[i]=[x-d*y for x,y in zip(rows[i],rows[k])]
    return [r[-1] for r in rows]

def dual(n,M):
    m=n+1; lam=Q(n,m);h=[Q(i)-Q(n,2) for i in range(m)]
    A=[[M[j][i]-(lam if i==j else Q(0)) for j in range(m)] for i in range(m)]
    A[-1]=h
    b=[Q(0)]*(m-1)+[Q(1)]
    w=linear_solve(A,b)
    assert mv([[M[j][i] for j in range(m)] for i in range(m)],w)==[lam*t for t in w]
    return w

def leading(n,M=None):
    M=M or transition(n);m=n+1;lam=Q(n,m)
    w=dual(n,M)
    partial=[abs(sum(w[:j],Q(0))) for j in range(1,m)]
    optimal=[j for j,p in enumerate(partial,1) if p==max(partial)]
    return Q(n,4)/lam*max(partial),optimal,w

def bernstein(n,x):return [comb(n,i)*x**i*(1-x)**(n-i) for i in range(n+1)]
def integrated_basis(n,j,x):
    return comb(n,j)*sum(comb(n-j,k)*(-1)**k*x**(j+k+1)/(j+k+1) for k in range(n-j+1))

def exact_step_coeffs(n,r,j,M):
    v=[Q(int(i<j)) for i in range(n+1)]
    for _ in range(r-1):v=mv(M,v)
    return v

def step_l1(n,r,j,M):
    c=exact_step_coeffs(n,r,j,M)
    theta=j/(n+1)
    def h(x):return sum(float(v)*b for v,b in zip(c,bernstein(n,x)))-theta
    assert h(0)>0 and h(1)<0
    lo,hi=0.0,1.0
    for _ in range(65):
        mid=(lo+hi)/2
        if h(mid)>0:lo=mid
        else:hi=mid
    z=(lo+hi)/2
    return 2*(sum(float(v)*integrated_basis(n,i,z) for i,v in enumerate(c))-theta*z)

def sharp(n,r,M):
    values=[step_l1(n,r,j,M) for j in range(1,n+1)]
    jmax=1+max(range(n),key=lambda k:values[k])
    return values[jmax-1],jmax,values

def main():
    checks=0
    results=[]
    for n in range(1,9):
        M=transition(n);m=n+1
        assert all(sum(row)==1 for row in M)
        assert all(sum(M[i][j] for i in range(m))==1 for j in range(m))
        assert all(M[i][j]==M[n-i][n-j] for i in range(m) for j in range(m))
        h=[Q(i)-Q(n,2) for i in range(m)];lam=Q(n,m)
        assert mv(M,h)==[lam*t for t in h]
        A,central,w=leading(n,M)
        expected=[m//2] if m%2==0 else [m//2,(m+1)//2]
        assert central==expected,(n,central,expected)
        assert all(w[i]<0 for i in range((n+1)//2))
        assert all(w[i]==-w[n-i] for i in range(m))
        checks+=6*m
        for r in [1,2,3,5,8,13]:
            v,j,values=sharp(n,r,M)
            assert v>0 and all(abs(values[k]-values[n-k-1])<2e-10 for k in range(n))
            checks+=n+2
        last,j,_=sharp(n,42,M)
        if n>=2:
            assert abs(last/float(lam)**42-float(A))<1e-5,(n,last,float(A)*float(lam)**42)
        else:
            assert abs(last-float(A)*float(lam)**42)<1e-11
        checks+=1
        results.append((n,str(A),central,round(sharp(n,1,M)[0],9)))
    assert [a for n,a,j,v in results[:5]]==['1/2','3/8','17/42','115/304','413/1060']
    print('PASS',checks,'counted finite check units')
    print('n, rational A_n, eventual grid-step indices, C_(n,1):')
    for row in results:print(*row)

if __name__=='__main__':main()
