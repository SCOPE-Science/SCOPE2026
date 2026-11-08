"""Independent exact computation of the F_5 and F_25 points of y^2=x^9+3*x^3+2*x.

Represent F_25=F_5[w]/(w^2-2). The quadratic character of z in
F_25 equals the quadratic character of Norm(z) in F_5.
"""
P=5

def add(u,v):
    return ((u[0]+v[0])%P,(u[1]+v[1])%P)

def times(u,v):
    a,b=u;c,d=v
    return ((a*c+2*b*d)%P,(a*d+b*c)%P)

def power(u,n):
    v=(1,0)
    while n:
        if n&1:v=times(v,u)
        u=times(u,u);n>>=1
    return v

def f(x):
    return add(add(power(x,9),times((3,0),power(x,3))),times((2,0),x))

def norm(x):
    a,b=x
    return (a*a-2*b*b)%P

def chi(x):
    if x==0:return 0
    if x in {1,4}:return 1
    return -1

if __name__=='__main__':
    norm_table=[[norm(f((a,b))) for a in range(5)] for b in range(5)]
    character_table=[[chi(v) for v in row] for row in norm_table]
    assert character_table[0]==[0,1,0,0,1]
    assert all(row==[-1]*5 for row in character_table[1:])
    assert norm_table==[[0,1,0,0,1],[3,3,3,3,3],[3,2,2,2,2],
                        [3,2,2,2,2],[3,3,3,3,3]]
    n25=26+sum(sum(row) for row in character_table)
    n5=6+sum(chi((a**9+3*a**3+2*a)%5) for a in range(5))
    assert n25==8 and n5==8
    # Nonzero roots of f and f' would force t=x^2=3, but 3^4+3*3+2=2 !=0.
    assert (3**4+3*3+2)%5==2
    assert 2%5!=0  # derivative at x=0
    print('N1=',n5,'N2=',n25,'B2=',(n25-n5)//2)
    print('Norm rows:',norm_table)
    print('Quadratic-character rows:',character_table)
    print('VERIFIED_F25')
