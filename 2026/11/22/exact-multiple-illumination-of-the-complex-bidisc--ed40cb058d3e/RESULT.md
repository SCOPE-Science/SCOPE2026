# Exact multiple illumination of the complex bidisc

## Finding
Let \(D=\{z\in\mathbb C:|z|\le1\}\) and let \(B=D\times D\subset\mathbb C^2\cong\mathbb R^4\). For each positive integer \(m\), write \(I^{(m)}(B)\) for the smallest cardinality of a multiset of nonzero real directions such that every point of \(\partial B\) is illuminated inward by at least \(m\) directions, counted with multiplicity. Then
\[
\boxed{I^{(m)}(B)=4m+3\qquad(m=1,2,3,\ldots).}
\]
The case \(m=1\) is previously known. The new assertion is the complete formula for \(m\ge2\); for example, \(I^{(2)}(B)=11\), \(I^{(3)}(B)=15\). Equivalently, the minimum number of translates of the *open* square \((0,1/2)^2\) required to cover every point of the flat torus \(\mathbb T^2=(\mathbb R/\mathbb Z)^2\) at least \(m\) times is exactly \(4m+3\). The excess over the fractional-covering mass \(4m\) is identically three, not proportional to \(m\).

## Assumptions and scope
A direction \(v\in\mathbb R^4\setminus\{0\}\) illuminates \(x\in\partial B\) if \(x+tv\in\operatorname{int}(B)\) for some \(t>0\). The minimizing collection is a *multiset*: repeated directions count separately. All covering squares are open (not closed or half-open), have the coordinate axes as sides, and are translated modulo one. The conclusion holds for all positive integer multiplicities, with strict illumination at tangent directions excluded. The primary geometric classification is in MSC2020 52A20.

A supporting angular criterion is useful. At a distinguished-boundary point \((e^{2\pi i x},e^{2\pi i y})\), a complex direction \((v_1,v_2)\) illuminates precisely when \(\operatorname{Re}(e^{-2\pi ix}v_1)<0\) and \(\operatorname{Re}(e^{-2\pi iy}v_2)<0\). A direction with either component zero cannot illuminate a distinguished-boundary point. For nonzero components, the two strict inequalities describe a translate of \((0,1/2)^2\) in angular coordinates. Conversely, every translated open half-square is realized by an appropriate choice of the two phases of the direction. If a multiset illuminates every distinguished-boundary point \(m\) times, it also illuminates every other boundary point \(m\) times: for a point with only one saturated coordinate, choose an arbitrary value of modulus one for the other coordinate; each of the \(m\) directions illuminating the resulting distinguished-boundary point remains strictly inward on the saturated coordinate and stays inside the nonsaturated disk for sufficiently small positive time.

## Proof
**One-dimensional lemma.** If \(h\) open arcs of length \(1/2\) cover the circle \(\mathbb T=\mathbb R/\mathbb Z\) at every point at least \(r\) times, then \(h\ge2r+1\). Indeed, integrating multiplicity gives \(h/2\ge r\). If \(h=2r\), multiplicity must equal \(r\) almost everywhere. Choose a left endpoint of at least one arc. Immediately to its right, the count is \(r\), but at the endpoint every arc beginning there is excluded; other arcs have the same status as immediately to the right, except those ending there, which are also excluded. Thus multiplicity at that endpoint is strictly less than \(r\), a contradiction. The same argument works for a multiset of arcs.

**Lower bound.** Suppose \(N\) open half-squares cover \(\mathbb T^2\) at least \(m\) times. Fix the second coordinate \(y\) and retain the squares whose second-coordinate arcs contain \(y\). Their first-coordinate arcs must \(m\)-cover \(\mathbb T\); the lemma shows that at least \(2m+1\) squares are retained for *every* \(y\). Hence the \(N\) second-coordinate arcs form a \((2m+1)\)-fold open half-circle covering. The same lemma gives
\[
N\ge2(2m+1)+1=4m+3.
\]
The argument includes the boundary of every covering square; replacing open arcs by closed arcs would invalidate the strict endpoint step.

**Explicit matching covering.** Put \(N=4m+3\) and, for \(k=0,1,\ldots,N-1\), let
\[
Q_k=\left(\frac{k}{N},\frac{k}{N}+\frac12\right)
\times\left(\frac{2k}{N},\frac{2k}{N}+\frac12\right)
\pmod{\mathbb Z^2}.
\]
Fix any first coordinate \(x\in\mathbb T\). An open half-circle contains at least \(\lfloor N/2\rfloor=2m+1\) consecutive points of the regular \(N\)-point grid. Therefore there exist \(2m+1\) consecutive residues \(k_0,k_0+1,\ldots,k_0+2m\pmod N\) whose first-coordinate arcs all contain \(x\). Their second-coordinate starting points \(2k/N\pmod1\) are cyclically ordered with \(2m\) successive gaps \(2/N\) and one closing gap \(3/N\), since \(N-4m=3\).

Any closed half-circle contains at most \(m+1\) of these \(2m+1\) starting points: to contain \(m+2\) of them would require a span of at least
\[
\frac{2(m+1)}{N}=\frac{2m+2}{4m+3}>\frac12.
\]
Consequently every *open* half-circle in the second coordinate contains at least \(m\) of these starting points. In particular, for every \(y\in\mathbb T\), at least \(m\) of the selected squares \(Q_k\) contain \((x,y)\). This holds even when either coordinate lies on a grid boundary, because the complement used above is closed. Thus the \(N=4m+3\) squares form an \(m\)-fold open cover, proving the matching upper bound and the formula.

Finally, translate each square \(Q_k\) to its corresponding complex illumination direction, using a phase \(2\pi(k/N-1/4)\) in the first component and \(2\pi(2k/N-1/4)\) in the second. The angular criterion above yields the claimed bidisc illumination number. \(\square\)

## Verification
The included standalone `verify.py` checks the explicitly defined cyclic family with exact modular integer arithmetic for every multiplicity from \(1\) through \(15\). It samples each open two-cell, each one-dimensional boundary stratum and every boundary intersection in the finite arrangement of all square edges. The minimum multiplicity is exactly the prescribed \(m\) in every checked case. These finite checks confirm the implementation and endpoint handling; the preceding argument, not the enumeration, proves the assertion for all positive integers.

Run with `python3 verify.py`. No external dependencies or stochastic seeds are required.

## Relationship to prior work
Rotem, Schejter and Slomka, *The complex Illumination problem*, arXiv:2410.12021v1 (publicly posted 2024-10-15), prove the ordinary \(m=1\) formula for polydiscs, including \(I^{(1)}(D\times D)=7\), and identify the equivalent single-cover problem on a torus by open half-squares. Their Theorems 1.3–1.6 and Propositions 2.2, 2.3, 2.7 concern ordinary or fractional (real-weighted) covering, not the integer \(m\)-fold spectrum. The new construction depends on the multiplicity through \(4m+3\), and its two-stage lower bound is tight for every \(m\).

Sriamorn, *On the multiple illumination numbers of convex bodies*, arXiv:2306.13517v1 (publicly posted 2023-06-23), defines the multiplicity parameter, proves \(2m+1\) for smooth planar bodies, gives other general bounds and treats polygons/cap bodies. The bidisc is a nonsmooth four-dimensional Cartesian product; neither its exact formula nor a torus half-square multiple-cover theorem is stated there. The lower bound \(2m+1\) for open half-circle covers is consistent with that planar result. No assertion of novelty is made for the \(m=1\) case, for the fractional covering number \(4\), or for the one-dimensional lemma by itself.

## Limitations
The proof is specific to the two-coordinate complex polydisc, or equivalently axis-aligned open half-squares on the flat two-torus. It does not determine higher-dimensional polydisc multiple illumination numbers, general covering side lengths, or uniqueness of extremal covering configurations. The novelty assessment is literature- and index-based; an unindexed equivalent formula or an earlier more general theorem remains a possible priority risk. No independent mathematical audit has been performed.

## References
1. K. Sriamorn, *On the multiple illumination numbers of convex bodies*, arXiv:2306.13517v1, first submitted 2023-06-23. https://arxiv.org/abs/2306.13517
2. L. Rotem, A. Schejter, and B. A. Slomka, *The complex Illumination problem*, arXiv:2410.12021v1, first submitted 2024-10-15. https://arxiv.org/abs/2410.12021
