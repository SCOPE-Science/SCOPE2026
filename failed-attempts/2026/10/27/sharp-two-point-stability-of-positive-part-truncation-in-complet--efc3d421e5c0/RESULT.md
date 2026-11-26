# Sharp two-point stability of positive-part truncation in complete-graph Sobolev norms

## Finding
For every integer \(n\ge2\) and coupling \(\gamma>0\), equip \(\mathbb R^n\) with the graph-Sobolev norm
\[
\|x\|_{\gamma}^{2}=\sum_{i=1}^n x_i^2+\gamma\sum_{1\le i<j\le n}(x_i-x_j)^2.
\]
Let \(R(x)_i=\max\{x_i,0\}\). Its **global two-point Lipschitz constant** is exactly
\[
\boxed{\operatorname{Lip}_{\gamma}(R)=\left(1+\frac{\gamma^2\lfloor n^2/4\rfloor}{1+n\gamma}\right)^{1/2}.}
\]
The constant is achieved by a pair of points entirely inside a single open sign orthant; a sign orthant is locally norming precisely when its positive and negative coordinate counts differ by at most one. Yet for every \(x\), one has the one-point contraction \(\|R(x)\|_\gamma\le\|x\|_\gamma\). Thus energy contraction at the origin coexists with strictly expansive two-point perturbation amplification.

At fixed \(\gamma>0\), \(\operatorname{Lip}_\gamma(R)\sim\tfrac12\sqrt{\gamma n}\) as \(n\to\infty\). If \(\gamma=\lambda/n\) with fixed \(\lambda>0\), then
\[
\operatorname{Lip}_{\lambda/n}(R)\longrightarrow\left(1+\frac{\lambda^2}{4(1+\lambda)}\right)^{1/2}.
\]

## Assumptions and scope
All inputs are real vectors; all unordered edges of the complete graph carry the same positive conductance \(\gamma\), and each vertex has unit \(\ell^2\) mass. The Lipschitz modulus uses the same norm on its domain and codomain and takes the supremum over distinct pairs \(x,y\in\mathbb R^n\). The assertion is for all finite dimensions \(n\ge2\) and all positive \(\gamma\), including arbitrary values not tested numerically. There is no restriction to nonnegative input vectors.

## Proof
**1. Piecewise-linear reduction.** For each \(S\subseteq\{1,\ldots,n\}\), write \(D_S\) for the diagonal mask with entries one on \(S\), zero outside. On the open orthant whose positive support is \(S\), the map \(R\) equals \(D_S\). Along the line segment from \(x\) to \(y\), each coordinate changes sign at most once unless it is identically zero. Splitting the segment at those finitely many crossings and using the triangle inequality yields
\[
\|R(x)-R(y)\|_\gamma\le\max_S\|D_S\|_{\gamma\to\gamma}\,\|x-y\|_\gamma.
\]
Conversely, every \(D_S\) acts on differences of sufficiently nearby points inside its own open orthant, so equality holds for the global modulus:
\[
\operatorname{Lip}_\gamma(R)=\max_S\|D_S\|_{\gamma\to\gamma}.
\]

**2. Exact norm of one mixed mask.** Fix \(S\) of cardinality \(k\) with \(1\le k<n\), and let \(\ell=n-k\). The quadratic-form matrix is \(A=(1+n\gamma)I-\gamma\mathbf1\mathbf1^\top\). For prescribed active coordinates \(z=x|_S\), the numerator \(\|D_Sx\|_\gamma^2\) is fixed, while the denominator \(\|x\|_\gamma^2\) is uniquely minimized by setting every inactive coordinate to
\[
 b=\frac{\gamma\sum_{i\in S}z_i}{1+\gamma k}.
\]
Indeed, differentiating the strictly convex denominator in each inactive coordinate gives \((1+n\gamma)x_j-\gamma\sum_i x_i=0\), whose unique solution is the displayed \(b\). Writing \(a=1+n\gamma\), the resulting quotient is
\[
\frac{a\|z\|_2^2-\gamma(\sum_{i\in S}z_i)^2}
 {a\left[\|z\|_2^2-\frac{\gamma}{1+\gamma k}(\sum_{i\in S}z_i)^2\right]}.
\]
Decompose \(z\) into its constant-vector component and the orthogonal zero-sum component. On the zero-sum component this quotient is \(1\). On the constant component it is
\[
\frac{(1+\gamma k)(1+\gamma\ell)}{1+n\gamma}
=1+\frac{\gamma^2k\ell}{1+n\gamma}.
\]
Since the second value is strictly greater than one, the exact mask norm squared is this expression. Its maximizing directions have equal active coordinates, and the unique optimal inactive coordinates are given by \(b\). The empty and full masks have norms zero and one respectively.

**3. Maximize the support balance, and attain the bound.** Since \(k(n-k)\le\lfloor n^2/4\rfloor\), with equality only for balanced \(k\), the boxed formula and balanced-mask characterization follow. To obtain an actual two-point extremizer, choose a balanced nonempty proper \(S\) and define \(h_i=1\) for \(i\in S\), while \(h_j=\gamma k/(1+\gamma k)\) for \(j\notin S\). Put \(z_i=1\) for \(i\in S\), \(z_j=-1\) otherwise. For sufficiently small \(\varepsilon>0\), both \(z\) and \(z+\varepsilon h\) lie in the same strict sign orthant, and
\[
\frac{\|R(z+\varepsilon h)-R(z)\|_\gamma}{\|\varepsilon h\|_\gamma}
=\|D_S\|_{\gamma\to\gamma}=\operatorname{Lip}_\gamma(R).
\]

**4. One-point contraction and scaling.** The scalar map \(t\mapsto\max(t,0)\) is one-Lipschitz and vanishes at zero, so \(|R(x)_i|\le|x_i|\) and \(|R(x)_i-R(x)_j|\le|x_i-x_j|\). Summation proves \(\|R(x)\|_\gamma\le\|x\|_\gamma\). The two asymptotic laws follow directly by substituting fixed \(\gamma\) or \(\gamma=\lambda/n\) into the exact formula. No finite-sample extrapolation is required.

## Verification
The standalone `CHECK.py` computes every diagonal-mask norm independently through symmetric generalized eigenvalues for sizes \(2\le n\le8\) and four couplings, compares the explicit maximizing direction against the closed formula, and checks exact rational identities for \(2\le n\le17\). Execution reported 2,552 passing comparisons. These checks are consistency tests, not substitutes for the quantified analytical proof. Run with `python CHECK.py`; dependency: NumPy.

## Relationship to prior work
Van Gennip, Guillen, Osting and Bertozzi study finite-graph Laplacians and threshold dynamics, providing the underlying graph-energy setting but not the two-point operator modulus of coordinatewise positive-part truncation. Musina and Nazarov study truncation continuity in continuum fractional Sobolev spaces rather than the sharp finite complete-graph norm. Cai and Wang establish that pointwise ReLU does not increase a graph Dirichlet energy; their lemma concerns each individual embedding, and does not assert two-point nonexpansion or the sharp perturbation factor under a graph energy plus vertex mass. The theorem above computes that missing factor and identifies its balanced-mask extremizers.

## Limitations
The exact balanced-mask formula uses identical positive edge weights on a complete finite graph and unit vertex masses. It is not asserted for arbitrary weighted graphs, other nonlinear activations, continuum Sobolev spaces, or norms without the vertex-mass term. The full classification of all possible pairs attaining the norm is not claimed; the theorem characterizes the locally norming orthants and constructs explicit attaining pairs. Published equivalence in older operator-ideal or Nemytskii literature cannot be completely excluded by the inspected sources and searches.

## References
- Y. van Gennip, N. Guillen, B. Osting and A. L. Bertozzi, *Mean curvature, threshold dynamics, and phase field theory on finite graphs*, arXiv:1307.0045 (first submitted 28 June 2013); *Milan Journal of Mathematics* 82 (2014), 3–65. DOI: 10.1007/s00032-014-0216-8.
- R. Musina and A. I. Nazarov, *A note on truncations in fractional Sobolev spaces*, *Bulletin of Mathematical Sciences* (2017). DOI: 10.1007/s13373-017-0107-8.
- C. Cai and Y. Wang, *A Note on Over-Smoothing for Graph Neural Networks*, arXiv:2006.13318 (2020), especially Lemma 3.3.
