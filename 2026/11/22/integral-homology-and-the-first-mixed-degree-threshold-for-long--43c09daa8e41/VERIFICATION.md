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

Each facet is the one-line successor map of a cyclic listing, not the listing itself; the cellular basis consists of distinct ordered subwords with augmented signed deletion. An independent run, python3 /workspace/branches/reproduce_1_2.py 2, generated cycles by permuting the tail of a cycle rooted at 0, converted each to successor form, and closed downward by single deletions. This is different from scanning all permutations and choosing positions as in the frozen code. It checked B_(k-1)B_k=0 for each pair and separately reduced each original boundary by integer unit pivots, giving only unit nonzero Smith factors and zero residual blocks for every boundary. Thus every H_k is torsion-free, since its torsion equals the cokernel torsion of the incoming boundary (the cokernel modulo H_k is the free image of the outgoing boundary). In degree order starting at -1 the resulting free-rank vectors for n=2,3,4,5,6 are (0,0,0), (0,0,1,0), (0,0,0,3,0), (0,0,0,0,15,0), and (0,0,0,0,1,88,0). This checks the complete box, including the interval n=2 and the first possible mixed-degree occurrence among all smaller allowed n. Inspected the frozen checker and output; no uploaded code was executed. This establishes no homotopy wedge type and makes no n>=7 claim.

## originality

PASS

Mixed-degree permutation complexes are already known, but the original claim is the threshold and exact integral homology for the full conjugacy class of single n-cycles. No inspected distinct prior result computes this subcomplex or implies the threshold. In particular, the closest six-letter derangement result concerns a larger facet set with different upper homology.

## value

PASS

The single-cycle class is a natural conjugacy-class generator family independent of the observed homology. The first threshold is determined by an exhaustive lower range, and the size-six exact result is a useful witness that concentration in one degree does not persist in this family. The integer groups, including absence of torsion, distinguish it quantitatively from neighboring cycle classes and the derangement superset; the cutoff is motivated by determining the threshold, not by extrapolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
