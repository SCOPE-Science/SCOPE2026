# Parity of the stationary Wigner-positivity interval under Poisson Fock re-preparation

## Finding

Let \(n\ge1\) and \(\alpha=r/\gamma>0\), with re-preparation and loss as defined below. The unique stationary state is number-diagonal with occupations
\[
p_k(\alpha)=\frac{\alpha n!\,\Gamma(\alpha+k)}{k!\,\Gamma(\alpha+n+1)},\qquad k=0,\ldots,n.
\]
Its von Neumann entropy is strictly increasing on \((0,1)\), strictly decreasing on \((1,\infty)\), and has its unique maximum \(\log(n+1)\) at \(\alpha=1\). The set of rates with pointwise nonnegative stationary Wigner function is an initial interval \((0,\alpha_n]\). The endpoint coincides with the entropy maximum, \(\alpha_n=1\), for every odd \(n\); for every even \(n\) it satisfies \(1<\alpha_n<\infty\). The contribution is the all-index separation by parity together with the strict rate dependence of entropy, not the previously documented two-photon cutoff.

## Assumptions and scope

There is one bosonic mode with annihilation operator \(b\), a vacuum reservoir inducing single-photon loss at rate \(\gamma>0\), and instantaneous independent Poisson re-preparation to \(\rho_n=|n\rangle\langle n|\) at rate \(r>0\). The trace-preserving equation is
\[
\dot\rho=\gamma(b\rho b^\dagger-\tfrac12\{b^\dagger b,\rho\})+r(\rho_n\operatorname{tr}\rho-\rho).
\]
A free harmonic rotation does not affect the diagonal stationary state. There is no thermal excitation or selective addition. Wigner positivity means pointwise nonnegativity of the symmetrically ordered Wigner function, not positivity of the Glauber–Sudarshan representation.

## Proof

**Stationary law.** Write \(T_t\) for the pure-loss channel and use time units \(1/\gamma\). For initial \(\rho_n\) the output is binomial thinning with transmission \(u=e^{-t}\), with probabilities \(\binom nk u^k(1-u)^{n-k}\). The age since the last Poisson reset in stationarity has density \(\alpha e^{-\alpha t}\); hence the age mixture uses the transmission density \(\alpha u^{\alpha-1}\,du\) on \((0,1)\). The beta integral gives \(p_k\). For any two initial states, conditional on at least one reset their outputs at time \(t\) agree; the no-reset component has weight \(e^{-\alpha t}\) and its trace distance cannot increase under \(T_t\). This proves uniqueness and attraction of the stationary state.

**Strict entropy monotonicity.** The ratio \(p_{k+1}/p_k=(\alpha+k)/(k+1)\) orders the occupation vector decreasingly for \(\alpha<1\), uniformly for \(\alpha=1\), and increasingly for \(\alpha>1\). For \(a<b\), the ratio \(p_k(b)/p_k(a)\) strictly increases with \(k\), because successive ratios are multiplied by \((b+k)/(a+k)>1\). Since both vectors sum to one, their differences change sign from negative to positive only once, with possible equality at a single index. All proper lower-index cumulative sums therefore strictly decrease as the rate increases. Below \(1\), these are the proper largest-component sums; above \(1\), their complements are the largest-component sums. Strict Schur concavity of entropy proves the two strict monotonicities. At \(1\) the state is uniform on \(n+1\) levels and attains the maximum.

**Rate ordering for Wigner positivity.** Put \(R_a=\int_0^\infty ae^{-at}T_t\,dt\). If \(0<a<b\), then
\[
R_a=\frac{a}{b}R_b+\left(1-\frac ab\right)R_aR_b.
\]
Indeed, the composed channel integrates \(T_{t+v}\) by the semigroup law; the convolution of the two exponential densities is \(ab(e^{-at}-e^{-bt})/(b-a)\). Loss and its exponential averages preserve Wigner positivity by scaled positive Gaussian convolution. Thus if \(R_b(\rho_n)\) is Wigner-positive then so is \(R_a(\rho_n)\). With \(z=4|w|^2\), the Wigner function is \((2/\pi)e^{-z/2}P_{n,\alpha}(z)\), where \(P_{n,\alpha}(z)=\sum_{k=0}^n(-1)^kp_k(\alpha)L_k(z)\) and \(L_k\) denotes the ordinary Laguerre polynomial. Continuity at each fixed \(z\ge0\) shows that any finite positive upper endpoint is included.

**Wigner positivity at equal rates.** The mixed input \((n+1)^{-1}\sum_{m=0}^n |m,n-m\rangle\langle m,n-m|\) is the normalized projection onto the total-number-\(n\) subspace. A balanced beam splitter preserves that subspace and the projection; reducing one output therefore gives the uniform single-mode state at \(\alpha=1\). Equivalently this is the mean of the reduced outputs \(\sigma(m,n-m)\) for the individual Fock inputs. Each has nonnegative Wigner function: the reduced balanced output is a scaled convolution of the two input Wigner functions, proportional at a fixed amplitude to the trace overlap of one input with a displaced parity conjugate of the other. This is the uniform mixture construction of Vanbever [1, Lemma 2 and Eq. (30)]. The \(m=0\) output is binomial half-loss, with polynomial \((z/2)^n/n!\), by expanding \(L_k\) and summing the binomial coefficients. Its contribution is strictly positive for \(z>0\), as is the polynomial of the uniform state. At the origin the latter has value \((1+(-1)^n)/(2(n+1))\).

**Parity and the upper bound.** For odd \(n\) the origin value equals
\[
P_{n,\alpha}(0)=\alpha\int_0^1u^{\alpha-1}(1-2u)^n\,du.
\]
Pairing \(u\) and \(1-u\) for \(0<u<1/2\) gives a strictly negative value for every \(\alpha>1\). Together with equal-rate positivity and rate ordering, this proves \(\alpha_n=1\). For even \(n\) the equal-rate polynomial is also strictly positive at the origin. This positivity persists for rates in a neighborhood of \(1\): on a compact \(z\)-interval it follows from a positive minimum and continuity, while for all sufficiently large \(z\) the leading coefficient \(p_n(\alpha)/n!\), uniformly bounded below near \(1\), dominates the lower powers with uniformly bounded coefficients. Hence \(\alpha_n>1\). As \(\alpha\to\infty\), \(p_n\to1\) and the polynomial tends to \((-1)^nL_n\). This nonzero polynomial has a negative value on the positive real axis, since its integral against \(e^{-z}dz\) vanishes for \(n\ge1\). The stationary polynomial is negative there for sufficiently large \(\alpha\), giving a finite upper endpoint. The rate order and endpoint closure finish the proof.

## Verification

The accompanying `checker.py` is an exact finite check using Python and SymPy. It checks occupation normalization and balance, the equal-rate and balanced-loss identities, and rational examples of strict majorization; its two-photon calculation checks the established special case described below. These checks are not an all-index proof. The all-index result follows from the occupation order, semigroup identity, equal-rate positivity, and parity argument above.

## Relationship to prior work

Vanbever [1] proves Wigner positivity of the equally weighted initial Fock mixture. That result is used here at \(\alpha=1\), not claimed as new. Nugmanov, Zunikov and Khalili [2] study the half-transmissivity Wigner threshold for a pure non-Gaussian input subjected to fixed loss. This does not give the sign of the reset-age mixture. Li et al. [3] use cascaded selective photon addition rather than full-state Poisson re-preparation. A separate Poisson-loss result for odd optical cats [4] has the same numerical odd-state boundary but a different family of prepared states.

The separate two-photon renewal-clock record [5] explicitly gives the exponential-clock case \(\alpha^3-\alpha-2=0\). This overlap is exact; publication priority within the shared date is not inferred. For this special case the polynomial is an upward-opening quadratic with minimum \((-\alpha^3+\alpha+2)/[(\alpha+1)^2(\alpha+2)]\) at \(z=2\alpha/(\alpha+1)\); above the cutoff its negativity lies between two positive radial roots, hence on one annulus. This calculation is a check and illustration of the all-index result, not an independent original claim.

## Limitations

No closed form or asymptotic is claimed for the general even-index boundary. The analysis does not address arbitrary renewal laws, nonideal re-preparation, finite reservoir temperature or implementation cost. The precedent comparison does not certify exhaustive historical priority.

## References

1. L. Vanbever, *In Wigner phase space, convolution explains why the vacuum majorizes mixtures of Fock states*, [arXiv:2104.14996](https://arxiv.org/abs/2104.14996), Lemma 2 and Eq. (30).
2. B. Nugmanov, N. Zunikov and F. Ya. Khalili, *Robustness of negativity of the Wigner function to dissipation*, [arXiv:2201.03257](https://arxiv.org/abs/2201.03257), pp. 1–2.
3. S. Li et al., *Autonomous Stabilization of Fock States in an Oscillator against Multiphoton Losses*, [arXiv:2308.08296](https://arxiv.org/abs/2308.08296), pp. 1–2.
4. [*Sharp stationary Wigner negativity onset for Poisson-reprepared odd optical cats*](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-sharp-stationary-wigner-negativity-onset-for-poisson-reprepared--1f1b1bcb8b19).
5. [*A sharp mean-clock threshold for renewal-preserved two-photon Wigner negativity*](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-a-sharp-mean-clock-threshold-for-renewal-preserved-two-photon-wi--0f4bc643e42b), exponential-wait comparison and relationship to prior work.
