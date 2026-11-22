# A cubic-root optimal three-stage unmasking law at the ordered Ising edge

## Finding
For exactly three parallel reveal rounds on an infinite zero-field binary Ising/Markov chain, the sharp near-perfect-order optimal reveal probabilities have different powers of correlation length. If \(\xi=(-\log\lambda)^{-1}\), with chain correlation \(0<\lambda<1\), every global minimizer obeys
\[
p_*\sim (2\log2)^{-2/3}\xi^{-2/3},\qquad
q_*\sim (2\log2)^{-1/3}\xi^{-1/3},
\]
and its optimal forward-path relative entropy per spin is
\[
\min B_3\sim 3(\log2/4)^{1/3}\xi^{-2/3}.
\]
Here \(q_*\) is a **conditional** second-round reveal probability among not-yet-revealed sites; the cumulative density revealed after two rounds is \(p_*+(1-p_*)q_*\sim q_*\). This is a fixed-three-round, infinite-volume, strong-correlation asymptotic, not a fine-step/geodesic limit.

## Assumptions and scope
Let \((X_i)_{i\in\mathbb Z}\) be a stationary \(\{-1,+1\}\)-valued Markov chain with \(\Pr(X_{i+1}\ne X_i)=(1-\lambda)/2\), \(0<\lambda<1\). On a finite interval of \(L\) sites, assign each site independently to round 1 with probability \(p\), round 2 with probability \((1-p)q\), and round 3 with probability \((1-p)(1-q)\), where \(0\le p,q\le1\). In each round all assigned sites are generated independently conditional on the *previously* revealed sites, using the exact single-site conditional distribution of the source. The exact comparator generates each round's assigned sites jointly from their true conditional law. Write \(P_L\) and \(Q_L\) for the respective joint laws of reveal assignments and values, and define
\[
B_3(p,q;\lambda)=\lim_{L\to\infty}L^{-1}D_{\mathrm{KL}}(P_L\Vert Q_L).
\]
Logs are natural. The source Markov chain is held at fixed \(\lambda\) when taking the thermodynamic limit, and only then is \(\lambda\uparrow1\) taken. The result covers *path* relative entropy, not the relative entropy of the final output after forgetting round assignments.

## Proof
Put \(r=1-\lambda\), \(h(x)=-x\log x-(1-x)\log(1-x)\), with \(h(0)=h(1)=0\), and
\[
a_k(r)=h\!\left(\frac{1-(1-r)^k}{2}\right),\qquad k=0,1,2,\ldots.
\]
These are exactly the \(k\)-step transition entropies of the symmetric chain, with \(a_0=0\). Conditional on knowing the two closest revealed values at distances \(k,\ell\ge1\), the Markov property and the chain rule give the single-site conditional entropy
\[
H(X_0\mid X_{-k},X_\ell)=a_k+a_\ell-a_{k+\ell}.
\]
With only one known boundary it is \(a_k\); with none it is \(\log2\). If each site independently belongs to a previously revealed set at density \(u\in(0,1)\), its left and right nearest revealed distances \(K_u,K'_u\) are independent geometric random variables of parameter \(u\). Thus define
\[
F_r(u)=2\mathbb E a_{K_u}(r)-\mathbb E a_{K_u+K'_u}(r).
\]
This extends continuously to \(F_r(0)=\log2\) and \(F_r(1)=2a_1-a_2\). The true source entropy rate is \(a_1\). The path likelihood ratio cancels the reveal-assignment law; its expectation is the sum of the conditional entropies used by the parallel sampler minus source block entropy. Consequently the thermodynamic limit exists and has the exact form
\[
B_3(p,q;1-r)=p\log2+(1-p)qF_r(p)
 +(1-p)(1-q)F_r(p+(1-p)q)-a_1(r).\tag{1}
\]
Finite-interval boundary contributions are \(o(L)\) for fixed \(r,p,q\), including endpoints by continuity. Each term of the path KL is nonnegative, and the continuous objective attains its minimum on the closed unit square.

**Geometric-neighbor asymptotic.** For every pair \(r,u\downarrow0\) with \(r/u\to0\),
\[
F_r(u)=\frac{r}{2u}(1+o(1)).\tag{2}
\]
To prove (2), write \(\mu=-\log(1-r)\) and \(\phi(z)=h((1-e^{-z})/2)\). As \(z\downarrow0\),
\[
\phi(z)=\frac z2\bigl(1-\log(z/2)\bigr)+O\bigl(z^2(1+|\log z|)\bigr).
\]
Geometric tails and the bound \(0\le\phi\le\log2\) make this expansion integrable uniformly when \(\mu/u\to0\), with error \(o(\mu/u)\). Since \(2\mathbb E K_u=\mathbb E(K_u+K'_u)\), the terms proportional to \(z\), \(z\log\mu\) cancel. Therefore
\[
F_r(u)=\frac\mu2\left\{\mathbb E[(K_u+K'_u)\log(K_u+K'_u)]-2\mathbb E[K_u\log K_u]\right\}+o(\mu/u).
\]
Here \(uK_u\) and \(uK'_u\) converge with integrable \(x\log x\) moments to independent unit exponentials \(E,E'\). Using the Gamma shape-one and shape-two moments gives
\[
\lim_{u\downarrow0}u\left\{\mathbb E[(K_u+K'_u)\log(K_u+K'_u)]-2\mathbb E[K_u\log K_u]\right\}=\mathbb E[(E+E')\log(E+E')]-2\mathbb E[E\log E]=1.
\]
Since \(\mu\sim r\), (2) follows. In addition, for \(r,u\downarrow0\) with \(r/u\to t\in(0,\infty)\), geometric scaling gives
\[
F_r(u)\to2\mathbb E\phi(tE)-\mathbb E\phi(t(E+E'))>0,
\]
while for \(r/u\to\infty\), \(F_r(u)\to\log2\). Positivity follows from strict concavity, increase and subadditivity of \(\phi\), with \(\phi(0)=0\). In particular \(F_r(u)\to0\) when \(r,u\downarrow0\) forces \(r/u\to0\).

**Upper bound and localization of every minimizer.** Set \(C=(2\log2)^{-2/3}\), \(D=(2\log2)^{-1/3}\), and take the trial probabilities \(p=Cr^{2/3}\), \(q=Dr^{1/3}\). Equation (2) and \(a_1(r)=O(r\log(1/r))=o(r^{2/3})\) give
\[
B_3(p,q;1-r)=r^{2/3}\left(C\log2+\frac D{2C}+\frac1{2D}+o(1)\right)=3(\log2/4)^{1/3}r^{2/3}(1+o(1)).\tag{3}
\]
For any minimizer, the upper bound (3) and \(B_3\ge p\log2-a_1\) imply \(p=O(r^{2/3})\). If a subsequence had \(q\ge\varepsilon>0\), its nonnegative second-round entropy contribution would force \(F_r(p)=O(r^{2/3})\), hence \(r/p\to0\), while (2) would give \(F_r(p)\gtrsim r^{1/3}\), a contradiction. Thus \(q\to0\). With \(s=p+(1-p)q\), the third-round contribution now forces \(F_r(s)=O(r^{2/3})\), whence \(r/s\to0\) and (2) yields \(s\gtrsim r^{1/3}\). Since \(p=O(r^{2/3})\), it follows that \(q\gtrsim r^{1/3}\) and \(q\gg p\). The second-round contribution similarly forces \(r/p\to0\), then (2) gives \(p\gtrsim q r^{1/3}\gtrsim r^{2/3}\). Finally, the same second-round bound gives \(q\lesssim r^{1/3}\). Thus all minimizers lie in a common compact range after scaling \(p/r^{2/3}\), \(q/r^{1/3}\) away from zero and infinity.

**Limit optimization.** Uniformly for \(p=cr^{2/3}\), \(q=dr^{1/3}\) with \(c,d\) in any compact positive rectangle, (1)–(2) give
\[
r^{-2/3}B_3(p,q;1-r)\to\Psi(c,d)=c\log2+\frac d{2c}+\frac1{2d}.\tag{4}
\]
The unique global minimizer of \(\Psi\) has \(d=\sqrt c\) and \(d=2c^2\log2\), hence \((c,d)=(C,D)\); the three positive contributions all equal \((\log2/4)^{1/3}\). The compactness argument promotes this to **every** minimizer of the exact objective. Since \(r\xi\to1\), substituting \(r\sim\xi^{-1}\) yields the theorem.

## Verification
The accompanying `verify_three_round.py` uses only Python's standard library and checks 12 complete finite-path likelihood-ratio enumerations on binary chains of lengths three through six, independent conditional-entropy reconstructions, and 14 asymptotic/numerical constant identities (26 checks total). Its deterministic output is `PASS: 26 independent finite-path and asymptotic numerical checks`. This finite test evidence supplements, rather than replaces, the geometric-neighbor and compactness proof above. Near-optimal trials using direct geometric sums approach the predicted constants as \(r\) decreases; no finite experiment is used to establish the infinite-volume or zero-domain-wall limit.

## Relationship to prior work
Baule [1] identified the exact source-specific mean-field path error, solved a labelled-gap random sequential adsorption process at arbitrary finite step counts, and derived a **large-number-of-steps** thermodynamic metric. The present claim extracts and proves a sharp **fixed-three-round** global optimization in a singular correlation-length regime. The exact finite-step framework in [1] makes its objective computable, but does not state the \(2/3\)-power optimum or its coefficient. The general schedule and information-profile frameworks in [2,3] cover broader samplers but do not give this binary-chain singular three-round classification. A separate two-round result gives a different square-root scaling; its third-round consequence is neither an identical statement nor a direct substitution, and the new proof identifies two distinct intermediate scales. The result makes no publication-priority claim beyond examined literature.

## Limitations
The theorem applies to path KL including reveal-round assignments, not output-only KL, finite-sample training error, correlated/adaptive site assignments, arbitrary Markov alphabets, fixed finite-chain limits with changing correlation length, or more than three rounds. No uniqueness at fixed \(\lambda\) is claimed. General finite-step formulae already occur in [1]; the claimed contribution is the nontrivial singular optimizing limit. Unindexed identical results and possible implications of broader information-profile analyses remain residual priority risks.

## References
[1] Adrian Baule, *Masked diffusion as random sequential adsorption: an exactly solvable model for parallel decoding*, arXiv:2611.07845v1 (first public 2026-11-05), https://arxiv.org/abs/2611.07845.

[2] Hugo Lavenant and Giacomo Zanella, *Error Bounds and Optimal Schedules for Masked Diffusions with Factorized Approximations*, arXiv:2510.25544 (first public 2025-10-29), https://arxiv.org/abs/2510.25544.

[3] Martin J. Wainwright, *The data geometry of masking diffusion: Certified-optimal schedules via unmasking growth complexity*, arXiv:2608.13520 (first public 2026-08-13), https://arxiv.org/abs/2608.13520.
