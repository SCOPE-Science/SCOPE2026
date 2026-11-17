# Sharp metric-valued Poincaré constants for arbitrary complete multipartite graphs

## Finding
Let \(k\ge2\) and let \(G=K_{n_1,\ldots,n_k}\), with integers \(n_1\ge\cdots\ge n_k\ge1\). Write \(N=\sum_i n_i\), \(E=\sum_{i<j}n_i n_j\), and \(M=\binom N2\). For \(1\le r\le k\) set
\[
A_r=\sum_{i=1}^r n_i(n_i-1),\qquad
B_r=E-\sum_{r<i<j\le k}n_i n_j.
\]
Then the **optimal exponent-one metric-valued Poincaré constant**, uniformly over every metric target \((X,d)\) and every map \(f:V(G)\to X\), is
\[
\boxed{\gamma_1^{\rm met}(G)=\frac E M\left(1+\max_{1\le r\le k}\frac{A_r}{B_r}\right).}
\]
In particular, for every such map,
\[
\frac1M\sum_{\{u,v\}\subset V(G)}d(f(u),f(v))
\le\frac{\gamma_1^{\rm met}(G)}E
\sum_{\{u,v\}\in E(G)}d(f(u),f(v)).
\]
The constant is attained using a finite metric target and therefore also using a finite-dimensional real \(\ell_\infty\) target. Although a priori every subset of the \(k\) vertex parts could determine the optimum, **one of the \(k\) initial segments of parts ordered by size always attains it**.

The prefix phenomenon can genuinely select an intermediate initial segment. For \(K_{4,3,1,1}\), the unique optimal size is \(r=2\) and \(\gamma_1^{\rm met}=33/26\); for \(K_{4,3,2,1,1}\), it is \(r=3\) and \(\gamma_1^{\rm met}=144/121\).

## Assumptions and scope
The graph is finite, simple and unweighted, and has \(k\ge2\) nonempty independent vertex classes. Distances may come from any metric space; the map is not assumed injective, and all sums range over unordered vertex pairs. The target supremum permits finite metric targets (and equivalently their isometric embeddings into real \(\ell_\infty\)). The denominator of the displayed ratio is interpreted through the inequality, so constant maps cause no division-by-zero issue. Since \(E>0\), every \(B_r>0\). The claim concerns exponent one only, not the squared-distance Poincaré constant or a fixed Hilbert target.

## Proof
**1. Averaged triangle bounds.** Write \(V_i\) for the part with \(n_i\) vertices. For \(i\ne j\), define the average cross-part distance
\[
y_{ij}=\frac1{n_i n_j}\sum_{u\in V_i,\,v\in V_j}d(f(u),f(v))=y_{ji}.
\]
Let \(W_i=\sum_{\{u,v\}\subset V_i}d(f(u),f(v))\) be the within-part sum. For any fixed \(w\in V_j\), apply the triangle inequality \(d(f(u),f(v))\le d(f(u),f(w))+d(f(w),f(v))\) to each unordered pair \(\{u,v\}\subset V_i\). Summing and averaging over \(w\in V_j\) gives
\[
W_i\le n_i(n_i-1)y_{ij}.
\]
Consequently \(W_i\le a_i t_i\), where \(a_i=n_i(n_i-1)\) and \(t_i=\min_{j\ne i}y_{ij}\). (When \(n_i=1\), \(W_i=a_i=0\).) The edge-distance sum is
\[
Q=\sum_{i<j}n_i n_j y_{ij},
\]
and the all-pair sum is \(P=Q+\sum_i W_i\).

**2. Layer-cake domination.** For any set \(S\subseteq\{1,\ldots,k\}\) put
\[
A(S)=\sum_{i\in S}a_i,\qquad
B(S)=\sum_{i<j:\ i\in S\ \mathrm{or}\ j\in S}n_i n_j
=E-\sum_{i<j:\ i,j\notin S}n_i n_j.
\]
Let \(\Lambda=\max_{\varnothing\ne S\subseteq\{1,\ldots,k\}}A(S)/B(S)\). For \(s\ge0\), the set \(S_s=\{i:t_i>s\}\) has the property that every cross-part distance \(y_{ij}\) incident to \(S_s\) exceeds \(s\). Therefore
\[
A(S_s)\le\Lambda B(S_s)\le\Lambda\sum_{i<j:y_{ij}>s}n_i n_j.
\]
Integrating in \(s\) from zero to infinity, using \(\int_0^\infty\mathbf1_{t_i>s}\,ds=t_i\) and the analogous identity for \(y_{ij}\), yields
\[
\sum_i a_i t_i\le\Lambda Q,\qquad P\le(1+\Lambda)Q.
\]
No finiteness or linearity condition on the metric target was used.

**3. Equality metric for every subset.** Fix a nonempty set \(S\) of parts. On the original vertices define a symmetric pseudometric by assigning distance zero between any two vertices in parts outside \(S\); distance two between two distinct vertices in the same part belonging to \(S\); and distance one for every other pair of distinct vertices. This is a pseudometric: the only distance-two pairs can be connected via any third vertex only by two distances of at least one (unless that third vertex is the same endpoint). Quotient the zero-distance equivalence classes to obtain an actual finite metric space. For the identity map to this quotient, the cross-part edge sum equals \(B(S)\), while the within-part sum equals \(A(S)\). Hence \(P/Q=1+A(S)/B(S)\), proving sharpness of \(\Lambda\). The finite target embeds isometrically into a finite-dimensional real \(\ell_\infty\) via distance-to-landmark coordinates. Thus the constant is also attained in a real Banach space.

**4. Initial-segment maximization.** Sort \(n_1\ge\cdots\ge n_k\). If a subset \(S\) omits exactly one part, then \(B(S)=E=B(\{1,\ldots,k\})\) and \(A(S)\le A(\{1,\ldots,k\})\); so a maximizing set may be taken with either no omitted parts or at least two omitted parts. A singleton \(S=\{i\}\) has score \((n_i-1)/(N-n_i)\), nondecreasing in \(n_i\), and may be replaced by the largest part.

Suppose a maximizing \(S\) has at least two selected and at least two omitted parts, and there is an inversion: a selected class of size \(a\) and an omitted class of strictly larger size \(b>a\). Let \(t\) be the total size of the omitted classes; then \(x=t-b>0\), and denote the score by \(R=A(S)/B(S)\). Swapping those two classes changes the numerator by \((b-a)(a+b-1)\) and the denominator by \((b-a)x\). If the swap strictly improves the score, maximality fails. Otherwise comparing the two ratios shows
\[
R\ge\frac{a+b-1}{x}>\frac{a-1}{t}.
\]
Removing the selected class of size \(a\) changes numerator by \(-a(a-1)\) and denominator by \(-at\), so its new score is strictly larger precisely when \(R>(a-1)/t\). This contradicts maximality too. Thus every maximizing subset can be arranged without a strict size inversion; equal-sized classes may be exchanged freely. Therefore an initial segment \(\{1,\ldots,r\}\) maximizes \(A/B\), proving the formula.

## Verification
The supplementary standard-library program `CHECK.py` performs 7,136 exact-rational assertions, including exhaustive comparisons of the prefix and all-subset formulas for part-size profiles in \(\{1,2,3,4\}\) with two to five parts, equality-witness calculations, and sampled \(\ell_1\)-metric inequalities. It also checks the two stated intermediate-prefix examples. Command: `python CHECK.py`. The infinite family and arbitrary-target statement follow from the preceding proof, not from finite checks.

## Relationship to prior work
Polavarapu's 2026 cotype estimates concern general regular scalar expanders and selected Banach targets, giving upper bounds in terms of cotype and a spectral gap. The present conclusion is different: an **exact** optimal metric-target constant for every unbalanced complete multipartite graph, independent of target geometry, with a prefix extremizer theorem. Earlier quantitative nonlinear spectral-gap studies establish broader frameworks but do not imply these concrete multipartite subset ratios. Some previously reported exact constants for bipartite and restricted tripartite families are special cases here; the present result is the all-part-size classification and demonstrates new intermediate selected-prefix phases.

## Limitations
The formula concerns complete multipartite graphs and exponent-one distance sums; no claim is made for arbitrary graphs, exponent \(p>1\), or Hilbert-only optimal constants. The cotype-source abstract and first-public/MSC record were checked; its full manuscript was unavailable during this comparison, so bibliographic priority is provisional and does not amount to an independent literature certification. Full mathematical validation by an independent reviewer has not been performed.

## References
- A. R. Polavarapu, *Linear Cotype Bounds for Nonlinear Spectral Gaps of Scalar Expanders*, arXiv:2611.05649v1, first submitted 3 November 2026, https://arxiv.org/abs/2611.05649.
- D. J. Altschuler, P. Dodos, K. Tikhomirov and K. Tyros, *A combinatorial approach to nonlinear spectral gaps*, arXiv:2410.04394, https://arxiv.org/abs/2410.04394.
