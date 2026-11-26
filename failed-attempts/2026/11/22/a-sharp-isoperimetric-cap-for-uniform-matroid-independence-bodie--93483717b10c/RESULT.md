# A sharp isoperimetric cap for uniform-matroid independence bodies

## Finding
For each integer \(n\ge2\) and real \(0<t\le n\), let
\[
K_{n,t}=\left\{x\in[0,1]^n:\sum_{i=1}^{n}x_i\le t\right\}.
\]
Let \(F_n(t)\) and \(f_n(t)\) be the distribution function and density of the sum of \(n\) independent uniform random variables on \([0,1]\), with \(F_m(t)=0\) for \(t\le0\) and \(F_m(t)=1\) for \(t\ge m\). Denote the ordinary Euclidean \(n\)-volume and \((n-1)\)-dimensional boundary area of \(K_{n,t}\) by \(V_n(t)\) and \(S_n(t)\), respectively.

**Theorem.** For all these parameters,
\[
\boxed{\begin{aligned}
V_n(t)&=F_n(t),\\
S_n(t)&=n\bigl[F_{n-1}(t)+F_{n-1}(t-1)\bigr]+\sqrt n\,f_n(t)\\
      &=2nF_n(t)+(n-2t+\sqrt n)f_n(t).
\end{aligned}}
\tag{1}
\]
The scale-invariant Euclidean surface quotient \(Q_n(t)=S_n(t)/V_n(t)^{(n-1)/n}\) is constant for \(0<t\le1\), strictly decreases for \(1<t<t_n^*\), and strictly increases for \(t_n^*<t\le n\), where
\[
\boxed{t_n^*=\frac{n+\sqrt n}{2}.}\tag{2}
\]
Thus \(t_n^*\) is its unique global minimizer, and the exact sharp inequality along the family is
\[
\boxed{S_n(t)\ \ge\ 2n F_n(t_n^*)^{1/n}\,V_n(t)^{(n-1)/n},}\tag{3}
\]
with equality if and only if \(t=t_n^*\).

At every integer cap \(k\in\{1,\ldots,n\}\), this polytope is the independence polytope of the uniform matroid of rank \(k\). Its minimizing integer rank lies among \(\lfloor t_n^*\rfloor\) and \(\lceil t_n^*\rceil\), retaining only candidates in \(\{1,\ldots,n\}\); both candidate quotients are explicit finite binomial sums, and no assertion is made here about absence of ties between the two. As \(n\to\infty\), the best continuous and the best integer-cap quotients both satisfy
\[
\boxed{\min Q_n=2n+2\log\Phi(\sqrt3)+o(1)=2n-0.0850474214\ldots+o(1),}\tag{4}
\]
where \(\Phi\) is the standard normal distribution function. For every sequence of minimizing integer caps \(k_n\),
\[
\frac{2k_n-n}{\sqrt n}\longrightarrow1.
\]
The exact optimizer (2) coincides numerically and algebraically with the *upper contact threshold* of the already known John ellipsoid of the same body; this equality of parameters is a comparison of two distinct geometric optimizations, not an assertion that one theorem implies the other.

## Assumptions and scope
The ambient metric is the ordinary Euclidean metric on \(\mathbb R^n\); the surface area counts **all** boundary facets, including those lying on the original cube. Consequently this is not the relative isoperimetric problem inside the cube (where its own boundary would be excluded). The real cutoff ranges over \(0<t\le n\), so nonintegral cuts and the cube endpoint are covered. It is not an optimization over all convex bodies or all cuts of the cube. The normalizing exponent is precisely \((n-1)/n\), reflecting uniform volume rescaling. Standard B-spline conventions define \(f_n\) at integer knots by its continuous extension when available; the statement only uses limits at endpoints.

The explicit finite forms, for \(0<t<n\), are
\[
F_n(t)=\frac1{n!}\sum_{j=0}^{n}(-1)^j\binom nj(t-j)_+^n,\qquad
f_n(t)=\frac1{(n-1)!}\sum_{j=0}^{n}(-1)^j\binom nj(t-j)_+^{n-1},
\]
where \(u_+=\max(u,0)\), with the natural one-sided interpretation at the endpoints. Thus all asserted finite-dimensional values are explicit, not merely implicit integrals.

## Proof
**1. Exact area by independent facet classes.** Since the independent uniforms are uniform on the cube, \(V_n(t)=F_n(t)\). Each of the \(n\) lower-coordinate boundary facets \(x_i=0\) has area \(F_{n-1}(t)\); each upper-coordinate facet \(x_i=1\) has area \(F_{n-1}(t-1)\). The remaining rank facet \(\sum_i x_i=t\), clipped to the cube, has intrinsic Euclidean \((n-1)\)-measure \(\sqrt n\,f_n(t)\) by the coarea formula: the coordinate sum has gradient length \(\sqrt n\). Summing these areas proves the first expression for \(S_n(t)\), with degenerate facets counted as zero.

**2. A conditional-symmetry identity.** By exchangeability of the uniform coordinates, conditional on \(\sum_i U_i=t\), every coordinate has mean \(t/n\). Taking the infinitesimal density contribution with \(U_n\) at the lower or upper end of \([0,1]\), or equivalently integrating the derivative of \(u\mapsto u f_{n-1}(t-u)\), yields
\[
F_{n-1}(t)=F_n(t)+\frac{n-t}{n}f_n(t),\qquad
F_{n-1}(t-1)=F_n(t)-\frac{t}{n}f_n(t).
\tag{5}
\]
An elementary verification is to write \(f_n(t)=\int_0^1f_{n-1}(t-u)\,du\), integrate the derivative of \(u f_{n-1}(t-u)\), and use \(\int_0^1u f_{n-1}(t-u)\,du=(t/n)f_n(t)\). Substitution of (5) proves the second area expression in (1).

**3. Exact factorization of the isoperimetric derivative.** Write \(F=F_n(t)\), \(f=f_n(t)\), \(c=n-2t+\sqrt n\), and \(\alpha=(n-1)/n\). At each noninteger \(t\in(0,n)\), ordinary differentiation of \(S_n=2nF+cf\) gives
\[
\boxed{Q_n'(t)=\frac{c}{F^{\alpha+1}}\left(Ff'-\frac{n-1}{n}f^2\right).}\tag{6}
\]
Indeed the independent \(f\)-terms cancel because \(2n-2=2n\alpha\).

**4. The Brunn–Minkowski sign is strict exactly beyond the simplex interval.** For \(s,t>0\) and \(0<\lambda<1\), convexity of the cube and linearity of the rank inequality give
\[
(1-\lambda)K_{n,s}+\lambda K_{n,t}
\subseteq K_{n,(1-\lambda)s+\lambda t}.
\]
Brunn–Minkowski therefore makes \(H_n(t)=F_n(t)^{1/n}\) concave. At noninteger arguments,
\[
H_n''(t)=\frac{F_n(t)^{1/n-2}}{n}
\left(F_n(t)f_n'(t)-\frac{n-1}{n}f_n(t)^2\right)\le0.
\tag{7}
\]
For \(0<t\le1\) all bodies are homothetic simplices \(K_{n,t}=tK_{n,1}\), so \(H_n\) is linear and \(Q_n\) constant. In contrast, for distinct parameters whose interval meets \((1,n]\), the bodies cannot be homothetic: when \(t>1\) every coordinate projection is the full interval \([0,1]\), whereas for \(t\le1\) it is \([0,t]\); among distinct parameters both above one, every coordinate range is \([0,1]\), fixing any homothety factor at one and the translation at zero, while the bodies are still different. Thus the equality condition in Brunn–Minkowski gives *strict* concavity across any nontrivial interval reaching beyond one. The density is polynomial between integer knots, so (7) and strict concavity show that the bracket in (6) is nonpositive everywhere it is defined and cannot vanish throughout any nontrivial interval of \((1,n)\).

Since \(c=2(t_n^*-t)\), (6) shows that \(Q_n\) decreases strictly on \((1,t_n^*)\) and increases strictly on \((t_n^*,n)\); continuity joins the finitely many integer knots. Because \(n\ge2\) implies \(1<t_n^*<n\), the global minimum is unique. At \(t_n^*\), the density term in (1) vanishes, giving (3).

**5. Integer caps and asymptotics.** Strict monotonicity on each side forces the best integer cutoff to be one of the two integers adjacent to \(t_n^*\). The central limit theorem for bounded independent uniforms gives
\[
F_n\left(\frac{n+\sqrt n}{2}\right)\longrightarrow
\Phi\!\left(\frac{1/2}{\sqrt{1/12}}\right)=\Phi(\sqrt3).
\]
Consequently \(2nF_n(t_n^*)^{1/n}=2n+2\log\Phi(\sqrt3)+o(1)\). Both neighboring integer caps have the same limiting CDF by the central limit theorem; by (1), their density correction is \(O(n^{-1/2})\) because \(n-2k+\sqrt n=O(1)\), while their density is \(O(n^{-1/2})\) by the standard bounded-density local central limit theorem for uniform sums. This yields the same additive asymptotic for the minimizing integer cap, as well as the stated scaling of \(k_n\).

## Verification
A standalone independent computation `verify.py` evaluates exact rational B-spline and density identities (442 parameter cases), compares the predicted surface areas and volumes against independently constructed Euclidean convex hulls for 28 low-dimensional integer and noninteger cuts (dimensions two through five), and checks the unique critical-cap location numerically in 14 dimensions through 200. It reports `CAPPED_CUBE_SURFACE_PASS` if all checks succeed. These are finite diagnostics; the proof of the all-dimensional assertions is the preceding coarea, conditional-symmetry and Brunn–Minkowski argument, not a finite enumeration or a numerical scan. Reproduce from the same directory with `python verify.py`, using Python, NumPy, and SciPy.

## Relationship to prior work
Ferroni's first arXiv version (December 8, 2020) identifies the integer-cut bodies as uniform-matroid independence polytopes and studies their Ehrhart polynomials and half-open hypersimplex decompositions. The elementary truncated-cube volume expression is known and not claimed new. Earlier exact analysis of John ellipsoids of the **same real-cut body** established a second transition precisely at \((n+\sqrt n)/2\); the equality of numerical thresholds is notable but the earlier result optimizes *inscribed ellipsoid volume* and does not determine ordinary whole-boundary area or the unique minimum of its normalized area. A known circumball classification and a known Santaló polar-volume formula likewise concern the same family but different objectives. The new statement is the sharp full-dimensional Euclidean surface inequality (3) and its unique equality case, including the integer-rank consequence; the Brunn–Minkowski theorem and the central limit theorem are standard proof ingredients, not new claims.

## Limitations
The result depends on equal coordinate bounds and one equally weighted clipping halfspace, the fixed Euclidean metric, and the full boundary area. It does not establish the optimal clipping direction, handle arbitrary weighted knapsack cuts, or solve the relative isoperimetric problem in the cube. The independent integer-cap minimizer is localized to two adjacent choices but uniqueness of that integer choice is not asserted. Although targeted searches and close full-text comparisons found no directly covering theorem, mathematically equivalent unindexed literature remains a priority risk. No independent mathematical audit is claimed.

## References
1. Luis Ferroni, *Integer point enumeration on independence polytopes and half-open hypersimplices*, arXiv:2012.04711v1 (first public 2020-12-08), https://arxiv.org/abs/2012.04711.
2. *Three-phase John ellipsoid of a capped hypercube*, published research record (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-three-phase-john-ellipsoid-of-a-capped-hypercube--9b8726b32127.
3. *Exact enclosing spheres and contact-phase transitions of fractionally capped cubes*, published research record (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-enclosing-spheres-and-contact-phase-transitions-of-fractio--4ccf5ee9c9a2.
4. *Santaló dual volumes of uniform-matroid independence polytopes and exponential stability of the near-cube center*, published research record (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-santal-dual-volumes-of-uniform-matroid-independence-polytopes-an--d0ee7a0a8aa0.
5. Rolf Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, 2nd expanded edition, Cambridge University Press (2014); standard Brunn–Minkowski equality criteria.
