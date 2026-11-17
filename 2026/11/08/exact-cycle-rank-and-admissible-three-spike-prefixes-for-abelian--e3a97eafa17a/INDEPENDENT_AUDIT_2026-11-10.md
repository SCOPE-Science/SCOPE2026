# Independent mathematical audit

## correctness

PASS

PASS: The sum-c edges match all L_i with R_{c−i}; contracting that matching preserves cyclomatic number and yields simple two-distance interval graph H_c(s,t) with s=c−b, t=c−a. Its edges are distances s and t; on Z/(s+t) the translation by s decomposes into g=gcd(s,t) cycles, each with at least three vertices because s<t. Deleting the last g labels (one from each residue class) leaves g paths, so H_{s+t−g−1} is a forest; beyond this cutoff each new vertex remains in its existing residue component, and counting edges 2(N+1)−s−t gives β1=max(0,N+1−s−t+g). Substitution N=c yields the formula and exact strict forest inequality. For any acyclic triple, each added sum d>2c contributes a matching with at most one endpoint in previous nonisolated core; iterating a superlacunary sequence preserves acyclicity. Zeng–Xue–Zeng forest-support theorem then establishes the characteristic-word statement without arbitrary symbol relabeling. Independent original-bipartite-graph union-find verified 12,000 triples, including boundary and gcd cases; analytic graph argument proves all triples.

## originality

PASS

PASS, with Fine–Wilf priority reservation: Zeng–Xue–Zeng (Sep23 2026, v5 Nov6) proves the general forest-support characterization of Abelian pattern Sturmian words, and its superlacunary construction, but not an explicit first-three sparse support feasibility inequality or full β1 formula. Rankin/Fine–Wilf characterize the connectivity threshold of two-distance period graphs, and edge/component counting makes the cycle rank approachable, so the ingredients are credited; however the exact matching-contraction transfer to additive three-sum graphs and sharp prefix feasibility condition are not stated by the inspected sources. This is a best-of-knowledge narrow structural classification, not a claim that the general forest characterization is new.

## value

PASS

PASS: The set of admissible first-three designated sparse support positions is a natural local obstruction in an established infinite symbolic-word construction. A sharp all-triples gcd/interval boundary and complete cycle rank determine which finite prefixes can be extended at all; the result is an exact natural complete three-point classification. Although elementary after the correct contraction, it resolves a motivated feasibility problem and records the full defect β1; no artificial parameter slicing or paper-sized expansion is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
