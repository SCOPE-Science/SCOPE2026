---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

Reduction of the universal integral binary-cubic discriminant modulo 3 yields Δ=b²c²−ac³−b³d, with four derivatives exactly −c³, −bc², −b²c, −b³. Therefore the projective intrinsic Jacobian ideal is (b,c)^3; the graded pieces of its third infinitesimal line neighborhood have Hilbert polynomial (n+1)+2n+3(n−1)=6n−2. The repeated-linear-factor morphism from P¹×P¹ is proper, finite, birational, radicial and induces cubic Frobenius over L. On chart a≠0, the finite normal free-module lattice R=k[b,d]⊕k[b,d](bt)⊕k[b,d](b²t²)⊂k[b,d]⟨1,t,t²⟩ with t³+bt²=d gives conductor b²S=(b,c)^2; the symmetric chart d≠0 covers the rest of the singular line, and the complement is normal, so the global conductor is I_L². Finite-field Frobenius bijectivity gives #(D(F_q))=(q+1)²; zeta formula follows, while standard quartic hypersurface and Künneth cohomology give H²(O_D)=k versus H²(O_P1×P1)=0. Independent characteristic-3 symbolic derivative check confirms the Jacobian; source verification code includes finite GF(3)/GF(9) projective enumeration but not proof of all fields.

## originality

FAIL

A 2026-10-25 full theorem on the universal monic characteristic-three cubic discriminant explicitly proves the same cubic Jacobian ideal, square conductor, affine normalization lattice, and cubic Frobenius along the singular line. The binary-cubic projective discriminant restricts to exactly that monic chart, with its remaining singular-line chart the symmetric exchanged-variable copy. Hence the ostensibly new projective conductor/Jacobian statement is an immediate gluing corollary. The remaining point-count/coherent-cohomology observations follow from the classical projective repeated-factor parameterization, finite-field Frobenius, and elementary quartic hypersurface cohomology; no independent non-implied classification remains.

## value

FAIL

The projective binary-cubic discriminant is a natural geometric object, but the submitted distinguishing structural assertion—cubic Jacobian thickening versus square conductor and Frobenius normalization—is the direct global restatement of an existing exactly matching local theorem on two symmetry-related affine charts. The appended zeta and H² computations are basic formal consequences of P¹×P¹ normalization and degree-four hypersurface sequence. They do not supply a substantively motivated new structural theorem beyond the stronger already published local calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
