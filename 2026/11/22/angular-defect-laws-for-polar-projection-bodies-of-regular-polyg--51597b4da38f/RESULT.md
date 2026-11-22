# Angular defect laws for polar projection bodies of regular polygons

## Finding

Let \(K_N\) be the regular \(N\)-gon with circumradius one and center at the origin, where \(N\ge4\) is even. Let \(\Pi K_N\) be its projection body and \(K_N^\circ\) its polar. Write \(\alpha=\pi/N\), \(c=\cos\alpha\), \(s=\sin\alpha\), and choose \(\Theta\) uniformly on \([0,2\pi)\). Define the dimensionless directional ratio
\[
R_N(\Theta)=\frac{h_{\Pi K_N}(e_\Theta)}{h_{K_N^\circ}(e_\Theta)},\qquad e_\Theta=(\cos\Theta,\sin\Theta).
\]
The known exact planar parity phenomenon is \(R_N\equiv2c\) when \(N\equiv2\pmod4\). In the complementary case \(4\mid N\), the ratio has support \([2c^2,2]\), with exact cumulative distribution function
\[
\Pr(R_N\le r)=\begin{cases}
0,&r<2c^2,\\
1-\dfrac1\alpha\arctan\!\left(\dfrac{c(2-r)}{sr}\right),&2c^2\le r\le2,\\
1,&r>2.
\end{cases}
\]
Thus its interior density is \(2cs/[\alpha(s^2r^2+c^2(2-r)^2)]\). Along multiples of four, the random variable \((2-R_N)/(2\sin^2\alpha)\) converges in distribution to the uniform law on \([0,1]\).

For the least-squares homothety, define
\[
E_N=\min_{\lambda>0}\int_0^{2\pi}\bigl(h_{\Pi K_N}(e_\theta)-\lambda h_{K_N^\circ}(e_\theta)\bigr)^2\,d\theta.
\]
For \(N\equiv2\pmod4\), the unique minimum is at \(\lambda=2c\) and \(E_N=0\). For \(4\mid N\), the unique minimizer and positive squared error are
\[
\lambda_{2,N}=\frac{2c(s+\alpha c)}{\alpha+sc},\qquad
E_N=\frac{4Ns^2(\alpha^2-s^2)}{\alpha+sc}.
\]
The scale-free relative squared error is
\[
\frac{E_N}{\int_0^{2\pi}h_{\Pi K_N}(e_\theta)^2\,d\theta}
=\frac{s^2(\alpha^2-s^2)}{(\alpha+sc)^2}.
\]
For \(4\mid N\), the unique best Hausdorff homothety is different:
\[
\lambda_{\infty,N}=2c>\lambda_{2,N},\qquad
\min_{\lambda>0}d_H(\Pi K_N,\lambda K_N^\circ)=2(1-c).
\]
In particular, as \(N\to\infty\) through multiples of four,
\[
E_N=\frac{2\pi^5}{3N^4}+O(N^{-6}),\quad
\sqrt{\frac{E_N}{\int h_{\Pi K_N}^2}}=\frac{\pi^2}{2\sqrt3N^2}+O(N^{-4}),\quad
\min_\lambda d_H=\frac{\pi^2}{N^2}+O(N^{-4}).
\]

## Assumptions and scope

The Euclidean metric, standard angular measure, and unnormalized projection body \(h_{\Pi K}(u)=\operatorname{length}(\operatorname{proj}_{u^\perp}K)\) are used throughout. The polar is \(K^\circ=\{y:x\cdot y\le1\text{ for all }x\in K\}\). These formulas concern centered, Euclidean-circumradius-one regular polygons with an even vertex count. They assert no stability theorem for arbitrary planar convex bodies.

## Proof

**Step 1: projection and polarity.** For any centrally symmetric planar convex body \(K\), the length of its shadow perpendicular to a direction \(u\) is twice its support function in the perpendicular direction. Consequently \(\Pi K=2QK\), where \(Q\) is rotation through \(\pi/2\). The polar of \(K_N\) has vertices in directions \((2j+1)\pi/N\), of radius \(1/c\). When \(N\equiv2\pmod4\), a quarter-turn rotates \(K_N\) through one half of a vertex step, modulo a symmetry of \(K_N\). Therefore \(QK_N=cK_N^\circ\), proving the stated known exact branch. When \(4\mid N\), a quarter-turn fixes \(K_N\), hence \(h_{\Pi K_N}=2h_{K_N}\).

**Step 2: angular reduction and exact distribution.** On a sector whose vertex direction is zero, let \(u\in[0,\alpha]\) be the unsigned angular distance to that vertex. Directly from the vertices of \(K_N\) and \(K_N^\circ\),
\[
h_{\Pi K_N}=2\cos u,\qquad h_{K_N^\circ}=c^{-1}\cos(\alpha-u),\qquad
R_N=\frac{2c\cos u}{\cos(\alpha-u)}.
\]
Folding a uniform direction into the nearest-vertex sector makes \(u\) uniform on \([0,\alpha]\). The ratio is strictly decreasing, since its derivative has sign \(-\sin\alpha\), and it takes endpoint values \(2\) and \(2c^2\). Solving \(R_N(u)=r\) gives \(u=\arctan(c(2-r)/(sr))\), so \(\Pr(R_N\le r)=1-u/\alpha\). Differentiation proves the density. Uniformly for \(t\in[0,1]\), Taylor expansion yields
\[
R_N(\alpha t)=2-2\alpha^2 t+O(\alpha^4),\qquad 2\sin^2\alpha=2\alpha^2+O(\alpha^4).
\]
Because \(t=u/\alpha\) is uniform, the normalized ratio converges to a uniform random variable.

**Step 3: exact least-squares integrals.** Integrating the two elementary sector support functions and summing the \(N\) congruent angular sectors gives
\[
\begin{aligned}
A&=\int_0^{2\pi}h_{\Pi K_N}^2\,d\theta=4N(\alpha+sc),\\
B&=\int_0^{2\pi}h_{K_N^\circ}^2\,d\theta=\frac N{c^2}(\alpha+sc),\\
C&=\int_0^{2\pi}h_{\Pi K_N}h_{K_N^\circ}\,d\theta=\frac{2N}{c}(s+\alpha c).
\end{aligned}
\]
The quadratic \(A-2\lambda C+\lambda^2B\) has unique positive minimizer \(C/B\) and minimum \(A-C^2/B\). The exact factorization
\[
(\alpha+sc)^2-(s+\alpha c)^2=s^2(\alpha^2-s^2)
\]
yields the formulas for \(\lambda_{2,N}\), \(E_N\), and their normalized quotient. Positivity follows from \(0<s<\alpha\). For the known \(N\equiv2\pmod4\) branch, the minimum is zero and is uniquely attained at \(2c\).

**Step 4: uniform error.** For \(4\mid N\), the difference of support functions at the trial scale \(\lambda=2c\) is \(2\cos u-2\cos(\alpha-u)\), strictly decreasing from \(2(1-c)\) to \(-2(1-c)\). It follows that the Hausdorff error is exactly \(2(1-c)\). For any \(\lambda<2c\), the error at \(u=0\) is \(2-\lambda>2(1-c)\); for any \(\lambda>2c\), the error at \(u=\alpha\) has magnitude \(\lambda/c-2c>2(1-c)\). This proves the unique global Hausdorff minimizer. The strict inequality between the two optimal scales follows from \((\alpha+sc)-(s+\alpha c)=(1-c)(\alpha-s)>0\).

**Step 5: asymptotics.** Expand \(s=\alpha-\alpha^3/6+O(\alpha^5)\), \(c=1-\alpha^2/2+O(\alpha^4)\) in the exact formulas, using \(N=\pi/\alpha\). The leading terms are precisely those stated above; analyticity of the trigonometric expressions supplies the stated remainders.

## Verification

The accompanying standalone Python 3 script `verify_polar_defect.py` constructs both polygonal vertex sets and their polars, computes projection lengths directly from vertex extrema (without using the sector formula), compares direct angular quadrature with the exact least-squares and Hausdorff values for \(N=4,6,8,10,12,16,20\), checks the stated cumulative distribution against angular frequencies, and tests three large-side asymptotic examples. These are finite numerical cross-checks; the proof above is the justification for arbitrary even \(N\) and all directions. Run `python3 verify_polar_defect.py` in the same directory.

## Relationship to prior work

The planar exactness branch and the failure of planar ellipsoid rigidity are established background: Zhang's 2026 paper explicitly gives the regular hexagon as a polar-projection counterexample, and Mandal, Sain, and Paul prove the regular-polygon Radon parity criterion, noting its earlier observation by Heil. Their results do not state the present complete directional-ratio distribution, normalized uniform scaling limit, the exact least-squares defect, or the distinct optimal homotheties for the two geometric metrics. The calculation is thus a quantitative supplement to planar exactness, not a new parity criterion. An older paper by Martini concerns exact polar projection relations of difference bodies but its full text was not verified in this study. Historical priority beyond the inspected material remains open.

## Limitations

The uniform direction is Euclidean angular measure, not cone measure or boundary arclength. The error norms are support-function \(L^2\) and Euclidean Hausdorff metrics, not affine-invariant distances. The precise endpoint law is restricted to these canonical regular polygons; no claim is made about arbitrary Radon planes, almost-Radon bodies, or all near-solutions of Petty's equation. Numerical tests do not establish an infinite-family identity. The primary historical risk is that a version of these elementary sector-integral formulas may have been recorded in older specialized Radon-plane literature not inspected in full. Independent mathematical validation has not been performed.

## References

1. Y. Zhang, *A solution to Petty's polar projection problem*, arXiv:2611.17926v1, 13 November 2026, https://arxiv.org/html/2611.17926v1 (full text inspected, especially Theorem 1.1 and Remark 3.1).
2. K. Mandal, D. Sain, K. Paul, *A complete characterization of polygonal Radon planes*, arXiv:1809.04760, https://arxiv.org/abs/1809.04760 (full text inspected, especially Theorem 2.8 and Remark 2.1); journal version *A Geometric Characterization of Polygonal Radon Planes*, Journal of Convex Analysis 26 (2019), 1113–1123, doi:10.68381/jca26061.
3. H. Martini, *Convex polytopes whose projection bodies and difference sets are polars*, Discrete & Computational Geometry 6 (1991), 83–91, doi:10.1007/BF02574676 (abstract assessed; complete text not inspected).
