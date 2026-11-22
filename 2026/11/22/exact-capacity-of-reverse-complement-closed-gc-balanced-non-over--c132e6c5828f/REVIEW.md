# Scientific review

## Correctness — PASS

The involution on GC-balanced six-mers has no fixed points, because every reverse-complement-fixed word has an even number of C/G bases. All admissible two-word orbits and all cross-prefix/suffix constraints are constructed from definitions. The exact compatibility graph has 248 vertices and 9048 edges. The included branch-and-bound checks the complete finite candidate space using rigorous greedy-coloring bounds; a 22-clique and the absence of a 23-clique establish optimality. The 44-word independent witness passes all closure, balance and non-overlap checks.

## Originality — PASS (qualified)

The most pertinent full-text prior work is Stanovnik–Moškon–Mraz (arXiv:2410.18458), which gives balanced non-overlapping code sizes but does not impose Watson–Crick reverse-complement closure. Its exact four-letter balanced six-mer maximum of 192 is not the present 44. The unrestricted non-overlapping code work arXiv:2307.12593 and Frith–Noé–Kucherov (2020) likewise concern larger feasible families. Existing short-strand reverse-complement-closed results address different block lengths and sometimes different GC conditions, and do not imply this six-mer optimum. A pre-existing unindexed treatment could still exist.

## Value — PASS

The three constraints are jointly motivated by self-synchronizing DNA addresses: constant GC composition, reverse-complement strand symmetry, and avoidance of every proper prefix/suffix clash. Their interaction is not captured by the individual constraints; the optimum 44 quantifies a sharp finite-length penalty relative to the known unrestricted balanced maximum 192. This supplies a reproducible short-block benchmark, not a claim about physical primer performance or longer-block asymptotics.

## Boundaries and prior comparison

The checker constitutes an exhaustive finite proof, not an informal sample. The result is restricted to exactly six symbols, three GC bases, and the standard Watson–Crick involution. Published results on five-mers or four-mers do not determine the six-mer graph optimum. No independent mathematical audit or experimental validation has been carried out.

Self-review: passed. Independent audit: not yet performed.
