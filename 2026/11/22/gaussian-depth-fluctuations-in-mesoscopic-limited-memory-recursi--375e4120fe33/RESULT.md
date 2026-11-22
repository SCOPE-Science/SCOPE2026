# Gaussian depth fluctuations in mesoscopic limited-memory recursive trees

## Finding

The last-born vertex in a polynomial-window recursive tree obeys a Gaussian depth law at a scale smaller than its mean. For each fixed \(0<\beta<1\), write
\[
b_\ell=\min\{\ell-1,\,1+\lfloor(\ell-1)^\beta\rfloor\},\qquad
F_\beta(n)=\sum_{\ell=2}^{n}\frac{2}{b_\ell+1}.
\]
If \(D_n\) is the root distance of vertex \(n\) in the tree defined below, then
\[
0\le F_\beta(n)-\mathbb E D_n\le C_\beta(1+\log n),
\qquad F_\beta(n)\sim\frac{2}{1-\beta}n^{1-\beta},
\]
\[
\boxed{\frac{D_n-F_\beta(n)}{n^{(1-\beta)/2}}
\xRightarrow[n\to\infty]{}N\!\left(0,\frac{2}{3(1-\beta)}\right)}
\]
and
\[
\boxed{\frac{\operatorname{Var}(D_n)}{n^{1-\beta}}
\longrightarrow\frac{2}{3(1-\beta)}.}
\]
The centering \(F_\beta(n)\) is explicit at every integer size, including the floor effects of the actual attachment window. The claim concerns the last-born vertex only, not tree height or joint depths.

## Assumptions and scope

Fix a real \(\beta\in(0,1)\). The random rooted increasing tree has vertices \(1,\ldots,n\), with root \(1\). For every \(\ell\ge2\), vertex \(\ell\) independently chooses one parent uniformly from
\[
\{\max(1,\ell-1-\lfloor(\ell-1)^\beta\rfloor),\ldots,\ell-1\}.
\]
The number of eligible parents is exactly \(b_\ell\). Define \(D_n\) as the number of parent edges from \(n\) to \(1\), and define \(F_\beta(n)\) in the finding. All limits keep \(\beta\) fixed; no uniformity at the endpoints \(\beta=0,1\) is claimed. Constants \(C_\beta\) are finite and may depend on \(\beta\), not on \(n\).

## Proof

**1. Backward ancestry and an exact potential decomposition.** Because the parent choices for distinct vertices are independent, the ancestry of vertex \(n\) has the same law as the strictly decreasing Markov chain \(L_0=n\), \(L_{s+1}=L_s-J_s\), stopped on first reaching \(1\), where conditional on \(L_s=\ell\) the jump \(J_s\) is uniform on \(\{1,\ldots,b_\ell\}\). Its stopping time \(T\) equals \(D_n\) in law and is bounded by \(n-1\).

Set \(a_\ell=2/(b_\ell+1)\) for \(\ell\ge2\) and \(F_\beta(1)=0\). Since \(\mathbb E(J_s\mid L_s=\ell)=(b_\ell+1)/2\),
\[
\mathbb E(a_\ell J_s-1\mid L_s=\ell)=0.
\]
For any allowable downward jump from \(\ell\) to \(\ell-J\), define
\[
\epsilon(\ell,J)=\sum_{u=\ell-J+1}^{\ell}(a_u-a_\ell)\ge0.
\]
The nonnegativity follows because \(b_u\) is nondecreasing, so \(a_u\) is nonincreasing. The identity
\[
F_\beta(\ell)-F_\beta(\ell-J)
=\sum_{u=\ell-J+1}^{\ell}a_u=a_\ell J+\epsilon(\ell,J)
\]
telescopes along the ancestry. Consequently, with
\[
M_T=\sum_{s<T}(a_{L_s}J_s-1),\qquad
R_T=\sum_{s<T}\epsilon(L_s,J_s),
\]
we have the *pathwise exact equation*
\[
F_\beta(n)=T+M_T+R_T.
\]
The stopped process \(M_T\) is a zero-mean martingale: the jumps are centered, \(|a_\ell J-1|\le1\), and the stopping time is bounded.

**2. Deterministic logarithmic control of the discretization error.** We prove that a constant \(C_\beta<\infty\) exists such that for *every ancestral path*,
\[
0\le R_T\le C_\beta(1+\log n).
\]
The integer widths \(b_\ell\) are nondecreasing and increase by at most one at each successive integer label. Let \(\mathcal B\) be their strict-increase locations. At \(v\in\mathcal B\), put \(m=b_v=b_{v-1}+1\). Its potential drop is
\[
\delta_v=a_{v-1}-a_v=\frac{2}{m(m+1)}.
\]
Expanding each \(a_u-a_\ell\) into such drops, the contribution of any particular boundary \(v\) crossed during one downward jump starting at \(\ell\) is at most \(J\delta_v\le b_\ell\delta_v\). Because the successive ancestor labels strictly decrease, a given boundary can be crossed by at most one jump of the complete path.

For all sufficiently large \(\ell\), \(b_\ell\le\ell/2\). If a jump from \(\ell\) crosses a boundary \(v\), then \(v\ge\ell-b_\ell+2\ge\ell/2\). The polynomial width assumption therefore gives \(b_\ell\le C_\beta b_v=C_\beta m\); enlarging \(C_\beta\) handles the finitely many smaller \(\ell\). Hence a crossed boundary contributes at most \(2C_\beta/(m+1)\). As the width increases by one per boundary, each positive integer \(m\) is associated with at most one such boundary. Summing across all crossed boundaries yields
\[
R_T\le 2C_\beta\sum_{m=2}^{b_n}\frac1{m+1}
\le C'_\beta(1+\log n).
\]
In particular, \(M_T\) has expectation zero and
\[
\mathbb E T=F_\beta(n)-\mathbb E R_T,
\qquad 0\le F_\beta(n)-\mathbb E T\le C'_\beta(1+\log n).
\]

**3. Quadratic variation and first-order concentration.** The conditional variance of the centered increment at state \(\ell\) is exactly
\[
v_\ell=\frac{4}{(b_\ell+1)^2}\operatorname{Var}(J_s\mid L_s=\ell)
=\frac{b_\ell-1}{3(b_\ell+1)}\longrightarrow\frac13.
\]
Its predictable quadratic variation is \(Q_T=\sum_{s<T}v_{L_s}\), satisfying \(Q_T\le T/3\). Optional martingale isometry gives
\[
\mathbb E M_T^2=\mathbb E Q_T\le\frac{\mathbb E T}{3}\le\frac{F_\beta(n)}3.
\]
Because \(F_\beta(n)\sim2n^{1-\beta}/(1-\beta)\to\infty\) and \(R_T=O_\beta(\log n)\) pathwise, the decomposition and Chebyshev's inequality imply \(T/F_\beta(n)\to1\) in probability. Moreover, \(Q_T/F_\beta(n)\to1/3\) in probability: for each fixed \(B\), there are only finitely many states with \(b_\ell\le B\), each state can be visited at most once, and at all other states \(|v_\ell-1/3|\le2/[3(B+1)]\). This controls \(|Q_T-T/3|\) by a fixed finite number plus an arbitrarily small multiple of \(T\).

**4. Gaussian law.** Pad the stopped martingale with zero increments to obtain a triangular martingale array. Every increment divided by \(\sqrt{F_\beta(n)}\) is bounded by \(F_\beta(n)^{-1/2}\), so the conditional Lindeberg condition holds. The predictable quadratic variation divided by \(F_\beta(n)\) converges in probability to \(1/3\). The martingale central limit theorem therefore gives
\[
\frac{M_T}{\sqrt{F_\beta(n)}}\Rightarrow N(0,1/3).
\]
The pathwise estimate \(R_T=O_\beta(\log n)=o(\sqrt{F_\beta(n)})\) and the identity \(T-F_\beta(n)=-M_T-R_T\) give the stated centered CLT after substituting the asymptotic for \(F_\beta(n)\).

**5. Exact variance asymptotic.** By optional isometry, \(\mathbb E M_T^2=\mathbb E Q_T\). Since \(T\le F_\beta(n)-M_T\), the preceding moment bounds give \(\mathbb E T/F_\beta(n)\to1\). The same bounded-variation comparison as in step 3, this time in expectation, gives \(\mathbb E Q_T/F_\beta(n)\to1/3\). Therefore \(\operatorname{Var}(M_T)\sim F_\beta(n)/3\). The deterministic \(O_\beta(\log n)\) bound on \(R_T\) implies \(\operatorname{Var}(R_T)=O_\beta((\log n)^2)\), and Cauchy–Schwarz makes the covariance of \(M_T\) and \(R_T\) equal to \(o(F_\beta(n))\). Thus \(\operatorname{Var}(T)\sim F_\beta(n)/3\), completing the proof.

## Verification

The bundled `verify_depth.py` uses only the Python standard library. At each of \(\beta=1/3,1/2,2/3\), it compares the exact backward-chain depth distribution with **independent enumeration of all vertex-parent configurations** through nine vertices. It separately enumerates every ancestral path in these finite sizes and tests both the exact potential identity and \(R_T\ge0\). Larger dynamic programs inspect mean and variance through \(n=3000\). The checker finished with **973 passed finite assertions and diagnostics**. These finite calculations are cross-checks; the infinite claims follow from the proof above and not from numerical extrapolation. Run `python3 verify_depth.py` in the folder containing this document and the checker.

## Relationship to prior work

Angel, Bhamidi, Donderwinkel, Maitra and Sakanaveeti (2025, arXiv:2510.18856) introduce the recent-window recursive-tree model, including the polynomial mesoscopic regime, and derive first-order height and depth behavior through ancestry methods. The present result identifies a second-order *last-born-depth* central limit theorem, a finite-size centering that preserves integer-rounding effects, and the exact leading variance constant. It makes no claim of a new first-order depth law or of a Gaussian height theorem.

Devroye, Fawzi and Fraiman (2011/2012) establish depth properties and fluctuation results for *scaled-attachment* recursive trees with multiplicative parent indices. That model has a logarithmic depth scale, unlike the present sublinear recent-window attachment process with polynomial depth. The usual bounded-increment martingale central limit theorem is standard; the specific pathwise logarithmic potential-error bound connects that general tool to this model.

## Limitations

The parameters \(\beta=0\) and \(\beta=1\), a varying-\(\beta\) triangular regime, the tree's maximum height, multivertex joint fluctuations, rates of Gaussian approximation, and a local limit theorem are outside the claim. The expectation centering may not be replaced by its leading-order power without controlling smaller deterministic terms. The findings have not undergone independent mathematical assessment. A general or unindexed absorption-time theorem might imply this specialization; the literature comparison is limited to inspected and searchable sources.

## References

1. O. Angel, S. Bhamidi, S. Donderwinkel, N. Maitra and A. Sakanaveeti. *Evolution of recursive trees with limited memory*. arXiv:2510.18856, v1 posted 2025-10-21. https://arxiv.org/abs/2510.18856 ; https://arxiv.org/html/2510.18856.
2. L. Devroye, O. Fawzi and N. Fraiman. *Depth properties of scaled attachment random recursive trees*. Random Structures & Algorithms, 41 (2012), 66–98; first published online 2011. https://doi.org/10.1002/rsa.20391 ; https://luc.devroye.org/devroye-fawzi-fraiman-sarrt-2012.pdf.
3. A standard bounded-increment martingale central limit theorem (conditional-Lindeberg and predictable-quadratic-variation formulation); used as a classical probability tool, not as an originality claim.
