---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The height fiber of K_d at x has length 2−||x||_1−||x||∞, and each integer dilation n contributes max(0,2n−||x||_1−||x||∞+1) lattice heights. Max-norm shell summation of F_m(u)=[(1+u−2u^{m+1})/(1−u)]^d produces the claimed rational A_d(u); selecting even powers from A_d(u)/(1−u)^2 proves the full Ehrhart series for every d≥1. For odd d, the potential u=i poles of the j≡3 (mod 4) summands cancel in the even extraction because the relevant ratio is i^{2d−j+1}=1. Independent rational SymPy reduction in d=4,5 reconstructs coprime denominators with cyclotomic factors orders (1,2,3,5) and (1,3,5), yielding exact minimal periods 30 and 15 by partial fractions and the pole-converse. Independent lattice enumeration at n=1 matches each rational-series coefficient. Order/sign chamber volume integration has determinant one and gives 2^{2d+1}/[(d+1)(d+1)!]. Finite checks do not substitute for the arbitrary-d shell and parity proof.

## originality

PASS

Best-of-knowledge PASS for this specified standard-lattice *Cayley polar* series and the sharp d=4→5 minimal quasiperiod reversal, not for general Ehrhart quasipolynomial theory or the existence of period collapse. McAllister–Woods already gives rational examples of arbitrary denominator/period collapse. The published Resultary dyadic-axis cross-polytope theorem uses Σa_i|x_i|≤1 and a product generating series, not the mixed max-plus-one body K_d. Black–De Loera studies the monotone-path *fiber* polytope of a crosspolytope, whose combinatorics resemble cube-cross sums but it is not the identified Cayley polar with this lattice. No inspected prior gives the exact denominators or consecutive 30→15 reversal for these K_d.

## value

PASS

A geometrically natural polar of a symmetric-height cube/cross-polytope Cayley construction has an all-dimensional rational lattice-count law and a systematic parity cancellation. The sharp reversal of exact quasiperiod at consecutive ambient dimensions supplies a motivated arithmetic counterexample to naive monotonicity, not a numerical curiosity; it extends beyond one finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
