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

In the asserted physical complex coordinate the exact map is multiplication by ω=α+i√(1−α²) plus the real cubic −2α(Re z−c Im z)^3. Its z² z̄ coefficient divided by ω is −a+iac with a=3α/[2(1+α)]>0. The other cubic homological denominators require only ω²≠1 and ω⁴≠1, automatic on the open interval. Oddness gives an O(|u|⁵) remainder after the odd near-identity change. For ρ=|u|², sufficiently small nonzero states stay small, cannot hit zero, and obey ρ′=ρ−2aρ²+O(ρ³). Reciprocation first gives ρ=Θ(1/n), then 1/ρ=2an+O(log n). The phase increments are θ+acρ+O(ρ²); subtracting θ+c/(2n) leaves O(log n/n²), whose tail is O(log n/n). Thus the corrected phase converges with the advertised error after multiplication by the n⁻¹ᐟ² amplitude; returning to z changes it by only O(n⁻³ᐟ²). Irrational rotation follows by bounded exponential partial sums and summation by parts against n^{ikc/2}; rational rotation follows on each residue class because the unbounded increasing logarithm has increments tending to zero. Inverse real-linear coordinates give the exact full ellipse. All conclusions exclude the origin and are for fixed α and sufficiently small data.

## originality

PASS

The exact map, neutral boundary, cubic normal form and O(n⁻¹ᐟ²) upper bound are antecedents. In the inspected evidence, the distinct claim is the controlled complex-orbit asymptotic in the original coordinate, including an initial-state phase, quantitative remainder and rational-angle full accumulation ellipse. The cited radial upper estimate and formal radial truncation do not yield those statements by substitution.

## value

PASS

The result resolves what a known stability/decay bound leaves open: exact amplitude, a phase correction needed to approximate each orbit, and the fate of the rescaled limit set at commensurate rotation. In particular, merely predicting a finite set of rational rotation phases misses the whole ellipse because the drift keeps accumulating. This is a meaningful distinction for the canonical neutral-boundary example without claiming a new normal-form method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
