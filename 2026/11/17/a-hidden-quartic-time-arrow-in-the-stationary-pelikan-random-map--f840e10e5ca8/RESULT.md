# A hidden quartic time arrow in the stationary Pelikan random map

## Finding
Consider the stationary random interval process whose independent steps are doubling modulo one with probability \(p\) or halving with probability \(q=1-p\), where \(1/2<p\leq1\). For every integer lag \(n\geq0\) and every pair of nonnegative integers \(a,b\) with \(a+b\leq3\), its two-time coordinate moments are time-symmetric:
\[
\boxed{\mathbb E[X_0^aX_n^b]=\mathbb E[X_0^bX_n^a].}
\]
Nevertheless, the first asymmetric two-time coordinate monomial has total degree four: for **every** integer \(n\geq1\),
\[
\boxed{\Delta_n=\mathbb E[X_0^3X_n]-\mathbb E[X_0X_n^3]>0,\qquad
\Delta_1=\frac{2p-1}{320}.}
\]
The entire positive sequence is given exactly by a finite path sum. Put \(r=q/p\). Let \(K_0\) have geometric distribution \(\Pr(K_0=k)=(1-r)r^k\). Given \(K_{j-1}\), double steps of probability \(p\) replace \(K_{j-1}\) by \(\max(K_{j-1}-1,0)\), while half steps of probability \(q\) replace it by \(K_{j-1}+1\). Write \(L_n\) for the number of double steps taken at \(K_{j-1}=0\) during the first \(n\) steps. Then
\[
\boxed{\Delta_n=\frac1{120}\,\mathbb E\!\left[2^{-3K_0-K_n}\left(2^{-L_n}-2^{-3L_n}\right)\right].}
\]
In particular, only the finitely many starting depths \(K_0\in\{0,\ldots,n-1\}\) contribute; enumerating the \(2^n\) possible step words supplies an exact rational expression for every rational \(p\). At the deterministic endpoint \(p=1\),
\[
\boxed{\Delta_n=\frac{2^{-n}-2^{-3n}}{120}.}
\]
The distinction concerns stationary **two-time polynomial coordinate statistics**, not reversibility of the entire trajectory law or equality of every three-time cubic moment.

## Assumptions and scope
The state space is \([0,1)\), with maps \(D(x)=2x\bmod1\) and \(H(x)=x/2\). At each time step choose \(D\) independently with probability \(p\) and \(H\) with probability \(q\). The stationary law is the absolutely continuous invariant law for \(p>1/2\), with density constant on shells \(I_j=(2^{-j-1},2^{-j})\), namely
\[
 a_j=\frac{2p-1}{p}\sum_{k=0}^{j}(2q/p)^k,\quad j\geq0.
\]
At \(p=1\), the invariant law is uniform. Endpoints of binary shells have zero stationary mass. Excluded is the null-recurrent case \(p=1/2\), for which there is no such stationary probability law. All claims are annealed under stationary initialization and independent map choices.

## Proof
**Step 1: a reversible hidden-depth realization.** Let \(U\) be uniform on \([0,1)\), independent of \(K_0\) with \(\Pr(K_0=k)=(1-r)r^k\). Define \(X_0=2^{-K_0}U\). On shell \(I_j\), each mixture component \(K_0=k\leq j\) contributes density \((1-r)r^k2^k\), hence their sum equals the displayed invariant density \(a_j\). A double step at positive depth decreases \(K\) by one and leaves \(U\) unchanged; a double step at depth zero leaves \(K\) at zero and replaces \(U\) by \(D(U)\); a half step increases \(K\) by one and leaves \(U\) unchanged. All three prescriptions give exactly the physical action of \(D\) or \(H\) on \(X=2^{-K}U\). Consequently, for every finite time,
\[
\boxed{X_n=2^{-K_n}D^{L_n}(U),\qquad X_0=2^{-K_0}U.}
\]
The depth chain has nearest-neighbor transitions \(k\to k-1\) with probability \(p\) when \(k>0\), \(k\to k+1\) with probability \(q\), and a self-loop at zero with probability \(p\). It is reversible under the geometric distribution: \((1-r)r^kq=(1-r)r^{k+1}p\). In particular its joint path law is invariant under reversing any finite path, and the path statistic \(L_n\) (the number of zero-to-zero transitions) is unchanged by reversal. Uniform \(U\) remains uniform after applying \(D^m\) for any integer \(m\geq0\), proving that this representation is stationary.

**Step 2: exact universal two-time mixed moments for the binary shift.** Let \(h_{a,b}(m)=\int_0^1u^a(D^mu)^b\,du\). Write \(N=2^m\) and decompose \(u=(J+V)/N\), where \(J\) is uniform on \(\{0,1,\ldots,N-1\}\) and \(V=D^m(u)\) is uniform on \([0,1)\), independent of \(J\). Expanding finite powers and using the elementary sums of powers of \(J\) gives
\[
\begin{aligned}
 h_{2,1}(m)&=h_{1,2}(m)=\frac16+\frac{2^{-m}}{12},\\
 h_{3,1}(m)&=\frac18+\frac{2^{-m}}{12}-\frac{2^{-3m}}{120},\\
 h_{1,3}(m)&=\frac18+\frac{3\,2^{-m}}{40}.
\end{aligned}
\]
Thus
\[
\boxed{h_{3,1}(m)-h_{1,3}(m)=\frac{2^{-m}-2^{-3m}}{120}.}
\]
The identities include \(m=0\), where both sides of each antisymmetric difference vanish. For total degree at most three, the only potentially nontrivial unordered mixed-exponent pair is \((a,b)=(2,1)\); the pairs with one exponent zero are symmetric simply by stationarity. The remaining pair \((1,1)\) is symmetric by commutativity.

**Step 3: time reversal transfers asymmetry entirely to the binary shift.** Conditioning on the hidden path and \(U\), for any nonnegative integers \(a,b\),
\[
\mathbb E[X_0^aX_n^b]
=\mathbb E\!\left[2^{-aK_0-bK_n}h_{a,b}(L_n)\right].
\]
Reversing a stationary depth path changes \(K_0\) into \(K_n\), preserves \(L_n\), and leaves its probability unchanged. Hence
\[
\mathbb E[X_0^aX_n^b]-\mathbb E[X_0^bX_n^a]
=\mathbb E\!\left[2^{-aK_0-bK_n}\left(h_{a,b}(L_n)-h_{b,a}(L_n)\right)\right].
\]
Substituting the shift identities proves symmetry through degree three and the claimed quartic formula with \(a=3,b=1\).

**Step 4: strictness, finiteness, and the leading exact value.** Since \(2^{-L}-2^{-3L}\) is nonnegative for all nonnegative integers \(L\) and strictly positive exactly when \(L\geq1\), every summand in the quartic formula is nonnegative. For every \(n\geq1\), the event \(K_0=0\) followed by \(n\) double steps has probability \((1-r)p^n>0\), and on it \(L_n=n\geq1\). Thus \(\Delta_n>0\). If \(K_0\geq n\), no trajectory can visit a zero-to-zero transition during \(n\) steps, so that entire initial-depth tail contributes zero: the expectation is a **finite** path sum. For \(n=1\), its only positive term is \(K_0=K_1=0\) under a double step, giving
\[
\Delta_1=\frac1{120}(1-r)p\left(\frac12-\frac18\right)
=\frac{2p-1}{320}.
\]
For \(p=1\), the hidden depth is identically zero, while \(L_n=n\), yielding the stated endpoint law. This completes all quantifiers.

## Verification
The included `verify.py` uses only Python's standard library and exact rational arithmetic. It checks the four uniform-shift moment identities by independent dyadic-cylinder integration for \(m=0,\ldots,7\); verifies the one-step arrow formula independently from a stationary fourth-moment balance and direct polynomial integration on the two map branches for \(p\in\{3/5,2/3,4/5,1\}\); and evaluates the finite hidden-depth path formula exactly through \(n=7\) at these four probabilities. It also tests the deterministic endpoint identity at every tested lag. Run `python3 verify.py` from the package directory. The checks are finite diagnostics; the proof above establishes the all-lag theorem.

## Relationship to prior work
Yan, Majumdar, Ruffo, Sato, Beck and Klages (2023/2024) establish the invariant density and ordinary second-order stationary correlations of this map, including short exact lag formulas. Monthus (2024 preprint, revised 2025), Section VI.2 and Section VI.5, introduces a binary-stack trajectory representation and studies the **uniform-initial** linear two-time correlation; the hidden-depth structure is therefore credited, not claimed as newly discovered. The recently indexed stationary-covariance result *Exact stationary correlation transform and spectral-edge amplitudes for the Pelikan random map* evaluates the degree-two position covariance across all lags, not the degree-four antisymmetric two-time statistic. Independently, *Exact third-order correlations distinguish full-branch interval maps with identical linear and quadratic autocorrelations* considers a deterministic full-branch map and three-time cubic statistics under Lebesgue measure; it does not subsume this random-map two-time hierarchy. The new contribution assessed here is the **degree-four minimality of directional two-time polynomial information**, the strict all-lag arrow, and the exact finite path formula and one-step amplitude. These do not follow solely from the published degree-two formulas without additional fourth-moment and reversibility analysis.

## Limitations
The model is one-dimensional and uses the particular observable \(x\), stationary annealed sampling, and independent map choices. Polynomial moment symmetry through degree three is only a necessary weak condition for time reversibility, not a claim of full dynamical reversibility, full two-time distributional symmetry, or three-time cubic symmetry. The existing binary-stack machinery could permit an independent derivation of these identities, and unindexed equivalent high-order calculations cannot be ruled out. No asymptotic rate for \(\Delta_n\) as \(n\to\infty\) is claimed. No independent mathematical audit or historical-priority certification is represented.

## References
1. J. Yan, M. Majumdar, S. Ruffo, Y. Sato, C. Beck and R. Klages, *Transition to anomalous dynamics in a simple random map*, arXiv:2308.09269, first public version 2023-08-18; *Chaos* 34, 023128 (2024), https://arxiv.org/abs/2308.09269 .
2. C. Monthus, *Explicit dynamical properties of the Pelikan random map in the chaotic region and at the intermittent critical point towards the non-chaotic region*, arXiv:2409.19999, first public version 2024-09-30, https://arxiv.org/html/2409.19999v2 .
3. S. Pelikan, *Invariant densities for random maps of the interval*, *Transactions of the American Mathematical Society* 281 (1984), 813–825, doi:10.1090/S0002-9947-1984-0722776-1 .
4. *Exact stationary correlation transform and spectral-edge amplitudes for the Pelikan random map*, published-finding corpus indexed finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-stationary-correlation-transform-and-spectral-edge-amplitu--d19d3482d20b .
5. *Exact third-order correlations distinguish full-branch interval maps with identical linear and quadratic autocorrelations*, published-finding corpus indexed finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-third-order-correlations-distinguish-full-branch-interval--2158555bdbfa .
