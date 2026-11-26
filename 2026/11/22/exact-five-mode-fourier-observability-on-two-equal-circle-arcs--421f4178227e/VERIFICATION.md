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

In normalized Haar measure the exact Toeplitz moments are 2 sin(ka) cos(k beta)/(pi k), with diagonal 2a/pi. At antipodal placement the odd and even character blocks have sizes two and three. The smaller eigenvalue of the symmetric two-dimensional piece of the even block lies strictly below all other eigenvalues, since h=(sqrt(p^2+8)-p)/2>1 and |p|<1. Reconstructed the shifted trial form on 1 and the cosine quadratic, independently dropping the constant term of the latter. Dividing the determinant by the positive common scale and reducing modulo y^2+c(2c^2-1)y-2c^2 gives t^2(A+t^2D), t=cos(beta). The bounding quadratics for h and the strict signs of A,D were checked by exact arithmetic, using the positive-coefficient transform c=x/(1+x) for the signs on 0<c<1. Every nonantipodal placement, including touching arcs at beta=a, has t>0 and a negative determinant, so its least Rayleigh quotient is strictly smaller. The exact Taylor series has leading term 64 a^5/(135 pi).

## originality

PASS

The supported distinct claim is the exact finite-width maximum and strict antipodal uniqueness for two equally wide arcs in the five-mode band. The optimized small-width leading coefficient and leading-order antipodal design are already covered. Close same-day results were compared for statement-level implications, without assuming an order from the publication date.

## value

PASS

At fixed observation measure, maximizing the worst captured energy is the sharp conditioning problem for continuous observation on two equal sensor arcs. The first nontrivial extension beyond the previously known three-mode exact case and the known small-arc leading law gives a usable finite-width benchmark: it identifies the placement uniquely and quantifies conditioning at every width, not just at an endpoint. The two-vector comparison proves a structural result that would not follow from diagonalizing only the antipodal case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
