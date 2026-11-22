# Fractal imaginary-time boundedness for an immediately compact analytic semigroup

## Finding
For each real \(\gamma>0\), let \(H=\bigoplus_{n\ge1}\mathbb C^2\), with its Hilbert direct-sum norm, and put \(q_n=n!\), \(d_n=(n!)^2\). On the algebraic finite-support subspace \(D\), define the entire block family
\[
S_n(z)=e^{-d_n z}\begin{pmatrix}1&n^\gamma(1-e^{-q_n z})\\0&e^{-q_n z}\end{pmatrix},\qquad S(z)=\bigoplus_{n\ge1}S_n(z)\big|_D.
\]
Its restriction \(T(t)=S(t)\), \(t\ge0\), extends to an immediately compact, bounded analytic \(C_0\)-semigroup on \(H\). The exact set of complex times where \(S(z)\) extends to a bounded operator is
\[
\mathcal B_\gamma=\{z:\operatorname{Re}z>0\}\;\cup\;\{2\pi i\alpha:\alpha\in E_\gamma\},\qquad E_\gamma=\left\{\alpha\in\mathbb R:\sup_{n\ge1}n^\gamma\operatorname{dist}(n!\alpha,\mathbb Z)<\infty\right\}.
\]
The set \(E_\gamma\) is a dense, proper, Lebesgue-null additive subgroup of \(\mathbb R\); it is exactly the additive imaginary-translation period group of \(\mathcal B_\gamma\) after division by \(2\pi\). Its cardinality and Hausdorff dimension have the sharp trichotomy
\[
\begin{array}{c|c|c}
\gamma>1&E_\gamma=\mathbb Q&\dim_H E_\gamma=0\\
\gamma=1&E_\gamma\text{ uncountable}&\dim_H E_\gamma=0\\
0<\gamma<1&E_\gamma\text{ uncountable}&\dim_H E_\gamma=1-\gamma.
\end{array}
\]
In every case the maximal locally bounded holomorphy region is exactly the open right half-plane. Hence an immediately compact analytic semigroup with strictly negative real discrete generator spectrum can possess a dense nonclosed group of bounded imaginary times, of any prescribed Hausdorff dimension strictly between zero and one.

## Assumptions and scope
All operators are on the complex Hilbert space \(H\). A complex-time operator at a boundary point means the bounded extension, when one exists, of the specifically defined algebraic family \(S(z):D\to D\); it is not asserted that this boundary point admits a holomorphic neighborhood. Distances are Euclidean distances to the nearest integer. The exponent \(\gamma\) is fixed and positive. The statement gives the entire boundedness set, not the set of contraction times or a claim of norm continuity at time zero.

## Proof
**1. Semigroup, analyticity, compactness.** Direct multiplication shows \(S_n(z+w)=S_n(z)S_n(w)\) and \(S_n(0)=I\). For real \(t\ge0\), use \(1-e^{-q_nt}\le q_nt\) and \(x e^{-x}\le e^{-1}\) to obtain
\[
\big|n^\gamma e^{-d_nt}(1-e^{-q_nt})\big|\le n^\gamma q_nt e^{-d_nt}\le\frac{n^\gamma}{e q_n}.
\]
The last bound is uniformly finite and tends to zero with \(n\). All diagonal entries have modulus at most one. Thus \(\sup_{0\le t\le1}\|S(t)\|<\infty\), and strong continuity at zero follows first on \(D\) and then on \(H\). At each fixed \(t>0\), every block entry tends to zero as \(n\to\infty\), so \(T(t)\) is compact. For every fixed angle \(0<\vartheta<\pi/2\) and \(z\) in the closed sector \(|\arg z|\le\vartheta\), integration of the exponential along the segment from zero to \(q_nz\) gives \(|1-e^{-q_nz}|\le q_n|z|\). Since \(\operatorname{Re}z\ge |z|\cos\vartheta\), the off-diagonal bound becomes
\[
 n^\gamma q_n|z|e^{-d_n\operatorname{Re}z}\le\frac{n^\gamma}{e q_n\cos\vartheta}.
\]
Thus the semigroup is uniformly bounded on each proper closed subsector and is holomorphic in the open right half-plane by locally uniform bounds on the analytic blocks. Its generator is the closure of the direct-sum block operator with matrices \(\begin{pmatrix}-d_n&q_nn^\gamma\\0&-(d_n+q_n)\end{pmatrix}\); its spectrum consists of the strictly negative real eigenvalues \(-d_n\) and \(-(d_n+q_n)\), with no finite accumulation points. For definiteness, \(T(t)=e^{tG}\) for this generator \(G\).

**2. Exact complex boundedness.** For \(\operatorname{Re}z>0\), diagonal entries are bounded by one and the off-diagonal entries by \(2n^\gamma e^{-d_n\operatorname{Re}z}\), whose supremum is finite. If \(\operatorname{Re}z<0\), already the first diagonal entry is unbounded over \(n\). If \(z=2\pi i\alpha\), both diagonals have modulus one, whereas the off-diagonal modulus is \(n^\gamma|1-e^{-2\pi i n!\alpha}|\). The elementary two-sided bounds between \(|1-e^{2\pi ix}|\) and \(\operatorname{dist}(x,\mathbb Z)\) establish exactly the displayed characterization by \(E_\gamma\). Local holomorphy can occur only in the interior of the boundedness set, which equals the open right half-plane because \(E_\gamma\) has empty interior (proved below).

**3. Factorial digits and the dimension bound.** Every \(\alpha\in[0,1)\) admits a factorial expansion \(\alpha=\sum_{j\ge2}a_j/j!\) with digits \(0\le a_j\le j-1\); choose the nonterminating ambiguity consistently. For each \(n\), the fractional part \(\{n!\alpha\}\) lies between \(a_{n+1}/(n+1)\) and \((a_{n+1}+1)/(n+1)\), because the remaining tail is bounded by \(1/(n+1)\). Suppose \(\alpha\in E_\gamma\) and \(\operatorname{dist}(n!\alpha,\mathbb Z)\le Cn^{-\gamma}\) for every \(n\). Then each sufficiently large digit \(a_{n+1}\) is either among the first \(O_C(n^{1-\gamma}+1)\) digits or among the last \(O_C(n^{1-\gamma}+1)\) digits. If \(0<\gamma<1\), the number of admissible factorial cylinders of order \(N\) is at most \(\exp((1-\gamma)N\log N+O_C(N))\). Each has length \(1/N!\), giving \(\dim_HE_\gamma\le1-\gamma\) after taking a countable union over integer \(C\). For \(\gamma\ge1\), at most \(O_C(1)\) digits are admissible at each level, giving dimension zero.

For \(0<\gamma<1\), restrict instead to digits \(0\le a_j\le\lfloor j^{1-\gamma}/4\rfloor\) for all sufficiently large \(j\). The tail bound then shows \(\operatorname{dist}(n!\alpha,\mathbb Z)=O(n^{-\gamma})\), so this Cantor set lies in \(E_\gamma\). Giving each allowed digit equal conditional probability, an order-\(N\) factorial cylinder has mass \(\exp(-(1-\gamma)N\log N+O(N))\). Any interval whose length lies between \(1/(N+1)!\) and \(1/N!\) meets at most two order-\(N\) factorial cylinders, hence has mass at most twice this amount. The mass-distribution bound implies dimension at least any \(s<1-\gamma\), and therefore exactly \(1-\gamma\). When \(\gamma=1\), allowing only digits \(a_j\in\{0,1\}\) for all sufficiently large \(j\) similarly gives an uncountable subset of \(E_1\), although the preceding upper bound forces dimension zero.

For \(\gamma>1\), write \(x_n=n!\alpha-k_n\), where \(k_n\in\mathbb Z\) and \(|x_n|\le Cn^{-\gamma}\). The integer \((n+1)k_n-k_{n+1}\) has absolute value at most \((n+1)|x_n|+|x_{n+1}|\to0\), hence eventually vanishes. Therefore \(x_{n+1}=(n+1)x_n\) for every sufficiently large \(n\). Because \(x_n\to0\), this forces \(x_n=0\) eventually, and \(\alpha\in\mathbb Q\). Every rational belongs to \(E_\gamma\) since \(n!\alpha\in\mathbb Z\) eventually.

**4. Subgroup and measure.** The triangle inequality for distances to integers makes \(E_\gamma\) an additive subgroup; it contains \(\mathbb Q\) and is dense. For any fixed \(C\), the Lebesgue measure in \([0,1)\) of \(\{\alpha:\operatorname{dist}(n!\alpha,\mathbb Z)\le Cn^{-\gamma}\}\) is at most \(2Cn^{-\gamma}\), which tends to zero. Taking the intersection in \(n\) and the union in integer \(C\) proves that \(E_\gamma\) is null and proper. Since the boundedness set contains the entire open right half-plane and meets the imaginary axis precisely in \(2\pi iE_\gamma\), its imaginary-translation symmetry group is exactly \(2\pi E_\gamma\).

## Verification
The proof is infinite-dimensional and self-contained. Finite checks supplied in `CHECKER.py` verify exact block-semigroup multiplication, the factorial digit recurrence, and sample bounded/unbounded frequencies; these are diagnostics and are not substituted for the dimension or infinite-time arguments. The operator norm on a direct sum is the supremum of block norms, so all boundedness tests are exact reductions rather than numerical extrapolations.

## Relationship to prior work
Perelmuter, *Semigroups with periodic complex-time boundedness and holomorphy regions* (arXiv:2611.15455v1, first posted 11 November 2026), studies isometric covariance and periodic boundedness and gives the classical Ornstein–Uhlenbeck and hypoelliptic examples. The present construction instead has an explicitly determined dense, nonclosed imaginary boundary period group, varying from countable to uncountable and with a tunable fractal dimension, while retaining immediate compactness and bounded analyticity. Arithmetic facts concerning factorial-digit Cantor sets are standard related tools: the mathematical novelty claimed is the operator-semigroup realization and exact complex-time boundedness classification, **not** the factorial-digit dimension lemma in isolation. The 2016 study by Airey and Mance develops general dimensions of Cantor-series digit sets; the direct elementary dimension proof here serves to make the operator theorem self-contained.

## Limitations
No general classification of boundary period groups of analytic semigroups is claimed. The construction uses a deliberately structured orthogonal sum of nonnormal two-dimensional blocks with superlacunary spectral scales; it does not assert similar behavior for normal or positive semigroups. The underlying standalone factorial-digit dimension calculation is not presented as new number theory. An older unindexed operator-semigroup realization of the same boundary group is a residual priority risk. Independent review has not been performed.

## References
- M. A. Perelmuter, *Semigroups with periodic complex-time boundedness and holomorphy regions*, arXiv:2611.15455v1 (2026), https://arxiv.org/abs/2611.15455.
- D. Airey and B. Mance, *The Hausdorff dimension of sets of numbers defined by their Q-Cantor series expansions*, Journal of Fractal Geometry 3 (2016), 163–186, https://doi.org/10.4171/jfg/33.
- K.-J. Engel and R. Nagel, *One-Parameter Semigroups for Linear Evolution Equations*, Springer (2000), general background on bounded analytic semigroups.
