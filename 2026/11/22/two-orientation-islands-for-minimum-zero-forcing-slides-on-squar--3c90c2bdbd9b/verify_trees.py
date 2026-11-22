"""Independent spanning-tree support and legal edge-pivot components for square rook graphs."""
from collections import deque
from itertools import combinations

def is_support_tree(cells,n):
    parent=list(range(2*n)); size=[1]*(2*n)
    def find(x):
        while parent[x]!=x:
            x=parent[x]
        return x
    for x in cells:
        a=x//n;b=n+x%n
        ra=find(a);rb=find(b)
        if ra==rb:return False
        if size[ra]<size[rb]:ra,rb=rb,ra
        parent[rb]=ra;size[ra]+=size[rb]
    roots={find(i) for i in range(2*n)}
    rows={i for i in range(n) if all(x//n != i for x in cells)}
    cols={j for j in range(n) if all(x%n != j for x in cells)}
    return len(roots)==2 and (len(rows),len(cols)) in [(1,0),(0,1)]

def run(n):
    N=n*n; white_size=2*n-2
    supports = []
    for cells in combinations(range(N), white_size):
        if is_support_tree(cells,n):
            supports.append(sum(1<<x for x in cells))
    expected=2*n*(n-1)**(n-1)*n**(n-2)
    assert len(supports)==expected
    idx={s:i for i,s in enumerate(supports)}
    graph=[[] for _ in supports]
    for i,s in enumerate(supports):
        for u in range(N):
            if not (s>>u)&1:continue
            for v in range(N):
                if (s>>v)&1 or not (u//n==v//n or u%n==v%n):continue
                j=idx.get(s^(1<<u)^(1<<v))
                if j is not None:graph[i].append(j)
    seen=set();comp=[]
    for i in range(len(supports)):
        if i in seen:continue
        queue=deque([i]);seen.add(i);c=0
        while queue:
            a=queue.popleft();c+=1
            for b in graph[a]:
                if b not in seen:seen.add(b);queue.append(b)
        comp.append(c)
    expected_parts=[1]*4 if n==2 else [expected//2]*2
    assert sorted(comp)==sorted(expected_parts)
    print('n=%d: tree supports=%d, pivot edges=%d, component sizes=%s' %
          (n,len(supports),sum(map(len,graph))//2,sorted(comp)))

if __name__=='__main__':
    for n in (2,3,4):run(n)
    print('Independent tree-pivot checks passed.')
