---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The original statement that the relaxation first fails to be integral at m=5 is false as a claim about the polytope. In lexicographic source order at m=3, (0,1/3,1/3,1/3,1/3) is feasible. The output rows for 001011, 001101, 010011 and 010101, together with x_000111=0, are tight and have rank five. The relaxations at m=1 and m=2 are simplices because a common output bounds the sum of all coordinates. The corrected RESULT distinguishes the first fractional vertex (m=3) from the first strict gap in the all-ones objective (m=5). It also corrects the effect of deleting redundant non-Dyck output rows: a swap changes only one prefix height, and a non-Dyck output A10B has a uniquely located negative prefix with unique Dyck preimage A01B. Such a row gives only x_w<=1, already implied by the no-error row. Counting pairs A,B gives C_m non-Dyck outputs, not zero extra outputs. Rebuilt output incidences and evaluated all frozen rational certificates exactly: primal and dual values are 1,1,2,4,19/2, and integral witnesses attain the floors 1,1,2,4,9. Using the dual upper bound at m=5, an ordered recursion over mutually compatible sources exhausts all nine-word codes, matching the eleven full lists; reversal-complement fixes nine and exchanges the rest. The repaired proof matches both exact replays and does not alter the validated tables, certificate data or channel definition.

## originality

PASS

For the repaired claim, the inspected evidence supports a distinct finite Dyck swap-shadow objective gap and exact extremizer census, supplemented by the precise distinction between first fractional vertex and first objective gap. The standard coding reduction, simplex/active-row method and Catalan convolution are not novelty claims. The exact indexed result was the assigned record itself; the stronger plausible neighboring claims have different channels or source families, not merely different notation. Same-day publication dates establish no priority.

## value

PASS

A single local swap on properly nested binary strings is a natural constrained-channel problem. The separate earliest thresholds for polytope integrality and for this code-size objective demonstrate that an exact integer optimum can conceal nonintegral vertices. At the first objective gap, listing all extremizers and their reflection-complement symmetry gives a concrete small-block benchmark beyond producing one feasible code. This value survives correction of the false original integrality assertion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
