# Self-review

## Correctness — PASS

The exact statement is universal over even alphabet sizes and every nonnegative length, with a fixed-point-free complement and *only* forbidden five-factors of the form \(ab c\bar b\bar a\). The 49-state polynomial transition proof is finite and constructive, using the standard-library code in `VERIFY.py` to enumerate canonical complement patterns and check the critical operator identity over \(\mathbb Z[q]\). A direct suffix-state dynamic program and exhaustive literal testing independently corroborate short instances. The proof does not infer an infinite claim from finite length tests. The DNA Perron rate is certified by strong connectivity and a self-loop in the finite 256-state graph.

## Originality — PASS (qualified)

The full arXiv treatment by Chu, Wang and Zhang studies global secondary-structure avoidance for arbitrary gaps, not the one-gap local language; Zhang and Wu use separation-at-least-\(k\) constraints and a different code-construction problem. The inspected local complement-duplication irreducible enumerator forbids length-four factors, not these length-five factors. Its cubic rational denominator does not encode the new fifth-order formula. published-finding corpus and primary-literature queries targeting one-letter loops, five-mer complement motifs, generalized palindromes and generating functions found no identified exact same statement. An unindexed implicit equivalence remains a genuine priority risk; a search miss is not novelty proof.

## Value — PASS

The first positive fixed loop gap supplies a natural exact finite-state benchmark beyond immediate stem adjacency: a single uniform theorem gives all word-length counts over every fixed-point-free even alphabet and the DNA counting capacity. Its relevance is structural constrained-language enumeration, not a claim that one-nucleotide loops form stable biological hairpins or that the global DNA coding problem has been solved.

## Limits

This is strictly local factor avoidance, no global secondary-structure control, no error correction, and no independent historical priority or expert proof validation. Nearby work on longer loops may be a better biological model.

Self-review: passed. Independent audit: not yet performed.
