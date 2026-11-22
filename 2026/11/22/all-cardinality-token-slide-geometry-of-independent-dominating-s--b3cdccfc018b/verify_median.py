from collections import deque
from itertools import combinations, combinations_with_replacement
from math import comb

for p in range(1,9):
    for z in range(p+1):
        states=list(combinations(range(1,p+1),z))
        idx={s:i for i,s in enumerate(states)}
        graph=[set() for _ in states]
        for s in states:
            m=set(s)
            for j in s:
                for t in (j-1,j+1):
                    if 1<=t<=p and t not in m:
                        v=tuple(sorted((m-{j})|{t}))
                        graph[idx[s]].add(idx[v])
        distances=[]
        for i in range(len(states)):
            d=[-1]*len(states)
            d[i]=0
            q=deque([i])
            while q:
                x=q.popleft()
                for y in graph[x]:
                    if d[y]<0:
                        d[y]=d[x]+1
                        q.append(y)
            assert all(a>=0 for a in d)
            distances.append(d)
        assert sum(map(len,graph))//2 == (p-1)*comb(p-2,z-1) if 0<z<p else sum(map(len,graph))==0
        for i,s in enumerate(states):
            for j,t in enumerate(states):
                assert distances[i][j]==sum(abs(a-b) for a,b in zip(s,t))
        assert max(map(max,distances))==z*(p-z)
        if len(states) <= 28:
            for a,b,c in combinations_with_replacement(range(len(states)),3):
                med=tuple(sorted((states[a][h],states[b][h],states[c][h]))[1] for h in range(z))
                m=idx[med]
                assert all(distances[i][j]==distances[i][m]+distances[m][j] for i,j in ((a,b),(b,c),(a,c)))
                assert sum(all(distances[i][j]==distances[i][v]+distances[v][j] for i,j in ((a,b),(b,c),(a,c))) for v in range(len(states))) == 1
        print('p=%d z=%d states=%d edges=%d diameter=%d' % (p,z,len(states),sum(map(len,graph))//2,z*(p-z)))
print('MEDIAN_AND_DISTANCE_PASS')
