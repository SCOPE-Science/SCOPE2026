# The zero-exponent Dowker dichotomy for regular even polygons and logarithmic honeycomb tilings

## Finding

Let \(P_k\) be the regular Euclidean \(2k\)-gon circumscribed about the unit disk, with integer \(k\ge2\). For every integer \(n\ge3\), let \(A_k(n)\) be the smallest Euclidean area of a convex polygon with at most \(n\) sides containing \(P_k\). For \(0<\alpha<\infty\), call \(P_k\) *weakly \(\alpha\)-Dowker* if, for all integers \(3\le m<6<n\),
\[
\frac{n-6}{n-m}A_k(m)^\alpha+\frac{6-m}{n-m}A_k(n)^\alpha\ge A_k(6)^\alpha.
\]
For \(\alpha=0\), interpret this as the corresponding weighted logarithmic inequality.

**Complete endpoint and exponent classification:**

1. If \(k\notin\{4,5,7\}\), then \(P_k\) is weakly log-Dowker and weakly \(\alpha\)-Dowker for **every** \(\alpha>0\).
2. If \(k\in\{4,5,7\}\), then \(P_k\) fails the weak log-Dowker inequality and every weak \(\alpha\)-Dowker inequality with \(0<\alpha<1\); it satisfies the weak \(\alpha\)-Dowker inequality for every \(\alpha\ge1\). The strict failure is already witnessed at \((m,n)=(5,7)\).

Consequently, for every regular \(2k\)-gonal unit ball with \(k\notin\{4,5,7\}\), every normal convex tiling of the corresponding normed plane by unit-area cells has lower average **logarithmic** Minkowski perimeter at least that of an appropriate hexagonal translation tiling. The corresponding property for the three exceptional normed planes is **not** decided by this result; failure of a sufficient Dowker condition is not failure of the honeycomb assertion.

## Assumptions and scope

All polygons are nondegenerate planar Euclidean convex polygons, and an \(n\)-gon may be understood as having at most \(n\) sides. For \(n\ge2k\), \(A_k(n)=\operatorname{area}(P_k)=2k\tan(\pi/(2k))\). The results for tilings concern normal, convex plane tilings whose cells all have unit Lebesgue area, using the unit-ball norm for perimeter. Only the *lower average* logarithmic perimeter in the usual large-ball exhaustion is asserted; no assertion is made for arbitrary nonconvex or nonnormal tilings.

We use the proved minimum-circumscribing-polygon formulas of Lángi and Wang (arXiv:2406.10622, Lemma 3.7; published version Lemma 3.2), as well as their theorem transferring weak \(0\)-Dowker to log-honeycomb. These are prior theorems, not new contributions.

## Proof

**1. Exact prior area formulas.** For \(4\le n\le2k\), put \(2k=nq+r\), \(0\le r<n\). The published exact formula is
\[
A_k(n)=(n-r)\tan\frac{q\pi}{2k}+r\tan\frac{(q+1)\pi}{2k}.
\]
For \(n=3\), the same source proves, with \(2k=3q+r\),
\[
A_k(3)=\begin{cases}
3\tan(\pi/3),&r=0,\\
\frac2{\cos^2(\pi/(2k))}\bigl((3-r)\sin(q\pi/k)+r\sin((q+1)\pi/k)\bigr),&r=1,2.
\end{cases}
\]
These formulas also supply all finite cases certified below.

**2. A universal strictly log-convex disk comparator.** For real \(x>2\), set \(B(x)=x\tan(\pi/x)\). The Euler product for sine gives the absolutely convergent expansion
\[
\log B(x)=\log\pi+\sum_{j=1}^{\infty}\frac{(4^j-2)\zeta(2j)}{j\,x^{2j}}.
\]
Every summand after the constant is strictly convex in \(x>2\); hence \(\log B(x)\) is strictly convex. For integers \(3\le m<6<n\), a convex-chord comparison at \(6\) yields
\[
\frac{n-6}{n-m}\log B(m)+\frac{6-m}{n-m}\log B(n)
\ge\tfrac12\log(B(5)B(7)).
\]
Since the unit disk is contained in \(P_k\), \(A_k(j)\ge B(j)\) for every \(j\ge3\). Thus it suffices to prove \(A_k(6)^2\le B(5)B(7)\).

**3. The entire infinite tail \(k\ge9\).** Write \(2k=6q+r\), where \(r\in\{0,2,4\}\) and \(q\ge3\). The area formula gives
\[
A_k(6)=(6-r)\tan\left(\tfrac\pi6-\tfrac{r\delta}{6}\right)+r\tan\left(\tfrac\pi6+\tfrac{(6-r)\delta}{6}\right),
\quad \delta=\frac\pi{6q+r}.
\]
For fixed \(r\), differentiation with respect to \(\delta\) gives
\[
\frac{r(6-r)}6\left[\sec^2\left(\tfrac\pi6+\tfrac{(6-r)\delta}6\right)-\sec^2\left(\tfrac\pi6-\tfrac{r\delta}6\right)\right]\ge0.
\]
Therefore the expression is nonincreasing in \(q\). It is enough to check \(k=9,10,11\). In all three cases, an exact-rational interval certificate verifies
\[
A_k(6)^2<B(5)B(7).
\]
For orientation, the three values of \(A_k(6)\) are approximately \(3.46410161514\), \(3.49118685399\), \(3.48401330448\), while \(\sqrt{B(5)B(7)}\approx3.49942215716\). The strict comparison, unlike these decimals, is certified with rational intervals by the accompanying executable checker.

**4. The remaining polygons.** For \(k=2,3\), \(A_k(j)=A_k(6)\) for \(j\ge6\), and \(A_k(m)\ge A_k(6)\) for \(m<6\). Thus the logarithmic inequality holds. For \(k=6\) and \(k=8\), the exact-rational checker proves respectively all \(18\) and \(30\) required integer-power inequalities
\[
A_k(m)^{n-6}A_k(n)^{6-m}>A_k(6)^{n-m},
\quad m\in\{3,4,5\},\quad7\le n\le2k.
\]
For \(n>2k\), \(A_k(n)\) is constant; the interpolation chord at \(6\), with its left endpoint fixed, is then nondecreasing in \(n\), since \(A_k(m)>A_k(2k)\). This exhausts every \(n\). The certificate uses only exact fractions, an alternating-series enclosure for \(\pi\), and Taylor remainder bounds for sine and cosine; it is not a numerical grid experiment.

**5. Sharp exceptional obstruction.** For each \(k\in\{4,5,7\}\), the exact formula from step 1 shows
\[
A_k(5)>A_k(6)>A_k(7),\qquad A_k(5)+A_k(7)=2A_k(6).
\]
Strict concavity of \(\log x\) and of \(x^\alpha\) for \(0<\alpha<1\) reverses the required weak inequality for \((m,n)=(5,7)\). Conversely, Dowker's classical theorem says that \(n\mapsto A_k(n)\) is convex. Because \(x\mapsto x^\alpha\) is increasing and convex for \(\alpha\ge1\), the weak \(\alpha\)-Dowker condition then holds for every \(k\). On the nonexceptional branch, weighted AM–GM applied to the weak logarithmic inequality proves all positive exponents. This completes the sharp classification.

**6. The tiling consequence.** The isoperimetrix of a regular even-sided polygonal norm is a rotated, scaled regular polygon of the same order. Lángi and Wang's published weak-Dowker-to-honeycomb theorem applies at exponent \(\alpha=0\) and gives the asserted lower average logarithmic-perimeter inequality for every normal convex unit-area tiling. It makes no assertion for the three exceptional orders.

## Verification

Run `python3 verification/check.py` using the Python standard library. It carries out \(18+30\) exhaustive finite pair comparisons for \(k=6,8\), three strict large-order bounds for \(k=9,10,11\), and the required exceptional-order strict comparisons. Sine, cosine and \(\pi\) are enclosed by explicit exact rational intervals. Every crucial check is a strict comparison of rational endpoints, not floating-point evaluation. Its expected final line begins with `RATIONAL_INTERVAL_CERTIFICATE_PASSED`. The infinite-order reduction and logarithmic convexity are proved analytically above, not inferred from code.

## Relationship to prior work

Lángi and Wang's original 2024 preprint, and its 2026 published version, already contain the exact formulas for \(A_k(n)\), weak \(\frac12\)-Dowker classification, the general tiling transfer theorem, and the three exceptional polygon orders. The new claim does not appropriate those statements. It strengthens the sufficient inequality from the square-root exponent to the **logarithmic endpoint**, gives the **complete all-exponent weak-Dowker phase diagram**, and thereby establishes the **log-honeycomb property** on the nonexceptional family. The earlier proof's square-root comparator does not imply the logarithmic inequality, because the latter is strictly stronger. The logarithmic disk-chord barrier, its uniform high-order check and the exhaustive small-order certificates supply the missing comparison.

The source's observation that the *full* \(\alpha\)-Dowker convexity fails for regular polygons with at least eight sides and \(\alpha<1\) is distinct from the present *weak* convexity about six sides. The current result concerns that weak property and its consequence for tilings.

## Limitations

The negative statements for the regular octagon, decagon, and tetradecagon concern failure of a sufficient *weak Dowker inequality* at exponents below one. They do not disprove the honeycomb conjecture for those normed planes. Nothing is claimed for nonregular polygonal norms or for general convex bodies. The mathematical proof is self-reviewed, not independently audited; historical priority is provisional, with a residual risk of a differently indexed endpoint result.

## References

1. Z. Lángi and S. Wang, *The Honeycomb Conjecture in normed planes and an alpha-convex variant of a theorem of Dowker*, arXiv:2406.10622, initially public June 15, 2024, https://arxiv.org/abs/2406.10622 . In particular Definitions 1.7–1.8, Theorem 1.9, Lemma 3.7 and Theorem 3.3 in the preprint.
2. Z. Lángi and S. Wang, same work, *International Mathematics Research Notices* 2026(1), rnaf372, https://doi.org/10.1093/imrn/rnaf372 . In particular Definition 1.4, Theorem 1.3, Lemma 3.2, Theorem 3.2. Journal date is not substituted for first public date.
3. C. H. Dowker, *On minimum circumscribed polygons*, 1944. Classical convexity theorem as explicitly restated in [1,2].
