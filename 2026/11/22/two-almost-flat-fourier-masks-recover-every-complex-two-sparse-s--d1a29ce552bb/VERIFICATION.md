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

# Verification and reproducibility

For any even \(N\ge2\), exact Fourier intensity inversion gives \(C_\ell(h)=\sum_{a-b=h}w^{(\ell)}_a\overline{w^{(\ell)}_b}x_a\overline{x_b}\), where subscripts on differences are modulo \(N\). The proof uses these identities, unique signed differences of powers of two, disjoint intervals of antipodal squared transmissions and nonzero imaginary cross-mask factors. All four are proved for every even \(N\), independently of finite tests.

The self-contained script `CHECK.py` uses NumPy and tests the exact reconstruction algorithm numerically on 2,952 simulated signals across lengths 2 through 17, at every support of size 0, 1 or 2, with three amplitude/phase choices per support. It confirms all combinatorial support signatures and target reconstructions up to phase at tolerance \(10^{-7}\). Invocation: `python3 CHECK.py` after installing `requirements.txt`. Observed output: `PASS 2952 signal_reconstructions, n=2..17; all ordered binary differences distinct`.

These numerical runs are not proofs of universally quantified recovery. They do not establish stability in noise, or recovery beyond two nonzero coordinates. No external independent validation has been performed.
