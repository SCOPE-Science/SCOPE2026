# Maximal face-equilibrium probability and stable-state law in Gaussian coupled replicators

## Finding

A two-strategy coupled-population evolutionary game can have a stationary point in the relative interior of **every face** of its strategy cube. In the independent Gaussian payoff ensemble with within- and between-population encounters, the probability of this maximally populated phase, the number of attracting states in that phase, and its sharp large-population decay have exact laws.

For every integer \(m\ge1\), define \(N_m\) as the number of distinct isolated stationary states in the closed strategy cube \([0,1]^m\). Almost surely \(N_m\le3^m\), and equality holds precisely when
\[
|a_{ii}|>2|h_i|+\sum_{j\ne i}|a_{ij}|\qquad (1\le i\le m).
\]
When equality holds, all \(3^m\) equilibria are hyperbolic. With \(K=\#\{i:a_{ii}>0\}\), exactly \(2^K\) are locally asymptotically stable relative to the full cube.

For independent standard normals \(Z_0,\ldots,Z_m\), put
\[
q_m=\Pr\!\left(|Z_0|>\sum_{j=1}^{m-1}|Z_j|+\sqrt m\,|Z_m|\right).
\]
Then the exact maximum-phase probability and conditional attractor law are
\[
\Pr(N_m=3^m)=q_m^m,\qquad K\mid\{N_m=3^m\}\sim\operatorname{Binomial}(m,\tfrac12).
\]
Consequently the probability of simultaneous maximal multiplicity and exactly \(2^k\) stable states is \(q_m^m\binom mk2^{-m}\), for integers \(0\le k\le m\). In particular, \(q_1=1/2\), \(q_2=1/6\), and \(\Pr(N_2=9)=1/36\).

The sharp rarity constant is
\[
\boxed{\log\Pr(N_m=3^m)=-\frac12m^2\log m+\frac12\!\left(1+\log\frac2\pi\right)m^2+O(m^{3/2})}.\tag{1}
\]

## Assumptions and scope

Fix an arbitrary positive integer \(m\). For each population \(i=1,\ldots,m\), the frequencies of its two behaviors are \(x_i\) and \(1-x_i\). Draw all \((2m)^2\) payoffs \(\beta_{rs}\) independently from the standard normal distribution and hold them fixed along each evolutionary trajectory. An individual using strategy \(r\) receives expected payoff
\[
\pi_r(x)=\sum_{j=1}^m[\beta_{r,2j-1}x_j+\beta_{r,2j}(1-x_j)].
\]
The usual within-population and cross-population comparisons yield the deterministic game, conditional on the payoffs:
\[
\dot x_i=x_i(1-x_i)f_i(x),\qquad f_i(x)=\pi_{2i-1}(x)-\pi_{2i}(x).
\]
Set \(b_{ij}=\beta_{2i-1,2j-1}-\beta_{2i,2j-1}\) and \(c_{ij}=\beta_{2i-1,2j}-\beta_{2i,2j}\), and define
\[
a_{ij}=b_{ij}-c_{ij},\qquad h_i=\tfrac12\sum_{j=1}^m(b_{ij}+c_{ij}).
\]
Thus \(f_i(x)=h_i+\sum_j a_{ij}(x_j-1/2)\). Within-population interactions are essential: there is no assumption that \(a_{ii}=0\). Distinct Gaussian payoffs, not independent chosen polynomial coefficients, define the probability law. The classification refers to ordinary rest points, not only Nash equilibria, and to local dynamical stability, not global attractor basins.

## Proof

**1. Gaussian reduction.** For each row \(i\), the \(2m\) Gaussian differences \(b_{ij},c_{ij}\) are independent with law \(N(0,2)\). Orthogonal sum/difference combinations show that all \(a_{ij}\) are independent \(N(0,4)\), the \(h_i\) are independent \(N(0,m)\), and every \(h_i\) is independent of every \(a_{kj}\). Although the conventional uncentered intercept is correlated with the slopes, the centered intercept is independent. Different rows use disjoint microscopic payoffs. Therefore the desired diagonal-dominance events are independent across \(i\).

**2. Complete face classification.** Label every relatively open face of \([0,1]^m\) by a word in \(\{0,1,*\}^m\). On a face with free index set \(F\), an interior equilibrium must solve \(f_i(x)=0\) for each \(i\in F\). Since the corresponding principal matrix \(A_{FF}\) is nonsingular almost surely (its determinant is a nonzero polynomial in independent continuous Gaussian entries), each open face contains at most one equilibrium. There are exactly \(3^m\) faces, so \(N_m\le3^m\) almost surely. Vertices count as zero-dimensional faces.

For every one-dimensional edge with free coordinate \(i\), its root lies in \((0,1)\) if and only if
\[
\left|h_i+\frac12\sum_{j\ne i}\varepsilon_j a_{ij}\right|<\frac12|a_{ii}|,
\qquad\varepsilon_j\in\{-1,+1\}.
\]
All such edges have roots precisely when \(2|h_i|+\sum_{j\ne i}|a_{ij}|<|a_{ii}|\). The maximum absolute value over the finite sign choices is \(|h_i|+\frac12\sum_{j\ne i}|a_{ij}|\). Hence achieving \(3^m\) equilibria forces all the asserted inequalities.

Conversely, under those strict inequalities, for any face with free set \(F\) and fixed choices \(x_j\in\{0,1\}\), define
\[
T_i(x_F)=\frac12-\frac{h_i+\sum_{j\notin F}a_{ij}(x_j-1/2)+\sum_{j\in F\setminus\{i\}}a_{ij}(x_j-1/2)}{a_{ii}},\quad i\in F.
\]
The strict bounds ensure \(T\) maps the closed free-coordinate cube strictly inside itself. Its sup-norm Lipschitz constant is at most \(\max_{i\in F}\sum_{j\in F\setminus\{i\}}|a_{ij}|/|a_{ii}|<1\), so Banach's contraction theorem gives exactly one root in the relative interior of every face. This proves equivalence and full multiplicity.

**3. Exact stability census.** At a face equilibrium the Jacobian is block triangular, with the free block \(D_FA_{FF}\), where \(D_F=\operatorname{diag}(x_i(1-x_i):i\in F)>0\), and the fixed-coordinate normal eigenvalues \((1-2x_j)f_j(x)\). Strict row dominance makes the sign of \(f_i\) at \(x_i=0\) equal to \(-\operatorname{sgn}(a_{ii})\), and at \(x_i=1\) equal to \(+\operatorname{sgn}(a_{ii})\), uniformly over all other coordinates. Therefore each fixed normal eigenvalue has sign \(-\operatorname{sgn}(a_{ii})\). The Gershgorin discs of \(D_FA_{FF}\) lie strictly in the open right or left half-plane according to the sign of \(a_{ii}\). Scaling its off-diagonal entries continuously to zero cannot move any eigenvalue across the imaginary axis. Consequently the free block has exactly as many unstable directions as it has positive diagonal coefficients. The unstable dimension at a face point is
\[
\#\{i\in F:a_{ii}>0\}+\#\{i\notin F:a_{ii}<0\}.
\]
It vanishes if and only if every positive-diagonal coordinate is fixed, while every negative-diagonal coordinate is free. The former coordinates independently take values zero or one, giving exactly \(2^K\) sinks, and all other equilibria are hyperbolic saddles or sources.

**4. Gaussian probability and conditional sink distribution.** Dividing each dominance inequality by two converts its \(i\)-th row into
\[
|Z_0|>\sum_{j=1}^{m-1}|Z_j|+\sqrt m|Z_m|.
\]
Row independence gives probability \(q_m^m\). Every strict inequality is invariant under independently changing the sign of any diagonal coefficient. Hence conditional on simultaneous dominance, the signs \(\operatorname{sgn}(a_{ii})\) remain independent fair coin flips, giving the binomial law and the joint formula. When \(m=1\) the event compares two independent normal magnitudes, so \(q_1=1/2\). When \(m=2\), symmetry maps the event to eight equal spherical cones in the eight octants of \(\mathbb R^3\). One cone is spanned by unit rays \((1,0,0)\), \((1,1,0)/\sqrt2\), and \((\sqrt2,0,1)/\sqrt3\). Their spherical triangle has angles \(\pi/2\), \(\pi/4\), and \(\pi/3\), as follows directly from tangent-vector dot products at its three vertices. Girard’s spherical-excess formula therefore gives
\[
\Omega=\frac\pi2+\frac\pi4+\frac\pi3-\pi=\frac\pi{12}.
\]
Thus \(q_2=8\Omega/(4\pi)=1/6\), yielding the exact all-nine probability \(1/36\).

**5. Superexponential asymptotic, with quantitative remainder.** For \(m\ge2\), write \(X,Y_1,\ldots,Y_{m-1},W\) for independent half-normal magnitudes, and \(L=X-\sum_jY_j-\sqrt mW\). Put \(s=\sqrt m\) and \(M=\mathbb E e^{sL}\). The half-normal moment transforms satisfy
\[
\mathbb E e^{sX}=2e^{s^2/2}\Phi(s),\qquad
\mathbb E e^{-sX}=2e^{s^2/2}\Phi(-s)=\sqrt{2/\pi}s^{-1}(1+O(s^{-2})),
\]
where \(\Phi\) is the standard normal cdf. Independence therefore yields
\[
\log M=-\frac m2\log m+\left(\frac12+\log\sqrt{\frac2\pi}\right)m+O(\log m).
\]
Markov's inequality implies \(q_m=\Pr(L>0)\le M\). Under the exponentially tilted law \(d\mathbb P_s=e^{sL}d\mathbb P/M\), the centered variable \(X-s\) tends to \(N(0,1)\), the centered triangular sum \(\sum_jY_j-s\) tends to an independent \(N(0,1)\) by the Lindeberg central limit theorem, and \(\sqrt m W\to0\) in probability. Thus \(L\Rightarrow N(0,2)\) under \(\mathbb P_s\), whence \(\mathbb P_s(0<L<1)\) stays bounded away from zero. Reversing the tilt gives \(q_m=M\mathbb E_s[e^{-sL}\mathbf1_{L>0}]\ge M e^{-s}\mathbb P_s(0<L<1)\). It follows that \(\log q_m=\log M+O(\sqrt m)\). Multiplying by \(m\) proves equation (1), including the stated \(O(m^{3/2})\) remainder.

## Verification

The standalone Python 3 script `checker.py` uses exact rational linear algebra to enumerate every relative-face equilibrium in strictly dominant three- and four-population examples. It confirms \(27\) and \(81\) equilibria and, from the proved Jacobian sign rule, \(4\) sinks in each. It independently checks the trihedral angle identity giving \(q_2=1/6\). Run with `python3 checker.py`; no third-party packages are needed. Additional nonessential Monte Carlo sampling of \(100000\) independent microscopic two-population Gaussian payoff matrices gave frequency \(0.02822\), compared to the exact \(1/36=0.027777\ldots\). These finite tests are not proofs of the infinite-dimensional or asymptotic assertions; the preceding arguments are the certificates for those claims.

## Relationship to prior work

Mocenni, Moraes, and Santos (2026) analyze boundary mixed states for networked evolutionary games without diagonal self-interaction and prove a structural instability/degeneracy result for mixed players. They explicitly identify self-regulation as a possible stabilizing extension. Their equilibrium equations motivate the face-by-face approach, but the present result uses an **independent random payoff ensemble retaining self-interaction**; it is not a theorem for their zero-diagonal model.

Madeo and Mocenni (2021) developed self-regulated evolutionary games with an internal feedback term and analyzed mixed consensus. That mechanism is established prior work; no new stabilization principle is claimed here. Instead, the result jointly quantifies **all** face equilibria, their attracting-state count, and a sharp Gaussian rare-event probability.

Song, Duong, and Han (arXiv:2611.23223, first public November 17, 2026) subsequently examine the same microscopic Gaussian payoff ensemble for two and three populations, reporting per-candidate probabilities and Monte Carlo count histograms. Their two-population histogram records roughly 0.0277 at nine equilibria, consistent with the exact \(1/36\) here. The sections of their main text inspected do not supply the all-population dominance equivalence, conditional binomial sink law, or quadratic-scale large-population rarity. Their supplementary material was not independently retrieved, so equivalence hidden there remains a priority risk. This November 2026 source is comparative literature; the starting problem was posed by the June 2026 boundary-equilibrium paper.

## Limitations

The probabilities apply only to the specified independent Gaussian *microscopic payoff* ensemble; replacing payoffs by independent affine coefficients generally changes the event probability. This is a per-game deterministic evolutionary flow sampled from a distribution of games, not temporally noisy evolution. The result counts rest points, including non-Nash stationary vertices, and proves local stability only; it does not calculate attraction basins or prove global convergence. The superexponential asymptotic takes the number of populations to infinity and does not give a finite-population biological prediction. The numerical checker cannot validate the analytic large-population limit. Historical priority is bounded by accessible full text and search, and not independently audited.

## References

1. C. Mocenni, J. C. Moraes, and M. C. Santos, *On the Structure and Stability of Boundary Mixed Steady States in Evolutionary Games on Networks*, first posted 2026-06-14, https://arxiv.org/abs/2606.20688 .
2. D. Madeo and C. Mocenni, *Consensus towards Partially Cooperative Strategies in Self-Regulated Evolutionary Games on Networks*, Games 12 (2021), article 60, https://doi.org/10.3390/g12020060 .
3. Z. Song, M. H. Duong, and T. A. Han, *Equilibrium Statistics and Stability in Random Two-Population and Three-Population Evolutionary Games*, first posted 2026-11-17, https://arxiv.org/abs/2611.23223 . This is later comparative literature, not the originating June 2026 paper.
