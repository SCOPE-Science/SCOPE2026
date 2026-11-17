---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For every simple labelled C_n, n>=3, explicitly identified all maximal geodesics as n consecutive length-floor(n/2)+1 vertex blocks (including antipodal even cycles). Hitting is exactly gap d_i<=L+1; essentiality of each chosen vertex is exactly d_(i-1)+d_i>=L+2. Sum of latter bounds forces at most three selected vertices. Two-gaps yield b_n=n (odd) or 3n/2 (even). Three-gaps yield d_i<=r=ceil(n/2)-2, and the bounded composition count gives c_n=(n/3)binom(3r-n+2,2) when 3r>=n, else zero. This implies the exceptional purity rebound at n=10. Independently constructed shortest-path maximal blocks and enumerated all candidate subsets for n=3..15; results agree. Infinite n follows from the gap argument rather than finite checks.

## originality

PASS

The known minimum geodesic-transversal size two for cycles and general circular-arc transversal enumeration are excluded from novelty credit. None of the inspected earlier statements implies the exact inclusion-minimal distribution or re-entrant purity; best-of-knowledge originality is confined to that explicit refinement.

## value

PASS

The complete inclusion-minimal transversal distribution of a basic graph family is a natural exact obstruction invariant: it distinguishes minimum hitting sets from larger essential hitting sets and determines the purity of the corresponding independence complex. The loss, return, and permanent loss of purity at n=9,10,11 is a nontrivial boundary, not a merely renamed minimum-two result. The exact cubic-vs-linear counts permit direct use in cyclic blocker and simplicial-complex work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
