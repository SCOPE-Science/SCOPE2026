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

The complete self-contained Python 3 checker is `verify.py`; it requires only the standard library. Execute `python3 verify.py` from the directory containing that file.

The checked execution returned:

`VERIFY_OK exact_triangle_cases=6 reconstruct_checks=6 sharp_envelope_samples=750 random_pair_trials=170000`

For the \(3\)-\(4\)-\(5\) test triangle the exact targets were \(\mathbb E[D^2]=11/2\) and \(\mathbb E[D^4]=2503/45\). The independent random-pair simulation gave approximately \(5.51154\) and \(55.82112\), respectively, against exact values \(5.5\) and \(55.62222\).

The rational tests compute side-conditioned moment integrals independently of the compact closed forms. The sampled sharp-envelope checks and Monte Carlo checks are finite stress tests only, not proofs of infinite-domain statements. The analytic proof and isosceles extremizer classification appear in `RESULT.md`.

Limitations: exact population moments and a known perimeter are assumed; conditioning and noise are not controlled uniformly as area vanishes. Historical novelty has not undergone independent verification.
