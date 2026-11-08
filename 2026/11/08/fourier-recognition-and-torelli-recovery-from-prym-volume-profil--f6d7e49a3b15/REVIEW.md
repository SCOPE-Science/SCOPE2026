# Review: Fourier recognition and Torelli recovery from Prym-volume profiles of banana curves

## Correctness — PASS

The proof derives the precise squared-volume normalization from Len–Zakharov's Theorem 3.4. For the two-vertex \(n\)-parallel-edge graph, every admissible odd genus-one decomposition leaves exactly two parallel edges and has rank one, so the contribution is the product of the other \(n-2\) edge lengths. Nontrivial monodromy around this cycle is equivalent to opposite edge signs. This gives an exact weighted-cut formula.

The cut-polarization identity then recovers every complementary edge product; counting exponents recovers the total product and each positive length. Fourier orthogonality gives necessity of the spectral conditions, and the four-index tetrads characterize positive rank-one weights and hence suffice. The \(n=3\) and \(n=2\) boundaries are treated explicitly. The standalone `VERIFY.py` file checks exact rational examples, Fourier and tetrad conditions and a nonrealizable positive profile. Finite checks support, but do not replace, the general proof.

## Originality — PASS, with historical-priority risk

The closest source, Len–Zakharov, *Kirchhoff's theorem for Prym varieties*, Theorem 3.4, gives the full **forward** volume formula for a single free cover and is acknowledged as a premise. It does not itself formulate recovery from the labeled family of volumes, nor characterize the joint realizable image through Walsh-band vanishing and positive tetrad equations. The inversion and semialgebraic realization statement compare differently quantified data: one prescribed metric graph yields many measurements, whereas the present theorem decides which measurement functions arise and reconstructs their unique graph.

Capobianco (2026) proves continuity and constructs integral Prym bases, without the inspected sections stating a multi-cover volume inverse. Zakharov (2025) treats higher tropical moments of individual covers and signed graphic matroids rather than joint scalar-volume recognition. Searches of published mathematical records and the accessible research claims did not find equivalent full image/recovery coverage; absence from searches is not a novelty proof. A more general unpublished or differently phrased cut-spectrum inverse could imply the result. The known forward formula makes this an accessible, not a deep, inverse theorem; this priority/subsumption risk is expressly retained.

## Value — PASS

The result solves a natural Torelli-style **inverse** problem in the simplest stable multi-edge strata of tropical curves using only scalar Prym volumes, rather than full principally polarized tori. It gives both a reconstruction algorithm from one- and two-edge monodromy cuts and a complete **recognition** theorem—linear Fourier constraints, positivity, and nonlinear tetrads—for all possible data. For genus three the realized profiles form a four-dimensional semialgebraic locus inside seven scalar measurements; a positive cut profile can fail the tetrad conditions and hence be geometrically unrealizable. The theorem thus supplies a concrete compatibility test for cover-indexed tropical period data, not simply another value of a known volume. Genus one is a sharp failure boundary.

## Limitations and closest literature

The profile is indexed by covering monodromy relative to the original labeled edge set; an unordered multiset of Prym volumes need not determine the same data. The zero at the trivial sign class is formal. Only free unramified double covers of positive-length banana graphs are included, and independent mathematical validation remains outstanding.

1. Len–Zakharov, *Kirchhoff's theorem for Prym varieties* (2020/2022), Theorem 3.4: the essential forward formula.
2. Capobianco, *Continuity of the tropical Prym–Torelli map* (arXiv:2608.21625v1; 2026): recent motivating literature.
3. Zakharov, *The trigonal construction and the second moment of the tropical Prym variety* (arXiv:2507.06401v1; 2025): higher-moment framework.

Self-review: passed. Independent audit: not yet performed.
