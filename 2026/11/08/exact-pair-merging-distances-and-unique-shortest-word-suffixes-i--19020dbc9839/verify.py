#!/usr/bin/env python3
"""Reproduce the pair-merging spectrum for the labeled Cerny automata.

The program checks the closed formula against independently generated
reverse breadth-first distances, and checks uniqueness of each shortest
word by counting distance-decreasing outgoing transitions.
"""
from collections import defaultdict, deque


def predicted(n, pair):
    i,j=pair
    g=j-i
    if 2*g<n:
        return n*g-i
    return (n+1)*(n-g)-n-i


def next_pair(n, pair, letter):
    i,j=pair
    if letter=='a':
        return tuple(sorted(((i+1)%n,(j+1)%n)))
    if letter=='b':
        if j==n-1:
            if i==0: return None
            return (0,i)
        return pair
    raise ValueError(letter)


def predicted_longest_word(n):
    m=n//2
    if n%2:
        return ('a'*(n-1)+'b')*m
    return ('a'*(m-1)+'b')+('a'*(n-1)+'b')*(m-1)


def check(n, exhaustive=True):
    nodes=[(i,j) for i in range(n) for j in range(i+1,n)]
    N=n*(n-1)//2
    distances={p:predicted(n,p) for p in nodes}
    assert sorted(distances.values())==list(range(1,N+1)),n
    reverse=defaultdict(list)
    for p in nodes:
        successors=[next_pair(n,p,letter) for letter in 'ab']
        differences=[]
        for s in successors:
            ds=0 if s is None else distances[s]
            differences.append(distances[p]-ds)
            reverse[s].append(p)
        assert differences.count(1)==1,(n,p,differences)
        assert max(differences)<=1,(n,p,differences)
    q=deque([None]); bfs={None:0}
    if exhaustive:
        while q:
            v=q.popleft()
            for p in reverse[v]:
                if p not in bfs:
                    bfs[p]=bfs[v]+1
                    q.append(p)
        # Only directly b-merging pair maps to the sink.
        assert len(bfs)==N+1,n
        assert all(bfs[p]==distances[p] for p in nodes),n
    target=max(nodes,key=lambda p:distances[p]); assert distances[target]==N
    word=predicted_longest_word(n); assert len(word)==N
    s=target
    for pos,letter in enumerate(word):
        assert distances[s]==N-pos,(n,pos,s,letter)
        s=next_pair(n,s,letter)
        if pos!=N-1:assert s is not None
    assert s is None,n
    # Every state has a unique decreasing successor, hence all shortest
    # words are precisely the nonempty suffixes of this word.
    return len(nodes)


def main():
    count=0
    for n in range(2,81):
        count+=check(n,True)
    for n in range(81,401):
        count+=check(n,False)
    print('PASS: n=2..80 independent BFS; n=2..400 potential/unique-greedy/longest-word checks')
    print('Total pair instances:',count)
if __name__=='__main__':main()
