# Sharp fixed-zealot switching law for nonlinear voter dynamics

## Finding

Consider the homogeneous complete-graph nonlinear \(q\)-voter model with exactly one inflexible supporter of each of two opinions and \(S\) changeable voters. For each **fixed integer** \(q\geq2\), let \(\tau_S\) be the first time, starting with all changeable voters supporting opinion B, at which all changeable voters support opinion A. The dynamics use the exact voter-selection and with-replacement unanimity rule specified below. Then

\[
\boxed{\displaystyle
\mathbb E\tau_S\sim C_q\,S^{-(q-2)/2}2^{(q-1)S},\qquad
C_q=\frac{2^{q+1}}{\sqrt{q-1}}\left(\frac2\pi\right)^{(q-2)/2},
\quad S\longrightarrow\infty.}
\]

In particular, for \(q=2\), the mean is asymptotic to \(8\cdot2^S\); for \(q=3\), it is asymptotic to \(16\cdot4^S/\sqrt{\pi S}\). These are sharp asymptotics, including their leading constants, for the **fixed-count** zealot regime; the source's analysis of switching times does not give these constants. The exact finite-population mean also has a finite binomial sum given below.

## Assumptions and scope

There are \(N=S+2\) individuals, where \(S\geq2\) is an integer. Exactly one permanently supports A, exactly one permanently supports B, and the other \(S\) are changeable. At each opportunity, choose one of the \(N\) individuals uniformly. If it is changeable, draw \(q\) neighbors **independently with replacement** from the other \(N-1\) individuals. The chosen voter adopts the neighbors' opinion if all \(q\) agree, otherwise does not change. Time is normalized so these opportunities occur at rate one; self-loops from unsuccessful opportunities are included by thinning. This produces a continuous-time count chain \(X(t)\) on \(\{0,\ldots,S\}\), where \(X(t)\) counts changeable A-supporters.

For \(0\le k\le S\), the exact jump rates are

\[
\lambda_k=\frac{(S-k)(k+1)^q}{(S+2)(S+1)^q},
\qquad
\mu_k=\frac{k(S-k+1)^q}{(S+2)(S+1)^q},
\]

where \(\mu_0=\lambda_S=0\). Both endpoint states are **nonabsorbing** in the original model; the first hitting time of \(S\) is calculated by making \(S\) absorbing only for that stopping problem. The limit fixes \(q\) while \(S\) increases. It does not cover \(q\) growing with \(S\), zealot proportions bounded away from zero, or heterogeneous unanimity group sizes.

## Proof

Let \(r=q-1\ge1\), \(b_{S,k}=\binom Sk\), \(c_S=(S+2)(S+1)^q\), and \(w_k=b_{S,k}^{-r}\). Directly from the two jump rates,

\[
\frac{\lambda_k}{\mu_{k+1}}=
\left(\frac{k+1}{S-k}\right)^r
=\frac{w_{k+1}}{w_k}.
\]

Hence \(\{w_k\}\) are unnormalized reversible stationary masses. They are strictly positive, so the chain is irreducible. Write \(u_i=\mathbb E_i\tau_S\), with \(u_S=0\). The backward equations are \(-1=\lambda_i(u_{i+1}-u_i)+\mu_i(u_{i-1}-u_i)\) for \(0\le i<S\). Set \(d_i=u_i-u_{i+1}\), so \(\lambda_i d_i-\mu_i d_{i-1}=1\), with \(\mu_0d_{-1}=0\). Multiplication by \(w_i\) and reversibility telescope to

\[
 w_i\lambda_i d_i=\sum_{j=0}^i w_j.
\]

Summing \(d_i\) from \(i=0\) to \(S-1\) proves the exact identity

\[
\boxed{\displaystyle
\mathbb E_0\tau_S=c_S\sum_{k=0}^{S-1}
\frac{\binom Sk^{q-1}}{(S-k)(k+1)^q}
\left(\sum_{j=0}^{k}\binom Sj^{1-q}\right).}
\tag{1}
\]

All terms are finite and positive; this is valid at every integer \(S\ge2\) and \(q\ge2\).

The inner sum is uniformly close to one. For \(S\ge4\), since \(r\ge1\),

\[
1\le\sum_{j=0}^k b_{S,j}^{-r}
\le1+\sum_{j=1}^{S-1}b_{S,j}^{-1}
\le1+\frac2S+\frac{S-3}{\binom S2}
=1+O(S^{-1}),
\quad 0\le k<S.
\tag{2}
\]

Therefore (1) is asymptotic to \(c_S\) times the same outer sum without the inner factor.

For fixed \(r\ge1\), Stirling's formula and Gaussian localization of the central binomial coefficients yield

\[
\sum_{k=0}^{S}\binom Sk^r
\sim 2^{rS}\left(\frac{2}{\pi S}\right)^{r/2}
\sqrt{\frac{\pi S}{2r}}.
\tag{3}
\]

For clarity, writing \(k=S/2+y\sqrt S\) gives the central approximation \(\binom Sk\sim 2^S\sqrt{2/(\pi S)}\exp(-2y^2)\); the resulting Riemann sum evaluates \(\int_{-\infty}^{\infty}\exp(-2ry^2)\,dy=\sqrt{\pi/(2r)}\). The tails outside \(\lvert k-S/2\rvert\le S^{2/3}\) are exponentially small relative to (3), by standard binomial concentration (or elementary exponential bounds for coefficient ratios), even after multiplication by the polynomial rate denominators.

On that central window, uniformly,

\[
\frac{c_S}{(S-k)(k+1)^q}=2^{q+1}(1+o(1)),
\]

because \(c_S/S^{q+1}\to1\). Off the window, the weighted contribution is negligible by the preceding exponential bound and the fact that the rate-denominator factors grow at most polynomially in \(S\). Inserting (2) and (3) into (1) therefore gives

\[
\mathbb E_0\tau_S\sim
2^{q+1}\,2^{rS}\left(\frac2{\pi S}\right)^{r/2}
\sqrt{\frac{\pi S}{2r}}
=\frac{2^{q+1}}{\sqrt{q-1}}
\left(\frac2\pi\right)^{(q-2)/2}
S^{-(q-2)/2}2^{(q-1)S},
\]

which proves the stated law. The derivation also shows explicitly why the parameter regime \(Z_+=Z_-=1\) must not be replaced by a positive fixed zealot density when taking the limit.

## Verification

Run `python3 checker.py` with Python 3 and no external dependencies. Its exact-rational finite-state checks form the jump generator independently and solve the absorbing-state linear equations by Gaussian elimination, then compare with identity (1). It also checks each detailed-balance ratio and prints stable numerical ratios of finite exact sums to the claimed limit for \(S=30,60,120,240\) and \(q=2,3,4,5\). It reports **260 passed checks**. Those finite tests verify the generator algebra and provide numerical diagnostics; the infinite asymptotic is proved analytically above, not by finite enumeration.

## Relationship to prior work

Mobilia's 2015 original paper [1], notably Sections II, IV, and V.A, defines exactly this nonlinear voter chain and gives its birth/death rates and full reversible stationary distribution. It also studies mean switching times using a large-population backward Fokker–Planck approximation and reports approximately exponential growth at low zealotry. The **model, exact stationary law, and qualitative exponential switching phenomenon are prior results**, not new claims here. The distinction in the present result is the exact finite birth–death first-passage expression and its **sharp all-fixed-\(q\) asymptotic leading factor** in the singular regime of one zealot per opinion, which the inspected Section V.A does not compute.

Mellor, Mobilia and Zia [2] study a heterogeneous two-type nonlinear voter system with unequal unanimity sizes and a nonequilibrium stationary state, not the homogeneous two-zealot birth–death passage problem. Nakajima and Masuda [3] study zealot effects on evolution in two-strategy games and fixation with zealots committed to one side, rather than symmetric two-sided switching. These related sources do not imply the stated exact prefactor through their announced results. The mathematical derivation itself uses standard reversible birth–death passage equations and central-binomial asymptotics; it is a new application and sharp evaluation of those tools, not a claim to have invented them.

## Limitations

The source model is an idealized, completely mixed binary social imitation mechanism. Fixed zealot **counts** are essential; using positive fixed zealot **densities** yields a different large-population problem. The leading factor depends on the rate-one global voter-selection time convention; adopting a rate-one clock per individual multiplies the mean by \(1/N\). No claim is made about the full hitting-time distribution, mixing, nonhomogeneous networks, empirical voting behavior, or uniformity when \(q\) grows. Originality is based on inspected sources and mathematical-record searches; uninspected historical treatments of this singular weak-zealotry limit remain a priority risk.

## References

[1] M. Mobilia, *Nonlinear q-voter model with inflexible zealots*, Physical Review E **92**, 012803 (2015), arXiv:1506.04911 (first publicly posted June 16, 2015), https://arxiv.org/abs/1506.04911 ; accepted-version full text https://eprints.whiterose.ac.uk/id/eprint/87063/1/QvotersZealots_Mobilia_PRE_Accepted_12June2015.pdf .

[2] A. Mellor, M. Mobilia, and R. K. P. Zia, *Characterization of the Nonequilibrium Steady State of a Heterogeneous Nonlinear q-Voter Model with Zealotry*, EPL **113**, 48001 (2016), arXiv:1601.03766, https://arxiv.org/abs/1601.03766 .

[3] Y. Nakajima and N. Masuda, *Evolutionary dynamics in finite populations with zealots*, Journal of Mathematical Biology **70**, 465–484 (2015), arXiv:1308.2273, https://doi.org/10.1007/s00285-014-0770-2 .
