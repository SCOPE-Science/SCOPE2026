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

Minimal numerator and denominator have disjoint prime supports, so coordinatewise divisibility of the two terms gives exactly the stated signed order. The componentwise sign map is monotone, idempotent, equivariant and below the identity; the natural transformation to the identity gives a homotopy fixed on the image. The map is norm nonincreasing and its image at cutoff k is exactly the signed faces of size at most min(k,r), with the empty face excluded. This gives the barycentric skeleton model compatibly with inclusions. The truncated partition-matroid complex is pure shellable; its only reduced homology is free in degree k-1 with rank from the alternating signed face counts. This also follows from cellular approximation in the sphere for the lower skeleton, with a connected graph for k=2 and the stated discrete convention for k=1. At k=r the full sphere appears, and for r=1 it is S^0 at every cutoff. Successive nonstable source and target homology degrees differ, so maps on reduced integral homology are zero intermediately and are identities under the stable identifications. Chain orbits are determined exactly by their ordered support sizes (coordinates can be permuted in the successive blocks of newly added signs, and signs flipped); every size sequence occurs and quotient simplex face maps delete sizes. Thus the core quotient is a simplex, and the original quotient is homotopy equivalent to it. The fresh bounded script `python3 /workspace/replay/audit_checks.py 3` (output `/workspace/replay/3.txt`) checks subsets, sign retraction, and complete signed-face chain orbit types on sixteen small ranks/cutoffs, not the general topology or torsion claim.

## originality

FAIL

A distinct indexed record on the punctured join-Grothendieck group publishes the exact equivariant signed-support retraction, not just an abstract terminal sphere equivalence. Its pointwise inequality sign(x) <= x preserves every length sublevel, including throughout its poset homotopy, and the published signed-face identification restricts by face size. Hence the claimed compatible skeleton model is a direct restriction of an existing explicit construction; the barcode and full-group quotient are immediate consequences of that model and standard skeleton and signed-permutation structure. This is demonstrable mathematical coverage, not a claim that one of the two same-day records came first or that the other record prints the barcode verbatim.

## value

FAIL

The length filtration is natural, and the explicit tables of transient classes can be useful as exposition. As a standalone claimed finding against the published explicit equivariant model, however, the new cutoff statement just restricts a pointwise order contraction to a downward-closed sublevel. Persistence then follows from the dimension shift and stabilization, and the quotient is the usual size chamber of signed flags. No independently new invariant or nonroutine claim survives this specific comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
