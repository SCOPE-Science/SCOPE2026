"""Exact enumeration checks for source/sink dependence in bipartite uniform trees.

Run with Python 3, standard library only. Finite checks support (but do not replace)
the analytic all-size statements in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import combinations


def terms(a, b):
    assert a >= 1 and b >= 1
    c_a = (1 - Q(1, 2*a)) ** (b-1)
    c_b = (1 - Q(1, 2*b)) ** (a-1)
    q_a = (1 - Q(1, a)) ** (b-1)
    q_b = (1 - Q(1, b)) ** (a-1)
    p_edge = Q(1, 2*a-1) + Q(1, 2*b-1) - Q(1, (2*a-1)*(2*b-1))
    r = Q(1, 4)*c_a*c_b*p_edge
    d_a = Q(a*(a-1), 4)*q_a - Q(a*a,4)*c_a*c_a
    d_b = Q(b*(b-1), 4)*q_b - Q(b*b,4)*c_b*c_b
    t = Q(a*b)*r
    return ((d_a, t), (t, d_b)), r, (c_a,c_b,q_a,q_b)


def tree_edges(a,b):
    n=a+b
    edges=[(i,a+j) for i in range(a) for j in range(b)]
    for chosen in combinations(edges,n-1):
        parent=list(range(n))
        def find(i):
            while parent[i]!=i:
                i=parent[i]
            return i
        for i,j in chosen:
            ri,rj=find(i),find(j)
            parent[ri]=rj
        if len({find(i) for i in range(n)})==1:
            yield chosen


def brute_cov(a,b):
    n=a+b
    counts=[0]*4
    outer=[[0]*4 for _ in range(4)]
    total=0
    pair_cross=pair_same=0
    for edges in tree_edges(a,b):
        for bits in range(1<<(n-1)):
            incoming=[0]*n;outgoing=[0]*n
            for k,(u,v) in enumerate(edges):
                if bits>>k & 1:
                    u,v=v,u
                outgoing[u]+=1;incoming[v]+=1
            src=[int(x==0) for x in incoming]
            snk=[int(x==0) for x in outgoing]
            vec=[sum(src[:a]),sum(src[a:]),sum(snk[:a]),sum(snk[a:])]
            total+=1
            for i in range(4):
                counts[i]+=vec[i]
                for j in range(4): outer[i][j]+=vec[i]*vec[j]
            pair_cross+=src[0]*snk[a]
            if a>=2: pair_same+=src[0]*snk[1]
    def cov(i,j):
        return Q(outer[i][j],total)-Q(counts[i]*counts[j],total*total)
    return ((cov(0,2),cov(0,3)),(cov(1,2),cov(1,3))),Q(pair_cross,total),Q(pair_same,total) if a>=2 else None,total


def main():
    tests=0
    for a,b in [(1,1),(1,2),(1,3),(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)]:
        expected,r,(ca,cb,qa,qb)=terms(a,b)
        got,joint_cross,joint_same,total=brute_cov(a,b)
        assert expected==got,(a,b,expected,got)
        assert joint_cross==Q(1,4)*ca*cb+r,(a,b,joint_cross,r)
        if a>=2:
            assert joint_same==qa/4,(a,b,joint_same)
        assert total==a**(b-1)*b**(a-1)*(1<<(a+b-1))
        tests+=4 if a>=2 else 3
        print('EXACT',a,b,'outcomes',total,'matrix',got)
    for m in range(3,18):
        matrix,_,_=terms(m,m)
        assert matrix[0][0]<0 and matrix[1][1]<0
        assert matrix[0][0]*matrix[1][1]-matrix[0][1]**2>0
        tests+=3
    for a in range(2,9):
        matrix,_,_=terms(a,a)
        assert matrix[0][0]*matrix[1][1]-matrix[0][1]**2>=0
        tests+=1
        seen=False
        for b in range(a+1,220):
            M,_,_=terms(a,b)
            if M[0][0]*M[1][1]-M[0][1]**2<0:
                seen=True
                print('EXACT_NEG_DET_WITNESS',a,b)
                break
        assert seen
        tests+=1
    print('PASS',tests,'assertion groups; symbolic all-size statements proved separately')

if __name__=='__main__':main()
