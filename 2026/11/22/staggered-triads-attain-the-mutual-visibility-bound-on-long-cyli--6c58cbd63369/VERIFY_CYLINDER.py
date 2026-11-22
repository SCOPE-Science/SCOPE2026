#!/usr/bin/env python3
"""Finite stress tests for a three-staggered-band mutual-visibility construction.
This executable is supporting evidence only; the all-parameter theorem is proved in RESULT.md.
"""
from collections import deque

def vertices(s,n):
    g=n//3
    base=(0,g,2*g+(n%3==2))
    return {(r,(base[j]+r)%n) for r in range(s) for j in range(3)}

def distance(u,v,n):
    return abs(u[0]-v[0])+min((u[1]-v[1])%n,(v[1]-u[1])%n)

def independent_bfs_check(s,n):
    marks=vertices(s,n)
    for start in marks:
      for target in marks:
        if start>=target: continue
        want=distance(start,target,n)
        q=deque([(start,0)])
        seen={start}
        ok=False
        while q:
          (r,c),d=q.popleft()
          if (r,c)==target:
            assert d==want
            ok=True
            break
          if d>=want: continue
          nbr=[((r+1,c) if r+1<s else None), ((r-1,c) if r else None), (r,(c+1)%n),(r,(c-1)%n)]
          for v in nbr:
            if v is None or v in seen or (v in marks and v != target):continue
            if d+1+distance(v,target,n)!=want:continue
            seen.add(v);q.append((v,d+1))
        assert ok,(s,n,start,target)

def explicit_witness_check(s,n):
    g=n//3
    base=(0,g,2*g+(n%3==2))
    M=vertices(s,n)
    for j in range(3):
      for k in range(3):
        for r in range(s):
          for t in range(s):
            if j==k and r==t:continue
            if j!=k and (k-j)%3!=1:continue # reverse orientation is symmetric
            a=(r,(base[j]+r)%n)
            b=(t,(base[k]+t)%n)
            path=[a]
            if j==k:
              sign=1 if t>r else -1
              while path[-1][1]!=b[1]:
                row,c=path[-1]; path.append((row,(c+sign)%n))
            else:
              gap_col=(base[j]+s)%n
              while path[-1][1]!=gap_col:
                row,c=path[-1]; path.append((row,(c+1)%n))
            sign=1 if t>r else -1
            while path[-1][0]!=t:
              row,c=path[-1];path.append((row+sign,c))
            if j!=k:
              while path[-1][1]!=b[1]:
                row,c=path[-1];path.append((row,(c+1)%n))
            assert path[-1]==b
            assert len(path)-1==distance(a,b,n),(s,n,a,b,len(path),distance(a,b,n))
            assert all(v not in M for v in path[1:-1]),(s,n,a,b,path)
            for u,v in zip(path,path[1:]):
              assert abs(u[0]-v[0])+min((u[1]-v[1])%n,(v[1]-u[1])%n)==1

if __name__=='__main__':
    total=0
    for s in range(3,18):
       for n in [6*s-6]+list(range(6*s-4,6*s+19)):
          explicit_witness_check(s,n)
          independent_bfs_check(s,n)
          total+=1
    print('VISIBILITY_CYLINDER_VERIFY_OK', 'instances',total,'height_range','3..17','circumference','6s-6 and 6s-4..6s+18')
