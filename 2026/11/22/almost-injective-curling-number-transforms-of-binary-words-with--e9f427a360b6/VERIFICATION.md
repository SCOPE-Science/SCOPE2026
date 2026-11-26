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

A repeated suffix with any one can only be a square, of period d=b+1, with exactly one marker per copy. In zero-based indexing the earliest marker p=a must lie in [t-2d+1,t-d] in a square ending at t, with p+d the other marker. This gives a>=b at the second marker and b>=1,a>=b-1 one step later. Otherwise the terminal zero run supplies the maximum; for runs of length >=2 the possible square cannot increase it. Thus the three-gap factorization is valid. Initial starts 123,121,11 distinguish the stated leading-gap cases; 121 can hide only (2,0,0) versus (0,0,2), and comparison through positions 3–6 in the 11 case gives the other two length-four and the one length-five cross-leading-gap collisions. For fixed a, b=0 is separate, and a staircase of length >=3 gives b uniquely. The local entry index in line 58 is off: for b=1 versus 2 the second entries after R_a(1) agree iff a>=1; the third entries then agree iff a>=2, with the third entries 2 and 1 when a=1. Length equality matches c with c-1. At a>=2 the resulting sequences coincide for c=1,2 and differ at position five after R_a(1) for c>=3. This verifies the claimed pairs despite that indexing slip. Direct n=2,3 cases are injective. The count and uniform conditional entropy and success formulas follow from exactly two doubletons at n>=7. Inspected VERIFICATION.md and both Python 3 replay scripts without executing the uploads: direct suffix comparisons through n=40 and formula grouping through n=100 supplement, but do not prove, the reconstruction.

## originality

PASS

The full prefix statistic itself is prior art. The best-supported distinct claim is the complete inverse classification on fixed binary weight two for every n, including exact ambiguity. The closest full texts and result statements use the same transform with a different constraint, or measure a single curling number instead.

## value

PASS

Weight two is the first binary sparsity level at which a repeated suffix can use both symbols. The exact all-length inverse fibers identify precisely the failed reconstructions and give the exact ambiguity and decoder accuracy, a complete answer to a natural inverse observation problem rather than a finite table or arbitrary cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
