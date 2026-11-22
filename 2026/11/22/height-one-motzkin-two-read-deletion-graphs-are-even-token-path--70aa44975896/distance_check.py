"""Independent finite geometry check for exclusion graph components."""
from collections import deque
from itertools import combinations
from math import factorial


def neighbors(S,n):
    occupied=set(S)
    for j in range(n-1):
        if (j in occupied) != (j+1 in occupied):
            yield tuple(sorted(occupied.symmetric_difference((j,j+1))))


def bfs(source,n):
    d={source:0}; num={source:1}; queue=deque([source])
    while queue:
        u=queue.popleft()
        for v in neighbors(u,n):
            if v not in d:
                d[v]=d[u]+1; num[v]=0; queue.append(v)
            if d[v]==d[u]+1:
                num[v]+=num[u]
    return d,num


def rectangular_tableaux(k,m):
    den=1
    for i in range(k):
        for j in range(m):
            den*=i+j+1
    return factorial(k*m)//den


def main():
    for n in range(1,10):
        for t in range(n//2+1):
            k=2*t
            nodes=list(combinations(range(n),k))
            maxi=0
            for i,source in enumerate(nodes):
                dist,paths=bfs(source,n)
                assert len(dist)==len(nodes), (n,k,source,len(dist))
                for target in nodes:
                    val=sum(abs(a-b) for a,b in zip(source,target))
                    assert dist[target]==val, (n,k,source,target,dist[target],val)
                    maxi=max(maxi,val)
            assert maxi == k*(n-k)
            lower=tuple(range(k))
            upper=tuple(range(n-k,n))
            dist,paths=bfs(lower,n)
            assert paths[upper] == rectangular_tableaux(k,n-k), (n,k,paths[upper],rectangular_tableaux(k,n-k))
        print('geodesic n=',n,'passed')
    print('ALL GEOMETRY TESTS PASS')

if __name__=='__main__':main()
