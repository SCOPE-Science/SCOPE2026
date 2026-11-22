# A logarithmic re-preparation frontier for genuine multipartite GHZ entanglement

## Finding
For every integer \(n\geq3\), an \(n\)-qubit GHZ state subject to independent spontaneous emission of rate \(\gamma>0\) per qubit and collective Poisson re-preparation of rate \(r>0\) has a unique stationary genuine-multipartite-concurrence transition. With \(a=r/\gamma\), define
\[
R_n(a)=\frac{n+2a}{4}\frac{\Gamma(n+1)}{\Gamma(n+a+1)}\sum_{b=1}^{n-1}\sqrt{\frac{\Gamma(a+b)\Gamma(a+n-b)}{\Gamma(b+1)\Gamma(n-b+1)}}.
\]
There exists exactly one \(a_n>0\) such that \(R_n(a_n)=1\). Stationary genuine multipartite concurrence is positive exactly when \(a>a_n\), and zero when \(0<a\leq a_n\). Moreover,
\[
a_n=\frac{\log n-\tfrac12\log\log n+\log(\sqrt{2\pi\log2}/4)}{\log 2}+o(1)\quad(n\to\infty).
\]
For \(n=2\), stationary two-qubit concurrence is positive for every \(a>0\); there is no positive transition.

## Assumptions and scope
The reset state is \(|G_n\rangle=(|0\rangle^{\otimes n}+|1\rangle^{\otimes n})/\sqrt2\). Between reset events each qubit independently obeys zero-temperature amplitude damping with generator \(\gamma[\sigma_-\rho\sigma_+-(\sigma_+\sigma_-\rho+\rho\sigma_+\sigma_-)/2]\). A common Poisson clock of rate \(r\) instantaneously replaces the complete system state by \(|G_n\rangle\langle G_n|\). There is no Hamiltonian, thermal pumping, local reset, or dephasing. Genuine multipartite concurrence denotes the convex-roof concurrence for multiqubit X matrices as exactly characterized in Rafsanjani et al. (2012).

## Proof
**Stationary state.** Regeneration at the last full reset gives the unique stationary state
\[
\rho_{n,a}=r\int_0^\infty e^{-rt}{\cal E}_t^{\otimes n}(|G_n\rangle\langle G_n|)\,dt.
\]
The amplitude-damping survival parameter \(Q=e^{-\gamma t}\) under the stationary reset-age law has density \(a q^{a-1}\) on \((0,1)\). Every computational-basis word with exactly \(b\) excitations has diagonal weight
\[
p_b=\tfrac a2 B(a+b,n-b+1)\quad(1\le b\le n),\qquad p_0=\tfrac12+\tfrac a2 B(a,n+1),
\]
and the sole offdiagonal pair has amplitude \(c=\langle0^n|\rho_{n,a}|1^n\rangle=a/(n+2a)\). Thus the state is an X matrix, with complementary-word diagonal populations \(p_b,p_{n-b}\).

**Exact concurrence and uniqueness.** The exact X-matrix genuine multipartite concurrence theorem gives
\[
C_{\rm GM}(n,a)=2\max\left\{0,\frac{a}{n+2a}-\frac12\sum_{b=1}^{n-1}\binom nb\sqrt{p_b p_{n-b}}\right\}
=\frac{2a}{n+2a}\max\{0,1-R_n(a)\}.
\]
Here the sum counts complementary bit-string pairs exactly once after its factor \(1/2\). For each summand of \(R_n\), logarithmic differentiation yields
\[
\frac{2}{n+2a}-\frac12\left(\sum_{j=b}^{n}\frac1{a+j}+\sum_{j=n-b}^{n}\frac1{a+j}\right)<0,
\]
for every \(a>0\), \(1\le b\le n-1\), \(n\ge2\). Indeed the sum has \(n+2\) terms, each at least \(1/(a+n)\), and \((n+2)/[2(a+n)]\ge2/(n+2a)\); strictness holds because some denominators are smaller than \(a+n\). Consequently \(R_n\) decreases strictly. Directly, \(R_2(a)=1/(a+2)\). For \(n\ge3\),
\[
R_n(0+)=\frac n4\sum_{b=1}^{n-1}\frac1{\sqrt{b(n-b)}}\ge\frac{n}{2\sqrt{n-1}}>1,
\]
where the last bound uses the two endpoint terms. Also \(R_n(a)\to0\) as \(a\to\infty\), since each complementary mixed population vanishes while \(c\to1/2\). The intermediate-value theorem gives one and only one positive threshold.

**Size asymptotics.** Uniform Gamma-ratio estimates for \(a=O(\log n)\), applied on \(b/n\) away from the endpoints, followed by beta-integral tail bounds, imply
\[
R_n(a)=\frac n4 B\left(\frac{a+1}{2},\frac{a+1}{2}\right)(1+o(1))
=\frac n4\,2^{-a}\sqrt{\frac{2\pi}{a}}(1+o(1))
\]
uniformly for \(a\) between any two positive constant multiples of \(\log n\). For clarity: the summand is uniformly \((b(n-b))^{(a-1)/2}(1+O(a^2/\min(b,n-b)))\) on a central region; the beta distribution with parameter \((a+1)/2\) concentrates exponentially near \(1/2\), making the excluded endpoint contribution negligible. Monotonicity and the last equation first bracket \(a_n\) between \((1-\delta)\log_2 n\) and \((1+\delta)\log_2 n\), for any fixed \(\delta>0\), and then yield the displayed logarithmic expansion by taking logarithms at \(R_n(a_n)=1\). This is an asymptotic equivalence, not an exact finite-size formula.

## Verification
The accompanying standalone script `check.py` computes the complete Lindblad-reset stationary state from the \(4^n\)-dimensional linear generator for small \(n\), independently reconstructs the beta-integral density matrix, verifies normalization and positivity, evaluates the exact X-matrix concurrence expression and threshold monotonicity, and compares large-size thresholds with the proved asymptotic law. It returned `PASS 413 assertions`. These finite checks corroborate the preceding proof rather than proving the all-size statements.

## Relationship to prior work
Rafsanjani et al. (2012) prove the exact concurrence formula for arbitrary multiqubit X matrices and study ordinary finite-time amplitude-damping trajectories, but do not provide the Poisson-GHZ re-preparation transition or its large-size logarithmic frontier. Wald et al. (first public 2024-10-15) develop stochastic resetting of few-qubit unitary evolution, rather than the independently amplitude-damped collective re-preparation process analyzed here. Other existing studies of GHZ amplitude-damping controls and collective reset purity address different operations and observables; no general uniqueness or logarithmic size law is obtained by applying their stated results directly. The X-state concurrence theorem is essential prior work, not claimed new.

## Limitations
The result establishes positive genuine-multipartite concurrence for one exact family, not a general characterization of noisy multipartite entanglement. The reset prepares a genuinely entangled pure GHZ state and is a nonlocal resource; it does not create entanglement using only local operations. The asymptotic relation applies to integer \(n\to\infty\), not as an error-certified formula at fixed \(n\). Equivalent previously published re-preparation calculations, including those not indexed under the terminology used here, remain possible and warrant independent priority review.

## References
1. S. M. Hashemi Rafsanjani, M. Huber, C. J. Broadbent and J. H. Eberly, *Genuinely multipartite concurrence of N-qubit X matrices*, Physical Review A **86**, 062303 (2012), https://arxiv.org/abs/1208.2706, https://doi.org/10.1103/PhysRevA.86.062303.
2. S. Wald et al., *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, first posted 2024-10-15, https://arxiv.org/abs/2410.11497.
