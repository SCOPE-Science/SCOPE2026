# Review status

Independent audit completed on 2026-10-01 (UTC).

Disposition: **FAILED**.

## Correctness — PASS

The binomial law determines raw moments through order N by factorial moments. Equal weights and known anchors therefore determine the first M power sums of the M unknown support points. Newton identities recover the support polynomial from the first M power sums. Below M, perturbing only the constant coefficient of a simple-root polynomial preserves the first M minus one power sums while changing the support, giving sharp nonidentifiability.

## Originality — FAIL

After reduction to moments, the claim is a direct classical consequence of Newton–Girard identities: M equal-weight atoms are determined by their first M power sums, while the first M minus one power sums leave the constant coefficient free. The binomial observation model merely supplies those moments. This implication is standard finite-moment/symmetric-polynomial theory even though the exact mixture-model wording was not located.

## Scientific value — FAIL

The result is correct and may be pedagogically useful, but under the required value bar it is a routine textbook deduction once equal weights are imposed: no nonstandard structural lemma, difficult boundary, or independently motivated new invariant remains after the moment reduction.
