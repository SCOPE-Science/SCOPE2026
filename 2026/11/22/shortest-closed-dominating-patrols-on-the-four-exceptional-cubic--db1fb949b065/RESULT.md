# Shortest closed dominating patrols on the four exceptional cubic symmetric graphs of girth six

## Finding

For the four exceptional cubic symmetric graphs of girth six singled out by Kutnar and Marušič, shortest *closed dominating walks* (watchman's walks) have the following exact statistics. A rooted oriented walk specifies a starting vertex and direction. A temporal dihedral class identifies cyclic changes of starting position and reversal, but does **not** identify graph automorphisms. The final column counts orbits of temporal classes under the **full** automorphism group.

| Graph | Vertices | Watchman length \(w(G)\) | Rooted oriented optimum walks | Temporal dihedral classes | Automorphisms | Spatial orbits of temporal classes |
|---|---:|---:|---:|---:|---:|---:|
| Heawood | 14 | 10 | 10,920 | 546 | 336 | 5 |
| Möbius–Kantor | 16 | 8 | 96 | 6 | 96 | 1 |
| Pappus | 18 | 12 | 5,400 | 225 | 216 | 3 |
| Desargues | 20 | 10 | 240 | 12 | 240 | 1 |

There are exactly **ten** spatial symmetry types in all. Their representatives are given below with the last-to-first closing step understood. The ``support'' columns count distinct vertices and distinct **traversed** undirected edges; they do not silently include unused chords of the graph's induced subgraph. Vertex labels are those of the explicit graph constructions in the next section.

| Graph | Number of temporal classes in orbit | Support vertices | Support edges | Representative closed cyclic word (closing vertex omitted) |
|---|---:|---:|---:|---|
| Heawood | 42 | 6 | 5 | `0,1,0,5,0,13,8,13,12,13` |
| Heawood | 84 | 8 | 8 | `0,1,0,5,4,3,2,3,12,13` |
| Heawood | 168 | 8 | 8 | `0,1,0,5,4,3,2,7,6,5` |
| Heawood | 168 | 8 | 8 | `0,1,0,5,4,3,12,13,8,13` |
| Heawood | 84 | 10 | 10 | `0,1,2,3,4,5,6,7,8,13` |
| Möbius–Kantor | 6 | 8 | 8 | `0,1,2,3,4,5,6,7` |
| Pappus | 108 | 10 | 10 | `0,1,0,5,4,15,16,17,12,11,6,5` |
| Pappus | 9 | 12 | 12 | `0,1,2,3,10,11,6,7,14,15,16,17` |
| Pappus | 108 | 12 | 12 | `0,1,2,3,4,5,6,7,8,9,16,17` |
| Desargues | 12 | 10 | 10 | `0,1,2,3,4,5,6,7,8,9` |

The **geometric distinction** is striking. Every shortest Möbius–Kantor or Desargues patrol is a simple dominating cycle, of length eight or ten respectively. The Heawood graph also permits 42 optimal temporal walks with *tree-only* traversed support (a six-vertex double star with both central vertices of support degree three); its other temporal classes consist of 420 six-cycles with two-edge excursions and 84 ten-cycles. The Pappus graph has 108 optimum temporal classes traversing an eight-cycle with a two-edge pendant excursion, besides 117 twelve-cycles. All figures count labeled graphs using the construction below, not merely unlabeled pictures.

## Assumptions and scope

All graphs are finite, simple, connected, undirected, and cubic. A closed walk of length \(L\) is a sequence \((v_0,\ldots,v_L)\) with each \(v_i v_{i+1}\) an edge and \(v_L=v_0\); vertices and edges may repeat. Its visited vertex set \(S\) dominates if \(\bigcup_{v\in S}N[v]=V(G)\), where \(N[v]\) is the closed neighborhood in \(G\). No stationary steps are allowed. All four graphs are bipartite, so no odd-length closed walk exists. As \(G\) has more than four vertices, length zero cannot dominate.

The four graphs are uniquely fixed by these labeled constructions:

- **Heawood:** LCF sequence `[5,-5]^7` on labels \(0,\ldots,13\). Add each rim edge \(\{i,i+1\pmod {14}\}\) and each chord \(\{i,i+a_i\pmod {14}\}\), where \(a_i\) repeats \((5,-5)\).
- **Möbius–Kantor:** generalized Petersen graph \(GP(8,3)\), with outer labels \(0,\ldots,7\), inner labels \(8,\ldots,15\), rim edges \(\{i,i+1\}\), spokes \(\{i,i+8\}\), and inner edges \(\{i+8,8+(i+3)\pmod 8\}\), indices reduced modulo eight on each shore.
- **Pappus:** LCF sequence `[5,7,-7,7,-7,-5]^3` on labels \(0,\ldots,17\), with the same rim-and-chord convention as above.
- **Desargues:** \(GP(10,3)\), defined exactly analogously with ten outer, ten inner vertices and inner step three.

A *temporal dihedral class* is the set of the \(2L\) possibly coincident words produced from a length-\(L\) cyclic walk word by rotation and reversal. It is not a graph automorphism orbit. The *spatial orbit* of a temporal class is under every vertex permutation preserving adjacency. Support edges are edges actually traversed, ignoring multiplicity.

## Proof

Define the bit mask \(B_v\) of \(N[v]\), and the full mask \(U\) of all vertices. For each starting vertex \(s\), endpoint \(v\), cumulative observed mask \(M\), and integer \(t\ge 0\), let \(F_t(s,v,M)\) be the number of length-\(t\) walks from \(s\) to \(v\) whose visited closed-neighborhood union is exactly \(M\). Start with

\[
F_0(s,s,B_s)=1
\]

and every other initial entry zero. Propagate by the exact finite recurrence

\[
F_{t+1}(s,u,M\cup B_u)\mathrel{+}=F_t(s,v,M)
\qquad\text{for every edge }vu.
\]

This recurrence has no approximation: each rooted oriented vertex word contributes to exactly one transition at each step. The number of rooted closed dominating walks of length \(t\) is therefore

\[
R_t=\sum_s F_t(s,s,U).
\]

A second, structurally distinct proof certificate enumerates each length-\(t\) adjacent-vertex sequence directly, accumulating closed neighborhoods and accepting it exactly if it closes and covers \(U\). For the four graphs it finds the following *maximum number of covered vertices* among closed walks of each displayed even length:

| Graph | \(t=2\) | \(t=4\) | \(t=6\) | \(t=8\) | \(t=10\) | \(t=12\) |
|---|---:|---:|---:|---:|---:|---:|
| Heawood | 6 | 8 | 12 | 13 | **14** | — |
| Möbius–Kantor | 6 | 8 | 12 | **16** | — | — |
| Pappus | 6 | 8 | 12 | 15 | 16 | **18** |
| Desargues | 6 | 8 | 12 | 14 | **20** | — |

Each value less than graph order rules out domination at that length, while the first full-cover count is achieved by the displayed representatives. Bipartiteness eliminates all odd lengths, and length zero observes only four vertices. This proves each stated watchman number, including the possibility of repeated edges.

For each shortest closed dominating walk, delete its repeated closing vertex to obtain a cyclic word of length \(L\). Compute the lexicographic minimum among its rotations and reversed rotations. In a finite graph this is a well-defined canonical representative of the temporal dihedral class. Exhaustive direct enumeration then produces the exact temporal-class column in the first table. To obtain full graph automorphisms, independently enumerate bijections \(p\) of vertices with \(\operatorname{dist}(p(u),p(v))=\operatorname{dist}(u,v)\) for all pairs; such bijections are precisely graph automorphisms because distance one is adjacency. Apply all of them to each canonical cyclic word, canonicalize again, and partition the finite set of optimum temporal classes. The ten representatives and orbit sizes in the second table result. The sizes in each row sum to the independent total of temporal classes: \(546,6,225,12\).

The support statements follow by listing the unordered edges actually traversed in each representative and observing that an automorphism preserves their incidence structure. One representative has traversed tree support of degree sequence \((1,1,1,1,3,3)\); the Heawood eight-edge supports have a unique six-cycle, the Pappus ten-edge support has a unique eight-cycle, and all remaining orbit representatives traverse simple cycles. Thus no distinct support structure is conflated by the counting convention.

## Verification

`check_watchman.py` is a self-contained Python 3 script using only its standard library. It implements the exact mask recurrence, a separately written direct depth-first walk enumeration, temporal canonicalization, distance-preserving automorphism generation and orbit partitioning; it asserts every figure in both tables. Run `python3 check_watchman.py` from the extracted package directory.

`check_watchman.cpp` is an independently written C++17 depth-first enumerator with its own graph constructors, bit masks, dihedral normal form and traversed-support tally. Compile using `c++ -O2 -std=c++17 -Wall -Wextra -pedantic check_watchman.cpp -o check_watchman` and execute `./check_watchman`. It checks all minimum lengths, optimum rooted/dihedral counts, all smaller even lengths, coverage maxima, and support-type subtotals. Both programs were executed from their final on-disk source files and printed `ALL PASS`. Python additionally verifies the complete automorphism orbit decompositions; the C++ implementation independently confirms the walk and structural input to this orbit check.

The domain for the finite certificate is all rooted directed closed walks of lengths up to \(12\) on the four explicitly constructed labeled graphs, rather than samples or a heuristic search. Larger graph orders, related graph families, weighted walks and constraints on continuous surveillance are not claimed.

## Relationship to prior work

The 1990s watchman's walk literature established the minimum closed dominating walk model. Dyer and Milley (2012), pages 97–108, define that model precisely in their introduction and proceed to a different multiple-guard time-constrained problem on trees. Dyer and Howell's work on Steiner triple systems (2017) examines the *block intersection graph* (its vertices are triples), not the point–line Levi graph represented here by Heawood. Kutnar and Marušič (2009), with an identified public presentation in February 2008, single out exactly these four cubic symmetric girth-six graphs as exceptions to their generalized-dihedral-Cayley classification; that classification concerns graph symmetry rather than dominating patrols.

The directly plausible competing work is Dyer and Howell, *The multiplicity of watchman's walks*, Congressus Numerantium 226 (2016), pages 301–317. Its full text could not be obtained from the accessible open sources, so its possible overlap with optimum-walk counting is an explicit historical priority risk, not a proof of novelty. The authors' accessible abstract on *Unique watchman's walks* concerns existence/constructions of unique walks, with no identified named-graph classification. A separate 2016 pursuit-evasion paper by Choi, Georges and Mauro uses the same phrase *watchman number* for a **different parameter**—the number of agents required to capture moving intruders—and must not be conflated with shortest dominating closed-walk length.

Searches for aliases (watchman's walk, MCDW, minimum closed dominating walk, closed neighborhood dominating tour), graph names, counts, equivalences, and existing indexed graph results revealed no implication of the complete ten-orbit classification. A negative search is not a novelty certificate.

## Limitations

The statements are exact only for the four specified simple graphs under the specified static closed-domination model. The finite certificates rigorously settle each listed graph but do not establish a formula for arbitrary cubic graphs of girth six or prove publication priority. One directly relevant multiplicity paper is inaccessible in full and must be checked before asserting absolute originality. The source date below identifies a verified public mathematical presentation associated with the graph family, **not** an invented original publication date for the walk classification. No independent scholarly audit has been carried out.

## References

1. Klavdija Kutnar, *A complete classification of cubic symmetric graphs of girth 6*, workshop talk, Yeungnam University, 4 February 2008; library record COBISS.SI-ID 1024003924. https://plus-legacy.cobiss.net/cobiss/up/sl/bib/1024003924?db=upuk&ds=true
2. K. Kutnar and D. Marušič, *A complete classification of cubic symmetric graphs of girth 6*, Journal of Combinatorial Theory Series B 99 (2009), 162–184, DOI:10.1016/j.jctb.2008.06.001. https://doi.org/10.1016/j.jctb.2008.06.001
3. D. Dyer and R. Milley, *A time-constrained variation of the Watchman's Walk Problem*, Australasian Journal of Combinatorics 53 (2012), 97–108. https://ajc.maths.uq.edu.au/pdf/53/ajc_v53_p097.pdf
4. D. Dyer and J. Howell, *Watchman's walks of Steiner triple system block intersection graphs*, Australasian Journal of Combinatorics 68 (2017), 23–34. https://ajc.maths.uq.edu.au/pdf/68/ajc_v68_p023.pdf
5. D. Dyer and J. Howell, *The multiplicity of watchman's walks*, Congressus Numerantium 226 (2016), 301–317. Full text not inspected; bibliographic identification only.
6. D. Dyer, J. Howell and B. Pittman, *The watchman's walk problem on directed graphs*, arXiv:2007.13901 (first submitted 27 July 2020); its undirected definition supplies further context, but its stated results concern directed tournaments and multipartite orientations. https://arxiv.org/abs/2007.13901
