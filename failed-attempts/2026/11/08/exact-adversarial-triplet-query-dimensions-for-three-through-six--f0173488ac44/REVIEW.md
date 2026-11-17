# Independent mathematical audit

## correctness

PASS

For binary rooted-triplet one-vs-rest incidence on all strictly binary nonplane labeled rooted trees, independent leaf insertion enumerated exactly 3,15,105,945 trees for n=3,4,5,6. The actual strategy JSON blob was independently replayed by reconstructing LCA responses for all trees and every branch, confirming depths 1,3,5,9; n=6 has 511 query nodes and 512 nonempty disjoint complete leaves. For n=5, all 30 possible first positive queries have 35 trees; the only viable 16/16 split has a 17-child with no next 8/8 split, excluding depth six. Cardinality 2^d<=|H| gives all other upper bounds. This is a complete finite certification, not a sample.

## originality

FAIL

FAIL. Published 2026-11-02 primary full RESULT.md states precisely the identical one-vs-rest binary rooted-triplet semantics and the complete Littlestone dimension vector (1,3,5,9) for n=3..6, plus six-taxon VCdim 4. This fully implies the submitted principal theorem. The earlier source also contains a 511-node depth-nine strategy and a five-taxon exact recursion; new certificate format does not restore originality.

## value

FAIL

FAIL as distinct contribution: a correct new implementation of an already published complete finite classification, without a further motivated unproved structural theorem or new invariant, does not provide novel scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
