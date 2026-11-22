# Scientific review: parity-filtered fence ideals

## Correctness

PASS. The finite-poset trace interval \([\downarrow B, P\setminus\uparrow(S\setminus B)]\) proves that a parity conflict can occur only at a unique ideal. Maximum antichains of the odd fence are classified using the consecutive-edge equality case for an incidence path. The edge-cover and independent-exterior-minima conditions characterize *all* rigid patterns, not only examples. They give both the one-unit VC loss and the exceptional \(1,3,3,1\) top-face count. The homology argument explicitly analyzes every exceptional small rank. `CHECK.py` exhaustively tested 328 size-maximal candidate antichain/parity pairs through \(m=8\), and small top boundary ranks.

## Originality

PASS with a historical-priority qualification. The closest primary fence literature treats rank polynomials, unimodality, interlacing, partial symmetry, and rowmotion rather than individual Boolean trace patterns. Other closely matched recorded work on parity-restricted ideals concerns *disjoint unions of chains*, not the connected odd fence. The new statement is the rigid-trace and topological classification, not the elementary fact that unrestricted ideals shatter antichains. Unindexed or differently named equivalent classifications remain possible; the scientific comparison does not claim absolute uniqueness.

## Value

PASS. Rank enumeration of a distributive lattice does not specify the VC-shattering complex of its parity halves. The theorem produces an exact all-rank maximum-face classification, a stable loss of exactly one VC dimension, and a transitory binomial-pattern difference between the odd and even parity classes. In particular, it identifies the precise top integral homology classes, including two exceptional ranks. These are natural invariants of parity-filtered ideal systems and furnish structural benchmarks for their learning-theoretic and topological analysis.

## Closest literature and limitations

The closest publications are E. Kantarcı Oğuz and M. Ravichandran, *Rank Polynomials of Fence Posets are Unimodal* (arXiv:2112.00518, first posted 2021-12-01), and S. Elizalde and B. Sagan, *Partial Rank Symmetry of Distributive Lattices for Fences* (arXiv:2201.03044, first posted 2022-01-09). Their stated theorems do not imply the parity-specific support classification; the full bibliographic space is not guaranteed exhausted. This theorem does not cover even-length fences, arbitrary segment lengths, lower-face coefficients, lower-degree homology, or online learning dimension. Finite computation is corroborative only.

Self-review: passed. Independent audit: not yet performed.
