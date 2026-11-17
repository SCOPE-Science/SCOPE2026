"""Exact standalone checks of three generalized Petersen degree-two matching complexes.

Run with Python 3.10+. Standard library only. Prints a machine-readable JSON line.
All graph-edge subsets are exhaustively generated, with no random sampling.
"""
import json
import sys
from collections import Counter, deque
from functools import lru_cache


def graph_edges(n):
    # Vertices 0..n-1 (outer), n..2n-1 (inner); n=6,7,8.
    result = ([(i,(i+1)%n) for i in range(n)]
              + [(i,n+i) for i in range(n)]
              + [(n+i,n+(i+2)%n) for i in range(n)])
    assert len(result)==3*n
    assert all(a!=b for a,b in result)
    assert len({tuple(sorted(e)) for e in result})==3*n
    degree=Counter(x for a,b in result for x in (a,b))
    assert len(degree)==2*n and set(degree.values())=={3}
    return result


def enumerate_faces(es):
    """Enumerate every edge subset with incident degree <= 2, including empty."""
    v=len(es); N=1+max(max(e) for e in es)
    d=[0]*N; result=[]
    def extend(i,mask):
        if i==v:
            result.append(mask); return
        extend(i+1,mask)
        a,b=es[i]
        if d[a]<2 and d[b]<2:
            d[a]+=1; d[b]+=1
            extend(i+1,mask|(1<<i))
            d[a]-=1;d[b]-=1
    extend(0,0)
    assert len(result)==len(set(result)) and 0 in result
    # An independent vertex-wise count checks each retained subset's condition.
    for mask in result:
        deg=[0]*N
        for i,(a,b) in enumerate(es):
            if mask>>i&1:
                deg[a]+=1;deg[b]+=1
        assert max(deg)<=2
    return result


def faces_with_sign(face):
    i=0;original=face
    while face:
        bit=face&-face
        yield original^bit, (1 if i%2==0 else -1)
        face-=bit;i+=1


def toggled_morse_matching(all_faces,order):
    available=set(all_faces);available.remove(0)
    paired={}
    for p in order:
        bit=1<<p
        for face in all_faces:
            upper=face|bit
            if not face&bit and face in available and upper in available:
                paired[face]=upper
                available.remove(face);available.remove(upper)
    assert 2*len(paired)+len(available)+1==len(all_faces)
    return available,paired


def verify_acyclic(paired):
    """Verify all reversed-match Hasse cycles via exact gradient graph contraction."""
    upper_to_lower={up:lo for lo,up in paired.items()}
    assert len(upper_to_lower)==len(paired)
    for lo,up in paired.items():
        assert up&lo==lo and (up^lo).bit_count()==1
    indegree=dict.fromkeys(upper_to_lower,0)
    for up,lo in upper_to_lower.items():
        for other,_ in faces_with_sign(up):
            if other!=lo and other in paired:
                indegree[paired[other]]+=1
    ready=deque(up for up,v in indegree.items() if not v)
    completed=0
    while ready:
        up=ready.popleft();completed+=1
        for other,_ in faces_with_sign(up):
            if other!=upper_to_lower[up] and other in paired:
                target=paired[other]
                indegree[target]-=1
                if indegree[target]==0:ready.append(target)
    assert completed==len(paired), 'Directed gradient cycle detected'
    return completed


def integral_morse_boundary(critical,paired,low_size):
    """Exact signed elimination of matched incidence pairs.

    Rows are critical faces containing low_size graph edges; columns contain
    low_size+1 graph edges. Every coefficient is an integer.
    """
    lows=sorted(f for f in critical if f.bit_count()==low_size)
    highs=sorted(f for f in critical if f.bit_count()==low_size+1)
    index={x:i for i,x in enumerate(lows)}
    uppers=set(paired.values())
    in_progress=set()
    @lru_cache(None)
    def project(face):
        if face in index: return {index[face]:1}
        if face in uppers: return {}
        assert face in paired, 'Unclassified lower-dimensional face'
        assert face not in in_progress
        in_progress.add(face)
        higher=paired[face]
        sign=next(s for other,s in faces_with_sign(higher) if other==face)
        ans={}
        for other,s in faces_with_sign(higher):
            if other==face:continue
            for i,z in project(other).items():
                ans[i]=ans.get(i,0)-sign*s*z
                if ans[i]==0:del ans[i]
        in_progress.remove(face)
        return ans
    A=[[0]*len(highs) for _ in lows]
    for j,higher in enumerate(highs):
        for face,sign in faces_with_sign(higher):
            for i,z in project(face).items():
                A[i][j]+=sign*z
    return A,lows,highs


def unimodular_unit_reduction(matrix):
    """Perform integer row/column changes and count diagonal unit pivots."""
    A=[r[:] for r in matrix]
    m=len(A);n=len(A[0]) if m else 0
    pivots=0
    for k in range(min(m,n)):
        loc=next(((i,j) for i in range(k,m) for j in range(k,n)
                  if abs(A[i][j])==1),None)
        if loc is None:break
        i,j=loc
        A[k],A[i]=A[i],A[k]
        for row in A:row[k],row[j]=row[j],row[k]
        sign=A[k][k]
        for i in range(k+1,m):
            if A[i][k]:
                q=A[i][k]*sign
                for j in range(k,n):A[i][j]-=q*A[k][j]
        for j in range(k+1,n):
            if A[k][j]:
                q=A[k][j]*sign
                for row in A:row[j]-=q*row[k]
        pivots+=1
    assert all(A[i][j] == 0 if i!=j else A[i][j] in (-1,0,1)
               for i in range(m) for j in range(n))
    return pivots,A


def main(reverse=False):
    expected={
        6:{'augmented_faces':69415,'pairs':34704,'critical':{0:1,8:3,9:2}},
        7:{'augmented_faces':447641,'pairs':223819,'critical':{0:1,10:1}},
        8:{'augmented_faces':2873983,'pairs':1436990,'critical':{0:1,12:1}}
    }
    records=[]
    for n in (6,7,8):
        es=graph_edges(n)
        ff=enumerate_faces(es)
        assert len(ff)==expected[n]['augmented_faces']
        sizes=Counter(x.bit_count() for x in ff)
        # Full Hasse cover count, every one of these incidences is a legitimate face relation.
        covers=sum(x.bit_count() for x in ff)
        euler_reduced=sum((-1)**(x.bit_count()-1) for x in ff if x) - 1
        if not reverse:
            critical,paired=toggled_morse_matching(ff,range(3*n))
            assert len(paired)==expected[n]['pairs']
            assert dict(Counter(x.bit_count()-1 for x in critical))==expected[n]['critical']
            assert verify_acyclic(paired)==len(paired)
            assert euler_reduced == sum(v*(-1)**k for k,v in expected[n]['critical'].items())-1
        else:
            critical,paired=toggled_morse_matching(ff,reversed(range(3*n)))
            assert verify_acyclic(paired)==len(paired)
        d={'n':n,'vertices':2*n,'graph_edges':3*n,
           'augmented_faces':len(ff),'face_vector': [sizes.get(i,0) for i in range(1,max(sizes)+1)],
           'hasse_covers':covers,'morse_pairs':len(paired),
           'critical':{str(k):v for k,v in sorted(Counter(x.bit_count()-1 for x in critical).items())},
           'reduced_euler_characteristic':euler_reduced,
           'gradient_acyclic':True}
        if n==6 and not reverse:
            matrix,lows,highs=integral_morse_boundary(critical,paired,9)
            assert matrix==[[0,-1],[-1,-1],[0,-1]],matrix
            rank,diagonal=unimodular_unit_reduction(matrix)
            assert rank==2
            assert all(abs(diagonal[i][j])==(1 if i==j and i<2 else 0)
                       for i in range(3) for j in range(2))
            d.update({'critical_8_masks':lows,'critical_9_masks':highs,
                      'signed_morse_boundary':matrix,'unimodular_pivots':rank})
        # A second complete independent matching can be run with --reverse.
        reverse_expected={6:({0:1,8:2,9:1},[[1],[-1]]),
                          7:({0:1,9:1,10:2},[[1,-1]]),
                          8:({0:1,11:1,12:2},[[1,1]])}
        alt_counts=dict(Counter(f.bit_count()-1 for f in critical))
        if reverse: assert alt_counts==reverse_expected[n][0]
        # The reverse CW model contains just one adjacent-dimensional cell pair,
        # with primitive attaching-degree vector and the same residual sphere.
        alt_low={6:9,7:10,8:12}[n]
        if reverse:
            alt_matrix,_,_=integral_morse_boundary(critical,paired,alt_low)
            assert alt_matrix==reverse_expected[n][1]
            assert unimodular_unit_reduction(alt_matrix)[0]==1
            d.update({'signed_morse_boundary':alt_matrix,'unimodular_pivots':1})
        records.append(d)
    print(json.dumps({'theorem':'M2(GP(n,2)) = S^(2n-4), n=6,7,8',
                      'mode':'reverse' if reverse else 'forward','checks':records,'status':'PASS'},sort_keys=True,separators=(',',':')))

if __name__=='__main__':
    assert sys.argv[1:] in ([],['--reverse'])
    main(reverse=(sys.argv[1:]==['--reverse']))
