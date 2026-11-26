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

For odd m≥3 the consecutive turning points and endpoints bound exactly m full monotone laps with alternating values ±1. Refinement by inverse branches multiplies the lap count by m at every iteration: adjacent refined laps meet at genuine turns, including prior lap boundaries because the new outer map is strictly monotone near each endpoint on the appropriate one-sided interval. Lap growth gives log m. For d=1−|x|<k⁻², the identity d′=1−cos(kd) gives d′≤k²d²/2, so the endpoint bands are forward invariant, contracting doubly exponentially, with endpoint signs determined by the residue of m modulo four. The derivative k|sin(kd)| along the captured tail is at most k²d there, so logarithmic derivative averages tend to −∞, also when a derivative vanishes exactly. For x in the survivor, |f′(x)|²=k²(1−f(x)²)≥2−k⁻². Nullity can be verified directly: put a=1−k⁻², J=[−a,a], and restrict the m inverse branches g_i to J. They map into J by forward invariance of the bands, have contraction 1/√(2−k⁻²), and log|g_i′(y)|=−log k−(1/2)log(1−y²) is Lipschitz on J. Summing along compositions bounds the derivative distortion of every depth-n inverse branch, uniformly in n by a geometric series. The first-level survivor misses a fixed positive-length hole in J near an interior turn. Pulling that hole back inside every depth-n cylinder removes a uniformly positive fraction of its length, so survivor lengths decay geometrically. Thus almost all points enter a band, reflection equates the two fixed-endpoint basin masses in the first parity, and alternating capture gives the uniform two-cycle empirical measure in the second. The empirical limits on this full-measure set exclude any other physical measure.

## originality

PASS

The single-sine formula, entropy tool, and distortion method are prior work. The supported distinct result is their use with the exact odd resonance to classify the full-measure physical statistics simultaneously with unbounded entropy, explicit expansion of the survivor and an almost-sure derivative exponent of −∞. The compared primary model passage and distinct indexed inverse-level result do not give this joint classification. This is not a claim of priority for the general possibility of large entropy with simple physical statistics.

## value

PASS

For a published sine family used to study chaotic dynamics this supplies an exact diagnostic: the computably increasing topological entropy and the entirely atomic physical statistics give opposite pictures of this same natural parameter family. It identifies where the noncaptured dynamics must lie, with an explicit expansion floor, and makes the physical outcome determinate even down to the two half-measure basins versus a single full-measure two-cycle. Its value is that concrete classification and a caution against reading typical chaos from entropy, not a new general entropy theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
