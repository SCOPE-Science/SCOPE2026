# A unique two-bath tuning makes a dissipative Gaussian dimer exactly Ornstein–Uhlenbeck to one observer

## Finding

For every \(a>k>0\) and \(T_1,T_2>0\), consider the stationary two-temperature diffusion defined below. **Its entire scalar path law \((X_t)_{t\in\mathbb R}\) is a stationary equilibrium Ornstein–Uhlenbeck law if and only if**

\[
\boxed{\frac{T_2}{T_1}=\frac{2a+k}{k}.}
\]

At this unique admissible tuning, for every finite collection of times, the corresponding joint distributions of \(X\) coincide exactly with those of

\[
 dZ_t=-(a-k)Z_t\,dt+\sqrt{2T_1}\,dB_t,
 \qquad Z\text{ stationary}.
\]

Nonetheless, the coupled system has a nonzero steady heat flux \(J_1=kT_1\) delivered into the first (colder) bath and positive total entropy-production rate

\[
\boxed{\sigma=\frac{2ak}{2a+k}>0.}
\]

In fact, fixing an arbitrary visible stationary Ornstein–Uhlenbeck law with relaxation \(\lambda>0\) and noise intensity \(T_1>0\), the choice \(a=\lambda+k\) and \(T_2=T_1(3+2\lambda/k)\), for any \(k>0\), preserves **that same complete visible path law**, while \(\sigma=2k(\lambda+k)/(3k+2\lambda)\) increases strictly from \(0\) to infinity. The entire visible passive trajectory therefore cannot bound the physical entropy-production rate. The invisibility is not robust to intervention: the impulse response to a force on \(X\) is \(e^{-at}\cosh(kt)\), not \(e^{-(a-k)t}\).

## Assumptions and scope

Let \(W_1,W_2\) be independent standard two-sided Brownian motions. For all \(a>k>0\) and \(T_1,T_2>0\), let \((X,Y)\) be the unique stationary solution of

\[
\begin{aligned}
 dX_t&=(-aX_t+kY_t)dt+\sqrt{2T_1}\,dW_{1,t},\\
 dY_t&=(kX_t-aY_t)dt+\sqrt{2T_2}\,dW_{2,t}.
\end{aligned}
\]

Both position coordinates have even time-reversal parity; friction coefficients and Boltzmann's constant are set to one. The conservative potential is \(U(x,y)=\frac a2(x^2+y^2)-kxy\), which is strictly confining. The heat flux from bath one is the stationary Stratonovich power \(J_1=\mathbb E[(-aX+kY)\circ\dot X]\); positive values indicate heat delivered by the system into bath one. The total entropy-production rate is \(\sigma=J_1/T_1+J_2/T_2\), where \(J_2=-J_1\). The stationary path-law claim concerns **passive measurement without externally applied forces**, not conditional laws when the full hidden state is observed, nonstationary preparation, or driven responses.

## Proof

**1. Unique stationary Gaussian law and exact two-mode covariance.** Set \(A=\begin{psmallmatrix}a&-k\\-k&a\end{psmallmatrix}\), \(D=\operatorname{diag}(T_1,T_2)\). Both eigenvalues \(a-k\) and \(a+k\) are strictly positive, so the stationary stochastic convolution exists uniquely and is a centered jointly Gaussian process. The stationary covariance \(S\) solves \(AS+SA=2D\). Direct substitution yields

\[
\begin{aligned}
 S_{11}&=\frac{2a^2T_1-k^2T_1+k^2T_2}{2a(a^2-k^2)},\\
 S_{12}&=\frac{k(T_1+T_2)}{2(a^2-k^2)},\\
 S_{22}&=\frac{2a^2T_2-k^2T_2+k^2T_1}{2a(a^2-k^2)}.
\end{aligned}
\]

With \(s\ge0\), stationarity and independence of future Wiener increments give \(\operatorname{Cov}((X_s,Y_s),(X_0,Y_0))=e^{-As}S\). Diagonalizing \(A\) in its sum and difference modes gives

\[
 C_X(s):=\mathbb E[X_sX_0]
 =b_-e^{-(a-k)s}+b_+e^{-(a+k)s},
\]
\[
 b_- =\frac{T_1(2a-k)+kT_2}{4a(a-k)}>0,
 \qquad b_+=\frac{T_1(2a+k)-kT_2}{4a(a+k)}.
\]

**2. Necessary and sufficient complete path-law equality.** A centered nonsingular stationary scalar Gaussian Markov process has \(C(s+t)C(0)=C(s)C(t)\) for all \(s,t\ge0\): the conditional covariance of its future and past given its present must vanish. Conversely, a continuous positive covariance satisfying this multiplicative equation is a single decaying exponential, and the associated stationary Gaussian law is an Ornstein–Uhlenbeck law. For two distinct positive rates and \(b_- >0\), direct expansion shows that the multiplicative identity can hold at all positive \(s,t\) only when \(b_+=0\). Solving this linear equation in the positive temperatures gives uniquely \(T_2/T_1=(2a+k)/k\). Substitution then gives \(S_{11}=T_1/(a-k)\), so

\[
 C_X(s)=\frac{T_1}{a-k}e^{-(a-k)|s|}\qquad(s\in\mathbb R).
\]

Because the full system and its projection are Gaussian, this covariance and its zero mean determine **all** scalar finite-dimensional distributions, establishing equality of stationary continuous-path probability laws. For every other positive temperature ratio the nonzero fast coefficient violates the Gaussian Markov criterion, even though every one-time marginal remains Gaussian. This is an exact all-lag statement, not an inference from finite sampling.

**3. Hidden heat dissipation and unbounded invisible family.** For \(F_x=-aX+kY\), the Itô–Stratonovich conversion and the Gaussian stationary moment equations give

\[
 J_1=\mathbb E[F_x^2]+T_1\partial_xF_x
 =\mathbb E[F_x^2]-aT_1
 =\frac{k^2(T_2-T_1)}{2a},\qquad J_2=-J_1.
\]

Thus

\[
 \sigma=J_1\left(\frac1{T_1}-\frac1{T_2}\right)
 =\frac{k^2(T_2-T_1)^2}{2aT_1T_2}.
\]

This is also obtained independently from the exact stationary Fokker–Planck current: \(Q=D-AS=\frac{k(T_2-T_1)}{2a}\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}\), and \(\sigma=\operatorname{tr}(S^{-1}Q^{\mathsf T}D^{-1}Q)\). At the tuning, \(J_1=kT_1\), \(Q_{12}=T_1\), and \(\sigma=2ak/(2a+k)\). Fixing \(\lambda=a-k>0\) and \(T_1>0\), the tuning demands \(T_2=T_1(3+2\lambda/k)\). Therefore

\[
 \sigma(k)=\frac{2k(k+\lambda)}{3k+2\lambda},\quad
 \sigma'(k)=\frac{2(3k^2+4k\lambda+2\lambda^2)}{(3k+2\lambda)^2}>0,
\]

and its limits as \(k\downarrow0\) and \(k\to\infty\) are \(0\) and \(+\infty\), respectively. Every finite \(k>0\) has finite positive parameters. The visible law is unchanged throughout this family.

**4. Active-response discriminator.** A small deterministic impulse applied additively to the \(X\)-equation changes the conditional mean by the exact linear response \(R(s)=(e^{-As})_{11}=e^{-as}\cosh(ks)\). The scalar equilibrium process inferred from passive data would instead predict \(R_{\mathrm{OU}}(s)=e^{-(a-k)s}\). For every \(s>0\) and \(k>0\), \(\cosh(ks)<e^{ks}\), so \(R(s)<R_{\mathrm{OU}}(s)\). Thus passive path-law equality does not imply an equilibrium response or vanishing hidden heat flow.

## Verification

The standalone `verify.py` (Python 3 with SymPy, NumPy, and SciPy) independently solves the stationary Lyapunov equation; checks the covariance amplitudes, Fokker–Planck current and heat-bath entropy rate as rational symbolic identities; verifies the tuned cancellation and strict dissipation; and tests off-tuning Gaussian Markov failure, force response, and the fixed-law family on deterministic parameter samples. Run `python verify.py` in the same directory. A replay passed 3,267 symbolic identities and numerical assertions. The all-positive-real-parameter result follows from the preceding exact arguments; numerical tests are corroboration, not an infinite proof.

An exact checkpoint is \((a,k,T_1,T_2)=(2,1,1,5)\). Then \(S=\begin{psmallmatrix}1&1\\1&3\end{psmallmatrix}\), \(C_X(s)=e^{-|s|}\), \(J_1=1\), and \(\sigma=4/5\), while the forced response is \(e^{-2s}\cosh(s)\).

## Relationship to prior work

Godrèche and Luck [1] give the general multivariate Gaussian Ornstein–Uhlenbeck Lyapunov, current, response and entropy-production formulas, including a general two-dimensional case. These standard ingredients are not claimed as novel; specializing them to the specified symmetric drift already permits derivation of the algebra above. However, their inspected complete article does not state a unique positive **bath-ratio calibration giving equality of complete scalar Gaussian path laws**, an exhaustive one-coordinate Markov iff condition, or an unbounded entropy-production family with the *same* full scalar law.

Cerasoli, Dotsenko, Oshanin and Rondoni [2] analyze this two-temperature harmonic gyrator and time-dependent effective temperatures, focusing particularly on a vanishingly cold bath. Their inspected complete preprint does not derive the finite positive-temperature path-law equality criterion or fixed-visible-law dissipation fiber. Ginot et al. [3] resolve multiple response eigenmodes in a harmonic probe–bath model but not this stationary two-temperature stochastic cancellation. Busiello, Ciarchi and Di Terlizzi [4] prove thermodynamic consequences of integrating out coupled variables; they do not classify the present exact passive-Markovian tuning.

Two closely related publicly archived switching-harmonic-trap results [5, 6] establish **covariance-only** Ornstein–Uhlenbeck mimicry in a non-Gaussian scalar process, where higher moments still distinguish the model. They therefore cannot imply the complete Gaussian path-law equality or the same-path-law unbounded heat dissipation established here. A published block-skew Gaussian thermal multiplier [7] has different antisymmetric drift coupling and yields no scalar trajectory criterion for the symmetric Brownian gyrator. Their general linear-algebra techniques can overlap, but neither the object-specific tuning nor its implications are supplied by the compared claims.

## Limitations

The claim is about the exact stationary law under ideal passive observations. If the bath temperature, coupling or hidden coordinate is independently known or manipulated, the hidden dissipation can be inferred; the active response explicitly distinguishes the systems. The unbounded family holds within the overdamped linear stochastic model, not as a physically realizable arbitrary-heat laboratory claim. At any fixed off-tuning parameters the scalar process is non-Markovian. The theorem does not extend automatically to non-Gaussian forcing, underdamped coordinates, time-varying baths, or nonstationary initial conditions. Classical general OU formulas are sufficient to reproduce the calculations by specialization; an unlocated equivalent older scalar-projection result remains a substantive publication-priority risk. Independent validation has not been performed.

## References

1. C. Godrèche and J.-M. Luck, *Characterising the nonequilibrium stationary states of Ornstein-Uhlenbeck processes*, arXiv:1807.00694 (first public 2018-07-02), https://arxiv.org/html/1807.00694v2 .
2. S. Cerasoli, V. Dotsenko, G. Oshanin and L. Rondoni, *Time-dependence of the effective temperatures of a two-dimensional Brownian gyrator with cold and hot components*, arXiv:2011.03124 (first public 2020-11-05), https://arxiv.org/abs/2011.03124 .
3. F. Ginot et al., *Recoil experiments determine the eigenmodes of viscoelastic fluids*, arXiv:2204.02369 (first public 2022-04-05), https://arxiv.org/abs/2204.02369 .
4. D. M. Busiello, M. Ciarchi and I. Di Terlizzi, *Unraveling active baths through their hidden degrees of freedom*, arXiv:2310.00620 (first public 2023-10-01), https://arxiv.org/abs/2310.00620 .
5. *Exact equilibrium-like covariance with hidden dissipation in a two-state fluctuating harmonic trap*, publicly archived 2026-10-25, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-exact-equilibrium-like-covariance-with-hidden-dissipation-in-a-t--0b2306697c41/RESULT.md .
6. *A complete equilibrium-covariance camouflage manifold for a switching harmonic trap*, publicly archived 2026-11-02, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-a-complete-equilibrium-covariance-camouflage-manifold-for-a-swit--8f817ade8710/RESULT.md .
7. *Universal two-temperature multiplier for bipartite skew Ornstein–Uhlenbeck networks*, publicly archived 2026-11-08, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-universal-two-temperature-multiplier-for-bipartite-skew-ornstein--68bc5baaf3bc/RESULT.md .
