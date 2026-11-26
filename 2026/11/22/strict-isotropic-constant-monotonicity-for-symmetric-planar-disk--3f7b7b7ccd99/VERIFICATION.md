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

Two reflections give a centered diagonal covariance. The strip at |x| has half-height √(1−(a+|x|)²) for |x|≤1−a; integrating 1, x² and y² gives A, X and Y and thus F=XY/A⁴. Substituting u=cos v in the three strip integrals (using cos/sin power identities) recovers all closed forms. Independently the moving-boundary derivatives are A′=−4s, Y′=−4s³/3, and X′=−8(s³/3−aA/4); substituting them and reducing by s²=1−a² reproduces F′=−4aP/(9sA⁵). I reconstructed P's Taylor coefficients by exponentials in `python3 /workspace/checks/independent_01_05.py` (check 4), checked the exact cancellation through degree 15, the increasing cubic bound, the five nonpositive coefficient pairs, the last negative coefficient, and the strict full-interval remainder margin (approximately 7.35316e−5 after dividing by θ¹⁶). In each exponential term θ^p exp(ikθ) the real-variable integral remainder is bounded by |k|^(45−p)θ^45/(45−p)!, since derivatives along the real angle have unit exponential magnitude. This makes the sign strict for 0<θ<π/2 independently of numerical sampling. At a=0 the moments are those of the unit disk. Rescaling x by 1/(1−a) and y by 1/√(2(1−a)) gives the stated limiting strip heights; integrating the parabolic strip produces 8/3, 64/105, and 8/15. Dominated convergence gives the corresponding limit 9/1400 for F, and strict increase on the interior plus continuity supplies the equality structure. The author-reported 150 tests are not an independent rerun.

## originality

PASS

The supported distinct claim is strict monotonicity and the sharp range for the normalized covariance determinant on the entire two-disk family. Individual moments are recoverable from prior work and ordinary circular-segment integration. No priority is claimed for those moments or for the disk lower bound alone.

## value

PASS

The equal-disk lens is the basic nonscalar intersection family. The theorem orders it by a canonical affine invariant, despite both axial scales changing, and identifies a sharp limiting parabolic lens. This yields a meaningful benchmark beyond raw inertia or anisotropy ordering; no claim is made for unequal disks or arbitrary nesting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
