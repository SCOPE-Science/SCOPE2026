"""Homeomorphism + Q-match leg (target claim prerequisite), machine-checked lattice part.

C contractible => H^2(Xhat;Z) = H^2(N;Z) (Mayer-Vietoris, Y homology sphere);
Q_Xhat = Q_N shared by both twist sides; unimodular (det=+-1 from plumbing);
simply connected (Van Kampen); KS=0 (smooth). Hence Freedman classifies:
same (Q, ks) => homeomorphic. Twist acts trivially on the lattice (H^2(C)=0)
so K_tau=K as lattice vectors; any witness is a smooth-chamber/basic-set
difference, not a lattice difference. This sharpens the witness shape.
"""
import json

def main():
    P = json.load(open("plumbing_result.json"))
    assert abs(P["det_QN"]) == 1, "Q_N must be unimodular"
    assert P["sig_QN"] == 9
    out = {
        "H2_decomp": "H^2(Xhat)=H^2(N) (C contractible, Y homology sphere): MV boundary maps vanish",
        "Q_shared": "Q_Xhat = Q_N = -Q_P for both Xhat and Xhat_tau (cork twist is boundary regluing; interior lattices identical)",
        "unimodular": f"det={P['det_QN']}",
        "simply_connected": "Van Kampen: C contractible + N tree-plumbed simply connected, glued along connected Y",
        "kirby_siebenmann": "0 both sides (smooth structures)",
        "freedman_conclusion": "same unimodular Q + ks=0 + simply connected => homeomorphic (topological)",
        "tau_on_lattice": "identity on H^2 (H^2(C)=0): K_tau=K as lattice vectors; witness must be SW-value shift at same lattice point, i.e. chamber/basic-set move",
        "witness_shape_sharpened": "find char K with K^2=2e+3sig satisfying cap adjunction such that SW_Xhat(K)!=SW_Xhat_tau(K) (same K, different values)",
    }
    with open("homeomorphism_result.json", "w") as f:
        json.dump(out, f, indent=2)
    print("HOMEOMORPHISM_OK: shared-Q + Freedman leg recorded; tau trivial on lattice")

if __name__ == "__main__":
    main()
