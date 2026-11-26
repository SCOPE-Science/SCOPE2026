"""Direct finite-field checks for a Heisenberg-to-niltriangular Hom variety.
Public-domain-style standalone implementation; Python 3 standard library only.
The polynomial conditions are checked against actual 4-by-4 matrix brackets.
"""
from itertools import product

def field(q):
    if q == 4:
        def add(a,b): return a ^ b
        def mul(a,b):
            t=0
            while b:
                if b&1:t^=a
                b>>=1;a<<=1
                if a&4:a^=7
            return t
        def neg(a):return a
    else:
        def add(a,b):return (a+b)%q
        def mul(a,b):return a*b%q
        def neg(a):return -a%q
    def sub(a,b):return add(a,neg(b))
    return add,mul,sub

def matrices(vals):
    a,b,c,d,e,f=vals
    return ((0,a,d,f),(0,0,b,e),(0,0,0,c),(0,0,0,0))

def bracket(X,Y,add,mul,sub):
    return tuple(tuple(sub(sum_field((mul(X[i][k],Y[k][j]) for k in range(4)),add),
                         sum_field((mul(Y[i][k],X[k][j]) for k in range(4)),add))
                       for j in range(4)) for i in range(4))

def sum_field(it,add):
    s=0
    for x in it:s=add(s,x)
    return s

def run(q):
    add,mul,sub=field(q)
    count=0
    for a,b,c,A,B,C in product(range(q),repeat=6):
        p=sub(mul(a,B),mul(A,b))
        v=sub(mul(b,C),mul(B,c))
        expected=(sub(mul(a,v),mul(c,p))==0 and sub(mul(A,v),mul(C,p))==0)
        # Compute the two actual iterated Lie brackets, without using p or v.
        X=matrices((a,b,c,0,0,0));Y=matrices((A,B,C,0,0,0))
        Z=bracket(X,Y,add,mul,sub)
        actual=(not any(y for row in bracket(X,Z,add,mul,sub) for y in row)
                and not any(y for row in bracket(Y,Z,add,mul,sub) for y in row))
        assert expected==actual,(q,a,b,c,A,B,C)
        count+=actual
    target=((q**5+2*q**4-2*q**3-q**2+q) if q%2==0
            else (4*q**4-2*q**3-3*q**2+2*q))
    assert count==target,(q,count,target)
    print(f'q={q}: base={count}, total={count*q**6}, expected={target*q**6}: PASS')

if __name__=='__main__':
    for q in (2,3,4,5):run(q)
    print('HEISENBERG_N4_HOMVAR_OK')
