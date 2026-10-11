from itertools import product

Q=3
EXPECTED={2:1,3:3,4:7,5:13}
WITNESSES={
2:['22'],
3:['222','121','020'],
4:['2222','2020','2121','1111','1010','0112','0000'],
5:['22222','22120','21110','12121','11111','10101','20202','20001','10002','02122','01112','02010','00000'],
}

def parse(s): return tuple(map(int,s))

def burst_ball_slice(w,k):
    return {w[:i]+w[i+k:] for i in range(len(w)-k+1)}

def burst_ball_filter(w,k):
    n=len(w)
    out=set()
    for start in range(n-k+1):
        out.add(tuple(w[j] for j in range(n) if not (start <= j < start+k)))
    return out

def error_signature(w):
    return (burst_ball_slice(w,1), burst_ball_slice(w,2))

def compatible(sig1,sig2):
    # Outputs from 1 and 2 deletions have different lengths, so cross-length intersections are impossible.
    return sig1[0].isdisjoint(sig2[0]) and sig1[1].isdisjoint(sig2[1])

def build_graph(words):
    sig=[]
    for w in words:
        a1=burst_ball_slice(w,1); a2=burst_ball_slice(w,2)
        b1=burst_ball_filter(w,1); b2=burst_ball_filter(w,2)
        assert a1==b1 and a2==b2
        sig.append((a1,a2))
    N=len(words); adj=[0]*N
    for i in range(N):
        for j in range(i):
            if compatible(sig[i],sig[j]):
                adj[i] |= 1<<j
                adj[j] |= 1<<i
    return adj,sig

def maximum_clique(adj):
    # Exact branch-and-bound. A greedy proper coloring of the candidate graph gives an upper bound
    # on how many more vertices any clique can take. Every branch includes one candidate v, then
    # restricts to its neighbors; the exclusion is effected by deleting v before the next branch.
    N=len(adj); best=[]; nodes=0
    def expand(R,P):
        nonlocal best,nodes
        nodes += 1
        if not P:
            if len(R)>len(best): best=R[:]
            return
        order=[]; bounds=[]; U=P; color=0
        while U:
            color += 1
            Qset=U
            while Qset:
                vb=Qset & -Qset
                v=vb.bit_length()-1
                order.append(v); bounds.append(color)
                U ^= vb
                Qset ^= vb
                Qset &= ~adj[v]
        for t in range(len(order)-1,-1,-1):
            if len(R)+bounds[t] <= len(best):
                return
            v=order[t]; vb=1<<v
            if P & vb:
                expand(R+[v], P & adj[v])
                P ^= vb
    expand([], (1<<N)-1)
    return best,nodes

def check_clique(indices,adj):
    for a,i in enumerate(indices):
        for j in indices[:a]:
            assert (adj[i]>>j)&1

def main():
    got=[]
    for n in range(2,6):
        words=list(product(range(Q), repeat=n))
        adj,sig=build_graph(words)
        idx={w:i for i,w in enumerate(words)}
        witness=[idx[parse(s)] for s in WITNESSES[n]]
        check_clique(witness,adj)
        best,nodes=maximum_clique(adj)
        check_clique(best,adj)
        assert len(best)==EXPECTED[n], (n,len(best),EXPECTED[n])
        assert len(witness)==EXPECTED[n]
        got.append(EXPECTED[n])
        print(f'n={n} vertices={len(words)} optimum={len(best)} search_nodes={nodes}')
    print('VERIFY_OK profile=' + ','.join(map(str,got)))

if __name__=='__main__': main()
