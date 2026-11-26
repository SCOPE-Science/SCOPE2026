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

After splitting E, write S2=sum x_i^2 on sum x_i=0. The constrained gradient condition says x_i^3-(S2/4)x_i is constant over the coordinates, so there are at most three distinct values. With three values a,b,c, their sum is zero and S2=2(a^2+b^2+c^2). The three moment equations for their multiplicities minus two form a nonsingular Vandermonde system, hence each value occurs twice (char >=7). With two values of multiplicities m,n and m+n=6, using ma+nb=0 and equating the gradient coordinates yields 18(mn-8)=0, forcing multiplicities two and four in the stated characteristics. The quartic equation follows from the constrained gradient by Euler's identity. Thus the reduced singular curve is exactly the union of the paired-coordinate lines; a (2,4) point is incident to the three matchings containing its distinguished pair, and a point with three distinct values is on exactly one line. This verifies the duad–syntheme geometry and its natural coordinate action. In a separately constructed graph I computed the connected reduced determinant 3^10*5^8, all eleven exact Hermite/Smith forms on the degree-zero lattice using successive differences, and all fixed vertex counts. They match every row, including the five-cycle with no fixed vertices but C5+C45. The equivariant perfect graph pairing transfers the coinvariant factors to fixed groups. All eleven coordinate types are realized by étale field-factor products; extra graph color-swapping automorphisms are not part of the claim.

## originality

PASS

The same graph and all coordinate actions are antecedents; the inspected same-graph records give independence-complex homology, geometric spectra or a connected Picard torus rather than the finite graph critical group. Other graph-critical-group results treat different graphs. No equivalent table or stronger equivariant discriminant calculation was found in the material inspected.

## value

PASS

This is the canonical incidence graph of the entire singular boundary, a natural setting for integral divisor equivalence. The complete coordinate-twist table refines its ordinary critical group. The five-cycle gives 225 fixed classes with no fixed geometric vertices, and the (5,1) and (4,2) actions have different fixed vertex counts but identical fixed class groups. These contrasts explain why the finite arithmetic invariant is worth knowing beyond zeta and torus data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
