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

# Reproduction and mathematical boundary

Run `python3 check_cyclotomic.py` and `python3 check_finitefield.py` in the same directory; both use only the standard Python library and should print a `...CHECK_PASS` marker. The two programs iterate all \(2^8\) normalized length-nine binary windows and report exactly \((R,n_R)=(9,1),(21,3),(65,54),(69,81),(73,117)\).

`check_cyclotomic.py` applies the exact minimal-polynomial tests for primitive ninth and cubic roots and separately checks the \(27\)-pattern orbit partition. `check_finitefield.py` evaluates all \(81\) raw ambiguity sums per window at a primitive ninth root in \(\mathbb F_{531613}\), after elementary primality and root-order checks. Its reduction is lossless: every nonzero integer combination of nine ninth roots with signed coefficients has nonzero algebraic norm of magnitude at most \(9^6=531441<531613\), so it cannot reduce to zero in that field. Distinct implementations give the same rank multiset.

This verifies the finite census and all critical arithmetic computations, not an independent audit. The proof in `RESULT.md` supplies the Weyl-rank relation, cyclotomic zero characterization, three-periodicity dichotomy, and orbit counting. The asserted rank is the complex-linear rank of the matrix-intensity lift, **not** Gabor synthesis rank or general phase-retrieval injectivity. No dimension other than nine or phase alphabet other than \(\{+1,-1\}\) is claimed.
