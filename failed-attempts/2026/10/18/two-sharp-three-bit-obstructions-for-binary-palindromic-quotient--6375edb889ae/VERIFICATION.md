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

With N=A/B and L=ℓ(N), the length difference of A and B is L−1 or L. Normalize N into (p,p+1) for odd N of length ≥6, take the two leading-interval scales 4 and 8, and reverse the leading blocks to get the residue condition. The only short palindromic denominators 1 and 3 have padded leading blocks 100 and 110, whose reversals are their residues; their normalized values are valid lower endpoints. The ratio still lies strictly inside the claimed necessary product/quotient bounds. Independently checked all 16 cells in exact fractions with the equivalent product interval test and recovered the stated witnesses and exactly two empty cells (5,1),(7,3). For each length shell [4t,8t), t=2^k, earlier shells contribute t/4+O(1); the two residue classes add affine ramps of slope 1/8 on [5t,6t) and [7t,8t), up to bounded errors. Dividing by X gives an affine-over-linear ratio on each quarter. At X/t=4,5,6,7,8 the limiting values are 1/16,1/20,1/16,3/56,1/16, yielding both exact densities. Even numbers are disjoint from the two odd cylinders and unrepresentable, proving the 11/20 lower bound. Passing this test is not a statement of representability. Replay of finite classification: python3 /workspace/replay/finite_checks.py.

## originality

FAIL

The 2022 paper does not give the second cylinder or the 16-cell classification. But a distinct indexed width-k theorem uses exactly this interval-and-reversal predicate at k=3, with its exact enumeration and the 1/20 lower density already present. The remaining upper density and short-denominator detail are immediate from its boundary-count argument and checking B=1,3. Its 14-bit bound also strictly dominates 11/20. The broader record has a later displayed date: this is statement-level coverage, not a claim about priority or derivation of the frozen result.

## value

FAIL

Sharpness of the small necessary test is a natural question, and the density calculation is sound. In the presently available comparison, however, the exact width-three classification and density behavior follow mechanically from the broader interval predicate and shell formula, and the global inequality is strictly weaker. The short-denominator check is needed for exact statements but does not leave a distinct valuable invariant on its own.

The dated certificate retains the supplied scientific assessment, sources and limitations.
