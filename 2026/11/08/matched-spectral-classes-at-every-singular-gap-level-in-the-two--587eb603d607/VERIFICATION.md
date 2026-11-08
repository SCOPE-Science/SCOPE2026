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

# Reproducibility and scientific limits

Run `python check_twisted_joint.py` with Python 3. The program was executed from the package source and printed `CHECK_OK 4083 finite word/periodic geometry/spectrum identities across n=1..11`. For each word up to length eight, it independently solves the affine periodic-point equation with exact fractions and verifies the branch signs and return. For lengths through eleven it checks the integer derivative products, both gap indices, and complete joint binomial histograms. The mathematical proof above establishes the arbitrary-length statement via exact parity and binomial identities; finite tests cannot establish it alone.

Mathematical inputs: the symbolic fixed-point coding and absence of periodic boundary points in Saiki--Takahasi--Yorke, arXiv:2202.04304, Lemmas 2.4--2.6. Independently derived: signed monomial stretch coding, binomial histogram symmetry, one-word correction, joint Gaussian weak limit. The result covers iterate-fixed-point counting, not just primitive periods. No external mathematical audit has been performed.
