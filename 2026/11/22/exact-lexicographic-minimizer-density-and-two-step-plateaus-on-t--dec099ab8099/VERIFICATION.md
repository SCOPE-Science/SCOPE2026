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

With fixed leftmost lexicographic ties the selected indices cannot move backward as the window slides, so a charge adds exactly one distinct index. The Parry chain is stationary and ergodic, and the bounded charge average converges in mean and almost surely. From a leading zero, an adjacent shifted k-mer cannot be smaller: the first adjacent disagreement, if any, is 01. From a leading one the shift is strictly smaller. Thus 00 prefixes charge, 100 does not, 010 charges exactly when K0=K2, and 101 charges exactly when K3<K1. After an initial 010, the first break in alternation replaces an expected 1 by 0, and makes the later lag-two k-mer strictly smaller if within the compared segments; otherwise they tie. This gives the alternating prefix and alternating suffix exceptions. After 00 and 1010 the numbers of completions to each endpoint are the first rows of A^(k+1) and A^(k-1), respectively, for A=[[1,1],[1,0]]. In the 010 case one alternating prefix can be completed with terminal 0, and also with terminal 1 iff k is odd; the one excluded completion in the 1010 case ends with 0 iff k is odd. This includes k=1, where 1010 itself is uncharged. The Parry probabilities telescope to the given endpoint weights because the squared norm of (phi,1) is phi+2; substituting the four counts and checking the Fibonacci identity at k=1,2 yields the closed density, plateaus and limit. The frozen enumeration script was read, not executed; no finite check is needed as a premise of this proof.

## originality

PASS

The evidence supports the fixed-lexicographic all-k endpoint counts and density as distinct from the inspected results. Charging is known. The closest indexed result with the same source family and width averages over orders, while the bound claim uses the single lexicographic order, which changes both the density and the periodic correction. The conclusion is bounded by the listed access risks.

## value

PASS

Exact expected sampling density is a natural performance measure for a constrained stationary source, not the fraction of uniform finite contexts. The all-length endpoint counts expose a specific alternating-run mechanism for exact two-step plateaus and give enough information to distinguish stationary and finite-uniform sampling. Generic charge and Parry formulas do not mechanically supply that count. The result is useful without claiming lexicographic optimality or applicability beyond width three.

The dated certificate retains the supplied scientific assessment, sources and limitations.
