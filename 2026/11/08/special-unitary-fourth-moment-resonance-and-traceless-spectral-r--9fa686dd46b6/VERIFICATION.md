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
# Verification and scope

Execute `python su4_fourth_checker.py` with Python 3, SymPy and NumPy installed. This script computes the two-pair unitary Weingarten inverse from its Gram matrix, checks the determinant contraction using the alternating tensor, checks 12,000 exact rational diagonal parameter profiles, including the tracezero Hermitian reduction, and generates 48,000 numerical Haar samples on \(\mathrm{SU}(4)\) by unitary QR decomposition with determinant-one normalization. It checks the unrestricted rank-one and full-rank endpoints, both traceless-Hermitian endpoints, and a negative-determinant intermediate profile.

The expected final line is `ALL_SU4_FOURTH_MOMENT_CHECKS_PASSED`. The numerical tolerance is \(0.20\) for fourth-moment ratios because of Monte Carlo fluctuations. These calculations do not certify the universal inequalities or historical novelty. The universal proof is the invariant-theory reduction followed by AM--GM and the exact eigenvalue-parameter optimization in `RESULT.md`.

Status: self-reviewed; independent mathematical audit not performed.
