"""Independent finite-field instances for short Gorenstein ring zero-divisor graphs.
Science-only executable; no external dependencies.
"""
from itertools import product
from collections import Counter

def mul(a,b,q):
    if q==4:
        c=0
        for i in range(2):
            for j in range(2):
                if (a>>i)&1 and (b>>j)&1: c ^= 1<<(i+j)
        if c&8: c^=0b1100
        if c&4: c^=0b111
        return c
    return a*b%q

def add(a,b,q):return a^b if q==4 or q==2 else (a+b)%q

def diag_matrix(diag,q):return [[diag[i] if i==j else 0 for j in range(len(diag))] for i in range(len(diag))]
def alt_matrix(d):return [[1 if (i^1)==j and i//2==j//2 else 0 for j in range(d)] for i in range(d)]
def bilinear(v,w,M,q):
    s=0
    for i in range(len(v)):
        for j in range(len(w)):
            s=add(s,mul(mul(v[i],M[i][j],q),w[j],q),q)
    return s

def counts(q,M):
    d=len(M); V=[v for v in product(range(q),repeat=d) if any(v)]; base=q*(q**(d-1)-1)+(q-1)
    z=sum(bilinear(v,v,M,q)==0 for v in V)
    # Full direct graph from ring product.  Fq*V + Fqz ring, elements of m are (v,t).
    X=[(v,t) for v in V for t in range(q)]; X+= [((0,)*d,t) for t in range(1,q)]
    degrees=Counter(); edges=0
    for i,x in enumerate(X):
        for y in X[i+1:]:
            if bilinear(x[0],y[0],M,q)==0:
                edges+=1; degrees[i]+=1;degrees[X.index(y)]+=1
    predicted= ((q-1)*(q-2)//2 +(q-1)*q*(q**d-1)+ (q*q*(q**d-1)*(q**(d-1)-1)-q*z)//2)
    assert edges==predicted,(q,d,edges,predicted)
    observed=Counter(degrees.values())
    predicted_degrees=Counter({q**(d+1)-2:q-1,base-1:q*z,base:q*(q**d-1-z)})
    assert observed==predicted_degrees,(q,d,observed,predicted_degrees)
    return len(X),edges,z,sorted(observed.items())

def main():
    cases=[(2,diag_matrix([1]*3,2),'odd binary'), (2,diag_matrix([1]*4,2),'even binary nonalternating'), (2,alt_matrix(4),'even binary alternating'),(3,diag_matrix([1]*3,3),'odd ternary square det'),(3,diag_matrix([1,1,2],3),'odd ternary nonsquare det'),(3,diag_matrix([1]*4,3),'even ternary split'),(3,diag_matrix([1,1,1,2],3),'even ternary nonsplit'),(4,diag_matrix([1]*3,4),'odd quaternary'),(4,diag_matrix([1]*4,4),'even quaternary nonalternating'),(4,alt_matrix(4),'even quaternary alternating')]
    for q,M,name in cases:
        result=counts(q,M)
        d=len(M); z=result[2]
        if d%2: target=q**(d-1)-1
        elif q%2==0: target=q**d-1 if 'alternating'==name.split()[-1] and 'nonalternating' not in name else q**(d-1)-1
        else: target=None
        if target is not None:assert z==target,(q,d,z,target)
        print('PASS',name,'q=',q,'d=',d,'vertices=',result[0],'edges=',result[1],'isotropic=',z,'degrees=',result[3])
    print('VERIFY_OK cases=',len(cases))
if __name__=='__main__':main()
