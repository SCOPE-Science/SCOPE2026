---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For a flipper of degree two, both neighbors must supply the new bit in both phases; hence they flip in the opposite phase. This propagates along the interior of each arc up to both endpoints. If neither interior flips, a lone endpoint flipper would see three constant inputs and cannot flip back. With opposite endpoint phases, a stationary arc with one interior vertex can carry either bit; longer stationary arcs have exactly the words with run lengths at least two, protecting the two boundary sites in both phases. Their unsigned and alternating run counts use z²/(1−z−z²) and z²/(1−z+z²). When both arcs are stationary their two endpoint bit pairs must be complementary. One flipping arc must have odd edge length in the opposite-phase case and the other arc is unrestricted among admitted stationary words. When both arcs flip, the only phase assignments are the two alternating configurations at even n (both arcs odd, or both even with the chord neighbor not supporting the flip). These disjoint cases yield the stated normalization, since every primitive orbit has two phases. Binet's formula and |D|≤1 give bounds by positive multiples of φ^n uniformly for large n; if both arcs grow, the mixed terms divided by A_u A_v tend to zero, leaving (2/5)φ^(n−4). The parity cases also give existence at every legal chord and the usual bare-cycle count. Independent replay: python3 /workspace/reproductions/2.py directly applied bitwise synchronous majority on 64 reflection-distinct graphs for 4≤n≤18, 3,844,784 initial states, checking every population and both endpoint flips, including P(4,2)=6. Finite counts corroborate the all-length proof. Frozen verification statuses and recorded script reports are not independent certification.

## originality

FAIL

An earlier indexed and text-inspected result gives the same exact graph family, update, and all-distance census up to the factor of two from counting ordered phases instead of unordered temporal orbits. Its proof also includes the endpoint flip property. The uniform entropy and the bulk coefficient are direct consequences of the earlier Fibonacci formula, so the apparent additions cannot support an independent repaired claim.

## value

PASS

Considered as mathematics, an all-distance census with rigidity for a minimal graph perturbation answers a natural dynamics question: it distinguishes recurrence from convergence and detects the appearance of oscillations on every odd ring. The already available classification has this value. Once the overlapping classification is credited, change of counting convention and routine Binet asymptotics do not constitute a separately valuable repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
