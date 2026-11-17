# Spectral universality of trivial adjoint-product domains for essentially selfadjoint restrictions

## Finding

**Spectral-prescription theorem.** Let \(\mathcal H\) be a separable infinite-dimensional complex Hilbert space and let \(H\) be a nonnegative selfadjoint operator on \(\mathcal H\), with no injectivity, spectral-gap, or compact-resolvent assumption. The following are equivalent.

1. \(H\) is unbounded.
2. There exists a densely defined, nonnegative, essentially selfadjoint operator \(T\) with \(\operatorname{dom}(T^*T)=\{0\}\) and \(\overline T^{\,*}\overline T=H\).
3. The operator \(A=H^{1/2}\) has a linear graph core \(\mathcal D\) satisfying \(\mathcal D\cap\operatorname{dom}H=\{0\}\).

In (2), \(T\) may always be chosen as the restriction \(A|_{\mathcal D}\), so that \(\overline T=A=T^*\). In particular, every unbounded nonnegative selfadjoint spectrum (including its multiplicities and continuous or point spectral type) can be retained *exactly* by the closed product even though the original product is nowhere defined except at zero.

## Assumptions and scope

All adjoints and closures refer to the original Hilbert-space norm, and products use their natural operator domains:
\[\operatorname{dom}(T^*T)=\{x\in\operatorname{dom}T:Tx\in\operatorname{dom}T^*\}.\]
A **graph core** for a closed operator \(A\) means a linear subspace dense in \(\operatorname{dom}A\) for \(\|x\|_A^2=\|x\|^2+\|Ax\|^2\). A nonnegative essentially selfadjoint \(T\) is a densely defined symmetric operator with \(\langle Tx,x\rangle\geq0\) and selfadjoint closure. No claim is made of an explicit computable graph-core basis; the existence theorem for disjoint unbounded-operator domains is used as a classical input.

## Proof

**Classical domain-separation input.** For an unbounded selfadjoint operator \(A\) on a separable infinite-dimensional complex Hilbert space, von Neumann's disjoint-domain theorem provides a Hilbert-space unitary \(U\) such that
\[U\operatorname{dom}A\cap\operatorname{dom}A=\{0\}.\]
This statement is explicitly recalled in Arlinskiĭ–Zagrebnov, *Around the Van Daele–Schmüdgen Theorem*, introductory discussion of von Neumann's theorem (see references). This classical input is **not** claimed as new.

**1. Transfer the separation to the graph Hilbert space.** Assume \(H\geq0\) is unbounded and set \(A=H^{1/2}\). Then \(A\) is also unbounded and selfadjoint. Let
\[\mathcal E=(\operatorname{dom}A,\langle x,y\rangle+\langle Ax,Ay\rangle),\qquad W=(I+H)^{1/2}.\]
The map \(W:\mathcal E\to\mathcal H\) is unitary, by the spectral theorem: \(W\) is an isometry for the graph norm and has bounded inverse \((I+H)^{-1/2}\) on all of \(\mathcal H\).

The crucial exact identity is
\[W(\operatorname{dom}H)=\operatorname{dom}A.\tag{1}\]
Indeed, if \(x=W^{-1}y\), spectral calculus gives
\[x\in\operatorname{dom}H\iff\int_{[0,\infty)}\frac{\lambda^2}{1+\lambda}\,d\mu_y(\lambda)<\infty,\]
where \(\mu_y\) is the spectral measure of \(H\) at \(y\). Since \(\lambda^2/(1+\lambda)\) is bounded on \([0,1]\) and is comparable to \(\lambda\) on \([1,\infty)\), the right-hand side is equivalent to \(y\in\operatorname{dom}H^{1/2}=\operatorname{dom}A\). This proves (1), including the spectral point zero.

Choose the separating unitary \(U\) from the classical input for \(A\), and define
\[\mathcal D=W^{-1}\bigl(U\operatorname{dom}A\bigr).\tag{2}\]
Because \(\operatorname{dom}A\) is dense in \(\mathcal H\), its unitary image is dense in \(\mathcal H\). Equation (2) therefore makes \(\mathcal D\) dense in \(\mathcal E\); thus \(\mathcal D\) is a graph core for \(A\). Equations (1)–(2) also give
\[\mathcal D\cap\operatorname{dom}H=W^{-1}\bigl(U\operatorname{dom}A\cap\operatorname{dom}A\bigr)=\{0\}.\tag{3}\]

**2. Calculate the two products with their domains.** Let \(T=A|_{\mathcal D}\). The graph-core property implies \(\overline T=A\), so \(T\) is densely defined, nonnegative, symmetric and essentially selfadjoint. Adjoints do not change on passage to a closure, hence \(T^*=A\). Accordingly,
\[\operatorname{dom}(T^*T)=\{x\in\mathcal D:Ax\in\operatorname{dom}A\}=\mathcal D\cap\operatorname{dom}A^2=\mathcal D\cap\operatorname{dom}H=\{0\}.\]
On the other hand, \(\overline T^{\,*}\overline T=A^*A=A^2=H\) with its *full* selfadjoint domain \(\operatorname{dom}H\). This proves (1) implies (2) and (3). The graph-core construction also proves (3) implies (2).

**3. Exclude bounded \(H\).** Suppose \(\overline T^{\,*}\overline T=H\) for a densely defined closable \(T\). When \(H\) is bounded, polar-decomposition theory gives \(\operatorname{dom}\overline T=\operatorname{dom}H^{1/2}=\mathcal H\), so \(\overline T\) is bounded. Thus \(T^*=\overline T^*\) is bounded and everywhere defined. Consequently \(\operatorname{dom}(T^*T)=\operatorname{dom}T\), a nonzero dense set. In particular, no \(T\) in (2) exists. Likewise, when \(H\) is bounded, \(\operatorname{dom}A=\operatorname{dom}H=\mathcal H\), so (3) is impossible for any nonzero graph core. This completes all implications.

## Verification

The four independent logical checkpoints are: (i) the standard disjoint-domain unitary for unbounded \(A\); (ii) the exact graph-space spectral identity (1), using \(\lambda^2/(1+\lambda)\asymp\lambda\) for \(\lambda\geq1\); (iii) the product-domain identity (3), without replacing \(T\) by its closure prematurely; and (iv) the bounded-case exclusion by the domain of \(\overline T\). No finite-dimensional computations, empirical approximations or externally certified steps are used. The proof relies on the explicitly attributed classical domain-separation theorem.

## Relationship to prior work

Hassi and de Snoo (2026), Theorem 5.4, construct a densely defined closable \(T\) with \(\operatorname{dom}(T^*T)=\{0\}\) and nontrivial \(T^*T^{**}\); their Proposition 6.4 also treats an essentially selfadjoint block operator whose unclosed product lacks dense domain. The present theorem is a different quantified statement: *for every specified* unbounded nonnegative selfadjoint \(H\), including its complete preassigned spectral data, the closed product is **exactly \(H\)**, and one obtains a graph-core restriction of \(H^{1/2}\) whose unclosed product domain is zero. Their stated results do not provide that universal spectral prescription.

Arlinskiĭ and Zagrebnov (2015) review the classical von Neumann disjoint-domain result and construct, for every unbounded selfadjoint operator, *closed proper restrictions* with trivial domains of differently formed products; Theorem 3.22 also constructs complementary **closed** subspaces of a form domain having zero intersection with the original operator domain. A proper closed subspace of the graph Hilbert space is not a graph core. The graph-*dense* and operator-*domain*-disjoint property in (3), and the exact prescription of \(\overline T^{\,*}\overline T\), are the distinctions asserted here. The classical separating-unitary theorem is essential and credited. Arlinskiĭ and Tretter (2019) treat intersections of domains with adjoints for closed operators, a related but different question.

## Limitations

The proof is existential and uses a classical nonconstructive unitary-separation theorem; it supplies no canonical or numerically stable core. The result is about *nonclosed* graph-core restrictions: it does not assert trivial \(T^*T\) for a closed operator, which would contradict the selfadjointness theorem. Its novelty relative to historical operator-domain literature is qualified: an equivalent graph-core formulation under different terminology remains possible. In particular, the theorem should not be confused with claims about \(\operatorname{dom}T^2\), \(\operatorname{dom}T\cap\operatorname{dom}T^*\), or domains of products formed using the adjoint of a **proper closed restriction**. Independent audit has not been performed.

## References

1. S. Hassi and H. de Snoo, *Non-standard behaviour of semibounded forms and their representations*, arXiv:2611.08225v1, first public November 5, 2026, especially Theorem 5.4 and Proposition 6.4. https://arxiv.org/abs/2611.08225
2. Yu. M. Arlinskiĭ and V. A. Zagrebnov, *Around the Van Daele–Schmüdgen Theorem*, arXiv:1312.6502 (2013), published in *Integral Equations and Operator Theory* 81 (2015), 53–95, especially introduction and Theorem 3.22. https://arxiv.org/abs/1312.6502
3. Yu. M. Arlinskiĭ and C. Tretter, *Everything is possible for the domain intersection dom T and dom T-star*, arXiv:1911.05042 (2019). https://arxiv.org/abs/1911.05042
4. J. von Neumann, *Zur Theorie der unbeschränkten Matrizen*, *Journal für die reine und angewandte Mathematik* 161 (1929), 208–236. The disjoint-domain unitary is used here via Reference 2.
