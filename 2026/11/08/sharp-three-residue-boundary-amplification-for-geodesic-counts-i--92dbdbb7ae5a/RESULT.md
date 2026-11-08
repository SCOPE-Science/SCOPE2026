# Sharp three-residue boundary amplification for geodesic counts in layered paths

## Finding
Let \(B(a_1,\ldots,a_k)\) be the connected graph formed from nonempty independent vertex layers of sizes \(a_1,\ldots,a_k\), joining every vertex in successive layers and no other pairs. Let \(\operatorname{gpn}(G)\) count all undirected shortest paths in \(G\), including each one-vertex path once. For any two **fixed** finite sequences \(L,R\) of positive integers (either may be empty), define
\[
G_m(L,R)=B(L,\underbrace{3,\ldots,3}_{m\text{ layers}},\operatorname{rev}(R)),\qquad m\ge2,
\]
where \(n_m=|V(G_m)|=s_L+s_R+3m\), \(s_L=\sum_{a\in L}a\), and \(s_R=\sum_{a\in R}a\). Put
\[
H(L)=\frac32+\sum_{i=1}^{|L|}\prod_{j=i}^{|L|}L_j,\qquad H(\varnothing)=\frac32.
\]
Then for each such pair \(L,R\) there is a constant \(K(L,R)\) independent of \(m\) such that
\[
\operatorname{gpn}(G_m(L,R))=H(L)H(R)3^m+\frac{33}{2}m+K(L,R),\qquad m\ge2.
\]
In particular the normalized limit is exactly \(F(L)F(R)\), where \(F(T)=H(T)/3^{(\sum T)/3}\). Among **all fixed-tail pairs** with \(s_L+s_R\equiv r\pmod3\), the sharp supremum of this limit is
\[
\boxed{\begin{aligned}
C_0&=\frac{121}{36},\\
C_1&=\frac{529}{4\,3^{10/3}},\\
C_2&=\frac{253}{12\,3^{5/3}}.
\end{aligned}}
\]
Each supremum is attained by a fixed-tail pair. Here \(r\) refers to the residue of the total number of vertices \(n_m\), not to \(m\). **There is no claim that these constants are optimal over all connected graphs, or even all variable-layer paths.**

## Assumptions and scope
Graphs are finite, simple, unweighted and connected. Layers consist of mutually nonadjacent vertices and only consecutive layers are joined completely. Every tail size is positive; the tail sequences \(L,R\) are fixed before taking \(m\to\infty\). The central run has \(m\) layers of size three. The asymptotic supremum ranges over all fixed finite tails and allows empty tails. The identity above holds for \(m\ge2\); the three explicit families below also satisfy their exact formulas for \(m\ge1\).

For \(r=0\), take \(L=R=(1,2)\). For \(r=1\), take \(L=R=(1,2,2)\). For \(r=2\), take \(L=(1,2)\) and \(R=(1,2,2)\). Write \(B_{r,m}=G_m(L,R)\) for these choices. Their exact numbers of geodesics are
\[
\boxed{\begin{aligned}
\operatorname{gpn}(B_{0,m})&=\frac{121}{4}3^m+\frac{33}{2}m-\frac94,\\
\operatorname{gpn}(B_{1,m})&=\frac{529}{4}3^m+\frac{33}{2}m+\frac{31}{4},\\
\operatorname{gpn}(B_{2,m})&=\frac{253}{4}3^m+\frac{33}{2}m+\frac{11}{4}.
\end{aligned}}
\]
The respective orders are \(3m+6\), \(3m+10\), and \(3m+8\). The first of these *construction formulas* is previously known and is included for comparison, not offered as a new example.

## Proof
**1. Count geodesics in any layered path.** Between vertices in different layers \(i<j\), every shortest path moves one layer right at each step. It therefore has exactly one freely chosen vertex in each intermediate layer, and the contribution from all endpoint choices is \(\prod_{t=i}^j a_t\). For two distinct vertices in a common layer \(i\), the distance is two, and the middle vertex may lie in either neighboring layer; this contributes \(\binom{a_i}{2}(a_{i-1}+a_{i+1})\), interpreting nonexistent neighboring sizes as zero. Adding one trivial geodesic for each vertex gives the exact identity
\[
\operatorname{gpn}(B(a_1,\ldots,a_k))=\sum_i a_i+\sum_{i<j}\prod_{t=i}^j a_t+\sum_i\binom{a_i}{2}(a_{i-1}+a_{i+1}).\tag{1}
\]
All paths are counted without orientation, including length zero; neither endpoint pairs nor paths are double-counted.

**2. The central-run coefficient.** Set \(E_j=\sum_{i=1}^{j}\prod_{t=i}^j a_t\) and \(E_0=0\), so \(E_j=a_j(E_{j-1}+1)\). Immediately after a left tail \(L\), \(E=H(L)-3/2\). After \(t\) central layers of size three,
\[
E=H(L)3^t-\frac32.\tag{2}
\]
The consecutive-product part of (1) equals \(\sum_j(E_j-a_j)\). Summing the \(m\) central terms gives \(\tfrac32H(L)3^m-\tfrac92m\) plus a tail-dependent constant. Appending the reversed right tail multiplies the coefficient of \(3^m\) by the sum of its nonempty prefix products, which is \(H(R)-3/2\). Thus the full consecutive-product contribution is \(H(L)H(R)3^m-\tfrac92m+O_{L,R}(1)\). The common-layer contribution in (1) is \(18m+O_{L,R}(1)\): each interior three-vertex layer contributes \(\binom32(3+3)=18\), and only the two boundary layers differ. The vertex count adds \(3m+O_{L,R}(1)\). These are exact identities with tail-dependent constant terms for every \(m\ge2\), giving the claimed \(33m/2\) coefficient and limit.

**3. Optimize an arbitrary tail.** Appending a layer of size \(a\) transforms \(h=H(T)\) by
\[
T_a(h)=ah+\frac{3-a}{2};\qquad h\ge\frac32.\tag{3}
\]
For \(a\ge4\), replacing that layer by layers of sizes \(2,a-2\) increases the result by \((a-4)h+a/2>0\). Iterating removes every part larger than three without increasing total tail size. Interchanging successive sizes \(b,a\) with \(a<b\) to \(a,b\) increases the result by \(b-a>0\). Hence an optimizing composition can be sorted nondecreasingly. Two successive ones can be replaced by one two without loss because \(T_2(h)-T_1(T_1(h))=h-3/2\ge0\). Four successive twos can be replaced by \(2,3,3\) without loss because \(T_3(T_3(T_2(h)))-T_2^4(h)=2h-3\ge0\). Therefore **every tail** can be replaced without reducing \(H\) or changing its total size by one of the forms \((1^\varepsilon,2^j,3^k)\), with \(\varepsilon\in\{0,1\}\), \(j\in\{0,1,2,3\}\), and \(k\ge0\).

Since \(T_3(h)=3h\), appending threes leaves \(F(T)=H(T)/3^{(\sum T)/3}\) unchanged. The only eight reduced possibilities (\(\varepsilon,j\)) have the following values of \(H\):
\[
\begin{array}{c|rrrr}
 &j=0&j=1&j=2&j=3\\\hline
\varepsilon=0&3/2&7/2&15/2&31/2\\
\varepsilon=1&5/2&11/2&23/2&47/2
\end{array}
\]
with respective total tail sizes \(2j+\varepsilon\). Comparing these eight exact values after division by \(3^{(2j+\varepsilon)/3}\) shows that the sharp one-tail bounds for residues zero, one, two are respectively
\[
c_0=\frac{11}{6},\qquad c_1=\frac{47}{2\,3^{7/3}},\qquad c_2=\frac{23}{2\,3^{5/3}},\tag{4}
\]
attained by \((1,2)\), \((1,2,2,2)\), and \((1,2,2)\). The comparisons are exact (cubing removes the cube roots); numerically \(c_1\approx1.81044<c_0\approx1.83333<c_2\approx1.84287\).

**4. Combine the tails.** Since \(s_L+s_R\equiv r\pmod3\), the only residue-pair possibilities, up to exchange, are \((0,0),(1,2)\) for \(r=0\); \((0,1),(2,2)\) for \(r=1\); and \((0,2),(1,1)\) for \(r=2\). Comparing their products gives respectively \(c_0^2>c_1c_2\), \(c_2^2>c_0c_1\), and \(c_0c_2>c_1^2\). This proves the three sharp constants and exhibiting tails. Substitution into (1), or the recurrence \(E_j=a_j(E_{j-1}+1)\), yields the three exact finite formulas stated above.

## Verification
Run `python3 artifacts/verify.py` with Python 3 and no third-party packages. The verifier independently constructs each small layered graph, counts all shortest paths using breadth-first search and shortest-path multiplicity dynamic programming, and compares this with (1). It also checks the exact maximizing-tail recurrence through total tail size 90, the eight reduced-tail representatives, all three exact construction formulas for 35 core lengths, and exact residue-envelope inequalities through size 90. The infinite upper bound and the asymptotic limit are proved algebraically above; they are not inferred from those finite checks.

## Relationship to prior work
Knor, Sedlar, Škrekovski, and Zhang introduced \(\operatorname{gpn}\) and in their 2026 paper analyzed equal-size layered joins \(G_{k,t}\), giving \(G_{3,t}\) as a candidate with leading constant \(9/4\) when normalized by \(3^{n/3}\); their Problem 14 asks for stronger extremal constructions or upper bounds. An earlier public result, *Boundary-tapered path blow-ups improve the geodesic-subpath lower bound* (September 20, 2026), already established the precise \(r=0\) example \((1,2,3,\ldots,3,2,1)\), including its \(121/36\) constant. Both results are credited and are not claimed as novel. The new assertion is the **sharp optimization over arbitrary fixed boundary tails** for each of the three residues, supported by the replacement principle and the two additional explicit residue-class formulas. A global optimum over all graphs or all layer-size profiles remains unproved.

## Limitations
The sharpness claim is deliberately confined to **fixed finite boundary tails around a growing all-three core**. Tails varying with the core length, non-three periodic cores, and arbitrary graphs are outside the upper-bound assertion. The general global extremal problem remains open. An accessible summary rather than the complete full text of the preceding public tapered-construction record was available, so unrecognized prior overlap in that document remains a residual historical-priority risk. Independent mathematical audit has not been performed.

## References
1. M. Knor, J. Sedlar, R. Škrekovski, X.-D. Zhang, *Counting geodesic paths in graphs*, arXiv:2604.04907v1 (first public 2026-04-06), later *Mediterranean Journal of Mathematics* 23, 171 (2026), doi:10.1007/s00009-026-03159-3. https://arxiv.org/abs/2604.04907
2. *Boundary-tapered path blow-ups improve the geodesic-subpath lower bound*, public mathematical-result record dated 2026-09-20, identifier `2026/9/20/SCOPE-boundary-tapered-geodesic-path-blowups--26120b82068c`, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-boundary-tapered-geodesic-path-blowups--26120b82068c.
