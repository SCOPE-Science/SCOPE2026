# Critical survival amplitudes for the open Pelikan random map

## Finding
For the open Pelikan chain at the critical collision of its renewal pole and algebraic singularity, every sufficiently light-tailed initial law has an exact exponential-times-square-root survival law. Let \(0<\varepsilon<1\), \(h=2-\varepsilon\), and set
\[
p=\frac4{4+h^2},\qquad q=1-p=\frac{h^2}{4+h^2},\qquad \lambda=2\sqrt{pq}=\frac{4h}{4+h^2}<1.
\]
These parameters satisfy the critical relation \(4q=p(2-\varepsilon)^2\). For an initial probability \(\mu=(\mu_i)_{i\ge0}\), let \(\Phi(w)=\sum_{i\ge0}\mu_iw^i\). If \(\sum_{i\ge0}\mu_i(2/h+\eta)^i<\infty\) for some \(\eta>0\), then
\[
\boxed{\Pr_\mu(X_n\text{ survives})\sim
\frac{4(1-\varepsilon)}{\varepsilon(2-\varepsilon)}\sqrt{\frac2\pi}\,
\Phi\!\left(\frac2{2-\varepsilon}\right)\,
\frac{\lambda^n}{\sqrt n}.}
\]
In particular, starting from a single state \(i\ge0\), the leading coefficient is multiplied by \((2/h)^i\). The natural initial law from uniform Lebesgue measure on the random interval map has \(\mu_i=2^{-i-1}\). For this law the amplitude simplifies unexpectedly to
\[
\boxed{\Pr_{\mathrm{Leb}}(X_n\text{ survives})\sim
\frac{2}{\varepsilon}\sqrt{\frac2\pi}\,\frac{\lambda^n}{\sqrt n}.}
\]
Thus the critical survival probability is not asymptotic to a positive constant times the bare exponential \(\lambda^n\): it has an additional, explicit inverse-square-root factor.

## Assumptions and scope
The state space is \(\mathbb N_0\) with a cemetery state. At each step from \(i\ge1\), move to \(i-1\) with probability \(p\) and to \(i+1\) with probability \(q\). At state zero, move to state one with probability \(q\); with total probability \(p(1-\varepsilon)\) re-inject to state \(j\ge0\) with conditional geometric probabilities \(2^{-j-1}\); and with probability \(p\varepsilon\) enter the cemetery state. This is the substochastic matrix of Brevitt and Klages [1], with columns as originating states. The event \(X_n\text{ survives}\) means no visit to the cemetery during the first \(n\) transitions. The parameter and moment hypotheses above are fixed as \(n\to\infty\); the claimed asymptotic is not asserted uniformly as \(\varepsilon\to0\) or \(\varepsilon\to1\). The initial law need not be positive at every state.

## Proof
**1. First hits and returns.** Write \(R=\lambda^{-1}=(4+h^2)/(4h)\), so \(R>1\). From state one, the probability generating function of the first hitting time of zero is the unique formal power series \(H(z)\) satisfying \(H=pz+qzH^2\) with \(H(0)=0\). Thus
\[
H(z)=\frac{1-\sqrt{1-4pqz^2}}{2qz}.
\]
By the skip-free property, starting from state \(i\) the corresponding first-hitting generating function is \(H(z)^i\). Starting from zero, the generating function of the first *surviving* return to zero is
\[
F(z)=\frac{p(1-\varepsilon)z}{2-H(z)}+qzH(z).
\]
Indeed, a re-injection to geometric state \(j\) contributes \(p(1-\varepsilon)z\sum_{j\ge0}2^{-j-1}H(z)^j\), while a move to state one contributes \(qzH(z)\). Therefore the generating function of surviving return probabilities at zero is \(G(z)=(1-F(z))^{-1}=\sum_{n\ge0}\Pr_0(X_n=0,\text{alive})z^n\).

**2. Exact survival transform.** Every killing transition occurs from zero, with probability \(p\varepsilon\). The generating function of the probability of being killed *at the next step* from an initial law \(\mu\) is consequently \(p\varepsilon z\Phi(H(z))G(z)\). Summing the loss of survival probability at successive steps gives the identity
\[
\mathcal S_\mu(z):=\sum_{n\ge0}\Pr_\mu(X_n\text{ survives})z^n
=\frac{1-p\varepsilon z\Phi(H(z))G(z)}{1-z}.
\]
This identity initially holds as a formal power series and for sufficiently small complex \(z\). The apparent singularity at \(z=1\) cancels: since \(p>q\), \(H(1)=1\) and \(F(1)=1-p\varepsilon\), hence \(p\varepsilon G(1)=1\) and \(\Phi(1)=1\).

**3. Collision expansion.** Put \(t=\sqrt{1-(z/R)^2}\). On the critical curve, direct substitution yields
\[
H(z)=\frac2h\frac{1-t}{\sqrt{1-t^2}},\qquad
F(z)=1-\frac{h}{2(h-1)}t+O(t^2).
\]
As \(z\to R\) in a slit complex neighborhood,
\[
G(z)=\frac{\sqrt2(h-1)}h(1-z/R)^{-1/2}+O(1).
\]
The elementary identity \(p\varepsilon R/(R-1)=4/\varepsilon\) gives
\[
\mathcal S_\mu(z)=\frac{4\sqrt2(h-1)}{\varepsilon h}
\Phi(2/h)(1-z/R)^{-1/2}+O(1),
\]
where the analytic moment hypothesis ensures \(\Phi(H(z))\) is analytic near \(z=R\).

**4. Dominant singularity and coefficients.** For \(|z|<R\), positivity gives \(|F(z)|\le F(|z|)<1\). On \(|z|=R\), equality \(F(z)=1\) can occur only at \(z=R\), because the positive coefficients at return times one and two force aperiodicity. The second algebraic branch point at \(z=-R\) is subdominant: direct substitution shows \(F(-R)=1/(h+1)<1\), hence \(G\) has no pole there and \(\mathcal S_\mu\) has at worst a square-root *vanishing* singular term. The moment assumption rules out nearer singularities from \(\Phi\), and standard algebraic-function continuation gives slit neighborhoods at the two branch points. Thus the coefficient contribution at \(-R\) is \(O(R^{-n}n^{-3/2})\), while the positive branch contributes \(R^{-n}n^{-1/2}/\sqrt\pi\) times the displayed amplitude (the transfer rule for \((1-z/R)^{-1/2}\)). This proves the formula.

**5. Natural starting distribution.** For \(\mu_i=2^{-i-1}\), \(\Phi(w)=(2-w)^{-1}\), so \(\Phi(2/h)=h/[2(h-1)]\). Multiplying into the general amplitude gives exactly \(2\sqrt{2/\pi}/\varepsilon\), proving the second boxed formula.

## Verification
The accompanying `verify.py` checks the collision identities using symbolic algebra, reconstructs the first-return coefficients through exact rational arithmetic, and separately propagates the original substochastic Markov recurrence. Its exact checks compare first-return and escaped-mass coefficients for three admissible rational hole parameters over the first thirteen transitions. Numerical long-time checks for two hole parameters test the predicted scale and coefficient (for example, at \(\varepsilon=1/2\) the normalized survival ratio is approximately \(0.9841\) by time 750). These finite checks confirm algebraic and indexing details but **do not establish** the all-time asymptotic; the proof uses the singularity analysis above. Reproduce with Python 3, SymPy, and NumPy using `python verify.py`.

## Relationship to prior work
Brevitt and Klages [1] give this exact open Pelikan chain, its generating function for returns, and its spectral classification. In their discussion of the critical pole/branch-point collision they explicitly call the boundary \(R\)-null recurrent and state that they do not consider that case in depth. Their description of generic exponential survival alone does not imply the critical \(n^{-1/2}\) factor or its starting-law-dependent coefficient. The calculation here concerns that narrowly specified boundary, not a new general renewal theory. Duvall [2] establishes survivor-conditioned return and observable laws for open intermittent maps, with different deterministic induced operators; it does not supply the present coefficient. Vega Coso [3] studies geometric resetting to the initial position on finite intervals and absorption channels, not geometric redistribution at zero in an infinite killed chain. The square-root transfer technique is standard; the model-specific cancellation and exact amplitude are the result.

## Limitations
This is a boundary theorem: the parameter relation is exact, \(0<\varepsilon<1\), and the initial law has an exponential moment strictly beyond \(2/(2-\varepsilon)\). It does not classify broader initial tails, nearby off-boundary crossover regimes, the complete conditional Yaglom distribution, or the original stochastic process under other partitions. The \(n^{-1/2}\) correction is a theoretical asymptotic, not a finite-time error certificate. Some historical material, especially a relevant earlier doctoral thesis mentioned by [1], was not available in complete text; exhaustive priority is not claimed.

## References
[1] S. Brevitt and R. Klages, *Quasi-stationary and quasi-ergodic distributions in the Pelikan random map*, arXiv:2607.19084v1, first posted 2026-07-21. https://arxiv.org/abs/2607.19084

[2] J. Duvall, *Survivor-conditioned renewal laws and observable bounds for open intermittent maps*, arXiv:2606.27488v1, 2026-06-25. https://arxiv.org/abs/2606.27488

[3] J. A. Vega Coso, *Critical Spectral Invariants in Random Walks with Geometric Resetting*, arXiv:2603.24803v1, 2026-03-25; later versions use a different title. https://arxiv.org/abs/2603.24803
