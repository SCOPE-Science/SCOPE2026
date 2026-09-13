import networkx as nx, itertools, time, sys
from collections import Counter

def all_cycles(G, maxlen=None):
    adj={u:list(G.neighbors(u)) for u in G.nodes()}
    nodes=sorted(G.nodes())
    N=len(nodes)
    cycles=set()
    def dfs(start, cur, path, visited):
        for nb in adj[cur]:
            if nb==start and len(path)>=3:
                if maxlen is not None and len(path)>maxlen:
                    continue
                L=len(path)
                best=None
                for i in range(L):
                    rot=tuple(path[(i+j)%L] for j in range(L))
                    rev=tuple(path[(i-j)%L] for j in range(L))
                    for cand in (rot,rev):
                        if best is None or cand<best:
                            best=cand
                cycles.add(best)
            elif nb not in visited and nb>start:
                if len(path)<N and (maxlen is None or len(path)<maxlen):
                    visited.add(nb); path.append(nb)
                    dfs(start,nb,path,visited)
                    path.pop(); visited.remove(nb)
    for s in nodes:
        dfs(s,s,[s],{s})
    return cycles

def min_cover_k(G, k=4, timelimit=60):
    cyc=list(all_cycles(G))
    all_edges=set(tuple(sorted(e)) for e in G.edges())
    edges=list(all_edges); eidx={e:i for i,e in enumerate(edges)}
    full=(1<<len(edges))-1
    def emask(c):
        L=len(c); m=0
        for i in range(L):
            m|=1<<(eidx[tuple(sorted((c[i],c[(i+1)%L])))])
        return m
    uniq={}
    for c in cyc:
        mm=emask(c); l=len(c)
        if mm not in uniq or l<uniq[mm]:
            uniq[mm]=l
    masks=list(uniq.keys()); lens=[uniq[m] for m in masks]
    oo=sorted(range(len(masks)),key=lambda i:lens[i])
    masks=[masks[i] for i in oo]; lens=[lens[i] for i in oo]
    best=[10**9]; bestt=[None]; t0=time.time(); calls=[0]; timed=[False]
    def dfs2(s, chosen, total, cov):
        calls[0]+=1
        if timed[0]:
            return
        if calls[0]%40000==0 and time.time()-t0>timelimit:
            timed[0]=True; return
        if cov==full:
            if total<best[0]:
                best[0]=total; bestt[0]=tuple(chosen)
            return
        if len(chosen)==k or total>=best[0]:
            return
        for i in range(s,len(masks)):
            l=lens[i]
            if total+l>=best[0]:
                break
            if masks[i]|cov==cov:
                continue
            chosen.append(i)
            dfs2(i+1,chosen,total+l,cov|masks[i])
            chosen.pop()
    dfs2(0,[],0,0)
    return best[0], bestt[0], masks, lens, len(cyc), timed[0]

def prism(n):
    G=nx.Graph(); G.add_nodes_from(range(2*n))
    for i in range(n):
        G.add_edge(i,(i+1)%n)
        G.add_edge(n+i,n+((i+1)%n))
        G.add_edge(i,n+i)
    return G

def gp(n,k):
    G=nx.Graph(); G.add_nodes_from(range(2*n))
    for i in range(n):
        G.add_edge(i,(i+1)%n)
        G.add_edge(n+i,n+((i+k)%n))
        G.add_edge(i,n+i)
    return G

if __name__=="__main__":
    for name,G in [("prism6",prism(6)),("prism7",prism(7)),("gp72",gp(7,2)),("gp82",gp(8,2))]:
        m=G.number_of_edges()
        best,bt,_,_,nc,timed=min_cover_k(G,4,timelimit=60)
        print(f"{name} n={G.number_of_nodes()} m={m} bound={8*m/5} ncyc={nc} opt4={best} ratio={best/m:.3f} timed={timed}", flush=True)
