---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For r≥3 a connected set missing the hub seeds at most one arm; even if it reaches the hub, at least two white arms cannot be entered. A connected set containing the hub must use arm prefixes and may omit at most one arm. Prefix forcing followed by the hub's one remaining force proves sufficiency. Counting the omitted long arm, the omitted short leaf with prefix length ℓ, and the full set of short leaves with prefix length ℓ gives z^r Q, including h=1. For real r>1, set F=(z−1)Q=z^h(z+r−1)−r. Its nonzero-it imaginary part is a nonzero multiple of t^(h+1) (h even), or of (r−1)t^h (h odd); and Q(0)=r. Monicity and coefficient continuity then give a locally constant right-half-plane count with multiplicity. Checked the frozen r→∞ expansion, including the +1/(hr) real correction for ±i. As a separate check, at r=1 the nontrivial (h+1)-st roots of unity are simple and implicit differentiation gives dz/dr=(ζ−1)/(h+1); any boundary roots ±i move left. The remaining positive-real-part roots occur in conjugate pairs indexed by integers 1≤k<(h+1)/4, giving exactly 2 floor(h/4) already near r=1. On z=−t the odd case has one increasing crossing beyond r−1. The even case has maximum h^h(r−1)^(h+1)/(h+1)^(h+1) on (0,r−1); its ratio to r is strictly increasing. Direct checks at h=2,4 and (r,t)=(3,3/2) for h≥6 recover the full table. The only possible nonzero multiple root of F is real at −h(r−1)/(h+1), which gives the double (r,h)=(4,2) case only. Q(1)>0 excludes the extra factor and positivity of coefficients excludes positive real roots. Reviewer-written `python /workspace/review_checks/5.py` corroborated coefficients for 20 small graphs and 120 exact negative-real counts including the double root. No numerical root computation is needed for the infinite result; frozen script inspected only.

## originality

PASS

Best-of-knowledge pass for the half-plane and negative-axis censuses, not for the enumerating polynomial. The directly matching published formula is credited. The comparison concerns counted complex zeros and multiplicities rather than coefficient inequalities or visual root locations.

## value

PASS

This gives a sharp instability family for an actual connected-forcing polynomial, with the number of unstable pairs depending on arm length even when the hub degree is unbounded. The unique double-root event and parity phases complete the nonzero real-root picture; these are structural results, not finite root plots or recomputation of known coefficients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
