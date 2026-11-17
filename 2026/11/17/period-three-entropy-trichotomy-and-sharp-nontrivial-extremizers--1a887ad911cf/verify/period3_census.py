"""Exact finite graph proof-checker for period-three reversible elementary CA.
Python 3 standard library only. Run: python verify/period3_census.py.
Every rule and every local triple is exhaustively checked. No floating arithmetic.
"""
import json
import hashlib


def bit(rule, a, b, c):
    return (rule >> (4*a + 2*b + c)) & 1


def transitions(rule):
    adj = [[] for _ in range(64)]
    for x in range(8):
        for y in range(8):
            aa, bb, cc = (y >> 2) & 1, (y >> 1) & 1, y & 1
            for z in range(8):
                a = ((x >> 2) & 1, aa, (z >> 2) & 1)
                b = ((x >> 1) & 1, bb, (z >> 1) & 1)
                c = (x & 1, cc, z & 1)
                if (bit(rule,*a)==(bb^cc) and
                    bit(rule,*b)==(aa^cc) and
                    bit(rule,*c)==(aa^bb)):
                    adj[8*x+y].append(8*y+z)
    return adj


def components(adj):
    index = 0
    stack = []
    onstack = set()
    indices = {}
    low = {}
    sccs = []
    def visit(v):
        nonlocal index
        indices[v]=low[v]=index
        index+=1
        stack.append(v)
        onstack.add(v)
        for w in adj[v]:
            if w not in indices:
                visit(w)
                low[v]=min(low[v],low[w])
            elif w in onstack:
                low[v]=min(low[v],indices[w])
        if low[v]==indices[v]:
            comp=[]
            while True:
                w=stack.pop();onstack.remove(w);comp.append(w)
                if w==v:break
            sccs.append(sorted(comp))
    for v in range(64):
        if v not in indices:visit(v)
    return sccs


def cyclic_components(adj):
    ans=[]
    for comp in components(adj):
        s=set(comp)
        e=sum(w in s for v in comp for w in adj[v])
        if len(comp)>1 or e>0:
            assert e>=len(comp)
            ans.append((comp,e))
    return ans


def traces(adj, lengths):
    out={}
    for n in lengths:
        total=0
        for start in range(64):
            x=[0]*64
            x[start]=1
            for _ in range(n):
                y=[0]*64
                for i in range(64):
                    for j in adj[i]:y[j]+=x[i]
                x=y
            total+=x[start]
        out[n]=total
    return out


def matmul(a,b):
    n=len(a)
    c=[[0]*n for _ in range(n)]
    for i in range(n):
        for k,v in enumerate(a[i]):
            if v:
                for j,w in enumerate(b[k]):
                    if w:c[i][j]+=v*w
    return c


def charpoly_by_newton(adj, comp):
    n=len(comp)
    where={v:i for i,v in enumerate(comp)}
    a=[[0]*n for _ in range(n)]
    for v in comp:
        for w in adj[v]:
            if w in where:a[where[v]][where[w]]+=1
    power=[[int(i==j) for j in range(n)] for i in range(n)]
    # det(tI-A) = t^n+c1*t^(n-1)+...+cn
    cs=[1]
    for k in range(1,n+1):
        power=matmul(power,a)
        pk=sum(power[i][i] for i in range(n))
        # Newton: k*c_k + sum_{j=1}^k c_{k-j}*p_j=0
        # store all traces for this computation
        if k==1: powers=[]
        powers.append(pk)
        val=-sum(cs[k-j]*powers[j-1] for j in range(1,k+1))
        assert val%k==0
        cs.append(val//k)
    return cs


def row_bound(adj,k=56):
    x=[1]*64
    for _ in range(k):x=[sum(x[j] for j in row) for row in adj]
    return max(x)


def main():
    classes={'exponential':[],'bounded':[],'empty':[]}
    table=[]
    maxratio=(0,0)
    char_data={}
    finite_counts=[]
    for r in range(256):
        adj=transitions(r)
        scc=cyclic_components(adj)
        if not scc:
            group='empty'
        elif any(e>len(comp) for comp,e in scc):
            group='exponential'
        else:
            group='bounded'
        classes[group].append(r)
        if r not in (50,51,76,204):
            value=row_bound(adj,56)
            assert value*(8**56)<(25**56), (r,value)
            if value>maxratio[0]:maxratio=(value,r)
        finite_counts.append(list(traces(adj,range(3,7)).values()))
        if r in (50,76):
            large=max(scc,key=lambda x:len(x[0]))
            assert len(large[0])==16
            cp=charpoly_by_newton(adj,large[0])
            # t^7 (t-1) (t^2+t+1)^2 (t^4-2t^3-2t^2-6t+3)
            def mult(p,q):
                z=[0]*(len(p)+len(q)-1)
                for i,x in enumerate(p):
                    for j,y in enumerate(q):z[i+j]+=x*y
                return z
            # ascending constant-to-leading coefficient
            pp=[3,-6,-2,-2,1]
            poly=mult(mult(pp,[-1,1]),mult([1,1,1],[1,1,1]))
            poly=[0]*7+poly
            assert cp==list(reversed(poly)), (r,cp,list(reversed(poly)))
            char_data[str(r)]=cp
        if r in (50,51,76,204,110,115,167,255):
            table.append({'rule':r,'class':group,'counts_3_to_8':list(traces(adj,range(3,9)).values())})
    assert [len(classes[x]) for x in ('exponential','bounded','empty')]==[129,116,11]
    assert classes['empty']==[167,173,181,189,191,229,231,239,247,253,255]
    assert classes['exponential'].__contains__(50) and classes['exponential'].__contains__(76)
    assert row_bound(transitions(50))*(8**56)>25**56
    assert row_bound(transitions(76))*(8**56)>25**56
    digest=hashlib.sha256(json.dumps(finite_counts,separators=(',',':')).encode('ascii')).hexdigest()
    out={'all_rule_counts_3_to_6_sha256':digest,'classes':{name:{'count':len(v),'rules':v} for name,v in classes.items()},
         'upper_bound':'For each rule outside 50,51,76,204: max row sum of A^56 *8^56 <25^56',
         'largest_other_rule_at_power56':maxratio[1],
         'largest_other_rule_power56_row_sum':str(maxratio[0]),
         'quartic':'t^4-2t^3-2t^2-6t+3',
         'charpoly_16node_50_76':char_data,'sample':table}
    print(json.dumps(out,separators=(',',':'),sort_keys=True))

if __name__=='__main__':main()
