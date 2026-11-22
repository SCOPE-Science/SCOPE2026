# Real-valued generic divergence of magnitude-ordered Fourier sums on odd cyclic Cantor groups

## Finding
Let \(p\ge 3\) be any odd integer, and let \(K_p=\prod_{n\ge1}(\mathbb Z/p\mathbb Z)\) with its compact product topology and normalized Haar probability measure \(\mu\). For a real-valued continuous function, let
\[
\widehat f(\gamma)=\int_{K_p}f(x)\overline{\gamma(x)}\,d\mu(x),\qquad
T_\delta f=\sum_{|\widehat f(\gamma)|\ge\delta}\widehat f(\gamma)\gamma\quad(\delta>0).
\]
The coefficient-threshold sum is finite. Define the subset of the **real** Banach space \(C(K_p;\mathbb R)\)
\[
\mathcal D_{\mathbb R}=\bigl\{f:\sup_{\delta>0}|T_\delta f(x)|=\infty\text{ for }\mu\text{-almost every }x\bigr\}.
\]
**Theorem.** For every odd \(p\ge3\), \(\mathcal D_{\mathbb R}\) is a dense \(G_\delta\) in \(C(K_p;\mathbb R)\). In particular, for every \(\rho>0\) and finite \(F\subset\widehat {K_p}\), there is \(f\in\mathcal D_{\mathbb R}\) with \(\|f\|_\infty<\rho\) and \(\widehat f=0\) on \(F\). Every nonincreasing-magnitude ordering of the nonzero Fourier coefficients has unbounded partial sums on one common full-measure set, irrespective of tie-breaking.

The key finite strengthening is also explicit: for every \(A>0\) and \(0<\varepsilon<1\), there are \(D\ge1\) and a **real-valued, zero-mean** polynomial \(H\) on \((\mathbb Z/p\mathbb Z)^D\), such that
\[
\|H\|_\infty\le1,\qquad
\mu_D\{x:\max_{\delta>0}|T_\delta H(x)|>A\}>1-\varepsilon.
\]
Here the existence of unbounded complex finite models is taken from the stated, publicly proved theorem in Reference [1]; the real-valued finite strengthening and its generic consequence are derived below.

## Assumptions and scope
Characters are \(\chi_\xi(x)=\exp(2\pi i\langle\xi,x\rangle/p)\). All finite Fourier transforms use normalized counting measure. All thresholds retain **all** coefficients whose magnitude is at least \(\delta\); no coefficients of equal magnitude are split. For continuous \(f\), Parseval/Bessel gives finitely many coefficients above each positive threshold and at most countably many distinct threshold sums. The theorem covers arbitrary odd, possibly composite, \(p\); it does not assert the same real-valued result for arbitrary infinite compact abelian groups.

We use the following published input (Nielsen [1], Theorem 2.1 and Proposition 3.7): for every odd \(p\ge3\), \(B>0\) and \(0<\eta<1\), there exist finite \(d\) and a complex polynomial \(P\) on \((\mathbb Z/p\mathbb Z)^d\) such that \(\|P\|_\infty\le1\) and
\[
\mu_d\{x:\max_{\delta>0}|T_\delta P(x)|>B\}>1-\eta.
\]
This is a substantive external theorem, not a claim established by the numerical checks below.

## Proof
**1. A phase-coordinate realification lemma.** Fix a complex polynomial \(P\) on \((\mathbb Z/p\mathbb Z)^d\). Add a fresh coordinate \(s\in\mathbb Z/p\mathbb Z\), put \(\omega=e^{2\pi i/p}\), and define
\[
R(x,s)=\omega^sP(x)+\omega^{-s}\overline{P(x)}=2\operatorname{Re}(\omega^sP(x)).
\]
The function \(R\) is real, has mean zero, and \(\|R\|_\infty\le2\|P\|_\infty\). Its nonzero Fourier coefficients occur only at fresh-coordinate frequencies \(+1\) and \(-1\). These slices are distinct because \(p\) is odd. At \((\xi,+1)\) the coefficient is \(\widehat P(\xi)\), and at \((\xi,-1)\) it is \(\overline{\widehat P(-\xi)}\). Therefore, **at every positive threshold**,
\[
T_\delta R(x,s)=2\operatorname{Re}\bigl(\omega^sT_\delta P(x)\bigr).
\tag{1}
\]
Because \(p\) is odd, \(\sum_{s=0}^{p-1}\omega^{2s}=0\), whence for every \(z\in\mathbb C\)
\[
\frac1p\sum_{s=0}^{p-1}|2\operatorname{Re}(\omega^sz)|^2=2|z|^2.
\]
Thus at least one \(s\) satisfies \(|2\operatorname{Re}(\omega^sz)|\ge\sqrt2|z|\). If \(P\)'s maximal threshold sum exceeds \(B\) at \(x\), the maximal threshold sum of \(R\) exceeds \(B\) for at least one \(s\). Consequently the finite model from [1], with \(\eta=1/2\), yields **for every** \(B\) a real zero-mean \(R\), depending on finitely many coordinates, with \(\|R\|_\infty\le2\) and
\[
\mu\{\max_{\delta>0}|T_\delta R|>B\}>\frac1{2p}.
\tag{2}
\]

**2. Amplify positive probability to arbitrarily high measure.** Choose a target \(A>0\), \(0<\varepsilon<1\), and \(N\) so that \((1-1/(2p))^N<\varepsilon\). On pairwise disjoint fresh coordinate blocks choose positive scalars \(c_1,\ldots,c_N\) and polynomials \(R_j\) as in (2), recursively. Make \(2\sum_jc_j\le1\); ensure the largest Fourier coefficient of \(c_{j+1}R_{j+1}\) is less than half the **smallest nonzero** coefficient magnitude of \(c_jR_j\). This is possible because \(\|\widehat{R_j}\|_\infty\le\|R_j\|_\infty\le2\); choose \(c_{j+1}\) before obtaining \(R_{j+1}\), using the preceding finite minimum. Choose the finite-model amplitude parameter \(B_j\) sufficiently large **after** choosing \(c_j\) that \(c_jB_j>A+2\sum_{i<j}c_i\).

Put \(H=\sum_{j=1}^Nc_jR_j\). Distinct blocks have disjoint nonzero frequency supports (their private phase coordinates have nonzero Fourier frequency), and coefficient magnitudes of later blocks are strictly below those of earlier blocks. If a threshold in block \(j\) witnesses \(|T_\delta R_j|>B_j\), the corresponding threshold for \(H\) selects all earlier blocks and no later blocks; its absolute value is larger than \(A\). The events in (2) are independent, as they depend on disjoint coordinate blocks. Therefore
\[
\mu\{\max_\delta |T_\delta H|>A\}>1-(1-1/(2p))^N>1-\varepsilon.
\]
The function \(H\) is real, mean zero, and bounded by one. This proves the claimed finite real model, with any finite ambient dimension sufficient to contain all blocks.

**3. Density and the \(G_\delta\) description.** Real cylinder character polynomials are dense in \(C(K_p;\mathbb R)\). Fix a real polynomial \(Q\), an approximation radius \(r>0\), a target \(m>0\) and \(k\ge1\). Build small disjoint blocks \(c_jR_j\), all on coordinates beyond those of \(Q\), with \(2\sum c_j<r\), largest coefficient less than the smallest nonzero magnitude of \(\widehat Q\) (if any), and less than \(1/k\). Choose each \(B_j\) so large that \(c_jB_j>m+\|Q\|_\infty+2\sum_{i<j}c_i\). By the same independence argument, \(Q+\sum c_jR_j\) is within \(r\) of \(Q\), and the threshold maximal function exceeds \(m\) on a set of measure greater than \(1-2^{-k}\), already using thresholds below \(1/k\).

Call a threshold *regular* if it equals no Fourier-coefficient magnitude. Each selected finite threshold sum can be represented at a slightly smaller regular threshold without changing the sum. Define \(U_{m,k}\) to consist of real continuous functions with finitely many regular thresholds in \((0,1/k)\) whose maximal absolute selected sums exceed \(m\) on measure greater than \(1-2^{-k}\). The preceding perturbation shows every \(U_{m,k}\) is dense. It is open: for a fixed regular threshold the finite selected frequency set remains constant under sufficiently small uniform perturbations, since individual Fourier coefficients vary by at most the uniform perturbation norm. The associated finite sums vary uniformly, and the strict measure inequality persists. The real Banach space is complete, so \(\bigcap_{m,k\ge1}U_{m,k}\) is dense \(G_\delta\). By continuity of measure as \(k\to\infty\), each member has unbounded threshold sums almost everywhere. Conversely, any such member belongs to every \(U_{m,k}\), since there are countably many threshold sums and their superlevel union has full measure. Thus \(\mathcal D_{\mathbb R}=\bigcap_{m,k\ge1}U_{m,k}\).

**4. Spectral avoidance and arbitrary small norm.** Given finite \(F\subset\widehat{K_p}\), reserve the finite initial coordinate set supporting all characters in \(F\). Choose infinitely many pairwise disjoint finite blocks beyond these coordinates. Recursively choose \(c_j>0\) with \(2\sum_jc_j<\rho\) and \(c_{j+1}\) sufficiently small that all nonzero coefficient magnitudes in \(c_{j+1}R_{j+1}\) lie strictly below every magnitude in \(c_jR_j\). Choose the complex source parameter for \(R_j\) after \(c_j\) so that \(c_jB_j>j+2\sum_{i<j}c_i\). Define \(f=\sum_{j\ge1}c_jR_j\); uniform convergence makes it continuous, real and bounded by \(\rho\). Its Fourier coefficients are exactly its disjoint block coefficients, and no block has a frequency in \(F\), by its nonzero private-coordinate frequency. Independent good events have measure exceeding \(1/(2p)\) each, so the second Borel--Cantelli lemma makes infinitely many occur almost surely. At each such index, all previous blocks are fully selected, all later blocks excluded and the current block contributes absolute size greater than \(j+2\sum_{i<j}c_i\). Thus some threshold sum of \(f\) exceeds \(j\), proving almost-everywhere unboundedness, spectral avoidance and the claimed norm bound.

**5. Ties in greedy order.** Each threshold sum is a finite partial sum of every nonincreasing-magnitude enumeration at the end of a full coefficient-magnitude level. Hence unbounded threshold sums imply unbounded greedy partial sums along these levels, simultaneously for all tie-breakings.

## Verification
The standalone script `check_realification.py` checks (1), both conjugate frequency slices, the phase-max inequality, and coefficient-level separation. It passed 120 finite threshold identities and a two-block Fourier calculation with maximum reported error \(1.11\times10^{-16}\). The constructive finite large-amplitude input is supplied by [1], not independently re-established by this script. The passage to arbitrary amplitude, full measure, and the dense \(G_\delta\) property follows from the exact proof above, not numerical extrapolation.

## Relationship to prior work
Nielsen [1] proves generic divergence in complex-valued \(C(G)\) for every infinite compact abelian group, with its new finite odd-cyclic theorem. Its explicit convention is that function spaces are complex-valued; the real-valued subspace is not supplied by the statement. Taking a real part of an arbitrary complex example is **not** valid because Fourier-coefficient magnitudes change and threshold selection is nonlinear. The phase-coordinate identity (1), followed by probability amplification, is the additional step here. The complex generic theorem is foundational input and no novelty is claimed for its finite tree, stopping-time, or general complex Baire arguments. Körner [2,3] treats the circle and Walsh systems; these do not directly provide the odd-base real-valued result. Related Vilenkin modified-data convergence [4] has different quantifiers.

## Limitations
The theorem is restricted to odd cyclic Cantor groups \(K_p\) and coefficient-magnitude threshold sums. It is not a proof of real-valued generic divergence on every infinite compact abelian group, nor does it give a quantitative dimension bound for the large-amplitude finite models beyond the bound already implicit in [1]. Existing older Vilenkin literature may contain an equivalent real-valued result; bibliographic priority needs independent checking. The numerical checker does not certify the published finite-model theorem or replace the infinite-dimensional proof. This work has not undergone independent mathematical validation.

## References
1. M. Nielsen, *Divergence of decreasing rearranged Fourier series on every infinite compact abelian group*, arXiv:2609.03506 (first public 2026-09-03), Theorem 2.1, Proposition 3.7, Sections 4–5. https://arxiv.org/abs/2609.03506
2. T. W. Körner, *Decreasing rearranged Fourier series*, Journal of Fourier Analysis and Applications 5 (1999), 1–19. https://doi.org/10.1007/BF01274186
3. T. W. Körner, *Hard summation, Olevskii, Tao and Walsh*, Bulletin of the London Mathematical Society 38 (2006), 705–729. https://doi.org/10.1112/S002460930601890X
4. M. G. Grigoryan and S. A. Sargsyan, *Almost Everywhere Convergence of Greedy Algorithm with Respect to Vilenkin System*, Journal of Contemporary Mathematical Analysis 53 (2018), 331–345. https://doi.org/10.3103/S1068362318060043
