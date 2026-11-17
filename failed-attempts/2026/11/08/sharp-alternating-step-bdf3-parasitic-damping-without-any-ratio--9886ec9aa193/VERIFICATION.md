---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The exact cubic interpolation weights on alternating h,rh nodes yield the claimed difference transfer a(r)=r^2(4r+3)/(5r^2+5r+1), b(r)=-r(r+1)/(5r^2+5r+1). Multiplying reciprocal phases and setting q=r+1/r gives trace (-q^2+q+7)/D and determinant (q+2)/D, D=5q^2+30q+41. The three strict quadratic Schur inequalities for 5P have manifestly positive numerators for q>=2. The discriminant numerator q^4-22q^3-173q^2-390q-279 has exactly one root q*>2 (Descartes plus signs). For q<q* the modulus is sqrt(d(q)), strictly decreasing; beyond collision, t<0, t' and d' are negative, so (-t+sqrt(t^2-4d))/2 increases. Thus the unique minimizing q and reciprocal r pair, no fixed ratio ceiling and sharp unattained 1/5 supremum are established. Independent exact rational transfer computation for six ratios agrees. Spectral results apply only to homogeneous BDF3 on a fixed two-periodic grid, not arbitrary grids or nonzero spectral parameter.

## originality

FAIL

FAIL: the earlier November 2 published Resultary primary theorem on the identical interpolation-based alternating BDF3 gives the exact same trace/determinant (via r+1/r), strict 1/5 sharp universal bound and precisely the SAME quartic discriminant and reciprocal collision ratios 28.515. The later purported global optimum occurs at that earlier identified double root, directly following by monotonicity of its previously published t(q),d(q); no independent theorem survives. An additional October 12 stronger all-BDF-order result also covers the unrestricted BDF3 homogeneous zero stability. This is positive mathematical implication evidence, not a negative keyword search.

## value

FAIL

FAIL: zero-stability, the sharp 1/5 bound and the shape of the collision already appear as exact claims in the earlier source. Selecting the collision as the minimum by an elementary monotonicity calculation does not supply a mathematically distinct worthwhile invariant or structural gap under the unchanged claim. Correctness and reproducible rational verification cannot rescue the covered result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
