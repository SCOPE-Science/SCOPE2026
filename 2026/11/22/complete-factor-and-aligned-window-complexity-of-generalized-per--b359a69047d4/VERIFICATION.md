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

# Verification and reproducibility

Run `python3 checks/exact_residue_checker.py` and `python3 checks/prefix_window_checker.py` from the directory containing this document. Both scripts use only the Python standard library; the exact output from the two runs is embedded alongside them.

The first script explicitly computes exhaustive factor sets of the infinite valuation word, rather than sampling a finite prefix: for \(2^J\) greater than the inspected factor length, each residue-class window has at most one position whose index plus one is divisible by \(2^J\). Cycling its higher binary valuation through all residues yields every actual factor. It checks 576 factor-set cardinalities over \(2\le q\le7\), \(1\le n\le96\), and 17,982 recurrence identities over \(2\le q\le7\), \(4\le n\le3000\).

The independent second script builds each word directly from the morphism and compares literal factors and *aligned* disjoint windows. It checks 120 factor counts and 120 window counts over \(2\le q\le6\), \(1\le n\le24\), on 32,768-symbol prefixes. Its finite horizon is deliberately restricted to the parameter range validated by its sample; it does not imply any result beyond that sample.

The unconditional conclusions are established by the five mathematical proof stages in `RESULT.md`: morphic recursion, parity-disjoint factor decomposition, closed-deficit induction, Chinese remainder alignment at odd lengths, and injective doubling of windows. Computation does not prove unbounded lengths. The scientific-priority concern regarding an earlier dyadic-only indexed result is discussed in `REVIEW.md`. No independent audit or external proof certification has been carried out.
