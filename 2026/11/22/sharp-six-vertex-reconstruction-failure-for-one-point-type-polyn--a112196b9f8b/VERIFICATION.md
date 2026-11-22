---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and verification

Run `python3 verify.py` using Python 3.9 or later; only the standard library is required. The bundled `verification_output.txt` records an actual successful run. The enumerator constructs all 2-trees up to six vertices from an initial edge using all possible old edges, deduplicates by minimizing labelled edge sets over every vertex permutation, and evaluates both triangle-freeness and independent cycle-detection algorithms on each induced subset. The outputs give class counts \(1,1,1,2,5\) at orders \(2,3,4,5,6\), with collision-pair counts \(0,0,0,0,1\). The script checks the actual six-point witnesses, distinguished-edge restricted polynomials, and fan expansions through \(t=8\).

The proof of the identity for every \(t\ge0\) is purely combinatorial: partition admissible old subsets according to whether they contain both endpoints of the fixed edge. The nonisomorphism for every \(t\) follows from the two distinct degree multisets. Thus the finite verification is not used as an infinite proof. No formal theorem prover or independent mathematical audit has been used. Historical novelty cannot be certified from finite computational checks or database absence.
