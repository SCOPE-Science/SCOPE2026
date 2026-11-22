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

The proof reduces the Chevalley--Eilenberg complex to two commuting degree-zero \(GL_3\) root operators, decomposes it with the skew Cauchy identity, and calculates invariants and coinvariants on each highest-weight summand. These are general arguments, not finite enumerations.

To reproduce the independent finite sanity checks, run `python3 verify_k2n.py` with a standard Python 3 interpreter. It evaluates the binomial determinant formula for \(1\le n\le9\) and directly reconstructs the exterior differential and computes cohomology over finite fields for \(n=1,2,3\), using primes three and 101. Compare its stdout with `verification_output.txt`.

Finite-field agreement does not imply rational equality; in particular, it is not a substitute for the general proof. This package makes no integral-torsion assertion. The classification uses standard highest-weight theory and therefore assumes characteristic zero. Exact primary-source comparison covers the stated closest papers; unindexed prior variants remain a novelty risk.
