# A graph-indexed overlap law for independent random recursive trees

## Finding

Take \(q\ge2\) independently and uniformly sampled **recursive trees** \(T_1,\ldots,T_q\) on the same birth-labelled vertex set \([n]\). Each vertex \(k+1\), for \(1\le k<n\), chooses one parent uniformly from \([k]\), independently over birth times and tree copies. For a simple graph \(F\) on the copy indices \([q]\), let \(X_{ab}\) be the number of parent edges common to trees \(T_a,T_b\) for each \(\{a,b\}\in E(F)\). Set \(r(A)=q-c([q],A)\) for \(A\subseteq E(F)\), where \(c\) counts connected components, including isolated index vertices.

**Complete joint law.** For all \(n\ge2\), \(q\ge2\), and all such \(F\), the probability generating function is
\[
\boxed{\mathbb E\prod_{e\in E(F)}z_e^{X_e}
=\prod_{k=1}^{n-1}Q_{F,k}(\mathbf z),\qquad
Q_{F,k}(\mathbf z)=\sum_{A\subseteq E(F)}k^{-r(A)}\prod_{e\in A}(z_e-1).}
\]
This is an exact expression for the **entire** multivariate distribution, not just its first moments.

**Forest independence is exact.** The family \((X_e:e\in E(F))\) is mutually independent if and only if \(F\) is a forest, provided \(n\ge3\). In a forest, every overlap is distributed as the number of cycles of a uniform permutation of \([n-1]\):
\[
\mathbb E z^{X_e}=\prod_{k=1}^{n-1}\left(1+\frac{z-1}{k}\right)
=\frac{\Gamma(n-1+z)}{\Gamma(z)\Gamma(n)}.
\]
For \(n=2\), all trees consist of the same single edge, so all overlaps are deterministic and the only-if direction is intentionally excluded.

**Cyclic dependence survives the large-size limit.** Whenever \(e_1,\ldots,e_\ell\) form a simple cycle in the index graph, with \(\ell\ge3\), their mixed cumulant is
\[
\boxed{\operatorname{cum}(X_{e_1},\ldots,X_{e_\ell})
=\sum_{k=1}^{n-1}\left(\frac1{k^{\ell-1}}-\frac1{k^\ell}\right).}
\]
For \(n\ge3\) this is strictly positive and converges, as \(n\to\infty\), to \(\zeta(\ell-1)-\zeta(\ell)>0\). In particular, three pairwise-independent overlap counts can have a strictly positive third cumulant tending to \(\zeta(2)-\zeta(3)\).

**Gaussian yet nontrivially dependent.** For any fixed \(F\), as \(n\to\infty\),
\[
\left(\frac{X_e-H_{n-1}}{\sqrt{\log n}}\right)_{e\in E(F)}
\Longrightarrow (Z_e)_{e\in E(F)},\qquad Z_e\text{ mutually independent }N(0,1),
\]
although the unnormalized cyclic cumulants have nonzero limits. More precisely, near \(\mathbf z=\mathbf1\),
\[
\frac{\mathbb E\prod_e z_e^{X_e}}{\prod_e\mathbb E z_e^{X_e}}
\longrightarrow \Psi_F(\mathbf z)
=\prod_{k=1}^{\infty}\frac{Q_{F,k}(\mathbf z)}{\prod_{e\in E(F)}(1+(z_e-1)/k)},
\]
locally uniformly as a nonvanishing analytic function; \(\Psi_F\equiv1\) exactly when \(F\) is a forest.

## Assumptions and scope

A recursive tree is rooted at vertex \(1\), and for every \(k\in\{1,\ldots,n-1\}\), vertex \(k+1\) independently attaches to one of the \(k\) older vertices, all choices having probability \(1/k\). This defines the uniform distribution on the \((n-1)!\) recursive trees. Different tree copies use independent choices. Common parent edges are compared by the fixed birth labels, not up to graph isomorphism. The copy-index graph \(F\) is simple: no loops or repeated edges. All exact formulas hold for arbitrary finite \(q\), \(F\), and \(n\) in the stated ranges. The Gaussian assertion holds for a fixed graph \(F\) as \(n\to\infty\); it is not a growing-number-of-copies theorem.

## Proof

**1. The one-arrival rank identity.** Write \(P_{a,k}\in[k]\) for the parent chosen in tree \(a\) by newborn vertex \(k+1\). The \(q\) labels \(P_{1,k},\ldots,P_{q,k}\) are independent uniform values on \([k]\). For an index edge \(e=\{a,b\}\), let \(I_{e,k}=\mathbf1\{P_{a,k}=P_{b,k}\}\). For any subset \(A\subseteq E(F)\), requiring \(I_{e,k}=1\) for all \(e\in A\) forces equality within each component of \(([q],A)\). Each component has one freely chosen parent value, so exactly \(k^{c([q],A)}\) of the \(k^q\) parent vectors satisfy the constraints. Therefore
\[
\mathbb E\prod_{e\in A}I_{e,k}=k^{-r(A)}.
\]
Expanding \(z_e^{I_{e,k}}=1+(z_e-1)I_{e,k}\) and summing over subsets gives \(Q_{F,k}\). For different birth times \(k\), all parent vectors are independent, and \(X_e=\sum_{k=1}^{n-1}I_{e,k}\). Multiplying the one-arrival PGFs proves the complete joint formula.

**2. Forest factorization and its converse.** If \(F\) is a forest, every subset \(A\) is acyclic and \(r(A)=|A|\). Thus \(Q_{F,k}(\mathbf z)=\prod_{e\in E(F)}(1+(z_e-1)/k)\), and the entire multivariate PGF is a product of marginal PGFs. These PGFs are those of sums of independent \(\operatorname{Bernoulli}(1/k)\), \(1\le k<n\), which are exactly the permutation-cycle-count distribution on \(n-1\) elements by the standard Feller/Chinese-restaurant insertion construction. Conversely, any cyclic \(F\) contains a simple index cycle, whose mixed cumulant is strictly positive when \(n\ge3\), as proved next, precluding mutual independence.

**3. All exact simple-cycle mixed cumulants.** Let \(C\) be a simple index cycle with \(\ell\) distinct edges. The PGF restricted to those edges depends only on the corresponding graph \(C\), irrespective of the other index edges. All proper subsets of \(E(C)\) are forests, so \(r(A)=|A|\) for proper subsets, whereas \(r(E(C))=\ell-1\). Therefore
\[
Q_{C,k}(\mathbf z)=\prod_{e\in E(C)}(1+(z_e-1)/k)
+\left(k^{-(\ell-1)}-k^{-\ell}\right)\prod_{e\in E(C)}(z_e-1).
\]
For distinct coordinates, the mixed derivative of the logarithm of a PGF at \(\mathbf z=\mathbf1\) equals their joint cumulant, since the derivative operator \(z_e\partial_{z_e}\) equals \(\partial_{z_e}\) at \(z_e=1\) when applied only once in each distinct coordinate. Every proper mixed derivative equals that of the independent product, and the full \(\ell\)-fold derivative of the extra term equals \(k^{-(\ell-1)}-k^{-\ell}\). Summing these derivatives of \(\log Q_{C,k}\) over independent arrival times gives the claimed exact cumulant. The \(k=1\) term is zero; all terms with \(k\ge2\) are strictly positive. Since \(\ell\ge3\), both sums converge as \(n\to\infty\), yielding the zeta difference.

**4. Gaussian limit.** Each overlap has mean \(H_{n-1}=\sum_{k<n}1/k\) and variance \(v_n=\sum_{k<n}(1/k-1/k^2)=\log n+O(1)\). The indicators corresponding to any two *distinct* index edges are independent at each arrival, because two index edges form a forest, hence their covariance vanishes exactly. Thus for any fixed real coefficient vector \(\mathbf a\), the centered linear combination \(\sum_e a_e(X_e-H_{n-1})\) is a sum over arrival times of independent, uniformly bounded random variables with variance \(v_n\sum_e a_e^2\). Lindeberg's condition holds automatically after normalization by \(\sqrt{\log n}\). The one-dimensional central limit theorem and Cramér–Wold yield the asserted independent multivariate Gaussian limit.

**5. Analytic residual dependence.** Put \(u_e=z_e-1\). For fixed \(F\), the empty subset gives \(1\), the singleton subsets give \(\sum_e u_e/k\), and every subset of size at least two has graphic rank at least two. Hence, uniformly on a sufficiently small complex polydisc centered at \(\mathbf z=\mathbf1\),
\[
Q_{F,k}(\mathbf z)=1+\frac{\sum_e u_e}{k}+O_F(k^{-2}),\qquad
\prod_e(1+u_e/k)=1+\frac{\sum_e u_e}{k}+O_F(k^{-2}).
\]
Every denominator factor and numerator is nonzero throughout a suitably small fixed polydisc: for large \(k\) this follows uniformly from closeness to \(1\), and for finitely many smaller \(k\) it follows by continuity and their value \(1\) at the center. Thus the ratio is \(1+O_F(k^{-2})\) locally uniformly, and its infinite product converges locally uniformly to a nonvanishing analytic function. If \(F\) is a forest, every factor equals one. If \(F\) contains a simple index cycle, the corresponding mixed derivative of \(\log\Psi_F\) at \(\mathbf1\) is \(\zeta(\ell-1)-\zeta(\ell)>0\), so \(\Psi_F\) cannot be identically one.

## Verification

The standalone Python standard-library file `verify.py` gives a direct finite cross-check. Its independent direct-enumeration path loops over complete tuples of uniformly generated parent sequences and computes overlapping labeled edges from those sequences, while its PGF path convolves per-arrival equality-vector distributions. It checks the entire joint law for the triangle and four-cycle copy-index graphs at feasible small sizes; all 3- and 4-cycle cumulants; the graphic-rank equality-event formula; forest joint independence; and the Stirling-number marginal probabilities through eight birth-labelled vertices. Executing `python3 verify.py` reports `VERIFY_OK 355 exact-rational assertions`. These finite checks are **not** used as proofs of the general or asymptotic claims; those follow analytically above.

## Relationship to prior work

Borovkov and Vatutin (2006) study weighted random recursive trees, giving the standard uniform-attachment model as a special case, but their analyzed functionals concern root distances and outgoing degrees rather than independently replicated parent-edge overlaps. Grübel and Michailow (first posted 2014) explicitly encode uniform recursive trees by independent birth-parent choices and study boundary theory, path length, and the Wiener index. That encoding supplies the established probabilistic starting point but not the graph-indexed joint overlap PGF.

For comparison, *Exact cycle cumulants and joint Poisson overlap laws for independent Cayley trees* (2026) analyzes trees sampled uniformly from all Cayley spanning trees, not birth-increasing recursive trees. It proves index-forest **product moments**, and cyclic cumulants that vanish at large size, with Poisson(2) scalar overlap limits. Our uniform recursive-tree model instead yields **full forest independence**, Stirling/logarithmic overlap growth, and nonvanishing zeta cyclic cumulants, so neither result implies the other by relabeling or parameter substitution. *Forest independence and the first triangular dependence in multiple-successor logic* (2026) studies independent random linear orders and shared directed successor pairs, where the triangular cumulant decays to zero, not the growing-recursive-tree model. The elementary principle that equality constraints of independent categorical variables are governed by graphic rank is pre-existing and is not presented as new; the combined all-size multi-tree law and its persistent zeta correction are the subject of this result.

## Limitations

The model requires independent **uniform** birth-parent choices and fixed birth labels. Nonuniform or correlated attachment processes need not satisfy forest factorization. The copy-index graph is simple. The exact cyclic cumulant concerns the \(\ell\) distinct overlap variables of a simple index cycle; it is not a formula for arbitrary repeated-index cumulants. The Gaussian limit fixes the number of copies and does not supply an explicit multivariate total-variation rate. Full historical priority is not certified: related older probability and network-overlap literature may contain equivalent formulations. Independent mathematical validation has not been conducted.

## References

1. K. Borovkov and V. Vatutin, *On the asymptotic behaviour of random recursive trees in random environment*, arXiv:math/0608211, first posted 2006-08-09. https://arxiv.org/abs/math/0608211
2. R. Grübel and I. Michailow, *Random recursive trees: A boundary theory approach*, arXiv:1406.7614, first posted 2014-06-30. https://arxiv.org/abs/1406.7614
3. *Exact cycle cumulants and joint Poisson overlap laws for independent Cayley trees*, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-cycle-cumulants-and-joint-poisson-overlap-laws-for-indepen--705bc2214115
4. *Forest independence and the first triangular dependence in multiple-successor logic*, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-forest-independence-and-the-first-triangular-dependence-in-multi--79dcaad9c554
