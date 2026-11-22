from math import gcd

def matching(M,N,H,V):
    assert M>=3 and N>=3 and 0<=H<=M and 0<=V<=N and N*H+M*V<=M*N
    s=gcd(H,V)
    if s==0: return {(i,j):'d' for i in range(M) for j in range(N)}
    p,q=H//s,V//s
    B=p*N+q*M
    assert s*B<=M*N
    labels={}
    for i in range(M):
        for j in range(N):
            z=(p*N*i+q*M*j)%(M*N)
            if z>=s*B: labels[(i,j)]='d'
            elif z%B<q*M: labels[(i,j)]='v'
            else: labels[(i,j)]='h'
    return labels

def test(M,N,H,V):
 t=matching(M,N,H,V)
 images=[]
 for (i,j),w in t.items():
  images.append(((i+(w=='v'))%M,(j-(w=='h'))%N))
 assert len(set(images))==M*N,(M,N,H,V,'not bijection')
 assert sum(x=='v' for x in t.values())==M*V,(M,N,H,V,'v')
 assert sum(x=='h' for x in t.values())==N*H,(M,N,H,V,'h')
 for j in range(N): assert sum(t[(i,j)]=='h' for i in range(M))==H
 for i in range(M): assert sum(t[(i,j)]=='v' for j in range(N))==V
 return True
# The constructive enumerator above uses only the Python standard library.
# For an independent polynomial comparison, Newton's identities compute
# the signed determinant coefficients in the finite honeycomb model.
def independent_slope_counts(M, N):
    from math import comb
    power_sums = []
    for k in range(1, M + 1):
        power_sums.append({j: M * comb(N*k, j*M) * (-1)**(N*k-j*M)
                           for j in range(N*k//M + 1)})
    elementary = [{0:1}]
    for p in range(1, M + 1):
        accum = {}
        for k in range(1,p+1):
            for a,va in elementary[p-k].items():
                for b,vb in power_sums[k-1].items():
                    accum[a+b] = accum.get(a+b,0) + (-1)**(k-1)*va*vb
        assert all(z%p==0 for z in accum.values())
        elementary.append({a:z//p for a,z in accum.items() if z})
    return {(H,V):abs(elementary[M-H].get(V,0))
            for H in range(M+1) for V in range(N+1)}


def run_all():
    from math import comb, gcd
    checked = 0
    for M in range(3, 26):
        for N in range(3, 26):
            for H in range(M+1):
                for V in range(N+1):
                    if N*H + M*V <= M*N:
                        test(M,N,H,V)
                        checked += 1
    assert checked == 60438,checked
    count_checks=0
    for M in range(3,16):
        for N in range(3,16):
            table=independent_slope_counts(M,N)
            for H in range(M+1):
                for V in range(N+1):
                    feasible=N*H+M*V<=M*N
                    actual=table[(H,V)]
                    assert (actual>0)==feasible,(M,N,H,V)
                    if feasible and H+V>0:
                        s=gcd(H,V)
                        p,q=H//s,V//s
                        B=p*N+q*M
                        lower=comb(M*N//B,s)
                        assert actual>=lower,(M,N,H,V,'binomial',actual,lower)
                        g=gcd(p*N,q*M,M*N)
                        if s*B<M*N:
                            assert actual>=M*N//g,(M,N,H,V,'orbit')
                    count_checks+=1
    assert count_checks == 16900,count_checks
    print('PASS: 60438 direct constructive cases, 16900 independent determinant coefficients, two certified lower bounds')

if __name__=='__main__':
    run_all()
