---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Xie Theorem 1.2 gives lct I_(3,4)=11/2 and (5.1) gives dim J_L≤floor(13L/2). In the split quadratic space, choose a unit-parameter isotropic vector A and orthogonal transverse z with B(z,z)=1. Set v_1=A and v_j=A Y_j+t^a z W_j, a=floor(L/2). For even L, no W-constraints; for odd L impose W_3(0)=W_4(0)=0, W_2(0)≠0, making each pairwise residual product vanish modulo t^L. Count 5L+3a (even) or 5L+3(a+1)-2 (odd), giving floor(13L/2). The dual pairings with b,z recover Y and the truncated W coefficients, proving no fiber-dimension collapse. The L=1 case correctly gives dimension 6. Independently checked the parameter counts and first nonzero coefficient products for L=1..18.

## originality

PASS

Xie Corollary 7.1 establishes jet equality when M or L is even; here M=3, so odd L is excluded. Its odd M=1,h=4,L=3 counterexample shows that rounding the lct bound alone does not imply equality. The new odd-L residual-axis chart supplies a nontrivial equality proof at M=3,h=4. The Casabella–Sammartano orthogonal-frame paper was not full-read; historical-priority risk preserved.

## value

PASS

The all-length jet-dimension function is a natural invariant of a specific off-diagonal Gram zero fiber highlighted in Xie’s odd-ambient open direction. The explicit odd-length lower-bound chart resolves a nonautomatic equality case at every odd L, not merely a finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
