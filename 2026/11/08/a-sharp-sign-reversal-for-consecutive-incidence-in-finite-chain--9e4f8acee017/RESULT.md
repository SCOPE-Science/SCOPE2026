# A sharp sign reversal for consecutive incidence in finite chain-binomial epidemics

## Finding

The sign of the correlation between two consecutive incidence counts is not fixed by the infection mechanism. In an exactly specified finite-population chain-binomial SIR epidemic, early rounds of new infections are positively correlated at low transmission probability and negatively correlated at high transmission probability, with a unique sharp transition and a population-dependent asymptotic location.

Write \(N=n+1\), with \(n\ge2\), and put \(q=1-p\), \(a=q+\mu p\), and \(H=1-p^2\). The exact identity is

\[
\operatorname{Cov}(C_1,C_2)=npq\left[a q(1+np)H^{n-2}-1\right]. \tag{1}
\]

For \(n\ge3\), or for \(n=2\) with \(\mu>0\), exactly one \(p_*(n,\mu)\in(0,1)\) satisfies

\[
(q+\mu p)q(1+np)(1-p^2)^{n-2}=1. \tag{2}
\]

The covariance is positive below this threshold, zero at it, and negative above it. When \(n=2\) and \(\mu=0\), the covariance is negative for every \(p\in(0,1)\). At any fixed \(n\) where a positive threshold exists, \(p_*(n,\mu)\) increases strictly with \(\mu\).

The asymptotic threshold, uniformly for \(0\le\mu\le1\), is

\[
n p_*(n,\mu)^2=\tfrac12\bigl(\log n+\log\log n-\log 2\bigr)+o(1),\qquad n\longrightarrow\infty. \tag{3}
\]

Thus \(p_*\sim\sqrt{\log n/(2n)}\) and, in contact-intensity parametrization, \(\beta_*=N p_*\sim\sqrt{N\log N/2}\). Conversely, when \(\beta\) is fixed and \(p=\beta/N\), \(\operatorname{Cov}(C_1,C_2)\to\beta^2>0\). The high-transmission reversal is a finite-susceptible-depletion effect that disappears from the ordinary early-epidemic branching limit.

## Assumptions and scope

The population contains exactly \(N=n+1\) individuals at time zero, of whom one is infectious and \(n\) are susceptible; there are no previously recovered persons and no imports, births, or reinfections. The process is observed for two synchronous discrete updates with constant \(p\in(0,1)\) and \(\mu\in[0,1]\). At each update, conditional on the current susceptible and infectious counts \((S_t,I_t)\), each susceptible independently becomes infected with probability \(1-(1-p)^{I_t}\). Each currently infectious person independently recovers with probability \(\mu\). Conditional on the starting state, infection draws and recovery draws are independent, and newly infected people enter the infectious class after that update rather than transmitting during it.

Equivalently, with the integer-valued number of newly infected people \(C_{t+1}\) and recovered people \(R_{t+1}\),

\[
C_{t+1}\mid(S_t,I_t)\sim\operatorname{Bin}\bigl(S_t,1-(1-p)^{I_t}\bigr),\quad
R_{t+1}\mid(S_t,I_t)\sim\operatorname{Bin}(I_t,\mu),
\]
\[
S_{t+1}=S_t-C_{t+1},\qquad I_{t+1}=I_t+C_{t+1}-R_{t+1}.
\]

These are the finite-population transitions (5)–(6) in Boudreau and St-Onge (2026). In particular, the two quantities compared in (1) are **incidence**, not the overlapping infectious-prevalence counts. All limits in (3) hold uniformly over recovery parameters in the closed interval \([0,1]\); no epidemiological time-continuum limit is asserted.

## Proof

**Exact covariance.** Put \(C=C_1\). The first incidence satisfies \(C\sim\operatorname{Bin}(n,p)\), and the first recovery indicator \(R=R_1\sim\operatorname{Bern}(\mu)\) is independent of \(C\). After the first update, \(S_1=n-C\) and \(I_1=1-R+C\). Thus

\[
\mathbb E[C_2\mid C=c,R=r]=(n-c)\bigl(1-q^{1-r+c}\bigr).
\]

Since \(\mathbb E[q^{1-R}]=(1-\mu)q+\mu=q+\mu p=a\), conditioning only on \(C\) gives

\[
\mathbb E[C_2\mid C]=(n-C)(1-aq^C). \tag{4}
\]

Standard binomial factorial-moment identities, obtained by singling out one or two distinct Bernoulli indicators, give

\[
\begin{aligned}
\mathbb E[n-C]&=nq,\\
\mathbb E[C(n-C)]&=n(n-1)pq,\\
\mathbb E[(n-C)q^C]&=nq(q+pq)^{n-1}=nqH^{n-1},\\
\mathbb E[C(n-C)q^C]&=n(n-1)pq^2(q+pq)^{n-2}=n(n-1)pq^2H^{n-2}.
\end{aligned} \tag{5}
\]

Inserting (5) in (4) yields

\[
\begin{aligned}
\mathbb E[C_1]&=np,\\
\mathbb E[C_2]&=nq(1-aH^{n-1}),\\
\mathbb E[C_1C_2]&=n(n-1)pq(1-aqH^{n-2}).
\end{aligned} \tag{6}
\]

Subtracting the product of the means and using \(nH-(n-1)q=q(1+np)\) proves (1), including the complete dependence on the recovery parameter.

**Existence and uniqueness of the sign boundary.** Define

\[
\Phi(p)=[1-(1-\mu)p](1-p)(1+np)(1-p^2)^{n-2},\qquad L(p)=\log\Phi(p).
\]

For \(n\ge2\), every factor is positive on \((0,1)\). Each logarithm of a positive affine factor is concave and \(\log(1+np)\) is strictly concave; also \(\log(1-p^2)\) is strictly concave on that interval. Hence \(L''(p)<0\). In addition,

\[
L(0)=0,\qquad L'(0)=n-2+\mu,\qquad \lim_{p\uparrow1}L(p)=-\infty. \tag{7}
\]

When \(n-2+\mu>0\), strict concavity means \(L\) rises above zero, has just one positive zero, and stays negative beyond it. Equation (1) gives the claimed signs. When \(n=2\) and \(\mu=0\), the derivative at zero is zero; strict concavity gives \(L(p)<0\) for every positive \(p\). For any fixed \(p>0\), \(\Phi(p)\) increases strictly with \(\mu\), so the unique crossing point, wherever defined, also increases strictly with \(\mu\). In particular, at \(n=2,\mu=1\), the crossing is exactly \(p_*=1/2\).

**Sharp large-population boundary.** Uniformly in \(\mu\in[0,1]\), let \(p_c(n)=c\sqrt{\log n/(2n)}\) for fixed \(c>0\). Directly expanding the four logarithms, using \(n p_c(n)^3\to0\), gives

\[
L(p_c(n))=\frac{1-c^2}{2}\log n+\frac12\log\log n+O_c(1) \tag{8}
\]

uniformly in \(\mu\). Therefore for each fixed \(0<c_-<1<c_+\) and sufficiently large \(n\), \(L(p_{c_-}(n))>0>L(p_{c_+}(n))\). Uniqueness of the zero proves

\[
p_*\sim\sqrt{\log n/(2n)}
\]

uniformly over recovery parameters. At that root set \(x=np_*^2\). The preceding estimate gives \(x\sim\tfrac12\log n\) and \(p_*\to0\), while the exact logarithmic equation simplifies, uniformly in \(\mu\), to

\[
0=\log(1+np_*)-np_*^2+o(1)=\tfrac12\log(nx)-x+o(1).
\]

Consequently \(x=\tfrac12\log n+\tfrac12\log x+o(1)\), and \(\log x=\log\log n-\log2+o(1)\). This proves the sharper expansion (3). All error terms are uniform because the only recovery-dependent log term \(\log[1-(1-\mu)p_*]\) is bounded in magnitude by \(-\log(1-p_*)=o(1)\).

**Branching-process comparison.** If \(\beta>0\) is fixed and \(p=\beta/N\), then \(np\to\beta\), \(q\to1\), \(a\to1\), and \(H^{n-2}\to1\). Formula (1) immediately implies \(\operatorname{Cov}(C_1,C_2)\to\beta^2\). This agrees with the Poisson branching-process calculation and proves that the negative regime cannot appear for fixed \(\beta\) and all sufficiently large \(N\).

## Verification

The standalone standard-library script `checks/verify.py` constructs the full joint two-round law by summing over the first incidence, first recovery, and second incidence. It computes the covariance with exact rational arithmetic, independently of the binomial-moment algebra. It checks (1) on \(54\) combinations of \(n\in\{2,3,4,5,6,7\}\), \(p\in\{1/7,3/5,4/5\}\), and \(\mu\in\{0,1/3,1\}\), and verifies exact sign witnesses and an exact boundary.

For a particularly small witness with \(N=4\), \(\mu=0\), the covariance is exactly \(114669/10000000>0\) at \(p=1/10\), but \(-711/16384<0\) at \(p=1/4\). With \(N=3\) and \(\mu=1\), the exact sign boundary is \(p=1/2\). The numerical sample checks do not prove the all-\(N\) theorem; the algebra and strict-concavity argument above do.

## Relationship to prior work

Boudreau and St-Onge (2026, section 2.1) define the exact chain-binomial SIR transitions used here and use them as a point of comparison with branching-process probability generating functions. Their sections 2.2–2.4 address time-series PGFs, joint observable distributions, and horizons for susceptible-depletion discrepancies, but do not present the two-step finite-population covariance or its sharp sign boundary. The present theorem is about that different, exact finite-size observable and gives a sharper dependence criterion than a general observation that susceptible depletion matters.

The CDC's Reed–Frost documentation and classical Reed–Frost theory supply the special \(\mu=1\) transition mechanism, so neither that mechanism nor the basic binomial expectation identities is claimed as new. The finite-population formula, the unique recovery-dependent threshold, its second-order large-size location, and the finite-versus-branching sign contrast are the assessed contribution. Earlier epidemic texts and chain-binomial work could contain equivalent moment formulas under another notation; absence from retrieved sources cannot certify uniqueness.

## Limitations

Only the first two rounds, a single initial infectious person, homogeneous independent contacts, synchronous transmission and recovery, constant parameters, and a closed susceptible population are treated. No claim is made for delayed observation, case under-ascertainment, network heterogeneity, continuous-time infection, or longer-lag incidence covariance. The covariance is across repeated stochastic outbreaks with fixed initial conditions, not a time-average covariance from one observed trajectory. The negative-covariance regime requires contact intensity growing with population size, so it does not contradict the fixed-intensity branching approximation. Scientific comparisons remain subject to possible unindexed equivalent classical chain-binomial calculations, and no independent audit has been conducted.

## References

1. M. C. Boudreau and G. St-Onge, *Probability generating functions for epidemiological time series*, arXiv:2610.17138v1 (first publicly posted 2026-10-12), sections 2.1–2.4 and Supplement S1. https://arxiv.org/abs/2610.17138 . Full HTML consulted at https://arxiv.t3mt.com/html/2610.17138v1 .
2. CDC, *Reed-Frost chain-binomial model descriptions*, https://cdcgov.github.io/reedfrost/chain_binomial/ .
3. J. C. Miller, *A primer on the use of probability generating functions in infectious disease modeling*, *Infectious Disease Modelling* (2018), https://doi.org/10.1016/j.idm.2018.08.001 .
4. *A multi-region discrete time chain binomial model for infectious disease transmission*, preprint 2025, https://www.medrxiv.org/content/10.1101/2025.05.26.25328280v3.full .
