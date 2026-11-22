from itertools import product
from collections import Counter

def cmul(a,b,fieldmul):
    s,u,v,t=a[0],a[1:4],a[4:7],a[7]
    h,x,y,k=b[0],b[1:4],b[4:7],b[7]
    mul=fieldmul
    dot=lambda A,B: mul(A[0],B[0])^mul(A[1],B[1])^mul(A[2],B[2])
    cross=lambda A,B: [mul(A[1],B[2])^mul(A[2],B[1]),mul(A[2],B[0])^mul(A[0],B[2]),mul(A[0],B[1])^mul(A[1],B[0])]
    xx=cross(v,y);yy=cross(u,x)
    return (mul(s,h)^dot(u,y),*[mul(s,x[i])^mul(k,u[i])^xx[i] for i in range(3)],*[mul(h,v[i])^mul(t,y[i])^yy[i] for i in range(3)],mul(t,k)^dot(v,x))

def calculate(q,exhaustive=False):
    if q==2: fm=lambda a,b:a&b
    elif q==4:
        def fm(a,b):
            p=0
            for i in range(2):
                for j in range(2):
                    if ((a>>i)&1) and ((b>>j)&1):p ^= 1<<(i+j)
            if p&8:p ^= 8^2^1
            if p&4:p ^= 4^2^1
            return p
    else:raise ValueError
    if exhaustive:
        elems=list(product(range(q),repeat=8)); cnt=Counter()
        for a in elems:
            for b in elems:
                ab=cmul(a,b,fm);ba=cmul(b,a,fm)
                z=tuple(x^y for x,y in zip(ab,ba)); cnt[z]+=1
        assert len(cnt)==q**7
        for z,c in cnt.items():
            assert z[0]==z[7]
            if all(z[i]==0 for i in range(8)):expected=q**13+q**10-q**7
            elif all(z[i]==0 for i in range(1,7)):expected=q**13-q**7
            else:expected=(q*q-1)*q**7
            assert c==expected,(z,c,expected)
        assert q**13+q**10-q**7+(q-1)*(q**13-q**7)+(q**7-q)*(q*q-1)*q**7==q**16
        print('FULL',q,'elements',len(elems),'ordered pairs',q**16,'commutator fibers',len(cnt), 'zero',cnt[(0,)*8], 'OK')
    else:
        from random import Random
        rr=Random(925)
        for j in range(15000):
            a=tuple(rr.randrange(q) for i in range(8));b=tuple(rr.randrange(q) for i in range(8))
            ab=cmul(a,b,fm);ba=cmul(b,a,fm);z=tuple(x^y for x,y in zip(ab,ba))
            alpha=a[0]^a[7];beta=b[0]^b[7];w=a[1:7];t=b[1:7]
            scalar=0
            for i in range(3):scalar^=fm(w[i],t[i+3])^fm(w[i+3],t[i])
            target=(scalar,*[fm(alpha,t[i])^fm(beta,w[i]) for i in range(6)],scalar)
            assert z==target,(z,target)
        print('SAMPLES',q,15000,'commutator formula OK')
if __name__=='__main__':
    calculate(2,True)
    calculate(4,False)
