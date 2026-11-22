---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

At frozen tree 7ab29eac reconstructed 4-by-4 ASM alternating row/column partial-sum definition and binary NONZERO support convention (minus-one entries are also support ones). A 4x4 row must be one of eight alternating rows; 8^4=4096 candidate matrices, exact column check yields 42 unique supports. Mod-2 odd row/column parities impose seven independent affine equations, leaving nine free bits; every reduced character has 128 ambient representatives with equal Walsh magnitudes. A separate exact-integer reduced enumeration and independent Walsh butterfly over 512 frequencies matched the supplied 13-level histogram, including 120 zeros; hence ambient nullity 15,360 and rank 50,176. The independent projection-support inverse transform has total absolute numerator 3,184, yielding 199/32. Package check_asm4.py directly recomputes all 65,536 ambient characters and compares frequency_spectrum.csv (512 rows) and support_masks.csv (42 rows) against exact enumeration; inspected source and certificate shape. Fourier translation averaging proves no arbitrary real/complex projection onto the range has lower endpoint norm. No higher ASM order inferred.

## originality

PASS

Classical ASM count 42, refined boundary/bulk partition functions, and ASM symmetry-class formulas do not state the 16-bit nonzero-support sign-character table nor its 9-dimensional affine reduction and sharp 199/32 projection norm. The representation differs from ternary signed ASM embeddings in nearby published records.

## value

PASS

The alternating-sign matrices of order four are the natural first reasonably rich small even ASM family, and their binary nonzero-support code is canonical under the parity constraints. Its complete first nontrivial support spectrum determines invertibility failure, exact rank and the best endpoint-stable Fourier recovery projection. The nontrivial 9-variable quotient, explicit 120 reduced zeros and exact 199/32 are independently useful concrete invariants, not merely a re-count of 42 matrices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
