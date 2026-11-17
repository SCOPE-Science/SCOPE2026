# Sharp two-mode angular stability of spherical widths of signed permutohedra

## Finding
For every integer \(n\ge2\), let \(B_n\subset\mathbb R^n\) be the convex hull of all signed permutations of \((1,3,5,\ldots,2n-1)\). Let \(W_n(u)\) denote its Euclidean directional width for \(\|u\|_2=1\). Write \(|u|_{(1)}\le\cdots\le|u|_{(n)}\) for its sorted absolute coordinates. Then
\[
W_n(u)=2\sum_{j=1}^n(2j-1)|u|_{(j)}.
\]
Every local extremum of \(W_n\) on the unit sphere is strict. Its local minima are **exactly** the \(3^n-1\) signed-flat vectors \(u^{S,\varepsilon}\) whose nonzero coordinates, on a nonempty support \(S\subseteq[n]\) of size \(k\), equal \(\varepsilon_i/\sqrt{k}\), with independent signs \(\varepsilon_i\in\{-1,1\}\). At each such vector,
\[
W_n(u^{S,\varepsilon})=2\sqrt{k}(2n-k).
\]
There are precisely \(2^nn!\) local maxima: the normalized signed permutations of \((1,3,\ldots,2n-1)\), all attaining the common global maximum
\[
W_{\max}=2\sqrt{n(4n^2-1)/3}.
\]
For \(n\ge3\), precisely the \(2n\) signed coordinate-axis directions are global minima, of width \(2(2n-1)\); for \(n=2\), the four fully supported signed-flat directions are the global minima, of width \(4\sqrt2\).

More sharply, put \(m=n-k\), define
\[
c_m=\begin{cases}0,&m=0,\\\min\{2m-1,m\sqrt m\},&m\ge1,\end{cases}
\]
and set
\[
\gamma_{n,k}=\min\bigl(\{\sqrt{k(k-1)}:k\ge2\}\cup\{c_m:m\ge1\}\bigr).
\]
The minimum is taken over the indicated nonempty set. At **every** signed-flat minimum, for every real angle
\[
0<\theta<\arctan\!\frac1{2\sqrt{k}},
\]
the exact, attained minimum width among all unit directions at spherical angle \(\theta\) from that minimum is
\[
\boxed{\quad 2\sqrt{k}(2n-k)\cos\theta+2\gamma_{n,k}\sin\theta.\quad}
\]
Whenever \(2\le k<n\), the minimizing tangent direction has a strict two-mode transition: if \(k<2(n-k)\), it splits one active coordinate from the other active coordinates and leaves all zeros unchanged; if \(k\ge2(n-k)\), it moves only the formerly zero coordinates, keeping every active coordinate unchanged to first order. No parameter has both modes tied. At \(k=1\) only zero activation is available; at \(k=n\) only active splitting is available.

## Assumptions and scope
All norms, angles and widths use the standard ambient Euclidean structure. Signed permutations mean arbitrary permutations of the \(n\) distinct positive odd integers followed by independent coordinate sign choices. The Euclidean width is the length of the orthogonal projection onto the line spanned by the direction. A *local* extremum is relative to the entire unit sphere, not only to a reflection chamber. The geodesic profile concerns a fixed angular distance from a specified signed-flat direction and is only asserted on the displayed uniform open interval. The result is about this particular arithmetic-progression realization of the type-\(B\) permutohedron, not all deformations of its normal fan.

## Proof
**1. Signed rearrangement and exact support.** The maximum of \(u\cdot x\) over signed permutations \(x\) of \((1,3,\ldots,2n-1)\) is \(F_n(u)=\sum_{j=1}^n(2j-1)|u|_{(j)}\) by sign choice and the rearrangement inequality. Central symmetry gives \(W_n=2F_n\).

**2. Identification of every local minimum.** Use signed-coordinate symmetry to put a putative minimum at \(u\) with nonnegative coordinates. Suppose \(u\) has \(g\ge2\) distinct positive coordinate levels, with positive multiplicities \(s_1,\ldots,s_g\); zero coordinates are allowed. The relative stratum in which all these level ties and zeros remain fixed is locally parameterized by \(0<b_1<\cdots<b_g\), subject to \(\sum s_jb_j^2=1\). On this stratum \(F_n=\sum a_jb_j\), where each \(a_j\) is a positive sum of the corresponding odd rearrangement weights. If this linear functional has nonzero tangent differential, a descent direction exists. At its only possible stationary point, a Lagrange multiplier gives \(a_j=\lambda s_jb_j\) with \(\lambda=F_n>0\), and its restricted second variation is \(-F_n\sum s_j(\delta b_j)^2<0\) for every nonzero tangent perturbation. Thus no point of such a stratum is a local minimum.

It remains to examine the one-positive-level vectors. The exact angular inequality established in Step 4 below gives a positive outward slope in every tangent direction, proving that **all** such vectors are strict local minima. There are \(\sum_{k=1}^n\binom nk2^k=3^n-1\) of them. Their widths follow by summing the largest \(k\) odd coefficients: \(\sum_{j=n-k+1}^n(2j-1)=k(2n-k)\).

**3. Every local maximum.** At a point where two nonzero absolute coordinates are tied, an infinitesimal perturbation increasing one magnitude and decreasing the other, after normalizing back onto the sphere, increases \(F_n\) to first order: the two ordered coefficients differ by at least two. At a point with a zero coordinate, turning on that coordinate increases \(F_n\) to first order. Neither kind of point is a local maximum. In every open signed Weyl chamber \(F_n(u)=w\cdot u\), where \(w\) is the corresponding signed permutation of the odd vector. A positive linear functional on a spherical open chamber has a local extremum only at its direction \(u=w/\|w\|\), and there its Hessian on the sphere is \(-\|w\|\) times the tangent metric. This point is a strict maximum. All signed permutations are distinct, giving \(2^nn!\) global maxima. Finally \(\|w\|^2=\sum_{j=1}^n(2j-1)^2=n(4n^2-1)/3\).

**4. Exact tangent minimization.** Fix a signed-flat vector with support size \(k\), apply signed-coordinate symmetry, and suppose its \(k\) nonzero coordinates equal \(1/\sqrt k\). Every point at angle \(\theta\in(0,\pi)\) is \(u\cos\theta+v\sin\theta\) with \(v\perp u\), \(\|v\|=1\). Split \(v=(a,z)\) into the \(k\) active and \(m=n-k\) inactive coordinates. Orthogonality gives \(\sum_i a_i=0\). If \(\tan\theta<1/(2\sqrt k)\), all perturbed active coordinates remain positive and larger than all absolute inactive coordinates. Sorted rearrangement therefore yields the **exact identity**
\[
F_n(u\cos\theta+v\sin\theta)=\sqrt k(2n-k)\cos\theta+
\bigl(A_k(a)+C_m(z)\bigr)\sin\theta,
\]
where \(A_k(a)=\sum_{i<j}|a_i-a_j|\) for \(\sum_i a_i=0\), and \(C_m(z)=\sum_{j=1}^{m}(2j-1)|z|_{(j)}\). Missing blocks are interpreted as zero.

For \(k\ge2\), sort the coordinates of \(a\) and express it as a nonnegative linear combination of centered upper-step vectors: one step is the centered indicator of the top \(j\) entries, \(1\le j<k\). Such a step has Euclidean norm \(\sqrt{j(k-j)/k}\) and \(A_k\)-value \(j(k-j)\). Since \(j(k-j)\ge k-1\), the triangle inequality proves
\[
A_k(a)\ge\sqrt{k(k-1)}\,\|a\|_2.
\]
The bound is attained when one coordinate is different from the other \(k-1\) coordinates. For \(m\ge1\), similarly express the sorted nonnegative absolute coordinates of \(z\) as a nonnegative combination of indicators of the largest \(j\) coordinates. Their norm is \(\sqrt j\) and their \(C_m\)-value is \(j(2m-j)\); therefore
\[
C_m(z)\ge\left(\min_{1\le j\le m}\sqrt j(2m-j)\right)\|z\|_2.
\]
The scalar function \(\sqrt t(2m-t)\) increases and then decreases on \([1,m]\), so its minimum occurs at an endpoint, giving \(c_m=\min\{2m-1,m\sqrt m\}\). Equality is attained by one nonzero inactive coordinate when \(m\ne2\), and by two equal-magnitude inactive coordinates when \(m=2\). (The case \(m=1\) has only one coordinate.)

Since \(\|a\|_2^2+\|z\|_2^2=1\), the two inequalities imply \(A_k(a)+C_m(z)\ge\gamma_{n,k}\). Equality is attained by a **pure** active or inactive perturbation in the cheaper block. This proves the exact claimed fixed-angle profile and strict local minimality. All steps apply uniformly for every \(n\ge2\), and rely on inequalities over all real tangent vectors, not finite sampling.

**5. Exact mode threshold and global minima.** For \(m\ge3\), \(m\sqrt m>2m-1\), so \(c_m=2m-1\); for \(m=2\), \(c_m=2\sqrt2\); for \(m=1\), \(c_m=1\). In each of these cases, a direct comparison of squares gives
\[
\sqrt{k(k-1)}<c_m\quad\Longleftrightarrow\quad k<2m
\]
for integers \(k\ge2,m\ge1\), with strict reverse inequality otherwise. Thus the transition is exact, without ties. The global minimum of \(F_n\) can be found by the same upper-step decomposition used for \(C_m\), now with \(m=n\): it is \(\min\{2n-1,n\sqrt n\}\), with equality only at a signed-flat vector of support one for \(n\ge3\), or full support for \(n=2\). This gives the stated global minima and completes the proof.

## Verification
Run `python3 verify_signed_width.py` with standard Python 3. The checker uses integer arithmetic to test the active upper-step and inactive upper-step inequalities through \(n=80\), samples deterministic exact integer tangent directions, verifies attained equality rays for each mode, and enumerates all ternary signed-support patterns through \(n=8\). Its expected completion marker begins `SIGNED_B_PERMUTO_WIDTH_EXACT_PASS`. The all-dimensional proof is Steps 1–5, not a numerical extrapolation.

## Relationship to prior work
Godland and Kabluchko describe the signed-permutation realization, signed-majorization inequalities and Weyl normal fan of type-\(B\) permutohedra, and prove that the arithmetic-progression realizations are zonotopes (arXiv:2009.04186, Sections 4 and 6). Bastidas treats the type-\(B\) generalized permutohedral algebra (arXiv:2009.05876). These are premises; their cited results concern polytope fans, projections, and algebra, rather than the full spherical local-extremum and sharp fixed-angle stability classification here.

Previously established geometric results for type-\(B\) generalized permutohedra include a sharp inradius-to-circumradius ratio for an **optimally chosen, non-arithmetic** signed orbit weight vector, with all signed-subset facets tangent to a global inball. Those facet identities do not determine the width-local-minimum angular slope in the present arithmetic realization, nor the active-splitting versus zero-activation transition. The ordinary (unsigned) type-\(A\) permutohedron has a related local-width classification on its zero-sum sphere, but the restriction to antipodally paired coordinates changes the tangent geometry: an inactive absolute-value block and a second sharp term appear. In particular neither quoted classification implies the type-\(B\) angular transition by a change of notation.

## Limitations
The theorem treats the fixed odd-weight realization, not arbitrary type-\(B\) signed orbit weights or other Coxeter types. The exact angular profile is guaranteed only on the specified open interval; it does not classify distant spherical level sets or global optimization under arbitrary perturbations of the orbit vector. Historical originality is provisional: a prior result in Weyl-group norm optimization may state an equivalent local angular formula under different terminology.

## References
1. T. Godland and Z. Kabluchko, *Projections and angle sums of belt polytopes and permutohedra*, first public 2020-09-09, arXiv:2009.04186, https://arxiv.org/abs/2009.04186; *Results in Mathematics* 78 (2023), 140, DOI 10.1007/s00025-023-01918-2.
2. J. Bastidas, *The polytope algebra of generalized permutahedra*, first public 2020-09-12, arXiv:2009.05876, https://arxiv.org/abs/2009.05876; *Algebraic Combinatorics* 4 (2021), 909–946.
3. F. Ardila, F. Castillo, C. Eur and A. Postnikov, *Coxeter submodular functions and deformations of Coxeter permutahedra*, first public 2019-04-24, arXiv:1904.11029, https://arxiv.org/abs/1904.11029; *Advances in Mathematics* 365 (2020), 107039.
