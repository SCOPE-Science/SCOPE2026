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

BMV's published classification gives exactly 540 rational Weierstrass points and identifies the nonrational ones at q=11 with P-order 2. In Lemma 3.11 this means B³ has order 3, equivalently B has order 9. The six B's have degree three over k=F₁₂₁ (121≡4 mod 9), and z=a⁴ is the invertible Möbius transform (ω−Bω²)/(ω²−Bω), also of degree three. To check the two necessary lifts independently, set K=F₁₁⁶. Over k the three conjugates of B are the roots of X³−B³, and ω∈k. Taking their product in the Möbius transform gives Norm(z)=(1−B³)/(1−B³)=1. Since z+1=(B−1)/(ω²−Bω), Norm(z+1)=−1, hence Norm(−z(z+1))=1. The norm-one group is the subgroup of (121−1)st powers in K×, contained in both the fourth and twelfth powers since 12 divides 120. The denominators and z,z+1 are nonzero by primitivity of B. K contains all fourth and twelfth roots of unity, so every one of the 48 distinct smooth affine lifts per B belongs to K. They cannot descend further as B is recovered from z. This gives 288 points in 96 cycles, plus the 540 known fixed points. The reduced zeta function follows from the product over closed points, and the extension-field cardinalities follow by cycle lengths. Separately, the independent SymPy computation python3 /workspace/branches/record3_norm_check.py checks all six finite-field norms and periods and recovers both frozen polynomial representatives and their v values. The supplied checker was inspected, not run; no point census is used to replace the prior exhaustiveness theorem.

## originality

PASS

The geometric classification and counts, and the degree-three orbit of the auxiliary ratio, are already known or immediate from BMV. The supported distinct conclusion is that every coordinate lift of that ratio is defined over the cubic extension; the reduced-support Frobenius cycle type and zeta function then follow. The prior ratio degree does not by itself imply a degree for the lifted point.

## value

PASS

This is the first parameter of the studied maximal-curve family with nonrational Weierstrass points. The least extension supporting all exceptional marked points and the exact factorization of their reduced zeta function are natural arithmetic data not obtained from the geometric count or the curve's maximality. The finding does not claim Weierstrass multiplicities or a classification for other parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
