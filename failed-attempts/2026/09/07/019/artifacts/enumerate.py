"""Full enumeration B18 x P10 order-26 both orientations, dedup, save reps."""
import sys, time, json
sys.path.insert(0,'/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-23/output/artifacts')
from pipeline_lib import *
from orbits_lib import *
from gen_cands import invariant_key
import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher
from collections import defaultdict

def build_seeds():
    P=petersen_adj()
    pairsP=independent_edge_pairs(P)
    autsP=all_automorphisms(P)
    repsPE,_=edge_pair_orbits(P,pairsP,autsP)
    vpP=adjacent_vertex_pairs(P)
    repsPV,_=vertex_pair_orbits(P,vpP,autsP)
    candsPP=[]
    for ri in repsPE:
        ab,cd=pairsP[ri]
        for rj in repsPV:
            x,y=vpP[rj]
            for w in range(8):
                candsPP.append(dot_product(P,P,ab,cd,x,y,w))
    repsPP,groupsPP=dedup_graphs(candsPP)
    B_adjs=[candsPP[r] for r in repsPP]
    def aut_size(a):
        G=to_networkx(a)
        return len(list(GraphMatcher(G,G).isomorphisms_iter()))
    sizes=[aut_size(a) for a in B_adjs]
    order=sorted(range(len(B_adjs)), key=lambda i: sizes[i])
    B1=B_adjs[order[0]]; B2=B_adjs[order[1]]
    J=flower_j5_adj()
    return P,B1,B2,J

if __name__=="__main__":
    t0=time.time()
    P,B1,B2,J=build_seeds()
    print(f"seeds built in {time.time()-t0:.1f}s", flush=True)
    print(f"P n={len(P)} girth={bfs_girth(P)}", flush=True)
    print(f"B1 girth={bfs_girth(B1)} B2 girth={bfs_girth(B2)} J girth={bfs_girth(J)}", flush=True)
    # orbit reps
    autsP=all_automorphisms(P)
    pairsP=independent_edge_pairs(P)
    repsPE,_=edge_pair_orbits(P,pairsP,autsP)
    vpP=adjacent_vertex_pairs(P)
    repsPV,_=vertex_pair_orbits(P,vpP,autsP)
    print(f"P: edge-orbits {len(repsPE)} vertex-orbits {len(repsPV)}", flush=True)
    all_cands=[]; all_meta=[]
    # Orientation A: B edge-factor, P vertex-factor
    for Bi,blabel in [(B1,"B18_1"),(B2,"B18_2")]:
        autsB=all_automorphisms(Bi)
        pairsB=independent_edge_pairs(Bi)
        repsB,_=edge_pair_orbits(Bi,pairsB,autsB)
        # P vertex side single orbit
        for ri in repsB:
            ab,cd=pairsB[ri]
            for rj in repsPV:
                x,y=vpP[rj]
                for w in range(8):
                    G=dot_product(Bi,P,ab,cd,x,y,w)
                    all_cands.append(G)
                    all_meta.append({"edge_factor":blabel,"vertex_factor":"P10","ab":list(ab),"cd":list(cd),"x":x,"y":y,"wiring":w, "orientation":"B.P"})
    print(f"Orientation B.P candidates: {len(all_cands)}", flush=True)
    # Orientation B: P edge-factor, B vertex-factor
    nA=len(all_cands)
    for Bi,blabel in [(B1,"B18_1"),(B2,"B18_2")]:
        autsB=all_automorphisms(Bi)
        vpB=adjacent_vertex_pairs(Bi)
        repsVB,_=vertex_pair_orbits(Bi,vpB,autsB)
        for ri in repsPE:
            ab,cd=pairsP[ri]
            for rj in repsVB:
                x,y=vpB[rj]
                for w in range(8):
                    G=dot_product(P,Bi,ab,cd,x,y,w)
                    all_cands.append(G)
                    all_meta.append({"edge_factor":"P10","vertex_factor":blabel,"ab":list(ab),"cd":list(cd),"x":x,"y":y,"wiring":w, "orientation":"P.B"})
    print(f"Orientation P.B additional: {len(all_cands)-nA}, total orbit-rep candidates: {len(all_cands)}", flush=True)
    # bridgeless filter
    t1=time.time()
    bridgeless_idx=[]
    for i,G in enumerate(all_cands):
        Gn=to_networkx(G)
        if len(list(nx.bridges(Gn)))==0:
            bridgeless_idx.append(i)
    print(f"bridgeless: {len(bridgeless_idx)}/{len(all_cands)} in {time.time()-t1:.1f}s", flush=True)
    # invariant buckets
    t1=time.time()
    buckets=defaultdict(list)
    keys={}
    for i in bridgeless_idx:
        k=invariant_key(all_cands[i])
        keys[i]=k
        buckets[k].append(i)
    print(f"invariant buckets: {len(buckets)} in {time.time()-t1:.1f}s", flush=True)
    for k,v in sorted(buckets.items(), key=lambda x: -len(x[1]))[:15]:
        print(f"  key {k}: {len(v)}", flush=True)
    # dedup within buckets via isomorphism
    t1=time.time()
    reps=[]; groups={}
    rep_nx={}
    # global reps list (indices into all_cands)
    for k,idxs in buckets.items():
        # dedup within bucket
        breps=[]
        bnx=[]
        for i in idxs:
            Gi=to_networkx(all_cands[i])
            found=None
            for bj,br in enumerate(breps):
                if GraphMatcher(Gi,bnx[bj]).is_isomorphic():
                    found=br
                    groups[br].append(i)
                    break
            if found is None:
                breps.append(i); bnx.append(Gi); groups[i]=[i]
        reps.extend(breps)
        # store nx for cross-bucket? No cross-bucket needed since invariants differ => non-isomorphic. But to be safe, verify cross-bucket non-isomorphic? Invariants are isomorphism-invariant, so different keys => non-isomorphic. Safe.
    print(f"distinct bridgeless types (union over buckets): {len(reps)} in {time.time()-t1:.1f}s", flush=True)
    # cross-check: ensure reps from different buckets are indeed non-isomorphic? They must be since key differs. No need.
    # But to guard against invariant bug, do a second pass: verify no two reps are isomorphic (sample check across buckets with same girth? Actually keys differ => cannot be isomorphic if key correct. Verify key correctness by checking isomorphic pairs share key (we already bucketed). For safety, run pairwise across reps with same girth? That's up to ~? Let's do full pairwise across reps to be rigorous (reps maybe few hundred, pairwise ~ tens of thousands, feasible).
    t1=time.time()
    # full pairwise dedup verification (independent path: different order + re-hash)
    # Use WL? No, use direct pairwise with early invariant filter
    reps_sorted=sorted(reps)
    # verify pairwise non-isomorphic
    ok=True
    for a in range(len(reps_sorted)):
        for b in range(a+1,len(reps_sorted)):
            i=reps_sorted[a]; j=reps_sorted[b]
            if keys[i]!=keys[j]:
                continue
            # same bucket already checked, should not happen (we deduped). Double-check:
            Gi=to_networkx(all_cands[i]); Gj=to_networkx(all_cands[j])
            if GraphMatcher(Gi,Gj).is_isomorphic():
                print(f"ERROR: reps {i},{j} isomorphic but both kept!", flush=True)
                ok=False
    print(f"pairwise verification within buckets done in {time.time()-t1:.1f}s, ok={ok}", flush=True)
    # save
    import os
    os.makedirs("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-23/output/artifacts", exist_ok=True)
    # save seeds
    with open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-23/output/artifacts/seeds.json","w") as f:
        json.dump({
            "P10": edgelist_from_adj(P),
            "B18_1": edgelist_from_adj(B1),
            "B18_2": edgelist_from_adj(B2),
            "J5": edgelist_from_adj(J),
        }, f, indent=1)
    # save reps
    rep_data=[]
    for r in sorted(reps):
        rep_data.append({
            "rep_index": r,
            "meta_example": all_meta[r],
            "edgelist": edgelist_from_adj(all_cands[r]),
            "invariant_key": list(keys[r]),
            "group_size": len(groups[r]),
            "group_members": sorted(groups[r]),
        })
    with open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-23/output/artifacts/reps.json","w") as f:
        json.dump(rep_data, f, indent=1)
    with open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-23/output/artifacts/cands_meta.json","w") as f:
        json.dump({"total_orbit_candidates": len(all_cands), "bridgeless": len(bridgeless_idx), "distinct": len(reps),
                   "orientation_counts": {"B.P": nA, "P.B": len(all_cands)-nA}}, f, indent=1)
    print(f"TOTAL time {time.time()-t0:.1f}s", flush=True)
