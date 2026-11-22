"""Independent tensor-algebra check for nonsingular derivation counts of free rank-two nilpotent Lie algebras."""
from functools import lru_cache
from itertools import product


def lyndon(w):
    n=len(w)
    return all(w < w[i:]+w[:i] for i in range(1,n))

def lie_words(n):
    return [w for w in product((0,1),repeat=n) if lyndon(w)]

@lru_cache(None)
def bracket_word(w):
    if len(w)==1:
        return {w:1}
    suffixes=[i for i in range(1,len(w)) if lyndon(w[i:])]
    i=min(suffixes)
    a=bracket_word(w[:i]); b=bracket_word(w[i:])
    out={}
    for x,c in a.items():
        for y,d in b.items():
            xy=x+y; yx=y+x
            out[xy]=out.get(xy,0)+c*d
            out[yx]=out.get(yx,0)-c*d
    return {w:c for w,c in out.items() if c}

def inv_mod_matrix(A,p):
    n=len(A); M=[[v%p for v in row]+[int(i==j) for j in range(n)] for i,row in enumerate(A)]
    for col in range(n):
        piv=next((r for r in range(col,n) if M[r][col]%p),None)
        if piv is None: raise ValueError('singular basis')
        M[col],M[piv]=M[piv],M[col]
        t=pow(M[col][col],-1,p)
        M[col]=[(x*t)%p for x in M[col]]
        for r in range(n):
            if r!=col:
                f=M[r][col]
                M[r]=[(M[r][j]-f*M[col][j])%p for j in range(2*n)]
    return [row[n:] for row in M]

def det(M,p):
    n=len(M)
    if n==0:return 1
    A=[[v%p for v in row] for row in M]; out=1
    for i in range(n):
        pivot=next((r for r in range(i,n) if A[r][i]),None)
        if pivot is None:return 0
        if pivot!=i:
            A[i],A[pivot]=A[pivot],A[i]; out=-out
        a=A[i][i]; out=(out*a)%p
        t=pow(a,-1,p)
        for r in range(i+1,n):
            f=A[r][i]*t%p
            if f:
                for j in range(i,n):
                    A[r][j]=(A[r][j]-f*A[i][j])%p
    return out%p

def data_degree(n,p):
    words=list(product((0,1),repeat=n)); base=lie_words(n)
    B=[[bracket_word(u).get(w,0)%p for u in base] for w in words]
    piv=[]
    for r in range(len(words)):
        test=piv+[r]
        if rank_matrix([B[i] for i in test],p)>len(piv):piv=test
        if len(piv)==len(base):break
    assert len(piv)==len(base), (n,p)
    inv=inv_mod_matrix([B[i] for i in piv],p)
    return base,piv,inv

def rank_matrix(M,p):
    if not M:return 0
    A=[[x%p for x in row] for row in M]; m=len(A); n=len(A[0]); rr=0
    for j in range(n):
        ii=next((i for i in range(rr,m) if A[i][j]),None)
        if ii is None:continue
        A[rr],A[ii]=A[ii],A[rr]
        inv=pow(A[rr][j],-1,p)
        A[rr]=[x*inv%p for x in A[rr]]
        for i in range(rr+1,m):
            t=A[i][j]
            A[i]=[(a-t*b)%p for a,b in zip(A[i],A[rr])]
        rr+=1
        if rr==m:break
    return rr

def induced_det(n,p,A,degree_data):
    base,pivs,inv=degree_data
    words=list(product((0,1),repeat=n))
    k=len(base); matrix=[[0]*k for _ in range(k)]
    for col,w in enumerate(base):
        vec=bracket_word(w)
        dvec={}
        for word,co in vec.items():
            for pos,letter in enumerate(word):
                for new in (0,1):
                    ww=word[:pos]+(new,)+word[pos+1:]
                    dvec[ww]=(dvec.get(ww,0)+co*A[new][letter])%p
        vals=[dvec.get(words[br],0) for br in pivs]
        for row in range(k):
            matrix[row][col]=sum(inv[row][j]*vals[j] for j in range(k))%p
    return det(matrix,p)

def is_allowed(A,p,c):
    a,b=A[0];cc,d=A[1]
    t=(a+d)%p; detA=(a*d-b*cc)%p
    if not detA:return False
    for n in range(2,c+1):
        for i in range(1,n):
            j=n-i
            if i%p==0 and j%p==0:return False
    # brute test via polynomial recurrence on 2x2 matrix after quadratic extension,
    # using resultant for each i,j. For i and j nonzero mod p,
    # i*eigen1+j*eigen2 zero iff a certain polynomial in trace/det vanishes.
    # The product of the two conjugate weights is ij*t^2 + (i-j)^2*detA.
    for n in range(2,c+1):
        for i in range(1,n):
            j=n-i
            product_val=(i*j*t*t+(i-j)**2*detA)%p
            if not product_val:return False
    return True

def expected_count(q,c):
    p=q
    if c>=2*p:return 0
    E={(-j*pow(i,-1,p))%p for i in range(1,c) for j in range(1,c+1-i) if i%p and j%p}
    h=(q-1)-len(E)-(0 if 1 in E else 1)
    irr=q*q*(q-1)**2//2 if p==2 else q*(q-1)**3//2
    return irr+(q-1)*h*q*(q+1)//2 + ((q-1)*q*q if 1 not in E else 0)

def main():
    for q,maxc in ((2,4),(3,6),(5,5),(7,3)):
        dd={n:data_degree(n,q) for n in range(1,maxc+1)}
        for c in range(2,maxc+1):
            actual=0;from_resultant=0
            for a,b,cc,d in product(range(q),repeat=4):
                A=((a,b),(cc,d))
                independent=all(induced_det(n,q,A,dd[n]) for n in range(1,c+1))
                algebraic=is_allowed(A,q,c)
                assert independent==algebraic,(q,c,A,independent,algebraic)
                actual+=independent;from_resultant+=algebraic
            expected=expected_count(q,c)
            assert actual==expected,(q,c,actual,expected)
            print(f'q={q}, class={c}, admissible generator matrices={actual}, full proof formula={expected}, PASS')
    print('FREE_LIE_MODULAR_DERIVATION_CHECK_OK')

if __name__=='__main__':main()
