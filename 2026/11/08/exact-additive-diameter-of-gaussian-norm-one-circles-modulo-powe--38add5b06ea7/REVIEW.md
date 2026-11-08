# Scientific review: dyadic Gaussian norm-one additive diameter

## Correctness — PASS

The proof covers all integers \(k\ge1\). For an odd–odd target \((u,v)\), the integer \(h=(u^2+v^2)/2\) is odd and congruent to \(1\) modulo \(4\). Hence \(2h^{-1}-1\equiv1\pmod8\) has a square root modulo every power of two. The two explicit half-sum vectors are integral, sum to the target, and both have norm \(1\) modulo \(2^k\). This proves \(2C_k\) contains the entire odd–odd class; subtracting a coordinate unit proves \(3C_k=O_k\) and \(4C_k=E_k\). The lower bound uses a genuine modulo-eight obstruction to writing \((2,2)\) as two norm-one sums. The square-root lemma is proved, not inferred from finite tests. All boundary cases \(k=1,2\) are addressed. The standalone checker independently constructs every target certificate through exponent nine and exhausts sumsets through exponent seven. Remaining mathematical risk is limited to possible errors not detected by this review; no unsupported extrapolation from a finite search is used.

## Originality — PASS, with historical-priority risk

The underlying norm-one group is classical. Grau et al., arXiv:1401.4708 (2014), develop its **multiplicative** structure and related pseudoprime tests. Covert–Demiroğlu Karabulut–Pakianathan, arXiv:1808.06665 (2018), study additive unit-circle sums, but Sections 4.1–4.1.1 explicitly assume **finite fields of odd characteristic**. A 2026 preprint on sums of units in finite rings studies **all ring units** and normalized norm-one subgroups in finite fields; the inspected parts do not identify the restricted dyadic additive diameter. Targeted literature searches did not locate an equivalent theorem for \(\mathbb Z/2^k\mathbb Z\). The closest mathematical research summary instead concerns norm-one tori in odd-characteristic finite fields, so does not cover dyadic local rings. The residual risk is that an overlooked local-ring Cayley graph theorem or a classical norm-form identity may imply this exact statement.

## Mathematical value — PASS

The additive Cayley diameter of the canonical Gaussian norm-one subgroup is an intrinsic graph invariant. Its value changes sharply from \(2\) to \(4\) after exponent two; a uniform constructive \(2\)-adic square-root method gives the upper bound, while a local modulo-eight obstruction proves optimality. The result supplies full parity-coset coverage at exact additive lengths three and four, not just connectivity or an arbitrary finite computation. It complements existing odd-characteristic circle-sum theory without claiming to solve its generalizations.

## Limitations and closest literature

This result does not classify the complete double sumset or count individual representations. The 2014 source concerns multiplicative norm-one groups. The 2018 source is a relevant additive analogue in a different coefficient ring, and the 2026 source supplies a general units framework rather than this restricted circle. Exhaustive checks are finite corroboration only. All originality assessments are qualified by the possibility of unlocated prior work.

Self-review: passed. Independent audit: not yet performed.
