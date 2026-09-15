"""Enumerate 2-vertex quivers with arrows a,b,c, t(a)=s(b), t(b)=s(c),
relations ab=0, bc=0. Check gentle degrees, properness (finite-dim via
cycle test), list nonzero paths, Euler matrix E(d) for arrow degrees
|a|=|c|=1-d, |b|=d, and Serre matrix S = E (E^T)^-1 over QQ."""
from itertools import product
from fractions import Fraction

def shapes():
    sols=[]
    for sa,sb,sg,tg in product([0,1],[0,1],[0,1],[0,1]):
        ta=sb; tb=sg
        verts={sa,ta,sb,tb,sg,tg}
        if verts!={0,1}: continue
        sols.append(dict(a=(sa,ta),b=(sb,tb),c=(sg,tg)))
    return sols

def indeg_outdeg(sh):
    ind={0:0,1:0}; out={0:0,1:0}
    for (s,t) in sh.values():
        out[s]+=1; ind[t]+=1
    return ind,out

def cycles_ok(sh):
    """properness: every oriented simple cycle contains ab or bc as consecutive subpath.
    Build adjacency with arrow labels; check all simple cycles up to length 4."""
    adj={0:[],1:[]}
    for name,(s,t) in sh.items(): adj[s].append((name,t))
    bad=[]
    # enumerate closed walks without repeated (vertex,path) blowup: simple cycles len<=4
    def dfs(v0,v,path,depth):
        if depth>0 and v==v0:
            # closed walk; check if it contains 'ab' or 'bc' consecutively (cyclically)
            seq=''.join(path)
            cyc=seq+seq
            if ('ab' not in cyc) and ('bc' not in cyc):
                bad.append(seq)
            # don't extend closed walks
        if depth==4: return
        for (nm,w) in adj[v]:
            # avoid immediate backtrack counting? allow all; bound depth
            # prune: avoid reusing same arrow more than twice
            if path.count(nm)>=2: continue
            dfs(v0,w,path+[nm],depth+1)
    for v0 in [0,1]:
        dfs(v0,v0,[],0)
    return bad

def nonzero_paths(sh, maxlength=12):
    """BFS all nonzero paths (avoid ab, bc substrings). Returns dict {(s,t): [degrees-as-(k,m) with deg=k+m*d]} and flag infinite."""
    adj={0:[],1:[]}
    degmap={'a':(1,-1),'b':(0,1),'c':(1,-1)}  # deg = k + m*d where |a|=1-d etc.
    for name,(s,t) in sh.items(): adj[s].append((name,t))
    paths={(0,):[],(1,):[]}  # not needed
    from collections import defaultdict
    by_endpoints=defaultdict(list)
    frontier=[(v, v, '', (0,0)) for v in [0,1]]  # (start,current,names,(k,m))
    count=0
    while frontier:
        nxt=[]
        for (s,v,names,(k,m)) in frontier:
            for (nm,w) in adj[v]:
                nn=names+nm
                if 'ab' in nn or 'bc' in nn: continue
                dk,dm=degmap[nm]
                by_endpoints[(s,w)].append((k+dk,m+dm))
                nxt.append((s,w,nn,(k+dk,m+dm)))
                count+=1
                if count>5000:
                    return by_endpoints, False  # infinite-dim (not proper)
        frontier=nxt
        # bound length by total names length
        if frontier and len(frontier[0][2])>maxlength and count>200:
            # check if still growing -> infinite
            return by_endpoints, False
    return by_endpoints, True

def euler(km_list,d):
    s=0
    for (k,m) in km_list:
        n=k+m*d
        s+= 1 if n%2==0 else -1
    return s

shs=shapes()
print(f"#shapes connected: {len(shs)}")
for i,sh in enumerate(shs):
    ind,out=indeg_outdeg(sh)
    gentle = all(ind[v]<=2 and out[v]<=2 for v in [0,1])
    bad=cycles_ok(sh)
    proper = (len(bad)==0)
    bp,fin=nonzero_paths(sh)
    npaths=sum(len(v) for v in bp.values())
    print(f"--- shape {i}: a:{sh['a'][0]}->{sh['a'][1]} b:{sh['b'][0]}->{sh['b'][1]} c:{sh['c'][0]}->{sh['c'][1]} "
          f"in={ind} out={out} gentle={gentle} proper_cyclefree={proper} fin={fin} npaths={npaths}")
    if bad: print(f"    bad cycles (no relation): {bad[:6]}")
    if fin:
        for d in [0,1]:
            E=[[0,0],[0,0]]
            for vi in [0,1]:
                for vj in [0,1]:
                    lst=bp.get((vj,vi),[])
                    # include lazy path when i==j
                    extra=[(0,0)] if vj==vi else []
                    E[vi][vj]=euler(extra+lst,d)
            print(f"    d={d} E={E} det={E[0][0]*E[1][1]-E[0][1]*E[1][0]}")
