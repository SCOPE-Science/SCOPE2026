---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For n≥3 the only minimal nonfaces are {e_{i−1},e_i,f_i}; the full rim is an invariant facet. On its complement each selected rim set is proper. Toggle the first pendant whose two incident rim edges are not both selected. For fixed rim set the index is fixed, and rim sets are nonincreasing on gradient paths, so a closed path would keep its rim set and would have to make an illegal second upward move after the chosen pendant stays present. The complete augmented matching restricts to an ordinary matching with just one critical vertex. The invariant subcomplex is therefore contractible. It is a CW subcomplex, so collapsing it gives an ordinary homotopy equivalence by an equivariant map to the rim simplex modulo its boundary. On integral top homology a rim rotation has the sign of an n-cycle, while reflection permutes e_i to e_{−i−1}, with one fixed rim edge at odd n and none at even n. Over Q the cellular chains of the ordinary quotient are the orbit chains after subdivision, and averaging gives the invariant homology; the representation is trivial only at n≡1 mod 4. A point invariant under full rotation has barycentric support equal to a union of whole rim or pendant orbits. Each alone is a face and their union is not, leaving the two barycenters. No equivariant homotopy-equivalence or integral orbit homology claim is needed.

## originality

FAIL

The strongest overlap is not merely Vega's nonequivariant sphere statement. Vega's proofs of Proposition 3.7 and Theorem 3.9 identify the full rim facet as the sole critical cell in an augmented matching. This already certifies the contractible complement by restriction, because the full rim is an unmatched facet and its deletion removes no matched pair or cover relation between surviving faces. The relative chain group of that invariant pair is the rim orientation line. This yields the asserted integral character and then the stated rational chain-invariant computation without new equivariant input. The source's even statement does not literally include n=4, but its alternating pendant toggles apply verbatim: at two opposite vertices the paired incident rim sets partition the four rim edges, so a proper rim subset admits one of the toggles. The rotation-fixed assertion is the direct invariant-support consequence of the two edge orbits and their union not being a face. These implications leave no distinct scientific claim of the stated scope, though the packaged formulas and proof phrasing are not stated literally in the prior article.

## value

FAIL

The dihedral orientation and geometric quotient are natural, but for this finding the cited prior proof already isolates the full rim facet. The exact representation and rational quotient then require only the sign of a permutation and characteristic-zero averaging, while the full-rotation locus follows by taking unions of two barycentric support orbits. The isolated length-four extension uses the same alternating two-claw construction. This is a correct and useful restatement with elementary consequences, not an independent new exact invariant or structural advance of the claimed scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
