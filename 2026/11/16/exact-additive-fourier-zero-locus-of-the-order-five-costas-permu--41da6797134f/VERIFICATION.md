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

The Costas definition checks ordinary integer differences for all d=1..4; enumerating all 120 permutations yields exactly 40. The multiplier W_C(k) is a degree-4 integer polynomial at a primitive fifth root; minimal cyclotomic polynomial Φ5 implies zero iff all five residue counts equal 8. k→k+c*1 and k→a*k (a nonzero F5) act on zeros; all nonconstant frequency orbits have size20 and exactly 156 canonical representatives (plus one constant). Complete exact integer residue tables for all 157 canonical representatives identify 16 vanishing classes (12 also vanishing for all permutations, 4 additional), and every other class is nonvanishing. This is exhaustive finite proof, not sampled evidence or floating-point testing. An independent enumeration across all 3125 frequencies reproduced Costas count 40, 320 zeros, rank2805, all-permutation rank625, 240/80 overlap and weight distribution 4,4,92,108,112.

## originality

PASS

Earlier Costas-array construction, parity, correlation and nonlinear phase literature concerns individual arrays or their enumeration, not the sum of characters over the full forty-element ensemble in (F5)^5. The closest indexed order-five binary Fourier permutation-matrix result is over 25 binary coordinates, not the additive five-coordinate quinary operator. Exact finite tables could nevertheless have been computed elsewhere; novelty is best-of-knowledge with this risk.

## value

PASS

All order-five Costas arrays form a classical canonical finite signal-design family; a complete additive ensemble Fourier zero locus determines which translation-convolution modes are visible. The exact contrast against all permutations (rank 2805 vs 625) and the 16 symmetry orbits are mathematically interpretable and nontrivial despite finite order.

The dated certificate retains the supplied scientific assessment, sources and limitations.
