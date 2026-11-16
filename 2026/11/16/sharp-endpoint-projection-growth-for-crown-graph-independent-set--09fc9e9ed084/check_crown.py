"""Exact, independent Walsh checks for crown-graph independent-set convolution.

Run: python check_crown.py
Requires Python 3 standard library only.
"""
from math import comb, isclose

def fwht(v):
    v = v[:]
    h = 1
    while h < len(v):
        for base in range(0,len(v),2*h):
            for j in range(h):
                a,b=v[base+j],v[base+j+h]
                v[base+j],v[base+j+h]=a+b,a-b
        h*=2
    return v

def mask_val(n,u,v):
    return ((1<<n) if u==0 else 0)+((1<<n) if v==0 else 0)-1+n-2*(u^v).bit_count()

def kraw(n,r,t):
    return sum((-1)**j*comb(t,j)*comb(n-t,r-j)
               for j in range(max(0,r-(n-t)),min(r,t)+1))

def kernel_zero(n,x,y):
    A=1<<n; r=(n-1)//2
    return ((A if x==y else 0)*kraw(n,r,y.bit_count())
           -kraw(n,r,x.bit_count())-kraw(n,r,y.bit_count()))

def norm_num(n):
    A=1<<n;r=(n-1)//2;B=comb(n,r)
    vals=[kraw(n,r,t) for t in range(n+1)]
    L=sum(comb(n,t)*abs(vals[t]) for t in range(n+1))
    D=sum(comb(n,i)*comb(n,j)*abs(vals[i]+vals[j]) for i in range(n+1) for j in range(n+1))
    return A*A+D+(A-4)*L-2*(A-2)*B

def run():
    count=0
    for n in range(3,8):
        A=1<<n
        f=[]
        for v in range(A):
            for u in range(A):
                yes=(u==0 or v==0 or (u.bit_count()==v.bit_count()==1 and u==v))
                f.append(int(yes))
        W=fwht(f)
        for v in range(A):
            for u in range(A):
                assert W[v*A+u]==mask_val(n,u,v),(n,u,v,W[v*A+u],mask_val(n,u,v))
                count+=1
        zeros=sum(w==0 for w in W)
        expected=(A-2)*comb(n,(n-1)//2) if n%2 else 0
        assert zeros==expected,(n,zeros,expected)
        gap=min(abs(w) for w in W if w)
        assert gap==(2 if n%2 else 1),(n,gap)
        if n%2:
            r=(n-1)//2
            for t in range(n+1):
                predicted=((-1)**(t//2)*comb(n,r)*comb((n-1)//2,t//2))//comb(n,t)
                assert predicted==kraw(n,r,t),(n,t,predicted,kraw(n,r,t))
            assert sum(comb(n,t)*abs(kraw(n,r,t)) for t in range(n+1))==2**((n+1)//2)*comb(n,r)
            if n<=5:
                zero_mask=[int(w==0) for w in W]
                # Inverse Walsh transform: Q(x,y)=4^(-n) sum_{zero frequencies} (-1)^(ux+vy).
                Q_num=fwht(zero_mask)
                norm_num_direct=0
                for y in range(A):
                    for x in range(A):
                        q=Q_num[y*A+x]
                        assert q==kernel_zero(n,x,y),(n,x,y,q,kernel_zero(n,x,y))
                        norm_num_direct+=abs((A*A if (x==y==0) else 0)-q)
                assert norm_num_direct==norm_num(n),(n,norm_num_direct,norm_num(n))
            print('n=',n,'independent_sets=',sum(f),'zeros=',zeros,'gap=',gap,'projection_norm=',f'{norm_num(n)}/{A*A}')
        else:
            print('n=',n,'independent_sets=',sum(f),'zeros=',zeros,'gap=',gap,'projection_norm=1')
    print('CROWN_WALSH_PROJECTION_EXACT_PASS coefficients=',count)

if __name__=='__main__':run()
