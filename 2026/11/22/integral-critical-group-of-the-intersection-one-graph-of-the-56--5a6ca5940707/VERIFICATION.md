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

The seven-point blowup classification gives the four complete curve families. I used an alternative signed-pair model: assign E_i to +{i,8}, H−E_i−E_j to −{i,j}, and each Geiser mate the opposite sign on its pair. For signed pairs (s,A),(t,B), checking the Picard pairing gives intersection (1−st(2|A∩B|−1))/2; the remaining two curve families are the Geiser complements. I constructed the 56-vertex graph using this formula and checked it equals the distance-two relation for intersection-zero adjacency. It has 756 edges and degree 27. The exact characteristic polynomial gives eigenvalues 0(1), 24(21), 28(27), 36(7) for the Laplacian, so it is connected and has 2^128·3^35·7^26 spanning trees, confirmed by integer cofactor determinant. Exact integer Smith form yields 1(8), 2(14), 4(7), 28(5), 336(14), 3024, 6048(6), with parenthesized multiplicities. In particular the exponent is 6048. The classification and pairing model apply to every surface in the stated smooth characteristic-zero scope.

## originality

PASS

The geometric construction and distinction between distance relations are classical. The strongest independently inspected arithmetic match computes a different, intersection-weighted graph. No checked source establishes the full integral group for the specific intersection-one graph, and none is excluded on title or date alone.

## value

PASS

The intersection-one relation and its integral divisor quotient are canonical for all surfaces in scope. The 2-, 3- and 7-primary multiplicities refine the distance graph's spectrum and tree count and are a concrete comparison invariant for chip-firing on exceptional-curve graphs. This is neither the ordinary Gosset graph nor an arbitrary subset of exceptional curves, and the full Smith group is not supplied by the geometric distance counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
