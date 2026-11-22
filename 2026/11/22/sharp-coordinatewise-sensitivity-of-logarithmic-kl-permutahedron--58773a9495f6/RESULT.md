# Sharp coordinatewise sensitivity of logarithmic KL permutahedron projection

## Finding
Let \(n\ge 2\), let \(b=(b_1,\ldots,b_n)\in(0,\infty)^n\) be nonconstant, and put \(B=\sum_i b_i\), \(m=\min_i b_i\), and \(\mathcal P(b)=\operatorname{conv}\{(b_{\pi(1)},\ldots,b_{\pi(n)}):\pi\in S_n\}\). Define
\[
F_b(z)=\log\left[\operatorname*{argmin}_{\mu\in\mathcal P(b)}\sum_{i=1}^n\left(\mu_i\log\frac{\mu_i}{e^{z_i}}-\mu_i+e^{z_i}\right)\right],\quad z\in\mathbb R^n,
\]
where logarithm is componentwise. The exact global two-input coefficient in the coordinate maximum norm is
\[
\sup_{z\ne z'}\frac{\|F_b(z)-F_b(z')\|_\infty}{\|z-z'\|_\infty}=2\left(1-\frac mB\right).
\]
The supremum is approached at interior projections converging to permutahedron vertices, but it is not attained by any distinct finite inputs. In particular, the entropy-regularized soft-rank map based on \(b=(e^n,e^{n-1},\ldots,e)\) and scale \(\varepsilon>0\) has coefficient
\[
\frac2\varepsilon\left(1-\frac{e-1}{e^n-1}\right).
\]
This is strictly greater than the quadratic-regularized soft-rank coefficient \((2-2/n)/\varepsilon\) for every \(n\ge2\).

## Assumptions and scope
All inputs are arbitrary real \(n\)-vectors; all target weights are strictly positive, and nonconstancy is essential. The case of constant \(b\) gives a singleton permutahedron and a constant map, with Lipschitz coefficient zero. The logarithmic projection is well defined since every coordinate of any feasible \(\mu\) is at least \(m>0\). For the soft-rank specialization, the sign reversal of the scores leaves the Lipschitz coefficient unchanged.

## Proof
**1. Local Jacobian.** Sort \(z\) and \(b\) in decreasing order. The isotonic reduction of the log-KL permutahedron projection partitions coordinates into blocks \(I\), on each of which the output satisfies \(\mu_i=c_I e^{z_i}\) with a positive common scale \(c_I\) and \(\sum_{i\in I}\mu_i\) fixed. On a smooth active-set region, differentiation yields
\[
\frac{\partial F_{b,i}}{\partial z_j}=\delta_{ij}-\mathbf1_{\{i,j\in I\}}\frac{\mu_j}{\sum_{k\in I}\mu_k}\quad(i\in I).
\]
The row absolute sum is exactly \(2(1-\mu_i/\sum_{k\in I}\mu_k)\) (and is zero on singleton blocks). For every feasible \(\mu\), we have \(\mu_i\ge m\) and \(\sum_{k\in I}\mu_k\le B\); hence every Jacobian has induced \(\ell_\infty\) norm at most \(2(1-m/B)\). The map is continuous and locally Lipschitz: the isotonic representation has finitely many sorting/block types, each with a smooth formula on its type region and denominators bounded away from zero. Integrating its almost-everywhere derivative along any segment proves the stated global upper bound.

**2. Sharpness.** Since \(b\) is not constant, its permutahedron has affine hull \(\sum_i\mu_i=B\) and its centroid \(\bar b\mathbf1\), \(\bar b=B/n\), lies in the relative interior. Fix a permutation \(v\) of \(b\) with \(v_j=m\), and let \(\mu^{(\delta)}=(1-\delta)v+\delta\bar b\mathbf1\) for \(0<\delta<1\). This is in the relative interior. At \(z^{(\delta)}=\log\mu^{(\delta)}\), the KL projector is \(\mu^{(\delta)}\); for sufficiently small changes to \(z\), only the total-mass equality is active, so
\[
F_b(z)=z+\log B\,\mathbf1-\log\left(\sum_i e^{z_i}\right)\mathbf1.
\]
Its Jacobian row \(j\) has absolute sum \(2(1-\mu^{(\delta)}_j/B)\), realized infinitesimally by a sign vector taking value \(+1\) at \(j\) and \(-1\) elsewhere. Letting \(\delta\downarrow0\) proves the reverse bound.

**3. Strict finite-pair inequality.** On an open differentiability cell with a proper block \(I\), there are coordinates outside \(I\) carrying positive total mass; thus \(\sum_{k\in I}\mu_k<B\) and the row norm is strictly smaller than \(2(1-m/B)\). On a full-block cell, the projected point is in the relative interior of the permutahedron, so \(\mu_i>m\) for all \(i\); again the row bound is strict. Along any affine input segment the sorted-coordinate and pool-block structure changes only on boundaries of finitely many real-analytic formulas. On open subsegments in a fixed lower-dimensional tie stratum, the one-dimensional derivative is the restriction of an adjacent smooth formula; if the projected coordinate remains fixed at its vertex-minimum value its derivative is zero. Therefore on every nonconstant segment the coordinate derivatives have absolute value strictly less than the displayed coefficient almost everywhere. Absolute continuity and integration yield strict inequality for any two distinct inputs. The only possible sharp limit is consequently a degeneration of the full-block region toward a vertex, as constructed above.

**4. Quadratic comparator.** Euclidean projection onto any nondegenerate permutahedron has a.e. derivative with blocks equal to coordinate-centering matrices \(I-|I|^{-1}\mathbf1\mathbf1^\top\). Their maximum absolute row sum is \(2-2/n\), realized on the full-dimensional relative interior of the permutahedron. Since nonconstant positive \(b\) obeys \(m/B<1/n\), the entropic coefficient is strictly larger. Substituting geometric weights yields the soft-rank formula.

## Verification
The standalone script `check_projection.py` implements the isotonic pool-adjacent-violators projection in log coordinates, tests deterministic random input pairs against the claimed coefficient, and approaches the coefficient from the interior at increasing vertex proximity. These finite checks corroborate, but do not replace, the universal proof. Run with Python 3, NumPy, and SciPy: `python check_projection.py`.

## Relationship to prior work
Blondel, Teboul, Berthet, and Djolonga (2020, arXiv:2002.08871) define the log-KL permutahedron projection and provide its blockwise Jacobian (Proposition 3, Lemma 2, Proposition 4). Lim and Wright (2016) establish general Bregman projection reductions for permutahedra. Those formulas and the underlying algorithm are prior work; the finding here is the sharp **global** coordinatewise modulus, its dependence only on the least vertex coordinate relative to total mass, nonattainment, and the exact quantitative contrast with quadratic soft-ranking. None of those sharp global assertions appears in the inspected main texts. Published equivalents under alternative convex-duality language remain possible.

## Limitations
The result is finite-dimensional, assumes strictly positive and nonconstant \(b\), and concerns the logarithm of the KL projection, not the unlogged Bregman projector or entropic optimal-transport Sinkhorn ranks. It does not assert independent validation or absolute historical priority. Its sharpness is asymptotic near a vertex, not a finite pair attaining equality.

## References
- M. Blondel, O. Teboul, Q. Berthet, J. Djolonga, *Fast Differentiable Sorting and Ranking*, arXiv:2002.08871, first submitted 2020-02-20; ICML/PMLR 119 (2020), https://proceedings.mlr.press/v119/blondel20a.html.
- C. H. Lim and S. J. Wright, *Efficient Bregman Projections onto the Permutahedron and Related Polytopes*, AISTATS/PMLR 51 (2016), https://proceedings.mlr.press/v51/lim16.html.
