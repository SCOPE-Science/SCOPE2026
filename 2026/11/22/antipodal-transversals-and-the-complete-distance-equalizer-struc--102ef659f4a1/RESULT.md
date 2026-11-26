# Antipodal transversals and the complete distance-equalizer structure of the dodecahedral graph

## Finding

Let \(D=GP(10,2)\) be the dodecahedral graph. A distance-equalizer set \(S\) requires that for each distinct \(u,v\notin S\), there is a vertex \(w\in S\) with \(d(u,w)=d(v,w)\). The new assertion here is the **distribution of symmetry orbit sizes** of the minimum distance-equalizer sets, under the full \(120\)-element graph automorphism group:

| Orbit size | Stabilizer order | Number of orbits |
|---:|---:|---:|
| 12 | 10 | 2 |
| 20 | 6 | 4 |
| 40 | 3 | 2 |
| 60 | 2 | 10 |
| 120 | 1 | 2 |

In particular, 240 of the 1024 labeled minimum sets have trivial stabilizer, and 24 have stabilizer of order ten. The distribution refines the known count of 20 equivalence classes of self-dual dodecahedral vertex 2-colorings (Palmer and Robinson [1]); that count is not claimed as new.

## Assumptions and scope

Use vertices \(o_i,p_i\) for \(i\in\mathbb Z/10\mathbb Z\), with edges \(o_io_{i+1},o_ip_i,p_ip_{i+2}\). Distances are ordinary unweighted shortest-path distances, and the antipodes of these vertices have index \(i+5\) in the same layer. A configuration is an unordered vertex subset; the action is by all graph automorphisms, including orientation-reversing symmetries. The stabilizer orders in the table do not classify stabilizer subgroups up to conjugacy.

## Reduction and proof

**Distance-equalizer sets as antipodal transversals.** The distance rows and witness-locus table in [2, proof steps 1–2] give \(d(w,u)+d(w,\bar u)=5\) and show that for non-antipodal distinct \(u,v\) the locus \(W(u,v)=\{w:d(w,u)=d(w,v)\}\) is the union of two whole antipodal pairs. Thus no antipodal pair admits a witness. A distance-equalizer set must hit every antipodal pair, and this condition suffices: two distinct outside vertices are then non-antipodal, and the set hits each of the complete antipodal pairs in their witness locus. These are direct consequences of [2], although [2] uses the loci to study the different predicate of ordinary resolving sets.

For context, the generating polynomial is therefore \((2z+z^2)^{10}\). The minimum is ten, attained by the \(2^{10}\) transversals choosing exactly one vertex from each of ten pairs; these are also the only inclusion-minimal equalizers. The labeled token-jump graph on these transversals is the ten-cube since a valid single replacement flips one pair choice. None is a token slide, as antipodal vertices are at distance five. These are consequences of the same reduction, not additional originality claims.

**Group and exact orbit calculation.** With black for selected vertices and white for the rest, a transversal is a self-dual coloring, meaning that opposite vertices have different colors. This bijection is equivariant. The regular dodecahedron's 120 geometric symmetries act faithfully by graph automorphisms. To certify exhaustiveness independently, fix the oriented two-edge path \((o_9,o_0,o_1)\). Its ordered triples of distances distinguish all 20 vertices, as checked from the defining graph. Each automorphism must take this path to one of the \(20\cdot3\cdot2=120\) oriented two-edge paths and is uniquely determined by these three distance coordinates. Construct each candidate by matching signatures, and keep it precisely when it is a permutation preserving the adjacency lists. All 120 candidates pass.

Enumerate all transversals as the ten-bit endpoint choices. For each not-yet-marked choice, form its image under every one of the 120 permutations, discard duplicate images (they arise from its stabilizer), record the cardinality and mark all these images. Every set is visited exactly once in this disjoint orbit census. The resulting frequencies at sizes \(12,20,40,60,120\) are \(2,4,2,10,2\), respectively. They account for \(2\cdot12+4\cdot20+2\cdot40+10\cdot60+2\cdot120=1024\) labeled choices. Orbit–stabilizer gives the orders in the table.

## Verification

The included `verify_symmetry.py` computes all path signatures from breadth-first distances, checks every candidate against adjacency, and explicitly partitions the 1024 transversals under the resulting permutations. It then gives the five orbit-size frequencies in the Finding. `verify_direct.cpp` verifies the distance context by computing every witness locus and testing the definition on all \(2^{20}\) vertex subsets. Commands and expected results are in `VERIFICATION.md`. These are exact computations for the specified graph, not extrapolations to other graphs.

## Relationship to prior work and limitations

Palmer and Robinson [1, Introduction and Tables 4–5] count the same 20 orbits as self-dual dodecahedral 2-colorings under rotations and reflections. Their tables give total counts and element cycle structures. Those totals and single-element data do not specify the distribution of sizes of configuration orbits, which involves simultaneous stabilizers. The table above distinguishes actual orbit and stabilizer sizes rather than claiming the already known total as a new enumeration. Likewise, the full metric witness-locus calculation of [2] implies the antipodal hitting criterion and thereby the polynomial and the reconfiguration observations. Gonzalez, Hernando and Mora [3] introduce the general distance-equalizer problem. The present refinement is confined to this finite graph, and historical priority of the size profile is not established by the available comparisons.

## References

1. E. M. Palmer and R. W. Robinson, *Enumeration of self-dual configurations*, Pacific Journal of Mathematics 110(1), 1984, pp. 203–221, https://msp.org/pjm/1984/110-1/pjm-v110-n1-p20-s.pdf .
2. *Antipodal pair criterion and complete resolving polynomial of the dodecahedral graph*, Resultary, 2026-10-12, especially proof steps 1–2, https://github.com/Resultary/2026/tree/main/2026/10/12/SCOPE-antipodal-pair-criterion-and-complete-resolving-polynomial-of-th--3c3e39e438c1 .
3. A. González, C. Hernando and M. Mora, *The Equidistant Dimension of Graphs*, https://arxiv.org/abs/2107.10805 , Bulletin of the Malaysian Mathematical Sciences Society (2022), https://doi.org/10.1007/s40840-022-01295-z .
