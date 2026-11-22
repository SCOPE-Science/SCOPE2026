# Scientific review — Transversal-matroid structure of minimum paired domination

## Correctness — PASS

The proof directly establishes minimum size four (no dominating adjacent pair), classifies all optimal four-sets by 13 class-occupancy patterns, and matches these patterns exactly to a four-role transversal presentation. The standard matroid basis-exchange theorem then proves isometric shortest exchange paths; explicit complementary constructions prove the diameter. All parameters are arbitrary positive integers. The Python program compared 50,832 four-subsets over 64 parameter pairs; an independently coded C++17 verifier compared 94,941 four-subsets over 81 parameter pairs and checked full basis exchange at one nontrivial parameter pair. These are checks, not the infinite proof.

## Originality — PASS, subject to prior-art risk

Henning–McCoy–Southey (2014) identify the graph family as an edge-extremal equality case for paired domination four but the inspected extremal theorem does not imply the classification of all optimizer configurations. Classical transversal-matroid literature supplies the abstract matching theorem, not the new class-to-role presentation. Searches for the exact family, alternate matroid language, stronger implications and mathematical-result records did not identify a covering theorem. Particularly close published records concern triangular graphs under paired domination and cyclic clique blowups under super domination, so their actual statements do not cover the present invariant/object combination. The original publisher's full PDF could not be read and remains a genuine priority risk, not an asserted exclusion.

## Value — PASS

The 2014 edge-extremal family is mathematically motivated. An exact transversal presentation reveals graph-independent optimization structure: greedy weighted selection, optimal reconfiguration geodesics, the sharp all-parameter diameter and the exact placement polynomial. The property is nontrivial since \(C_7\) has minimum paired-dominating sets failing matroid basis exchange. The result is not merely a scalar recomputation or an arbitrary small census.

## Closest work and limitations

Relevant sources include Henning, McCoy and Southey (2014), doi:10.1016/j.dam.2014.01.019; Haynes and Slater (1998), the original paired-domination invariant; Brualdi and Dinolt (1972) for transversal-matroid theory; and the SageMath transversal-matroid documentation. The main source's available rendered sections were inspected for the graph construction and scalar theorem, but the complete publisher PDF was inaccessible. Unindexed equivalent prior work remains possible. The theorem is limited to five-cycle blowups with three singleton classes and to ordinary paired domination.

Self-review: passed. Independent audit: not yet performed.
