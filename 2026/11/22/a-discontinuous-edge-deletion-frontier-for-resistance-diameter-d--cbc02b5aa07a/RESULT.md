# A discontinuous edge-deletion frontier for resistance-diameter design on priced cycles

## Finding

Let \(m\ge2\), and consider a simple undirected cycle on the labeled vertices \(0,1,\ldots,m\). Each consecutive edge \(\{i-1,i\}\) has independently selected conductance \(a_i\ge0\) at unit price. The closing edge \(\{0,m\}\) has independently selected conductance \(x\ge0\) at price \(c>0\). Fix budget \(B>0\), impose \(\sum_{i=1}^m a_i+cx\le B\), and minimize the resistance diameter \(\Delta=\max_{u<v}R_{uv}\). A disconnected design is assigned \(\Delta=+\infty\).

**Theorem (sharp price transition and complete critical set).** The closing-edge price threshold is \(c_*=m^2\). When \(c>m^2\), the unique optimal design has
\[
x=0,\quad a_i=B/m\ (1\le i\le m),\quad\Delta_*=m^2/B.\]
When \(c=m^2\), every global optimum, and no other design, belongs to the closed line segment
\[
0\le x\le\frac{B}{m(2m-1)},\qquad a_1=\cdots=a_m=\frac{B-m^2x}{m},\qquad\Delta_*=\frac{m^2}{B}.
\]
When \(0<c<m^2\), the optimal resistance diameter is strictly less than \(m^2/B\), and every optimal design has \(x>0\). There is moreover a **sharp nonzero optimizer jump** at the threshold: for any sequence \(c_k\uparrow m^2\) and any choices of corresponding global minimizers, their closing conductances tend to \(B/[m(2m-1)]\), and every ordinary conductance tends to \(B(m-1)/[m(2m-1)]\). For every \(c>m^2\), in contrast, the unique optimum has closing conductance zero. No uniqueness or explicit optimum below threshold is asserted.

For the four-vertex cycle, the cutoff is \(c=9\), and the critical closing-edge interval is \(0\le x\le B/15\). The approach from smaller prices has limiting conductance tuple \((a_1,a_2,a_3,x)=(2B/15,2B/15,2B/15,B/15)\), but from larger prices the optimizer is \((B/3,B/3,B/3,0)\).

## Assumptions and scope

The network is exactly the \((m+1)\)-cycle for an integer \(m\ge2\). All conductances are real nonnegative independent decision variables, all prices are positive, and there are no individual rate caps. Effective resistance between nodes is the voltage difference under unit injected and withdrawn current, equivalently a quadratic form of the weighted Laplacian pseudoinverse. Resistances are homogeneous of degree minus one under positive common conductance scaling. A zero edge is allowed if the remaining positive-support network is connected. The largest resistance is taken over all unordered distinct vertex pairs, including the two endpoints of the priced closing edge.

## Proof

**1. An endpoint dual certificate.** Let \(s=\sum_i a_i\). If the path edges are all positive, their series resistance is \(H=\sum_i a_i^{-1}\), and the effective resistance between vertices \(0\) and \(m\) is
\[
R_{0m}=\left(x+H^{-1}\right)^{-1}.
\]
Cauchy--Schwarz gives \(H\ge m^2/s\), with equality if and only if all \(a_i\) are equal. Thus, with the convention \(H^{-1}=0\) when any ordinary edge vanishes,
\[
\Delta\ge R_{0m}\ge\frac{m^2}{s+m^2x}\ge\frac{m^2}{B+(m^2-c)x}.\tag{1}
\]
The same inequality holds for all connected designs with missing path edges: if an ordinary edge vanishes, the only surviving endpoint route is the closing edge, and the formula follows by the stipulated convention. When \(c\ge m^2\), inequality (1) proves \(\Delta\ge m^2/B\). The path with \(x=0\) and \(a_i=B/m\) attains this lower bound, since its largest path resistance is the endpoint resistance \(m^2/B\). For \(c>m^2\), equality in (1) forces \(x=0\), budget saturation, and equality in Cauchy--Schwarz, so every ordinary conductance is \(B/m\): unrestricted uniqueness is proved.

**2. The complete critical face.** Suppose \(c=m^2\) and \(\Delta=m^2/B\). Equality in (1) forces the budget to be tight and all ordinary conductances equal, say \(a_i=y=(B-m^2x)/m\). A zero ordinary conductance would leave a degenerate endpoint equality and cannot attain the full bound at positive budget: directly, at \(x>0\) with an ordinary edge zero, \(R_{0m}=1/x\) and equality requires \(m^2x=B\), making every ordinary weight zero and disconnecting interior vertices for \(m\ge2\). Hence \(y>0\).

For a pair of vertices separated by \(k\) consecutive ordinary edges, \(1\le k\le m\), its two series routes have resistances \(k/y\) and \((m-k)/y+1/x\). With \(t=x/y\), the parallel combination simplifies to
\[
R_k=\frac{k[1+(m-k)t]}{y(1+mt)},\qquad R_m=\frac{m}{y(1+mt)}=\frac{m^2}{B}.
\]
The formulas extend by continuity to \(x=0\). The condition \(R_k\le R_m\) for every \(k<m\) is equivalent to
\[
(m-k)(kt-1)\le0\quad (1\le k<m),\qquad\text{i.e.}\quad 0\le t\le\frac1{m-1}.
\]
Together with \(my+m^2x=B\), this is precisely \(0\le x\le B/[m(2m-1)]\). Every connected vertex pair is represented by some such \(k\), so the interval is both necessary and sufficient for \(\Delta=R_m=m^2/B\). This classifies all global critical designs, not just symmetric candidates.

**3. Strict retention below the threshold.** At \(x=0\), the unique best path design is \(a_i=B/m\) and its diameter is \(m^2/B\) by the same Cauchy--Schwarz argument. For \(c<m^2\), take sufficiently small \(x>0\) and let \(a_i=(B-cx)/m\). Then \(s+m^2x=B+(m^2-c)x>B\), and the endpoint resistance, which attains equality in Cauchy--Schwarz, is strictly below \(m^2/B\). At \(x=0\), every other vertex pair has path resistance \(k m/B<m^2/B\) for \(k<m\). Finitely many resistances vary continuously in a neighborhood of the connected path design, so for sufficiently small positive \(x\) every pair has resistance strictly less than \(m^2/B\). This gives an improvement, and every below-threshold optimum must have \(x>0\), since no closing-edge-deleted design can beat the best path. The budget simplex is compact; lower semicontinuity of effective resistance extended by \(+\infty\) on disconnected designs ensures existence of a global optimum.

**4. Unique one-sided limiting design.** Fix any \(0<c<m^2\) and set \(\varepsilon=m^2-c>0\). Use the critical-budget simplex \(\mathcal S=\{(a_i,x)\ge0:\ \sum_i a_i+m^2x=B\}\). Every member \(v\in\mathcal S\) with closing conductance \(x_v\) can be uniformly scaled by \(B/(B-\varepsilon x_v)\) into a feasible, budget-saturating design for price \(c\); the resistance diameter scales to \((1-\varepsilon x_v/B)\Delta(v)\). Conversely all below-threshold optimal designs have saturated budgets and arise this way (any unsaturated connected design can be uniformly enlarged and strictly improved).

Let \(v_\varepsilon\) minimize \((1-\varepsilon x_v/B)\Delta(v)\) over \(\mathcal S\), and let \(x_*=B/[m(2m-1)]\), the largest critical-optimal closing conductance. The endpoint lower bound (1), applied at the critical price, gives \(\Delta(v)\ge m^2/B\) for every \(v\in\mathcal S\). Comparison to the feasible critical design at \(x_*\) yields
\[
\frac{m^2}{B}\left(1-\frac{\varepsilon x_{v_\varepsilon}}B\right)
\le\left(1-\frac{\varepsilon x_{v_\varepsilon}}B\right)\Delta(v_\varepsilon)
\le\frac{m^2}{B}\left(1-\frac{\varepsilon x_*}B\right).
\]
Every factor is strictly positive, because \(\varepsilon<m^2\) and \(x_v\le B/m^2\). Consequently \(x_{v_\varepsilon}\ge x_*\), and \(\Delta(v_\varepsilon)\to m^2/B\) uniformly along every choice of minimizers as \(\varepsilon\to0+\). By compactness, any accumulation point of these normalized designs is a critical optimizer, whose closing conductance is at most \(x_*\) by step 2. The lower inequality forces its closing conductance to equal \(x_*\), and the critical classification then fixes all ordinary conductances. Finally the rescaling factor \(B/(B-\varepsilon x_v)\to1\). Therefore **all** optimal designs converge to the asserted positive-edge endpoint as \(c\uparrow m^2\), whereas the entire region \(c>m^2\) has the fixed deleted-edge optimum. This completes the proof.

## Verification

The standalone file `verify.py` uses Python 3's standard library and `fractions.Fraction`. It independently computes every unordered-pair resistance by the parallel combination of the two disjoint cyclic arc resistances, with the disconnected-arc convention. On execution it reports `VERIFY_OK exact_rational_tests= 2883`. It checks exact critical face equalities and beyond-face strictness for cycle sizes from three through fifteen vertices at three budgets; verifies the high-price lower bound on pseudorandom nonuniform allocations; and verifies strict feasible improvement at several subcritical prices. The program confirms finite rational examples, not the universal theorem; that follows from the proof above.

## Relationship to prior work

Ghosh, Boyd, and Saberi (2006 conference version, 2008 journal version) establish convex conductance optimization and identify minimum maximum pairwise effective resistance as a semidefinite-program design objective. They do not present this exact all-size one-price cycle resistance-diameter transition in the inspected paper and its extensions section. The resistance-diameter objective is **not** the Kirchhoff index (sum of all pair resistances); that related priced-cycle allocation has a different explicit cutoff and a **unique** optimizer at equality. Likewise, published rate-budget optimal spectral-gap results on an unusually priced four-cycle and heterogeneously priced cycles yield the same square-length closing-edge threshold under uniform ordinary prices, but have **different optimal conductance allocations**, including different high-price paths. Thus agreement in the numeric threshold is not an implication of this complete minimax-resistance classification; the discontinuous limiting allocation and the complete critical face require their own resistance comparisons.

## Limitations

Below the price threshold, the theorem determines strict retention and the universal one-sided limit but does not give a closed-form optimum or assert uniqueness. The scope is a cycle with identical ordinary unit prices and one exceptional closing-edge price; arbitrary prices and multiple chords are not treated. The novelty assessment is based on examined sources and searchable prior claims, not exhaustive publication-priority certification. Independent mathematical audit has not been performed.

## References

1. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, Proceedings of the 17th International Symposium on Mathematical Theory of Networks and Systems, Kyoto, July 24--28, 2006, pp. 1185--1196. https://stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf
2. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50(1) (2008), 37--66. DOI https://doi.org/10.1137/050645452 ; author full text https://stanford.edu/~boyd/papers/pdf/eff_res.pdf
3. *Sharp quadratic price threshold for retaining the closing edge of an optimally weighted cycle*, published-finding corpus mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-quadratic-price-threshold-for-retaining-the-closing-edge-o--4f89042df17b
4. *Mass-independent edge screening and complete critical optimizers for priced reversible cycles*, published-finding corpus mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-mass-independent-edge-screening-and-complete-critical-optimizers--b8eae264de71
5. *A sharp shortcut-cost phase transition for fastest mixing on a four-vertex cycle*, published-finding corpus mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-a-sharp-shortcut-cost-phase-transition-for-fastest-mixing-on-a-f--798a42b2934c
