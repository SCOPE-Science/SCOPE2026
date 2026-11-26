from fractions import Fraction as F

def matmul(A,B):
    n=len(A); m=len(B[0]); k=len(B)
    return [[sum(A[i][t]*B[t][j] for t in range(k)) for j in range(m)] for i in range(n)]

def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

def madd(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A))] for i in range(len(A))]

def mscale(c,A):
    return [[c*x for x in row] for row in A]

def inv(A):
    n=len(A); M=[row[:] + eye(n)[i] for i,row in enumerate(A)]
    for c in range(n):
        pivot=next(r for r in range(c,n) if M[r][c])
        M[c],M[pivot]=M[pivot],M[c]
        d=M[c][c]; M[c]=[x/d for x in M[c]]
        for r in range(n):
            if r==c: continue
            a=M[r][c]
            if a: M[r]=[M[r][j]-a*M[c][j] for j in range(2*n)]
    return [row[n:] for row in M]

def pade(L,h):
    n=len(L); I=eye(n); L2=matmul(L,L)
    num=madd(madd(I,mscale(-h/F(2),L)),mscale(h*h/F(12),L2))
    den=madd(madd(I,mscale(h/F(2),L)),mscale(h*h/F(12),L2))
    return matmul(num,inv(den))

def lap_complete_bipartite(p,q):
    n=p+q; L=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(p):
        L[i][i]=q
        for j in range(p,n): L[i][j]=L[j][i]=F(-1)
    for j in range(p,n): L[j][j]=p
    return L

def phi(x): return (x*x-F(6)*x+F(12))/(x*x+F(6)*x+F(12))

def check_kpq(p,q,h):
    M=pade(lap_complete_bipartite(p,q),h); n=p+q
    a=phi(q*h); b=phi(p*h); c=phi(n*h)
    cross=(F(1)-c)/n
    offp=(F(p)+F(q)*c-F(n)*a)/(p*n) if p>1 else None
    offq=(F(q)+F(p)*c-F(n)*b)/(q*n) if q>1 else None
    for i in range(p):
        for j in range(p,n): assert M[i][j]==cross
    if offp is not None:
        for i in range(p):
            for j in range(p):
                if i!=j: assert M[i][j]==offp
    if offq is not None:
        for i in range(p,n):
            for j in range(p,n):
                if i!=j: assert M[i][j]==offq
    assert all(sum(row)==1 for row in M)
    assert all(x>=0 for row in M for x in row)

def main():
    for p in range(1,5):
        for q in range(1,6):
            for h in (F(1,10),F(1),F(7,3),F(12)):
                check_kpq(p,q,h)
    L=[[F(1),F(-1),F(0),F(0)],
       [F(-1),F(2),F(-1),F(0)],
       [F(0),F(-1),F(2),F(-1)],
       [F(0),F(0),F(-1),F(1)]]
    M=pade(L,F(12))
    target=[[45505,-60,16776,22752],[-60,62341,5916,16776],[16776,5916,62341,-60],[22752,16776,-60,45505]]
    target=[[F(x,84973) for x in row] for row in target]
    assert M==target
    assert all(sum(row)==1 for row in M)
    assert M[0][1]==F(-60,84973)
    def g(x): return x**4-6*x**3-60*x**2-108*x-72
    assert g(F(11))<0 and g(F(12))>0
    print('VERIFY_OK')

if __name__=='__main__': main()
