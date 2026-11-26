# Minimum identifying-code mobility in the McGee cage: two tetrahedra and frozen optima

## Finding

The McGee graph \(H\), the unique cubic graph with \(24\) vertices and girth \(7\), has \(384\) minimum ordinary radius-one identifying codes, each with \(11\) selected vertices. The minimum size and code count were determined previously; they are used as inputs to a new classification of the **optimum-preserving one-detector exchange graphs**.

For two minimum codes \(C,D\), a **token jump** replaces one selected vertex with one unselected vertex, so \(|C\setminus D|=|D\setminus C|=1\). A **token slide** is a token jump with the removed and inserted vertices adjacent in \(H\). Let \(\mathcal J\) and \(\mathcal S\) be the graphs on all \(384\) minimum codes with these two types of adjacency. Then

\[
\boxed{\mathcal J\cong176K_1\;\sqcup\;16K_2\;\sqcup\;16T,\qquad
\mathcal S\cong320K_1\;\sqcup\;32K_2.}
\]

Here \(T\) is the following particular connected eleven-vertex graph. Take two disjoint copies of \(K_4\), identify exactly one vertex of one copy with exactly one vertex of the other, and attach four distinct pendant vertices, one to each of two distinct nonshared vertices in each copy of \(K_4\). Thus \(T\) has \(11\) vertices, \(16\) edges, and diameter \(4\). Of its \(16\) edges, exactly two are slides of minimum identifying codes; both of these slide-edges are pendant edges of \(T\). None of the sixteen isolated \(K_2\) components of \(\mathcal J\) gives a legal slide.

Consequently, \(\mathcal J\) has exactly \(208\) connected components and \(272\) edges, whereas \(\mathcal S\) has exactly \(352\) components and \(32\) edges. In particular, \(176\) of the \(384\) minimum configurations admit no legal jump at all, while \(320\) admit no legal slide.

## Assumptions and scope

Label vertices \(0,1,\ldots,23\) cyclically modulo \(24\). Add each undirected cycle edge \(\{i,i+1\}\), then add chord \(\{i,i+s_i\}\), where \(s_i=12\) for \(i\equiv0\pmod3\), \(s_i=7\) for \(i\equiv1\pmod3\), and \(s_i=-7\) for \(i\equiv2\pmod3\). This is the standard LCF notation \([12,7,-7]^8\), with duplicate undirected chords counted only once. The graph has \(36\) edges and degree three.

For any \(C\subseteq V(H)\) and \(v\in V(H)\), define its identifying signature \(I_C(v)=C\cap N_H[v]\), where \(N_H[v]\) is the closed neighborhood of \(v\). The set \(C\) is an identifying code if all \(24\) signatures are nonempty and pairwise distinct. This result concerns **only** size-minimal identifying codes and moves maintaining that minimum at every step. It does not concern reconfiguration through larger intermediate sets, nor codes robust against multiple simultaneous failures.

## Proof

**Lower cardinality bound.** Let \(k=|C|\) for an identifying code. Since \(H\) is cubic, the total number of incidences of selected vertices with closed neighborhoods equals \(\sum_v|I_C(v)|=4k\). Pairwise distinct nonempty signatures include at most \(k\) singletons, because there are only \(k\) possible singleton labels. All other signatures have size at least two. Hence \(4k\ge 2(24-k)+k=48-k\), and \(k\ge\lceil48/5\rceil=10\). In particular, to determine the minimum it suffices to check all subsets of sizes \(10\) and \(11\), provided an identifying code of size \(11\) is found.

**Exhaustive identification.** A vertex set \(C\) identifies \(H\) precisely when it intersects the \(24\) nonempty closed-neighborhood masks \(N_H[v]\) and each of the \(276\) symmetric-difference masks \(N_H[u]\mathbin\triangle N_H[v]\) for distinct vertices \(u,v\). Both standalone verifiers construct the LCF graph and enumerate **every** one of the \(\binom{24}{10}=1{,}961{,}256\) ten-element sets and \(\binom{24}{11}=2{,}496{,}144\) eleven-element sets. One uses direct signature comparison on bit masks, while the other uses the equivalent complete 300-constraint hitting-set test on combinatorially generated masks. The results are zero identifying codes of size ten and exactly \(384\) of size eleven, reproducing the previously known optimum classification with a complete finite certificate.

**Exact transition graphs.** Store the \(384\) successful eleven-element masks in a lookup dictionary. For each such mask, choose each of its eleven selected vertices \(a\) and each of the thirteen unselected vertices \(b\); replace \(a\) by \(b\) and test membership of the new mask in that dictionary. This enumerates **every** token jump, since every one-vertex replacement is represented exactly once in this ordered search. Retain just those transitions where \(\{a,b\}\in E(H)\) to obtain all token slides. Divide oriented adjacency totals by two to count undirected edges.

Both verifiers reconstruct the exact jump degree distribution (degree \(0\): \(176\) states; degree \(1\): \(96\); degree \(3\): \(32\); degree \(4\): \(64\); degree \(6\): \(16\)). Breadth-first component enumeration gives \(176\) isolated vertices, \(16\) two-vertex one-edge components, and \(16\) eleven-vertex sixteen-edge components. A separate test of each eleven-vertex component verifies that its seven nonleaf vertices consist of exactly two four-cliques with one common vertex, and that its four leaves have distinct noncentral attachments, two in each four-clique. Hence all sixteen are isomorphic to \(T\), as defined above; this is not inferred merely from a matching size or degree sequence.

For token slides, component enumeration gives \(320\) isolated vertices and \(32\) isolated edges. Cross-checking each jump component shows precisely two slide-edges inside each copy of \(T\), always at its leaves, and none inside a jump-only \(K_2\). This proves both displayed decompositions and all their consequences for counts, mobility, and component diameter.

The finite enumeration is exhaustive because every subset in the two relevant cardinality layers, every selected/unselected replacement, and every resulting finite connected component is examined. No sample, partial prefix, probability estimate or unverified solver certificate is used.

## Verification

The accompanying `verify_cpp.cpp` is a standalone C++17 implementation of the direct-signature exhaustive search and reconfiguration component counts. The accompanying `verify_python.py` is an independent Python standard-library implementation using all \(300\) identification constraints; it additionally checks girth seven, the precise graph structure of each eleven-state component, and the position of slides within jump components.

From the directory containing both files, execute:

```sh
g++ -O3 -std=c++17 verify_cpp.cpp -o verify_mcgee
./verify_mcgee
python3 verify_python.py
```

Both scripts terminate with `VERIFY_OK` when every asserted equality holds. The Python and C++ searches were executed independently from the packaged source code before the result was finalized. The original code set and its thirteen automorphism orbits had been established in prior work; no new claim is made for those antecedents.

## Relationship to prior work

The basic identification requirement and its role in sensor placement are classical. Balbuena, Foucaud, and Hansberg (initial public arXiv version July 27, 2014) study bounds for locating-dominating sets and identifying codes in graphs of girth at least five, including cubic graphs, but not optimum-preserving exchange components on the McGee cage. Laihonen (2008) studies existence of stronger identifying codes in cages, not the present token-mobility question; the complete text was not obtained for comparison, so there is residual literature-access risk.

An earlier published **exact** McGee classification, *All \(384\) minimum identifying codes of the McGee cage* (2026), established the minimum size, the count, and thirteen symmetry orbits with representatives. That prior result logically supplies all feasible configurations, but does not state their exchange adjacency, component types or restrictions on adjacent detector relocation. The present finding is a new computation and structural classification **on the previously known set of optimal codes**; it is not an independent discovery of the 384 masks. Published reconfiguration studies on other graphs address the same general move notions but not this graph's particular optimum space.

## Limitations

This is a finite theorem about the unique \((3,7)\)-cage only; there is no claim for all cubic graphs, other cages or larger detector budgets. The result relies on exhaustive exact computation for the connected-component classification; the code artifacts, input graph and output checks are self-contained, but no short closed-form structural proof of the component counts is asserted. The earlier exact optimizer census makes it possible to derive the result by a finite secondary computation; the novelty claimed is strictly the resulting exchange geometry, not the optimum cardinality or the list of codes. Historical priority cannot be guaranteed for unindexed enumerations, and the full 2008 cages paper was not available to inspect.

## References

1. W. F. McGee, *A Minimal Cubic Graph of Girth Seven*, Canadian Mathematical Bulletin 3 (1960), 149–152, DOI: 10.4153/CMB-1960-018-1.
2. C. Balbuena, F. Foucaud, A. Hansberg, *Locating-dominating sets and identifying codes in graphs of girth at least 5*, first public arXiv version July 27, 2014, arXiv:1407.7263, https://arxiv.org/abs/1407.7263.
3. T. Laihonen, *On cages admitting identifying codes*, European Journal of Combinatorics 29 (2008), 737–741, DOI: 10.1016/j.ejc.2007.02.016.
4. *All \(384\) minimum identifying codes of the McGee cage*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-all-384-minimum-identifying-codes-of-the-mcgee-cage--9c86d0c9b13e.
5. E. W. Weisstein, *McGee Graph*, MathWorld, https://mathworld.wolfram.com/McGeeGraph.html.
