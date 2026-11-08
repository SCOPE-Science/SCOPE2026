"""Exact checks for the nine-species bipartite richness-variance reversal.
No external packages. All degree sequences and probability comparisons are integer-exact.
"""
from collections import defaultdict, Counter
from itertools import combinations
from math import comb
from fractions import Fraction

# Each secondary row is a bitmask of primary neighbors, bits 0..Q-1.
WITNESS_A = (0b11011, 0b00110, 0b00001, 0b00001)
WITNESS_B = (0b11101, 0b00011, 0b00010, 0b00001)

def connected(rows, q):
    """Test connectedness of a simple bipartite incidence graph, both guilds nonempty."""
    p = len(rows)
    if any(not row for row in rows):
        return False
    if any(not any((row >> j) & 1 for row in rows) for j in range(q)):
        return False
    discovered_left = {0}
    discovered_right = set()
    frontier = [0]
    while frontier:
        i = frontier.pop()
        for j in range(q):
            if (rows[i] >> j) & 1 and j not in discovered_right:
                discovered_right.add(j)
                for h in range(p):
                    if ((rows[h] >> j) & 1) and h not in discovered_left:
                        discovered_left.add(h)
                        frontier.append(h)
    return len(discovered_left) == p and len(discovered_right) == q

def degrees(rows, q):
    left = tuple(row.bit_count() for row in rows)
    right = tuple(sum((row >> j) & 1 for row in rows) for j in range(q))
    return left, right

def variance_numerator(rows, q, k):
    """Return C(q,k)^2 Var(Y_k) as a nonnegative integer, by all live subsets."""
    total = 0
    squares = 0
    count = 0
    for subset in combinations(range(q), k):
        live = sum(1 << j for j in subset)
        y = sum(bool(row & live) for row in rows)
        total += y
        squares += y*y
        count += 1
    assert count == comb(q, k)
    return count*squares - total*total

def var_pair_formula(rows, q, k):
    """An independent exact inclusion-exclusion calculation of Var(Y_k)."""
    N = comb(q,k)
    zero = [Fraction(comb(q-row.bit_count(), k),N) if q-row.bit_count() >= k else Fraction(0) for row in rows]
    answer = sum((x-x*x for x in zero),Fraction(0))
    for i,j in combinations(range(len(rows)),2):
        union = (rows[i] | rows[j]).bit_count()
        joint_zero = Fraction(comb(q-union,k),N) if q-union>=k else Fraction(0)
        answer += 2*(joint_zero-zero[i]*zero[j])
    return answer

def distributions(rows,q,k):
    d=Counter()
    for S in combinations(range(q),k):
        live=sum(1<<j for j in S)
        d[sum(bool(row&live) for row in rows)]+=1
    return dict(sorted(d.items()))

def witness():
    A,B = WITNESS_A,WITNESS_B
    q=5
    assert connected(A,q) and connected(B,q)
    da, ea = degrees(A,q); db,eb=degrees(B,q)
    assert da==db==(4,2,1,1)
    assert ea==eb==(3,2,1,1,1)
    assert sum(da)==8
    va=[Fraction(variance_numerator(A,q,k),comb(q,k)**2) for k in range(1,q)]
    vb=[Fraction(variance_numerator(B,q,k),comb(q,k)**2) for k in range(1,q)]
    assert va==[Fraction(16,25),Fraction(17,20),Fraction(89,100),Fraction(16,25)],va
    assert vb==[Fraction(16,25),Fraction(21,20),Fraction(69,100),Fraction(6,25)],vb
    assert va[1]<vb[1] and va[2]>vb[2]
    assert [var_pair_formula(A,q,k) for k in range(1,q)]==va
    assert [var_pair_formula(B,q,k) for k in range(1,q)]==vb
    assert distributions(A,q,2)=={1:1,2:5,3:2,4:2}
    assert distributions(B,q,2)=={1:3,3:6,4:1}
    assert distributions(A,q,3)=={2:4,3:1,4:5}
    assert distributions(B,q,3)=={1:1,3:6,4:3}
    print('WITNESS_OK 9 vertices, 8 edges, two connected trees')
    print('A_VARIANCE',list(map(str,va)))
    print('B_VARIANCE',list(map(str,vb)))
    print('A_B_DIFF',list(map(str,(x-y for x,y in zip(va,vb)))))


def census():
    total_graphs=0
    total_degree_classes=0
    distinct_profiles=0
    for p in range(2,7):
        for q in range(2,9-p):
            # Here p+q<=8. Every possible labelled simple bipartite graph
            # appears in the complete range 0,...,2^(p*q)-1, exactly once.
            by_degrees=defaultdict(set)
            graph_count=0
            for code in range(1<<(p*q)):
                rows=tuple((code>>(q*i))&((1<<q)-1) for i in range(p))
                if not connected(rows,q):
                    continue
                graph_count+=1
                dl,dr=degrees(rows,q)
                key=(tuple(sorted(dl)),tuple(sorted(dr)))
                profile=tuple(variance_numerator(rows,q,k) for k in range(1,q))
                by_degrees[key].add(profile)
            total_graphs+=graph_count
            total_degree_classes+=len(by_degrees)
            distinct_profiles+=sum(map(len,by_degrees.values()))
            for key,profiles in by_degrees.items():
                for v,w in combinations(profiles,2):
                    differences=[a-b for a,b in zip(v,w)]
                    if min(differences,default=0)<0<max(differences,default=0):
                        raise AssertionError(('EARLIER_REVERSAL',p,q,key,v,w))
            print('CENSUS_OK',p,q,'connected',graph_count,
                  'degree_classes',len(by_degrees),
                  'variance_profiles',sum(map(len,by_degrees.values())))
    print('MINIMALITY_OK p+q <= 8; graphs',total_graphs,'degree_classes',total_degree_classes,'variance_profiles',distinct_profiles)

if __name__=='__main__':
    witness()
    census()
