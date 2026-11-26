---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Contracting the c-antidiagonal matching gives the interval [0,c] with exactly the edges of lengths d=c-b and e=c-a. The contracted graph has the same cycle rank. Put N=c+1 and g=gcd(d,e)=gcd(b-a,d). At the Fine–Wilf threshold N0=d+e-g each residue modulo g is connected, and there are N0-g edges, so the threshold graph is a forest. Shorter intervals induce subgraphs of it; longer intervals have g components and (N-d)+(N-e) edges. This proves the rank max(0,N-d-e+g)=max(0,a+1-d+g) and the strict forest boundary a<d-g. In particular this includes the equality boundary, d=1, and g=d. Cycles persist under extension. Appending t=2m+1 after maximum sum m adds a matching all of whose edges have a fresh degree-one endpoint, hence preserves forestness. Every cycle is finite. Theorem E applies with the sparse symbol relabeled 1, using exactly the same zero-based incidence graph. An independent bounded DSU check also matched all 4,495 triples through c=30: initialize 2(c+1) vertices, union i with c+1+t-i for t=a,b,c and 0<=i<=t, and compare the number of unsuccessful unions with the formula. The frozen checker and output were inspected, not executed.

## originality

FAIL

The claimed quantitative formula is a direct specialization of the classical two-period Fine–Wilf theorem, not merely analogous to it: one matching contraction makes the graphs identical, and Euler's formula at and above the exact threshold gives the stated rank, with shorter intervals induced below it. The existence equivalence then follows from Theorem E and the maximal-edge argument in Proposition 7.14, applied only to cycles using at least one newly appended sum. The explicit support-prefix wording is useful but does not add a separate mathematical result not mechanically implied by this combination. The exact November match is noted separately and is not the basis of the earlier-coverage finding.

## value

FAIL

The prefix question and exact cycle rank are natural and the formula is convenient, but the submitted contribution is a repackaging of the immediate two-period threshold and cycle count, combined with the earlier forest characterization and its doubling proof. It supplies no distinct previously undetermined invariant or obstruction beyond that deduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
