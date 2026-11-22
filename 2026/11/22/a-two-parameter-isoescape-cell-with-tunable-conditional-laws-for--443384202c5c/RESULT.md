# A two-parameter isoescape cell with tunable conditional laws for negative doubling

## Finding

**Theorem (all-horizon isoescape with changing terminal laws).** Let \(T:[0,1]\setminus\{1/2\}\to[0,1]\) be the negative-doubling map
\[
T(x)=\begin{cases}1-2x,&0\le x<1/2,\\2-2x,&1/2<x\le1.\end{cases}
\]
For every pair of real parameters
\[
\frac13<a<\frac25,\qquad \frac35<b<\frac23,
\]
let \(H=(a,b)\), \(h=b-a\), and let \(X_0\) be uniform on \([0,1]\) with \(X_j=T^j(X_0)\) until its first entry into \(H\). The value of \(T(1/2)\) is immaterial because \(1/2\in H\). For every integer \(n\ge0\),
\[
\boxed{\Pr(X_j\notin H\text{ for all }0\le j\le n)
=\frac{1-h+n(1-3h)}{2^n}.}
\]
Thus **every pair of holes of equal length lying in this open parameter rectangle has exactly the same entire escape-time distribution**, not merely the same exponential rate. The rate is \(\log2\) and the survival prefactor is asymptotically linear.

For the state at the last surviving observation, the conditional law of \(X_n\) given survival through \(n\) converges in total variation to
\[
\boxed{\frac{3a-1}{1-3h}\,\operatorname{Unif}[1-2a,a]
+\frac{2-3b}{1-3h}\,\operatorname{Unif}[b,2-2b].}
\]
The weights are both strictly positive. At fixed \(h\), the left weight varies strictly with \(a\), so **identical escape-time laws need not determine the terminal survivor law**. In particular the two non-reflected, unequal holes
\[
H_1=(9/25,61/100),\qquad H_2=(19/50,63/100)
\]
both have \(h=1/4\) and survival probability \((n+3)/2^{n+2}\) at every horizon, but their limiting left-channel weights are \(8/25\) and \(14/25\), respectively. These holes are neither equal nor each other's reflection about \(1/2\).

The infinite-time survivor is countable and has zero topological entropy; its only periodic orbits are the two fixed points \(1/3\), \(2/3\) and the period-two orbit \(\{0,1\}\).

## Assumptions and scope

Lebesgue measure on the unit interval is normalized to probability one. A surviving trajectory is tested at all integer times from zero to the given horizon *inclusive*. The parameter inequalities are strict. All statements on Lebesgue distributions hold irrespective of the one-sided convention at finitely or countably many boundary preimages. The countability and periodic-orbit assertions use the natural branch map away from its hole, and no nonescaping orbit meets the discontinuity.

Set
\[
u=1-2a,\qquad w=2-2b,
\]
and partition the complement of the hole, up to endpoints, into four intervals in the order
\[
I_1=[0,u],\quad I_2=[u,a],\quad I_3=[b,w],\quad I_4=[w,1].
\]
Their respective lengths are \(u,3a-1,2-3b,2b-1\). Strict parameter bounds make each length positive.

## Proof

**1. Covering and transition structure.** On each \(I_i\), the map is affine and decreasing with absolute slope two. The four images, with irrelevant endpoint conventions omitted, are
\[
T(I_1)=[4a-1,1],\quad T(I_2)=[u,4a-1],\quad
T(I_3)=[4b-2,w],\quad T(I_4)=[0,4b-2].
\]
The strict inequalities \(a<4a-1<b\) and \(a<4b-2<b\) follow from the hypotheses. Consequently each image either covers an entire partition element or misses its interior. The source-to-destination adjacency matrix, in the stated interval order, is
\[
A=\begin{pmatrix}
0&0&1&1\\0&1&0&0\\0&0&1&0\\1&1&0&0
\end{pmatrix}.
\]
Equivalently, the outer intervals \(I_1,I_4\) alternate until leaving to the absorbing fixed-point channels \(I_3,I_2\), respectively.

**2. Exact transfer density.** Let \(\rho_n\) be the unnormalized Lebesgue density of \(X_n\) restricted to the event that \(X_0,\ldots,X_n\) all avoid \(H\). At time zero this density equals one on all four intervals. Every admissible inverse branch has absolute derivative \(1/2\); therefore its vector of constant interval densities evolves by \(p_{n+1}=A^\mathsf{T}p_n/2\) with \(p_0=(1,1,1,1)^\mathsf{T}\). Direct multiplication gives, for **every** integer \(n\ge0\),
\[
p_n=2^{-n}(1,n+1,n+1,1)^\mathsf{T}.
\]
Integrating over the four intervals yields
\[
\Pr(\tau>n)=2^{-n}\bigl[(1-2a)+(2b-1)
+(n+1)((3a-1)+(2-3b))\bigr].
\]
Since the outer lengths sum to \(2h\) and the inner lengths sum to \(1-3h\), this equals \(2^{-n}(1-h+n(1-3h))\). Here \(\tau=\inf\{j\ge0:X_j\in H\}\), with \(\inf\varnothing=\infty\). The formula tends to zero, hence \(\tau<\infty\) almost surely; its whole distribution is determined by these survival tails. Summation also gives \(\mathbb E\tau=4-8h\).

**3. Terminal conditional limit.** Given survival through time \(n\), the density is uniform on each of the four partition intervals with weights proportional to their lengths times \(1,n+1,n+1,1\), respectively. The total outer mass is \(2h/(1-h+n(1-3h))\), which tends to zero as \(n\to\infty\). The two inner masses converge to \((3a-1)/(1-3h)\) and \((2-3b)/(1-3h)\). As the underlying normalized restrictions to the four intervals do not depend on \(n\), this is convergence in total variation, not merely weak convergence.

**4. Non-identifiability and survivor structure.** At fixed \(h\), the exact survival formula is independent of hole placement, whereas the left-channel limiting weight \((3a-1)/(1-3h)\) is strictly increasing in \(a\). Each admissible fixed width \(1/5<h<1/3\) has a nonempty open interval of possible placements in the displayed rectangle. The two explicit rational examples verify non-identifiability without merely applying the reflection symmetry \(x\mapsto1-x\).

Finally the transition graph has only three directed cycles: loops at \(I_2\) and \(I_3\), and the alternating two-cycle \(I_1\leftrightarrow I_4\). Every infinite path in this finite graph either stays on one cycle forever or makes exactly one passage from the outer two-cycle to an inner loop. Thus the infinite itinerary set is countable. Expansion by two gives at most one point for each fixed itinerary (nested inverse cylinders shrink geometrically), proving countability of the survivor. The three periodic itineraries correspond to \(1/3\), \(2/3\), and \(\{0,1\}\). Their countable finite-type survivor has topological entropy zero, also directly from \(\rho(A)=1\) and polynomial path growth.

## Verification

The standalone `checker.py` uses only Python's exact `fractions.Fraction` class. It constructs survivor intervals by independent inverse-branch recursion, intersecting each preimage with the two allowed outer intervals. It checks the closed formula against 11 horizons for each of 42 rational parameter pairs, and checks the non-reflection example and distinct limiting weights. Invoke `python3 checker.py`. The complete proof for every real parameter and every horizon is the four-state transfer argument above, not the finite checks.

## Relationship to prior work

Ding, Steiner, and Sun (2026) define the negative-doubling interval map with arbitrary central hole and prove symbolic admissibility, plateau, and dimension devil's-staircase results, including Theorems 1.3–1.5; their inspected statements do not give this joint all-horizon Lebesgue law and terminal-density formula. A previously published symmetric-hole analysis gives the exact survival law on the diagonal \(b=1-a\). That is recovered on this cell by substituting \(h=1-2a\), but the diagonal statement does **not** imply invariance under independently varying \(a\) and \(b\), nor distinguish conditional survivor laws at fixed width. A published calculation at the single symmetric boundary hole \((2/5,3/5)\) derives a switching-time and terminal-profile phenomenon; its parameter and conclusion are different from the present open two-dimensional cell. Bunimovich and Yurchenko analyze hole-location effects for expanding maps and the trivial equality supplied by commuting measure-preserving symmetries. The current equal-width examples are neither reflection-related nor related by a small commuting translation, and the claim is equality at every finite horizon plus distinguishable terminal conditioning, not only equality of asymptotic escape rates.

## Limitations

The theorem asserts neither uniformity outside the displayed open Markov cell nor a global classification of isoescape families. It does not assert an invariant probability absolutely continuous with respect to Lebesgue measure supported on the infinite-time survivor. The limiting conditional terminal distribution is not an invariant survivor law: its support comprises positive-length intervals of points that may eventually escape. The finite-rational program is a consistency check and does not substitute for the exact covering proof. Priority comparison remains subject to unindexed or inaccessible historical work; independent mathematical audit has not been performed.

## References

1. Y. Ding, W. Steiner, Y. Sun, *Open dynamical systems in topologically expansive decreasing Lorenz maps*, arXiv:2610.03327v1, first public October 2, 2026. https://arxiv.org/abs/2610.03327
2. L. A. Bunimovich, A. Yurchenko, *Where to place a hole to achieve a maximal escape rate*, arXiv:0811.4438v1 (2008); Israel J. Math. **182** (2011), 229–252. https://arxiv.org/abs/0811.4438
3. *Exact escape-time phase transition for symmetric negative-doubling holes*, published mathematical research record, 2026-10-26. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-escape-time-phase-transition-for-symmetric-negative-doubli--ca3ad35b54de
4. *Exact uniform switching times and a polynomial escape tail at a negative-doubling critical hole*, published mathematical research record, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-uniform-switching-times-and-a-polynomial-escape-tail-at-a--36a44984c1f2
