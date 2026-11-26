"""Independent centralizer enumeration for 2x2 matrices over F_p[e_1,...,e_d]/(e_ie_j)."""
from itertools import product
from collections import Counter

# Coefficients are grouped by ring layer; each layer is a 2x2 matrix in row-major order.
def mm(A,B,p):
    return tuple((A[2*(i//2)]*B[i%2]+A[2*(i//2)+1]*B[2+i%2])%p for i in range(4))

def subtract(A,B,p):return tuple((x-y)%p for x,y in zip(A,B))

def comm(A,B,p,d):
    ab=subtract(mm(A[:4],B[:4],p),mm(B[:4],A[:4],p),p)
    output=list(ab)
    for i in range(d):
        off=4*(i+1)
        a0,a1=A[:4],A[off:off+4]
        b0,b1=B[:4],B[off:off+4]
        ab1=mm(a0,b1,p); ab2=mm(a1,b0,p); ba1=mm(b0,a1,p);ba2=mm(b1,a0,p)
        output.extend((ab1[k]+ab2[k]-ba1[k]-ba2[k])%p for k in range(4))
    return output

def rank(mat,p):
    n=len(mat); m=len(mat[0]);r=0
    for j in range(m):
        k=next((i for i in range(r,n) if mat[i][j]%p),None)
        if k is None:continue
        mat[r],mat[k]=mat[k],mat[r]
        z=pow(mat[r][j],-1,p)
        mat[r]=[(z*t)%p for t in mat[r]]
        for i in range(r+1,n):
            z=mat[i][j]
            if z:mat[i]=[(x-z*y)%p for x,y in zip(mat[i],mat[r])]
        r+=1
        if r==n:break
    return r

def census(p,d):
    N=4*(d+1)
    basis=[]
    for j in range(N):
        e=[0]*N;e[j]=1;basis.append(e)
    counts=Counter()
    for A in product(range(p),repeat=N):
        columns=[comm(A,e,p,d) for e in basis]
        M=[[columns[j][i] for j in range(N)] for i in range(N)]
        counts[p**(N-rank(M,p))]+=1
    q=p
    B=(q*q+q+1)*(q**(2*d)-q**d)
    prediction={q**(2*d+2):(q**4-q)*q**(4*d),q**(4*d+4):q**(d+1),q**(4*d+2):q*B,q**(4*d+1):q*(q**(4*d)-q**d-B)}
    prediction={k:v for k,v in prediction.items() if v}
    assert counts==prediction,(p,d,counts,prediction)
    print('PASS p=',p,'d=',d,'elements=',p**N,'counts=',dict(sorted(counts.items())),'commuting_pairs=',sum(a*b for a,b in counts.items()))

def brute_pairs(p,d):
    N=4*(d+1)
    elems=list(product(range(p),repeat=N))
    if len(elems)>256: return
    count=0
    for A in elems:
        count+=sum(1 for B in elems if not any(comm(A,B,p,d)))
    q=p;v=q*q+q+1
    predicted=((q**4-q)*q**(6*d+2)+q**(4*d+2)*(q**(4*d)-q**d+(q-1)*v*(q**(2*d)-q**d))+q**(5*d+5))
    assert count==predicted,(count,predicted)
    print('PASS_DIRECT_PAIRS',p,d,count)

if __name__=='__main__':
    for p,d in ((2,1),(2,2),(3,1)):
        census(p,d)
    brute_pairs(2,1)
    print('VERIFY_OK')
