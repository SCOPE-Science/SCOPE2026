# Exact Jung-defect decomposition in constant-curvature space forms

## Result

Let \(X^n_\kappa\) be one of the simply connected constant-curvature spaces
\[
\mathbb R^n\quad(\kappa=0),\qquad \mathbb S^n\quad(\kappa=+1),\qquad \mathbb H^n\quad(\kappa=-1),
\]
with curvature normalized to \(0,+1,-1\). In the spherical case, assume the compact set below lies in the non-antipodal Jung regime; it is enough to assume its diameter
\[
0<D<\arccos(-1/n).
\]

Let \(K\subset X^n_\kappa\) be compact with diameter \(D>0\), and let \(B(c,R)\) be a minimum enclosing ball. Choose active boundary points
\[
p_1,\dots,p_m\in K\cap\partial B(c,R),\qquad 2\le m\le n+1,
\]
and positive weights \(\lambda_i\) such that
\[
\sum_{i=1}^m\lambda_i=1,
\qquad
\sum_{i=1}^m\lambda_i u_i=0,
\tag{1}
\]
where \(u_i\in T_cX^n_\kappa\) is the unit initial tangent of the geodesic from \(c\) to \(p_i\). Such a support exists by first-order optimality of the circumcenter and Carathéodory's theorem. Pad the weight vector by zeros to length \(n+1\).

Define
\[
\Phi_0(t)=\frac{t^2}{2},\qquad
\Phi_+(t)=1-\cos t,\qquad
\Phi_-(t)=\cosh t-1,
\]
and
\[
\Psi_0(R)=R^2,\qquad
\Psi_+(R)=\sin^2R,\qquad
\Psi_-(R)=\sinh^2R.
\]
Then there is an exact support identity
\[
\boxed{
\Psi_\kappa(R)
=2\sum_{1\le i<j\le m}\lambda_i\lambda_j\,
\Phi_\kappa(d(p_i,p_j)).
}
\tag{2}
\]
Consequently the normalized Jung deficit
\[
\varepsilon_\kappa(K)
:=\frac{\frac{n}{n+1}\Phi_\kappa(D)-\Psi_\kappa(R)}{\Phi_\kappa(D)}
\tag{3}
\]
admits the exact nonnegative decomposition
\[
\boxed{
\varepsilon_\kappa(K)
=\sum_{i=1}^{n+1}\left(\lambda_i-\frac1{n+1}\right)^2
+2\sum_{1\le i<j\le m}\lambda_i\lambda_j
\left(1-\frac{\Phi_\kappa(d(p_i,p_j))}{\Phi_\kappa(D)}\right).
}
\tag{4}
\]
Thus the Jung deficit splits exactly into a barycentric-imbalance term and a weighted edge-shortfall term.

Equation (4) immediately recovers the sharp Jung inequalities
\[
R^2\le \frac{n}{2(n+1)}D^2,
\tag{5a}
\]
\[
\sin^2R\le \frac{n}{n+1}(1-\cos D),
\tag{5b}
\]
and
\[
\sinh^2R\le \frac{n}{n+1}(\cosh D-1).
\tag{5c}
\]
Equality holds if and only if the active support consists of \(n+1\) equally weighted points with every mutual distance equal to \(D\), hence is a regular \(n\)-simplex of edge length \(D\). For a general compact \(K\), this characterizes the extremal support (equivalently, \(K\) contains such a diameter simplex), not necessarily every point of \(K\).

## Sharp support-dimension hierarchy

Let \(\nu(K)\) be the least number of active points in a positive equilibrium support satisfying (1). Then
\[
\boxed{
\nu(K)\ge
\left\lceil
\frac{1}{\varepsilon_\kappa(K)+\frac1{n+1}}
\right\rceil.
}
\tag{6}
\]
Equivalently, any support of cardinality \(m\) satisfies the sharp inequality
\[
\boxed{
\Psi_\kappa(R)\le \frac{m-1}{m}\,\Phi_\kappa(D).
}
\tag{7}
\]
Both statements are sharp for every \(m=2,\dots,n+1\): equality is attained by a regular \((m-1)\)-simplex of edge length \(D\), embedded in \(X^n_\kappa\).

In particular,
\[
\boxed{
\varepsilon_\kappa(K)<\frac1{n(n+1)}
\quad\Longrightarrow\quad
\nu(K)=n+1.
}
\tag{8}
\]
The threshold is exact: a regular \((n-1)\)-simplex has
\[
\varepsilon_\kappa=\frac1n-\frac1{n+1}=\frac1{n(n+1)}.
\]
So sufficiently near equality in Jung's inequality forces a full \(n\)-dimensional circum-support before any global shape comparison is invoked.

## Quantitative balance and edge control

From (4), every equilibrium support obeys
\[
\boxed{
\sum_{i=1}^{n+1}\left(\lambda_i-\frac1{n+1}\right)^2
\le \varepsilon_\kappa(K)
}
\tag{9}
\]
and
\[
\boxed{
2\sum_{i<j}\lambda_i\lambda_j
\left(1-\frac{\Phi_\kappa(d(p_i,p_j))}{\Phi_\kappa(D)}\right)
\le \varepsilon_\kappa(K).
}
\tag{10}
\]
If \(\varepsilon:=\varepsilon_\kappa(K)<1/[n(n+1)]\), then \(m=n+1\) and every weight satisfies
\[
\lambda_i\ge
\ell_n(\varepsilon)
:=\frac1{n+1}-\sqrt{\frac{n\varepsilon}{n+1}}>0.
\tag{11}
\]
Hence every support edge satisfies
\[
\boxed{
\frac{\Phi_\kappa(d(p_i,p_j))}{\Phi_\kappa(D)}
\ge 1-\frac{\varepsilon}{2\ell_n(\varepsilon)^2}.
}
\tag{12}
\]
whenever the right-hand side is nonnegative. Thus the same scalar Jung deficit controls both the support weights and each active edge.

## Proof

### 1. Active equilibrium support

Consider
\[
f(x)=\max_{p\in K}d(x,p).
\]
At a minimizing center \(c\), let \(A=K\cap\partial B(c,R)\) be the active set. If the origin were not in the convex hull of the unit tangent directions \(u_p\in T_cX^n_\kappa\) toward active points, a separating tangent vector would strictly decrease all active distances to first order; compactness would then decrease the maximum distance, contradicting minimality. Hence
\[
0\in\operatorname{conv}\{u_p:p\in A\}.
\]
Carathéodory's theorem supplies at most \(n+1\) active directions whose positive convex combination is zero, giving (1) after discarding redundant zero coefficients. In the spherical case, choosing any point of \(K\) as a center gives \(R\le D<\pi\). Hence no active point is antipodal to \(c\), so the relevant distance functions are smooth at the center; the stronger classical conclusion \(R<\pi/2\) in the stated Jung regime is not needed for this first-order step.

### 2. A space-form cosine identity

For active points \(p_i=\exp_c(Ru_i)\) and \(p_j=\exp_c(Ru_j)\), the Euclidean, spherical, and hyperbolic laws of cosines give respectively
\[
\frac{d_{ij}^2}{2}=R^2(1-\langle u_i,u_j\rangle),
\]
\[
1-\cos d_{ij}=\sin^2R\,(1-\langle u_i,u_j\rangle),
\]
and
\[
\cosh d_{ij}-1=\sinh^2R\,(1-\langle u_i,u_j\rangle).
\]
Thus in all three cases
\[
\Phi_\kappa(d_{ij})
=\Psi_\kappa(R)(1-\langle u_i,u_j\rangle).
\tag{13}
\]
On the other hand, (1) implies
\[
0=\left\|\sum_i\lambda_i u_i\right\|^2
=\sum_i\lambda_i^2+2\sum_{i<j}\lambda_i\lambda_j\langle u_i,u_j\rangle,
\]
while \((\sum_i\lambda_i)^2=1\). Subtracting yields
\[
\sum_{i<j}\lambda_i\lambda_j(1-\langle u_i,u_j\rangle)=\frac12.
\tag{14}
\]
Multiplying (14) by \(2\Psi_\kappa(R)\) and using (13) proves (2).

### 3. Exact Jung deficit decomposition

Since all support distances satisfy \(d_{ij}\le D\), write
\[
\begin{aligned}
\frac{n}{n+1}\Phi_\kappa(D)-\Psi_\kappa(R)
&=\frac{n}{n+1}\Phi_\kappa(D)
-2\sum_{i<j}\lambda_i\lambda_j\Phi_\kappa(d_{ij})\\
&=\Phi_\kappa(D)
\left(\sum_i\lambda_i^2-\frac1{n+1}\right)\\
&\quad+2\sum_{i<j}\lambda_i\lambda_j
\bigl(\Phi_\kappa(D)-\Phi_\kappa(d_{ij})\bigr).
\end{aligned}
\tag{15}
\]
After zero-padding to \(n+1\) coordinates,
\[
\sum_i\lambda_i^2-\frac1{n+1}
=\sum_{i=1}^{n+1}\left(\lambda_i-\frac1{n+1}\right)^2.
\]
Divide (15) by \(\Phi_\kappa(D)\) to obtain (4). Its two terms are nonnegative, proving (5). Equality forces both terms to vanish, hence \(m=n+1\), \(\lambda_i=1/(n+1)\), and \(d_{ij}=D\) for every pair. The converse is immediate.

### 4. Support hierarchy and componentwise stability

For a support with \(m\) positive weights,
\[
\sum_{i=1}^m\lambda_i^2\ge\frac1m.
\]
Equation (15) therefore gives
\[
\varepsilon_\kappa(K)\ge \frac1m-\frac1{n+1},
\]
which is equivalent to (6) and (7). A regular \((m-1)\)-simplex has equal weights and all its active edges equal to \(D\), so equality is attained.

Equation (9) is the first term of (4), and (10) is the second. If \(m=n+1\), write \(x_i=\lambda_i-1/(n+1)\), so \(\sum_i x_i=0\) and \(\sum_i x_i^2\le\varepsilon\). For any fixed \(i\), Cauchy--Schwarz applied to the other \(n\) coordinates gives
\[
\varepsilon\ge x_i^2+\frac{x_i^2}{n}
=\frac{n+1}{n}x_i^2.
\]
This proves (11). Finally, each summand of (10) is nonnegative, so
\[
2\lambda_i\lambda_j
\left(1-\frac{\Phi_\kappa(d_{ij})}{\Phi_\kappa(D)}\right)
\le\varepsilon,
\]
and (11) yields (12).

## Relation to prior work

Jung's classical Euclidean theorem gives the sharp circumradius--diameter bound and regular-simplex equality case. Dekster established spherical and hyperbolic Jung theorems, and Lang--Schroeder extended Jung-type bounds to Alexandrov spaces of curvature bounded above. A recent hyperbolic convex-geometry treatment records the existence of at most \(n+1\) circum-support points and the regular-simplex equality characterization. Schneider proved a different Euclidean/Minkowski stability theorem: near equality in a Jung-type ratio forces a convex body to be close to a simplex in Banach--Mazur distance.

The Euclidean weighted identity underlying (2) is also closely related to standard dual formulations of the minimum-enclosing-ball problem, so no novelty is claimed for that Euclidean ingredient by itself. The claim here is the unified constant-curvature identity (2), its exact nonnegative Jung-defect decomposition (4), and the sharp support-cardinality hierarchy (6)--(8), together with the direct balance and active-edge consequences (9)--(12).

Searches under “Jung theorem stability,” “quantitative Jung inequality,” “minimum enclosing ball support weights,” “spherical/hyperbolic Jung defect,” “circumradius diameter stability,” and equivalent Chebyshev-center language did not locate these displayed space-form identities or the sharp deficit-to-support-number threshold. The originality claim is therefore only to the best of our knowledge.

## Limitations

- The spherical statement is restricted to the non-antipodal Jung regime; the displayed normalization is not intended for large spherical sets whose minimum enclosing radius reaches \(\pi/2\).
- The quantitative conclusion controls the active circum-support, not the entire set in Hausdorff or Banach--Mazur distance.
- The decomposition is proved only for the three simply connected constant-curvature model spaces. Lang--Schroeder's much more general CAT\((\kappa)\) setting does not provide the exact cosine-law equality used here.
- Originality is to the best of our knowledge. The full text of Dekster's 1995 paper was not available in a directly inspectable form in this check, and its proof is the most plausible older source in which part of the constant-curvature calculation could already appear implicitly. Lang--Schroeder's 1997 generalization is a second residual-risk source.

## Reproducibility

Given an active support \((u_i,\lambda_i)\) satisfying (1), verify (13) from the appropriate law of cosines and (14) by expanding \(\|\sum_i\lambda_i u_i\|^2\). Equation (2) follows immediately; adding and subtracting \(2\Phi_\kappa(D)\sum_{i<j}\lambda_i\lambda_j\) gives (15) and hence all stated inequalities. No numerical computation is needed.

## References

1. H. Jung, *Über die kleinste Kugel, die eine räumliche Figur einschliesst*, J. Reine Angew. Math. 123 (1901), 241--257.
2. B. V. Dekster, *The Jung theorem for spherical and hyperbolic spaces*, Acta Math. Hungar. 67 (1995), 315--331. https://doi.org/10.1007/BF01874495
3. U. Lang, V. Schroeder, *Jung's theorem for Alexandrov spaces of curvature bounded above*, Ann. Global Anal. Geom. 15 (1997), 263--275. https://doi.org/10.1023/A:1006574402955
4. R. Schneider, *Stability for Some Extremal Properties of the Simplex*, J. Geom. 96 (2009), 135--148. https://doi.org/10.1007/s00022-010-0028-0
5. F. Nielsen, G. Hadjeres, *Approximating Covering and Minimum Enclosing Balls in Hyperbolic Geometry*, GSI 2015, LNCS 9389, 586--594. https://doi.org/10.1007/978-3-319-25040-3_63
6. H. Hirai, *On a manifold formulation of self-concordant functions*, arXiv:2212.10981.
7. K. J. Böröczky, A. Csépai, Á. Sagmeister, *Hyperbolic width functions and characterizations of bodies of constant width in the hyperbolic space*, J. Geom. 115 (2024), 15. https://doi.org/10.1007/s00022-024-00714-9
