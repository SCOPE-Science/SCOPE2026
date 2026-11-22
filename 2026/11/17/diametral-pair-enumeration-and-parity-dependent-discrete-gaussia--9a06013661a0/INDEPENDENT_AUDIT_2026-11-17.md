# Independent mathematical audit

## correctness

PASS

Every strong-total-cover indicator is a {0,1}^N vertex; Euclidean squared distance is Hamming distance and is at most N=n+binom(n,2), with equality exactly for complementary cover indicators. Both V(K_n) and E(K_n) are covers for n>=3, so diameter sqrt(N) is attained. Two-coloring all vertices and edges means each edge-triple (u,v,uv) and each vertex star {v}∪delta(v) must use both colors. Choosing a red original vertex set A of size a forces each internal-A edge blue and internal-B edge red; all a(n-a) cross edges are freely colored. Only the one singled-out edge-color assignment for each singleton part size a=1 or n-1 violates a vertex-star constraint, yielding M_{n,a}=binom(n,a)2^{a(n-a)}-n(1_{a=1}+1_{a=n-1}). Dividing all ordered covers by 2 gives H_n. At a=floor(n/2)+j, weights factor as a central binomial coefficient times 2^{-j^2} (even) or 2^{-j(j-1)} (odd), with binomial ratios 1-O(j^2/n); summable Gaussian tails and negligible singleton corrections imply O(1/n) total-variation error and theta asymptotics. Independent direct exhaustive enumeration for n=3,4,5 exactly reproduced ordered distributions (1,9,9,1), (1,28,96,28,1), (1,75,640,640,75,1) and unordered 10,77,716. Finite checks are not the proof of all n.

## originality

PASS

The source Aprile–Ferrarini defines strong-total-cover polytopes and the incidence-graph domination equivalence, and studies full dimension, facet systems, complexity and triangular cacti. Its complete accessible text does not derive ambient Euclidean diametral pairs, a complete complementary-cover enumerator or parity-dependent theta total-variation law. Resultary searches and exact complementary-domatic formulations did not identify a stronger all-n theorem. Full prior coverage not ruled out under differently indexed domatic polynomial terminology.

## value

PASS

The trivial binary-diameter upper bound is not the novelty. The exact enumeration of ALL Euclidean extremal vertex pairs for a newly natural covering polytope, including a nontrivial singleton constraint correction, and the parity-dependent discrete Gaussian composition law are motivated, useful exact geometric and probabilistic invariants; they extend the initial structural polytope results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
