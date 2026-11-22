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
The proof rests on (i) the pointwise period Möbius identity; (ii) finite abelian character orthogonality; (iii) divisibility of every active divisor by the squarefree kernel; (iv) domination of the largest distinct power of the alphabet size; and (v) an explicit opposite-character witness for the minimal multiplier. These are verified algebraic steps for all parameter ranges.

The included `verify.py` was executed using standard Python 3. Its complete output was:

```text
PASS binary_frequency_tests=8188 ternary=1089 cyclic4=336 klein=336
```

Binary checks use direct words and a fast integer Walsh transform; ternary and cyclic-four checks use explicit cyclotomic coefficient counts; Klein-four checks use bit-pair character signs. Their exhaustively compared lengths are \(2\) through \(12\) for binary, \(2\) through \(6\) for ternary, and \(2\) through \(4\) for both order-four groups. Each coefficient matches the independently computed period-divisor expression. The ranks and sharp extrema also match. Tests of finitely many cases are not presented as a proof for all \(n\) or all \(A\).

The source publication and indexing comparisons are bounded. No independent mathematical audit or expert verification has occurred.
