---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The weight-three reduced Swiatkowski chain basis is specified by distinct vertices with two reduced halfedge choices and monomials in the 24 graph-edge variables. Reconstructed 4480 C3 and 11520 C2 basis elements, their integral D3 columns, and independently computed rank_F2(D3)=4475 and rank_F3(D3)=4479 (GF3 sparse elimination). Read the original 1919-term primitive kernel certificate: re-evaluated D3*k=0 and gcd coefficients=1, so rank_Q D3=4479 and H3=Z. Re-evaluated each of four certificate mod2 chains c_i: D3 c_i has all even coefficients; the five mod2 vectors k,c1..c4 are independent. Hence w_i=D3c_i/2 give four independent exact order-two H2 classes. Since nullity_F2 D3=5 and rank_Z ker D3=1, UCT/SNF gives exactly four independent order-two classes in coker D3. The quotient to im D2 is torsion-free, so H2[2]=(Z/2)^4. This does not determine possible higher 2-power torsion nor H2 free rank.

## originality

PASS

Best-knowledge original integral rank and order-two subgroup for B3 of the nonplanar Möbius–Kantor graph; known graph-braid chain comparison is a method, while checked neighboring graph computations and planar theorems do not imply these exact ranks.

## value

PASS

Exact 2-torsion rank in three-particle configurations of the natural 16-vertex Möbius–Kantor cubic graph is a motivated integral topological invariant; torsion information is not implied by rational Betti numbers and the explicit generating cycles are reusable. The self-contained exact fact need not complete all integral H2 invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
