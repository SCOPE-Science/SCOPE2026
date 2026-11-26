"""Exhaustive semilength-eight Dyck deletion-confusability metric."""
from collections import defaultdict, Counter, deque

def paths(n):
    def rec(w,h):
        if len(w)==2*n:
            if h==0: yield w
            return
        if h<n: yield from rec(w+'1',h+1)
        if h: yield from rec(w+'0',h-1)
    return list(rec('',0))

def check():
    n=8; words=paths(n); N=len(words)
    assert N==1430==len(set(words))
    inverse=defaultdict(set)
    for i,w in enumerate(words):
        for j in range(2*n): inverse[w[:j]+w[j+1:]].add(i)
    common=Counter()
    for inds in inverse.values():
        inds=sorted(inds)
        for j,a in enumerate(inds):
            for b in inds[j+1:]: common[a,b]+=1
    adj=[set() for _ in words]
    for (a,b),v in common.items():
        if v>=2: adj[a].add(b); adj[b].add(a)
    assert sum(map(len,adj))//2==6733
    ecc=[];dist_hist=Counter(); diam_pairs=[]
    for i in range(N):
        D=[-1]*N; D[i]=0; q=deque([i])
        while q:
            a=q.popleft()
            for b in adj[a]:
                if D[b]<0: D[b]=D[a]+1;q.append(b)
        assert -1 not in D
        ecc.append(max(D))
        for j in range(i+1,N):
            dist_hist[D[j]]+=1
            if D[j]==12: diam_pairs.append((words[i],words[j]))
    assert sum(dist_hist.values())==N*(N-1)//2
    expected=[6733,33784,106065,213636,274051,223067,115996,38930,8325,1073,73,2]
    assert [dist_hist[k] for k in range(1,13)]==expected
    assert dict(sorted(Counter(ecc).items()))=={6:1,7:68,8:387,9:581,10:320,11:69,12:4}
    assert [words[i] for i,d in enumerate(ecc) if d==6]==['1101010101010100']
    assert sorted(diam_pairs)==sorted([
        ('1111111100000000','1011111100000010'),
        ('1111111000000010','1011111110000000')])
    return N,sum(map(len,adj))//2,dist_hist
if __name__=='__main__':
    print(check())
    print('VERIFY_A_OK')
