---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For a finite poset, comparable queried cells cannot be shattered. For an antichain, the all-in and all-out labels impose the two closure-size bounds; for any labelling the forced down-closure lies in the complement of the forbidden up-closure, and a linear extension of the difference realizes the desired intermediate size. On the square grid the two closures intersect exactly in the s queried points. Their total size must be at most m², so there are at least s cells incomparable to the entire support. Such cells occur only in the (m−s) unused rows and (m−s) unused columns, giving s≤(m−s)² and the stated ceiling. For the anti-diagonal prefix of length d_m, the down- and up-closures separately sum to d_m(2m−d_m+1)/2; the quadratic inequality makes the band nonempty and includes floor(m²/2). The argument includes s=0 and m=1 and does not say the displayed band is exhaustive. An independently written direct trace enumeration for every rank through m=4 gave central dimensions 0,1,1,2 (for m=4 the maximal band is actually k=5,…,11, wider than guaranteed). The source package's verify.py and verify_output.txt give an additional finite antichain-trace check, inspected without executing it; the all-order conclusion rests on the proof.

## originality

PASS

The supported distinct claim is the sharp square-grid universal bound and its central and band attainment, not the general closure criterion or the incomparable-cell technique as such. The strongest distinct indexed overlap is the rectangular Young-diagram record. Its unused-row/column argument is substantially the same mechanism, and it determines rigid ranks in one aspect ratio, but its stated theorem neither contains the square regime nor supplies the square central witness and band. Inspected primary literature concerns other shattering notions or computational objectives. This is a best-of-knowledge assessment, not a priority finding.

## value

PASS

Middle fixed-area Ferrers layers are natural slices of a classical distributive lattice. Their trace complexity need not be read off from rank size or width. The quantitative square-root deficit supplies an exact all-order comparison with unrestricted width, and a concrete support gives every labelling on a specified interval of ranks. The claim does not determine the VC dimension at every rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.
