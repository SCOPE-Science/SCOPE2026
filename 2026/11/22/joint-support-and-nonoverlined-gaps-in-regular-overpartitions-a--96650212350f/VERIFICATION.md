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

# Reproducibility and limits

Run `python3 verify.py` with Python 3. This requires only the standard library. It independently enumerates all admissible overpartitions through \(n=12\) for \(2\le\ell\le6\); evaluates the constrained generating factors; verifies the exact coincidence count and gives finite trends through \(n=500\). Expected final output: `PASS: 520 exact coefficient and exhaustive marked-multiset comparisons; finite convergence illustration`.

The exact generating identities have elementary combinatorial proofs. The infinite limit and the first-order lattice coincidence correction are supported by the Fourier/saddlepoint proof in RESULT.md, not by the finite checker. No independent audit has been performed, no peer review is asserted, and no external certification is claimed.
