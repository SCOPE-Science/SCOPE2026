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

Each choice of how many sum-two reads represent 02 rather than 11 produces a looped undirected graph on the three symbols. A realizing word is precisely the vertex record of an Euler trail or an Euler circuit on its connected nonzero-degree support; a single loop handles cyclic m=1. For a trail, parity is automatic on three vertices. If a2>0 allocate all of it to 02 and the support is connected; if a2=0, there are exactly the three listed disjoint connectivity obstructions, counted by two binomial(m,2) terms and m-1. A circuit requires a1, a3 and the 02 multiplicity to have the same parity. With both adjacent cross-edge bins positive, they connect the support, and odd parity costs one sum-two read. With only one adjacent cross-edge bin positive it must be even, and a loop at the opposite end requires at least two sum-two reads to attach it. With neither adjacent cross-edge bin positive, a positive even a2 can all be allocated to 02, a positive odd a2 can only be realized at vertex 1 without outer loops, and with a2=0 exactly one nonempty loop bin remains. Summing the resulting disjoint geometric series yields the stated generating function. Its partial fractions at 1 have coefficients 1/2, -1/4, -17/8, 87/16 and -105/32 in descending pole order; the term at -1 is -9/[32(1+z)]. Coefficient extraction gives the stated quasipolynomial and leading coefficient. Selecting one word per histogram proves the finite-block code claim. Independent direct enumeration of 118,092 linear/cyclic words at m=1..9 matched both counts, as a finite check only. The frozen script was read and not executed.

## originality

PASS

The exact counts concern the image after erasing read order and merging 02 with 11. The inspected closest results either keep read order or count richer pair-profile categories, and their cardinalities and inverse-fiber statistics do not determine the size of this image. The evidence supports distinct exact five-bin counts, subject to the cited comparison limits.

## value

PASS

This is the first nontrivial collision of unordered pair types under ordinary addition on the given alphabet. Exact projected support counts are the useful finite-block code sizes for this observation, not just counts for a richer sensor. The all-length comparison at fixed number of observed windows isolates the arithmetic effect of closure: parity removes half the leading-order histograms, while connectivity governs the lower-order corrections. Standard Euler existence for a fixed graph does not mechanically give these projected counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
