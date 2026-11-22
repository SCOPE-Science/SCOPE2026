---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The inradius defect vanishes for each cocircular quadruple by the Japanese theorem. At a regular n-gon, radial differentiation yields the exactly four-tap Jacobian κ[−I+(1+2cos h)S−(1+2cos h)S²+S³], factoring as κ(S−I)(S−e^ih I)(S−e^-ih I). The circle translation/radius tangent modes 0,±1 form its complete 3D kernel. On Fourier k its singular value is 8κ|sin(kx)sin((k−1)x)sin((k+1)x)|. For 2≤k≤floor(n/2) this is increasing by s(s²−sin²x), so k=2,n−2 are least positive; μn=4 sin x sin 2x sin 3x/[cos x(1+cos x)(1+2cos x)]∼4π³/n³. Rank n−3, implicit-function uniqueness, and a tubular nearest circle point yield local F=0 iff cocircular and the sharp distance/error limit. Independently differentiated inradius numerically at n=4,5,7,10,16 and reproduced the Jacobian and gap; exact symbolic identity in supplied verification was inspected, not treated as proof alone.

## originality

PASS

The full 2012 Minculete–Barbu–Szöllősy pages 188–193 derive the cyclic equality and further multiplicative/weighted radius identities, not a transverse Jacobian or local coercivity. Reyes 2002 is a proof of equality. The full 2026 separable-functional Resultary theorem concerns affine functions of inradius for Delaunay flips, not geometric radial perturbation stability. Lambert 1994 gives global Delaunay sum maximality; full proceedings unavailable. The sharp n-dependent local quantitative converse is not implied by the inspected source statements.

## value

PASS

The exact singular gap and attained normal perturbation produce a quantitative near-cyclicity test from only n consecutive flip measurements. The detection of second Fourier mode and n^(−3) condition loss are motivated and potentially useful in polygon rigidity and geometric reconstruction; no global rigidity is overclaimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
