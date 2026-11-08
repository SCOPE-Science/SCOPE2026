# Quenched covariance fluctuations in a fair random bootstrap walk

## Finding

Let \((\beta_j)_{j\geq0}\) be independent fair Bernoulli variables and let \((\xi_i)_{i\geq1}\) be independent symmetric signs, independent of the coefficients. Define
\[
S_t=\sum_{i=1}^{t}\mathbf1_{\{\xi_i=-1\}},\qquad
\omega_j=(-1)^{\sum_{r=0}^j\binom jr\beta_r},\qquad
A_j=\sum_{r=0}^{j-1}\omega_r,\quad A_0=0.
\]
All exponents are interpreted modulo two. Put \(\zeta_0=1\), \(\zeta_t=\omega_{S_t}\) for \(t\geq1\), and form two adapted walks by \(X_n=\sum_{i=1}^n\xi_i\) and \(Y_n=\sum_{i=1}^n\zeta_{i-1}\xi_i\). Their predictable cross-covariation is \(H_n=\sum_{t=0}^{n-1}\zeta_t\).

**Theorem.** For almost every coefficient realization \(\beta\), conditional on \(\beta\), the diffusively normalized pair \((X_{\lfloor nt\rfloor},Y_{\lfloor nt\rfloor})/\sqrt n\), \(0\leq t\leq1\), converges in the Skorokhod space \(D([0,1],\mathbb R^2)\) to two independent standard Brownian motions. More sharply, for the same almost every coefficient realization,
\[
\left(\frac{H_{\lfloor nt\rfloor}-2A_{\lfloor nt/2\rfloor}}{\sqrt n}\right)_{0\leq t\leq1}
\ \Longrightarrow\ (B_t)_{0\leq t\leq1}
\]
under the conditional walk law, where \(B\) is standard Brownian motion. Unconditionally, \((H_{\lfloor nt\rfloor}/\sqrt n)_{t\in[0,1]}\) converges to Brownian motion with variance rate **three**, rather than one. The environment-dependent centering satisfies
\[
\limsup_{n\to\infty}\frac{2A_{\lfloor n/2\rfloor}}{\sqrt{n\log\log n}}=2,
\qquad
\liminf_{n\to\infty}\frac{2A_{\lfloor n/2\rfloor}}{\sqrt{n\log\log n}}=-2
\]
almost surely in the environment. Consequently, the uncentered conditional laws of \(H_n/\sqrt n\) are not tight along the full sequence. At every positive integer horizon, \(\mathbb EH_n=1\) and
\[
\operatorname{Var}(H_n)=3n-7+2^{3-n}.
\]

The model is the **fair-coefficient subcase** of the inclusion-induced, cardinality-grouped, time-invariant randomization in Hamza and Tournier (2026). Its conditional invariance principle is a special-case answer to their explicitly unresolved quenched question, not a result for all elliptic Bernoulli coefficients.

## Assumptions and scope

All coefficient and increment families are mutually independent across the specified indices and between families. The original walk increments are \(\pm1\) with equal probabilities; every coefficient \(\beta_j\) has parameter exactly \(1/2\). The coefficient environment is sampled once and held fixed for all times. The first recycling sign is set to one to match the original bootstrap convention. The floor in the centering is \(\lfloor nt/2\rfloor\) at time \(\lfloor nt\rfloor\); the one-index discrepancy is bounded and immaterial. The Gaussian assertions are functional weak limits, not uniform finite-sample normal approximations. Conditional statements hold for a single environment-null-set independent of the fixed time interval \([0,1]\).

## Proof

**1. An invertible parity transform produces independent scenery.** Write \(c_j=\sum_{r=0}^j(\binom jr\bmod2)\beta_r\) in the field of two elements. The matrix \((\binom jr\bmod2)_{j,r\geq0}\) is lower triangular with diagonal entries one. Every finite truncation is therefore invertible over this field, so \((c_0,\ldots,c_m)\) consists of independent fair bits. Accordingly, the \(\omega_j=(-1)^{c_j}\) are independent symmetric signs. They are independent of the original increments. The representation for \(\zeta_t\) is precisely the inclusion-induced cardinality formula, since each subset of a size-\(S_t\) set contributes one corresponding coefficient.

**2. A pathwise martingale–scenery decomposition.** Put \(B_i=\mathbf1_{\{\xi_i=-1\}}\) and, for each positive integer \(n\), let
\[
D_n=\sum_{t=0}^{n-1}\omega_{S_t},\qquad
M_n=\sum_{t=0}^{n-1}(1-2B_{t+1})\omega_{S_t}.
\]
For each step the scenery partial sum changes by \(A_{S_{t+1}}-A_{S_t}=B_{t+1}\omega_{S_t}\). Hence, with no approximation,
\[
\boxed{D_n=2A_{S_n}+M_n,\qquad H_n=D_n+1-\omega_0.}
\]
Fix any deterministic scenery of signs. Conditional on the increments already exposed, \((1-2B_{t+1})\omega_{S_t}\) is a fresh symmetric sign. Iteration of conditional probabilities proves that these martingale increments are **independent fair signs**. Their complete sequence has the same law for every fixed scenery, so \(M\) is also independent of the whole random scenery \(\omega\) under the joint probability law. In particular, the standard functional central limit theorem applies conditionally and unconditionally to \(M\).

**3. First-order quenched normality of the bootstrap pair.** For almost every scenery, the strong law gives \(A_j/j\to0\). For each fixed scenery, the Bernoulli strong law gives \(S_n/n\to1/2\), and the martingale strong law gives \(M_n/n\to0\). The exact decomposition thus shows \(H_n/n\to0\) almost surely under the conditional walk law, and also \(\max_{k\le n}|H_k|/n\to0\). Both \(X\) and \(Y\) have predictable conditional squared increments equal to one; their predictable cross-increment product is \(\zeta_{i-1}\). Bounded vector martingale increments satisfy the Lindeberg condition. The functional martingale central limit theorem with the preceding uniformly vanishing cross-covariation therefore gives two independent Brownian coordinates. This proves the previously unresolved quenched conclusion for the stated fair subcase.

**4. A uniform random-index replacement.** For almost every iid-sign scenery, and every sufficiently large dyadic integer \(N\),
\[
\max_{0\leq u,v\leq2N:\,|v-u|\leq N^{2/3}}|A_v-A_u|\leq N^{5/12}.
\]
Indeed, for an interval of length at most \(N^{2/3}\), Hoeffding's inequality bounds the probability of an absolute increment exceeding \(N^{5/12}\) by \(2\exp(-N^{1/6}/2)\). There are at most \((2N+1)^2\) pairs of endpoints, so Borel–Cantelli applies along dyadic \(N\). Replacing \(N\) by the next larger dyadic integer extends the resulting \(o(\sqrt N)\) bound to all \(N\). On the walk event \(\max_{k\le N}|S_k-k/2|\le N^{2/3}\), the discrepancy \(\sup_{k\le N}|A_{S_k}-A_{\lfloor k/2\rfloor}|\) is therefore \(o(\sqrt N)\). A bounded-increment maximal Hoeffding/Azuma inequality makes the complement of this walk event tend to zero (in fact exponentially in \(N^{1/3}\)). Thus for almost every fixed scenery,
\[
\frac1{\sqrt N}\max_{k\le N}|A_{S_k}-A_{\lfloor k/2\rfloor}|\xrightarrow{\mathbb P_\xi}0.
\]
The decomposition and the conditional Donsker theorem for \(M\) prove the centered quenched functional limit.

**5. Annealed variance and separation of fluctuations.** Since \(M\) and \(\omega\) are independent, the environment partial-sum process satisfies \(2A_{\lfloor nt/2\rfloor}/\sqrt n\Longrightarrow\sqrt2\,B^{(e)}_t\), independently of \(M_{\lfloor nt\rfloor}/\sqrt n\Longrightarrow B^{(d)}_t\). The random-index replacement gives the annealed limiting process \(\sqrt2 B^{(e)}+B^{(d)}\), of variance rate three. For exact finite-sample variance, with \(t\geq s\), independence of the scenery implies \(\mathbb E[\omega_{S_s}\omega_{S_t}]=\Pr(S_t=S_s)=2^{-(t-s)}\). Therefore
\[
\operatorname{Var}(D_n)=n+2\sum_{h=1}^{n-1}(n-h)2^{-h}=3n-4+2^{2-n}.
\]
As \(H_n=D_n+1-\omega_0\) and \(\operatorname{Cov}(D_n,\omega_0)=\sum_{t=0}^{n-1}2^{-t}=2(1-2^{-n})\), the claimed mean and variance follow.

**6. Failure of an uncentered quenched second-order limit.** The classical two-sided law of the iterated logarithm for iid symmetric signs yields the displayed \(\pm2\) centering limits. The centered quenched Gaussian family is tight, but its deterministic-for-fixed-environment mean-shift \(2A_{\lfloor n/2\rfloor}/\sqrt n\) has subsequences diverging to both signs. The uncentered conditional laws of \(H_n/\sqrt n\) thus escape to plus and minus infinity in conditional probability along respective subsequences. This does **not** contradict first-order quenched Brownian independence of the walk pair, for which the relevant scale is \(H_n/n\).

## Verification

The standalone `verify.py` checks that the finite Pascal parity transform is bijective through eight coefficients; checks the exact martingale decomposition for all sign sceneries and Bernoulli paths through eight steps; checks the exact rational mean and variance at each horizon; and checks the pathwise bijection from coin paths to martingale-increment paths for every fixed scenery through six steps. Executing `python verify.py` produced `PASS: 670,074 exact integer/rational assertions; n <= 8 for variance, n <= 6 for conditional iid transform`. These finite tests do not certify any infinite limit. The arguments in Steps 3–6 establish the limits using standard strong laws, concentration bounds, the martingale functional CLT, Donsker's theorem, and the law of the iterated logarithm. All auxiliary source files needed to replay the tests accompany this result.

## Relationship to prior work

Hamza and Tournier (2026, Section 4.3, Proposition 11 and Corollary 12) give **annealed** Brownian convergence for the more general cardinality-grouped, time-invariant inclusion-induced randomization with elliptic coefficients, but explicitly leave the corresponding **quenched** assertion open. The current result specializes to independent fair coefficients and gives the quenched conclusion plus the precise order-\(\sqrt n\) fluctuation split and the necessity of random centering at that scale. It does not establish quenched convergence for general biased independent coefficients.

Collevecchio, Hamza, Shi and Williams (2022) prove a general necessary-and-sufficient covariation criterion for a **specified** bootstrap rule; the new proof supplies the previously missing almost-every-environment covariation verification for this particular random rule. Guillotin-Plantard and Poisat (2013) develop quenched limit theorems for random walks in random scenery. Their renewal-process theorem requires strictly positive jumps, whereas the scenery-index process used here has Bernoulli \(0/1\) jumps and geometric holding times. The renewal-reward/coboundary viewpoint and the need for environment-dependent centering also have broad precedents, so the generic random-scenery CLT mechanism is **not claimed as new**. The specific Pascal-parity identification, bootstrap-walk quenched consequence, exact variance-rate split, and accompanying no-uncentered-limit statement are the asserted contributions. Standard tools could lead to an independent derivation; historical priority beyond the inspected sources is not certified.

## Limitations

The result is for independent fair coefficient bits, not all uniformly elliptic parameters or more general level-dependent coefficients. It does not provide optimal finite-sample distributional rates, nor an independent mathematical audit. The LIL statement is about environmental partial sums and does not describe all conditional subsequential limit laws when a different centering is used. A broader historical theorem about lazy monotone random walks in iid scenery could imply portions of the second-order assertions even without the original bootstrap terminology. The primary theorem is proved analytically, not by the finite checker.

## References

1. K. Hamza and L. Tournier, *Are random random walks normal?* arXiv:2610.01658v1 (first public version October 1, 2026), https://arxiv.org/html/2610.01658, especially Introduction and Sections 2 and 4.3.
2. A. Collevecchio, K. Hamza, M. Shi and R. J. Williams, *Limit theorems and ergodicity for general bootstrap random walks*, Electronic Journal of Probability **27** (2022), Article 92; arXiv:2010.16000, https://arxiv.org/abs/2010.16000.
3. N. Guillotin-Plantard and J. Poisat, *Quenched central limit theorems for random walks in random scenery*, Stochastic Processes and their Applications **123** (2013), 1348–1367; arXiv:1210.6135, https://arxiv.org/abs/1210.6135, especially Theorem 1.1 and its strictly positive-increment hypothesis.
4. A. Bowditch, *Central limit theorems for biased randomly trapped random walks on \(\mathbb Z\)*, Stochastic Processes and their Applications **129** (2019), 740–770, DOI 10.1016/j.spa.2018.03.017 (related random-environment centering, a different model).
