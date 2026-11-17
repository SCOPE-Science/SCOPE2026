---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The symbolic proof in `RESULT.md` establishes the unrestricted fixed-parameter assertion. Finite verification is supplementary and is not a formal proof or external attestation. Run `python3 verify.py` using Python 3.9 or newer, without nonstandard dependencies. It compares digitwise Lucas divisibility with minimal zero-sum sequences, exhausts small maximal-length zero-sum words, checks digit-cutoff profile sums against direct row enumeration, and performs separate sparse counts for large **multiplier cutoffs**.

The two cutoffs must be distinguished. `exact_profile_count(m,p,L)` computes
\[
C_{m,p}(L)=\#\{q\ge2:mq<p^L,\ p\mid G(mq;m)\},
\]
whereas `multiplier_count_sparse(m,p,L)` uses `bound=m*(p**L)` and computes
\[
D_{m,p}(L)=\#\{2\le q\le p^L:p\mid G(mq;m)\}.
\]
For \((m,p)=(5,2)\) and \(L=8,12,16,20\), the **digit-cutoff** counts are \(15,65,191,453\), while the **correct multiplier-cutoff** counts are \(46,147,367,784\). These sequences are both correct for their distinct predicates. The original RESULT.md incorrectly identified the old truncated sparse-count values as values of \(C_{5,2}(L)\). The original `verify.py` also truncated its sparse search to only `L+2` base-`p` digit positions despite using `m*p**L` as its upper bound. Both the cutoff label and the missing leading positions have been corrected.

Finite diagnostics from the corrected verifier:

```
DIRECT_LUCAS_VS_MINIMAL_ZERO_SUM 11866
MAXIMAL_LENGTH_CYCLIC_WORDS 763424
MULTIPLIER_CUTOFF 3 2 8 44
MULTIPLIER_CUTOFF 3 2 10 75
MULTIPLIER_CUTOFF 3 2 12 118
MULTIPLIER_CUTOFF 3 2 14 175
MULTIPLIER_CUTOFF 3 2 16 248
MULTIPLIER_CUTOFF 4 3 6 47
MULTIPLIER_CUTOFF 4 3 8 104
MULTIPLIER_CUTOFF 4 3 10 200
MULTIPLIER_CUTOFF 4 3 12 349
MULTIPLIER_CUTOFF 5 2 8 46
MULTIPLIER_CUTOFF 5 2 12 147
MULTIPLIER_CUTOFF 5 2 16 367
MULTIPLIER_CUTOFF 5 2 20 784
VERIFY_OK finite_checks_only=True
EXACT_PROFILE_REPLAY 3 2 2 L=2..10
EXACT_PROFILE_REPLAY 4 3 2 L=2..10
EXACT_PROFILE_REPLAY 5 2 4 L=2..10
EXACT_PROFILE_REPLAY 5 3 4 L=2..10
EXACT_PROFILE_REPLAY 7 2 3 L=2..10
ALL_EXACT_PROFILE_TESTS_OK
ORDER_FOUR_BRANCH_POLYNOMIAL_CERTIFICATE_OK
```

The `MULTIPLIER_CUTOFF` lines above use the multiplier cutoff, not the digit cutoff. The exact profile checks and symbolic degree argument establish the claims stated in RESULT.md; numerical diagnostics do not establish originality or scientific value. Lean verification, expert attestation and any external certification remain **not performed**.
