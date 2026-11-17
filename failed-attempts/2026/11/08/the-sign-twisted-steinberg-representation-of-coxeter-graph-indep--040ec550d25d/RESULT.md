# The sign-twisted Steinberg representation of Coxeter-graph independence homology

## Finding
Let \(\mathbb F_2^3\setminus\{0\}\) denote the seven points of the Fano plane, indexed by integers 1 through 7 interpreted in binary. Let \(V\) be the 28 unordered triples \(\{a,b,c\}\) of nonzero vectors with \(a\oplus b\oplus c\ne0\), where \(\oplus\) denotes bitwise addition over \(\mathbb F_2\). Make two triples adjacent if and only if they are disjoint. The resulting graph \(\Gamma\) is the 28-vertex Coxeter graph. Let \(K=\operatorname{Ind}(\Gamma)\) be its ordinary independence complex. Set \(G=\operatorname{Aut}(\Gamma)\cong\operatorname{PGL}_2(\mathbb F_7)\), and let \(G_0\cong\operatorname{GL}_3(\mathbb F_2)\) be the index-two subgroup of Fano collineations. Let \(\varepsilon:G\to\{\pm1\}\) be the nontrivial quotient character of \(G/G_0\). Let \(\mathcal S\) be the set of eight Sylow-seven subgroups of \(G_0\), permuted by \(G\) through conjugation. Define the rational augmentation module \(T=\ker(\mathbb Q[\mathcal S]\xrightarrow{\mathrm{sum}}\mathbb Q)\).

**Theorem.** The full rational symmetry representation on the only nonzero reduced homology group is
\[
\boxed{\widetilde H_6(K;\mathbb Q)\cong \varepsilon\otimes T.}
\]
All other reduced rational homology vanishes. The seven-dimensional module \(T\) is the rational Steinberg module of \(\operatorname{PGL}_2(\mathbb F_7)\); both \(T\) and its twist \(\varepsilon\otimes T\) are absolutely irreducible. In particular, \(\widetilde H_6(K;\mathbb Q)^G=0\), despite the nonequivariant integral homotopy equivalence \(K\simeq\bigvee^7 S^6\).

The complete nine-class character is given here. The columns are element order, conjugacy-class size, quotient sign \(\varepsilon\), number of fixed members of \(\mathcal S\), and homology trace, respectively.

| Order | Class size | Quotient sign | Sylow fixed | Homology trace |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 1 | 1 | 8 | 7 |
| 2 | 21 | 1 | 0 | -1 |
| 2 | 28 | -1 | 2 | -1 |
| 3 | 56 | 1 | 2 | 1 |
| 4 | 42 | 1 | 0 | -1 |
| 6 | 56 | -1 | 2 | -1 |
| 7 | 48 | 1 | 1 | 0 |
| 8 | 42 | -1 | 0 | 1 |
| 8 | 42 | -1 | 0 | 1 |

The two order-eight conjugacy classes have identical character values but are distinct classes, verified by explicit conjugacy enumeration.

## Assumptions and scope
All graph vertices are lexicographically ordered non-collinear triples from the seven nonzero 3-bit vectors. The graph has 28 vertices, 42 edges, degree three, and 336 full automorphisms. Each finite independent set is a simplex; the empty simplex is included only in augmented-chain computations. All asserted representation isomorphisms are over \(\mathbb Q\). The theorem does not assert a particular integral representation lattice or an equivariant homotopy equivalence. The ordinary full Coxeter-graph automorphism group is intended, not a Coxeter reflection group, a Coxeter complex, or the distinct Tutte–Coxeter graph.

## Proof
**1. Integral homotopy premise independently reconstructed.** Enumerate all independent sets of \(\Gamma\) by a deletion-and-closed-neighborhood recursion on lexicographically increasing vertex indices. This yields exactly 196,009 subsets including the empty set. The counts by subset cardinalities 0 through 12 are
\[
(1,28,336,2268,9506,25788,45836,52928,38556,16660,3752,336,14).
\]
On the remaining augmented face poset, for each index \(v\) count all pairs \(\sigma\leftrightarrow\sigma\cup\{v\}\) in which both faces remain and \(v\notin\sigma\). Choose \(v\) maximizing (pair count, index), match **all** these pairs, delete them, and repeat until no pair remains. The construction matches 98,001 augmented pairs. Remove the single pair containing the empty face, retain its singleton as critical, and keep the other 98,000 pairs. Exactly one critical vertex and seven critical six-faces remain. Reverse matched Hasse arrows, orient all unmatched covering relations from smaller to larger face, and run a complete topological sort. The 196,008 nonempty faces and all 1,319,724 codimension-one incidences are processed with no directed cycle. This is a complete combinatorial acyclicity certificate. By Forman's discrete-Morse theorem the resulting CW complex has one zero-cell, seven six-cells and no other cells. The attaching maps into the one-point five-skeleton are null; thus \(K\simeq\bigvee^7 S^6\) integrally. This independently reconstructs the previously published nonequivariant result, which is *not* claimed as new.

**2. Exact symmetry group.** Every invertible linear transformation of \(\mathbb F_2^3\) permutes the Fano lines and hence the 28 non-lines, yielding 168 distinct graph automorphisms. The explicitly checked vertex permutation

```text
(0,1,4,5,2,3,7,6,12,14,15,13,8,11,9,10,16,24,25,20,19,26,27,23,17,18,21,22)
```

is an involutory graph automorphism not in the collineation subgroup. Its products with the 168 collineations form a verified group of 336 automorphisms. The full order 336 is also the classical known Coxeter-graph automorphism order; therefore this is the full group \(G\), and the Fano-collineation subgroup \(G_0\) has index two.

**3. Signed Lefschetz character.** Let \(g\in G\) and partition its 28-vertex permutation into cycles. A simplex is setwise fixed by \(g\) precisely if its vertex set is a union of cycles, each individually independent and pairwise nonadjacent. If \(c\) cycles are selected and their union has \(k\) vertices, the simplex has dimension \(k-1\), and its orientation sign is \((-1)^{k-c}\). Its alternating chain-trace contribution is therefore \((-1)^{c+1}\). Including the augmented empty face, the reduced Lefschetz number is minus the independence polynomial of the eligible-cycle adjacency graph evaluated at \(-1\):
\[
\operatorname{tr}(g\mid\widetilde H_6(K;\mathbb Q))
=-\sum_{J\text{ allowable vertex-cycle unions}}(-1)^{|J|}.
\]
The first standalone program enumerates every element of \(G\), applies this exact formula, and organizes the results into all nine conjugacy classes. The second program independently checks each class representative by enumerating every setwise fixed simplex and directly taking the sign of the induced vertex permutation; the nine results agree.

**4. Identification with a natural module.** The subgroup \(G_0\) has 48 elements of order seven, forming exactly eight distinct Sylow-seven subgroups. Their conjugation action by \(G\) yields a permutation character \(g\mapsto f(g)\), where \(f(g)\) is the number of fixed subgroups. The augmentation character of \(T\) is \(f(g)-1\). Exact enumeration verifies for **every** one of the 336 group elements that
\[
\operatorname{tr}(g\mid\widetilde H_6)=\varepsilon(g)(f(g)-1).
\]
Maschke semisimplicity and equality of rational characters establish the claimed module isomorphism. The action of \(G\) on the eight subgroups is doubly transitive: the exact sums \(\sum_g f(g)=336\) and \(\sum_g f(g)^2=672\) show one orbit on points and two on ordered pairs. Consequently the seven-dimensional augmentation is absolutely irreducible, as is its one-dimensional twist; equivalently, the homology character has inner product one with itself. Averaging the homology character gives zero fixed-vector dimension.

## Verification
Run `python3 verify_coxeter_st.py` using only Python's standard library. It reconstructs the graph and 336-element group, checks group closure, independently enumerates all simplices, verifies the full finite acyclic Morse certificate, computes Sylow conjugation and orbit-signed Lefschetz characters, and verifies all nine conjugacy classes. The output ends with `COXETER_SIGN_TWISTED_STEINBERG_PASS`. With the option `--write-classes` it writes `character_classes.json`. Then run `python3 check_coxeter_signed.py`, which reads that JSON file and independently enumerates the setwise fixed simplices of every class representative with explicit orientation inversion counts; it ends with `COXETER_NINE_CLASS_INDEPENDENT_SIGNED_LEFSCHETZ_PASS`. Recorded output files are included. The complete finite checks establish this exact graph-specific claim; there is no inference from a sample or a finite truncation of an infinite problem.

## Relationship to prior work
Barmak's 2010 star-cluster results include the general suspension theorem for triangle-free graphs (Theorem 3.4) and a precise wedge theorem for two-subset Kneser graphs (Theorem 4.11). Neither calculates the Coxeter graph's full symmetry module. Feng and Wang's 2024 Theorem 8 and Table 1 concern the *full* 35-vertex Kneser graph on three-subsets of a seven-element set; its Fano-plane cycles and homology do not determine the action on the proper induced 28-vertex non-line subcomplex. Dejter's Coxeter/Klein paper provides a geometric presentation and 336-automorphism description, but no independence-homology character. A published Coxeter-graph independence-complex calculation proves the nonequivariant \(\bigvee^7 S^6\) homotopy type; that is used as context and independently verified here, not asserted to be new. A separate published Heawood-graph **matching**-complex result already contains the untwisted Sylow-seven augmentation \(T\) as one constituent of its fourth homology. The present theorem identifies its *nontrivial quotient-sign twist* on the distinct Coxeter-graph independence complex; no inspected theorem provides a connecting equivariant isomorphism, and equality of a module dimension would not imply that result.

## Limitations
This is an exact rational group-module classification for one canonical 28-vertex graph. It is not an integral lattice classification, an equivariant CW-homotopy decomposition, a result about all Fano-derived complexes, or a general theorem for other finite fields. The absence of a matching indexed record is not proof of universal publication priority; unindexed equivalent literature and an undiscovered general representation-theoretic reduction remain possible. No independent mathematical audit of the new theorem is claimed.

## References
[1] I. J. Dejter, *From the Coxeter graph to the Klein graph*, arXiv:1002.1960v1 (first public 2010-02-09), especially the Coxeter-graph construction and automorphism order. https://arxiv.org/abs/1002.1960

[2] J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1 (first public 2010-07-02), Theorems 3.4 and 4.11. https://arxiv.org/abs/1007.0418

[3] Z. Feng and G. Wang, *Exploring Homological Properties of Independent Complexes of Kneser Graphs*, arXiv:2404.10566v1 (first public 2024-04-16), Theorem 8 and Table 1. https://arxiv.org/html/2404.10566v1

[4] *The Coxeter graph independence complex is \(\bigvee^7 S^6\)*, public mathematical record (2026-10-11), public research-record identifier `8a1bdfa47e09`.

[5] *Full \(\operatorname{Aut}(H)\)-module of the Heawood matching complex*, public mathematical record (2026-10-11), public research-record identifier `d7a042784870`.

[6] R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
