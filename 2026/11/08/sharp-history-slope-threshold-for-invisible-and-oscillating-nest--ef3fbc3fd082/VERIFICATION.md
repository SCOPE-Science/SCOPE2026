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

Run `python3 verify.py` from the directory containing the extracted files. The program uses only the standard-library `fractions.Fraction` class and asserts equality of all local formulas; it does not need network access.

Checks performed: 140 exact-rational triples of positive \(\eta,a,M\), the three regimes of \(q=\eta M\), explicit implicit fixed-point substitution, exact second-delay sign and trajectory difference, 25 nested orders in the subcritical and critical regimes, and sample verification of the long-time triangle-wave reference against the prescribed sign-feedback derivative away from switching times. The completed program reported PASS.

The parameter-uniform result, unique local implicit delay, and infinite all-order critical nesting claim follow from the analytical proof in RESULT.md; finite computations alone do not establish them. At \(q>1\) only order two and the implicit branch are classified locally. The global strict-regime result invokes the source's already-published Theorem 1.1 after verifying its assumptions.
