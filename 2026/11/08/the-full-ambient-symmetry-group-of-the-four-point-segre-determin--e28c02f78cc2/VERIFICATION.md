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

The multihomogeneous determinant is squarefree: a repeated nonconstant multihomogeneous factor would force degree at least two in one of the eight factors. Thus preserving the reduced divisor is equivalent to preserving the section line. By independently generating the determinant from the 24 assignments of its columns and reducing the action matrix modulo 101, I obtained rank 18 and augmented rank 19. These are rational lower bounds, and the six independent diagonal kernel vectors give the corresponding upper bounds. The projective stabilizer Lie algebra has dimension six, so the known connected diagonal pair is the identity component over C. The normalizer preserves or interchanges the blocks since these are the supports of the two simple factors; within each block its factorwise conjugations must be the same because PGL2 is centerless. In the tensor support each block selects two positions, thereby specifying a matching. The support rejects precisely the pairs with the same matching, so a block-preserving permutation must induce equal matching actions. Conversely, simultaneous relabelings and individual Klein-four relabelings preserve the cross-multiplied bracket relation. The latter follows since each double transposition fixes the two bracket products defining the cross-ratio with their common sign. Block exchange swaps the tensor coordinates. A separate exhaustive check of all 40320 pure permutations gave exactly 192 signed symmetries. The connected group meets the pure permutations trivially, giving the stated semidirect product.

## originality

PASS

Pass specifically for maximality of the ambient stabilizer, including the connected component and split finite quotient. The determinant/cross-ratio interpretation and the classical anharmonic transformations are not new. The strongest retrieved same-object results give the defining cross-ratio relation and a singular-locus description, not the full ambient-group computation.

## value

PASS

Four-point coplanarity on the Segre quadric is a canonical incidence relation. The exact symmetry classification says which label reductions are valid for the incidence problem: the full finite quotient includes the less evident independent Klein-four relabelings, and maximality guarantees there are no additional factorwise redundancies. This is more than identifying the standard simultaneous PGL2 and relabeling actions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
