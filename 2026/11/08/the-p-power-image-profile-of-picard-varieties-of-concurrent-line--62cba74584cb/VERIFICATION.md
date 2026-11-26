---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For the reduced concurrent plane-line pencil, a product of all but one line equation isolates one branch in degree m-1, while a binary form of degree less than m-1 cannot vanish on the other m-1 directions and be nonzero there. Thus the conductor is the product of the branch ideals (t_i^{m-1}). In degree d through m-2 the local-ring image is the independent evaluation space V_d of dimension d+1. The normalization units exact sequence gives the connected Picard group as G/H, with G the principal branch jets and H the ring units with common constant 1; independent branch constants remove the torus and the normalized components have trivial Pic^0. G and H are smooth connected unipotent, with the degree filtration giving additive factors. At s=p^r the reduced image G_s consists of all jets supported on degrees sj, by coefficient Frobenius and algebraic closedness. G_s intersection H is the linear coefficient locus V_{sj} in precisely those degrees. Fibers of the quotient map restricted to G_s are cosets of that intersection, so the image dimension is mL-sum_{j=1}^L(sj+1); at r=0 it is (m-1)(m-2)/2. A single-branch unit 1+t_1 retains a nonzero class whenever s<=m-2, by the same zero-count argument; s>=m-1 kills the whole group. This yields the exact k-point exponent, threshold and m=4, p=2 example. Packaged verify.py and verify_output.txt were inspected, not executed; finite-field ranks do not on their own establish the group-scheme image formula.

## originality

PASS

Passes for the complete reduced multiplication-image dimension profile on the concurrent plane-line family. The relative-unit quotient, unipotent structure for singular curves, and examples of higher unipotent period are prior. None of the materially compared results supplies the all-m, all-r profile or the specific graded intersection computation.

## value

PASS

For a natural reducible plane-curve family, the full succession of multiplication images distinguishes characteristic-sensitive group structure missed by the arithmetic genus or dimension alone. It gives an exact uniform numerical invariant and identifies the first nontrivial p-image in each characteristic, with a concrete order witness, without needing a full group classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
