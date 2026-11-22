# Self-review

## Correctness — PASS

The 14 binary rotation classes partition 64 labeled six-mer vertices and each is a directed cycle, forcing at least 14 deletions. An explicit 14-vertex acyclic witness establishes sharpness. Every size-14 solution chooses exactly one per class, so the exact 181,398,528-choice domain is exhaustive. Pruning a branch only when its already-finalized survivor subgraph has a directed cycle is sound by monotonicity under adding vertices. C++ Kahn topological/longest-path computation and separately authored Python DFS cycle/longest-path computation (with different necklace order) both returned each of the 14 matching frequencies totaling 68,288; the latter explicitly verified the action and orbit counts. Finite full-domain proof, not extrapolation. The optimal mask example and two exceptional symmetry masks are replayable.

## Originality — PASS (qualified)

published-finding corpus queries for exact k=6 MDS longest-path multiplicities, 408 minima and 103 symmetry classes found no identical indexed statement. The directly relevant 2023 arXiv and 2024 journal full-text sections state the old total 68,288, known sharp endpoints 13 and 26 and component extrema, but not the complete per-set 14-bin distribution or sharp-minimizer orbit census. Their source code is algorithmic, not a published bin table. All local prior claims were checked for overlap. An unindexed supplemental census remains a specific priority risk.

## Value — PASS

At the first binary order with 68,288 minimum-size selectors, optimizing worst-case uncovered k-mer windows is the motivating objective of the primary sketching literature. The exact entire guarantee distribution establishes how rare sharp optimum 13 is (408/68,288), how many very poor designs exist (48 at 26), and a 103-class reversible symmetry enumeration suitable for benchmarking optimizer sampling/coverage. This is a natural complete classification of an exact performance invariant, not an arbitrary slice or an incremental tweak of the known min/max; it claims no clinical or genome-scale performance benefit.

## Closest literature and boundaries

Marçais, DeBlasio and Kingsford, arXiv:2311.03592, Tables 1/2 and Sections 4.3, 5.2–5.3, already provide the total \(68,288\) and range \(13\) to \(26\). Their journal version is DOI 10.1089/cmb.2024.0544. The new measured invariant is the entire per-length frequency table and the group-action classification of the \(408\) global optimizers. A public but unindexed supplementary table could affect historical priority. The proof is exhaustive at order six only; no all-orders theorem or independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
