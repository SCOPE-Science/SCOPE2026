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

The secondary-polytope theorem for convex polygons gives a simple polytope of dimension n−3 with facets indexed by diagonals; collections of facets meet exactly for pairwise noncrossing sets because these extend to a triangulation. The sum and first moment of GKZ coordinates are independent of triangulation by area and triangle centroids. Their three linearly independent constraints cut out an affine translate of W_n, so the dimension theorem gives equality. Rotation permutes coordinates and fixes the vertex average in the relative interior. Translating to that origin, taking the Euclidean polar in W_n, and projecting radially gives actual equivariant homeomorphisms from the diagonal complex to the representation sphere. The discarded real Fourier modes are the constant and the two first modes. The frequency representatives are 2 through floor(n/2), with a real sign line at n/2 when n is even. At a prime all surviving weights give no eigenvalue one for any nonidentity rotation; for composite n, a divisor weight d with 2≤d≤n/2 is fixed by r^(n/d). At p≥7 the sphere is simply connected and its complex rotations preserve orientation. The lens-space cellular homology gives exactly the stated odd-degree torsion and top integral class. The classifying map to BC_p is an isomorphism in integral cohomology below sphere dimension p−4 (the first nonzero positive fibre row has degree p−4). Pulling back the cyclic degree-two class gives nonzero powers through 2k≤p−5; any generator is a unit multiple. The p=5 circle exception and the generator change (2,3)→(1,5) mod 7 are correct. The independent check `python3 /workspace/review_calculations/small_cases.py polygon` checks every orbit of a diagonal under each nonidentity rotation for the specified small n. An invariant nonempty face must contain at least one noncrossing orbit, so this checks all geometric stabilizer types there, not merely fixed maximal triangulations. It does not prove the homeomorphism or the topology by enumeration.

## originality

FAIL

Distinct Resultary record 43771cca48e4 already states the same prime weighted lens-space homeomorphism, freeness at primes, π_1, integral homology and seven-gon example, with the same GKZ–Fourier proof. The added composite nonfreeness follows from published fixed-dissection counts, and the stated cup powers are a standard consequence of the already-known lens homeomorphism. No distinct substantive finding remains; this is a statement-level comparison, not a provenance judgment.

## value

FAIL

Determining precise lens weights for this natural action is mathematically meaningful but already done on exactly the frozen prime domain, even including p=5 in the covering theorem. The composite freeness check and the standard cohomology of a known lens space do not give a useful new invariant beyond the reviewed source material. No surviving original valuable claim in scope warrants repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
