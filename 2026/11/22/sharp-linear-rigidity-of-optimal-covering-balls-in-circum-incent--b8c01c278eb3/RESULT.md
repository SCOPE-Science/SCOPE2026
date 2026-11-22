# Sharp linear rigidity of optimal covering balls in circum-incenter simplex unions

## Finding
Let \(n\geq 3\) and let \(\Delta=\operatorname{conv}\{u_0,\ldots,u_n\}\subset\mathbb R^n\) be a nondegenerate simplex whose vertices lie on the unit sphere and whose incenter is the origin. Write \(h>0\) for its inradius and \(n_j\) for the outward unit normal to the facet opposite \(u_j\). Define
\[
\rho=\frac{h}{\sqrt{1-h^2}},\qquad c_j=\frac{n_j}{\sqrt{1-h^2}},\qquad M=\frac1{2\sqrt{1-h^2}},\qquad
S_\Delta=\overline B(0,\rho)\cup\bigcup_{j=0}^n\overline B(c_j,1).
\]
The exact radius \(M\) of the largest ball contained in \(S_\Delta\) and containing the origin was established by Nour [1]. The following *complete equality classification and sharp quantitative stability* hold:

1. The only radius-\(M\) balls contained in \(S_\Delta\) and containing the origin are precisely the \(n+1\) distinct balls \(\overline B(Mn_j,M)\), one per facet.
2. Put \(N=\{n_0,\ldots,n_n\}\), \(g(w)=\max_{0\le i\le n}\langle w,u_i\rangle\) for \(\|w\|=1\), and
\[
\kappa_\Delta=\inf_{\substack{\|w\|=1\\w\notin N}}
\frac{g(w)-h}{\operatorname{dist}(w,N)}.
\]
Then \(\kappa_\Delta>0\). For every
\[
0\le\varepsilon\le \varepsilon_0:=\frac{M(1-4h^2)}4
\]
and every closed Euclidean ball \(\overline B(z,T)\subset S_\Delta\) containing the origin and having \(T\ge M-\varepsilon\),
\[
\boxed{\operatorname{dist}(z,MN)\le\left(\frac2{1-4h^2}+\frac1{h\kappa_\Delta}\right)\varepsilon.}
\]
3. The error exponent one is optimal: for each \(j\), there are admissible balls with \(T\uparrow M\) whose center distance from \(MN\) is exactly \(M-T\). In particular, no exponent greater than one can replace the displayed linear dependence with a constant independent of the near-optimal ball.

Here \(MN=\{Mn_j:0\le j\le n\}\). This is a rigidity statement for **all** contained candidate balls, not merely those formed by two-ball interpolation. The constant depends on the fixed simplex and is effective from its finite vertex and facet data.

## Assumptions and scope
The simplex is full dimensional, \(\|u_i\|=1\), and \(0\) is both its circumcenter and incenter. Thus \(\Delta=\bigcap_j\{x:\langle x,n_j\rangle\le h\}\) with \(\langle u_i,n_j\rangle=h\) for \(i\ne j\). The cited Lemma 2.1 of [1] gives \(h\le1/n\), so \(0<h<1/2\). Every ball is closed and Euclidean. An admissible ball must be contained in the *specified union* \(S_\Delta\) and must contain \(0\); no assertion is made about balls not containing \(0\), or arbitrary unions of balls.

## Proof
**Step 1: the spherical support gap has a sharp linear error bound.** Since \(\overline B(0,h)\subset\Delta\), its support function satisfies \(g(w)\ge h\) on the unit sphere. Equality is possible only when the supporting plane of \(\Delta\) is tangent to its insphere: each tangency point lies in the relative interior of a unique facet, so \(g(w)=h\) exactly at \(w\in N\). Fix a facet \(F_j\). Its point \(hn_j\) of insphere contact is in \(\operatorname{relint}F_j\). Hence the tangential convex hull of \(\{u_i-hn_j:i\ne j\}\) contains \(0\) in its relative interior, and
\[
k_j:=\min_{\substack{\|v\|=1\\v\perp n_j}}\max_{i\ne j}\langle v,u_i-hn_j\rangle>0.
\]
For a unit vector \(w=\cos\theta\,n_j+\sin\theta\,v\), \(v\perp n_j\), with small \(\theta\ge0\),
\[
g(w)-h\ge h(\cos\theta-1)+k_j\sin\theta\ge\frac{k_j}{4}\theta
\ge\frac{k_j}{4}\|w-n_j\|,
\]
whenever \(\theta\le \min\{1,k_j/(2h)\}\); we used \(\sin\theta\ge\theta/2\), \(1-\cos\theta\le\theta^2/2\), and \(\|w-n_j\|\le\theta\). Outside the union of sufficiently small neighborhoods of the finitely many facet normals, \(g(w)-h\) has a strictly positive minimum by compactness. Therefore \(\kappa_\Delta>0\) and
\[
g(w)\ge h+\kappa_\Delta\operatorname{dist}(w,N) \quad (\|w\|=1).
\tag{1}
\]

**Step 2: universal candidate-ball inequalities.** From [1, Lemma 2.2 and Theorem 2.3], each \(p_i=\rho u_i\) lies on \(\partial S_\Delta\); additionally \(S_\Delta\) contains the \(n+1\) balls \(\overline B(c_j/2,\|c_j\|/2)=\overline B(Mn_j,M)\). For any admissible \(\overline B(z,T)\), write \(t=\|z\|\le T\). Every \(p_i\) lies outside its open interior, so
\[
T^2\le\rho^2+t^2-2\rho\max_i\langle z,u_i\rangle.
\tag{2}
\]
If \(t>0\), write \(w=z/t\) and \(\phi(w)=g(w)-h\ge0\). Then
\[
T^2\le f(t)-2\rho t\phi(w),\qquad f(t)=\rho^2+t^2-2\rho ht.
\tag{3}
\]
Using \(t\le T\) in (3) gives \(2\rho ht\le\rho^2\), hence \(t\le M=\rho/(2h)\). On \([0,M]\), \(f\) is convex, \(f(M)=M^2\), and \(f(0)=\rho^2<M^2\) (because \(h<1/2\)), hence \(f(t)\le M^2\). Thus \(T\le M\), independently reproducing the upper bound needed from [1].

**Step 3: equality.** If \(T=M\), (3) forces \(f(t)=M^2\) and \(\phi(w)=0\). As \(f(0)<M^2\) and \(f\) is strictly below \(M^2\) on \([0,M)\), we obtain \(t=M\), \(w\in N\). Therefore \(z=Mn_j\) for some \(j\). Each such ball is admissible by the cited two-ball identity, so the list is complete. The same conclusion follows without the notation \(w\) when \(t=0\): there \(T\le\rho<M\).

**Step 4: linear stability.** For any admissible ball with \(T\ge M-\varepsilon\), \(0\le\varepsilon\le\varepsilon_0\), let \(d=M^2-T^2\le2M\varepsilon\). From (3),
\[
(M-t)(M+t-2\rho h)=M^2-f(t)\le d.
\]
Since \(\rho=2hM\), \(M+t-2\rho h\ge M(1-4h^2)>0\), giving
\[
0\le M-t\le\frac{2\varepsilon}{1-4h^2}\le\frac M2.
\tag{4}
\]
Thus \(t\ge M/2>0\). Combining (3) with \(f(t)\le M^2\),
\[
0\le\phi(w)\le\frac{d}{2\rho t}\le\frac{2\varepsilon}{\rho}.
\]
By (1), \(\operatorname{dist}(w,N)\le2\varepsilon/(\rho\kappa_\Delta)\). Taking the nearest normal and using (4),
\[
\operatorname{dist}(z,MN)\le (M-t)+M\operatorname{dist}(w,N)
\le\left(\frac2{1-4h^2}+\frac{2M}{\rho\kappa_\Delta}\right)\varepsilon.
\]
The identity \(2M/\rho=1/h\) gives the claimed constant.

**Step 5: optimality of exponent.** The ball \(\beta_j=\overline B(Mn_j,M)\) contains \(0\); convexity gives \((1-s)\beta_j\subseteq\beta_j\subseteq S_\Delta\) for \(0<s<1\). It has center \((1-s)Mn_j\), radius \((1-s)M\), and contains \(0\). Since distinct facet normals are separated, for all sufficiently small \(s\), its nearest member of \(MN\) is \(Mn_j\), so
\[
\operatorname{dist}((1-s)Mn_j,MN)=sM=M-(1-s)M.
\]
This rules out every improvement to an exponent strictly exceeding one. \(\square\)

## Verification
The inequalities are analytic and apply to every permitted dimension and simplex. The accompanying `check_geometry.py` independently reproduces the tangent data of an explicit nonregular tetrahedron in [1], the strict gap \(h<1/2\), and the homothetic sharpness construction. It also numerically checks the positive support gap in a finite grid of sampled directions. The grid is not used to prove the global infimum is positive; that follows from Step 1. Reproduce with `python3 check_geometry.py` (standard library only).

## Relationship to prior work
Nour [1, Theorem 2.3] establishes the exact covering radius \(M\) for this union and displays the \(n+1\) achieving balls. The new statement classifies *every* optimizer and establishes a quantitatively sharp global-to-local error bound on centers of all near-optimal balls. Its proof makes explicit the strict support-gap property of a circumscribed simplex, which is absent from the radius-only theorem. The 2011 union-of-balls result [2] concerns universal existence of contained balls of fixed radius, rather than optimizer classification in this finite-ball construction. Generic convex error-bound theory [3] motivates linear error bounds but does not supply this particular geometric equality classification or the exhibited sharpness family.

## Limitations
This is a fixed-simplex statement: the stability constant may deteriorate for degenerating simplices, and no uniform bound over all simplices is claimed. The result concerns covering balls containing the origin, not all maximal inscribed balls of the set. The strict radius bound and construction of candidate optimal balls are from [1], not rediscovered here. The supporting-facet equality classification is short; the principal incremental content is the sharp quantitative linear stability of unrestricted near-optimizers. Historical-priority comparisons cannot exclude every unpublished or unindexed analogue. Independent validation has not been performed.

## References
[1] Chadi Nour, *A counterexample to the strong version of the union of uniform closed balls conjecture in dimensions three and higher*, arXiv:2611.14181v1 (first public 2026-11-10), https://arxiv.org/html/2611.14181v1. Sections 2--3, especially Theorem 2.3 and equations (2.1)--(2.5).

[2] C. Nour, R. J. Stern, J. Takche, *Validity of the Union of Uniform Closed Balls Conjecture*, J. Convex Anal. 18 (2011), 589--600, https://journalofconvexanalysis.com/articles/jca18037/.

[3] H. V. Ngai, A. Kruger, M. Théra, *Stability of Error Bounds for Semi-infinite Convex Constraint Systems*, SIAM J. Optim. 20 (2010), 2080--2096, https://doi.org/10.1137/090767819.
