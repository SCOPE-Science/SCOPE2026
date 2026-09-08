# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Certified linear Fano-free Turan maxima on 9-10 vertices via link-graph induction and Lagrangian replay
- **Round:** 2026-09-07-first-light-01
- **Lane:** 144
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Extremal Combinatorics
- **Method:** isomorphism-free hypergraph generation with link-graph induction and Lagrangian-bound replay

## Problem

Let H be a linear 3-uniform hypergraph (any two edges share at most one vertex) on n in {9,10} vertices containing no (not necessarily induced) copy of the Fano plane F (7 vertices, 7 edges). Determine the exact linear Turan numbers ex_lin(n,F) for n=9 and n=10, exhibit one certified max-edge extremal hypergraph per order by explicit edge list, and prove edge-optimality by a replayable certificate combining vertex-link-graph Turan induction with a Lagrangian upper-bound check, plus a per-order extremal census table separating the record from the runner-up and from Steiner-triple-system baselines.

## Attempted claim

For each n in {9,10}: ex_lin(n,F) equals an explicitly stated integer E_n achieved by a committed edge list H_n that is linear and Fano-free, and every linear 3-uniform Fano-free hypergraph on n vertices has at most E_n edges, certified by a committed vertex-link-graph induction log plus an independent Lagrangian-bound replay; including a per-order census table (number of extremal / near-extremal isomorphism types and degree sequences) and a stability fragment describing all hypergraphs attaining E_n or E_n-1.

## Research outcome

Exact linear Fano-free Turan numbers ex_lin(9,F)=12 and ex_lin(10,F)=13 with committed edge-list witnesses H9 (STS(9)=AG(2,3)) and H10 (13-triple max packing, degrees 4^9 3^1), proved optimal by the link-matching degree cap + Schoenheim saturation, Fano-freeness by exhaustive 7-set scan (max span 5), plus forced degree sequences, n=9 uniqueness (one extremal type), and >=2 non-isomorphic max packings on n=10 as computed evidence.

## Why this attempt failed

Failed axes: value.

value: Even taking correctness and literal novelty as given, the result as delivered is not independently worth finding later. The upper bound uses no Fano hypothesis: it is the classical Schoenheim pair-packing bound for ANY linear 3-graph, so the Fano restriction is inert (ex_lin = max linear). Witnesses are classical designs: H9 is STS(9)=AG(2,3) covering all 36 pairs; H10 is a standard 13-triple maximum packing (degrees 4^9 3^1). The only non-textbook step is the 36/120 seven-set scan showing max span 5 <6, a seconds-scale check with margin, equivalent to noting the pair-optimal packings happen to have no Fano (STS(7)) subsystem. Promised advances beyond this — vertex-link Turan induction, substantive Lagrangian replay, per-order stability census with extremal-type counts and E_n-1 classification — were not delivered: n=10 iso-type count left open/conjectural, E_n-1 classification left open, >=2-types claim unevidenced, Lagrangian section restates the integer cap. Downstream uses as benchmark for Lagrangian/flag-algebra bounds and Brown-Erdos-Sos/stability conjectures are inflated because the bound is trivial pair-counting with no Fano-specific theory. This is a textbook restatement (Schoenheim + standard packings) plus a tiny inert-property check and an unexplained enumeration fragment, exactly the class value is meant to reject even if correct and new.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Full isomorphism-type census on n=10 and E_n-1 near-extremal classification are not closed; the >=2-types count on n=10 is sampled computed evidence with exact pairwise isomorphism tests, not a complete enumeration. n=9 uniquenessUpToIso cites the classical uniqueness of STS(9) after the machine-checked forcing to pairwise-balanced. Fano-freeness certificate is the exhaustive 7-set span check (36/120 sets), not a structural lemma.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
