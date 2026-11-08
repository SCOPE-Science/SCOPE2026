# Exact five-threshold field diagram of the three-state Clebsch Potts antiferromagnet

## Finding

For the sixteen-site, five-regular Clebsch graph, the three-state classical antiferromagnetic Potts model with a field favoring one named color has the following **exact ground-state energy at every real field**:

\[
\frac{E_0(h)}{J}=\min\{8,\;3-4x,\;3-7x,\;4-8x,\;15-11x,\;40-16x\},\qquad x=\frac hJ.
\]

Exactly five coexistence fields occur, at \(x=-5/4,0,1,11/3,5\). The favored-color population and number of labeled ground states on each open interval are:

| Field interval | Favored sites | Degeneracy |
|---|---:|---:|
| \(x<-5/4\) | 0 | 10 |
| \(-5/4<x<0\) | 4 | 160 |
| \(0<x<1\) | 7 | 160 |
| \(1<x<11/3\) | 8 | 160 |
| \(11/3<x<5\) | 11 | 512 |
| \(x>5\) | 16 | 1 |

At the five coexistence fields, the participating favored populations and total labeled degeneracies are respectively \((0,4):170\), \((4,5,6,7):720\), \((7,8):320\), \((8,11):672\), and \((11,12,13,14,15,16):4065\). In particular, the minimum number of monochromatic bonds with three named colors is exactly three, attained by 720 configurations. The last coexistence count equals the independent-set polynomial of this graph evaluated at two:

\[
I_C(t)=1+16t+80t^2+160t^3+120t^4+16t^5,\qquad I_C(2)=4065.
\]

The five exact threshold values, energy branches, phase populations and degeneracies form one finite-cluster classification; the independence-polynomial identity explains its saturation boundary.

## Assumptions and scope

Let \(V=\{0,1,\ldots,15\}\) be identified with the binary four-cube. Two distinct vertices are adjacent exactly when their four-bit XOR is one of \(1,2,4,8,15\). This is the five-regular Clebsch graph, also called the folded five-cube, with 40 undirected edges and strongly regular parameters \((16,5,0,2)\). The complementary ten-regular graph sometimes also called Clebsch is **not** used.

For all \(J>0\) and \(h\in\mathbb R\), assign each vertex one of the **three named** colors \(0,1,2\). Define

\[
H_{J,h}(\sigma)=J\sum_{\{u,v\}\in E}\mathbf1_{\sigma_u=\sigma_v}-h\sum_{v\in V}\mathbf1_{\sigma_v=0}.
\]

Degeneracies count individual labeled assignments, without dividing by graph automorphisms or interchanging colors 1 and 2. This is a zero-temperature, finite-volume statement; no thermodynamic phase transition, generic-coupling extension, or quantum-spin assertion is made.

## Proof

**1. Exhaustive exact reduction.** For each integer \(k\in\{0,\ldots,16\}\), define \(b_k\) as the least number of monochromatic edges among configurations with exactly \(k\) vertices of color 0, and \(c_k\) as the number attaining that minimum. For a subset \(A\subseteq V\), write \(e(A)\) for the number of edges induced by \(A\). Every coloring corresponds uniquely to an ordered partition \(V=S\sqcup T\sqcup U\) into the three color classes, so its number of monochromatic edges is exactly

\[
e(S)+e(T)+e(U),\qquad |S|=k.
\]

For nonempty \(A\), with \(v\) its least-numbered vertex,

\[
e(A)=e(A\setminus\{v\})+|N(v)\cap(A\setminus\{v\})|,\quad e(\varnothing)=0.
\]

This integer recurrence computes every \(e(A)\) for all \(2^{16}\) vertex subsets. For each \(S\), looping through all \(T\subseteq V\setminus S\) and taking \(U=V\setminus(S\cup T)\) visits **every one of the \(3^{16}=43,046,721\) named colorings once**. The recurrence and complete loops in `verify_subset.py` yield the following exact sector table, independently reproduced by direct ternary enumeration in `verify_ternary.c`:

| \(k\) | \(b_k\) | \(c_k\) | \(k\) | \(b_k\) | \(c_k\) |
|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 10 | 9 | 8 | 1,280 |
| 1 | 7 | 160 | 10 | 12 | 6,400 |
| 2 | 6 | 800 | 11 | 15 | 512 |
| 3 | 5 | 2,240 | 12 | 20 | 1,920 |
| 4 | 3 | 160 | 13 | 25 | 1,280 |
| 5 | 3 | 320 | 14 | 30 | 320 |
| 6 | 3 | 80 | 15 | 35 | 32 |
| 7 | 3 | 160 | 16 | 40 | 1 |
| 8 | 4 | 160 | | | |

The actual per-sector color-class-mask witnesses are stored in `sector_data.json`; all files use the same vertex/edge definition.

**2. Complete field envelope.** In sector \(k\), the minimum energy divided by \(J\) is \(b_k-kx\). Compare all 17 integer-affine functions in the table, using exact rational arithmetic. The lower hull consists precisely of sector indices \(0,4,7,8,11,16\), with consecutive crossings at \(-5/4,0,1,11/3,5\). At \(x=0\) the two additional collinear sectors \(5,6\) also minimize; at \(x=5\) sectors \(12,13,14,15\) do so. At each knot, the exact verifier compares every omitted affine function with the candidate minimum. Between knots the difference between any omitted function and the active candidate is affine and nonnegative at both ends. On the outer unbounded intervals its slope gives the same conclusion. Thus no omitted sector can minimize for any other real \(x\), and the lower envelope above holds globally. Degeneracies follow by summing the \(c_k\) of every minimizing sector.

**3. Structural explanation of saturation.** At \(x=5\), begin with all sites in color 0 and let \(A\) be the set changed to colors 1 or 2. The graph is five-regular, hence the induced monochromatic-edge count in the remaining color-0 vertices equals \(40-5|A|+e(A)\). If \(e_1(A)\) and \(e_2(A)\) count edges internal to the two alternative colors, then

\[
H_{J,5J}/J=-40+e(A)+e_1(A)+e_2(A).
\]

The three nonnegative terms vanish exactly when \(A\) is independent. Every independent \(A\) then has \(2^{|A|}\) choices of the two other named colors. The same subset recurrence, with the exact predicate \(e(A)=0\), gives independence-set counts \(1,16,80,160,120,16\) at sizes zero through five, and none above five. Therefore the coexistence degeneracy is exactly \(I_C(2)=4065\), as claimed.

## Verification

The self-contained `verify_subset.py` and `sector_data.json` use the binary XOR graph and subset induced-edge recurrence. Running `python verify_subset.py` recomputes all 43,046,721 configurations, all 17 minima and multiplicities, a witness for each sector, all five rational crossing sets, and the exact independence polynomial. The independent `verify_ternary.c` uses base-three digit decoding of every integer from zero to \(3^{16}-1\), evaluates 40 edges per configuration, and checks the same sector arrays; compile and run with `cc -O3 -std=c99 verify_ternary.c -o verify_ternary && ./verify_ternary`. Both were run and agreed. Their complete finite enumerations, not sampling, support the exact finite assertions.

## Relationship to prior work

DeVos and Šámal, *High-girth cubic graphs are homomorphic to the Clebsch graph*, arXiv:math/0602580 (initial public posting 2006-02-27), identify the Clebsch graph with the projective/folded four-cube and investigate graph homomorphisms, not a three-state field-dependent Potts ground-state enumeration. Shrock and Xu, *Exact Results on Potts Model Partition Functions in a Generalized External Field and Weighted-Set Graph Colorings*, arXiv:1009.1182 (initial posting 2010-09-07), give general magnetic-field partition-function theory and results for paths, complete graphs, wheels and small pairs; this is the relevant parent formalism but does not tabulate this Clebsch classification. Klazar, Loebl and Moffatt, *The Potts model and chromatic functions of graphs*, arXiv:1311.4348 (initial posting 2013-11-18), establish general polynomial equivalences, not the evaluated Clebsch field diagram. The graph's well-known chromatic number four and independence number five are background facts, not novel claims.

The complete finite result is not a generic claim that the Potts partition function exists: the contribution is the explicit 17-sector optimization, globally exact five-knot field envelope and multiplicities for this named frustrated graph. The two-color limiting sector and the general independent-set interpretation of saturation may be inferred from established graph-spin methods; they are included only as checks and explanations, not separately claimed as new general theorems.

## Limitations

The result concerns a single, explicitly specified 16-vertex graph and three named spin colors. It does not compute finite-temperature partition functions, thermodynamic limits or any infinite graph. Prior literature not indexed by the checked sources may contain some or all of this specific numerical classification; historical priority is therefore provisional. The general graph-polynomial identities can formally recover all finite counts after graph-specific evaluation; they do not themselves provide the explicit sector table reported here.

## References

1. M. DeVos and R. Šámal, *High-girth cubic graphs are homomorphic to the Clebsch graph*, arXiv:math/0602580 (2006-02-27), https://arxiv.org/abs/math/0602580.
2. R. Shrock and Y. Xu, *Exact Results on Potts Model Partition Functions in a Generalized External Field and Weighted-Set Graph Colorings*, arXiv:1009.1182 (2010-09-07), https://arxiv.org/abs/1009.1182.
3. M. Klazar, M. Loebl and I. Moffatt, *The Potts model and chromatic functions of graphs*, arXiv:1311.4348 (2013-11-18), https://arxiv.org/abs/1311.4348.
4. E. W. Weisstein, *Clebsch Graph*, MathWorld, https://mathworld.wolfram.com/ClebschGraph.html (graph construction, parameters and chromatic number).
