# One-clock identifiability and finite-moment ambiguity in a semi-Markov switching harmonic trap

## Finding

A static spatial measurement can determine an entire unknown residence-time distribution in an alternating free-diffusion/Ornstein–Uhlenbeck trap, provided the other residence-time distribution and the physical coefficients are calibrated. This is a *global injectivity* theorem for the forward map, not a claim of numerically stable inversion. In contrast, for every prescribed finite number of even spatial moments there are two different positive, finite-support confinement-time laws, of exactly the same mean, that produce those identical moments under the same calibrated free clock.

More precisely, let the released duration be the positive random variable \(B\), the confined duration be the positive random variable \(C\), and suppose these are independent within and between cycles. Put \(r=2D>0\), \(\lambda=2k>0\), \(q=r/\lambda\). Assume \(0<\mathbb EB,\mathbb EC<\infty\) and that \(B\) has moments of every order; impose moment determinacy on \(B\) when its distribution is to be recovered. If the stationary **conditional released-state** spatial probability law of \(X\) is known exactly, then:

1. Given the complete law of \(B\), that spatial law uniquely identifies the law of \(C\), with an explicit triangular recovery of the entire sequence \(\mathbb E[e^{-m\lambda C}]\), \(m\ge1\).
2. Given the complete law of \(C\) and the positive mean \(\mathbb EB\), that spatial law uniquely identifies the law of \(B\) whenever \(B\) is moment-determinate (in particular, for compactly supported released durations). A second triangular recovery yields every \(\mathbb E[B^m]\).
3. For every integer \(K\ge1\), with the released duration and the two physical coefficients fixed, distinct finitely supported positive confinement-time laws can have equal means and nevertheless produce identical stationary conditional released-state spatial moments of every order up to \(2K\). **Exactly \(K+3\) distinct possible confinement durations (in the union of both supports) are necessary and sufficient** for such a matched-mean alias: no two different discrete clocks on a combined support of at most \(K+2\) durations can agree on these data.

The full conditional spatial law is therefore identifying with one calibrated clock, but no *fixed finite set* of its even moments is uniformly identifying, even when the unknown clock's mean is supplied.

## Assumptions and scope

The one-dimensional particle obeys \(dX_t=\sqrt{2D}\,dW_t\) in released intervals and \(dX_t=-kX_t\,dt+\sqrt{2D}\,dW_t\) in confined intervals; switching alternates without changing position. The independent positive durations \((B_i,C_i)\) are identically distributed across cycles; the Brownian noise is independent. We use the stationary regenerative version and the conditional law given that the observed phase is **released**. The drift parameter is \(k>0\); all moments stated below are finite because all positive moments of \(B\) exist. No density for either duration is required; atomic laws are allowed. The forward and inverse statements concern exact distributions, not finite-sample estimators.

For \(m\ge0\), define \(b_m=\mathbb E[B^m]\), \(a_m=\mathbb E[e^{-m\lambda C}]\), \(b_0=a_0=1\), and \(s_m=\mathbb E[X^{2m}\mid\mathrm{released}]/(2m-1)!!\), taking \((-1)!!=1\). The unknown spatial observation supplies every \(s_m\). Define \(F_m=\sum_{j=0}^m\binom mj(-q)^{m-j}s_j\), with \(F_0=1\). These are the moments of the stationary excess Gaussian variance during release.

## Proof

**1. Stationary excess variance.** Conditional on the entire switching history, the linear stochastic differential equation has a centered Gaussian stationary solution of variance \(V\). Since the drift never exceeds \(k\), its variance satisfies \(V\ge q=D/k\). Set \(U=V-q\ge0\). During release, \(\dot U=r\); during confinement, \(\dot U=-\lambda U\). At successive release starts this gives the random affine recursion
\[
U_{i+1}=A_i(U_i+rB_i),\qquad A_i=e^{-\lambda C_i}\in(0,1).
\]
Since \(\mathbb E\log A=-\lambda\mathbb EC<0\), there is a unique stationary perpetuity. For each positive integer \(m\), \(\mathbb EA^m<1\) and \(\mathbb EB^m<\infty\), so the perpetuity has finite \(m\)-th moment by the triangular recursion below. This justifies all polynomial expectations. Let \(H_m=\mathbb E[U_{\mathrm{release\ start}}^m]\) and \(H_0=1\). Independence yields, for each \(m\ge1\),
\[
H_m=\frac{a_m}{1-a_m}T_m,\qquad
T_m=\sum_{j=0}^{m-1}\binom mj r^{m-j}b_{m-j}H_j>0.
\tag{1}
\]
The strict positivity follows from \(r>0\), \(B>0\) and the positive \(j=0\) term.

**2. Observable moments.** In stationary continuous time conditional on release, the starting variance is sampled at a cycle's release start and the release age has equilibrium renewal reward measure \(\Pr(B>a)\,da/b_1\). Because the fresh \(B\) is independent of the starting \(U\), integration of \((U+ra)^m\) over ages yields
\[
F_m=\frac1{b_1}\sum_{j=0}^{m}\binom mj\frac{r^{m-j}b_{m-j+1}}{m-j+1}H_j,
\qquad m\ge0.
\tag{2}
\]
Conditional Gaussianity gives \(s_m=\mathbb E[(q+U)^m\mid\mathrm{released}]\). Binomial inversion gives precisely the stated \(F_m\).

**3. Recovering the confined clock.** Suppose the released law, hence every \(b_j\), is known. In (2) the coefficient of \(H_m\) is \(b_1/b_1=1\). Starting with \(H_0=1\), recursively compute
\[
H_m=F_m-\frac1{b_1}\sum_{j=0}^{m-1}\binom mj\frac{r^{m-j}b_{m-j+1}}{m-j+1}H_j.
\]
Then (1) yields the uniquely determined quantity
\[
\boxed{a_m=\frac{H_m}{H_m+T_m}},\qquad m\ge1.
\tag{3}
\]
This is the entire power-moment sequence of \(A=e^{-\lambda C}\) on \([0,1]\). Polynomials are dense in \(C([0,1])\), so two probability laws with these identical moments coincide (Hausdorff moment determinacy). The injective map \(C\mapsto e^{-\lambda C}\) then recovers the full confined-duration law, including the mean, uniquely.

**4. Recovering the released clock.** Suppose instead that the law of \(C\) (every \(a_m\)) and \(b_1\) are known. Equations (1)–(2) are triangular in the opposite direction. Given \(b_1,\ldots,b_m\) and \(H_0,\ldots,H_{m-1}\), (1) uniquely obtains \(H_m\), because its right side uses no \(b_{m+1}\). Equation (2) then isolates its \(j=0\) term \(r^m b_{m+1}/[(m+1)b_1]\), determining \(b_{m+1}\). Repeating for all \(m\) recovers every moment of \(B\). By the assumed moment determinacy, these moments uniquely determine its probability law. The extra input \(b_1\) is essential for this reconstruction as formulated; no uniqueness is asserted without it.

**5. Sharp finite-moment nonidentifiability.** For a given integer \(K\ge1\), fix \(B\equiv1\), \(r=\lambda=1\), and possible confined times \(c_j=j\log2\) for \(j=1,\ldots,K+3\). Form the \((K+2)\times(K+3)\) matrix whose rows are \(1\), \(j\), and \(2^{-mj}\) for \(m=1,\ldots,K\). Its nullspace contains a nonzero real vector \(v\). Choose base weights all equal to \(1/(K+3)\) and sufficiently small \(\varepsilon>0\), so the two weight sets \(1/(K+3)\pm\varepsilon v_j\) are strictly positive. The kernel constraints make the two duration laws different but give them the same total mass, the same mean, and the same first \(K\) quantities \(a_m\). The forward recurrences (1)–(2) then force identical \(F_m\) and \(s_m\) for all \(m\le K\). No approximation or finite sampling is involved.

For the concrete \(K=1\) case, take four times \(c_j=j\log2\), weights \(1/4\pm v_j/20\) with \(v=(-1/2,2,-5/2,1)\). They have identical mean \((5/2)\log2\) and first exponential moment \(a_1=15/64\), but distinct second exponential moments. With \(B\equiv1\), \(r=\lambda=q=1\), the two systems have exactly
\[
\mathbb E[X^2\mid\mathrm{released}]=\frac{177}{98},
\quad
\mathbb E[X^4\mid\mathrm{released}]
\in\left\{\frac{24449}{2401},\frac{390461}{38269}\right\},
\]
with the two displayed fourth moments different. Thus second moments and the mean confined residence cannot distinguish the clocks; the fourth moment does in this example. The general kernel construction supplies the same obstruction at every finite order.

**6. Sharp minimal support for finite aliasing.** If two finite-support confined laws have the same mean and first \(K\) exponential moments, the signed difference \(\mu\) annihilates the \(K+2\) functions \(1,t,e^{-\lambda t},\ldots,e^{-K\lambda t}\). These form a strict Chebyshev system on the real line: any nonzero linear combination \(f(t)=c_0+c_1t+\sum_{m=1}^K d_m e^{-m\lambda t}\) has at most \(K+1\) distinct zeros. Indeed, multiplying by \(e^{K\lambda t}\), differentiating, and dividing by the same positive exponential removes \(d_K\) and leaves a function of the same form with \(K-1\) exponentials and a linear polynomial; Rolle\'s theorem and induction from the linear-polynomial base case give the zero count. If the derivative vanishes identically, the original exponential multiple is constant and the same conclusion holds. Consequently, every square evaluation matrix of these \(K+2\) functions at \(K+2\) distinct times is nonsingular. An annihilating nonzero signed measure cannot therefore have at most \(K+2\) support points (extend any smaller evaluation set to \(K+2\) points). Our \(K+3\)-point construction is thus support-optimal. Because identical first \(K\) spatial moments under a known \(B\) determine the first \(K\) confined exponential moments by (3), this is the sharp number of distinct waiting times needed to conceal \(K\) measurements in the stated model.

## Verification

The standalone `check.py` uses exact rational arithmetic to verify the moment and inverse recurrences for nine distinct atomic-law pairs, the fixed-mean four-point alias and nullspace constructions for \(1\le K\le8\). It reports 369 passed deterministic assertions. The separate `simcheck.py` numerically simulates stationary variance cycles for one benchmark law and compares release-phase moment predictions, giving relative errors under \(0.003\) for the first three variance moments at the specified sample length and seed. The infinite-dimensional identifiability theorem and nonidentifiability for every finite \(K\) are analytical arguments, not consequences of those finite tests. To reproduce, run `python check.py` and `python simcheck.py` with Python 3 and no third-party packages.

## Relationship to prior work

Frydel, *Semi-Markovian switching in a fluctuating harmonic trap: An age-structured formulation* (arXiv:2607.05173; Phys. Rev. E 114, 024105, 2026), developed the alternating released/confined trap, the Gaussian variance-mixture representation and the **forward** moment hierarchy; in particular, its Eqs. (52)–(59) and (66)–(70) contain the foundational forward ingredients used here. Those results are not claimed as new. The present theorem addresses a different, inverse question: which calibrated temporal clock is identifiable from the complete stationary released-state spatial law, with explicit triangular reconstruction in both directions and a matched-mean counterexample at every finite moment depth. In contrast, earlier Frydel (2024) studied primarily Markovian fluctuating traps, not this one-clock semi-Markov inverse identification problem. Standard Hausdorff moment determinacy is used as a classical theorem, not claimed new.

## Limitations

The reconstruction assumes independent alternating clocks, known diffusion and confinement coefficients, exact phase-conditioned stationary spatial data, and all released-duration moments finite. Reconstructing the released law additionally requires its mean and moment determinacy. Identifiability from the **unconditioned** spatial law, or joint identification when both clocks are unknown, is not proved. Infinite exact moments do not imply that recovery from finite noisy samples is well-conditioned; in fact the finite-moment aliases show why low-order data can be fundamentally insufficient. No assertion of novelty over every possible unindexed inverse-renewal theorem is made, and independent scientific evaluation remains appropriate.

## References

- D. Frydel, *Semi-Markovian switching in a fluctuating harmonic trap: An age-structured formulation*, arXiv:2607.05173, first submitted July 6, 2026; *Physical Review E* **114**, 024105 (2026), https://doi.org/10.1103/7pxv-tg3b. Primary full-text comparison: Sections V–VII, especially Eqs. (52)–(59), (66)–(70).
- D. Frydel, *Statistical mechanics of passive Brownian particles in a fluctuating harmonic trap*, arXiv:2407.12213; *Physical Review E* **110**, 024613 (2024), https://doi.org/10.1103/PhysRevE.110.024613.
- F. Hausdorff, *Momentprobleme für ein endliches Intervall*, Math. Z. **16** (1923), 220–248. Classical uniqueness of probability measures on a compact interval from their power moments.
