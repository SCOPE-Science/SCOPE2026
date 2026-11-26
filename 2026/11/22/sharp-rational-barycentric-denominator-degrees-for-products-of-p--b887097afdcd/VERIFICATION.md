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

Nonnegativity and affine precision force every off-facet coordinate to vanish on that facet. Taking limits from the dense domain of the quotients gives the corresponding polynomial numerator vanishing even where q vanishes. The supporting form divides that numerator. At an intersection of nonadjacent nonparallel side lines of one factor, each product vertex misses one of the two facets; hence every numerator and their sum q vanish on the entire residual cylinder. Coefficient extraction puts each coefficient in the corresponding two-variable ideal. On a given side line the residual intersections are distinct: a point outside a convex polygon admits at most two supporting lines through it, and an adjacent endpoint is not residual. There are m-3 residual intersections per line with no parallel sides, and m-4 in the centrally symmetric case; restriction forces a polynomial of smaller degree to have all the side forms as factors. A non-parallelogram quadrilateral has at least one residual point, including a trapezoid. For additivity, take a top-degree monomial of q and extract coefficients of its complementary-block monomial in turn. Each extracted coefficient is nonzero, belongs to its factor ideal, and has degree exactly the chosen monomial's block degree. Summing gives the required lower bound for arbitrary representations. Attainment can be checked directly: with inward side forms L_i(x)=det(e_i,x-v_i), the numerator at v_i is det(e_{i-1},e_i) times the product of the nonincident L_j. Dividing the precision identity by the product of all L_j reduces it to the telescoping sum of e_i/L_i-e_{i-1}/L_{i-1}. This bounds deg q by m-3, and centered symmetry cancels the odd top degree m-3 for a centrally symmetric polygon. The sum of the numerators is positive even on the boundary because at least one incident vertex numerator is positive. Products preserve the required identities and degree sums; invertible affine pullback preserves total degree. The exact independent replay `python3 /workspace/branches/frozen_review_checks.py` (section 1, passes) checked residual ranks and planar identities on six rational examples including a triangle, and product precision on a generic quadrilateral times a trapezoid. The bundled script was inspected, not executed.

## originality

PASS

Best-of-knowledge pass for Cartesian-product minimum degree over arbitrary nonnegative rational representations, not for product coordinates, adjoint product degree, residual vanishing itself, or the single-factor theorem. The new lower bound needs blockwise degree control: restriction to one factor, even using the full planar minimum theorem, gives at most separate lower bounds and not their sum.

## value

PASS

This is a structural sharp formula for a natural high-dimensional family. The quadrilateral examples show exact positive degree k with the same d=2k and m=4k for which the conjectured general expression m-2d vanishes; replacing the factors by parallelograms instead gives degree zero with identical counts. Thus denominator complexity detects geometry invisible to those parameters. The reusable blockwise lower bound, not the known Wachspress construction alone, is the value added.

The dated certificate retains the supplied scientific assessment, sources and limitations.
