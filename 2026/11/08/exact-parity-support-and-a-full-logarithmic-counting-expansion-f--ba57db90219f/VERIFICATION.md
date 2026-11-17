---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Modulo 2, the generating product f16/f1 equals f1^15, and Jacobi gives the exact triangular-pair parity formula T_i+4T_j. Completing squares yields 8n+5=(2i+1)^2+(4j+2)^2; since 8n+5 is 5 mod 8, every sum-of-two-squares representation has one positive odd coordinate and one 2-mod-4 coordinate and r2(M)/8 equals the nonnegative triangular-pair count. The two-square product formula makes odd count equivalent to exactly one 1-mod-4 prime with exponent 1 mod 4 and all other exponents even, then M=5 mod 8 forces that prime to 5 mod 8. The prime-power a>=1 and p|u exclusions contribute O(sqrt(Y) log Y); splitting the remaining sum over odd u at Y^(1/10), the fixed-AP PNT and a uniformly summable Li expansion prove every fixed logarithmic order and displayed zeta-derivative coefficients. Independent original-partition dynamic programming and separate prime-factor tests matched 2001 indices n=0..2000. The PNT error/finite checks are distinct from proof of the full expansion.

## originality

PASS

Keith–Zanello establish density-zero behavior for even-regular eta quotients and exact prime-exponent support for b8; Cui–Gu give families of progressional parity congruences for b16, not an all-index prime-square equivalence or a full logarithmic support count. A near-identical prime-times-square parity mechanism in a signed two-block odd partition has a different coefficient definition and arithmetic condition and does not imply the b16 theorem.

## value

PASS

An exact all-index parity classification for a natural partition function and a full quantitative support law beyond mere density zero fill a motivated arithmetic gap. The prime-times-square mechanism yields a sharp X/log X sparsity scale and all explicit fixed-order logarithmic coefficients; these are not a routine restatement of a fixed progression congruence or a known b8 theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
