"""Independent alternating-interval neighbor generation and adjacency BFS."""
from collections import Counter

def generate(n):
    # Enumerate balanced length 2n words as combinations of up-step positions.
    from itertools import combinations
    out=[]
    for positions in combinations(range(2*n),n):
        S=set(positions); h=0; okay=True; bits=[]
        for i in range(2*n):
            b='1' if i in S else '0';bits.append(b)
            h+=1 if b=='1' else -1
            if h<0:okay=False;break
        if okay and h==0:out.append(''.join(bits))
    return out

def check():
    W=generate(8);N=len(W);assert N==1430
    index={w:i for i,w in enumerate(W)}
    adj=[set() for _ in W]
    for i,w in enumerate(W):
        for lo in range(16):
            for hi in range(lo+2,17,2):
                seg=w[lo:hi]
                if all(seg[t]!=seg[t+1] for t in range(len(seg)-1)):
                    toggled=''.join('1' if c=='0' else '0' for c in seg)
                    u=w[:lo]+toggled+w[hi:]
                    if u in index and u!=w:
                        j=index[u];adj[i].add(j)
    assert all(i in adj[j] for i,nei in enumerate(adj) for j in nei)
    assert sum(len(x) for x in adj)//2==6733
    # Compute all shortest paths using array-based breadth-first search.
    counts=[0]*17; ecc=[0]*N;far=[]
    for i in range(N):
        dist=[-1]*N;dist[i]=0;queue=[i];head=0
        while head<len(queue):
            k=queue[head];head+=1
            for j in adj[k]:
                if dist[j]<0:dist[j]=dist[k]+1;queue.append(j)
        assert len(queue)==N
        ecc[i]=max(dist)
        for j in range(i+1,N):
            counts[dist[j]]+=1
            if dist[j]==12:far.append((W[i],W[j]))
    target=[6733,33784,106065,213636,274051,223067,115996,38930,8325,1073,73,2]
    assert counts[1:13]==target
    assert Counter(ecc)==Counter({6:1,7:68,8:387,9:581,10:320,11:69,12:4})
    assert [W[i] for i in range(N) if ecc[i]==6]==['1101010101010100']
    assert len(far)==2
    print('VERIFY_B_OK',N,counts[1:13])
if __name__=='__main__':check()
