#!/usr/bin/env python3
"""Exact certificates for the first and second full-shift images of ECA 22.
Pure Python 3, no external packages. Run with: python rule22_verify.py CERTIFICATE.json
"""
import json,sys,hashlib
from collections import defaultdict

def local3(a,b,c):
    return (22 >> (4*a+2*b+c)) & 1

def local_at_time(word, t):
    for _ in range(t):
        word=[local3(word[j],word[j+1],word[j+2]) for j in range(len(word)-2)]
    assert len(word)==1
    return word[0]

def determinize(t):
    width=2*t; vcount=1<<width
    dt=[[0,0] for _ in range(vcount)]
    for v in range(vcount):
        bits=[(v>>(width-1-j))&1 for j in range(width)]
        for a in (0,1):
            output=local_at_time(bits+[a],t)
            dest=((v<<1)&(vcount-1))|a
            dt[v][output] |= 1<<dest
    full=(1<<vcount)-1
    masks=[full]; index={full:0}; edges=[]
    for mask in masks:
        row=[]
        for sym in (0,1):
            nxt=0; b=mask
            while b:
                bit=b&-b; b-=bit
                nxt |= dt[bit.bit_length()-1][sym]
            if nxt not in index:
                index[nxt]=len(masks);masks.append(nxt)
            row.append(index[nxt])
        edges.append(row)
    return masks,edges

def minimize(masks,edges):
    colors=[int(s!=0) for s in masks]
    for _ in range(len(masks)+1):
        keys=[(colors[i],colors[edges[i][0]],colors[edges[i][1]]) for i in range(len(masks))]
        classes={key:i for i,key in enumerate(sorted(set(keys)))}
        new=[classes[key] for key in keys]
        if new==colors:
            break
        colors=new
    else:raise AssertionError('non-convergent partition refinement')
    representatives={c:colors.index(c) for c in sorted(set(colors))}
    classid={c:i for i,c in enumerate(representatives)}
    states=[masks[representatives[c]] for c in representatives]
    transitions=[[classid[colors[edges[representatives[c]][a]]] for a in (0,1)] for c in representatives]
    start=classid[colors[0]]
    # Verify all states in the same class have the same acceptance and transition classes.
    for i in range(len(masks)):
        j=classid[colors[i]]
        assert bool(masks[i])==bool(states[j])
        assert transitions[j]==[classid[colors[edges[i][a]]] for a in (0,1)]
    return states,transitions,start

def sccs(states,edges):
    # Tarjan decomposition of the nonempty-state graph.
    order={};low={};stack=[];onstack=set();blocks=[];clock=[0]
    def visit(v):
        order[v]=clock[0];low[v]=clock[0];clock[0]+=1
        stack.append(v);onstack.add(v)
        for w in edges[v]:
            if states[w]==0:continue
            if w not in order:
                visit(w);low[v]=min(low[v],low[w])
            elif w in onstack:low[v]=min(low[v],order[w])
        if low[v]==order[v]:
            comp=[]
            while True:
                w=stack.pop();onstack.remove(w);comp.append(w)
                if w==v:break
            blocks.append(sorted(comp))
    for i,v in enumerate(states):
        if v and i not in order:visit(i)
    blocks.sort(key=lambda b:(-len(b),min(b)))
    return blocks

def exact_bounds(edges,core,power,lo,hi):
    # B is the integer adjacency matrix inside the strongly connected class.
    pos={v:i for i,v in enumerate(core)}
    rows=[[pos[w] for w in edges[v] if w in pos] for v in core]
    assert all(row for row in rows)
    v=[1]*len(core)
    for _ in range(power):v=[sum(v[j] for j in row) for row in rows]
    vnext=[sum(v[j] for j in row) for row in rows]
    # exact rational Collatz-Wielandt bounds: lo < rho(B) < hi
    assert all(v[i]*lo.denominator*hi.denominator>0 for i in range(len(v)))
    assert all(vnext[i]*lo.denominator>v[i]*lo.numerator for i in range(len(v)))
    assert all(vnext[i]*hi.denominator<v[i]*hi.numerator for i in range(len(v)))
    return v,rows

def named_words(t,n):
    masks,edges=determinize(t)
    start=0
    # Enumerate binary output words by following deterministic transitions.
    result=[]
    for a in range(1<<n):
        m=start
        for j in range(n-1,-1,-1):
            bit=(a>>j)&1;m=edges[m][bit]
        if masks[m]:result.append(format(a,'0%db'%n))
    return result

def counts_from_graph(masks,edges,nmax=18):
    v=[0]*len(masks);v[0]=1
    ret=[]
    for n in range(1,nmax+1):
        nxt=[0]*len(masks)
        for s,weight in enumerate(v):
            if not weight:continue
            for q in edges[s]:
                if masks[q]:nxt[q]+=weight
        v=nxt;ret.append(sum(v))
    return ret

def main(path):
    from fractions import Fraction
    with open(path,encoding='utf-8') as f: cert=json.load(f)
    assert cert['rule']==22 and cert['spatial_shift']=='two_sided_full_shift'
    expectedcounts={1:[2,4,8,16,32,64,128,254,500,981,1917,3732,7252,14062,27211,52595,101536,195787],
                    2:[2,4,8,16,32,64,126,246,477,926,1788,3428,6552,12478,23691,44918,84994,160499]}
    expected_sizes={1:(16,16,15),2:(361,281,273)}
    for t in (1,2):
        masks,edges=determinize(t)
        states,medges,start=minimize(masks,edges)
        blocks=sccs(states,medges)
        core=blocks[0]
        assert (len(masks),len(states),len(core))==expected_sizes[t]
        assert any(masks[i]==0 for i in range(len(masks)))
        assert start==cert[str(t)]['start']
        assert states==cert[str(t)]['states']
        assert medges==cert[str(t)]['transitions']
        assert core==cert[str(t)]['core']
        assert counts_from_graph(masks,edges)==expectedcounts[t]
        # One dominant essential component; every other recurrent singleton has <=1 loop.
        for bl in blocks[1:]:
            assert len(bl)==1
            s=bl[0]
            assert medges[s].count(s)<=1
        lo,hi=map(lambda a:Fraction(int(a),100000),cert[str(t)]['bounds_1e5'])
        v,rows=exact_bounds(medges,core,99,lo,hi)
        assert [str(z) for z in v]==cert[str(t)]['pf_vector_B99']
        assert [len(rows),sum(len(z) for z in rows)]==cert[str(t)]['core_matrix_shape_edges']
        print('time',t,'subset_states',len(masks),'minimal_states',len(states),
              'core_size',len(core),'bounds',lo,hi,'n18',expectedcounts[t][-1],
              'PF vector SHA256',hashlib.sha256(','.join(map(str,v)).encode()).hexdigest())
    for n in range(1,7):assert len(named_words(2,n))==(1<<n)
    A=set(named_words(1,7)); B=set(named_words(2,7))
    assert len(A)==128 and A-B=={'1010111','1110101'} and len(B)==126
    print('first obstruction',sorted(A-B))
    print('PASS: exact integer spectral enclosures and all-language counts')
if __name__=='__main__':
    if len(sys.argv)!=2:raise SystemExit('usage: python rule22_verify.py CERTIFICATE.json')
    main(sys.argv[1])
