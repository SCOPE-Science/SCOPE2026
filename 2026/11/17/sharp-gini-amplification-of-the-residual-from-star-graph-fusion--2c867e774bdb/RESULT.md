# Sharp Gini amplification of the residual from star-graph fusion

## Finding

Let \(n\ge2\). On a star with hub \(0\) and leaves \(1,\ldots,n-1\), choose arbitrary positive edge penalties \(c_i>0\). Define the unique fitted vector
\[
T_c(x)=\operatorname*{argmin}_{y\in\mathbb R^n}
\left\{\frac12\sum_{i=0}^{n-1}(y_i-x_i)^2+
\sum_{i=1}^{n-1}c_i|y_i-y_0|\right\},
\]
and the **data residual** \(R_c(x)=x-T_c(x)\). For the complete-pair Gini seminorm
\[
G_n(h)=\sum_{0\le i<j<n}|h_i-h_j|,
\]
the exact global two-input Lipschitz coefficient of the residual, for every choice of positive penalties, is
\[
\boxed{\operatorname{Lip}_{G_n}(R_c)=
\max_{2\le m\le n}\frac{(m-1)(2n-m)}{m(n-1)}.}
\]
Every maximizer \(m\) is characterized by \(m(m-1)\le2n\le m(m+1)\). All claimed coefficients are attained by arbitrarily close pairs of actual inputs, not merely by formal active-set matrices. In particular, the coefficient equals \(1\) for \(n=2,3\), is strictly greater than \(1\) for every \(n\ge4\), and obeys
\[
\operatorname{Lip}_{G_n}(R_c)=2-2\sqrt{2/n}+O(1/n)\quad(n\to\infty).
\]
For contrast, the fitted map \(T_c\) itself is Gini-nonexpansive. Thus its complementary residual has a genuine amplification threshold at four vertices, although the fit does not.

## Assumptions and scope

The ambient vectors and penalties are real; the squared fidelity is unweighted, the graph is a finite star, and every edge penalty is strictly positive. One may write \(c_i=\lambda\beta_i\) with arbitrary \(\lambda>0\) and \(\beta_i>0\). The Lipschitz quotient is taken over all input pairs \(x,z\in\mathbb R^n\) with \(G_n(x-z)>0\). Because both the fit and residual commute appropriately with common translations, the quotient seminorm is well defined on the quotient by constants. The residual is the **difference between data and fitted signal**, not the fitted signal.

## Proof

**1. Exact affine regions.** With the hub fit denoted \(u\), leaf stationarity gives \(y_i=u\) when \(|x_i-u|<c_i\), and \(y_i=x_i-c_i\operatorname{sgn}(x_i-u)\) otherwise. The hub equation is
\[
u-x_0-\sum_{i=1}^{n-1}\operatorname{clip}(x_i-u,-c_i,c_i)=0.
\]
Here \(\operatorname{clip}(a,-c,c)=\min\{c,\max\{-c,a\}\}\). Its left side is strictly increasing, hence the fitted vector is uniquely determined. At every open strict-complementarity region, let \(S\) contain the hub and the \(m-1\) leaves fused to it. On this region \(u\) is the average of the input coordinates in \(S\) plus a constant depending on fixed unfused-leaf signs. All unfused leaves respond with derivative \(1\). Consequently the fitted map has derivative \(P_S\), which averages on \(S\) and is the identity outside, and the residual has derivative \(Q_S=I-P_S\), which subtracts the mean on \(S\) and is zero outside. These are the only affine derivatives (up to their values at boundaries). The map is continuous and piecewise affine with finitely many regions; integrating a segment and applying the triangle inequality reduces the global Lipschitz coefficient to the largest \(G_n\)-operator seminorm of these \(Q_S\).

**2. Exact norm of one complementary block projection.** Write \(m=|S|\), \(z=n-m\), and first consider a binary vector with \(j\) ones in \(S\) and \(t\) ones outside, where \(1\le j\le m-1\) and \(0\le t\le z\). Its Gini seminorm is \((j+t)(n-j-t)\). The image under \(Q_S\) is \(1-j/m\) on the \(j\) selected coordinates, \(-j/m\) on the other \(m-j\) coordinates in \(S\), and zero outside. Therefore
\[
G_n(Q_S\mathbf1_E)=\frac{j(m-j)(m+2z)}m.
\]
For fixed \(j\), the concave denominator \((j+t)(n-j-t)\) is minimized at \(t=0\) or \(t=z\). The larger corresponding ratio is
\[
\frac{m+2z}{m}\max\left\{\frac{m-j}{n-j},\frac{j}{j+z}\right\}.
\]
The first term is nonincreasing in \(j\), the second nondecreasing, and the maximum over \(1\le j<m\) is attained at \(j=1\) or \(j=m-1\). Thus its exact binary-cut norm is
\[
\|Q_S\|_{G_n\to G_n}=\frac{(m-1)(m+2z)}{m(n-1)}
=\frac{(m-1)(2n-m)}{m(n-1)}.
\]
For completeness, the transfer from binary indicators to arbitrary real vectors follows from the coarea decomposition of a finite vector (after subtracting its minimum): write \(h=\int \mathbf1_{\{h>t\}}\,dt\), and use the triangle inequality both for \(G_n(Q_Sh)\) and the exact identity \(G_n(h)=\int G_n(\mathbf1_{\{h>t\}})dt\). The cases \(j=0,m\) map to zero, and \(m=1\) gives the zero map.

**3. Maximization and finite-size transition.** Writing the preceding expression as \((2n+1-m-2n/m)/(n-1)\), its forward difference in \(m\) is
\[
\frac{1}{n-1}\left(\frac{2n}{m(m+1)}-1\right).
\]
The exact maximizing integers therefore satisfy \(m(m-1)\le2n\le m(m+1)\). The values for \(n=2,3\) are \(1\), while choosing \(m=3\) for \(n\ge4\) gives \(2(2n-3)/(3(n-1))>1\). The optimum is attained near \(\sqrt{2n}\), yielding the displayed asymptotic expansion.

**4. Attainability by the nonlinear residual.** For any chosen \(m\ge2\), fuse the hub and \(m-1\) specified leaves at fitted value zero; put all other fitted leaf values strictly above zero and well separated. Set the active-edge subgradients to zero and the other edge subgradients to \(+c_i\); define the input as fitted data plus the incidence-divergence of these edge subgradients. The resulting proximal KKT system has strict active-edge slack and strict unfused gaps. For sufficiently small \(\varepsilon>0\), perturb just one fused leaf input by \(\varepsilon\). The fused fit increases by \(\varepsilon/m\) on \(S\), with the other leaves unchanged, and the residual difference is exactly \(\varepsilon Q_S e_i\). Hence its Gini quotient is exactly \((m-1)(2n-m)/(m(n-1))\). This establishes genuine local attainment for every strictly positive penalty vector.

**5. Contrast with the fit.** Each fitted affine derivative \(P_S\) is doubly stochastic. Since complete-pair Gini variation is convex and invariant under coordinate permutations, the Birkhoff representation of doubly stochastic matrices gives \(G_n(P_Sh)\le G_n(h)\). Integrating along input segments proves \(G_n(T_c(x)-T_c(z))\le G_n(x-z)\). This contraction does not imply contraction of \(I-T_c\), as the explicit sharp residual witnesses demonstrate.

## Verification

The standalone standard-library script `check_star_residual.py` carries out exact rational binary-cut enumeration of every possible local pooled-block size through \(n=18\), tests the optimizing integer sizes, constructs actual strictly complementary proximal input pairs reaching the coefficient, and independently solves 1500 random nonlinear proximal pairs using exact one-dimensional KKT roots. Its output is reported in `VERIFICATION.md`. The unrestricted statement is proved analytically above; finite computation is only a diagnostic and witness check.

## Relationship to prior work

Tibshirani, Saunders, Rosset, Zhu and Knight introduced fused-lasso penalization, and Tibshirani and Taylor's generalized-lasso analysis derives fused-coordinate groups and their block-average projection structure. Kirisits, Scherzer and Setterqvist establish universal convex-minimality of the **fitted signal** for anisotropic graph total-variation regularization. Those foundations do not state the precise global **two-input Gini coefficient of the complementary residual** above: the residual involves \(I-P_S\), not the averaging projector \(P_S\). In particular, nonexpansivity or universal minimality of the fit alone does not supply the nontrivial sharp amplification coefficient or the \(\sqrt{2n}\) pooled-block law. Searches and close statement comparisons are documented in `AUDIT.json`; absence from searched records is not a proof of universal historical priority.

## Limitations

Unequal observation masses, nonstar graphs, zero penalties, changing penalties between the two inputs, other norms and other fidelity losses are outside the theorem. The quantity computed is a global worst-case *two-input* coefficient, not a bound on a single residual's dispersion relative to its own input. Historical originality remains provisional pending independent literature review.

## References

1. R. Tibshirani, M. Saunders, S. Rosset, J. Zhu and K. Knight, *Sparsity and smoothness via the fused lasso*, J. R. Stat. Soc. B 67 (2005), 91–108. First publicly dated 2004-12-13. DOI: 10.1111/j.1467-9868.2005.00490.x.
2. R. J. Tibshirani and J. Taylor, *The solution path of the generalized lasso*, Ann. Statist. 39 (2011), 1335–1371. arXiv:1005.1971 (initial submission 2010-05-11).
3. C. Kirisits, O. Scherzer and E. Setterqvist, *Invariant \(\varphi\)-minimal sets and total variation denoising on graphs*, SIAM J. Imaging Sci. 12 (2019), 1643–1668. arXiv:1807.10514 (initial submission 2018-07-27).
