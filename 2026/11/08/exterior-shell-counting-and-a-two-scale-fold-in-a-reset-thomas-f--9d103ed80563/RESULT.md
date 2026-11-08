# Exterior-shell counting and a two-scale fold in a reset Thomas–Fermi condensate

## Finding

In the stationary, Poisson-reset Thomas–Fermi expansion of a one-dimensional weakly repulsive Bose condensate, consider the macroscopic fraction \(K_{a,b}\) of particles in the *two-sided exterior shell* \(a<|x|/x_0<b\), where \(1\le a<b<\infty\). Let \(\Lambda\ge1\) be the stationary random expansion factor, let \(r_0=r/(\sqrt2\,\omega)>0\), and set
\[
S(\lambda)=\Pr(\Lambda\ge\lambda)
=\exp\!\left[-r_0\left(\sqrt{\lambda(\lambda-1)}+
\operatorname{arsinh}\sqrt{\lambda-1}\right)\right],\qquad
h(\lambda)=-S'(\lambda)=r_0\sqrt{\frac{\lambda}{\lambda-1}}S(\lambda).
\]
Define the geometry-only critical scale and maximum shell fraction by
\[
\lambda_c=\sqrt{a^2+ab+b^2},\qquad
k_c=\frac{b-a}{\lambda_c}.
\]
Then \(0<k_c<1\) and the complete law is the atom-plus-density measure
\[
\boxed{\Pr(K_{a,b}\in dk)=[1-S(a)]\,\delta_0(dk)
+\mathbf1_{0<k<k_c}\,g_{a,b}(k)\,dk.}
\]
For each \(0<k<k_c\), there are **exactly two** expansion scales \(\lambda_-(k)\in(a,\lambda_c)\) and \(\lambda_+(k)\in(\lambda_c,\infty)\) yielding this count, and
\[
g_{a,b}(k)=\frac{h(\lambda_-(k))}{|k'(\lambda_-(k))|}
+\frac{h(\lambda_+(k))}{|k'(\lambda_+(k))|},
\qquad
\boxed{\Pr(K_{a,b}>k)=S(\lambda_-(k))-S(\lambda_+(k)).}
\]
Here \(k'(\lambda)\) denotes the derivative of the deterministic shell-count map defined below, not differentiation of its value parameter. The upper endpoint \(k_c\) is independent of the resetting rate.

The two distinct lower-endpoint regimes are sharp:
\[
\boxed{g_{a,b}(k)\sim
\begin{cases}
\displaystyle\frac{a\,h(a)}{\sqrt6}\,k^{-1/2},&a>1,\\[6pt]
\displaystyle\frac{r_0}{\sqrt6}\left(\frac32\right)^{1/4}k^{-3/4},&a=1,
\end{cases}\qquad k\downarrow0.}
\]
For \(a>1\), the zero atom is strictly positive. For \(a=1\), it vanishes, but the density is more singular. At the geometry-controlled upper edge,
\[
\boxed{g_{a,b}(k)\sim
h(\lambda_c)\sqrt{\frac{2\lambda_c^3}{3(b-a)}}
(k_c-k)^{-1/2},\qquad k\uparrow k_c.}
\]
The contribution from the *large-scale* inverse branch is exponentially negligible at the lower edge, with its exact logarithmic rate
\[
\lim_{k\downarrow0}k\log\left[
\frac{h(\lambda_+(k))}{|k'(\lambda_+(k))|}\right]
=-\frac{3r_0(b-a)}{2}.
\]
Moreover, conditioned on any \(0<k<k_c\), the expansion scale has two-point conditional weights proportional to the two summands of \(g_{a,b}(k)\). These weights both converge to \(1/2\) as \(k\uparrow k_c\). This gives a universal, two-scale ambiguity in inferring cloud size from a near-maximum exterior-shell count.

## Assumptions and scope

The source model starts with an initial one-dimensional Thomas–Fermi density of half-width \(x_0>0\), expands self-similarly after release from the longitudinal trap, and undergoes global instantaneous resets at Poisson rate \(r>0\). The original trap frequency \(\omega>0\) fixes the scale clock. For every fixed expansion factor \(\lambda\ge1\), the normalized spatial density in \(z=x/x_0\) is
\[
p(z\mid\lambda)=\frac{3}{4\lambda}\left(1-\frac{z^2}{\lambda^2}\right)
\mathbf1_{|z|<\lambda}.
\]
The single stationary random variable \(\Lambda\) is distributed according to \(h\) above. We study \(K_{a,b}=\int_{a<|z|<b}p(z\mid\Lambda)\,dz\) for **every** \(r_0>0\) and \(1\le a<b<\infty\), with fixed finite spatial cutoffs. The theorem concerns macroscopic, resetting-induced fluctuations of \(N_{a,b}/N\) in the Thomas–Fermi hydrodynamic approximation. Microscopic quantum counting fluctuations are neglected, consistent with the motivating model's counting-statistics approximation. These expressions are not a finite-particle quantum full-counting theorem.

## Proof

**1. Exact count map and its monotonicity.** Direct integration of the conditional inverted-parabola profile over both positive and negative parts of the shell gives
\[
k(\lambda):=\int_{a<|z|<b}p(z\mid\lambda)\,dz
=\begin{cases}
0,&1\le\lambda\le a,\\[3pt]
\displaystyle1-\frac{3a}{2\lambda}+\frac{a^3}{2\lambda^3},&a<\lambda\le b,\\[6pt]
\displaystyle\frac{3(b-a)}{2\lambda}-\frac{b^3-a^3}{2\lambda^3},&\lambda>b.
\end{cases}
\]
The two positive branches match continuously with the same first derivative at \(\lambda=b\). Their derivatives are
\[
k'(\lambda)=\begin{cases}
\displaystyle\frac{3a(\lambda^2-a^2)}{2\lambda^4}>0,&a<\lambda<b,\\[6pt]
\displaystyle\frac{3(b-a)(a^2+ab+b^2-\lambda^2)}{2\lambda^4},&\lambda>b.
\end{cases}
\]
Since \(a^2+ab+b^2>b^2\), \(k\) grows strictly from zero at \(a\) to its unique peak at \(\lambda_c>b\), then decreases strictly to zero as \(\lambda\to\infty\). Substitution at the critical scale yields \(k(\lambda_c)=k_c\). These facts prove the two inverse branches and that no further positive-count branches or atoms occur. They also show \(k_c<1\).

**2. Exact stationary law.** The known stationary expansion-scale survival \(S\) follows from the Poisson age law and the invertible deterministic scale clock. Because \(k\) is identically zero on \([1,a]\), that event has probability \(1-S(a)\). For \(0<k<k_c\), the event \(K_{a,b}>k\) is precisely \(\lambda_-(k)<\Lambda<\lambda_+(k)\); integration of \(h=-S'\) gives the boxed survival identity. Differentiating it, with the inverse function theorem on both smooth branches, produces the stated density. Letting \(k\downarrow0\) and \(k\uparrow k_c\) shows normalization: the total smooth mass is \(S(a)\), while the atom carries \(1-S(a)\). The conditional two-point distribution of \(\Lambda\) given a regular value of \(K_{a,b}\) is the standard change-of-variables disintegration with normalized branch weights.

**3. Lower-edge asymptotics.** At \(\lambda=a\), the count has a quadratic contact:
\[
k(a+u)=\frac{3u^2}{2a^2}+O(u^3),\qquad
\lambda_-(k)-a\sim a\sqrt{\frac{2k}{3}},\qquad
\frac{d\lambda_-}{dk}\sim\frac{a}{\sqrt6}\,k^{-1/2}.
\]
If \(a>1\), \(h\) is continuous and positive at \(a\), which gives the first lower-edge coefficient. If \(a=1\), the stationary density instead obeys \(h(1+u)\sim r_0u^{-1/2}\); composing the two asymptotics yields the \(k^{-3/4}\) coefficient. The far-scale branch has \(\lambda_+(k)\sim3(b-a)/(2k)\). Since \(\log h(\lambda)=-r_0\lambda+O(\log\lambda)\) and \(|k'(\lambda)|\) is polynomial in \(\lambda^{-1}\), its contribution has the asserted logarithmic rate and is negligible against either power law.

**4. Upper-edge fold and inverse ambiguity.** At the unique peak, direct differentiation gives
\[
k''(\lambda_c)=-\frac{3(b-a)}{\lambda_c^3}<0,
\quad
k_c-k(\lambda_c+u)=\frac{3(b-a)}{2\lambda_c^3}u^2+O(u^3).
\]
For \(\delta=k_c-k\downarrow0\), the inverse scales have displacements
\[
\lambda_\pm(k)=\lambda_c\pm
\sqrt{\frac{2\lambda_c^3}{3(b-a)}}\sqrt\delta+O(\delta).
\]
Each inverse Jacobian is asymptotic to half the square-root prefactor times \(\delta^{-1/2}\), while \(h(\lambda_\pm)\to h(\lambda_c)>0\). Adding the two contributions proves the upper-edge coefficient. Their ratio tends to one, proving equal conditional weights at the fold. All exponents \(-1/2\), \(-3/4\), and \(-1/2\) are locally integrable, as required by the probability law.

## Verification

The standalone script `verify_shell.py` evaluates independent symbolic identities for the piecewise count, matching conditions, derivatives and critical geometry. Numerical checks for six separated choices of \((a,b,r_0)\) then compare the two-branch probability with direct numerical integration over expansion scales, compare the Jacobian density with numerical differentiation, and test both endpoint prefactors and the equal-weight fold limit. The script completed 381 assertions on the stated computational environment. These finite calculations support reproducibility and do not establish the theorem's universal quantifiers; all-parameter claims are proved analytically above.

## Relationship to prior work

Mesquita, Kulkarni, Majumdar and Sabhapandit (2026), arXiv:2609.37110, derive the Thomas–Fermi expansion, the stationary scale law \(h\), and the full counting statistics **for one centered interval** \([-L,L]\) [their Eqs. (48)–(49), (63)–(69), and Appendix H]. Their centered-interval count is monotone in the scale, and its positive lower endpoint has a suppressed essential singularity. Those inputs and their method of pushforward from reset age are prior work, not claimed here. The present result treats the distinct, physically natural **two-sided exterior shell** \(a<|z|<b\). It classifies for all admissible shell radii a nonmonotone two-inverse map, the sharp geometry-only maximum, the atom at zero, two distinct lower-edge exponents, the fold singularity, and the conditional inverse ambiguity. These properties do not follow by substituting a new radius into a single centered-interval marginal, because the two centered counts are perfectly coupled through the same random expansion scale. The exact law requires the joint dependence and both inverse branches. Related work on fermionic annular counting involves a different, nonreset model and does not imply these Thomas–Fermi reset statistics. This is a bounded literature comparison, not a guarantee of publication priority.

## Limitations

The theorem concerns only the large-particle-number, hydrodynamic Thomas–Fermi approximation under ideal global Poisson resetting. It does not include quantum number shot noise, imperfect resets, arbitrary initial density shapes, finite imaging resolution, or a finite-particle error estimate. Endpoint limits hold for fixed \(r_0\) and fixed \(a,b\), not uniformly as the cutoffs merge or the rate vanishes. The conditional two-point interpretation applies to regular observed counts strictly between zero and the maximum; at zero an atom may be present and the conditional scale distribution is not two-point. A more general unindexed result about nonmonotone pushforwards could subsume the elementary fold mechanism; the model-specific full classification and comparison should be independently checked for publication priority.

## References

1. N. Mesquita, M. Kulkarni, S. N. Majumdar, and S. Sabhapandit, *Weakly interacting Bose-Einstein condensate with stochastic resetting*, arXiv:2609.37110 (first publicly available September 29, 2026), https://arxiv.org/abs/2609.37110. Inspected main stationary counting section and Appendix H, together with the expansion and scale-density formulas.
2. P. Goswami, A. Dhar, S. N. Majumdar, and A. Kundu, *Entanglement Scaling and Full Counting Statistics in Excited States of Two-Dimensional Rotating Fermions*, arXiv:2608.05722 (2026), https://arxiv.org/abs/2608.05722. Related annular observable in a different quantum system; only bibliographic material and an abstract were available for this comparison.
