# Sharp coordinatewise sensitivity of logarithmic KL permutahedron projection

## Finding

Let \(n\ge2\), let \(b\in(0,\infty)^n\) be nonconstant, set \(B=\sum_i b_i\), \(m=\min_i b_i\), and let \(\mathcal P(b)\) be the convex hull of the coordinate permutations of \(b\). For \(z\in\mathbb R^n\), define
\[
F_b(z)=\log\operatorname*{argmin}_{\mu\in\mathcal P(b)}\sum_i[\mu_i\log(\mu_i/e^{z_i})-\mu_i+e^{z_i}],
\]
where the logarithm of the minimizer is componentwise. Its sharp two-input Lipschitz coefficient in the coordinate maximum norm is \(2(1-m/B)\). No distinct finite inputs attain this coefficient. It can be approached with relative-interior projections tending to a vertex, or more generally to any feasible point with some coordinate equal to \(m\).

For the entropy-regularized soft rank with target \(b=(e^n,e^{n-1},\ldots,e)\) and score scaling \(-1/\varepsilon\), \(\varepsilon>0\), the sharp coefficient is \(2\varepsilon^{-1}(1-(e-1)/(e^n-1))\). The quadratic soft rank has sharp coefficient \((2-2/n)/\varepsilon\), which is strictly smaller.

## Assumptions and scope

The objective is strictly convex on the feasible set and the minimum exists by compactness. Every feasible coordinate is at least \(m>0\), so all logged coordinates are defined. A constant \(b\) instead gives a constant map and coefficient zero. The theorem concerns the logged projection, not the unlogged KL projection or a Sinkhorn map.

## Proof

**Block formulas along segments.** Sort \(z\) and \(b\) decreasingly. Use the isotonic reduction of Blondel et al., Proposition 3 and Lemma 2. In sorted order a pool \(I\) is an interval with mass \(B_I=\sum_{j\in I}b_j\) in that order. The output on it satisfies
\[
F_{b,i}(z)=z_i+\log B_I-\log\sum_{j\in I}e^{z_j},\qquad i\in I.
\]
Undo the sorting permutation in the output. The row of the derivative of this formula has absolute sum \(2(1-\mu_i/B_I)\), since the derivative row is \(\delta_{ij}-\mathbf1_{j\in I}\mu_j/B_I\).

These formulas also apply piecewise to any affine input segment, including a segment contained in a tie stratum. Sorting changes only at finitely many nonidentical linear crossings; equal inputs along the whole segment can be ordered by a fixed tie rule. Pool-adjacent-violators compares values \(\log\sum_{j\in I}e^{z_j}-\log B_I\) for candidate consecutive intervals \(I\). Each possible comparison after sorting is a difference of real-analytic functions of the segment parameter, analytic on a neighborhood of the whole closed parameter interval with that fixed ordering. It has finitely many zeros there unless it is identically zero, in which case use a fixed tie rule. There are only finitely many comparisons. Thus along the segment the output is a finite piecewise-smooth selection of the formulas. The projection is continuous, by compactness, continuity of the objective and uniqueness of the minimizer; the piecewise-smooth selection is therefore absolutely continuous along the segment.

**Upper bound and strictness.** For \(z(t)=z+t(z'-z)\), \(0\le t\le1\), set \(h=z'-z\). On a smooth segment piece the row bound gives \(|(F_{b,i}\circ z)'(t)|\le2(1-\mu_i/B_I)\|h\|_\infty\). When \(I\) is proper, the inequality \(B_I<B\) makes the coefficient strictly less than \(2(1-m/B)\). For a full pool, the same is true if \(\mu_i>m\). At any differentiability time \(0<t<1\) with \(\mu_i=m\), the scalar output \(F_{b,i}(z(t))\) attains its lower bound \(\log m\), and its derivative is zero. For \(h\ne0\), the bound by \(2(1-m/B)\|h\|_\infty\) is consequently strict almost everywhere for every coordinate. Integrating and taking the maximum over finitely many coordinates proves the upper bound and excludes finite-pair equality.

**Sharpness.** The affine hull is \(\sum_i\mu_i=B\): differences of permutations put a nonzero multiple of \(e_i-e_j\) into the span for every pair \(i,j\). The centroid \(c=(B/n)\mathbf1\) lies in the relative interior, as it is a positive average of all vertices. Choose any feasible \(v\) with \(v_j=m\), and for \(0<\eta<1\) let \(\mu^\eta=(1-\eta)v+\eta c\), in the relative interior. In a neighborhood of \(z=\log\mu^\eta\) the total-mass-only minimizer \(B e^z/\sum_i e^{z_i}\) remains feasible, hence is the minimizer. The \(j\)-th derivative row of its logarithm has absolute sum \(2(1-\mu_j^\eta/B)\), realized using \(+1\) in coordinate \(j\) and \(-1\) elsewhere. Taking local pair ratios and then \(\eta\downarrow0\) proves sharpness. In particular the limit point need not be a vertex: for \(b=(3,2,1)\), one can take \(v=(5/2,5/2,1)\), the midpoint of a minimum-coordinate edge.

**Soft ranks.** In Blondel et al., equation (6), the sorted rank target is \(\rho=(n,n-1,\ldots,1)\). The entropy map uses \(b=e^\rho\), with \(m/B=(e-1)/(e^n-1)\); the quadratic map uses Euclidean projection onto \(\mathcal P(\rho)\). Its affine-cell derivatives are coordinate-centering blocks \(I-|I|^{-1}\mathbf1\mathbf1^\top\) after permutation. Their absolute row sums are \(2-2/|I|\). The continuous piecewise-affine projector has coefficient at most \(2-2/n\) by segment integration, and the full centering derivative is realized in a neighborhood of a relative-interior point, giving equality for the coefficient. The scaling contributes \(1/\varepsilon\), irrespective of the score sign. Finally, \(m/B<1/n\) because the weights are nonconstant.

## Verification and relation to prior work

The proof above gives the all-input assertion. The accompanying `check_projection.py` (Python, NumPy, SciPy) gives supplementary finite PAV checks for geometric weights and tests one vertex-limit construction. Those checks do not prove the general assertion and do not test every feasible limit point.

Blondel–Teboul–Berthet–Djolonga provide the map and its local blockwise Jacobians; Lim–Wright establish the broader projection reduction. The distinction is the sharp global maximum-norm coefficient and strict finite-pair inequality, not a new projector, soft-rank definition, or differentiation algorithm. The literature comparison is not a certification of absolute priority.

## References

- M. Blondel, O. Teboul, Q. Berthet and J. Djolonga, *Fast Differentiable Sorting and Ranking*, ICML/PMLR 119 (2020), arXiv:2002.08871, equation (6), Propositions 3–4 and Lemma 2.
- C. H. Lim and S. J. Wright, *Efficient Bregman Projections onto the Permutahedron and Related Polytopes*, AISTATS/PMLR 51 (2016), §3.
