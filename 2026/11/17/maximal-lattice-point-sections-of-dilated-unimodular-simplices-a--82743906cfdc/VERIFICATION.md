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

# Reproducible checks

Run `python verify.py` using Python 3 and no external packages. It performs exact rational reduced-row-echelon computations to enumerate all affine lattice-point-spanned \(\ell\)-flats for the finite test cases, then checks their lattice-point counts and the face-hull identities. The returned counts are 18 test cases, 2,499 distinct affine flats, with all assertions passing.

The proof in `RESULT.md` is the certificate for **every** integer \(d\ge2\), \(k\ge1\) and \(1\le\ell\le d-1\). Finite tests neither justify the quantifiers nor establish historical novelty. The conjecture comparison concerns exact degree, not eventual quasi-polynomiality or an at-most-degree variant. Independent mathematical audit has not been performed.
