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
# Reproduction and scope

The proof in `RESULT.md` is independent of finite enumeration. Run `python check.py` with Python 3 and SymPy 1.14 or compatible. The checker verifies both quotient cubic identities and the CM-invariant equation by exact polynomial reduction modulo \(d^4-5\), then computes the \(2\times2\) Hasse–Witt matrix for each odd prime \(3\le p<200\), \(p\ne5\). In each checked characteristic it confirms that the matrix is invertible in the split residue classes and identically zero in the inert classes. No finite range implies the all-prime theorem; that part follows from the explicit prime-to-\(p\) isogeny and classical CM reduction. The checks do not establish historical priority, which remains qualified.
