"""Exact independent finite-field counts and zeta numerator for y^2=x^9+3*x^3+2*x.

Uses polynomial basis with separately selected monic irreducible polynomials
of degrees 1, 2, 3 and 4. Standard-library Python only.
"""
P={1:[1,1],2:[1,1,1],3:[1,1,0,1],4:[4,1,0,0,1]}

def count_points(n):
    q=5**n;mod=P[n]
    vectors=[]
    for x in range(q):
        v=[];t=x
        for _ in range(n):v.append(t%5);t//=5
        vectors.append(v)
    def mul(x,y):
        a=vectors[x];b=vectors[y];c=[0]*(2*n-1)
        for i in range(n):
            for j in range(n):c[i+j]+=a[i]*b[j]
        for k in range(2*n-2,n-1,-1):
            z=c[k]%5
            for j in range(n):c[k-n+j]-=z*mod[j]
        return sum((c[i]%5)*5**i for i in range(n))
    def add(x,y):
        return sum(((vectors[x][i]+vectors[y][i])%5)*5**i for i in range(n))
    def scale(x,c):
        return sum((vectors[x][i]*c%5)*5**i for i in range(n))
    def power(x,k):
        r=1
        while k:
            if k&1:r=mul(r,x)
            x=mul(x,x);k>>=1
        return r
    # Check that all nonzero elements are units, hence this quotient is a field.
    assert all(power(x,q-1)==1 for x in range(1,q))
    squares={mul(x,x) for x in range(q)}
    assert len(squares)==(q+1)//2
    N=1;cnt=[0,0,0]
    for x in range(q):
        val=add(add(power(x,9),scale(power(x,3),3)),scale(x,2))
        if val==0:cnt[0]+=1;N+=1
        elif val in squares:cnt[1]+=1;N+=2
        else:cnt[2]+=1
    return N,tuple(cnt)

def multiply_polynomials(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):r[i+j]+=x*y
    return r

if __name__=='__main__':
    expected=[(8,(3,2,0)),(8,(3,2,20)),(152,(3,74,48)),(592,(3,294,328))]
    results=[count_points(n) for n in range(1,5)]
    assert results==expected,(results,expected)
    sums=[0]+[5**r+1-results[r-1][0] for r in range(1,5)]
    coeff=[1]
    for j in range(1,5):
        v=sum(coeff[j-i]*sums[i] for i in range(1,j+1))
        assert v%j==0
        coeff.append(-v//j)
    coeff+= [5**(j-4)*coeff[8-j] for j in range(5,9)]
    expected_coeff=[1,2,-7,-8,32,-40,-175,250,625]
    assert coeff==expected_coeff
    factor=multiply_polynomials(multiply_polynomials([1,-2,5],[1,4,5]),[1,0,-9,0,25])
    assert factor==expected_coeff
    for degree,(n,c) in enumerate(results,1):
        print('degree:',degree,'N:',n,'zero/square/nonsquare:',c)
    print('Zeta numerator:',coeff)
    print('VERIFIED_EXTENSIONS')
