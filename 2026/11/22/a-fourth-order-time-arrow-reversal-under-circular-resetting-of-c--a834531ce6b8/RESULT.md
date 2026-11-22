# A fourth-order time-arrow reversal under circular resetting of coupled harmonic modes

## Finding

Consider the harmonically coupled two-dimensional diffusion defined below, with Poisson resetting to an independently chosen uniform point of a fixed circle. Its two orthogonal normal-mode positions are uncorrelated at **every** time separation, yet their squared positions possess nonzero, time-ordered correlations that may reverse sign exactly once as the resetting rate is varied.

Write \(Q_+=(X+Y)/\sqrt 2\) and \(Q_-=(X-Y)/\sqrt 2\), and define their stationary connected squared-mode correlation \(K(r)=\operatorname{Cov}(Q_+^2,Q_-^2)\). Put \(z=R^2/(2T)\). Then

\[
K(r)=\frac{T^2r\,[8-16z+z^2(8-4u^2-(r+2)^2)]}{2(r+4)((r+2)^2-4u^2)}.
\]

For every \(t\geq0\), the two chronological energy correlations are **exactly**

\[
C_{+-}(t):=\operatorname{Cov}(Q_+(0)^2,Q_-(t)^2)=K(r)e^{-(r+2-2u)t},
\]
\[
C_{-+}(t):=\operatorname{Cov}(Q_-(0)^2,Q_+(t)^2)=K(r)e^{-(r+2+2u)t}.
\]

Whenever \(K(r)\ne0\), their ratio is \(C_{+-}(t)/C_{-+}(t)=e^{4ut}\), independent of the resetting rate, circle radius and bath temperature. The difference \(C_{+-}(t)-C_{-+}(t)\) has the sign of \(K(r)\) for **every** \(t>0\).

Set
\[
z_\pm(u)=\frac{2\pm\sqrt{2+2u^2}}{1-u^2}.
\]

If \(0<z<z_-(u)\) or \(z>z_+(u)\), there is **exactly one** positive resetting rate
\[
r_*(u,z)=\sqrt{8-4u^2+\frac8{z^2}-\frac{16}{z}}-2
\]
at which the time-order asymmetry vanishes; it is positive below this rate and negative above it. For \(z_-(u)\leq z\leq z_+(u)\), it is strictly negative for every positive resetting rate. At the isolated zero, both ordered squared-mode covariances vanish for all lags; this does not imply that the full stationary process is reversible. In particular, \(K(r)\to-R^4/8\) as \(r\to\infty\).

## Assumptions and scope

Fix \(0<u<1\), \(T>0\), \(R>0\), \(r>0\). Between resets let
\[
\mathrm dX_t=(-X_t-uY_t)\,\mathrm dt+\sqrt{2T}\,\mathrm dB^x_t,\qquad
\mathrm dY_t=(-Y_t-uX_t)\,\mathrm dt+\sqrt{2T}\,\mathrm dB^y_t,
\]
where \(B^x\) and \(B^y\) are independent standard Brownian motions. At times of an independent Poisson clock of rate \(r\), replace the pair by \((R\cos\Theta,R\sin\Theta)\), with a fresh independent \(\Theta\sim\operatorname{Uniform}[0,2\pi)\). Expectations are under the unique stationary law. The squared-mode correlations are connected covariances of positions at observation times, not instantaneous jump-current quantities.

The claim is restricted to *equal thermal bath intensities*, strictly positive finite reset circle radius, complete simultaneous resets, and stable nonzero coupling \(u\in(0,1)\). These restrictions matter; unequal bath intensities and other reset mark geometries need not have the same sign diagram.

## Proof

**1. Diagonalization and reset geometry.** The orthogonal transformation to \(Q_\pm\) gives independent thermal modes with decay rates \(a_+=1+u\) and \(a_-=1-u\): \(\mathrm dQ_\pm=-a_\pm Q_\pm\,\mathrm dt+\sqrt{2T}\,\mathrm dW_\pm\). A uniformly sampled circle remains uniform after the orthogonal transformation. At a reset its two normal-mode values \((U_+,U_-)\) satisfy
\[
\mathbb EU_\pm=\mathbb EU_+U_-=0,\quad
\mathbb EU_\pm^2=A:=R^2/2,\quad
\mathbb E(U_+^2U_-^2)=R^4/8=A^2/2.
\]
The reset marks' negative squared-coordinate covariance \(-A^2/2\) is the geometric contribution.

**2. Stationary moment equations.** The generator is the sum of independent Ornstein–Uhlenbeck generators and the complete-reset operator \(r(\mathbb E_{U}f(U)-f)\). For each mode this yields
\[
M_\pm:=\mathbb EQ_\pm^2=\frac{2T+rA}{r+2a_\pm}.
\]
For \(f(Q_+,Q_-)=Q_+Q_-\), the reset expectation and the thermal cross derivative both vanish, so \(\mathbb EQ_+Q_-=0\). For \(f=Q_+^2Q_-^2\), stationarity gives
\[
0=-(r+2a_++2a_-)M_{22}+2T(M_++M_-)+rA^2/2.
\]
Because \(a_++a_-=2\), this uniquely determines
\[
M_{22}=\frac{2T(M_++M_-)+rA^2/2}{r+4}.
\]
Subtracting \(M_+M_-\), substituting \(A=Tz\) and factoring proves the displayed formula for \(K(r)\). Bounded reset marks and stable OU motion ensure finite moments and justify the stationary equations.

**3. Exact chronological regression.** The generator maps \(Q_\pm^2-M_\pm\) to \(-(r+2a_\pm)(Q_\pm^2-M_\pm)\). By the Markov semigroup,
\[
\mathbb E[Q_\pm(t)^2-M_\pm\mid Q_+(0),Q_-(0)]
=e^{-(r+2a_\pm)t}(Q_\pm(0)^2-M_\pm).
\]
Multiplication by the other centered square at time zero proves both ordered formulas. The same regression applied to \(Q_\pm\), together with the zero instantaneous cross covariance, gives \(\mathbb E[Q_+(0)Q_-(t)]=\mathbb E[Q_-(0)Q_+(t)]=0\). For \(u>0\) and \(t>0\), the difference of the two squared-mode exponential factors is positive, proving the claimed sign of the time-order asymmetry.

**4. Exact sign classification.** For \(r>0\), every factor outside the square bracket in \(K(r)\) is positive. The bracket is the strictly decreasing function
\[
H(r)=8-16z+z^2[8-4u^2-(r+2)^2],\qquad H'(r)=-2z^2(r+2)<0.
\]
Its value at zero is \(H(0)=4[(1-u^2)z^2-4z+2]\), and \(H(r)\to-\infty\). The quadratic in brackets has the two positive roots \(z_-(u)\) and \(z_+(u)\). It is positive precisely in the two stated open intervals. Accordingly, if it is positive there is exactly one positive zero of \(H\), which gives \(r_*\) by solving \(H(r_*)=0\); otherwise \(H(r)<0\) for all \(r>0\), including equality at the radius boundaries. Finally the highest-power terms of the rational expression give \(K(r)\to-T^2z^2/2=-R^4/8\).

## Verification

The standalone `checker.py` reconstructs \(K(r)\) independently from the stationary moment equations and from the closed rational formula, comparing 180 parameter selections with exact rational arithmetic. It additionally compares seven parameter selections with independent quadrature of the reset-age Gaussian mixture, including both sign-reversal branches, and performs nine chronological regression comparisons. Execute with `python checker.py` (Python 3.9+, SciPy). These finite checks corroborate the generator derivation and cannot substitute for the general algebraic proof above.

## Relationship to prior work

Majumdar, Schehr, Viot and Oshanin (2026) introduce the complete circle-reset Brownian gyrator and give its stationary characteristic function, marginal and second moments, angular momentum, and angular velocity; especially their section 4, equations (51)–(54), supplies the starting dynamics and second-moment context. That full stationary characteristic function implicitly determines equal-time fourth moments; no independent invention of the underlying process or the general stationary distribution is asserted here. The *new assessed claim* is the explicit two-branch geometric sign classification and unique rate reversal for **ordered, two-time modal-energy correlations**, including their dimensionless rate-independent chronological ratio, which is not a statement about the mean angular momentum or any stationary one-point distribution. Standard Markov-generator moment methods are used transparently, not presented as novel.

Existing analyses of shared stochastic forcing and simultaneous multiplicative resetting show related fourth-order energy memory in different models. Those do not establish the circular-reset negative geometric term or the two disjoint radius intervals and their rate reversal. The comparison is about the hypotheses and implications, not merely different titles.

## Limitations

This is a self-reviewed analytic mathematical statement, not an independent certification, a thermodynamic entropy-production theorem, or a direct experimental observation. The sign of one fourth-order diagnostic can vanish without making the process reversible. The theorem does not treat unequal thermal noise, partial resets, nonuniform reset angles, or nonlinear potentials. The complete stationary characteristic function in the source manuscript is broad enough to recover any equal-time moment through differentiation; novelty is claimed only for the sharpened chronological and global sign-classification results. Unindexed or inaccessible equivalent results remain a publication-priority risk.

## References

1. S. N. Majumdar, G. Schehr, P. Viot, and G. Oshanin, *Brownian gyrator model with stochastic resetting*, arXiv:2611.06322v1, publicly submitted 2026-11-04. https://arxiv.org/abs/2611.06322
2. S. Cerasoli, S. Ciliberto, E. Marinari, G. Oshanin, L. Peliti, and L. Rondoni, *Spectral fingerprints of nonequilibrium dynamics: The case of a Brownian gyrator*, Physical Review E 106, 014137 (2022). https://doi.org/10.1103/PhysRevE.106.014137
