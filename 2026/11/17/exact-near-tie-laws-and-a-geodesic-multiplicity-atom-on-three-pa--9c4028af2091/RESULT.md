# Exact near-tie laws and a geodesic-multiplicity atom on three-path metric networks

## Finding
Join three intervals of lengths \(0<a\le b\le c\) at both common endpoint pairs to form a metric theta graph. Give the graph the intrinsic path metric and its normalized arclength probability measure. Independently sample \(X,Y\), and let \(\Delta\) be the gap between the first and second smallest lengths of **distinct simple routes** from \(X\) to \(Y\); distinct routes of equal length count separately. Almost surely neither sampled point is a branch vertex. Write \(L=a+b+c\).

For all \(0<\varepsilon<\varepsilon_0\), the following laws are **exact**, not merely asymptotic:
\[
L^2\Pr(\Delta<\varepsilon)=
\begin{cases}
3(b+c)\varepsilon-\frac32\varepsilon^2,& a<b\le c,\\
\frac{(c-a)^2}{4}+\frac{7a+5c}{2}\varepsilon-\frac34\varepsilon^2,&a=b<c,\\
6a\varepsilon-\frac34\varepsilon^2,&a=b=c.
\end{cases}
\]
A sufficient choice is \(\varepsilon_0=\min\{a,b-a\}/4\) in the first case, \(\varepsilon_0=\min\{a,c-a\}/4\) in the second, and \(\varepsilon_0=a/4\) in the third. Consequently the two shortest simple routes are tied with positive probability **if and only if exactly the two shortest arms have equal length**, and then
\[
\Pr(\Delta=0)=\frac{(c-a)^2}{4(a+b+c)^2}.
\]
The nonzero atom is supported on pairs lying on the longer arm for which the two equally short detours are both minimizing. For strictly unequal shortest arm, the near-tie probability has the universal negative quadratic correction \(-3\varepsilon^2/(2L^2)\).

## Assumptions and scope
Each arm is a compact Euclidean interval, with only its two endpoints identified with the common two branch vertices. Each arm has strictly positive finite real length; ties are allowed. Sampling is independent with arclength normalized by total graph length. A *simple route* visits each of the two branch vertices at most once, except at an endpoint when applicable. Routes with different edge sequences are distinct even when they have identical lengths; repeated walks are excluded. For almost every ordered pair of points there are exactly three simple routes when both lie on the same arm and exactly four when on different arms. Their first two lengths counted with multiplicity define \(\Delta\). A strict inequality \(\Delta<\varepsilon\) is used; the equal-gap boundary for \(\varepsilon>0\) has zero product measure. The finding concerns the complete local probability law near zero, not the full distribution at arbitrary thresholds.

## Proof
**1. Enumerate every simple-route length.** For points on the same arm of length \(u\), separated by coordinate distance \(d\in[0,u]\), the three route lengths are \(d\), \(u-d+v\) and \(u-d+w\), where \(v,w\) are the other arm lengths. The unnormalized ordered-pair area element of separation \(d\) is \(2(u-d)\,\mathrm{d}d\). For points on distinct arms \(u,v\), write their coordinates as \(x\in[0,u]\), \(y\in[0,v]\), starting from the same branch vertex, and put \(U=x-u/2\), \(V=y-v/2\), \(H=(u+v)/2\). The four route lengths are exactly
\[
H+U+V,\quad H-U-V,\quad H+w+U-V,\quad H+w-U+V,
\]
where \(w\) is the remaining arm length. These exhaust vertex-simple routes and directly determine the two smallest lengths, including ties.

**2. Area for distinct arms: two easy pairs.** If \(a<b\), then for the unordered arm pairs \(\{a,b\}\) and \(\{a,c\}\) the unused arm is longer than the smallest used arm by more than \(\varepsilon\). The last two candidate routes therefore cannot compete with the two routes through one branch vertex. The condition for a small gap is \(|U+V|<\varepsilon/2\). Its planar area equals \(a\varepsilon\), since the thin central strip lies within the constant-width part of the \(a\)-by-\(b\) or \(a\)-by-\(c\) rectangle.

**3. Area for distinct arms: the pair \(\{b,c\}\).** Set \(q=a/2\), \(B=b/2\), \(C=c/2\), \(h=\varepsilon/2\). On either same-sign quadrant of \((U,V)\), only the first two route lengths compete and the small-gap region is the triangle \(|U|+|V|<h\) of area \(h^2/2\). On either opposite-sign quadrant let \(s=|U|\in[0,B]\), \(t=|V|\in[0,C]\). The two smallest routes are nearly tied precisely on the union
\[
\{\min(s,t)<q,\ |s-t|<h\}\ \cup\ \{|\min(s,t)-q|<h\}.
\]
The first set has area \(2qh\), the second \(2h(B+C-2q)\), and their overlap has area \(2h^2\). Therefore each opposite-sign quadrant contributes \(2h(B+C-q)-2h^2\). Adding all four quadrants yields the exact area
\[
A_{bc}=\varepsilon(b+c-a)-\frac34\varepsilon^2.
\]
For the stipulated \(\varepsilon\) these regions lie inside the stated coordinate rectangles, so no omitted clipping occurs.

**4. Same-arm contributions when \(a<b\).** On arm \(a\), the direct route is separated from every detour by at least \(b-a>\varepsilon\). On arm \(u=b\) or \(u=c\), the shortest detour uses arm \(a\), while the other detour is longer by at least \(b-a\). The two shortest routes differ by less than \(\varepsilon\) exactly for \(|2d-(u+a)|<\varepsilon\). Integrating \(2(u-d)\,\mathrm{d}d\) over this interval gives \((u-a)\varepsilon\). In total the same-arm contribution is \((b+c-2a)\varepsilon\). The three unordered different-arm areas are \(a\varepsilon\), \(a\varepsilon\), and \((b+c-a)\varepsilon-3\varepsilon^2/4\). Counting both orders of different arms, the total area is
\[
(b+c-2a)\varepsilon+2\left((a+b+c)\varepsilon-\tfrac34\varepsilon^2\right)
=3(b+c)\varepsilon-\tfrac32\varepsilon^2.
\]
Divide by \(L^2\).

**5. Exactly two shortest arms tied.** Suppose \(a=b=s<c\). On each short arm the only near-tie region is a direct-versus-detour tie at the far end; its ordered-pair area is \(\varepsilon^2/4\). On the long arm, the two detours through the equal short arms have identical lengths. They are both shortest whenever \(d>(c+s)/2\), and the gap is less than \(\varepsilon\) exactly when \(d>(c+s-\varepsilon)/2\). The resulting ordered same-arm area is \((c-s+\varepsilon)^2/4\). For the pair \(\{s,s\}\), with the third arm of length \(c\), the distinct-arm rectangle has area \(s\varepsilon-\varepsilon^2/4\). For either pair \(\{s,c\}\) with unused arm length \(s\), the opposite-sign quadrant calculation has its shorter-coordinate endpoint exactly at \(q=s/2\), and yields \((s+c)\varepsilon/2-\varepsilon^2/4\). Adding same-arm terms and twice each of these three different-arm areas gives
\[
\frac{(c-s)^2}{4}+\frac{7s+5c}{2}\varepsilon-\frac34\varepsilon^2.
\]
The constant term is the product-area of the two-long-arm routes tied for first, proving the atom.

**6. All three arms tied.** If \(a=b=c=s\), each same-arm ordered area is \(\varepsilon^2/4\): the direct segment nearly ties the two equal detours only near the far endpoint. Every one of the three unordered distinct-arm pairs has area \(s\varepsilon-\varepsilon^2/4\), using the symmetric square in Step 3 with \(B=C=q\). The aggregate is \(3\varepsilon^2/4+6(s\varepsilon-\varepsilon^2/4)=6s\varepsilon-3\varepsilon^2/4\). No positive-dimensional pair of points has two shortest routes of exactly equal length in this case, so the atom is zero.

The specified threshold bounds ensure every decomposition above is valid. All calculations used full product arclength area, with density \(L^{-2}\), and therefore prove the exact probability formulas. \(\square\)

## Verification
A standalone numerical checker integrates the four explicit route-length functions independently of the quadrant decomposition, numerically integrates same-arm separation densities, and compares the resulting probabilities for unequal, two-equal, and three-equal length triples with the exact formulas at two small thresholds. It also checks the atom analytically against the length of the tie interval. The checker tests finite examples only; Steps 1–6 are the proof for all positive real arm lengths in the respective regimes.

## Relationship to prior work
Burago and Ivanov (2012) develop general theory of graph path metrics, without distributions of the first two route lengths. Lecci, Rinaldo and Wasserman (2013) study statistical reconstruction of embedded metric graphs from samples, rather than nearly tied simple routes. Mémoli and Needham (2018 preprint) study one-distance distributions and inverse problems for metric-measure spaces. Existing theta-network calculations of the shortest-distance distribution also produce an explicit inverse determination of the three arm lengths from that distribution, and geodesic-subpath counts for discrete theta graphs are known. Those results do not provide the present **second-smallest simple-route gap distribution**, its exact local quadratic term, or its singular positive geodesic-multiplicity atom. Knowledge of all arm lengths would of course permit a separate derivation, so the new assertion is a forward explicit probability law, not a new graph-reconstruction theorem. Historical priority remains provisional.

## Limitations
The result is for a three-arm, two-terminal length-metric graph with independent arclength sampling and distinct vertex-simple routes. It does not apply to arbitrary graphs, does not treat walks with revisited branch vertices, does not give the gap law at larger thresholds, and does not imply a universal near-tie coefficient across metric networks. The exact atom in the two-shortest-tied case disappears if one changes the sampling or route-counting convention. Numerical checks are finite and cannot independently certify the infinite-parameter proof or historical novelty.

## References
1. D. Burago and S. Ivanov, *Uniform approximation of metrics by graphs*, `arXiv:1210.2435v1`, first public October 8, 2012; https://arxiv.org/abs/1210.2435.
2. F. Lecci, A. Rinaldo, and L. Wasserman, *Statistical Analysis of Metric Graph Reconstruction*, `arXiv:1305.1212v1`, first public May 6, 2013; https://arxiv.org/abs/1305.1212.
3. F. Mémoli and T. Needham, *Distance Distributions and Inverse Problems for Metric Measure Spaces*, `arXiv:1810.09646`, first public October 2018; https://arxiv.org/abs/1810.09646.
