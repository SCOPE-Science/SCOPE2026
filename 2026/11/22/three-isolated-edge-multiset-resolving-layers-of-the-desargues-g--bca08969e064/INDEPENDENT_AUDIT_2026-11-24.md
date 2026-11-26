# Independent mathematical audit

## correctness

PASS

The graph is the explicitly defined 20-vertex middle-level inclusion graph, not the full 5-cube. Its graph distances equal Hamming distances: between 2-sets replace each mismatched element via the temporary 3-set union; complement handles pairs of 3-sets. Between a 2-set and a 3-set, first go to a 2-subset of the latter containing their intersection and then add the last element; this realizes the Hamming lower bound. Minimum distance to an edge therefore deletes the unique coordinate flipped by that edge. Independent exact replay /workspace/desargues_independent_replay.py uses this distance calculation, 32 blocks of 32768 masks, and sorts the 30 packed histograms for each mask to detect equality. Run python3 /workspace/desargues_independent_replay.py followed by the full path to the frozen min_masks.txt. A pilot block preceded the full run; all 1048576 masks yielded just (8,720), (10,960), (12,720), and the size-eight certificate matched byte for byte. All edge shells had histogram (2,4,8,4,2), proving complement duality; the census then gives the exact dimension and failure on every single-vertex addition. Connectedness forces an automorphism to preserve or swap parts. Those preserving parts act faithfully on 2-sets, since each 3-set is determined by its 2-subset neighbors. Common-neighbor adjacency of 2-sets is the triangular graph. Every four-member pairwise intersecting family of 2-sets has a common point (a family without one lies in a triangle and has size at most three). Thus the five size-four stars determine the parts-preserving action, with each 2-set the intersection of two stars. Complement swaps the parts, giving exactly the 240 advertised symmetries. Independent orbit computation gave (representative, orbit size, induced edges) = (3534,240,4), (5582,240,5), (5933,240,6). The replay did not execute the uploaded C++ programs and does not generalize to larger graphs.

## originality

PASS

The distinction is the exact edge-multiset polynomial and orbit census for the Desargues graph. Prior same-graph ordered edge codes, the full-cube multiset result, and earlier small-distance obstructions are mathematically different. No covering statement was identified in the inspected literature or catalogue.

## value

PASS

The Desargues graph is a canonical highly symmetric cubic graph, and unordered edge identification is a standard invariant. A complete inventory exposes separated feasible cardinalities and universal failure under a single added landmark, in sharp contrast with ordinary ordered resolution. It also distinguishes three types of minimal-size witnesses up to full symmetry. This is an exact reusable benchmark for unordered edge identification, not an arbitrary experiment or a general-family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
