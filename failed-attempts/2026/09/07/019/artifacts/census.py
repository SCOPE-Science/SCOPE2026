"""Decide hypohamiltonicity + invariants for 109 reps. Incremental save."""
import sys, time, json, os
sys.path.insert(0,'/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-23/output/artifacts')
from pipeline_lib import *
from orbits_lib import *
import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher

ART="/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-23/output/artifacts"

def load_reps():
    with open(os.path.join(ART,"reps.json")) as f:
        return json.load(f)

if __name__=="__main__":
    reps=load_reps()
    print(f"loaded {len(reps)} reps", flush=True)
    results=[]
    # resume?
    out_path=os.path.join(ART,"census.json")
    done=set()
    if os.path.exists(out_path):
        with open(out_path) as f:
            old=json.load(f)
        for r in old:
            done.add(r["rep_index"])
        results=old
        print(f"resuming: {len(done)} done", flush=True)
    for entry in sorted(reps, key=lambda x: x["rep_index"]):
        ri=entry["rep_index"]
        if ri in done:
            continue
        t0=time.time()
        adj=adj_from_edgelist(26, [tuple(e) for e in entry["edgelist"]])
        assert is_cubic(adj)
        girth=bfs_girth(adj)
        # |Aut|
        Gnx=to_networkx(adj)
        tA=time.time()
        auts=list(GraphMatcher(Gnx,Gnx).isomorphisms_iter())
        aut_size=len(auts)
        tAut=time.time()-tA
        # snark: bridgeless (already) + non-3-edge-colorable?
        tC=time.time()
        try:
            colorable=is_3_edge_colorable(adj, time_limit=20.0)
        except TimeoutError:
            colorable=None
        tCol=time.time()-tC
        is_snark=(not colorable) if colorable is not None else None
        # Hamiltonicity of G (both solvers)
        tH=time.time()
        try:
            cycA_G=ham_cycle_A(adj, time_limit=30.0, return_cycle=True)
        except TimeoutError:
            cycA_G="TIMEOUT"
        try:
            cycB_G=ham_cycle_B(adj, time_limit=30.0, return_cycle=True)
        except TimeoutError:
            cycB_G="TIMEOUT"
        hamA_G=(cycA_G is not None and cycA_G!="TIMEOUT")
        hamB_G=(cycB_G is not None and cycB_G!="TIMEOUT")
        # agreement check
        agree_G=(hamA_G==hamB_G)
        # verify cycles if found
        if isinstance(cycA_G,list):
            assert verify_ham_cycle(adj,cycA_G), f"bad cycle A G rep {ri}"
        if isinstance(cycB_G,list):
            assert verify_ham_cycle(adj,cycB_G), f"bad cycle B G rep {ri}"
        # G-v checks
        hypo_candidate=(not hamA_G) and (not hamB_G) and agree_G
        # if G Hamiltonian, not hypo; record example cycle, skip G-v? For completeness, still check first non-Ham G-v? Audit says for each non-witness record either Ham cycle of G OR first non-Ham G-v. So if G Ham, obstruction = G cycle, no need G-v. But for table completeness, we can still note.
        # To save time, if G Ham (both agree), skip G-v enumeration (obstruction already).
        Gv_data=None
        first_nonham_v=None
        all_ham=True
        hypo=False
        hypotrace_G=None
        if hypo_candidate:
            # need all 26 G-v Hamiltonian
            all_hamA=True; all_hamB=True
            cyclesA={}; cyclesB={}
            for v in range(26):
                Gv=delete_vertex(adj,v)
                try:
                    cA=ham_cycle_A(Gv, time_limit=30.0, return_cycle=True)
                except TimeoutError:
                    cA="TIMEOUT"
                try:
                    cB=ham_cycle_B(Gv, time_limit=30.0, return_cycle=True)
                except TimeoutError:
                    cB="TIMEOUT"
                hA=(cA is not None and cA!="TIMEOUT")
                hB=(cB is not None and cB!="TIMEOUT")
                if hA!=hB:
                    print(f"WARNING rep {ri} v {v} solver disagreement A={hA} B={hB}", flush=True)
                if isinstance(cA,list):
                    assert verify_ham_cycle(Gv,cA)
                    cyclesA[str(v)]=cA
                if isinstance(cB,list):
                    assert verify_ham_cycle(Gv,cB)
                if not hA:
                    all_hamA=False
                    if first_nonham_v is None:
                        first_nonham_v=v
                if not hB:
                    all_hamB=False
            all_ham=all_hamA and all_hamB
            hypo=all_ham
            # store cycles (A) for witness; for non-witness store first obstruction
            if hypo:
                Gv_data={"cycles_A":cyclesA}
            else:
                Gv_data={"first_nonham_v":first_nonham_v}
        else:
            # G Hamiltonian (or disagreement/timeout): obstruction is G cycle if exists
            all_ham=None
            hypo=False
        # hypotraceability screen: G has Ham path? and all G-v have Ham path? (only if quick; use path solver with short limit)
        # For hypo witnesses, also check traceability? Hypohamiltonian => non-Ham but traceable? Actually hypohamiltonian graphs are traceable? No: hypohamiltonian G is non-Ham but G-v Ham => G has Ham path? Deleting? Hmm. We'll screen: does G have Ham path?
        try:
            trace_G=ham_path_solver(adj, time_limit=10.0)
        except TimeoutError:
            trace_G=None
        elapsed=time.time()-t0
        rec={
            "rep_index": ri,
            "meta_example": entry["meta_example"],
            "edgelist": entry["edgelist"],
            "invariant_key": entry["invariant_key"],
            "group_size": entry["group_size"],
            "girth": girth,
            "aut_size": aut_size,
            "aut_time": round(tAut,2),
            "edge_colorable_3": colorable,
            "is_snark": is_snark,
            "color_time": round(tCol,2),
            "ham_G_A": hamA_G if cycA_G!="TIMEOUT" else "TIMEOUT",
            "ham_G_B": hamB_G if cycB_G!="TIMEOUT" else "TIMEOUT",
            "agree_G": agree_G,
            "ham_cycle_G_A": cycA_G if isinstance(cycA_G,list) else None,
            "hypo_candidate_G_nonham": hypo_candidate,
            "all_Gv_ham": all_ham,
            "is_hypohamiltonian": hypo,
            "first_nonham_v": first_nonham_v,
            "Gv_cycles_or_obstruction": Gv_data,
            "trace_G_has_hampath": trace_G,
            "elapsed": round(elapsed,1),
        }
        results.append(rec)
        # incremental save
        with open(out_path,"w") as f:
            json.dump(results,f,indent=1)
        print(f"rep {ri}: girth={girth} |Aut|={aut_size} colorable={colorable} hamG_A={hamA_G} hamG_B={hamB_G} hypo={hypo} traceG={trace_G} elapsed={elapsed:.1f}s ({len(results)}/{len(reps)})", flush=True)
    # summary
    hypos=[r for r in results if r["is_hypohamiltonian"]]
    print(f"DONE: {len(results)} reps, {len(hypos)} hypohamiltonian: {[r['rep_index'] for r in hypos]}", flush=True)
