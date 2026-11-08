# Self-review

## Correctness — PASS

The full cyclic inverse-swap bijection and its junction clauses are proved from the synchronous Rule 184 local map. The Lucas vertex-cover upper bound holds for every alternating-run count, and a forced-vertex path count realizes the Fibonacci bound in every odd length. The exceptional odd seven-cell case and the one-, two-, and three-cell bijective cases are handled explicitly. The three attached Python scripts independently check the full forward map through 18 cells, the inverse-swap law exhaustively through 14 cells, and the matrix closed forms through 200 cells. These finite checks supplement, but do not replace, the all-length proof.

## Originality — PASS, historically qualified

The principal result is the global optimization of one-step full-ring predecessor multiplicity, including exact equality cases, not the known Rule 184 update, the general inverse-word enumeration method, or Fibonacci counts of an individually selected alternating target. Jen (1989) develops generic finite-block predecessor recurrences and optimizes one-step probabilities for selected other rules, not this fixed-coordinate cyclic maximum; Fukś (1997, 1999) proves formulas for particular finite blocks and traffic flow; Evans, Rajewsky and Speer (1998) treat a probabilistic open-boundary variant; Powley (2009) covers general pointwise periodic-target preimage counts by transfer matrices. The inspected portions do not state the optimized Fibonacci–Lucas theorem or unique maximizing configurations. General transfer matrices could in principle be used to derive it, but do not themselves establish the required global comparison. Full historical priority remains subject to external checking, particularly for specialized traffic-model enumeration tables.

## Value — PASS

Worst-case one-step inverse branching measures the maximum ambiguity of time-reversing a deterministic, particle-conserving traffic system. The natural all-ring-length invariant and **all** attaining targets are determined. The sharp difference between even alternating and odd once-defective alternating targets is a structural boundary not supplied by a single example or a generic preimage algorithm. This is a complete exact extremal classification, rather than an arbitrary finite-instance census.

## Scientific limits and related work

The result assumes indexed cyclic binary words and one synchronous update. It does not cover noisy, asynchronous, open-boundary or multistep inverse reconstruction. The classical vertex-cover mechanism and generalized transfer-matrix pointwise methods are acknowledged rather than claimed as independent new machinery. References and exact source comparisons appear in `RESULT.md` and `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
