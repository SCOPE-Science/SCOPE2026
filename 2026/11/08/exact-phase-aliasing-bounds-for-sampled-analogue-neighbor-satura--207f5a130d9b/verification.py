"""Direct finite-state enumeration for periodic-history sampling identities."""
from math import gcd

def valid_count(phase, T, P, Y, H):
    last = T-Y-H
    return max(0, (last-phase)//P+1)

def run():
    checks=0
    for P in range(3,42):
        sequence=tuple(range(P))
        for K in range(1,6):
            for Y in range(1,4):
                for H in range(1,4):
                    T=(K-1)*P+Y+H
                    if T < Y+H: continue
                    admissible = list(range(0,T-Y-H+1))
                    count={p:sum(i%P==p for i in admissible) for p in range(P)}
                    assert all(count[p]==valid_count(p,T,P,Y,H) for p in range(P))
                    assert count[0]==K and all(count[p]==K-1 for p in range(1,P))
                    test=list(range(T,T+4*P))
                    exact=[count[j%P]>=K for j in test]
                    assert sum(exact)==4
                    for d in (1,2,P,2*P,P-1, max(1,P//2)):
                        g=gcd(P,d)
                        j0=K*P
                        phases=[(j0+t*d)%P for t in range(P//g)]
                        assert len(set(phases))==P//g
                        formula=sum(count[p]>=K for p in phases)/(P//g)
                        brute=sum(count[(j0+t*d)%P]>=K for t in range(P//g))/(P//g)
                        assert formula==brute
                        if g==1:
                            assert formula==1/P
                    checks+=1
    P,K,Y,H=29,3,5,5
    T=(K-1)*P+Y+H
    M=31
    N=T+Y+H-1+M*P
    training=list(range(0,T-Y-H+1))
    test=list(range(T,N-Y-H+1))
    assert len(test)==M*P
    def hist(j): return tuple((j+a)%P for a in range(Y))
    training_hist=[hist(j) for j in training]
    exact_all=[sum(hist(j)==h for h in training_hist)>=K for j in test]
    assert sum(exact_all)==M
    sampled=[j for j in test if j%P==0]
    assert len(sampled)==M and all(sum(hist(j)==h for h in training_hist)>=K for j in sampled)
    print(f'VERIFY_OK parameter_cases={checks} example_P={P} K={K} Y={Y} H={H} T={T} N={N} test={len(test)} full_exact={sum(exact_all)}/{len(test)} sampled_exact={len(sampled)}/{len(sampled)}')
if __name__=='__main__': run()
