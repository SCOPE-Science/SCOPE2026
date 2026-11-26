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

Final assessment applies to /workspace/repairs/2/RESULT.md, not the full original as written. Original RESULT.md line 38 is false under its unnormalized convention: it lists levels 2^8 through 2^16 in increments of two in the exponent, but at zero frequency the count alone is 4^12=2^24. The repaired levels are 2^16,2^18,2^20,2^22,2^24 with multiplicities 40,12,9,2,1; the ten fiber sizes and zero-target count 630784 survive. The repair also replaces the original's lift/truncation argument with a direct chain-ring computation. In diagonal-difference coordinates only five coordinates participate. Factor out the minimal frequency valuation a by passing to R/π^(ell-a) (a=ell handled separately). A unit h' gives two unit pivots; a unit s' or t' instead leaves a three-coordinate alternating complement with entry ideal (t',h') or (s',h'), respectively. The complement splits on an entry generating the ideal, without any division by 2, and has second exponent c=b-a. Counting the two free coordinates and q^(6a) lifts gives kernel size q^(2(ell+a+b)). Orthogonality contributes q^(6ell), and subtracting annihilator sums on successive ideals yields the stated inverse transform. Setting h=0 makes a+b=i+j and attains all levels; the unique trivial frequency is at 2ell, so the normalized radius is q^-2. Replayed the example independently by exactly multiplying triangular matrices over both order-four rings: take each bottom diagonal zero, enumerate 4^5 possibilities for each operand, and multiply each histogram contribution by 4^2 for the two omitted scalar diagonals. Compute the DFT of the resulting 64 targets using the usual fourth roots over Z/4 and the character (-1)^(epsilon coefficient) over the dual numbers. All 64 Fourier values in each ring agree with the repaired formula; independent shell summation from formula (1) gives the same ten-level histogram and total 16777216. The bounded replay checks the example, not the unbounded theorem, whose replay path is §§1–4 of the repair. The frozen checker and verification record were inspected, not executed; they do not state the false absolute exponents and need no replacement.

## originality

PASS

The repaired claim retains the exact non-field T3 chain-ring frequency profile, all target fibers and sharp walk radius. Its length-one fibers are known and its Fourier identities and pivoting methods are standard, not independently new. The corrected numerical example is corroboration, not the originality basis. The closest same-dimension exact precedent is field-only, and the closest chain-ring antecedents use different algebras or different output constraints.

## value

PASS

Counting all prescribed additive outputs on the standard triangular algebra yields a full ring-indexed invariant, not only a zero-bracket count. At fixed (q,ell) the distribution is the same across genuinely different rings, including mixed- and equal-characteristic examples; the positive Fourier structure also gives an exact mixing spectral parameter. These facts survive the repair independently of the example-exponent correction; correcting exponents alone would not supply scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
