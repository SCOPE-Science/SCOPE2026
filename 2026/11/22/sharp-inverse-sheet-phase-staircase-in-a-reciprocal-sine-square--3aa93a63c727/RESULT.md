# Sharp inverse-sheet phase staircase in a reciprocal sine-square planar map

## Finding

For every pair of real parameters \(a,b>0\), restrict the Zhu–Deng–Zhang–Zhu map
\[
F_{a,b}(x,y)=\bigl(\sin^2(a\pi/x+by),\ \sin^2(b\pi y+ax)\bigr)
\]
to the one-step source domain \(S=(0,1]\times[0,1]\). Fix any target \((u,v)\in(0,1)^2\). Write
\[
\alpha=\arcsin\sqrt u,\qquad \theta=\arcsin\sqrt v,\qquad \tau=\theta/\pi,
\]
and let \(P_b(v)\) be the **finite** set of positive phase values \(\zeta\le b\pi\) satisfying \(\sin^2\zeta=v\). Its cardinality is the exact phase staircase
\[
K_b(v)=\#P_b(v)=\max\{0,1+\lfloor b-\tau\rfloor\}
                  +\max\{0,\lfloor b+\tau\rfloor\}.
\]
The number of distinct preimages with first coordinate at least \(\varepsilon\) obeys, as \(\varepsilon\downarrow0\),
\[
\boxed{\ N_{a,b;u,v}(\varepsilon)
=\#\{(x,y)\in S:F_{a,b}(x,y)=(u,v),\ x\ge\varepsilon\}
=\frac{2aK_b(v)}{\varepsilon}+O_{a,b,u,v}(1).\ }
\]
In particular, the target has **countably infinitely many** preimages in \(S\) if and only if \(K_b(v)>0\); if \(K_b(v)=0\), it has only finitely many preimages. Every such preimage is regular: \(\det DF_{a,b}(x,y)\ne0\). The sharp all-interior-target threshold is
\[
\boxed{\ \text{every }(u,v)\in(0,1)^2\text{ has infinitely many preimages in }S
\quad\Longleftrightarrow\quad b\ge\tfrac12.\ }
\]
For \(0<b<1/2\), infinitely many preimages occur exactly when \(0<v\le\sin^2(b\pi)\), independently of \(u\).

There is also a precise spatial limit. If \(K_b(v)>0\), assign equal mass to the second coordinates of the \(N_{a,b;u,v}(\varepsilon)\) preimages. These empirical probability measures approach
\[
\boxed{\ \frac1{K_b(v)}\sum_{\zeta\in P_b(v)}
\delta_{\zeta/(b\pi)}\ }
\]
in Wasserstein-1 distance at rate \(O_{a,b,u,v}(\varepsilon\log(1/\varepsilon))\). Thus the high-multiplicity inverse sheets concentrate at explicitly computable transverse locations; this is a one-step inverse-fiber theorem, not an assertion about forward invariant distributions.

## Assumptions and scope

The parameters \(a,b\) are positive and fixed. The map is not defined at \(x=0\); the source domain includes the edges \(x=1\), \(y=0\) and \(y=1\) but never \(x=0\). Targets are strictly interior: \(0<u,v<1\); the excluded target-edge cases \(u\in\{0,1\}\) or \(v\in\{0,1\}\) can have merged phase solutions and are not asserted. One-step inversion is always defined at source points even though some subsequent forward iterates may land on the excluded singular boundary. The \(O\)-constants depend on the fixed parameters and target; no uniformity near phase-staircase jumps or target edges is asserted. The floor convention includes exact equality at \(\zeta=b\pi\).

## Proof

**1. Exact inverse-sheet parametrization.** The equation for the second coordinate is \(\sin^2(b\pi y+ax)=v\). Because \(0<x\le1\), \(0\le y\le1\), and \(a,b>0\), its phase lies in \((0,b\pi+a]\). Every possible phase has the form
\[
\zeta=k\pi+\theta\quad\text{or}\quad \zeta=(k+1)\pi-\theta,
\qquad k=0,1,2,\ldots,
\]
with \(0<\zeta\le b\pi+a\). Hence there are only finitely many second-phase options, and each gives the straight graph
\[
y_\zeta(x)=\frac{\zeta-ax}{b\pi}.
\]
For this graph, the first-coordinate equation becomes
\[
\sin^2\left(\frac{a\pi}{x}+\frac{\zeta}{\pi}-\frac{ax}{\pi}\right)=u.
\]
Its phase must equal \(m\pi+\delta\), for an integer \(m\) and \(\delta\in\{\alpha,\pi-\alpha\}\). With
\[
c_{m,\zeta,\delta}=m+\frac\delta\pi-\frac\zeta{\pi^2},
\]
this is exactly the quadratic relation
\[
\frac{a}{\pi^2}x^2+c_{m,\zeta,\delta}x-a=0.
\]
It has exactly one positive root, given without cancellation by
\[
\boxed{\ x_{m,\zeta,\delta}=
\frac{2a}{c_{m,\zeta,\delta}+\sqrt{c_{m,\zeta,\delta}^2+4a^2/\pi^2}},
\qquad y_{m,\zeta,\delta}=\frac{\zeta-a x_{m,\zeta,\delta}}{b\pi}.\ }
\]
Keep exactly the pairs satisfying \(0<x\le1\), \(0\le y\le1\). Conversely, substitution recovers \((u,v)\), so this parameterization is exhaustive and generates no duplicates: the second phase determines \(\zeta\), and the first phase uniquely determines \((m,\delta)\) for interior \(u\).

**2. Which phase sheets reach the singular edge.** An allowed second phase \(\zeta\) satisfies
\[
0\le\zeta-ax\le b\pi.
\]
For arbitrarily small \(x>0\), this inequality is feasible precisely when \(0<\zeta\le b\pi\); at equality \(\zeta=b\pi\) one has \(y=1-ax/(b\pi)<1\), so the endpoint phase really contributes. If \(\zeta>b\pi\), the inequality forces \(x\ge(\zeta-b\pi)/a>0\), hence this sheet contains only finitely many admissible inverse points. Counting the two positive phase progressions below \(b\pi\) gives
\[
\#\{k\ge0:k+\tau\le b\}=\max\{0,1+\lfloor b-\tau\rfloor\},
\]
\[
\#\{k\ge0:k+1-\tau\le b\}=\max\{0,\lfloor b+\tau\rfloor\},
\]
which proves the claimed exact formula for \(K_b(v)\).

**3. Sharp inverse count.** For each fixed \(\zeta\in P_b(v)\) and each of the two distinct values of \(\delta\), the positive root exists and is admissible for all sufficiently large integers \(m\). As \(m\to\infty\), the displayed exact root gives
\[
x_{m,\zeta,\delta}=\frac a m+O_{a,b,u,v}(m^{-2}),
\qquad y_{m,\zeta,\delta}=\frac\zeta{b\pi}-\frac{a^2}{b\pi m}+O(m^{-2}).
\]
The map \(x\mapsto a/x-ax/\pi^2\) decreases strictly on \((0,\infty)\). For each \((\zeta,\delta)\), the number of admissible integers \(m\) with \(\varepsilon\le x\le1\) is therefore \(a/\varepsilon+O(1)\), since the lower reciprocal-phase boundary differs from \(a/\varepsilon\) by a bounded amount. Summing both first-phase choices and all \(K_b(v)\) edge-reaching second-phase choices gives \(2aK_b(v)/\varepsilon+O(1)\). All other finitely many second-phase choices have \(x\) bounded away from zero and give only \(O(1)\) points. The same argument proves finiteness when \(K_b(v)=0\).

**4. Regularity and sharp global threshold.** With \(\Theta=a\pi/x+by\) and \(\Phi=b\pi y+ax\), direct differentiation gives
\[
\det DF_{a,b}(x,y)=-ab\left(1+\frac{\pi^2}{x^2}\right)\sin(2\Theta)\sin(2\Phi).
\]
At any inverse point of \((u,v)\in(0,1)^2\), both sine factors are nonzero. Thus *every* inverse is regular, including those on admissible domain edges. The first positive second-phase solution is \(\zeta=\theta\in(0,\pi/2)\). For every \(v\in(0,1)\) it lies at or below \(b\pi\) if \(b\ge1/2\), whereas if \(b<1/2\) this occurs exactly for \(v\le\sin^2(b\pi)\), and no other positive phase can lie below \(b\pi\). This proves the threshold claims.

**5. Transverse empirical law.** Every edge-reaching sheet has \(2a/\varepsilon+O(1)\) points, so their normalized weights converge to equal weights \(1/K_b(v)\); finitely many exceptional points are negligible. Along a sheet, \(|y_{m,\zeta,\delta}-\zeta/(b\pi)|=a x_{m,\zeta,\delta}/(b\pi)=O(1/m)\), whence summing over the \(O(\varepsilon^{-1})\) admissible indices yields a total displacement \(O(\log(1/\varepsilon))\). After division by the total count \(\asymp\varepsilon^{-1}\), the average transport cost is \(O(\varepsilon\log(1/\varepsilon))\). Correcting the finite counting imbalances between sheets costs only \(O(\varepsilon)\) in Wasserstein-1 distance on \([0,1]\). This proves the stated rate and completes the proof.

## Verification

Run `python checks/verify_inverse.py` with Python 3 and no third-party packages. The script verifies the analytic inverse formula by direct substitution at 21,424 enumerated regular inverse points, compares 270 independent inverse counts obtained from monotone phase crossings, tests exact phase thresholds and checks the \(O(1)\) counting residual for shrinking cutoffs. The numerical calculations supplement, but do not replace, the complete proof for all positive real parameters, interior targets and arbitrarily small cutoffs.

## Relationship to prior work

Zhu, Deng, Zhang and Zhu (2023) introduce the exact map in Equation (1), report numerical chaotic indicators and develop an encryption application. Their accessible full-text dynamics and conclusions do not state an all-target inverse-sheet parametrization, the \(b=1/2\) infinite-valence threshold, the phase-count staircase or the transverse empirical law. The published finding *Two fixed-point saddles per reciprocal phase band in a coupled sine-square map* (2026) treats the very same map, but its fixed-point constraint \(F(x,y)=(x,y)\) and small-state saddle spectrum do not imply inverse multiplicities for an arbitrary fixed interior target \((u,v)\) or the dependence on the independent output height \(v\). The published *Singular zero-to-infinite inverse-valence transition in a cosine-flux Chialvo map* (2026) proves a comparable counting principle for a different map, with unbounded source coordinates and nonidentical inverse equations; its theorem does not cover this bounded-square reciprocal-singularity model. Mira's general survey of noninvertible maps motivates inverse-fiber counts but supplies no such formula for this family. These comparisons are a best-knowledge priority assessment, not a proof of uniqueness in the literature.

## Limitations

This theorem is about one-step inverse fibers inside the specified source square and strictly interior targets. It does not prove forward invariant measures, orbitwise chaotic dynamics, cryptographic strength or physical recoverability of arbitrarily near-singular source points. The constant in the counting error can increase near target boundaries or phase thresholds. The finite test script cannot certify the universal asymptotics independently. Broader preimage-counting literature and unpublished equivalent formulations remain originality risks; external independent review has not been performed.

## References

1. S. Zhu, X. Deng, W. Zhang, C. Zhu, *Construction of a New 2D Hyperchaotic Map with Application in Efficient Pseudo-Random Number Generator Design and Color Image Encryption*, Mathematics **11** (2023), 3171, first public date July 19, 2023, https://doi.org/10.3390/math11143171 .
2. *Two fixed-point saddles per reciprocal phase band in a coupled sine-square map* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-two-fixed-point-saddles-per-reciprocal-phase-band-in-a-coupled-s--99bf14d32624 .
3. *Singular zero-to-infinite inverse-valence transition in a cosine-flux Chialvo map* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-singular-zero-to-infinite-inverse-valence-transition-in-a-cosine--8b96b0ec53ba .
4. C. Mira, *Noninvertible maps*, Scholarpedia **2**(9) (2007), 2328, https://doi.org/10.4249/scholarpedia.2328 .
