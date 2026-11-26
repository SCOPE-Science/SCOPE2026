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

The frozen theorem's consecutive-triple characterization fails literally at n=3: (1,1) satisfies it vacuously but gives 50 types, not the minimum 49 given by (1,2). The complete repaired Finding makes the six periodic prefixes the definition for every n>=3 and restricts the triple test to n>=4. The repaired proof checks the two-edge case explicitly. Free amalgamation and homogeneity identify nonalgebraic types with admissible one-point patterns: triangles with the extra point can involve only consecutive old vertices, and free duplication gives infinitely many realizations. From v'_0=v'_c=S and v'_a=S-v_b, v'_b=S-v_a, the retained sorted deficits a<=b give the componentwise update (2S+a+b; S+a+b,2S+a,2S+b). The choice of the two smallest or largest retained deficits bounds all future states by monotone induction; the coefficient 2 of S makes a strict earlier loss persist. After one edge the smallest deficit belongs uniquely to that colour; repeating chooses it again. For minimizers the second colour differs from the first and the ranks after two edges are (second, first, unused). Selecting the largest deficit rotates the ranks from (1,2,3) to (3,1,2) and preserves strict distinctness and positivity of the colour components, forcing exactly the periodic continuations. The maximum recurrence follows from reducing the monochromatic transfer to a two-by-two matrix; the minimum product and characteristic polynomial reproduce the stated first values and Perron growth. The exact inequalities rho^(1/3)<7/2<(3+sqrt(17))/2 separate the rates. All corrected mathematical statements were reassessed.

## originality

PASS

The supported distinct claim is the finite-length comparison over all colour words and the exact equality classification, including the corrected short path. Neither the component counts for fixed words nor the numerical sequences are treated as new. The primary and catalog comparisons are bounded, not a proof of historical priority.

## value

PASS

For a natural sparse named base in a standard homogeneous class the repaired theorem determines the structural limits of extension complexity across all colourings and gives every equality case. The sharper contribution is the uniform sorted-state comparison and its rigidity, not enumerating two already-tabulated sequences. The opposite equality patterns lead to genuinely distinct exponential rates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
