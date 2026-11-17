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
# Verification record

The analytical argument is in `RESULT.md` and is the evidence for the all-direction theorem. A standalone computational cross-check is included as `check.py`; it uses Python 3, NumPy, SciPy and no network access.

Running `python check.py` produced: `PASS 80183 finite checks; exact squared three-center radius 21/64`.

The program checks three exact contact cases, 40,000 sampled unit vectors with two inequalities each, 60 independently sampled pairs of trace-zero symmetric matrices with three residual tests each, and three rational identities. The random seed is fixed in the script. These numerical checks do not establish an infinite covering or the all-matrix common-zero lemma; those follow from the self-contained deterministic proof in `RESULT.md`.

The analysis assumes the five-dimensional Frobenius metric, three-by-three real symmetric matrices, and Euclidean balls. The exact optimal three-ball radius and a three-ball cover of the convex hull remain unproved.
