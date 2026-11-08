# Inclusion-minimal super domination on cycles: a five-gap census and sharp seven-period upper spectrum

## Finding

Let \(C_n\) be the labelled simple cycle on vertices \(0,1,\ldots,n-1\), with \(n\ge3\). A set \(S\) is *super dominating* if every vertex \(u\notin S\) has a neighbor \(v\in S\) with \(N(v)\cap(V(C_n)\setminus S)=\{u\}\). It is *inclusion-minimal* if none of its proper subsets is super dominating. Let \(M_n(z)=\sum_S z^{|S|}\), summed over precisely the inclusion-minimal super dominating sets.

Define the following explicit polynomial, with indeterminates \(x,z\):

\[
D(x,z)=1-z^2x^3-z^2x^4-2z^3x^5-2z^4x^6-z^5x^7+z^5x^8+2z^6x^9+z^7x^{10}.
\]

Then the complete labelled cardinality distribution is determined, for every \(n\ge3\), by

\[
\boxed{\quad \sum_{n\ge3}M_n(z)x^n=-\frac{x\,\partial D(x,z)/\partial x}{D(x,z)}.\quad}
\]

The largest cardinality of any inclusion-minimal super dominating set, denoted \(U_n\), is

\[
\boxed{\quad U_n=\left\lfloor\frac{5n}{7}\right\rfloor-
\mathbf 1_{\{n\ge10,\ n\equiv3\pmod7\}}-
\mathbf 1_{\{n\ge16,\ n\equiv2\pmod7\}}.\quad}
\]

If \(7\mid n\), precisely seven inclusion-minimal super dominating sets have cardinality \(5n/7\): they are the seven distinct rotations of the repeated length-seven omitted-vertex indicator word `1010000` (where `1` means omitted). For example,

\[
M_7(z)=7z^4+7z^5,\qquad M_{14}(z)=105z^8+56z^9+7z^{10}.
\]

## Assumptions and scope

Graphs are finite, labelled, simple, undirected cycles. Inclusion-minimal refers to the set-containment order, not to minimum cardinality. The variable \(z\) marks selected vertices and \(x\) marks total cycle vertices. All statements hold for integer \(n\ge3\), including triangles and quadrilaterals. The rational series is formal at \(x=0\), so there is no analytic convergence assumption.

## Proof

**1. Cyclic gaps.** Every inclusion-minimal super dominating set has at least one omitted vertex: the all-selected set is super dominating but is not inclusion-minimal when \(n\ge3\). For a set with \(k\ge1\) omitted vertices, list them in positive cyclic order and let \(g_i\ge0\) be the number of selected vertices encountered after the \(i\)-th omitted vertex and before the next, with cyclic indices. Thus

\[
 n=\sum_{i=1}^k(g_i+1),\qquad |S|=\sum_{i=1}^k g_i.
\]

An omitted vertex has a selected private-neighbor witness on its clockwise side exactly when the following gap is at least two, and similarly on its counterclockwise side exactly when the preceding gap is at least two. Therefore \(S\) is super dominating if and only if no two consecutive gaps are both in \(\{0,1\}\). This also applies when \(k=1\), using cyclic indexing.

**2. Exact inclusion-minimality condition.** Deleting one selected vertex in a gap of size \(g\) inserts an additional omitted vertex and replaces that gap by \(a,b\ge0\) with \(a+b=g-1\). If \(g\ge5\), choose \(a=2\), \(b=g-3\ge2\), and the new gap sequence remains valid; hence minimality excludes such gaps. If \(g\in\{3,4\}\), a split remains valid whenever either neighboring gap is at least two: choose respectively \((a,b)=(0,2)\) or \((1,2)\) when the preceding gap is long, and the reversed split when the following gap is long. Conversely, if both neighboring gaps are short, every split of a gap of size three or four creates adjacent short gaps, and is invalid. Gaps of sizes one or two cannot be split without creating adjacent short gaps; a gap of size zero contains no selected vertex to delete.

Consequently, a cyclic gap sequence describes an inclusion-minimal super dominating set if and only if all gaps lie in \(\{0,1,2,3,4\}\) and its neighboring pairs are precisely among

\[
(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,2)
\]

and their reversals. This condition is both necessary and sufficient. It also establishes that checking single-vertex deletions is sufficient: super domination is upward closed under adding vertices.

**3. Exact generating function.** Collapse the two short gap types \(0,1\) into class \(A\), retain \(2\) as class \(B\), and collapse \(3,4\) into class \(C\). The block generating polynomials are

\[
 u=x+zx^2,\qquad w=z^2x^3,\qquad v=z^3x^4+z^4x^5.
\]

A class-adjacency transfer matrix, placing the weight of each gap on its departure edge, is

\[
T=\begin{pmatrix}0&u&u\\w&w&0\\v&0&0\end{pmatrix}.
\]

A closed walk of length \(k\) records a cyclic sequence with \(k\) distinguished ordered gaps. The weight \(x^nz^{|S|}\) appears with exactly \(k\) distinguished omissions for each labelled subset and \(n\) possible placements of the first distinguished omission. Thus the labelled counting multiplier is \(n/k\), including periodic gap words. The formal identity

\[
\sum_{k\ge1}\frac{\operatorname{tr}(T^k)}k=-\log\det(I-T)
\]

then gives \(M_n(z)=[x^n](-x\,\partial_x\log\det(I-T))\). A direct determinant calculation yields

\[
\det(I-T)=(1-w)(1-uv)-uw=D(x,z),
\]

which proves the complete rational cardinality generating function, with its small-order boundary cases.

**4. Universal seven-sevenths inequality and rigidity.** Write \(s_0,s_1,c_2,c_3,c_4\) for the numbers of gaps of sizes \(0,1,2,3,4\); put \(t=s_0+s_1\) and \(h=c_3+c_4\). Every size-three or size-four gap has two short neighbors, and each short gap can neighbor at most two such long gaps. Therefore \(t\ge h\). Consequently

\[
5n-7|S|=\sum_i(5-2g_i)=3(t-h)+2s_0+2c_3+c_2\ge0.
\]

Equality forces \(t=h\), \(s_0=c_3=c_2=0\), hence an alternating sequence of gaps \(1,4,1,4,\ldots\). Conversely this gap sequence is allowed. It has total length a multiple of seven, selects five vertices per period, and gives exactly the seven cyclic rotations of `1010000`; its least period is seven. This proves the sharp bound and extremal multiplicity when \(7\mid n\).

**5. Two exceptional residues and exactness at every order.** For the upper integer rounding, put \(q=\lfloor5n/7\rfloor\), and observe that a set of size \(q\) must have deficit \(\delta=5n-7q\). The deficit is one when \(n\equiv3\pmod7\) and three when \(n\equiv2\pmod7\). If the deficit is one, the displayed nonnegative decomposition forces \(t=h\), \(s_0=c_3=0\), and \(c_2=1\). When \(t=h>0\), every short gap must be flanked by high gaps and every high gap by short gaps, leaving no place for a size-two gap. Thus \(t=h=0\), giving the single gap \((2)\), which has \(n=3\). If the deficit is three, either \(t-h=1\) and all gaps have size one or four (impossible because size-four gaps require alternating short neighbors), or \(t=h\) and \(2s_0+2c_3+c_2=3\). Again any high/short gaps would alternate and leave no room for a size-two gap, so the only possibility is three gaps all of size two, giving \(n=9\). The two stated residue corrections are therefore necessary.

For sufficiency, the following valid cyclic gap sequences realize the asserted largest cardinalities at starting orders \(n=4,5,6,7,8,10,16\), respectively:

`(0,2)`, `(1,2)`, `(0,4)`, `(1,4)`, `(1,2,2)`, `(0,2,0,4)`, `(0,2,0,3,1,4)`.

The separate starting orders \(n=3,9\) have the valid cyclic gap sequences `(2)` and `(2,2,2)`. For each of the seven other starting sequences, an adjacent short-to-long pair may be replaced by that short gap, a size-four gap, a size-one gap, and the former long gap. This preserves the adjacency rule while adding exactly seven vertices and five selected vertices. Repeating this operation covers every larger order in each residue class and proves the asserted formula for \(U_n\).

## Verification

The accompanying standalone `verify.py` derives cardinality polynomials from the displayed denominator and independently counts cyclic gap walks using a transfer-state dynamic program. It also exhaustively enumerates graph vertex subsets for \(3\le n\le19\), testing super domination by the original private-neighbor definition and inclusion-minimality by direct deletion tests. The program compares every coefficient and checks the upper-cardinality formula through \(n=154\), including the seven extremals at multiples of seven.

Run `python3 verify.py` using Python 3 standard library. One observed execution returned:

`VERIFY_OK direct_graph_n=3..19 subsets=1048568 minimal_sets=3874 rational_coefficients_n=3..154 upper_quasiperiodic=PASS extremal_seven=PASS`

The exhaustive computations are finite corroboration; the arbitrary-order assertions follow from Steps 1–5.

## Relationship to prior work

Ghanbari, Jäger, and Lehtilä (first posted September 5, 2022) establish the super-domination parameter and the number of **minimum-cardinality** super dominating sets for cycles, organized by residue modulo four. This is explicitly prior work. Their Section 6 does not count *all inclusion-minimal* super dominating sets at arbitrary cardinalities, nor determine the upper inclusion-minimal cardinality or the seven-period extremals. The present result concerns a different, more refined statistic of a standard super-domination problem.

Kaidash (2024) defines the *super domination polynomial* for **all** super dominating sets and obtains examples for some graph families. Even an all-set cardinality polynomial does not by itself determine which sets are inclusion-minimal. Only the abstract of this later work could be inspected, so possible additional overlap inside its inaccessible full text remains a publication-priority risk. The resulting inclusion-minimal polynomial must not be confused with that previously introduced all-set polynomial.

## Limitations

The theorem concerns labelled simple cycles only and inclusion-minimal sets, not general graphs or arbitrary super dominating sets. The upper formula does not assert that every cardinality below the maximum occurs. No claim is made that existing minimum super-domination numbers, counts of minimum sets, or the all-set super domination polynomial were discovered here. Independent mathematical review and comprehensive publication-priority certification have not been performed. The full text of the potentially relevant 2024 source remained inaccessible; its available abstract and metadata, rather than uninspected pages, were used in the comparison.

## References

1. N. Ghanbari, G. Jäger, and T. Lehtilä, *Super Domination: Graph Classes, Products and Enumeration*, arXiv:2209.01795, version 1 posted September 5, 2022; subsequently *Discrete Applied Mathematics* 349 (2024), 8–24. https://arxiv.org/abs/2209.01795 ; https://doi.org/10.1016/j.dam.2024.01.039
2. P. A. Kaidash, *Super Domination Polynomial of a Graph*, *Communications in Computer and Information Science* 2239 (2024), 85–95; first online December 20, 2024. https://doi.org/10.1007/978-3-031-73365-9_6
3. M. Lemańska, V. Swaminathan, Y. B. Venkatakrishnan, and R. Zuazua, *Super dominating sets in graphs*, *Proceedings of the National Academy of Sciences, India Section A* 85 (2015), 353–357 (foundational definition; not the dated motivating source).
