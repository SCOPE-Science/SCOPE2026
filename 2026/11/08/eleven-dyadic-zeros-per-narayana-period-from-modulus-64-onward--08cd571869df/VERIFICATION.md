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

## Arithmetic checks

Execute `python3 checker.py`. The script uses no third-party dependencies. It verifies exact integer matrix powers, base-period order obstructions, binomial coefficients for the singular branch, and complete zero censuses for every modulus \(2^k\) with \(1\le k\le12\). In particular, it obtains eleven zeros in each of the seven periods tested from \(k=6\) through \(k=12\), with the required \(2+8+1\) split.

## Infinite proof check

The checker's finite range cannot prove the all-\(k\) result. The matrix lifting argument is valid for every exponent because \(C_k\equiv C\pmod2\) remains nonzero. The singular branch is handled by the convergent integer-coefficient Lipschitz power series \(g\), whose odd linear part makes it a bijective isometry of \(\mathbb Z_2\). The root-count argument is independent of the numerical cutoff used by the checker.

## Scope and limitations

The derived counts are per least full period and include the index-zero term. Index shifts preserve these counts. Independent external verification has not been performed.
