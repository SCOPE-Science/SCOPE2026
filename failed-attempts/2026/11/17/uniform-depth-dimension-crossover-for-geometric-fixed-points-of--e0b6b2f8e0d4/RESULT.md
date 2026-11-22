# Uniform depth–dimension crossover for geometric fixed points of symmetric-power Lattès maps

## Finding
Let \(E\) be an elliptic curve over an algebraically closed field of characteristic zero. The multiplication map \([m]:E\to E\), for an integer \(m\ge2\), induces a rational Lattès map \(\ell_m:E/\{\pm1\}\cong\mathbb P^1\to\mathbb P^1\). Write \(F_{g,m}=\operatorname{Sym}^g(\ell_m):\mathbb P^g\to\mathbb P^g\), where \(\operatorname{Sym}^g\mathbb P^1\cong\mathbb P^g\).

For integers \(g,n\ge1\), let \(P_{g,n}\) be the proportion of elements of the **geometric** level-\(n\) iterated Galois group of \(F_{g,m}\) fixing a vertex of the generic level-\(n\) preimage fibre. Put \(P_{g,\infty}=\lim_{n\to\infty}P_{g,n}\), and define
\[
a_m=\begin{cases}\tfrac18,&2\mid m,\\[2pt]\tfrac12,&2\nmid m,\end{cases}\qquad \delta_{m,n}=\frac{m^{-2n}}{2}.
\]
Then, simultaneously for every integer \(g,m,n\) in the indicated domains,
\[
P_{g,n}=\frac{\Gamma(g+a_m+\delta_{m,n})}{\Gamma(a_m+\delta_{m,n})\Gamma(g+1)},\qquad
P_{g,\infty}=\frac{\Gamma(g+a_m)}{\Gamma(a_m)\Gamma(g+1)}.
\]
The pointwise finite-level formula is a specialization of established counting identities (see Relationship to prior work). The quantitative **uniform depth–dimension conclusion** is
\[
\boxed{\left|\log\frac{P_{g,n}}{P_{g,\infty}}-\frac{m^{-2n}}{2}\log g\right|\le7m^{-2n}.}
\]
For a fixed \(m\) and any integer sequence \(n(g)\ge1\), as \(g\to\infty\), the ratio \(P_{g,n(g)}/P_{g,\infty}\) tends to \(1\) **if and only if** \(m^{-2n(g)}\log g\to0\). More precisely, if the latter tends to \(\lambda\in(0,\infty)\), the former tends to \(e^{\lambda/2}\); if the latter diverges, so does the ratio. Thus the sharp transition in required iteration depth occurs at
\[
n\asymp\frac{\log\log g}{2\log m}.
\]
At infinite depth,
\[
P_{g,\infty}\sim \frac{g^{a_m-1}}{\Gamma(a_m)}.
\]
In contrast, omitting permutations and retaining only coordinatewise involutions on \(E^g\) gives exactly \(a_m^g\), an exponentially smaller limiting proportion. The distinction is intrinsic to symmetrization, not a difference in elliptic curves.

## Assumptions and scope
The base field is algebraically closed with characteristic zero; the preimage target is a geometric generic point. Parameters are integers \(m\ge2\), \(g\ge1\), and \(n\ge1\). The group of signed coordinate permutations is \(H_g=(\mathbb Z/2\mathbb Z)^g\rtimes S_g\); it acts on \(A=E^g\). Its quotient is \(A/H_g\cong\operatorname{Sym}^g(E/\{\pm1\})\cong\mathbb P^g\), and multiplication by \(m\) descends to the specified \(F_{g,m}\). The finite-level and limiting proportions are *geometric*, not the arithmetic Galois proportions over a number field.

## Proof
**1. Group and torsion reduction.** The known finite-level Lattès formula gives
\[
P_{g,n}=\frac1{|H_g|}\sum_{u\in H_g}\frac1{|E[m^n]^g\cap\ker(u-I)|}.
\]
Represent \(u\) by a permutation \(\pi\in S_g\) and independent coordinate signs. On each cycle of \(\pi\), the signed fixed-point condition reduces to \(z=\varepsilon z\) for one elliptic torsion coordinate, where \(\varepsilon\) is the product of the signs on that cycle. When \(\varepsilon=+1\), the kernel has \(m^{2n}\) points, since \(E[m^n]\cong(\mathbb Z/m^n\mathbb Z)^2\). When \(\varepsilon=-1\), the kernel has \(\gcd(2,m)^2\) points. For uniformly independent signs, the cycle products are independent fair signs. The mean reciprocal kernel cardinality per cycle is
\[
\frac12\left(m^{-2n}+\gcd(2,m)^{-2}\right)=a_m+\delta_{m,n}.
\]
Thus, writing \(c(\pi)\) for the number of cycles of \(\pi\),
\[
P_{g,n}=\frac1{g!}\sum_{\pi\in S_g}(a_m+\delta_{m,n})^{c(\pi)}.
\]
The classical permutation cycle identity \(\sum_{\pi\in S_g}t^{c(\pi)}=t(t+1)\cdots(t+g-1)\) gives the announced gamma quotient. Letting \(n\to\infty\) gives its limiting counterpart. Without permutations, the same cycle-wise count is simply \((a_m+\delta_{m,n})^g\), tending to \(a_m^g\).

**2. A uniform comparison that permits both parameters to grow.** Set \(a=a_m\), \(\delta=\delta_{m,n}\). The *exact* ratio satisfies
\[
\log\frac{P_{g,n}}{P_{g,\infty}}=\sum_{j=0}^{g-1}\log\left(1+\frac{\delta}{a+j}\right).
\]
The elementary inequalities \(x-x^2/2\le\log(1+x)\le x\) for \(x\ge0\) give, with \(H=\sum_{j=0}^{g-1}(a+j)^{-1}\) and \(J=\sum_{j=0}^{g-1}(a+j)^{-2}\),
\[
\delta H-\frac{\delta^2 J}2\ \le\ \log\frac{P_{g,n}}{P_{g,\infty}}\ \le\ \delta H.
\]
Since \(a\in\{1/8,1/2\}\), \(0<\delta\le1/8\), and \(g\ge1\), integral comparison yields
\[
\log g\le H\le\log g+1+a^{-1},\qquad J\le a^{-2}+2.
\]
Therefore the absolute difference from \(\delta\log g\) is at most
\[
\delta(1+a^{-1})+\frac{\delta^2}2(a^{-2}+2)\le 14\delta=7m^{-2n}.
\]
This bound is uniform in all three integer parameters. For a fixed \(m\), if \(m^{-2n(g)}\log g\to\lambda<\infty\), then \(n(g)\to\infty\), and the bound proves the claimed ratio \(e^{\lambda/2}\). If the parameter diverges, the lower bound gives divergence whenever \(n(g)\to\infty\); when \(n(g)\) remains bounded along a subsequence, the exact product grows by at least a positive multiple of \(\log g\). Equivalently, the bound plus \(\log(1+x)\ge x/(1+x)\) shows globally \(\log(P_{g,n}/P_{g,\infty})\ge\delta\log g/2\), because \(\delta\le a\). This establishes necessity and all diverging cases without assuming \(n(g)\to\infty\). The transition is \(m^{-2n}\log g\asymp1\), or \(n=(\log\log g)/(2\log m)+O(1)\).

**3. Infinite-depth dimension law.** For fixed \(a>0\), the classical gamma-ratio asymptotic \(\Gamma(g+a)/\Gamma(g+1)\sim g^{a-1}\) completes the proof.

## Verification
The accompanying self-contained `verify.py` performs exact-rational cycle-index checks for multiple small dimensions, multipliers and levels; compares direct enumeration of signed permutation torsion kernels with the formula; and evaluates the uniform inequality and predicted crossover numerically. It outputs `VERIFY_OK` on success. Finite numerical tests corroborate the algebraic identities; the universal statements follow from the proof above, not from enumeration.

## Relationship to prior work
Xin Li's 2026 theorem supplies the general Lattès torsion counting formula and its fixed-dimension limit; this is expressly not claimed anew. Boston et al. (1993), as restated and discussed by Arumugam–Dietrich–Glasby (2022), give the general fixed-point proportion formula for finite-group wreath products in product action; this implies the fixed-dimensional rising-factorial expression after the one-coordinate Lattès calculation. In particular, the gamma quotient by itself is **not** the proposed novelty. What is isolated here is the uniform high-dimensional, finite-depth approximation law, its necessary-and-sufficient \(\log\log g\) threshold, and the contrast of polynomial versus exponential geometric survival for the natural symmetric and Cartesian powers of the same Lattès map. These assertions require simultaneously varying the dimension and iteration depth and are not stated in the inspected sources. They follow here by an explicit uniform harmonic-sum estimate. Claims of definitive historical priority or independent verification are not made.

## Limitations
Only multiplication-by-integer Lattès maps and the full symmetric powers are considered. Other finite subgroups of automorphisms, non-scalar isogenies, arithmetic Galois groups, characteristic-positive dynamics, and non-generic fibres are not covered. Existing general finite-group formulas already imply the fixed-parameter exact proportions; the interest of the new assertion is quantitative two-parameter uniformity, not a new generic fixed-point counting theorem. Historical priority requires independent specialist scrutiny.

## References
1. Xin Li, *The fixed-point proportion of Lattès maps*, arXiv:2611.07816v1 (first public version, 2026-11-05), https://arxiv.org/html/2611.07816v1, especially Proposition 3.4 and Corollary 7.1.
2. N. Boston et al., *The proportion of fixed-point-free elements of a transitive permutation group*, Communications in Algebra 21 (1993), 3259–3275, DOI:10.1080/00927879308824728.
3. V. Arumugam, H. Dietrich, and S. P. Glasby, *Derangements in wreath products of permutation groups*, arXiv:2207.01215 (first public version, 2022), https://arxiv.org/abs/2207.01215, Theorem 2.1.
