"""Exact reproducibility checks for open-neighborhood NOR on cubic cyclic ladders.
Uses standard-library integer arithmetic; no external files or dependencies.
"""

from itertools import product

def flip(a):
    return ((a & 1) << 1) | ((a & 2) >> 1)

def matrix():
    pairs = list(product(range(4), repeat=2))
    index = {pair: i for i,pair in enumerate(pairs)}
    T = [[0] * 16 for _ in range(16)]
    J = [index[(flip(a),flip(b))] for a,b in pairs]
    for a,b in pairs:
        for c in range(4):
            if all((a & (1 << r)) or (c & (1 << r)) or (b & (1 << (1-r))) for r in (0,1)):
                T[index[(a,b)]][index[(b,c)]] = 1
    return T,J

def multiply(A,B):
    n=len(A);C=[[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k]:
                for j in range(n):
                    C[i][j] += A[i][k]*B[k][j]
    return C

def root_sums(which, limit):
    # p = x^3 - 3x^2 - x - 1, q = x^3 - x^2 + x + 1
    if which == 'p': a,b,c=3,1,1
    elif which == 'q': a,b,c=1,-1,-1
    else: raise ValueError
    values=[3,a,a*a+2*b]
    for n in range(3,limit+1):
        values.append(a*values[-1]+b*values[-2]+c*values[-3])
    return values

def graph(n,twist):
    N=2*n
    edges={(i,n+i) for i in range(n)}
    for i in range(n-1):
        edges.add((i,i+1));edges.add((n+i,n+i+1))
    if twist:
        edges.add((0,2*n-1));edges.add((n-1,n))
    else:
        edges.add((0,n-1));edges.add((n,2*n-1))
    adj=[0]*N
    for u,v in edges:
        adj[u] |= 1<<v
        adj[v] |= 1<<u
    return adj

def one_step(x,adj):
    return sum((1<<i) for i,neigh in enumerate(adj) if not(x&neigh))

def brute_basin(n,twist):
    adj=graph(n,twist);full=(1<<(2*n))-1
    total=0
    for x in range(full+1):
        # Global two-cycle's initial basin: x=0 or x total dominates.
        y=one_step(x,adj)
        in_basin=(x==0 or y==0)
        if in_basin: total+=1
        # Entire graph NOR dynamics is immediately recurrent after one update.
        assert one_step(one_step(y,adj),adj)==y
        if in_basin: assert (y==0 or y==full)
    return total

def main():
    T,J=matrix()
    for i in range(16):
        for j in range(16):
            assert T[J[i]][J[j]]==T[i][j]
    P=root_sums('p',50);Q=root_sums('q',50)
    power=[[int(i==j) for j in range(16)] for i in range(16)]
    for n in range(1,41):
        power=multiply(power,T)
        if n<3:continue
        tp=sum(power[i][i] for i in range(16))
        tm=sum(power[i][J[i]] for i in range(16))
        assert tp==P[n]+(1+(-1)**n)*Q[n], (n,'P',tp,P[n],Q[n])
        assert tm==P[n]+((-1)**n-1)*Q[n], (n,'M',tm,P[n],Q[n])
        assert tm-tp==-2*Q[n]
        if n<=12:print('TRANSFER n=%d totalP=%d totalM=%d difference=%+d'%(n,tp,tm,tm-tp))
        if n<=9:
            bp=brute_basin(n,False)
            bm=brute_basin(n,True)
            assert bp==tp+1 and bm==tm+1, (n,bp,bm,tp,tm)
            print('BRUTE n=%d statesPerGraph=%d basins=%d,%d PASS'%(n,4**n,bp,bm))
    print('PASS: exact transfer agreement for n=3..40; independent exhaustive NOR basins n=3..9; F^3=F per enumerated state.')

if __name__=='__main__':main()
