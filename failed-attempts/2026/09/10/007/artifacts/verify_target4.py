"""Target lemma audit 4 (TARGET phase): infinite-order vs vanishing distinction.

Proves (reproducibly) the sharp logical split inside target pursuit:
 I1. Twist-knot Alexanders for k=0..8 are pairwise distinct Laurent
     polynomials (exact sympy) => quoted FS98 distinguishes the knot
     surgeries E(n)_Kk pairwise (n>=2, b2+>1 sharp) => Teng infinite-order
     boundary twist (all powers nontrivial) is CONDITIONALLY certified
     given Teng's E(n) embedding + FS quote.
 I2. None of k>=1 has Alexander 1 => FS formula can NEVER yield SW=0 from
     SW-nontrivial base => the target's exact "+/-1 vs 0" vanishing shape
     is unreachable through the Gompf torus-twist/knot-surgery mechanism
     that Teng's construction uses. Vanishing needs a DIFFERENT mechanism
     (rational/PSC identification), unsourced for Teng W_1.
 I3. Formal blocker list for target closure (all must close; none does).

Quoted: FS98 knot-surgery diffeomorphism distinction + formula; Teng E(n)
embedding (n>=2); E(n) b2+ = 2n-1 > 1 for n>=2.
"""
import json
import sympy as sp

out = {"tables": {}, "checks": {}}
t = sp.symbols('t')

def alex(k):
    return sp.expand(k*t - (2*k-1) + k/t)

polys = {k: alex(k) for k in range(9)}
# pairwise distinct?
vals = list(polys.values())
distinct = len(set(vals)) == len(vals)
out["tables"]["twist_knot_alexanders"] = {str(k): str(polys[k]) for k in polys}
out["checks"]["I1_pairwise_distinct_k0_8"] = distinct
out["checks"]["I2_no_Alex1_for_k>=1"] = all(polys[k] != 1 for k in range(1, 9))
out["tables"]["I2_values"] = {"k=0": str(polys[0]),
    "note": "only k=0 (unknot = trivial twist) has Alexander 1"}
out["tables"]["I3_blockers"] = {
    "B1_embedding": "no source: Teng C(1,1;-1)/C_m into E(1)_{2,3} nucleus "
                    "(Teng: E(n) n>=2 via 6n vanishing cycles)",
    "B2_identification": "no source: Teng-twist X_f diffeomorphism type "
                    "(sourced vanishing twist is Akbulut positron/Wbar_1 -> E(1))",
    "B3_correspondence": "K_f<->K_X needs -F off W_1 (unsourced)",
    "B4_chamber": "b2+=1 chamber of K_f unspecified",
    "B5_mechanism": "knot-surgery route provably cannot give SW=0 (I2)",
    "B6_clause": "literal Q_X clause defective as written (audit3 P1/P2)",
}
out["checks"]["target_closed"] = False
out["checks"]["infinite_order_conditional"] = bool(distinct)

with open("output/artifacts/target_audit4.json", "w") as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1))
print("ARTIFACT_WROTE output/artifacts/target_audit4.json")
