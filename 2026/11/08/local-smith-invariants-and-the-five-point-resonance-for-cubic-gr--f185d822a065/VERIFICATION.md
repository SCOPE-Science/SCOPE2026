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

The derivation gives exact local valuations with the normalization \(v_\pi(\zeta-1)=1\). The matrix includes the zero row and zero column; its trivial character sector is not discarded. The p-adic unit character table and the strictly sub-\(p-1\) leading coefficient orders make the diagonalization and modular coefficient test exact.

Reproduce by running `python3 verify.py` (Python standard library only). The script constructs the full matrix over the truncated local ring \(\mathbb F_p[\pi]/(\pi^{p-1})\), performs valuation-minimal Smith elimination, and checks predicted finite exponent multisets. It tests six prime sizes (5 through 19, listed in the code), all nonzero cubic curvatures at primes 7 and 11, and all four curvatures at prime 5. The reported exponent \(p-1\) is a truncation bound, not an exact exponent: the proof's cyclotomic identity establishes exact singularity at the two exceptional five-point curvatures.

No test over finitely many primes verifies the theorem for all primes; the cyclotomic and character-orthogonality argument supplies the universal proof. Independent audit has not been performed.
