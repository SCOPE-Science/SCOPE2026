"""Exact all-ring temporal period-one/two transfer proof for elementary rule 73.
Standard library only; no external datasets or network requests.
"""
from collections import defaultdict, deque

RULE = 73

def local(a,b,c):
    return (RULE >> (4*a+2*b+c)) & 1

def bitword(value, width):
    return [(value >> (width-1-j)) & 1 for j in range(width)]

def build_graph(width):
    graph = [[] for _ in range(1 << width)]
    for a in range(1 << width):
        pref = bitword(a,width)
        for e in (0,1):
            w = pref + [e]
            if width == 2:
                ok = local(*w) == w[1]
            else:
                assert width == 4
                ok = local(local(*w[0:3]),local(*w[1:4]),local(*w[2:5])) == w[2]
            if ok:
                graph[a].append(((a << 1) | e) & ((1 << width)-1))
    return graph

def directed_cycles(graph):
    """Each directed elementary cycle once, canonical minimum start."""
    found=[]
    for start in range(len(graph)):
        def visit(cur,path,used):
            for nxt in graph[cur]:
                if nxt == start:
                    found.append(tuple(path))
                elif nxt > start and nxt not in used:
                    visit(nxt,path+[nxt],used | {nxt})
        visit(start,[start],{start})
    assert len(found) == len(set(found))
    return found

def det_I_minus_z_graph(graph):
    """Permutation expansion: choose disjoint directed cycles; sign per cycle -1."""
    cycles=directed_cycles(graph)
    terms=defaultdict(int)
    def choose(k,used,degree,sign):
        if k == len(cycles):
            terms[degree] += sign
            return
        choose(k+1,used,degree,sign)
        c=cycles[k]
        m=sum(1<<v for v in c)
        if not (used & m):
            choose(k+1,used|m,degree+len(c),-sign)
    choose(0,0,0,1)
    return [terms[i] for i in range(max(terms)+1)],cycles

def poly_mul(a,b):
    o=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):o[i+j]+=x*y
    return o

def poly_pow(p,k):
    ans=[1]
    for _ in range(k):ans=poly_mul(ans,p)
    return ans

def reachable(graph,origin,allowed,reverse=False):
    todo=[origin]
    seen={origin}
    while todo:
        a=todo.pop()
        targets=[i for i in allowed if a in graph[i]] if reverse else graph[a]
        for b in targets:
            if b in allowed and b not in seen:
                todo.append(b)
                seen.add(b)
    return seen

def trace_power(graph,n):
    N=len(graph)
    A=[[0]*N for _ in range(N)]
    for i,nb in enumerate(graph):
        for j in nb:A[i][j]+=1
    P=[[int(i==j) for j in range(N)] for i in range(N)]
    for _ in range(n):
        P=[[sum(P[i][k]*A[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
    return sum(P[i][i] for i in range(N))

def update(x,n):
    r=0
    for i in range(n):
        a=(x >> ((i-1)%n))&1
        b=(x >> i)&1
        c=(x >> ((i+1)%n))&1
        r |= local(a,b,c)<<i
    return r

def brute(n):
    f1=f2=0
    for x in range(1<<n):
        y=update(x,n)
        f1+=int(y==x)
        f2+=int(update(y,n)==x)
    return f1,f2

def main():
    assert [local(i>>2,(i>>1)&1,i&1) for i in range(8)] == [1,0,0,1,0,0,1,0]
    B=build_graph(2)
    A=build_graph(4)
    det1,cyc1=det_I_minus_z_graph(B)
    det2,cyc2=det_I_minus_z_graph(A)
    expected1=[1,0,0,-1,-1] # 1-z^3-z^4
    expected2=poly_mul(poly_mul(poly_pow([1,-1],2),poly_pow([1,0,1],2)),[1,0,-2,-1,1])
    assert det1 == expected1,(det1,expected1)
    assert det2[:len(expected2)] == expected2 and all(x==0 for x in det2[len(expected2):]),(det2,expected2)
    assert len(cyc1)==2 and len(cyc2)==10
    active={1,2,3,4,5,6,8,9,10,11,12,13}
    assert reachable(A,1,active)==active and reachable(A,1,active,True)==active
    # Shared vertex 6 lies on cycles of coprime lengths 3 and 4.
    assert any(len(c)==3 and 6 in c for c in cyc2)
    assert any(len(c)==4 and 6 in c for c in cyc2)
    assert reachable(B,0,set(range(4)))==set(range(4))
    assert reachable(B,0,set(range(4)),True)==set(range(4))
    assert {len(c) for c in cyc1}=={3,4}
    # Finitely many direct experiments, used as a cross-check only.
    for n in range(1,18):
        t1,t2=trace_power(B,n),trace_power(A,n)
        b1,b2=brute(n)
        assert (t1,t2)==(b1,b2),(n,t1,t2,b1,b2)
        assert (t2-t1)%2==0
        print(n,t1,t2,(t2-t1)//2)
    # Exact rational isolations of positive growth roots.
    from fractions import Fraction as Q
    p=lambda t: t**4-t-1
    q=lambda t: t**4-2*t*t-t+1
    assert p(Q(1220,1000))<0<p(Q(1221,1000))
    assert q(Q(1490,1000))<0<q(Q(1491,1000))
    assert q(Q(13,10))<0
    print('CERTIFICATE_OK')
    print('DET1=',det1)
    print('DET2=',det2)
    print('CYCLES_4=',len(cyc1),'CYCLES_16=',len(cyc2))

if __name__=='__main__':
    main()
