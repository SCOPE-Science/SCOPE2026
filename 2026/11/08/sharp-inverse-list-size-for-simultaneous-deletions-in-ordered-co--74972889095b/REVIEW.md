# Independent mathematical audit

## correctness

PASS

For each received row w of length n−1, distinct one-insertion supersequences I_q(w) partition disjointly by whether the initial received symbol is retained, proving |I_q(w)|=1+n(q−1). The product I_q(u)×I_q(v) is restricted by coordinatewise x_j≤y_j. Induction on n partitions by the two first symbols a,b. For a≤b, the count is ≤M_(n−1)+(q−1+b−a)T+q(q−1)/2−(b−a), with T=1+(n−1)(q−1), maximized at b−a=q−1, yielding M_n. For a>b, count ≤qT+q(q−1)/2<M_n for n≥2. At u=0^(n−1), v=(q−1)^(n−1), there are (1+n(q−1))² possible row supersequence pairs, with exactly nq(q−1)/2 incompatible same-position exceptional pairs. Equality in the bound forces every leading pair (a,b)=(0,q−1), proving unique receiver for n>=2; n=1 returns q(q+1)/2. Independent direct exhaustive enumeration on seven (q,n) parameter pairs corroborated all base/equality cases.

## originality

PASS

Best-of-knowledge: a nontrivial sharp unencoded two-row simultaneous-deletion inverse-list law with unique receiver, not implied by related code-size, sphere-packing and one-affected-row results in two complete primary articles.

## value

PASS

Exact largest candidate-source count and unique worst-case received pair directly quantify decoding ambiguity in a naturally ordered composite DNA channel; useful distinct invariant from optimized codebook capacity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
