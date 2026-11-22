# A sharp return-probability signature of hidden nematic memory in a planar four-state walk

## Finding

Consider a discrete-time nearest-neighbor walk \(S_n\) on \(\mathbb Z^2\) whose direction is one of \(\{+e_1,-e_1,+e_2,-e_2\}\). The direction is initially uniform. Conditional on the previous direction, the next direction is unchanged or exactly reversed with probability \((1+q)/4\) each, and turns clockwise or counterclockwise with probability \((1-q)/4\) each, where \(-1<q<1\). Then, for every fixed such \(q\), as positive integers \(m\) tend to infinity,

\[
\Pr_q\{S_{2m}=0\}=\frac{1}{\pi m}\left[1+\frac{3q-1}{4(1-q)m}+\frac{25q^2+2q+1}{32(1-q)^2m^2}+O_q(m^{-3})\right].
\]

The leading return asymptotic and the entire two-time displacement covariance are independent of \(q\); the first relative finite-time return correction instead changes sign exactly at \(q=1/3\). At this unique parameter its cancellation exposes the explicit positive next term:

\[
\Pr_{1/3}\{S_{2m}=0\}=\frac{1}{\pi m}\left[1+\frac{5}{16m^2}+O(m^{-3})\right].
\]

In particular, defining \(c(q)=\lim_{m\to\infty}m(\pi m\Pr_q\{S_{2m}=0\}-1)\), the hidden nematic parameter is identifiable from this return correction by

\[
q=\frac{4c(q)+1}{4c(q)+3}.
\]

These are return-at-a-given-time probabilities, not first-return probabilities.

## Assumptions and scope

The process is exactly the symmetric, zero-polar-memory and zero-chirality subfamily of the four-heading square-lattice reorientation model, with even angular mode \(q\) and microscopic weights given above. Steps occur at integer times, have unit length, and have no waiting periods or translational Brownian noise. The initial orientation is stationary, uniform over four headings. The theorem holds pointwise for each fixed \(-1<q<1\); its remainder is not claimed uniform as \(q\to\pm1\).

Write \(A_j\in\{1,2\}\) for the axis chosen at step \(j\), and \(\epsilon_j\in\{-1,+1\}\) for its sign, so \(S_n=\sum_{j=1}^n\epsilon_j e_{A_j}\). The axis chain has transition probability \(p=(1+q)/2\) of retaining its axis, and \(1-p\) of switching. Conditional on all axes, the signs are independent unbiased Rademacher variables. Consequently \(\mathbb E S_n=0\), \(\operatorname{Cov}(S_n)=(n/2)I_2\), and \(\mathbb E[(S_{t+1}-S_t)(S_{s+1}-S_s)^T]=0\) for distinct nonnegative integers \(s,t\), independent of \(q\).

## Proof

**1. Exact tilted transfer.** With \(c_i=\cos k_i\), \(D(k)=\operatorname{diag}(c_1,c_2)\), and

\[
T=\begin{pmatrix}p&1-p\\1-p&p\end{pmatrix},\quad K(k)=D(k)T,\quad\pi=\tfrac12(1,1)^T,
\]

the characteristic function is \(\phi_n(k)=(1,1)K(k)^n\pi\). Fourier inversion gives

\[
\Pr\{S_n=0\}=(2\pi)^{-2}\int_{[-\pi,\pi]^2}\phi_n(k)\,dk.
\]

The characteristic polynomial of \(K(k)\) is \(\lambda^2-p(c_1+c_2)\lambda+q c_1c_2\). Near zero the simple dominant eigenvalue \(\lambda_+(k)\) equals one at zero; the other \(\lambda_-(0)=q\). The amplitude of the dominant eigenvalue in \(\phi_n\) is

\[
A(k)=\frac{(c_1+c_2)/2-\lambda_-(k)}{\lambda_+(k)-\lambda_-(k)}.
\]

**2. Spectral localization.** Since every underlying four-direction transition has strictly positive probability for \(-1<q<1\), equality in the Perron-Frobenius bound on the modulus of a Fourier-twisted transition requires all four step phases to agree. Thus spectral radius one occurs only at \(k=(0,0)\) and \(k=(\pi,\pi)\), modulo \(2\pi\). At the latter point the matrix is the negative of its value at zero, so its contribution is identical when \(n\) is even. On the complement of small neighborhoods of these two points the integral is exponentially small. The second eigenvalue is uniformly smaller in modulus locally. Standard analytic perturbation and Laplace expansion therefore apply in the two contributing neighborhoods.

**3. Local Taylor coefficients.** Write \(k=z/\sqrt n\), \(r_2=z_1^2+z_2^2\). Expansion of the quadratic eigenvalue equation and of the amplitude yields

\[
\log\lambda_+(z/\sqrt n)=-\frac{r_2}{4n}+\frac{L_4(z)}{n^2}+\frac{L_6(z)}{n^3}+O_q(n^{-4}(1+|z|^8)),
\]

\[
L_4(z)=\frac{(7q-1)(z_1^4+z_2^4)-6(q+1)z_1^2z_2^2}{96(1-q)},
\]

\[
L_6(z)=\frac{r_2\big((31q-1)(z_1^4+z_2^4)-(46q+14)z_1^2z_2^2\big)}{1440(1-q)},
\]

and

\[
A(z/\sqrt n)=1-\frac{q(z_1^2-z_2^2)^2}{16(1-q)^2n^2}+O_q(n^{-3}(1+|z|^6)).
\]

The Taylor remainders are uniform on growing regions \(|z|\le n^\eta\) for sufficiently small fixed \(\eta>0\), and Gaussian domination controls the remaining part of each saddle neighborhood. Let \(G_1,G_2\) be independent \(N(0,2)\) variables and \(A_4(z)=-q(z_1^2-z_2^2)^2/[16(1-q)^2]\). Gaussian integration gives

\[
\mathbb E[L_4(G)]=\frac{3q-1}{2(1-q)},\qquad
\mathbb E[L_6(G)+\tfrac12L_4(G)^2+A_4(G)]=\frac{25q^2+2q+1}{8(1-q)^2}.
\]

The Gaussian integral at each saddle is \(1/(\pi n)\); the two equal contributions lead to

\[
\Pr\{S_n=0\}=\frac{2}{\pi n}\left[1+\frac{3q-1}{2(1-q)n}+\frac{25q^2+2q+1}{8(1-q)^2n^2}+O_q(n^{-3})\right]
\]

for even \(n\). Substituting \(n=2m\) proves the main expansion. Solving \(3q-1=0\) yields the unique cancellation at \(q=1/3\); substitution gives \(5/16\). The first coefficient is strictly increasing in \(q\), with derivative \(1/[2(1-q)^2]>0\), so solving for \(q\) yields the displayed identifiability formula.

## Verification

The accompanying standalone `check_return.py` computes finite-time return probabilities by an independent dynamic program over the number of horizontal steps and the last axis, followed by exact central-binomial return weights for each axis. It checks the ordinary square-lattice simple-walk case \(q=0\) against \(\binom{2m}{m}^2/16^m\); numerically compares the two asymptotic correction coefficients for five distinct memory parameters; and tests the vanishing first coefficient and emerging second term at \(q=1/3\). Executing `python check_return.py` returned `PASS: 16 finite-time/asymptotic consistency checks`. These finite numerical tests support the algebra but are not used to establish the infinite asymptotic statement. The Fourier and Gaussian expansions above supply that proof.

## Relationship to prior work

Sherf, Uhlig, Wójcik, Metzler, Roichman and Kalz (2026) introduced the full four-direction active chiral walk, established its orientation Fourier parameters, and derived velocity autocorrelation, mean-square displacement, diffusion and odd diffusion. The result here specializes to its physically meaningful polar-memory-free nematic parameter and resolves finer return probabilities that its two-time transport formulas do not imply. Classical work of Gillis (1955), Roerdink and Shuler (1985) and Iossif (1986) treats correlated walks and return asymptotics generally; those general foundations are not claimed as new. The present contribution is the explicit two-term return expansion, sharp cancellation at \(q=1/3\), and inversion of hidden axis memory from a subleading return observable.

## Limitations

This is a stationary-initial-heading, strictly positive four-direction transition family with fixed \(-1<q<1\). It does not cover the nonergodic endpoints \(q=\pm1\), arbitrary polar persistence or chirality, nonstationary initial headings, or first-return hitting laws. The asymptotic is pointwise in \(q\), and its inverse parameter formula assumes exact large-time return probabilities, not a finite-sample estimator. A potentially relevant 1986 correlated-walk return paper was accessible only through its abstract; it may contain implicitly overlapping general asymptotic formulae. The contribution is not independently audited.

## References

1. N. Sherf, J. Uhlig, J. Wójcik, R. Metzler, Y. Roichman and E. Kalz, *The active chiral random walk*, arXiv:2611.14446, first publicly posted 2026-11-10, https://arxiv.org/abs/2611.14446.
2. J. Gillis, *Correlated random walk*, *Mathematical Proceedings of the Cambridge Philosophical Society* **51** (1955), 639–651, https://doi.org/10.1017/S0305004100030711.
3. J. B. T. M. Roerdink, *A note on the asymptotic properties of correlated random walks*, *Journal of Applied Probability* **22** (1985), 951–956, https://doi.org/10.2307/3213964; see also J. B. T. M. Roerdink and K. E. Shuler, *Asymptotic properties of multistate random walks. I. Theory*, *Journal of Statistical Physics* **40** (1985), 205–228.
4. G. Iossif, *Return probabilities for correlated random walks*, *Journal of Applied Probability* **23** (1986), 201–207, https://doi.org/10.2307/3214129.
