"""Reproduction script: domination calculus for hypothesis graphs (n=5,6).
Verifies: (i) adjacent domination => leaf; (ii) nothing strictly <= leaf (no twins);
(iii) leaf-support maximal; (iv) every strict 3-chain pairwise nonadjacent;
(v) G0/G1 meet all target hypotheses. See output/WORKLOG.md.
"""
import itertools, json

def adj_of(n, edges):
    adj=[set() for _ in range(n)]
    for i,j in edges:
        adj[i].add(j); adj[j].add(i)
    return adj
def link(adj,v): return set(adj[v])
def star(adj,v): return set(adj[v])|{v}
def dom(adj,a,b): return link(adj,a) <= star(adj,b)
def connected(adj):
    seen={0}; stack=[0]
    while stack:
        u=stack.pop()
        for w in adj[u]:
            if w not in seen: seen.add(w); stack.append(w)
    return len(seen)==len(adj)
def triangle_free(adj):
    n=len(adj)
    for i in range(n):
        for j in adj[i]:
            if j>i and (adj[i]&adj[j]): return False
    return True
def leaves(adj): return [v for v in range(len(adj)) if len(adj[v])==1]
def has_SIL(adj):
    n=len(adj)
    for x in range(n):
        for y in range(x+1,n):
            if y in adj[x]: continue
            inter=link(adj,x)&link(adj,y)
            rem=set(inter); rest=[v for v in range(n) if v not in rem]
            seen=set()
            for s in rest:
                if s in seen: continue
                comp={s}; stack=[s]; seen.add(s)
                while stack:
                    u=stack.pop()
                    for w in adj[u]:
                        if w in rem: continue
                        if w not in seen: seen.add(w); comp.add(w); stack.append(w)
                if x not in comp and y not in comp: return True
    return False
def leaf_star_conn(adj,v):
    rem=star(adj,v); rest=[u for u in range(len(adj)) if u not in rem]
    if not rest: return True
    seen={rest[0]}; stack=[rest[0]]
    while stack:
        u=stack.pop()
        for w in adj[u]:
            if w in rem: continue
            if w not in seen: seen.add(w); stack.append(w)
    return len(seen)==len(rest)
def meets(adj):
    n=len(adj)
    if not connected(adj): return False
    if not triangle_free(adj): return False
    for c in range(n):
        if adj[c]==set(range(n))-{c}: return False
    L=leaves(adj)
    if not L: return False
    if any(link(adj,L[i])==link(adj,L[j]) for i in range(len(L)) for j in range(i+1,len(L))): return False
    if not all(leaf_star_conn(adj,v) for v in L): return False
    if not has_SIL(adj): return False
    return True

def all_graphs(n):
    edges=[(i,j) for i in range(n) for j in range(i+1,n)]
    m=len(edges)
    for mask in range(1<<m):
        adj=[set() for _ in range(n)]
        for k,(i,j) in enumerate(edges):
            if mask>>k & 1: adj[i].add(j); adj[j].add(i)
        yield adj

if __name__=="__main__":
    G0=adj_of(5,[(0,1),(1,2),(2,3),(3,0),(0,4)])
    G1=adj_of(6,[(0,3),(0,4),(1,3),(1,4),(2,3),(2,4),(3,5)])
    assert meets(G0) and meets(G1), "G0/G1 must meet hypotheses"
    total=0; v1=v2=v3=v4=0
    for n in [5,6]:
        for adj in all_graphs(n):
            if not meets(adj): continue
            total+=1; N=len(adj)
            for a in range(N):
                for b in range(N):
                    if a==b: continue
                    if dom(adj,a,b) and (a in adj[b]) and len(adj[a])!=1: v1+=1
                    if dom(adj,a,b) and len(adj[b])==1 and a!=b: v2+=1
            L=leaves(adj); S={next(iter(adj[v])) for v in L}
            for w in S:
                for u in range(N):
                    if u!=w and dom(adj,w,u): v3+=1
            for a in range(N):
                for b in range(N):
                    for c in range(N):
                        if len({a,b,c})<3: continue
                        if dom(adj,a,b) and dom(adj,b,c) and (not dom(adj,b,a)) and (not dom(adj,c,b)):
                            if (a in adj[b]) or (b in adj[c]) or (a in adj[c]): v4+=1; break
                    else: continue
                    break
    print(json.dumps({"total":total,"viol_adj_dom":v1,"viol_into_leaf":v2,"viol_max":v3,"adj_3chain":v4}))
    assert total==1620 and v1==0 and v2==0 and v3==0 and v4==0
    print("OK: all lemmas verified; chain lifts contain F2 via Stab(b,c) argument (see WORKLOG).")
