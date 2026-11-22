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
# Verification
The proof derives all claims analytically from the established higher-rank supporting half-plane theorem. The accompanying standard-library checker tests 110 pseudo-random positive-weight/center tuples, each against 51 supporting directions, and verifies explicit complex isometry/compression identities. All finite testing is supplementary; it neither checks every real parameter nor establishes priority.

The exact eigenvalue candidates for the Hermitian pencil are \(r,-r,u+s,u-s\), where \(u=|\beta-\alpha|\cos\theta\). The checker compares their sorted second value to the proof's three-case expression. It independently multiplies the \(4\times4\) operator and \(4\times2\) isometry in Python complex arithmetic and checks the result against the asserted weighted barycenter.

Reproduce with `python3 verify.py`. No third-party Python dependencies, network access, or separate files are required. If a check fails, the program raises an assertion rather than logging success. The independent audit remains unperformed.
