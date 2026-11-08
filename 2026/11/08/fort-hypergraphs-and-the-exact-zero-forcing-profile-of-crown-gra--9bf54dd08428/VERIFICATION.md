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

# Verification of crown-graph fort and zero-forcing formulas

Run `python3 verify.py` from the directory containing the source. The program requires Python 3 and only its standard library; it constructs the graph from the exact adjacency rule, checks all nonempty fort candidates, and performs the forcing rule on every initial blue subset. It tests all subsets of the crown graphs with \(3\le n\le8\), including exactly 87,360 labelled subsets, finding 3,037 zero-forcing sets and 66,243 forts. For every \(n\) in that range it verifies the exact polynomial coefficient profile, the list of minimal forts, and the completeness of the obstruction description.

The standalone verifier also computes the largest family of pairwise disjoint forts by an independent subset dynamic program for \(3\le n\le7\), agreeing with \(\lfloor2n/3\rfloor\). Numerical linear-program comparisons for \(3\le n\le8\) agreed with \(Z^*=2n/3\), but these numerical checks are not the basis for the unrestricted claim and are not part of the standalone program.

The complete mathematical proof, independent of finite experiments, appears in `RESULT.md`. The critical unrestricted steps are the exact external-neighbor formula, classification of forts of sizes at most four, the fort-obstruction equivalence for zero forcing, a disjoint-fort construction, and matching feasible/dual fractional certificates.

No third-party mathematical audit or formal proof-system validation has been performed. A successful computer run does not certify publication priority.
