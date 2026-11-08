# Arithmetic blind spots and an optimal two-time heat-sampling delay on cycles

## Finding

Two snapshots of the heat flow on every second vertex of a finite cycle have a sharp arithmetic obstruction and a universal asymptotically optimal separation in time. The initial state can be recovered from both snapshots for positive time exactly when the even cycle length is \(2\pmod4\); lengths divisible by four are unobservable at every positive delay. For reconstructible lengths, the best possible lower frame bound decays like a specified multiple of \(N^{-2}\), and the optimal delay converges to the same positive constant independently of cycle length.

More precisely, for the operator and notation below, if \(N\equiv2\pmod4\), put
\[
d_N=2\sin(\pi/N),\qquad q=e^{-4t},\qquad C_N(t)=\cosh(2d_Nt).
\]
The **sharp squared lower singular value** is
\[
A_N(t)=\frac{1+qC_N(t)-\sqrt{(1+qC_N(t))^2-2q(C_N(t)-1)}}{2}.
\]
The **sharp squared upper singular value**, valid for all even cycle lengths, is
\[
B_N(t)=\frac{3+q^2+\sqrt{(3+q^2)^2-4(1-q)^2}}4.
\]
If \(4\mid N\), \(A_N(t)=0\). Otherwise the lower bound is positive for every \(t>0\), and its maximum is attained at a finite, positive delay. For any maximizing delay \(t_N\),
\[
\lim_{\substack{N\to\infty\\N\equiv2\ (\mathrm{mod}\ 4)}}t_N=\tau,
\qquad
\lim_{\substack{N\to\infty\\N\equiv2\ (\mathrm{mod}\ 4)}}N^2\max_{t>0}A_N(t)
=\frac{4\pi^2\tau^2}{1+e^{4\tau}},
\]
where \(\tau\) is the unique positive root of \(2\tau=1+e^{-4\tau}\). Numerically, \(\tau=0.55442877643927\ldots\) and the limiting coefficient is \(1.19133546764856\ldots\).

## Assumptions and scope

The domain is the finite complex Hilbert space \(\ell^2(\mathbb Z/N\mathbb Z)\) with its unnormalized counting-measure norm \(\|f\|^2=\sum_{j=0}^{N-1}|f(j)|^2\); the codomain uses the corresponding sum of squared measurement magnitudes over both time snapshots. The integer \(N\) is even and at least four. The unweighted cycle Laplacian and alternate-vertex restriction are
\[
(L_N f)(j)=2f(j)-f(j-1)-f(j+1),\qquad(Pf)(r)=f(2r),\quad 0\le r<N/2,
\]
with vertex indices understood modulo \(N\). For each \(t>0\) define the \(N\)-component measurement map
\[
\mathcal S_{N,t}f=(Pf,Pe^{-tL_N}f).
\]
The sharp inequalities are \(A_N(t)\|f\|^2\le\|\mathcal S_{N,t}f\|^2\le B_N(t)\|f\|^2\), with equality possible at both ends; the quantities are eigenvalues of \(\mathcal S_{N,t}^*\mathcal S_{N,t}\), not singular values themselves. The choice of combinatorial rather than normalized Laplacian is essential for the numerical value of the optimal delay.

## Proof

**Fourier alias blocks.** The characters \(u_k(j)=N^{-1/2}e^{2\pi i kj/N}\) diagonalize the Laplacian with eigenvalue \(\lambda_k=2-2\cos(2\pi k/N)\). On even vertices \(u_k\) and \(u_{k+N/2}\) agree. After unitary Fourier transforms on input and on each observation snapshot, the measurement map splits as an orthogonal direct sum of \(N/2\) square matrices
\[
Q_\delta=\frac1{\sqrt2}
\begin{pmatrix}1&1\\e^{-(2-\delta)t}&e^{-(2+\delta)t}\end{pmatrix},
\qquad\delta=2\left|\cos\frac{2\pi k}{N}\right|,
\quad0\le k<N/2.
\]
If the cosine is negative the two columns are simply interchanged; this preserves singular values. Thus no dimensional factor is suppressed by the Fourier normalization.

**Monotonicity of the extremal spectral levels.** Write \(M_\delta=\sqrt2 Q_\delta\) and \(\mu_-(\delta)\le\mu_+(\delta)\) for the eigenvalues of \(M_\delta^*M_\delta\). Their trace and determinant are
\[
T(\delta)=2+2q\cosh(2\delta t),\qquad
D(\delta)=2q\bigl(\cosh(2\delta t)-1\bigr),\qquad q=e^{-4t}.
\]
For \(\delta>0\), \(T'(\delta)=D'(\delta)>0\). The unit vector \((1,-1)/\sqrt2\) gives \(\mu_-(\delta)\le(e^{-(2-\delta)t}-e^{-(2+\delta)t})^2/2\le1/2<1\); the unit vector \((1,1)/\sqrt2\) gives \(\mu_+(\delta)\ge2>1\). Differentiating the characteristic polynomial therefore yields
\[
\mu_-'(\delta)=\frac{T'(\delta)(1-\mu_-(\delta))}{\mu_+(\delta)-\mu_-(\delta)}>0,
\qquad
\mu_+'(\delta)=\frac{T'(\delta)(\mu_+(\delta)-1)}{\mu_+(\delta)-\mu_-(\delta)}>0.
\]
The lower and upper eigenvalues of each actual measurement block are \(\mu_-/2\) and \(\mu_+/2\). The smallest sampled \(\delta\) equals zero for \(4\mid N\), since \(k=N/4\) then aliases two equal Laplacian eigenvalues, and equals \(d_N=2\sin(\pi/N)\) for \(N\equiv2\pmod4\). The largest \(\delta\) equals two, attained by \(k=0\). Substitution into the two roots of \(z^2-Tz+D=0\) yields precisely the claimed expressions for \(A_N\) and \(B_N\). In particular, for positive delay, \(A_N=0\) exactly in the first parity class.

**Asymptotically optimal delay.** In the nonblind parity class, \(d_N\to0\), and Taylor expansion of the exact lower eigenvalue, uniformly for \(t\) in compact subsets of \([0,\infty)\), gives
\[
\frac{A_N(t)}{d_N^2}\longrightarrow
h(t)=\frac{t^2}{1+e^{4t}}.
\]
It remains to justify optimizing this convergence, rather than exchanging a supremum with an uncontrolled pointwise limit. The Rayleigh test vector \((1,-1)/\sqrt2\) in the worst alias block gives
\[
0\le A_N(t)\le e^{-4t}\sinh^2(d_Nt)
\le d_N^2t^2e^{-(4-2d_N)t}.
\]
For all \(N\equiv2\pmod4\) with \(N\ge6\), \(d_N\le1\), so \(A_N(t)/d_N^2\le t^2e^{-2t}\). That common upper envelope tends to zero as \(t\downarrow0\) and as \(t\to\infty\). On the other hand \(h(t)>0\) for positive \(t\). Thus all maximizing delays for sufficiently large admissible \(N\) lie in a fixed compact subinterval of \((0,\infty)\), and compact-uniform convergence applies.

Differentiation gives that the unique positive critical point of \(h\) satisfies
\[
2t=1+e^{-4t}.
\]
The left side strictly increases and the right side strictly decreases, so the critical point \(\tau\) is unique; since \(h\) vanishes at both endpoints of \((0,\infty)\), it is the strict global maximizer. Therefore every maximizing-delay sequence converges to \(\tau\) and \(\max_t A_N(t)/d_N^2\to h(\tau)\). Finally, \(Nd_N\to2\pi\) yields \(N^2\max_tA_N(t)\to4\pi^2h(\tau)\), as asserted. This uses analytic estimates for arbitrarily large \(N\), not finite enumeration.

## Verification

The self-contained checker `check_cycle_heat.py` constructs the full discrete Fourier heat operator, the two-snapshot measurement matrix, and its Gram eigenvalues. It compares both sharp endpoints with the formulas for every even \(N\) from 4 through 44 at five time delays (105 direct comparisons), and tests optimal-delay scaling for six additional lengths up to 502. Execute `python check_cycle_heat.py` in an environment with Python, NumPy, and SciPy. The reference numerical output reports `CYCLE_TWO_TIME_HEAT_PASS direct_bound_comparisons 105 asymptotic_scales 6`. Direct calculations are corroboration only; the exact identities, parity obstruction, and infinite-size asymptotic are proved above.

## Relationship to prior work

The dynamical-sampling framework concerns reconstruction from evolving, spatially undersampled signals; Christensen, Hasannasab and Stoeva (2018) study iterated-operator frame representations, while Cabrelli, Molter, Paternostro and Philipp (2017) give operator-frame characterizations. Aldroubi and collaborators (2020) study spatiotemporal bandlimited sampling, stability estimates and Fourier blind spots for continuous signal flows. The present finite-cycle theorem makes the arithmetic blind/observable alternative and both sharp frame bounds explicit for two fixed snapshots on alternate vertices, and optimizes the **sharp smallest squared singular value** over continuous delay. The conclusion is not a verbatim restatement of a general frame-existence condition or a continuous-bandwidth Remez estimate. Comparable exact statements under other graph-normalization or sampling conventions have not been fully excluded.

## Limitations

Only an unweighted even cycle, alternate-vertex sensors, precisely two observation times (one at zero) and the combinatorial heat Laplacian are covered. No assertion is made for odd cycles, unequal sampling patterns, noisy sampling beyond the frame bounds, or arbitrary semigroups. At each finite admissible \(N\), the theorem proves existence but not uniqueness of the optimizing delay; the asymptotic limit applies to all maximizing delays. The literature-priority determination remains provisional without exhaustive specialist comparisons, and no independent mathematical audit has been performed.

## References

- O. Christensen, M. Hasannasab and D. T. Stoeva, *Operator representations of sequences and dynamical sampling*, arXiv:1804.00077 (first posted 30 March 2018); frame-theoretic context.
- A. Aldroubi, K. Gröchenig, L. Huang, P. Jaming, I. Krishtal and J. L. Romero, *Sampling the flow of a bandlimited function*, arXiv:2004.14032 (first posted 29 April 2020); stability and blind-spot context.
- C. Cabrelli, U. Molter, V. Paternostro and F. Philipp, *Dynamical Sampling on Finite Index Sets*, arXiv:1702.03384 (first posted 11 February 2017); operator-frame existence theory.
- *Robust estimation of smooth graph signals from randomized space–time samples*, IMA Journal of Information and Inference (2024), DOI:10.1093/imaiai/iaae012; random graph-observation comparison.
