# Sharp two-time heat-sampling stability on the first Fourier band of a cycle

## Finding

Let \(N\ge5\). On the cycle \(C_N=\mathbb Z/N\mathbb Z\), let \(L=I-(T+T^{-1})/2\), with \((Tf)(j)=f(j+1)\), and let
\[
H_1=\operatorname{span}\{e_0,e_1,e_{-1}\},\qquad e_k(j)=N^{-1/2}e^{2\pi i k j/N}.
\]
Put \(\lambda_1=1-\cos(2\pi/N)\). Fix a positive observation time \(t\), set \(q=e^{-t\lambda_1}\in(0,1)\), and for a nonzero offset \(d\pmod N\) observe the four **raw**, equally weighted samples
\[
\mathcal M_{d,t}f=\bigl(f(0),f(d),(e^{-tL}f)(0),(e^{-tL}f)(d)\bigr),\qquad f\in H_1.
\]
Write \(c=\cos(2\pi d/N)\), \(h=1+q^2\), \(k=(1-q)^2\), and \(\mathcal T(c)=4+2h(1+c)\). The three eigenvalues of \(N\mathcal M_{d,t}^{*}\mathcal M_{d,t}\), with multiplicity, are exactly
\[
\eta(c)=2h(1-c),\qquad
\mu_{\pm}(c)=\frac{\mathcal T(c)\pm\sqrt{\mathcal T(c)^2-16k(1+c)}}2.
\]
Thus the sharp lower frame bound is
\[
A_{N,d}(q)=\frac1N\min\{\eta(c),\mu_-(c)\},
\]
and the sharp upper bound is \(N^{-1}\max\{\eta(c),\mu_+(c)\}\). The four samples recover every element of \(H_1\) exactly when the two sites are distinct and non-antipodal (that is, \(-1<c<1\)); two time levels are necessary for such recovery with only two sensors.

The **continuous-angle maximum** of the lower bound is attained at a single angular cosine \(c_*(q)\), namely the unique root in \((1/2,1)\) of
\[
2(1+q^2)^2c^2+\beta(q)c-(1+q)^2=0,
\qquad \beta(q)=1-q^2-2q-2q^4.
\]
Equivalently,
\[
c_*(q)=\frac{-\beta(q)+\sqrt{\beta(q)^2+8(1+q^2)^2(1+q)^2}}{4(1+q^2)^2}.
\]
The sharp continuous-angle design value is \(A_*(q)=2(1+q^2)(1-c_*(q))/N\). In particular, the best angle approaches \(\pi/3\) when \(q\downarrow0\), whereas as \(q\uparrow1\),
\[
1-c_*(q)=\frac{(1-q)^2}{6}+O((1-q)^3),\quad
\arccos c_*(q)=\frac{1-q}{\sqrt3}+O((1-q)^2),\quad
A_*(q)=\frac{2(1-q)^2}{3N}+O\bigl((1-q)^3/N\bigr).
\]
The optimal sensors thus migrate from a one-sixth-cycle separation toward coincidence as the two observation times become indistinguishable.

**Exact finite-cycle design.** For each \(1\le d\le\lfloor N/2\rfloor\), set \(c_d=\cos(2\pi d/N)\). Among this ordered finite grid, the maximizing offsets are precisely the better of (or both, in case of a tie) the grid point immediately below \(c_*(q)\) and the grid point immediately above \(c_*(q)\), omitting a nonexistent endpoint. Include the reflected offsets \(N-d\). This rule and the displayed spectral formulas give the exact best lower frame bound and every optimal sensor pair for each \(N\ge5\) and each \(t>0\). In particular, for every fixed \(N\), nearest-neighbor sensors become optimal for sufficiently small positive \(t\).

## Assumptions and scope

All signals and frame bounds use the ordinary counting-measure norm on \(\mathbb C^N\) and the ordinary Euclidean norm on the four complex observations, without spectral separation, time preconditioning, or stochastic noise weighting. The operator is the normalized graph Laplacian of the unweighted cycle. The active space comprises precisely the constant and first positive/negative Fourier modes, a natural three-dimensional graph Paley–Wiener subspace because the next Laplacian eigenvalue is strictly larger for \(N\ge5\). The parameter \(q\in(0,1)\) is equivalent to an arbitrary finite positive heat time.

## Proof

The complex basis \(e_0,e_1,e_{-1}\) is orthonormal. Replace the last two vectors by the equally normalized real cosine and sine modes; this unitary basis change leaves the frame spectrum invariant. Multiply the analysis matrix by \(\sqrt N\). With \(\phi=2\pi d/N\), the four rows become
\[
(1,\sqrt2,0),\quad(1,\sqrt2\cos\phi,\sqrt2\sin\phi),\quad
(1,q\sqrt2,0),\quad(1,q\sqrt2\cos\phi,q\sqrt2\sin\phi).
\]
For \(-1<c<1\), rotate the last two coordinate axes so that the nonconstant parts of the two spatial rows become \((\sqrt{1+c},\sqrt{1-c})\) and \((\sqrt{1+c},-\sqrt{1-c})\). Summing and differencing the corresponding two sensor outputs orthogonally shows that the Gram matrix is unitarily equivalent to the direct sum of the scalar \(\eta(c)=2(1+q^2)(1-c)\) and
\[
2\begin{pmatrix}
2&(1+q)\sqrt{1+c}\\
(1+q)\sqrt{1+c}&(1+q^2)(1+c)
\end{pmatrix}.
\]
The latter has trace \(\mathcal T(c)\) and determinant \(4(1-q)^2(1+c)\), proving the spectral formula. Continuity extends it to \(c=\pm1\). Its smaller eigenvalue is positive exactly when \(c>-1\) and \(q\ne1\); the decoupled eigenvalue is positive exactly when \(c<1\). One time level gives only two observations in a three-dimensional space, proving temporal minimality.

To optimize, \(\eta(c)\) is strictly decreasing. The smaller root \(\mu_-(c)\) of \(u^2-\mathcal T(c)u+4k(1+c)=0\) is strictly increasing on \([-1,1]\). Indeed, for \(u_0=2k/h\), substitution into this quadratic gives the negative, \(c\)-independent value \(-4k(1+q)^2/h^2\). Thus \(\mu_-(c)<u_0<\mu_+(c)\), and implicit differentiation gives
\[
\mu_-'(c)=\frac{4k-2h\mu_-(c)}{\mu_+(c)-\mu_-(c)}>0.
\]
At \(c=-1\) one has \(\mu_-=0<\eta\), while at \(c=1\) one has \(\eta=0<\mu_-\). Consequently \(\min\{\eta,\mu_-\}\) increases strictly to a unique crossing, then decreases strictly. Substituting \(\eta=2h(1-c)\) into the quadratic equation for \(\mu_-\), and simplifying, gives the stated quadratic in \(c\). Its constant term is negative, so it has exactly one positive root. Its values at \(c=1/2\) and \(c=1\) are, respectively, \(-q(q^3+q+6)/2<0\) and \(2(1-q)^2>0\), establishing the asserted root interval.

At \(q=0\) the positive quadratic root is exactly \(c=1/2\), and at \(q=1\) it is \(c=1\); continuity gives the first limiting angle. For the second, write \(q=1-\varepsilon\) and \(c=1-a\varepsilon^2+O(\varepsilon^3)\) in the same quadratic. The coefficient of \(\varepsilon^2\) is \(2-12a\), hence \(a=1/6\). Taylor expansion of \(\cos\) and \(h=1+q^2\) gives the remaining sharp asymptotics. Finally, strict unimodality implies that a maximum over any ordered cosine grid must occur immediately on either side of the continuous maximizer; reflection \(d\leftrightarrow N-d\) preserves all data. Since \(c_*(q)\uparrow1\) as \(q\uparrow1\) and \(c_1<1\), nearest-neighbor optimality eventually follows.

## Verification

Run `python CHECK.py` with `numpy>=1.24`. The checker independently constructs the four-by-three heat-sampling matrix from graph Fourier modes, obtains its Gram eigenvalues numerically, and compares them to the closed formulas for every cycle order from 5 through 90, every distinct representative sensor spacing, and five positive damping ratios. It also verifies the quadratic crossing and exact finite-grid bracketing rule, and samples the short-time asymptotic. These finite checks are corroboration only; the infinite-order statements follow from the proof.

## Relationship to prior work

Bulai, Cabrelli, Cordero, Molter and Saliani (2026) define graph Paley–Wiener dynamical frames and derive their finite-graph analysis matrices and sharp frame bounds in terms of singular values, emphasizing numerical sensor placement on paths. Aldroubi, Bailey, Krishtal, Miller and Petrosyan (2024) establish general dynamical observability criteria and numerical sensor-placement approaches under a different mean-square-error objective. A published sharp finite-cycle result for two sensors treats **spectrally demixed** outputs, in which separate Laplacian eigenspaces have been isolated; its bounds and optimal placement do not determine the smallest singular value of the four **raw, unweighted** time samples. In particular, the optimal raw heat-sampling cosine depends nontrivially on \(q\) and lies strictly above \(1/2\), whereas its demixed analogue is independent of heat time. The displayed eigenvalue crossing and migration law are the particular new conclusions not stated in the inspected sources.

## Limitations

The result does not optimize the sum of reciprocal eigenvalues, higher-bandwidth recovery, nonuniform time weights, or more than two observation sites. The continuous-angle optimizer is a relaxation; the exact finite-cycle answer requires the adjacent-grid comparison specified above. A general graph-frame theorem allows a direct construction of the present finite matrix, but does not itself give this explicit optimization. Publication priority has not been independently established, and differently indexed optimal-design work remains a residual literature risk.

## References

1. I. M. Bulai, C. Cabrelli, E. Cordero, U. Molter, S. Saliani, *Dynamical Sampling in Graph Paley–Wiener Spaces*, arXiv:2609.25472, first submitted September 21, 2026. https://arxiv.org/abs/2609.25472
2. A. Aldroubi, V. Bailey, I. Krishtal, B. Miller, A. Petrosyan, *Reconstructing Graph Signals from Noisy Dynamical Samples*, arXiv:2411.12670, first submitted November 19, 2024. https://arxiv.org/abs/2411.12670
3. *Sharp spectral-demixed two-sensor frame bounds on finite cycles*, publicly accessible mathematical finding, October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-spectral-demixed-two-sensor-frame-bounds-on-finite-cycles--b03d8e4c7818
