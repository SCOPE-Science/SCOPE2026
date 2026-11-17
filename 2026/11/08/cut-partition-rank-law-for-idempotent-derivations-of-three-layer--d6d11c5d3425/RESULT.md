# Maximum-rank concentration for projection derivations of balanced three-level incidence algebras

## Finding
Let \(q=2^e\), \(e\ge1\), and let \(P_n\) be the ordinal sum of three antichains of size \(n\ge1\). For the incidence algebra \(A_n=I(P_n,\mathbb F_q)\), let \(\mathcal D_n\) be the set of distinct coefficient-linear derivations \(D\) satisfying \(D^2=D\). Then the largest operator rank on \(\mathcal D_n\) is \(2n^2\), and **exactly**
\[
\boxed{3(2^n-1)q^{2n^2}}
\]
operators have that rank. If \(D_n\) is uniformly distributed on \(\mathcal D_n\), then, for every fixed field size \(q\),
\[
\boxed{\Pr\{\operatorname{rank}D_n=2n^2\}=1-O_q(\rho_q^n)}
\]
for some \(\rho_q\in(0,1)\). Thus an exponentially growing family of binary maximal-cut patterns corresponds to almost every concrete idempotent derivation, despite the presence of many lower-rank patterns.

The **general rank-weight enumerator** of idempotent derivations of arbitrary finite-poset incidence algebras was already established in *Projection derivations of finite-poset incidence algebras: Boolean cocycles and exact rank spectra* (November 2, 2026). This result does **not** claim that enumerator, the diagonalization of idempotent derivations, or its specialization to the tripartite poset as new. The present claim is the sharp extremal multiplicity and its nontrivial fixed-field concentration limit for this naturally frustrated family.

## Definitions and reduction to established structural theory
For a coefficient-linear derivation, rank is measured as a linear map on the \((3n+3n^2)\)-dimensional incidence algebra, not as the rank of an implementing matrix or a grading-isomorphism class. All strict comparabilities join different antichain levels. The earlier general cocycle-orbit theorem gives the complete *known* rank-weight expression
\[
\sum_{D\in\mathcal D_n}t^{\operatorname{rank}D}
=\frac12\sum_{a,b,c=0}^n\binom na\binom nb\binom nc(qt)^{R_n(a,b,c)}, \qquad (1)
\]
where
\[
R_n=a(n-b)+(n-a)b+a(n-c)+(n-a)c+b(n-c)+(n-b)c.
\]
Indeed the order complex is contractible, so each Boolean additive cocycle is the difference of binary vertex colors, uniquely up to simultaneous color complementation. Such a cocycle has rank the number of differently colored comparable pairs, and its radical-unit orbit has size \(q^{R_n}\). Formula (1) is cited as a **covered specialization**, used only as an input to the extremal and probabilistic analysis below. The division by two is over integers; it is not a field operation.

## Proof of the new extremal and concentration statements
Put \(s_1=2a-n\), \(s_2=2b-n\), \(s_3=2c-n\). Then
\[
R_n(a,b,c)=\frac{3n^2-s_1s_2-s_1s_3-s_2s_3}{2}.
\]
For \(s_i\in[-n,n]\), the multilinear expression is maximized at \(2n^2\); equality holds **exactly** when two distinct levels are monochromatic with opposite binary colors, while the third is arbitrary. To see the equality characterization, set \(x_i=s_i/n\) and minimize \(x_1x_2+x_1x_3+x_2x_3\) on the cube. For fixed two variables it is affine in the third, and its minimum is \(-1\); equality forces an opposite-sign endpoint pair (including the endpoint intersections). There are \(6\cdot2^n\) ordered choices of opposite pure levels and a free third coloring. Exactly six three-monochromatic colorings are counted twice, giving \(6(2^n-1)\) distinct maximizing vertex colorings. Division by the two-to-one global complementation and multiplication by the established orbit size \(q^{2n^2}\) proves the exact multiplicity.

For the concentration estimate, normalize the total orbit-weight sum from (1) by \(q^{2n^2}\). Maximizers contribute \(6(2^n-1)\) before the harmless global division by two. Fix \(\eta=1/100\). Outside the six regions where one level has at most \(\eta n\) wrong-colored vertices relative to color one and another has at most \(\eta n\) wrong-colored vertices relative to color zero, compactness and the preceding strict equality characterization give a deficit \(2n^2-R_n\ge\delta n^2\) for a fixed \(\delta>0\). All such patterns together contribute at most \(2^{3n}q^{-\delta n^2}\).

Within one of the six regions, let \(a,b\le\eta n\) be the wrong-color counts in the respective nearly pure levels, and let \(k\) be the number of ones in the free level. Then the exact rank deficit is
\[
2n^2-R_n=2[a(n-k)+bk-ab].
\]
Summing over the free level's colors gives normalized weight
\[
q^{2ab}(q^{-2a}+q^{-2b})^n.
\]
For \(a+b>0\), if one of \(a,b\) vanishes this is at most \((1+q^{-2})^n\). If both are positive, it is at most \((2q^{-2(1-\eta)})^n\), by \(a(n-k)+bk-ab\ge (1-\eta)n(a+b)/2\) in the appropriate elementary split, or directly by bounding \(q^{2ab}q^{-2n\min(a,b)}\). The number of choices of the two nearly pure wrong-color subsets is at most \(2^{2H_2(\eta)n}\), where \(H_2(x)=-x\log_2x-(1-x)\log_2(1-x)\). For \(q\ge2\),
\[
2^{2H_2(\eta)}\max\{1+q^{-2},\;2q^{-2(1-\eta)}\}<2.
\]
Thus the total normalized weight of nonmaximizers is \(O_q(\kappa_q^n)\) for some \(\kappa_q<2\), plus a superexponentially small term. Dividing by the maximizing contribution \(6(2^n-1)\) yields the stated \(1-O_q(\rho_q^n)\) probability. This proof is asymptotic with \(q\) held fixed; no uniform-in-\(q\) exponent is claimed. \(\square\)

## Verification and boundaries
The unchanged `verify.py` independently enumerates concrete derivation operators for \(n=1,2\) over \(\mathbb F_2\) and \(n=1\) over \(\mathbb F_4\), and checks the maximum-cut classification through \(n=10\). Finite enumerations corroborate only these sizes; the all-\(n\) statement follows from the exact extremal and entropy arguments above. There is exactly one rank-zero derivation. The finding does not concern other characteristics, unbalanced levels, or all derivations without the projection constraint.

## Prior-result implications and limits
The November 2 general Boolean-cocycle theorem **covers every coefficient of (1)**, including the special three-level operator-rank polynomial, so neither that formula nor its weighted-cut reinterpretation constitutes independent originality. Earlier group-grading classifications by Santulo–Souza–Yasumura (2019) and Dos Santos–Yasumura (2024) and incidence-derivation structure theorems also remain prior. The separately evaluated highest-rank multiplicity and its fixed-\(q\) concentration rate are the sole asserted contributions here. Their significance is the extremal and statistical behavior of a natural, increasingly large family of projection derivations; they are not a new general incidence-algebra classification. A more general extremal spin-partition or grading result may imply them, and priority remains best-of-knowledge rather than certified.

## References
- *Projection derivations of finite-poset incidence algebras: Boolean cocycles and exact rank spectra*, published November 2, 2026, https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-projection-derivations-of-finite-poset-incidence-algebras-boolea--445675d1fc6d/RESULT.md .
- E. A. Santulo Jr., J. P. Souza and F. Y. Yasumura, *Group gradings on finite dimensional incidence algebras*, arXiv:1905.08391.
- H. S. Dos Santos and F. Y. Yasumura, *Group gradings on finite-dimensional incidence algebras. II*, arXiv:2406.19329.
