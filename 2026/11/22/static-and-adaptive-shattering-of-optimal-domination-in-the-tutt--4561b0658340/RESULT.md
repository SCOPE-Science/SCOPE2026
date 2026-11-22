# Static and adaptive shattering of optimal domination in the Tutte–Coxeter graph

## Finding
Let \(G\) be the Tutte–Coxeter graph: the bipartite incidence graph of the unique generalized quadrangle \(GQ(2,2)\), with fifteen points and fifteen lines. Let \(\mathcal D\) consist of all **minimum-cardinality ordinary dominating vertex sets** of \(G\), regarded as Boolean concepts on the thirty vertices: a query at a vertex asks whether that vertex belongs to the unknown set. There are exactly ninety concepts, each containing nine vertices. Their complete VC-shattering polynomial is
\[
\Phi_{\mathcal D}(z)=1+30z+390z^2+2730z^3+420z^4.
\]
In particular,
\[
\operatorname{VCdim}(\mathcal D)=4,\qquad
\operatorname{Ldim}(\mathcal D)=5.
\]
The 420 shattered four-element supports have exact point/line compositions \((1,3),(2,2),(3,1)\), occurring respectively 120, 180, and 120 times. The shattered-support complex is nonpure, having 1980 inclusion-maximal three-element supports in addition to its 420 four-element facets; no two-element support is maximal.

There is also an exact geometric description of every shattered support. For a support \(S\), first demand that no selected point is incident with any selected line. The empty set and every singleton are shattered. Every two-element support satisfying this condition is shattered. A three-element support satisfying it is shattered unless all three vertices are points with **no collinear pair**, or all three are lines with **no concurrent pair**. For a four-element support satisfying it, shattering occurs precisely in these three cases:

- One point and three lines, the three lines concurrent.
- Three points and one line, the three points collinear.
- Two distinct collinear points \(P_1,P_2\) on a line \(L\), and two distinct concurrent lines \(m_1,m_2\) at a point \(Q\): writing \(R\) for the third point on \(L\), we require that \(Q\ne R\), the points \(Q,R\) are collinear, and \(m_1,m_2\) are precisely the other two lines through \(Q\) besides the line \(QR\).

No support of cardinality at least five is shattered. These conditions give a complete finite incidence characterization, not merely the VC dimension.

## Assumptions and scope
All graph domination is *ordinary closed-neighborhood domination*: \(D\subseteq V(G)\) dominates when every vertex is either in \(D\) or adjacent to a member of \(D\). “Minimum” means minimum cardinality, not inclusion-minimality. Shattering means that all \(2^{|S|}\) binary membership traces occur on \(S\). A complete binary adaptive test tree of depth \(d\), with distinct hypotheses witnessing the paths, establishes Littlestone dimension at least \(d\). The result concerns precisely the finite \(GQ(2,2)\) incidence graph, not all generalized quadrangles.

An entirely explicit model fixes reproducible vertex numbering. Represent the fifteen points by the nonzero vectors \(a\) of \(\mathbb F_2^4\), encoded by integers 1 through 15, in increasing order and labeled 0 through 14. Use the nondegenerate alternating form
\[
\langle a,b\rangle=a_0b_2+a_2b_0+a_1b_3+a_3b_1\pmod 2.
\]
The fifteen lines are the ordered-by-lexicographic-order triples \(\{a,b,a+b\}\), for distinct nonzero \(a,b\) with \(\langle a,b\rangle=0\), labeled 15 through 29. Incidence is membership of a point in one of these triples. This gives a connected, cubic, 30-vertex bipartite graph with 45 edges.

## Proof
**1. Exhaustiveness of the ninety optimal concepts.** Héger and Hernandez Lucas [1], Theorems 2.1, 4.5 and 5.1, prove that for every finite \(GQ(q,q)\), the ordinary domination number is \(2q^2+1\), and every dominating set at that size is one of two flag-based constructions. At \(q=2\), each of the 45 incident point–line flags \((P,L)\) supplies two sets. Let \(T(P,L)\) consist of the vertices whose graph distance from the **two-vertex set** \(\{P,L\}\) is exactly two. It contains eight vertices. The two optimum dominating sets are
\[
T(P,L)\cup\{P\},\qquad T(P,L)\cup\{L\}.
\]
The source provides the completeness theorem; the supplied independent programs construct all flags and check that all 90 produced sets are distinct, have nine members and dominate every vertex. Thus there are no omitted optimum concepts.

**2. Exact support criterion and face counts.** Fix any ordered query support \(S=\{v_1<\cdots<v_k\}\). For each vertex \(v\) construct the 90-bit mask \(Y_v\) of optimum concepts containing \(v\). Start with a single nonempty cell \(C_\varnothing\), the full 90-bit hypothesis space. At each query \(v_i\), split *every* current trace cell \(C\) into \(C\cap Y_{v_i}\) and \(C\setminus Y_{v_i}\). Then \(S\) is shattered if and only if **each** of its \(2^k\) terminal cells is nonempty. This follows directly by induction on the number of queried vertices: every cell contains exactly the hypotheses sharing its prescribed answer prefix.

The standalone `verify_gq2.py` constructs all concepts directly from the finite symplectic incidence model. It explicitly evaluates this trace condition on every one of the
\[
\sum_{k=0}^{5}\binom{30}{k}=174437
\]
query supports of cardinality at most five, and independently evaluates the stated incidence criterion on each support. The two Boolean answers agree for all 174437 supports. Its exhaustive, deterministic loops and test predicates are included verbatim. The independent C++17 program `crosscheck_gq2.cpp` regenerates the same graph and optimal concepts without input files, then recursively enumerates every shattered support up to cardinality five using increasing vertex order and hereditary pruning. Both implementations give the exact coefficient list
\[
(s_0,s_1,s_2,s_3,s_4,s_5)=(1,30,390,2730,420,0).
\]
No support of larger size can be shattered, because all of its five-element subsets would then be shattered. The finite enumeration is an exhaustive finite proof for this fixed graph; it is not an infinite extrapolation.

The geometric criterion additionally explains the counts. There are \(\binom{30}{2}-45=390\) nonincident two-vertex supports. Among the \(2890\) independent three-vertex sets, exactly 80 three-point and 80 three-line pairwise noncollinear/nonconcurrent triads are excluded, leaving 2730. For four-element supports, a choice of a concurrency point and a point outside its three incident lines gives \(15\cdot8=120\) of type \((1,3)\); duality gives 120 of type \((3,1)\). Of type \((2,2)\), choose the two point queries as one of the 45 collinear point pairs, let \(R\) be the third point on their line, choose \(Q\) as one of the four points off that line collinear with \(R\), then take the two lines at \(Q\) different from \(QR\). This gives \(45\cdot4=180\). The supplied enumeration checks every premise of these classifications, not just the numerical totals. Enumerating which shattered triples extend to four-element supports leaves exactly 1980 maximal triples, proving nonpurity.

**3. Exact adaptive dimension.** The file `TREE_DEPTH5.json` is a fully explicit complete binary depth-five tree: its 31 internal nodes are vertex queries and its 32 leaves are indices of pairwise distinct optimum concepts. The standalone Python verifier reconstructs the concepts in the specified order and checks **every** root-to-leaf answer against its indicated concept, establishing \(\operatorname{Ldim}\ge5\). For the upper bound, each of the thirty graph vertices belongs to exactly 27 of the ninety optimum concepts; both programs independently verify this uniform incidence number. If a complete depth-six tree existed, the **positive** child of its root would have to contain at least \(2^5=32\) distinct concepts, one for each length-five continuation, contradicting the 27 available positive concepts. Hence \(\operatorname{Ldim}\le5\), as claimed.

## Verification
Run `python3 verify_gq2.py TREE_DEPTH5.json` with Python 3 and standard library only. Compile and run `crosscheck_gq2.cpp` with `c++ -std=c++17 -O2 crosscheck_gq2.cpp -o crosscheck_gq2 && ./crosscheck_gq2`. Both reconstruct the geometry; no precomputed concept table is trusted. Python verifies all 174437 support subsets through cardinality five against the explicit structural criterion, verifies the depth-five adaptive tree and exact upper bound, and counts maximal faces. C++ performs a separate 90-concept construction and exhaustive hereditary recursion. The actual successful output is included in `VERIFY_OUTPUT.txt`. Files are indexed relative to the directory holding this package. This computation checks an **entire finite universe**, not a sample of larger cases.

## Relationship to prior work
Héger and Hernandez Lucas [1] determine the domination number and provide a complete classification of optimum dominating sets of every equal-order generalized quadrangle; their templates establish the 90 hypotheses used here. They do not enumerate binary membership traces, characterize shattered point–line supports, compute an adaptive decision tree or establish the strict learning gap in this 30-vertex example. The result here is a derived invariant of the *known* optimum family, not a new optimum-domination classification. Benediktsson, Macpherson and Adler [2] investigate VC-dimension for *vertex neighborhoods of Johnson and Hamming graphs*, not minimum-dominating-set membership on this incidence graph. Published mathematical computations of the **ordinary independence complex of the Tutte–Coxeter graph** [3] concern a different simplicial complex; in particular, the independent-set face counts do not equal the shattered-support counts. Published work on **inclusion-minimal** dominating sets of cycles [4] has a static–adaptive separation but neither the same graph nor the minimum-cardinality concept class, and does not imply this exact polynomial.

## Limitations
This is a fixed, finite classification of one canonical graph; there is no assertion of a uniform formula for all \(GQ(q,q)\), no integral homology calculation, no theorem about minimal (rather than minimum) dominating sets, and no independent external audit. The source [1] is decisive for completeness of the 90 concepts. The shattering and adaptive calculations are complete deterministic finite verifications with supplied executable sources and a full tree witness; they have not been formally verified by an external prover. Historical originality is assessed against the cited inspected material and accessible research records; an unindexed equivalent calculation may exist.

## References
[1] T. Héger and L. Hernandez Lucas, *Dominating sets in finite generalized quadrangles*, Ars Mathematica Contemporanea 19 (2020), 61–76, first published online 2020-11-02, doi:10.26493/1855-3974.2106.423. Lawful public primary PDF: https://www.dlib.si/stream/URN%3ANBN%3ASI%3ADOC-JR7GQZUD/b02789d0-d597-4cd0-85c5-b7c9e2e32e11/PDF.

[2] B. G. Benediktsson, D. Macpherson and I. Adler, *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042, first posted 2020-07-31, https://arxiv.org/abs/2007.16042.

[3] *Nine eight-dimensional spheres in the Tutte–Coxeter independence complex*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-nine-eight-dimensional-spheres-in-the-tutte-coxeter-independence--ace94fe0e86e.

[4] *The first minimal-domination cycle gap: complete five-query traces and a vertex-transitive amplification*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-first-minimal-domination-cycle-gap-complete-five-query-trace--84ef6ec729bc.
