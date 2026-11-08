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
# Finite verification and proof obligations

From an extracted directory containing `RESULT.md` and `verify.py`, execute `python3 verify.py` using Python 3. The reference execution returned `VERIFICATION_OK 1752 exact rational assertions`.

The checker computes skew-standard-tableau counts by corner deletion, verifies the count-square dimension identity, derives exact probabilities of each one-step permutation independently from the moved support and chosen-subset law, and matches exact trace moments from permutation convolution and the proposed Fourier eigenvalues for every \(2\le n\le6\). It tests point-mass sizes, independent Bernoulli marking, and a non-binomial exchangeable size distribution.

The all-\(n\) argument relies instead on two mathematical facts shown in `RESULT.md`: Young branching identifies subgroup-fixed dimensions, and the injection that moves a chosen minimal element left by one position in a linear extension yields a sharp tableau inequality. These arguments prove the claimed full spectrum and gap independently of finite testing.

Limitations: the checker is finite, so it cannot certify an infinite theorem or rule out prior publication. No independent audit was performed.
