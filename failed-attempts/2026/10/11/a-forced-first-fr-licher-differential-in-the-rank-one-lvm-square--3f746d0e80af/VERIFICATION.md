---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For any compact connected complex X with h^(2,0)=0, the first quadrant Frölicher bidegrees imply E_inf^(1,0)=h^(1,0): d1 of constants is zero, d1 from (1,0) lands in the vanished (2,0), and higher bidegrees cannot touch it. The only differential reducing E1^(0,1) is d1^(0,1), because d2 maps into E2^(2,0)=0 and r>=3 has negative antiholomorphic target. Thus b1=h10+h01-rank(d1^(0,1)). The source supplies h10=1,h01=2,b1=2 at t=0, so rank=1; punctured h10=0,h01=2,b1=2 and E1-degeneration give rank=0. The published family is proper holomorphic and smoothly locally trivial, so comparison is on a fixed smooth type. Independent exact symbolic expansion verified central E1 dimension 32 and punctured E1 dimension 16, with b1=2 in each case. It does not prove the geometric Hodge inputs or exhibit an image class.

## originality

FAIL

Although arXiv:2609.37936v1 does not print the exact rank in a separate proposition and published finding searches mostly return the same-record mirror, its Proposition 12.1, Lemma 11.12 and Theorem 12.7 already state all numerical and deformation inputs. A routine first-quadrant spectral-sequence edge chase gives rank(d1^(0,1))=h01+h10-b1 whenever h20=0, and substitution reproduces the entire final claim. This is an immediate mathematical corollary of prior statements, not an original independent theorem under the explicit implication-based originality standard.

## value

FAIL

The rank-one square and its Frölicher differential are natural and motivated; pinpointing a nonzero differential is descriptive. But the exact asserted rank and its 0-to-1 deformation jump are immediate arithmetic from the existing full Hodge table, b1, and the textbook low-degree edge argument. The package identifies no new differential representative, map computation, nonstandard structural lemma, uncomputed invariant, general mechanism, or boundary unavailable from those published data. Its value therefore does not pass the requirement that a narrow invariant be unknown and not mechanically implied by a known table; this is a routine deduction of the earlier paper rather than a distinct useful mathematical result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
