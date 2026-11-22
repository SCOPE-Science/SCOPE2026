# Exact all-direction square-lattice Voronoi visibility and its arithmetic corner constant

## Finding
Fix an integer \(R\ge1\) and the planar site set
\[
\Lambda_R=\{(a,b)\in\mathbb Z^2:|a|+|b|\le R\}.
\]
Assign independent, identically distributed real-valued heights with a common continuous distribution to its sites. Two distinct sites are horizontally visible when every **other** Voronoi cell meeting their joining segment in an interval of positive length has a strictly lower height than both endpoint heights. A cell touched only at one point does not obstruct visibility. Let \(D_R\) be the degree of the origin in this graph.

For positive integers \(a,b\), put \(g=\gcd(a,b)\) and
\[
\sigma(a,b)=\begin{cases}
 g,&a/g\text{ and }b/g\text{ are both odd},\\
 0,&\text{otherwise}.
\end{cases}
\]
Set \(\sigma(a,0)=\sigma(0,b)=0\) for positive \(a,b\). Then the number of obstructing cells on the segment from the origin to \((a,b)\) is exactly
\[
 M(a,b)=|a|+|b|-1-\sigma(|a|,|b|).
\]
Consequently the exact finite expected degree, for every integer \(R\ge1\), is
\[
\boxed{\mathbb E D_R=8(H_{R+1}-1)+8\sum_{k=1}^{\lfloor R/2\rfloor}\varphi(2k)
\sum_{g=1}^{\lfloor R/(2k)\rfloor}\left[
\frac{1}{g(2k-1)(g(2k-1)+1)}-
\frac{1}{2kg(2kg+1)}\right].}
\]
Here \(H_n=\sum_{j=1}^n 1/j\) is the harmonic number and \(\varphi\) is Euler's totient. The correction is strictly positive as soon as \(R\ge2\).

The exact constant
\[
\boxed{\mathcal C=8(\gamma-1)+8\sum_{k=1}^{\infty}\varphi(2k)
\sum_{g=1}^{\infty}\left[
\frac{1}{g(2k-1)(g(2k-1)+1)}-
\frac{1}{2kg(2kg+1)}\right]}
\]
is well defined by absolutely convergent positive corrections (\(\gamma\) is Euler's constant). In particular,
\[
\boxed{\mathbb E D_R=8\log R+\mathcal C+O\!\left(\frac{\log R}{R}\right),\qquad \mathcal C\approx4.22569.}
\]
Thus all-direction visibility on the square Voronoi tessellation has a provable logarithmic mean-degree divergence with sharp coefficient \(8\) per logarithmic increase of the lattice-radius window. The additive constant retains nontrivial parity and coprimality data from segments crossing Voronoi vertices.

## Assumptions and scope
The finite site set is the **closed graph-distance diamond** \(\Lambda_R\), and only the degree at its origin is considered. The cells are ordinary Euclidean Voronoi cells of these sites (not a periodic torus). Heights must be independent and identically distributed with no atoms; their marginal law is otherwise unrestricted. **Point-only** contacts with cells do not count; this convention is essential at the fourfold vertices of the square tessellation. No statement about the full degree distribution, almost-sure degree, all-vertex averaged degree, or random Poisson sites is made. The result is planar discrete geometry (MSC2020: 52C20).

## Proof
**1. Reduction to the infinite square tessellation.** Fix an endpoint \((a,b)\in\Lambda_R\). Reflect coordinates to assume \(a,b\ge0\). Every point of the segment \([0,(a,b)]\) has coordinates in \([0,a]\times[0,b]\). Any coordinatewise nearest integer point lies in this rectangle, which itself lies in \(\Lambda_R\). Thus, at all segment positions with a unique nearest integer site, its nearest site in the finite sample equals its nearest site in the entire integer lattice. The finite Voronoi sequence of positive-length traversals is therefore exactly the sequence of open unit-square cells of \(\mathbb Z^2\) intersected by the segment. Isolated ties at square corners contribute no obstructing cell.

**2. Exact corner-crossing count.** If \(a,b>0\), the segment \((at,bt)\) crosses the \(a\) vertical grid lines at times \((2i+1)/(2a)\) and the \(b\) horizontal grid lines at times \((2j+1)/(2b)\), with indices ranging from zero through one less than the corresponding coordinate. A simultaneous crossing requires
\[
 b(2i+1)=a(2j+1).
\]
Write \(a=gu,b=gv\) with \(\gcd(u,v)=1\). The equality is possible exactly when \(u,v\) are both odd, and then the simultaneous crossing times are \((2h+1)/(2g)\) for \(0\le h<g\), giving exactly \(g\) coincidences. Hence there are \(a+b-\sigma(a,b)\) distinct boundary-crossing times, and consequently \(a+b-1-\sigma(a,b)\) intermediate open-square traversals. For an axial endpoint there are \(a+b-1\) intermediate squares. Reflection proves the stated \(M(a,b)\) formula in every quadrant.

**3. Probability for one segment.** Given \(M\) intermediate cells, all \(M+2\) heights are independent with continuous common law. Among their ranks, the two endpoint heights must be the largest two, in either order. Their probability is therefore exactly
\[
 p_M=\frac{2}{(M+1)(M+2)}.
\]
Thus the expected degree is the sum of \(p_{M(a,b)}\) over nonzero sites in \(\Lambda_R\).

**4. Base shells and arithmetic correction.** The diamond shell \(|a|+|b|=m\) has \(4m\) sites. Replacing \(\sigma\) everywhere by zero would contribute \(4m\cdot2/[m(m+1)]=8/(m+1)\) on the shell, yielding \(8(H_{R+1}-1)\). Actual corrections come solely from \(a,b>0\) with both reduced coordinates odd. Write \(a=gu,b=gv\), where \(u,v\) are coprime positive odd integers. Their sum is \(u+v=2k\). There are precisely \(\varphi(2k)\) ordered such pairs: choosing \(u\) among the reduced residues modulo \(2k\) determines \(v=2k-u\). Each ordered pair, its four sign choices and its dilation \(g\) supply a probability increment
\[
 8\left[\frac{1}{g(2k-1)(g(2k-1)+1)}-\frac{1}{2kg(2kg+1)}\right].
\]
Imposing \(2kg\le R\) yields the exact finite formula.

**5. Limit and remainder.** Write \(h(x)=1/[x(x+1)]\). For all \(x>0\), \(0<-h'(x)\le2/x^3\). By the mean-value theorem,
\[
0<h(g(2k-1))-h(2kg)\le\frac{2}{g^2(2k-1)^3}.
\]
As \(\varphi(2k)\le2k\), the unrestricted double sum of corrections converges. The omitted terms with \(2kg>R\) are bounded by a constant multiple of
\[
\sum_{k\le R/2}\frac{1}{k^2}\sum_{g>R/(2k)}\frac{1}{g^2}+
\sum_{k>R/2}\frac{1}{k^2}
=O\!\left(\frac{\log R}{R}\right).
\]
Combining this with \(H_{R+1}=\log R+\gamma+O(1/R)\) gives the claimed expansion. The positive correction is already present at \(R=2\), where the diagonally adjacent squares have no positive-length intermediate cells.

## Verification
Run `python3 checker.py` with Python's standard library. This checker separately enumerates rational half-integer boundary crossing times, uses exact midpoint-nearest-cell calculations, and compares their intermediate-cell counts with the coprimality formula for all \(675\) nonzero pairs with coordinates between zero and \(25\). It independently enumerates height-rank permutations for \(M=0,\ldots,6\). Finally, two independent exact rational calculations of \(\mathbb E D_R\), by individual endpoint summation and by the totient formula, agree for \(1\le R\le16\). The first four expected degrees are \(4\), \(28/3\), \(34/3\) and \(72/5\). All these checks passed. They are finite tests; the proof of the asymptotic expansion is the analytic argument above. A numerical approximation of \(\mathcal C\) is optional and is not needed for its exact definition.

## Relationship to prior work
Muñoz and Nuño (arXiv:2611.16336v1, sections 2, 4, 5 and 6) introduce Voronoi-based horizontal visibility, provide the universal rank formula \(p_M\), and study random Poisson sites, including a mean-field logarithmic growth prediction. Their Remark 2 specifically suggests analogous logarithmic growth for **all-direction square-lattice visibility**, but does not give its exact coefficient, arithmetic parity effect, finite-radius enumeration, or convergent additive constant. Those are the contributions here. The present diamond-window coefficient concerns a fixed central lattice site, not their mean degree under randomly scattered sites; the two constants must not be conflated.

Lacasa and Iacovacci (arXiv:1702.07813, sections II and III) investigate image visibility on regular grids using a **fixed finite set of line directions**. Their obstruction set comprises collinear sample sites on selected rays, rather than all positive-length Voronoi cell traversals on every segment. For example, the primitive displacement \((2,1)\) has no intervening collinear lattice site but has two intervening Voronoi cells. Their finite-direction degree laws do not imply this result. Standard half-integer line-crossing and totient identities are used transparently, without claiming either as new.

## Limitations
The theorem does not establish an exact degree-distribution tail or an almost-sure law. The symmetric diamond boundary and the positive-interval convention are essential for the stated finite formula; other truncations may change additive constants. The original Voronoi-visibility source assumes general-position sites for some structural statements, whereas the square lattice has fourfold Voronoi vertices. The current theorem deliberately extends its explicit positive-length-cell definition to this degenerate case and independently proves the needed geometric identities, without importing generic-position conclusions. A non-exhaustive literature search cannot establish universal historical priority. The claim has undergone only self-review, not independent audit.

## References
1. Francisco J. Muñoz and Juan Carlos Nuño, *Visibility graphs of irregularly sampled two-dimensional fields via Voronoi tessellations*, arXiv:2611.16336v1 (first public version, 12 November 2026), https://arxiv.org/abs/2611.16336.
2. Lucas Lacasa and Jacopo Iacovacci, *Visibility graphs of random scalar fields and spatial data*, arXiv:1702.07813 (first public version, 25 February 2017); *Physical Review E* 96, 012318, https://arxiv.org/abs/1702.07813.
