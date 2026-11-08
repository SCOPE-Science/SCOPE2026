"""Independent transition-matrix checks of the complete-graph reset entropy theorem.
Only Python standard library is required.
"""
import math

def entropy_from_matrix(n, gamma):
    m = n - 1
    P = []
    for i in range(n):
        row = []
        for j in range(n):
            t = (1.0 - gamma)/m if j != i else 0.0
            if j == 0:
                t += gamma
            row.append(t)
        assert abs(sum(row) - 1.0) < 1e-12
        P.append(row)
    pi = [1.0/n]*n
    for _ in range(100000):
        nxt = [sum(pi[i]*P[i][j] for i in range(n)) for j in range(n)]
        if max(abs(a-b) for a,b in zip(nxt, pi)) < 1e-15:
            pi=nxt
            break
        pi=nxt
    return sum(pi[i]*sum(-v*math.log(v) for v in P[i] if v>0) for i in range(n)),pi

def entropy_closed(n, g):
    m=n-1
    p=1-g
    u=1+(m-1)*g
    d=m+1-g
    if g==0: return math.log(m)
    if g==1: return 0.
    z=-u*g*math.log(m*g)-m*p*math.log(p)-p*u*math.log(u)
    return math.log(m)+z/d

def overlap_deficit(n,g):
    m=n-1
    p=1-g
    pi_neighbors=m*p/(m+1-g)
    q=p/m
    return pi_neighbors*((g+q)*math.log(g+q)-g*math.log(g)-q*math.log(q))

def main():
    count=0
    for n in range(3,21):
        for g in [0.001,0.013,0.07,0.21,0.45,0.77,0.98]:
            direct,pi=entropy_from_matrix(n,g)
            exact=entropy_closed(n,g)
            assert abs(direct-exact)<5e-12, (n,g,direct,exact)
            predicted_pi=[(1+(n-2)*g)/(n-g)]+[(1-g)/(n-g)]*(n-1)
            assert max(abs(a-b) for a,b in zip(pi,predicted_pi))<5e-12
            split=-(1-g)*math.log((1-g)/(n-1))-g*math.log(g)
            assert abs(split-direct-overlap_deficit(n,g))<5e-12
            assert direct<math.log(n)
            count+=1
    print(f'PASS: {count} independent matrix, stationary-law, overlap-deficit and upper-bound comparisons')
    for n in [3,4,10,30,100]:
        lo, hi=1e-12,1-1e-12
        for _ in range(150):
            a=lo+(hi-lo)*0.3819660112501051
            b=lo+(hi-lo)*0.6180339887498949
            if entropy_closed(n,a)>entropy_closed(n,b): hi=b
            else: lo=a
        optimum=(lo+hi)/2
        print('n',n,'numerical maximizing candidate',format(optimum,'.10g'),'gain',format(entropy_closed(n,optimum)-math.log(n-1),'.10g'))
if __name__=='__main__': main()
