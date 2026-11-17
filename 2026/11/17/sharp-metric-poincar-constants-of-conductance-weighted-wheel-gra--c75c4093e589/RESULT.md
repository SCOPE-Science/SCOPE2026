# Sharp metric Poincaré constants of conductance-weighted wheel graphs

## Finding
For every integer \(r\ge4\) and every \(A,B>0\), let \(W_r=K_1\vee C_r\) be the wheel with \(r\) rim vertices and a hub. Give each spoke conductance \(A\) and each rim edge conductance \(B\). For any map \(f\) into any metric space, define the exponent-one Poincaré ratio as the mean target distance over **distinct unordered vertex pairs**, divided by the conductance-weighted mean target distance over edges. The denominator uses total conductance \(r(A+B)\).

The sharp ratio for **every** nontrivial metric target, for real-valued maps, and for all real \(L^1\) targets is the same number:
\[
\boxed{\Gamma_r(A,B)=\frac{2(A+B)}{r+1}\max\left\{\frac1A,\ \max_{1\le s<r}\frac{s(r+1-s)}{As+2B}\right\}.}
\]
The value is attained by an indicator of a set containing exactly \(s\) consecutive rim vertices (and not the hub) whenever that \(s\) maximizes the inner expression; the first alternative is attained by the indicator of the entire rim. Up to complements, **every nontrivial optimal cut** is of one of these types. Every real \(L^1\)-valued equality map has almost every nonzero level-set cut in this optimal family, in the standard cut representation of the \(L^1\) distance.

There is an exact full-rim transition:
\[
\text{the full-rim cut is optimal}\quad\Longleftrightarrow\quad
\frac BA\ge \frac12\left\lfloor\frac{r^2}{4}\right\rfloor.
\]
For proper arcs, the increment of their unscaled ratio changes sign according to
\[
\operatorname{sgn}\left(\frac{(s+1)(r-s)}{A(s+1)+2B}-\frac{s(r+1-s)}{As+2B}\right)
=\operatorname{sgn}\bigl(2B(r-2s)-As(s+1)\bigr),
\]
so the maximizing arc sizes form an explicit integer staircase, including all possible ties.

In particular, for \(A=B=1\), the common constant is
\[
\Gamma_r(1,1)=\frac4{r+1}\max_{1\le s<r}\frac{s(r+1-s)}{s+2}
=4-8\sqrt{2/r}+O(r^{-1})\quad(r\to\infty).
\]
This shows that arbitrarily large weighted wheels have a sharp exponent-one Poincaré constant which does **not** depend on the target metric geometry, despite target dependence for other familiar graph families.

## Assumptions and scope
All vertex sets and graphs are finite, all conductances are strictly positive, and target distances may vanish between distinct vertices. We take the supremum over maps with positive weighted edge-distance mean. For a metric target \((M,d)\), write
\[
P(f)=\binom{r+1}{2}^{-1}\sum_{\{u,v\}}d(f(u),f(v)),\qquad
E_{A,B}(f)=\frac{A\sum_{\mathrm{spokes}}d(f(u),f(v))+B\sum_{\mathrm{rim\ edges}}d(f(u),f(v))}{r(A+B)},
\]
and \(\Gamma_r(A,B)=\sup_{f:E_{A,B}(f)>0}P(f)/E_{A,B}(f)\). Any finite metric embeds isometrically into a Banach space \(\ell_\infty\), so taking arbitrary metric targets is unambiguous. The source paper's convention using all ordered pairs including the diagonal differs by the factor \(r/(r+1)\), and is not silently interchanged with the convention above.

## Proof
**1. Cut extremizers.** By taking complements, write any nontrivial cut with the hub outside and \(s\in\{1,\ldots,r\}\) rim vertices inside. For \(s=r\), the crossing-edge conductance is \(Ar\) and the number of separated unordered pairs is \(r\). For \(1\le s<r\), its number of rim crossing edges is at least two, with equality if and only if the selected rim vertices form a single consecutive arc. The cut ratio is therefore at most
\[
\frac{2(A+B)}{r+1}\frac{s(r+1-s)}{As+2B},
\]
with equality precisely for an arc. The full-rim cut contributes \(2(A+B)/(A(r+1))\). In a real \(L^1\) space, distances are integrals of scalar absolute differences, and scalar differences are integrals of threshold cuts. Fubini's theorem writes both \(P\) and \(E_{A,B}\) as nonnegative integrals of corresponding cut quantities. Thus the \(L^1\) ratio cannot exceed the maximal cut ratio; an optimal indicator attains it. The same argument gives the stated level-cut equality criterion, since every nonoptimal cut incurs a strictly positive deficit.

**2. Universal metric bound.** Let \(d_{uv}\) be an arbitrary metric or pseudometric induced by the map. Average this array over the dihedral symmetry group of the rim. The numerator and weighted edge denominator are both invariant under this averaging. Denote averaged hub-to-rim distances by \(a\ge0\), averaged adjacent-rim distances by \(b\ge0\), and distance at cyclic separation \(k\) by \(c_k\), with \(c_k=c_{r-k}\). Connectedness excludes \(a=0\) for a nonconstant averaged metric, because the triangle inequality gives \(b\le2a\). In particular \(0\le t=b/a\le2\). From the two-spoke path and each shorter rim path,
\[
c_k\le \min\{2a,\min(k,r-k)b\},\qquad 2\le k\le r-2.
\]
There are \(r\) hub-rim pairs, \(r\) rim edges, and the remaining rim pairs contribute \((r/2)\sum_{k=2}^{r-2}c_k\) to the unordered-pair distance sum. Therefore
\[
\frac{P(f)}{E_{A,B}(f)}
\le\frac{2(A+B)}{r+1}\,H_r(t),\qquad
H_r(t)=\frac{1+t+\frac12\sum_{k=2}^{r-2}\min\{2,\min(k,r-k)t\}}{A+Bt}.
\]
On \([0,2]\), this continuous function is a ratio of affine functions on every interval separated by the breakpoints \(t=2/s\), \(1\le s\le\lfloor r/2\rfloor\), along with the endpoint \(t=0\). Its maximum is attained at a breakpoint, because an affine-over-positive-affine function is monotone or constant on each interval.

**3. Every metric-upper-bound breakpoint is a cut metric.** The endpoint \(t=0\) is realized by the full-rim cut. Fix \(1\le s\le\lfloor r/2\rfloor\). Average the cut pseudometrics of all \(r\) rotations of an arc of \(s\) consecutive rim vertices. The resulting distances are
\[
a=\frac sr,\qquad b=\frac2r,\qquad c_k=\frac{2\min\{s,k,r-k\}}r.
\]
They satisfy \(t=2/s\) and \(c_k=\min\{2a,\min(k,r-k)b\}\) at every separation. Hence the upper bound at that breakpoint is attained by a real \(L^1\) metric (a finite convex combination of cuts). Since each individual cut ratio is bounded by the largest cut ratio in Step 1, the universal metric bound equals that cut optimum. This proves the displayed equality of all three target classes.

**4. Phase laws and asymptotics.** Comparing an arc with the full-rim cut gives
\[
\frac{s(r+1-s)}{As+2B}\ge\frac1A\quad\Longleftrightarrow\quad As(r-s)\ge2B.
\]
Maximizing \(s(r-s)\) over integer \(1\le s<r\) gives \(\lfloor r^2/4\rfloor\) and the stated transition. Direct cross multiplication gives the displayed increment sign. In the unweighted case the continuous extension of the arc score is \(r+3-s-2(r+3)/(s+2)\), with unique real maximizer \(s_*=\sqrt{2(r+3)}-2\); the optimum over integers differs from its continuous maximum by \(O(r^{-1/2})\) before multiplication by \(4/(r+1)\). This yields \(\Gamma_r(1,1)=4-8\sqrt{2/r}+O(r^{-1})\). The full-rim cut cannot dominate for unweighted \(r\ge4\), since the arc \(s=1\) is at least as good and a longer arc is better.

## Verification
The attached `check_wheels.py` uses exact rational arithmetic. It independently enumerates all nontrivial hub-outside cuts for rim sizes \(4\le r\le13\) and six conductance pairs, checks the metric breakpoint maximum against the claimed cut formula through \(r=159\), and verifies the rotated-arc distance identities through \(r=34\). Its output is `WEIGHTED_WHEEL_EXACT_OK 99340 exact checks; r=4..159; all cuts r=4..13`. Finite checks are supporting diagnostics, not a proof for arbitrary \(r,A,B\); the proof is Steps 1–4 above.

## Relationship to prior work
Polavarapu [1] derives quantitative nonlinear spectral-gap bounds for regular expanders with Banach targets of finite cotype, rather than exact exponent-one invariants of nonregular conductance-weighted wheels. The classical nonlinear spectral-gap formalism of Mendel–Naor [2] motivates distinguishing arbitrary metric targets from real \(L^1\) and scalar ones. Existing analyses of wheel distance matrices [3] and of wheel Lipschitz variance or cut/cycle projections involve different quadratic or operator-norm objectives: neither determines this exponent-one mean-distance/mean-edge-distance quotient with unrestricted metric targets. The separate target-specific results for complete bipartite and crown graphs illustrate that target-independence is not a formal consequence of the definition.

## Limitations
Only uniform conductance within each of the two wheel-edge orbits is covered; independently varying edge weights, other join graphs, and exponents greater than one are not covered. The cut equality class is complete, but a classification of **all** non-scalar metric equality maps is not asserted. No bibliographic search can establish absolute priority: an equivalent earlier all-pairs demand flow/cut formulation on wheels remains a specific residual risk. The theorem is proved in this note but has not received an independent mathematical audit.

## References
[1] A. R. Polavarapu, *Linear Cotype Bounds for Nonlinear Spectral Gaps of Scalar Expanders*, arXiv:2611.05649v1 (first public 2026-11-03), https://arxiv.org/abs/2611.05649.

[2] M. Mendel and A. Naor, *Nonlinear spectral calculus and super-expanders*, Publications mathématiques de l'IHÉS 119 (2014), https://doi.org/10.1007/s10240-013-0053-2.

[3] R. Balaji, R. B. Bapat, S. Goel, *An inverse formula for the distance matrix of a wheel graph with an even number of vertices*, Linear Algebra and its Applications 610 (2021), 274–292, https://doi.org/10.1016/j.laa.2020.10.003.
