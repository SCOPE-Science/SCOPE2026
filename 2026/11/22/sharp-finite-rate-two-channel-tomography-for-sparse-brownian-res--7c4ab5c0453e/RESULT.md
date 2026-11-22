# Sharp finite-rate two-channel tomography for sparse Brownian resetting on a ring

## Finding

**Theorem (sharp number of rates and an exact sparsity certificate).** Consider a Brownian particle moving on a ring of circumference \(L>0\), with diffusion generator \(D\partial_{xx}\), \(D>0\). It is absorbed upon reaching a distinguished point; the two sides of its *continuous* final approach are separately recorded. At independent Poisson times of rate \(r>0\), the particle is instantaneously transported to a fresh position drawn from an unknown, fixed Borel probability law \(\mu\) on the open ring with the absorber removed. Resets do not themselves count as arrivals. Each experiment starts at the same known \(x_0\in(0,L)\), and \(L,D,x_0\) are calibrated.

For a chosen \(\kappa>0\) and integer \(K\ge1\), measure at exactly the \(K\) positive rates
\[
 r_j=D\kappa^2j^2,\qquad j=1,\ldots,K,
\]
the exact population mean absorption time \(M_j=\mathbb E[T]\) and the probability \(P_j\) of ultimate continuous arrival at the left side of the cut. These \(2K\) scalar readings determine an explicit positive-semidefinite Hankel matrix \(H^{(K)}\) of order \(K+1\), with the following properties:

1. \(\det H^{(K)}=0\) **if and only if** the resetting law is supported on **at most \(K\) distinct sites**. This equivalence holds against *all* Borel resetting laws on \((0,L)\), including continuous or infinitely supported laws, not just under an assumed finite-atomic model.
2. In that case, \(s=\operatorname{rank}H^{(K)}\le K\) is the exact number of resetting sites, and all \(s\) **oriented** locations and positive weights are uniquely recoverable by a finite Hankel–Vandermonde procedure. In particular, mirror sites are distinguished; a single mean-time channel would not generally do so.
3. **\(K\) rates are necessary** for universal identification of the full class of laws with *exactly \(K\)* positive, distinct, unknown reset sites and their unknown weights, even when one may choose arbitrary positive rates and collect both observables there. Thus this two-channel protocol uses the sharp minimum number of rates for the \(K\)-site identification problem.

These statements concern exact population observables. No uniform noisy-data inverse stability, sampling-error rate, or recovery of uncalibrated \(D\) or \(L\) is claimed. The Prony/Hankel moment reconstruction used in the proof is classical; the result concerns its sharp realization by the specified pair of physical first-passage observables.

## Assumptions and scope

Cut the circle at the absorbing point, obtaining a Brownian interval \((0,L)\) whose endpoints represent the *same* absorbing physical site but different final continuous arrival directions. The process has generator \(D\partial_{xx}\) between jumps and an independent rate-\(r\) Poisson clock. Its resetting law \(\mu\), independent of the clock and past, is the same at every jump and at every experimental rate; no reset is to the absorbing point. Initial position \(x_0\in(0,L)\) is deterministic, known, and the same across experiments, and need not belong to the support of \(\mu\). The absorbing event occurs only by continuous diffusion to either boundary. The two scalar observations at a rate are (i) the unconditional mean completion time and (ii) unconditional probability that the final boundary is \(0\), rather than \(L\). Observations are theoretical exact ensemble values, not finite-trajectory estimates. Fix arbitrary \(\kappa>0\) and \(K\in\mathbb N\), \(K\ge1\).

For \(k=\sqrt{r/D}\), define the no-reset discounted left and right exit probabilities and their sum by
\[
 h_0(x;k)=\frac{\sinh(k(L-x))}{\sinh(kL)},\quad
 h_L(x;k)=\frac{\sinh(kx)}{\sinh(kL)},\quad
 f(x;k)=h_0(x;k)+h_L(x;k)=\frac{\cosh(k(L/2-x))}{\cosh(kL/2)}.
\]
The formula for \(f\) is the known Brownian first-passage resolvent for an absorbing ring; the individual channels are its standard Dirichlet boundary-value decomposition. Set \(F(k)=\int f(x;k)\,\mu(dx)\) and \(A(k)=\int h_0(x;k)\,\mu(dx)\), both strictly between zero and one under the stated interior-support assumptions.

## Proof

**1. Recovery of two independent transformed reset-source observables.** Each attempted Brownian excursion ends at the first absorbing boundary or at the next reset. An excursion starting at \(x\) has probability \(f(x;k)\) to absorb before the independent reset and probability \(h_0(x;k)\) to absorb specifically at the left boundary. Its expected duration until either event is \([1-f(x;k)]/r\). From a fresh reset location, geometric renewal gives mean additional time \((1-F)/(rF)\). Starting from the calibrated \(x_0\), therefore,
\[
 M(r)=\frac{1-f(x_0;k)}{rF(k)}.
\]
Similarly the ultimate probability to exit to the left after the first reset equals \(A/F\), since each fresh attempt succeeds to the left with probability \(A\) and succeeds to either boundary with probability \(F\). Consequently,
\[
 P(r)=h_0(x_0;k)+[1-f(x_0;k)]\frac{A(k)}{F(k)}.
\]
Since \(x_0\) lies strictly inside the interval, \(1-f(x_0;k)>0\) for every \(r>0\), so the observed pair \((M,P)\) determines
\[
 F(k)=\frac{1-f(x_0;k)}{rM(r)},\qquad
 A(k)=F(k)\frac{P(r)-h_0(x_0;k)}{1-f(x_0;k)}.
\]
No density assumption on \(\mu\) was used.

**2. From the two absorption channels to bilateral power moments.** Write \(y=L/2-x\). Direct hyperbolic identities yield
\[
 f(x;k)=\frac{\cosh(ky)}{\cosh(kL/2)},\quad
 2h_0(x;k)-f(x;k)=\frac{\sinh(ky)}{\sinh(kL/2)}.
\]
For each selected \(k_j=j\kappa\), form the *explicitly observed* quantities
\[
 C_j=\cosh(j\kappa L/2)F(k_j),\qquad
 S_j=\sinh(j\kappa L/2)[2A(k_j)-F(k_j)].
\]
It follows that \(C_j\pm S_j=\int\exp[\pm j\kappa(L/2-x)]\,\mu(dx)\). Put
\[
 t=\exp[\kappa(L/2-x)]\in I_\kappa=(e^{-\kappa L/2},e^{\kappa L/2})
\]
and denote by \(\rho\) the pushforward of \(\mu\) under this one-to-one map. We have recovered all \(2K+1\) consecutive *Laurent moments*
\[
 m_0=1,\qquad m_j=C_j+S_j,\quad m_{-j}=C_j-S_j
 \quad(j=1,\ldots,K),\qquad m_i=\int t^i\,\rho(dt).
\]
The sign of \(S_j\) retains orientation: reflection \(x\mapsto L-x\) reverses it, unlike the mean-time channel alone.

**3. Exact support-count certificate.** Since \(t>0\), the finite positive measure \(\nu(dt)=t^{-K}\rho(dt)\) has ordinary moments \(u_i=m_{i-K}\) for \(i=0,\ldots,2K\). Form
\[
 H^{(K)}=(u_{i+j})_{0\le i,j\le K}.
\]
For \(a\in\mathbb R^{K+1}\),
\[
 a^\mathsf TH^{(K)}a=\int\left(\sum_{i=0}^{K}a_it^i\right)^2\nu(dt)\ge0.
\]
Thus \(H^{(K)}\) is positive semidefinite. It is singular exactly when a nonzero polynomial of degree at most \(K\) vanishes \(\nu\)-almost everywhere. A nonzero real polynomial of degree at most \(K\) has at most \(K\) distinct real roots, so singularity is equivalent to support cardinality at most \(K\). If the source has \(s\le K\) distinct atoms with positive weights, the Gram factorization through their Vandermonde vectors has rank exactly \(s\). This proves the first statement and the model-order assertion, including the exclusion of every non-atomic or more-than-\(K\)-atomic alternative that matches the data.

**4. Explicit exact reconstruction and uniqueness.** Under the singularity condition, set \(s=\operatorname{rank}H^{(K)}\) and let \(H_s=(u_{i+j})_{0\le i,j<s}\). Positive masses at \(s\) distinct positive nodes make \(H_s\) positive definite. Solve the non-singular system
\[
 \sum_{j=0}^{s-1}c_ju_{i+j}=-u_{i+s},\qquad i=0,\ldots,s-1.
\]
The monic polynomial \(p(t)=t^s+\sum_{j=0}^{s-1}c_jt^j\) satisfies \(\int t^i p(t)\,\nu(dt)=0\) for \(i<s\). Vandermonde invertibility forces \(p\) to vanish at all \(s\) support nodes; hence its roots are the exactly recovered distinct positive \(t_1,\ldots,t_s\in I_\kappa\). Solve \(\sum_{\ell=1}^s v_\ell t_\ell^i=u_i\) for \(i=0,\ldots,s-1\). Then \(v_\ell>0\) are the \(\nu\)-weights, the physical reset weights are \(w_\ell=t_\ell^K v_\ell\), and the oriented sites are
\[
 x_\ell=L/2-\frac{\log t_\ell}{\kappa}\in(0,L).
\]
Any second physically admissible source having the same data has the same Hankel matrix, is therefore also supported at \(s\) sites, and has the identical annihilating polynomial and Vandermonde weights. This establishes uniqueness *without* requiring an a priori sparse-support restriction once the observed certificate is singular.

**5. Minimal number of rate settings.** Consider the subfamily of sources with exactly \(K\) distinct positions in strict increasing order inside \((0,L)\), and exactly \(K\) positive weights summing to one. The parameter set, parametrized by the \(K\) positions and the first \(K-1\) weights, is an open subset of \(\mathbb R^{2K-1}\). For arbitrary \(m\) fixed positive rates, the map from these parameters to the \(m\) mean times and \(m\) left-arrival probabilities is continuous and has values in \(\mathbb R^{2m}\). If \(m<K\), then \(2m<2K-1\). There is no continuous injection from a nonempty open subset of \(\mathbb R^{2K-1}\) to a lower-dimensional Euclidean space: padding such a putative injection with zeros and invoking invariance of domain would yield an open subset of a proper affine subspace, a contradiction. Hence no choice of fewer than \(K\) rate pairs identifies all \(K\)-site sources. Steps 1–4 show that the specified \(K\) rates do, proving sharpness. For \(K=1\), the lower bound merely excludes zero measurements, while one positive rate reconstructs the single source position.

## Verification

The standalone standard-library script `verify.py` executes 2,764 deterministic assertions, including exact-rational Gram determinant certificates on atomic measures with up to \(K+1\) sites for \(K=1,2,3,4\), positive Gram determinants on the \(K+1\)-site side, exact annihilator and weight reconstruction for smaller supports, and independently computed physical mean-time/left-arrival pairs at up to five rates compared against both recovered exponential moment channels. Reproduce using `python verify.py`. The exact rational tests check nontrivial finite instances; they do not replace the Gram-polynomial or topological arguments, which cover every positive integer \(K\) and every admissible Borel source.

## Relationship to prior work

Julián-Salgado, Castro-Villarreal, Dagdug and Boyer (arXiv:2605.08414, first public 2026-05-08) derived the survival/MFPT renewal framework on a reset Brownian ring and analyzed mirror transitions in optimal resetting. Their exact forward renewal setting and mirror ambiguity motivate this inverse question. They do not formulate the paired exit-direction/mean-time finite-rate reconstruction or the sharp \(K\)-rate theorem. Sezik, Knight, Alston, Roberts, Bertrand, Pruessner and Cocconi (arXiv:2508.07386, first public 2025-08-10) develop joint and conditional splitting probabilities, including resetting and hidden-state inference, but not the full distribution of independently chosen reset positions from finitely many paired rate measurements. Abundo (arXiv:2410.16889) develops inverse first-passage *specification* problems with resetting, not this exact support-identification certificate. Méndez, Flaquer-Galmés and Campos (arXiv:2401.01125) provide earlier distributed-resetting forward first-passage theory.

Classical Prony reconstruction, positive Hankel moment matrices, and invariance of domain are **not** novel. They underlie Steps 3–5. The distinct mathematical assertion is that the particular experimentally meaningful pair \((M,P)\) at the quadratic rates yields consecutive *signed* Laurent moments, producing simultaneously an if-and-only-if physical-support certificate and sharp sample-rate identification on the ring. Related inverse-source or moment-tomography formulations may imply this result in disguise; no unrestricted publication-priority claim is made.

## Limitations

The process must have instantaneous independent Poisson resets to a source law common to all measured rates; the target and two final approach directions must be distinguishable. The ring length, diffusivity and deterministic starting site are known. The result is purely about exact ensemble observables. Finite-sample estimation, noisy inversion, atom-separation stability, unknown diffusion parameters, moving targets, refractory resetting, correlated reset sites, drift and partially absorbing targets are outside the scope. The certificate requires exact rank or determinant zero, a condition which is not robust to measurement noise without additional analysis. There is no claim of identifying a genuinely continuous source from finitely many data; instead its Hankel matrix is strictly positive definite.

## References

1. P. Julián-Salgado, P. Castro-Villarreal, L. Dagdug, D. Boyer, *Mirror transitions in diffusion with stochastic resetting confined on a ring*, arXiv:2605.08414, first public 2026-05-08, https://arxiv.org/abs/2605.08414.
2. E. Sezik, J. Knight, H. Alston, C. Roberts, T. Bertrand, G. Pruessner, L. Cocconi, *Conditional splitting probabilities for hidden-state inference in drift-diffusive processes*, arXiv:2508.07386, first public 2025-08-10, https://arxiv.org/abs/2508.07386.
3. M. Abundo, *Inverse first-passage problems of a diffusion with resetting*, arXiv:2410.16889, first public 2024-10-22, https://arxiv.org/abs/2410.16889.
4. V. Méndez, R. Flaquer-Galmés, D. Campos, *First-passage time of a Brownian searcher with stochastic resetting to random positions*, arXiv:2401.01125, first public 2024-01-02, https://arxiv.org/abs/2401.01125.
5. T. Sauer, *Continued Fractions*, §§3.6–3.7, 2019, https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/sauer/geyer/Vorleseskripteab2012/ContinuedFraction-SS2021.pdf (classical Prony and flat moment methods).
