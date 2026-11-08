# Stretched-exponential scarcity and cube-root images of idempotent non-expansive fuzzy-chain operators

## Finding
For each integer \(m\ge1\), let \(L_m=\{0,1/m,\ldots,1\}\). Consider unary term operations on \(L_m\) constructed from one variable, constants in \(L_m\), minimum, maximum, involution \(u\mapsto1-u\), and truncated subtraction \(u\ominus c=\max(0,u-c)\). Two terms are identified if they induce the same unary function. These functions are exactly all maps \(f:L_m\to L_m\) with \(|f(u)-f(v)|\le|u-v|\).

Let \(I_m\) be the number of these functions satisfying \(f\circ f=f\). Define \(A_d\), for \(d\ge0\), to be the \((d+1)\)-square matrix indexed by \(\{0,\ldots,d\}\) with entry one exactly when the index difference is at most one, and put \(F_d(t)=(A_d^t\mathbf1)_0\) for integers \(t\ge0\). Then
\[
I_m=\sum_{d=0}^{m}\sum_{a=0}^{m-d}F_d(a)F_d(m-d-a).
\]
The first values, starting at \(m=1\), are \(3,8,21,56,149,395,1042,2741,7205,18961,50021\).

Writing
\[
t_*=\left(\frac{2\pi^2}{3\log3}\right)^{1/3},\qquad C_*=\frac32\,t_*\log3=3\left(\frac{\pi^2(\log3)^2}{12}\right)^{1/3},
\]
we have the sharp logarithmic asymptotic
\[
\log I_m=m\log3-C_*m^{1/3}+O(\log m).
\]
If \(N_m\) denotes the total number of unary term functions, including non-idempotent ones, then
\[
\log\frac{I_m}{N_m}=-C_*m^{1/3}+O(\log m).
\]
Moreover, for a uniformly chosen idempotent term function, let \(D_m=m(\max f-\min f)\) be the number of lattice steps across its image. Then \(D_m/m^{1/3}\to t_*\) in probability. Numerically, \(C_*\approx2.99265777654\) and \(t_*\approx1.81602300005\).

## Assumptions and scope
The finite truth chain is equipped with its ordinary absolute-value metric. Term functions are propositional and unary: no modal transition operators or additional variables are present. Every truth constant from \(L_m\) is available. Idempotence means idempotence under **composition of unary functions**, not idempotence of a connective on individual truth values. All limits are as the integer \(m\to\infty\). The random-function statement uses the uniform distribution on the finite set of idempotent unary term functions. The unscaled image width is an integer in \(\{0,\ldots,m\}\).

## Proof
**1. Exact description of unary terms.** Each permitted connective is non-expansive, and minimum/maximum preserve the one-Lipschitz property when both operands have it. Thus every term gives a one-Lipschitz function. Conversely, for a one-Lipschitz \(f:L_m\to L_m\), define
\[
D_a(x)=\max\{x\ominus a,(1-x)\ominus(1-a)\}=|x-a|.
\]
Truncated addition of a constant is definable from negation and truncated subtraction: \(u\oplus c=1-((1-u)\ominus c)\). The finite McShane identity
\[
f(x)=\min_{a\in L_m}\bigl(f(a)\oplus D_a(x)\bigr)
\]
holds: every summand is at least \(f(x)\) by the one-Lipschitz inequality, and choosing \(a=x\) gives equality. All functions counted below are therefore definable terms, not merely abstract metric maps.

**2. Retraction decomposition and exact count.** Identify \(L_m\) with \(\{0,\ldots,m\}\) by scaling by \(m\). A one-Lipschitz map sends consecutive input points to output points differing by at most one. Its image is therefore an integer interval \([a,a+d]\). The equation \(f^2=f\) is equivalent to fixing every point of its image; hence its values are the identity on \([a,a+d]\). On the left \(a\) input edges, values trace a walk in the strip \(\{a,\ldots,a+d\}\) starting at \(a\) when read outwards, with increments \(-1,0,1\). On the right \(m-a-d\) edges, values give a reflected walk starting at the other boundary. Their counts are respectively \(F_d(a)\) and \(F_d(m-a-d)\). Choosing \(a,d\) determines the image uniquely, so summing over the disjoint cases proves the exact expression for \(I_m\).

**3. Uniform strip-walk spectral bounds.** The Perron root of \(A_d\) is
\[
\lambda_d=1+2\cos\frac{\pi}{d+2}\quad(d\ge0).
\]
The spectral norm bound gives \(F_d(t)\le\sqrt{d+1}\lambda_d^t\). The square of the normalized Perron eigenvector's first coordinate is
\[
q_d=\frac{2}{d+2}\sin^2\frac{\pi}{d+2}\ge\frac8{(d+2)^3}.
\]
For even \(t\), spectral decomposition of \((A_d^t)_{00}\) consists of nonnegative terms, so \(F_d(t)\ge q_d\lambda_d^t\). For odd \(t\), append a self-loop to a returning walk of even length, obtaining \(F_d(t)\ge q_d\lambda_d^{t-1}\). This also gives a valid (weaker) inequality when \(t=0\). Uniformly for all \(d,t\ge0\),
\[
\frac8{(d+2)^3}\lambda_d^{t-1}\le F_d(t)\le\sqrt{d+1}\lambda_d^t.
\]
There are at most \((m+1)^2\) terms in the exact counting formula, and the lower bound may be applied to its term with \(a=0\). Thus
\[
\log I_m=\max_{0\le d\le m}(m-d)\log\lambda_d+O(\log(m+2)).
\]
The error is uniform in the maximizing width.

**4. Optimization and concentration.** Put \(h_d=\log(3/\lambda_d)\) and \(B_m(d)=d\log3+(m-d)h_d\). Taylor expansion at zero gives
\[
h_d=\frac{\pi^2}{3(d+2)^2}+O((d+2)^{-4})
\]
for large \(d\). For \(d=t m^{1/3}+O(1)\) with \(t\) restricted to any compact subinterval of \((0,\infty)\), uniformly
\[
\frac{B_m(d)}{m^{1/3}}=t\log3+\frac{\pi^2}{3t^2}+o(1).
\]
The limiting function diverges at both endpoints and has the unique minimizing argument \(t_*=(2\pi^2/(3\log3))^{1/3}\) and minimum \(C_*\). Indeed, for widths smaller than a sufficiently small multiple of \(m^{1/3}\), \(mh_d\) is too large, while for widths larger than a sufficiently large multiple, \(d\log3\) is too large (using \(B_m(d)\ge d\log3\) and the monotonicity of \(h_d\)). Therefore all minimizing widths lie in a compact multiple of \(m^{1/3}\), where a one-higher-order Taylor expansion yields \(\min_d B_m(d)=C_*m^{1/3}+O(1)\). Combining with step 3 proves the logarithmic asymptotic.

For each fixed \(\varepsilon>0\), the same compactness and strict uniqueness arguments give a positive excess \(\delta_\varepsilon m^{1/3}\) in \(B_m(d)\) whenever \(|d/m^{1/3}-t_*|\ge\varepsilon\), for sufficiently large \(m\). The uniform polynomial prefactors in step 3 and at most \(m+1\) widths cannot overcome this gap; dividing the total weight of such widths by \(I_m\) proves convergence in probability.

**5. Comparison with all terms.** Every one-Lipschitz map on the integer chain is encoded by its \(m\) increments from \(\{-1,0,1\}\), together with an initial value in \(\{0,\ldots,m\}\). For a fixed increment word, let \(R\) be the range of its prefix-sum walk. The number of valid starting values is \((m+1-R)_+\). For independent uniform increments, the maximal absolute displacement has expectation \(O(\sqrt m)\) by the maximal \(L^2\) inequality, hence \(\mathbb ER=O(\sqrt m)\). Thus
\[
3^m(m+1-O(\sqrt m))\le N_m\le3^m(m+1).
\]
In particular \(\log N_m=m\log3+O(\log m)\). Subtracting logarithms completes the rarity claim.

## Verification
Run `python3 checker.py` (standard Python library only). The checker independently enumerates all one-Lipschitz functions on chains with \(m\le5\) and compares the idempotent tally with the strip-walk formula. It verifies the first twelve exact counts, eight total-map counts using independent increment-walk dynamic programming, and direct walk counts for seven strip widths and thirteen walk lengths. Its reported successful completion is `ALL_CHAIN_RETRACTION_CHECKS_OK`. These finite checks do **not** establish the infinite asymptotic theorem; the spectral and optimization arguments above provide that proof.

## Relationship to prior work
Gebhart, Schröder and Wild (2026) establish uniform interpolation for non-expansive fuzzy modal logic and define the propositional connectives used here. Their theorem is about interpolation, not the idempotent unary term-function count or its asymptotic image profile. The McShane extension identity is standard and is not claimed as new. Knauer and Pipattanajinda (2018) count **all** weak endomorphisms of finite undirected paths; this is the comparison class \(N_m\), not the idempotent subclass \(I_m\). Dimitrova, Fernandes, Koppitz and Quinteiro (2018/2020) analyze ranks and regularity of the weak-endomorphism monoid of an **undirected** path and do not provide the present strip-walk enumeration and asymptotic. Fernandes and Paulista (2021/2023) count idempotents for **directed** paths, whose endomorphisms preserve order, and therefore do not cover the present nonmonotone walks or their stretched-exponential scaling. The novelty claim is limited to the combined idempotent count and asymptotic profile relative to inspected sources.

## Limitations
This theorem is for one variable, the specified finitary truth constants, and the propositional fragment; it is not a new interpolation theorem, a claim about arbitrary multimodal formulas, or a statement about continuum-valued random functions. Only the leading logarithmic deficit and image-width law are given; no exact polynomial prefactor, limiting fluctuation distribution, or uniform formula-size bound is established. Earlier semigroup-enumeration literature not identified by the searches could contain equivalent results. Independent proof and historical-priority validation have not been performed.

## References
1. S. Gebhart, L. Schröder, P. Wild, *Non-Expansive Fuzzy Modal Logic Has Uniform Interpolation* (first public October 23, 2026), arXiv:2610.32335, https://arxiv.org/abs/2610.32335.
2. S. Gebhart, L. Schröder, P. Wild, *Non-expansive Fuzzy ALC* (2025), arXiv:2505.09416, https://arxiv.org/abs/2505.09416.
3. U. Knauer, N. Pipattanajinda, *A formula for the number of weak endomorphisms on paths*, Algebra and Discrete Mathematics 26 (2018), 270–279, https://admjournal.luguniv.edu.ua/index.php/adm/article/view/349.
4. I. Dimitrova, V. H. Fernandes, J. Koppitz, T. M. Quinteiro, *Ranks of monoids of endomorphisms of a finite undirected path*, arXiv:1810.09307; Bull. Malays. Math. Sci. Soc. 43 (2020), 1623–1645.
5. V. H. Fernandes, T. Paulista, *On the Rank of Monoids of Endomorphisms of a Finite Directed Path*, arXiv:2112.13427 (2021); Asian-European Journal of Mathematics 16 (2023), 2350069.
