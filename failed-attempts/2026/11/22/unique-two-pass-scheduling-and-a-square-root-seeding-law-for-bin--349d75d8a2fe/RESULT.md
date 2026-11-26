# Unique two-pass scheduling and a square-root seeding law for binary Markov decoding

## Finding

For a stationary, symmetric binary Markov source with positive one-step correlation \(0<\lambda<1\), the two-round Bernoulli-site masked parallel decoder has a **strictly convex** path-relative-entropy density as a function of the initial reveal probability \(p\). The unique optimum \(p_*(\lambda)\) lies strictly between zero and one half. Let \(f=(1-\lambda)/2\) be the source's domain-wall probability. Its strong-correlation limit is
\[
p_*(\lambda)\sim\sqrt{\frac{f}{\log 2}},\qquad
\min_{0\le p\le1}b(p,\lambda)\sim2\sqrt{f\log 2}
\quad(f\downarrow0).
\]
The opposite, weak-correlation limit is
\[
p_*(\lambda)=\frac12-\frac{3}{16}\lambda^2+O(\lambda^4)
\quad(\lambda\downarrow0).
\]

## Assumptions and scope

Let \(L\ge2\) and let \(X_1,\ldots,X_L\in\{-1,+1\}\) form the stationary Markov chain with \(\Pr(X_1=\pm1)=1/2\) and \(\Pr(X_{i+1}\ne X_i)=f\in(0,1/2)\). Put \(\lambda=1-2f\). Independently of the source, place each site in the first reveal batch with probability \(p\in[0,1]\); reveal all remaining sites in the second batch. In each batch, the *parallel* decoder independently samples each scheduled site according to its exact single-site conditional distribution given the previously revealed sites. The reference process samples each scheduled batch jointly according to the actual Markov conditional law. Both use exactly the same random batch allocation. Let \(P_L\) and \(Q_L\) be these reference and approximate joint laws of the final string *and allocation*. The quantity studied is \(B_L=\operatorname{KL}(P_L\Vert Q_L)\), and \(b(p,\lambda)=\lim_{L\to\infty}B_L/L\), with natural logarithms. The theorem does not assert equality with \(\operatorname{KL}\) of the final-string marginals.

Define the distance-\(d\) mutual information, for integers \(d\ge1\), by
\[
I_d=\frac12\big[(1+\lambda^d)\log(1+\lambda^d)+(1-\lambda^d)\log(1-\lambda^d)\big].
\]
Set \(z=1-p\) and \(F_\lambda(z)=\sum_{d=1}^\infty I_dz^{d-1}\). The series converges absolutely for \(0\le z\le1\) and \(0<\lambda<1\). The exact thermodynamic path-error density is
\[
b(p,\lambda)=I_1-2p(1-p)F_\lambda(1-p)+p^2(1-p)F_\lambda'(1-p).
\tag{1}
\]
It is analytic in \(p\) on a neighborhood of \([0,1]\) for each fixed interior \(\lambda\).

## Proof

**1. Gap reduction and thermodynamic limit.** Conditional on the first-revealed sites, the Markov property makes different remaining masked gaps independent. The source entropy per symbol is \(h=\log2-I_1\). The expected first-pass total correlation, per length in the large-\(L\) limit, is \(p^2\sum_{d\ge1}z^{d-1}I_d=p^2F_\lambda(z)\), because consecutive initially revealed sites at separation \(d\) occur with density \(p^2z^{d-1}\). A masked interior gap of length \(\ell\ge1\), with its two boundary tokens revealed, has conditional total correlation
\[
C_\ell=(\ell+1)I_1-2\sum_{d=1}^\ell I_d+(\ell-1)I_{\ell+1}.
\tag{2}
\]
Indeed, the individual conditional entropies sum to \(\ell\log2-2\sum_{d=1}^\ell I_d+\ell I_{\ell+1}\), whereas the joint conditional entropy is \(\ell\log2-(\ell+1)I_1+I_{\ell+1}\). Such gaps occur with density \(p^2z^\ell\), giving the second-pass density \(p^2\sum_{\ell\ge1}z^\ell C_\ell\). At fixed \(p>0\), the two chain ends contribute \(O(1)\) to \(B_L\), as does the event of no first-revealed site after taking the limit. For \(p=0\), one pass reveals every site and the density is \(I_1\); this also equals the continuous limit of the formula below. Summing the absolutely convergent series yields (1).

For exact finite-size verification, the edge-gap conditional total correlation is \(E_\ell=\ell I_1-\sum_{d=1}^\ell I_d\), so one also has the entirely finite identity
\[
\begin{aligned}
B_L={}&p^2\sum_{d=1}^{L-1}(L-d)z^{d-1}I_d
+p^2\sum_{\ell=1}^{L-2}(L-\ell-1)z^\ell C_\ell\\
&+2p\sum_{\ell=1}^{L-1}z^\ell E_\ell+z^L(L-1)I_1.
\end{aligned}
\tag{3}
\]
This formula also covers \(p=0\) and \(p=1\) by continuity.

**2. Strict convexity and uniqueness.** The absolutely convergent positive expansion
\[
I_d=\sum_{k=1}^\infty a_k t_k^d,\quad
a_k=\frac{1}{2k(2k-1)}>0,\quad t_k=\lambda^{2k}\in(0,1)
\]
turns (1) into \(b(p,\lambda)=\sum_{k\ge1}a_kt_kg_{t_k}(p)\) with
\[
g_t(p)=1-\frac{2p(1-p)}{1-t+pt}+\frac{p^2(1-p)t}{(1-t+pt)^2}.
\tag{4}
\]
Twice differentiating the rational function gives the pointwise positive expression
\[
g_t''(p)=\frac{2(1-t)^2(2+t-pt)}{(1-t+pt)^4}>0
\quad (0<t<1,\ 0\le p\le1).
\tag{5}
\]
Termwise differentiation is permitted by exponential decay in \(k\) at fixed \(\lambda<1\). Moreover, \(g_t'(0)=-2/(1-t)<0\), while \(g_t'(1/2)=t(5t-6)/(t-2)^3>0\). Thus \(b'\) changes sign exactly once in \((0,1/2)\) and its zero is the unique global minimizer.

For \(\lambda\downarrow0\), only the first geometric mode contributes at order \(\lambda^2\), and \(g_t'(1/2)=3t/4+O(t^2)\), \(g_t''(1/2)=4+O(t)\). The remaining modes and their derivatives are \(O(\lambda^4)\) in the cost. Taylor's theorem at the unique minimizer gives \(p_* = 1/2-3\lambda^2/16+O(\lambda^4)\).

**3. Singular strong-correlation scale.** Put \(\delta=1-\lambda=2f\) and let \(p=c\sqrt\delta\), with \(c\) constrained to any fixed compact subinterval of \((0,\infty)\). Uniformly on that interval, expansion of the binary entropy gives
\[
I_d=\log2-\frac{\delta d}{2}\Bigl[1+\log\frac{2}{\delta d}\Bigr]
+O\bigl(\delta^2d^2(1+|\log(\delta d)|)\bigr)
\]
for \(d\le\delta^{-2/3}\), and contributions of larger \(d\) to the geometrically weighted series in (1) and its first derivative are exponentially small. To compute the first-order term, set
\[
G(z)=\sum_{d\ge1}d(\log d)z^{d-1},\qquad K_\delta=1+\log(2/\delta),\quad z=1-p.
\]
Then
\[
F_\lambda(z)=\frac{\log2}{p}-\frac\delta2\left(\frac{K_\delta}{p^2}-G(z)\right)+R,
\]
where substitution of \(R\) into the linear differential expression in (1) is \(O(\delta^2p^{-2}(1+|\log\delta|))\); its first \(p\)-derivative is \(O(\delta^2p^{-3}(1+|\log\delta|))\). These estimates follow directly by geometric-moment bounds \(\sum_{d\ge1}d^jz^{d-1}=O(p^{-j-1})\) and the cut-off. Standard exponential-sum comparison, or differentiation of the polylogarithm at order \(-1\), gives
\[
G(z)=\frac{\log(1/p)+1-\gamma}{p^2}+O\bigl(p^{-1}(1+|\log p|)\bigr),
\]
\[
G'(z)=\frac{2\log(1/p)+3-2\gamma}{p^3}+O\bigl(p^{-2}(1+|\log p|)\bigr),
\]
with analogous differentiated error bounds. On substituting these expansions in (1), every term containing \(K_\delta\) cancels exactly. The results, uniformly for \(p=c\sqrt\delta\), are
\[
b(p,\lambda)=p\log2+\frac\delta{2p}+o(\sqrt\delta),\qquad
\partial_pb(p,\lambda)=\log2-\frac\delta{2p^2}+o(1).
\tag{6}
\]
Here \(I_1-\log2=O(\delta|\log\delta|)\) is negligible. Choosing \(c_-<1/\sqrt{2\log2}<c_+\), the derivative in (6) is respectively negative and positive for sufficiently small \(\delta\); strict convexity traps the unique minimizer between \(c_-\sqrt\delta\) and \(c_+\sqrt\delta\). Then (6) and the derivative-root condition imply
\[
\frac{p_*(\lambda)}{\sqrt\delta}\to\frac1{\sqrt{2\log2}},\qquad
\frac{b(p_*,\lambda)}{\sqrt\delta}\to\sqrt{2\log2}.
\]
Replacing \(\delta\) by \(2f\) proves the two stated strong-correlation asymptotics.

## Verification

The standalone `check.py` verifies (3) by direct enumeration of the full two-pass path likelihood for short chains and various correlation/reveal parameters; it also compares the analytic derivative against a finite difference, tests strict positive curvature, locates the unique minimizer numerically, and checks its approach to the asymptotic coefficient. The formal infinite-length and singular-limit statements follow from the analytical proof, **not** from this finite computation. Run `python check.py` with Python, NumPy and SciPy available.

## Relationship to prior work

Baule, *Masked diffusion as random sequential adsorption: an exactly solvable model for parallel decoding* (arXiv:2611.07845v1, November 5, 2026), previously established exact finite-stage path-error identities for Markov data, including its gap decomposition, and developed geodesic-optimal **many-step** schedules. The present path-error construction specializes those identities; the substantive new claim is the **strictly convex finite-two-stage optimizer and its singular square-root scaling**, which are not explicitly obtained by Baule's many-step geodesic theorem. Chen, Cong and Li (arXiv:2511.04647v2) characterized optimal fixed-size inference schedules by the information curve for arbitrary data; Lavenant and Zanella (arXiv:2510.25544v2) studied optimal schedules through information profiles and many-step limits. Their frameworks give principled routes to an implicit numerical optimizer but do not directly state the closed two-pass Ising uniqueness and strong-correlation asymptotics above. Equivalence to an unstated consequence of those frameworks cannot be categorically excluded.

## Limitations

The theorem concerns the thermodynamic limit taken **before** the strong-correlation limit: it does not assert the same asymptotics in a coupled finite-size regime. Site assignment is independently Bernoulli, not chosen adaptively from observed tokens. Only positive nearest-neighbour correlations in a symmetric binary stationary chain are treated. The error is *path KL* of tokens plus reveal times, not output-only KL, total variation or perplexity. The exact one-site conditional sampler and independently factorized same-stage draws are essential. Novelty is a best-knowledge claim, not an independent priority certification.

## References

1. Adrian Baule, *Masked diffusion as random sequential adsorption: an exactly solvable model for parallel decoding*, arXiv:2611.07845v1, https://arxiv.org/html/2611.07845v1 (first public: November 5, 2026), especially sections I–V and Appendix C.
2. Sitan Chen, Kevin Cong, Jerry Li, *Optimal inference schedules for masked diffusion models*, arXiv:2511.04647v2, https://arxiv.org/html/2511.04647v2 (first public: November 6, 2025), especially Theorem 1.4 and discussion of optimal schedules.
3. Hugo Lavenant, Giacomo Zanella, *Error bounds and optimal schedules for masked diffusions with factorized approximations*, arXiv:2510.25544v2, https://arxiv.org/html/2510.25544v2 (first public: October 29, 2025), especially sections 4 and 5.
