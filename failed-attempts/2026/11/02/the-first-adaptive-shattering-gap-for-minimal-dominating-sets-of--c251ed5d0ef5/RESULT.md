# The first adaptive shattering gap for minimal dominating sets of paths, amplified inside connected trees

## Finding
For a finite simple graph \(G\), let \(\mathcal D_{\min}(G)\) be the family of its **inclusion-minimal** dominating vertex sets, viewed as Boolean functions on \(V(G)\) by membership. A set \(D\subseteq V(G)\) is dominating when every vertex lies in \(D\) or has a neighbor in \(D\). Inclusion-minimality is not the same as having the smallest cardinality.

For the path \(P_n\) on \(n\) vertices, \(1\le n\le 10\), the dimensions of \(\mathcal D_{\min}(P_n)\) agree. On the eleven-vertex path their first strict separation occurs:
\[
\operatorname{VCdim}(\mathcal D_{\min}(P_{11}))=4,
\qquad \operatorname{Ldim}(\mathcal D_{\min}(P_{11}))=5.
\]
There are exactly \(36\) inclusion-minimal dominating sets of \(P_{11}\).

For every integer \(s\ge1\), construct a connected tree \(T_s\) from \(s\) vertex-disjoint copies of \(P_{11}\), with vertices \(v_1^{(i)},\ldots,v_{11}^{(i)}\) in copy \(i\), by adding \(v_2^{(i)}v_2^{(i+1)}\) for \(1\le i<s\). Then \(T_s\) has exactly \(11s\) vertices, maximum degree at most \(4\), and
\[
\operatorname{VCdim}(\mathcal D_{\min}(T_s))=4s,
\qquad \operatorname{Ldim}(\mathcal D_{\min}(T_s))=5s.
\]
Hence adaptive minus static shattering has an unbounded, linearly growing gap on **connected trees of maximum degree four**.

## Assumptions and scope
Graphs are finite, simple, undirected; isolated vertices are allowed in the definition, although none occur in \(T_s\). A Boolean vertex query asks whether the unknown inclusion-minimal dominating set contains the specified vertex. VC dimension means a fixed set of queried vertices has all Boolean traces; Littlestone dimension means a complete adaptively queried binary tree has a consistent concept on every root-to-leaf branch. The finite minimality statement quantifies only over paths with \(1\le n\le 11\), not all trees of these orders. The connected infinite-family statement is exact for every positive integer \(s\).

## Proof
**1. Finite path certificate, with complete search.** Number the vertices of \(P_n\) by \(0,\ldots,n-1\). Represent a vertex subset by a bit mask \(d\). With \(N[i]\) the closed neighborhood mask, \(d\) dominates iff \(d\mathbin{\&}N[i]\ne0\) for every \(i\). A dominating \(d\) is inclusion-minimal iff removal of any selected bit makes it fail domination. Independently, inclusion-minimality is equivalent to the private-neighbor property: for every selected \(i\), some \(j\) has \(d\mathbin{\&}N[j]=2^i\). Both predicates are implemented and compared for every one of the \(2^n\) subsets at every \(1\le n\le11\).

For each resulting finite concept class, enumerate all \(2^n\) query supports \(S\) and evaluate all traces \(d\cap S\). The largest \(S\) for which all \(2^{|S|}\) traces appear is its exact VC dimension. In particular, the support \(\{0,3,5,7\}\) is shattered for \(P_{11}\), and **none of its \(\binom{11}{5}=462\) five-element supports is shattered**. Any larger shattered support would contain a shattered five-element subset, proving the sharp VC upper bound.

The exact finite Littlestone recurrence is
\[
r(C)=\max\bigl(\{0\}\cup\{1+\min(r(C^0_x),r(C^1_x)):\ C^0_x\ne\varnothing,\ C^1_x\ne\varnothing\}\bigr),
\]
where \(C_x^b\) retains the concepts answering \(b\) at vertex \(x\), and a class of at most one concept has rank zero. Every nontrivial query decreases class size on both children, so memoized recursion computes the rank exactly. The executable package evaluates the complete recursion for all sizes through eleven, constructs a full depth-\(r(C)\) binary tree, and verifies every leaf against its root-to-leaf answers. For \(P_{11}\), the resulting depth-five tree has \(32\) distinct leaf concepts. Conversely, \(|\mathcal D_{\min}(P_{11})|=36<64\), so a complete depth-six tree is impossible; this gives an independent cardinality upper bound of five.

The complete census, with rows \((n,|\mathcal D_{\min}(P_n)|,\operatorname{VCdim},\operatorname{Ldim})\), is:

| \(n\) | concepts | VC dimension | Littlestone dimension |
|---:|---:|---:|---:|
| 1 | 1 | 0 | 0 |
| 2 | 2 | 1 | 1 |
| 3 | 2 | 1 | 1 |
| 4 | 4 | 2 | 2 |
| 5 | 4 | 2 | 2 |
| 6 | 7 | 2 | 2 |
| 7 | 9 | 3 | 3 |
| 8 | 13 | 3 | 3 |
| 9 | 18 | 4 | 4 |
| 10 | 25 | 4 | 4 |
| 11 | 36 | 4 | 5 |

**2. Support-vertex gluing lemma.** Suppose a graph consists of nonempty components \(G_i\), each with a pendant leaf \(a_i\) whose unique neighbor is \(b_i\). Add arbitrary edges **only among the vertices \(b_i\)**, leaving every \(a_i\) pendant. Then the resulting graph's inclusion-minimal dominating sets are exactly unions \(\bigcup_i D_i\) with \(D_i\in\mathcal D_{\min}(G_i)\).

Indeed, every minimal dominating set of either graph contains exactly one of \(a_i,b_i\): at least one to dominate \(a_i\), and not both, since \(a_i\) would then be redundant. Thus each \(b_i\) is dominated by a vertex of its original component. Added edges cannot newly dominate any vertex other than a \(b_i\), and cannot create a new indispensable private neighbor for a selected vertex: any \(b_i\) is already dominated by its selected \(a_i\) or \(b_i\), so it cannot be the private neighbor of any other selected vertex. Conversely, the selected member of \(\{a_i,b_i\}\) always retains \(a_i\) as its private neighbor, and all other internal private neighbors are unaffected by added edges. Hence domination and inclusion-minimality factor componentwise.

**3. Additivity.** If \(C\) and \(E\) are nonempty finite Boolean concept classes on disjoint query domains, their Cartesian product satisfies
\[
\operatorname{VCdim}(C\times E)=\operatorname{VCdim}(C)+\operatorname{VCdim}(E),\quad
\operatorname{Ldim}(C\times E)=\operatorname{Ldim}(C)+\operatorname{Ldim}(E).
\]
The VC identity follows by independent traces and by restriction of any shattered support to the two domains. For Littlestone dimension, concatenate complete shattered trees for the lower bound. For the upper bound use induction on the number of concepts: a root query belongs to one factor, say \(C\); among its two nonempty answer classes at least one has rank at most \(\operatorname{Ldim}(C)-1\), or else \(C\)'s rank would be larger. Induction bounds the corresponding product child by \(\operatorname{Ldim}(C)+\operatorname{Ldim}(E)-1\), ruling out a deeper complete tree.

**4. Connected amplification.** Each module \(P_{11}\) has pendant \(v_1^{(i)}\) with support vertex \(v_2^{(i)}\). Linking consecutive support vertices yields a connected tree without changing the product description of its minimal dominating sets, by Step 2. Apply Step 3 to the exact module dimensions in Step 1. This establishes \(4s\) and \(5s\) for all \(s\).

## Verification
Run `python3 verify_minimal_domination.py` with the three adjacent generated JSON/text files. The script independently implements deletion and private-neighbor tests, enumerates all vertex subsets and query supports through eleven vertices, evaluates the exact Littlestone recurrence, regenerates and checks complete witness trees, checks every five-element support on \(P_{11}\), and checks all \(36^2=1296\) paired module concepts under one supporting-edge join. `adaptive_trees.json` contains complete adaptive certificates for all eleven orders; `path_census.json` contains the exhaustive dimension table and search counts; `verification_output.txt` is the expected terminal output. Successful completion prints `MINIMAL_DOMINATING_PATH_FIRST_GAP_ALL_CHECKS_PASS`.

## Relationship to prior work
Rote [1] established extremal counts and output-sensitive enumeration of minimal dominating sets in trees, including the private-neighbor formulation and the support-vertex gluing principle. Those ingredients are acknowledged as prior work; they do **not** determine the vertex-membership VC or Littlestone dimensions or the first path gap. Petr, Portier and Versteegen [2] study **minimum-cardinality** dominating sets, a different family of concepts. Existing results on maximal independent sets of forests concern the proper subclass of inclusion-minimal dominating sets consisting of independent sets: inclusion of concept families does not imply equality or strict inequality of their VC/Littlestone dimensions. The present result uses exact finite shattering to identify a different obstruction, then propagates it on connected trees.

## Limitations
The exact path census stops at eleven vertices; it establishes neither a closed formula for all paths nor a classification of every tree of order eleven. The infinite result applies to the particular explicitly glued trees, not all bounded-degree trees. Exhaustive small computations prove only the stated finite cases; the unrestricted infinite-family step has a separate mathematical proof. Historical priority beyond inspected sources and database searches remains uncertain, and independent audit has not been performed.

## References
[1] Günter Rote, *The Maximum Number of Minimal Dominating Sets in a Tree*, Proceedings of SODA 2019, published January 2, 2019, DOI 10.1137/1.9781611975482.73; expanded open preprint *Minimal Dominating Sets in a Tree: Counting, Enumeration, and Extremal Results*, arXiv:1903.04517 (March 11, 2019).

[2] Jan Petr, Julien Portier, Leo Versteegen, *On the number of minimum dominating sets and total dominating sets in forests*, arXiv:2206.13182 (June 27, 2022).
