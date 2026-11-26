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

PASS

The mathematical statement is true for each prime p and nonzero signed integer n=a p^e, with p∤a. For positive valuation m, D_p(b p^m)=b m p^(m−1), and the new valuation is m−1+ν_p(m). At valuation zero the next iterate is zero, and zero is fixed by definition. For valuations strictly between 0 and p or strictly between p and 2p, each step lowers the valuation by one and multiplies the unit by the current valuation. This gives the factorial iterates and exact landing times. At valuation p the multiplier is one, giving precisely the stated nonzero fixed points. The region m≥2p is forward invariant: for m>2p the next valuation is at least m−1, and for m=2p it stays at 2p for odd p or rises to 5 for p=2. Its magnitude therefore at least doubles each step, excluding any additional periodic integer orbit. A separate bounded exact check used primes 2,3,5,11,29,97, both signs, both finite bands and 16 iterates across the divergence boundary; the recorded larger regression was inspected, not rerun. The raw frozen RESULT.md has actual broken TeX escapes (e.g. byte 0x0C in frac and split valuation symbols); the intended mathematics is unambiguous from the remaining proof, verification text and tested formulas. This display defect was not treated as mathematical falsity, and the frozen file was not altered.

## originality

FAIL

The central classification is mechanically covered by Emmons–Xiao's more general explicit integer-iteration description and trichotomy, even though the complete phase diagram and uniform inequality are not boxed there. The earlier Lemma 4 proof explicitly gives the last nonzero iterate and the exact extinction step. More decisively, Theorem 8's proof already gives the integer iterates up to the first valuation divisible by p as a falling product, together with all subsequent valuation blocks. Reading those two parts under the proposed initial bands yields the middle-band formula and the high-band growth bound directly, without a new dynamical lemma. The 2024 extension also explicitly states the low-valuation extinction cutoff.

## value

FAIL

As exposition, the three numerical bands and the uniform inequality are convenient. As a distinct finding, the exact middle landing is the e mod p transient already computed in the earlier proof, and the uniform growth estimate is multiplication of the defining magnitude ratios along the earlier nondecreasing block minima. No independently substantive remainder is established by the asserted phase diagram. Correcting attribution and TeX alone would not repair that scientific limitation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
