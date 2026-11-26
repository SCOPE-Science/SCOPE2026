---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

FAIL

The frozen Finding (RESULT.md line 16) says the fixed-letter frame-validity theory increases strictly with the leaf count; it decreases under inclusion, as the proof itself correctly says at line 48. With one letter, p→Box p is valid on F_0 and false at the F_1 root when p holds only there. All the operation counts, collapse and sharpness are otherwise supported: a leaf only observes its color, and a root observes its color a and the set S of leaf colors. A uniform root is identified with the leaf type of color a; a nonuniform root detects every color in S by Diamond(chi_c and Box chi_c) because the root cannot witness the test. Depth zero has q types; depth one observes the root color and any set of at most k off-colors, while depth two distinguishes every nonempty S of size at most k (counting the uniform singleton as the terminal type, not an extra type). Boolean combinations of the characteristic formulas give the stated powersets. The single-world case and the q=1 case collapse at depth zero; for q>=2 and k>=2, supports {b} and {a,b} at a root of color a give the same depth-one palette and different depth-two types. At every step t to t+1 below q a new nonuniform support of size t+1 refutes the negation of its characteristic formula; duplicating colors, or using uniform assignments for t=0, embeds the old types in the new. This proves strict theory decrease and both stabilization cutoffs. Replay: RESULT.md lines 24–48. The first-step counterexample was also checked over all Boolean assignments on F_0 and F_1; the uploaded verify.py and VERIFICATION.md were inspected, not executed.

## originality

FAIL

Earlier indexed height-two work provides the very same normal form, terminal collapse, depth-one quotient and sharp depth-two witness for a larger class containing all these stars. Its full proof gives the fixed-star counts and cutoff by direct restriction to realizable profiles. This is demonstrated stronger coverage even though the finite-k binomial sums are not printed there. The other cited comparisons are not the basis for the rejection.

## value

FAIL

The leaf-depth cutoff is a meaningful question, but the frozen result adds only the mechanical truncation of the already explicit height-two palettes and leaf supports. The same identified profile, characteristic formula and small sharpness witness are already available, and the extra leaf follows directly from the known profile sizes q−1 and q. Correcting the direction in the Finding would not create a surviving distinct contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
