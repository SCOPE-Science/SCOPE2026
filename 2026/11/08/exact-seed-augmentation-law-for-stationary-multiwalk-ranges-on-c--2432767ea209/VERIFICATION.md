---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and limits

## Exact finite-state replay

Run `python check.py` using a standard Python 3 installation. The verifier performs 5,560 exact comparisons using `fractions.Fraction`. For every \(n\in\{2,3,4,5\}\), \(q\in\{0,1/3,1/2,1\}\), \(k\in\{1,2,3\}\), and \(T\in\{0,1,2,3,4\}\), it independently computes uniform-root random-walk range distributions by finite-state transitions on (visited mask, current vertex), convolves the laws for every weak composition of \(T\) into \(k\) lifespans, and compares them with both the one-walk-plus-seeds distribution and the exact subset probability formula. It additionally compares every uncovered factorial moment. The observed output was `PASS 5560 exact rational comparisons`.

## Analytic justification

The uniform-state avoidance factor \(\alpha_b=1-(1-q)b/(n-1)\) is a one-step conditional probability whenever the walker remains outside a forbidden set of size \(b<n\). Multiplying this factor along \(T\) steps proves all forbidden-set survival probabilities exactly. Inclusion-exclusion identifies the full distribution and is valid on the entire finite Boolean lattice, while an explicit augmented-range construction supplies stochastic coupling. The proof is not limited to the checked finite cases.

## Scope boundaries

The exact state identity requires uniform independent starts, common \(q\), and the complete graph with the stated self-loop convention. The example on the three-vertex path shows that complete-graph allocation invariance does not extend automatically to arbitrary graphs. No claim is made about process-level coupling, arbitrary graphs, or independent external validation.
