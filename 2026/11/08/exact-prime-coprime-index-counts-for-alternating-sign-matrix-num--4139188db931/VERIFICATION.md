---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The factorial product and Legendre layers produce a nonnegative triangular function h_{p^a}(n mod p^a), with zero exactly at the two endpoint residue intervals. For 0≤n<p^r, all layers a>r vanish. The two allowed boundary components lift digitwise: p=3d+1 gives c_{r+1}=(2d+1)c_r; p=3d+2 gives c_{r+1}=(2d+1)c_r+2 from two distinct surviving endpoints; c_0=1. Solving yields b_p^r or b_p^r+2(b_p^r-1)/(b_p-1). Direct independent factorial-increment valuations checked (p,r)=(5,4),(7,3),(11,3),(13,3), finding 161,125,457,729. Every admissible mod-p^r residue contains its least nonnegative representative with zero valuation, proving exact p-adic cylinder covering number and box dimension log_p b_p; the density vanishes since b_p<p. The result does not assert Hausdorff dimension or p=2,3.

## originality

PASS

Frey–Sellers already prove the nonnegative periodic p-power valuation profile and a pointwise zero/nonzero characterization, not the new all-prime population law across every p^r in the full 9-page primary paper read. The two-endpoint correction for p≡5 and precise p-adic box-cover count are a distinct counting problem. A preexisting digit-automaton corollary could conceivably imply these formulas, and this possibility is retained as risk.

## value

PASS

The support of prime-coprime indices of the classical alternating-sign-matrix sequence is a natural number-theoretic set. Exact counts for *all prime-power cutoffs*, their congruence-dependent boundary correction and p-adic box dimension quantify sparsity not supplied by qualitative infinitude/pointwise divisibility. No full arbitrary cutoff or Hausdorff classification is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
