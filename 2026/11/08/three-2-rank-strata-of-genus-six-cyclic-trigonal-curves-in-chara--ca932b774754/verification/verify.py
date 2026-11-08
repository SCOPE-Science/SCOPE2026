"""Exact GF(4) checks for a genus-six cyclic trigonal curve in characteristic two.
No external dependencies.
"""
from itertools import product

# GF(4) = F2[t]/(t*t+t+1).  Integers encode the polynomial basis 1,t.
def add(a,b): return a^b
def mul(a,b):
    z=0
    for i in range(2):
        if (b>>i)&1: z^=a<<i
    if z&8: z^=0b11100 # unused for field elems of degree <2
    if z&4: z^=0b111
    return z

def square(a):return mul(a,a)
def root(a):return square(a)
def inverse(a):
    if a==0: raise ZeroDivisionError
    return mul(a,a)

def ptrim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def pmod(a,b):
    a=ptrim(a[:]); b=ptrim(b[:]);
    while len(a)>=len(b) and a !=[0]:
        t=mul(a[-1],inverse(b[-1])); d=len(a)-len(b)
        for i in range(len(b)): a[d+i]^=mul(t,b[i])
        ptrim(a)
    return a

def sqfree(c):
    # c indexed a0,...,a6, lead a7=1
    f=list(c)+[1]
    d=[f[i] if i%2 else 0 for i in range(1,len(f))]
    d=ptrim(d)
    if d==[0]:return False
    u=ptrim(f);v=d
    while v != [0]:u,v=v,pmod(u,v)
    return len(u)==1

def matmul(A,B):
    n=len(A); out=[[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k]:
                for j in range(n):out[i][j]^=mul(A[i][k],B[k][j])
    return out

def rank(A):
    B=[row[:] for row in A]; m=len(B); n=len(B[0]); j=0;r=0
    while j<n and r<m:
        pivot=next((i for i in range(r,m) if B[i][j]),None)
        if pivot is None:j+=1;continue
        B[r],B[pivot]=B[pivot],B[r]
        inv=inverse(B[r][j]);B[r]=[mul(v,inv) for v in B[r]]
        for i in range(m):
            if i!=r and B[i][j]:
                factor=B[i][j];B[i]=[x^mul(factor,y) for x,y in zip(B[i],B[r])]
        j+=1;r+=1
    return r

def matrix(c):
    M=[[0]*6 for _ in range(6)]
    M[2][0]=root(c[1]);M[3][0]=root(c[3]);M[4][0]=root(c[5]);M[5][0]=1
    M[2][1]=root(c[0]);M[3][1]=root(c[2]);M[4][1]=root(c[4]);M[5][1]=root(c[6])
    M[0][3]=1; M[1][5]=1
    return M

def ranks(c):
    M=matrix(c);cur=M; result=[]
    for i in range(1,7):
        result.append(rank(cur))
        cur=matmul(M,[[root(v) for v in row] for row in cur])
    return result

def target(c):
    det=c[2]^mul(c[3],c[6])
    if det:return (4,[4]*6)
    if c[3]==square(square(c[6])) and c[2]==mul(c[3],c[6]):return (0,[4,3,2,1,0,0])
    return (2,[4,3,2,2,2,2])

def main():
    print('GF4 square/inverse tables:', [(v,square(v),inverse(v) if v else None) for v in range(4)])
    for a in range(4):
        for b in range(4):
            for c in range(4):
                assert mul(a,b^c)==mul(a,b)^mul(a,c)
        if a: assert mul(a,inverse(a))==1
    sample={4:None,2:None,0:None}; tallies={0:0,2:0,4:0}
    for c in product(range(4),repeat=7):
        if not sqfree(c):continue
        expected=target(c);got=ranks(c)
        assert got==expected[1],(c,got,expected)
        tallies[expected[0]]+=1
        if sample[expected[0]] is None:sample[expected[0]]=c
    assert all(tallies.values())
    print('EXHAUSTIVE_F4_SQUAREFREE_COUNTS',tallies)
    print('REPRESENTATIVE_COEFFICIENTS',sample)
    # exact witnesses over F2, c=(a0,...,a6)
    for want,c in [(4,(1,0,1,0,0,0,0)),(2,(1,0,0,1,0,0,0)),(0,(1,1,0,0,0,0,0))]:
        assert sqfree(c)
        assert target(c)[0]==want
        assert ranks(c)==target(c)[1]
        print('EXACT_F2_WITNESS',want,list(c),ranks(c))
    # A larger extension tests fourth powers that are nontrivial modulo 8.
    gf8_suite()
    print('ALL_CHECKS_PASSED')
def gf8_suite():
    def gf8mul(a,b):
        z=0
        for i in range(3):
            if (b>>i)&1:z^=a<<i
        for i in (4,3):
            if (z>>i)&1:z^=0b1011<<(i-3)
        return z
    def gf8square(x):return gf8mul(x,x)
    def gf8root(x):return gf8square(gf8square(x))
    def gf8inv(a):
        if a==0:raise ZeroDivisionError
        result=1
        for _ in range(6):result=gf8mul(result,a)
        return result
    global mul,square,root,inverse
    mul=gf8mul;square=gf8square;root=gf8root;inverse=gf8inv
    for a in range(8):
        if a: assert mul(a,inverse(a))==1
        assert square(root(a))==a
    checked=0
    for a6 in range(8):
        a3=square(square(a6));a2=mul(a3,a6)
        found=0
        for a1,a0 in product(range(8),repeat=2):
            c=(a0,a1,a2,a3,0,0,a6)
            if sqfree(c):
                assert ranks(c)==[4,3,2,1,0,0],(c,ranks(c))
                checked+=1;found+=1
        assert found>0,a6
    # cover the other strata in the extension too
    for x in range(8):
        for y in range(8):
            for z in range(8):
                c=(1,(x^y),z,x,0,0,y)
                if not sqfree(c):continue
                expected=target(c)
                assert ranks(c)==expected[1],(c,ranks(c),expected)
                checked+=1
    print('GF8_EXACT_TESTS',checked)
if __name__=='__main__': main()
