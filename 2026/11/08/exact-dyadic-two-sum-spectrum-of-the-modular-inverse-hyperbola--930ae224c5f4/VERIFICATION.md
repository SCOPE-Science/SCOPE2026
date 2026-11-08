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

# Verification of the dyadic inverse-hyperbola two-sum spectrum

The exact checker is `verify.py`, embedded in this package. It runs without external dependencies. Its independent direct method first enumerates all ordered pairs \((x,y)\) of odd residues modulo \(2^k\), accumulating the two-coordinate vector sum multiplicities. Separately, it computes the predicted multiplicity at each of the \(2^{2k}\) targets using the square-congruence formula, and asserts equality for every target for \(1\le k\le9\). It checks the image cardinality formula, conservation of the total ordered pairs, and the previously known dyadic energy formula.

Observed success line: `VERIFY_OK levels=1..9 exact_target_comparisons= 349524 sumset_cardinalities=PASS energy_crosscheck=PASS`.

Exact finite image sizes for \(k=1,\ldots,9\): \(1,2,4,12,24,72,216,792,2904\). The results corroborate the algebraic proof but do not constitute an infinite verification. The proof in `RESULT.md` supplies the unrestricted derivation from unit inversion, complete squares and explicit 2-adic square counts.

The independent-audit field in this front matter indicates only that an independent mathematical audit was not performed. It does not certify the claim.
