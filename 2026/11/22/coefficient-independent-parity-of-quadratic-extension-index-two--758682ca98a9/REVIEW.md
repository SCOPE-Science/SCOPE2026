# Review of coefficient-independent parity of index-two binomials

## Correctness — PASS

The claimed domain is every odd prime power and every admissible \(d,r,a\), not merely tested prime fields. The induced root-of-unity permutation forces odd \(r\) and the norm-like constraint \(B^D=1\). The Frobenius sign dichotomy forces \(B=a^{(q+1)/2}-(-1)^{(q+1)/2}\) into the base field. The even-sized cosets of \(\mathbb F_q^\times\) cancel the block and power-map signs. The root-of-unity factors each occur twice, giving the sole surviving contribution \((-1)^{(r-1)/2}\). All these steps are proved directly in `RESULT.md` and do not depend on a finite census. The separate direct evaluator found 2,132 permutations across five base fields, all with the predicted sign.

## Originality — PASS, with risk

The full 2026 Tang–Fan paper supplies an exhaustive **permutation existence** classification and a coefficient-square lemma, not a permutation parity theorem. Bors–Wang supplies the cyclotomic-coset and wreath-product method, not the specialized coefficient-independent sign. The earlier indexed result on signs of \(X^r(X^{q-1}+a)\) concerns an index-one family and gives coefficient-dependent values; its statement and proof do not subsume the index-two result. The full indexed coprime-index collision result counts functions, not signs, and is structurally inapplicable to \(\gcd(d,q+1)=2\). An implicit specialization of general wreath-product sign formulas remains a meaningful residual risk; literature searching cannot prove absence.

## Mathematical value — PASS

Permutation parity is a natural structural invariant of finite-field bijections, relevant to distinguishing alternating and odd permutation behavior. The theorem proves a uniform and sharp mod-four rule across all coefficients in the recently classified index-two family, including nonprime base fields and all admissible exponent-difference indices. The vanishing of every coefficient contribution arises from the simultaneous square constraint and the paired product over the root-of-unity quotient; it does not follow from mere existence or a relabeled one-index parity count. It contrasts with the neighboring index-one coefficient-dependent sign law. No wider classification of cycle types is claimed.

## Sources and remaining limits

Primary: Tang–Fan, arXiv:2611.14162v1, full HTML sections 1–6 inspected. Structural predecessor: Bors–Wang, arXiv:2103.00664v1, its cyclotomic and wreath-product framework inspected. Published comparisons: *A universal sign bias for classified finite-field permutation binomials* and *Collision rigidity and exact enumeration for coprime-index permutation binomials*, both full `RESULT.md` files inspected. External novelty remains provisional until independent specialist scrutiny, and all computational evidence is finite.

Self-review: passed. Independent audit: not yet performed.
