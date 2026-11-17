---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

The neighborhood conditions over F3 are b_i=-a_{i-1}-a_{i+1} and a_i=-b_{i-1}-b_{i+1}; eliminating b yields a_{i-2}+a_i+a_{i+2}=0. Every parity subsequence is then an arithmetic progression, with nonzero step forced by the required distinct horizontal neighbor colors. Hence a_{i+6}=a_i and x_{i+3}=row_swap(x_i), with exactly (3*2)^2=36 admissible four-entry initial choices and 6 row-symmetric period-three choices. Ordinary versus row-swapped cyclic closure gives prism/Mobius counts (0,0) if 3 does not divide n; (6,36) if n=3 mod 6; (36,6) if n=0 mod 6 for n>=3. Every cubic 3-balanced coloring is an ordered partition into three total dominating sets, so divide by 6 for unordered counts. Independent brute force of all 3^(2n) assignments for n=3..6 returned exactly those counts. The all-n proof is the field recurrence, not finite experiments.

## originality

PASS

The public full-text Minyard–Sepanski paper establishes existence of 3-balanced colorings on generalized Petersen/prism and Möbius families, but the inspected theorems classify existence, not all labelled colorings or the 36/6 periodic and twisted closure patterns. A complete six-periodic row-exchange census is a distinct stronger statement.

## value

PASS

This is a complete and exact classification of all 3-balanced colorings on two natural infinite cubic graph families and their total-domatic partitions, including a six-column rigidity/row-swap law and exact labelled counts. Such a full census is a mathematically motivated strengthening of known feasibility results; independent researchers can use the exact multiplicities and rigidity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
