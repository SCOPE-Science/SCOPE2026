---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Fresh arithmetic generation reproduces the exact bases n=1..10, and the eight realized augmented pairs are closed under substitution and contain the seed. Their third iterates cover every length-eight window, with 24 even and 32 odd words and no shared word. A collision of length n>=8 must have equal start parities. Even starts project to equal length-ceil(n/2) half-index factors. For odd starts, the even comparison at offset 1 and odd comparison at offset 2 force equal parity of the half-indices; then all comparisons give a contiguous equal block of length floor(n/2)+1 at the half-indices. Thus j<2R(ceil(n/2)) is impossible. Conversely, the earlier match at the origin doubles by the bit recurrence since the base repetition position is even, and this persists through induction for n>=11. At a first collision uniqueness follows because two earlier matches would already collide. The closed form follows by halving, and powers of two and lengths one greater give the two ratio extrema.

## originality

FAIL

A distinct indexed result gives the same exact all-length invariant, limiting ratios, and earlier starting indices. Its dyadic-block proof differs from the frozen decimation proof after the common parity certificate, but does not distinguish the claimed theorem. This is verified equivalent coverage, not a judgment of authorship, priority or dependence.

## value

PASS

An all-length classification for a canonical automatic word identifies the exact collision, its predecessor and the dyadic jump behavior. The parity-decimation proof explains the jumps by a small synchronization certificate and a recurrence rather than long prefix scans. This is mathematically useful content even though the theorem is covered elsewhere.

The dated certificate retains the supplied scientific assessment, sources and limitations.
