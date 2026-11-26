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

Meeting any selected off-diagonal atom edge with the two diagonal endpoints forces its two arms. These are the only constraints: a nonzero coordinate in a meet requires the two inputs to share that atom there, and two nonzero coordinates require the same input edge; diagonal pairs and zero-zero are already present. Counting all optional edges gives the size polynomial and summing over inclusion of each right arm gives the single sum. Symmetry ties the arms and orientations; a compatible equivalence can identify distinct atoms only inside the zero class, and every subset of atoms is possible in that class. For k missing arms, the frozen exponent deficit bound is valid; even the uniform bound Delta >= (n/2-1)k yields a relative error at most (1+2^(1-n/2))^(2n)-1=o(1). Full saturation is therefore typical and its conditional law is uniform on all directed edge subsets, so the unconditional count differs in total variation from the binomial law by at most the failure of saturation. Independent exact check `python /workspace/checks.py 3` enumerates reflexive relations for n=1,2,3, verifying all polynomial coefficients, saturated size distributions and the triples (4,2,2), (25,5,4), (322,18,8). No finite test substitutes for the proof. The verification note's Python 3.9 floor is too low for the bundled script's int.bit_count (3.10+); this documentation issue does not affect the theorem.

## originality

FAIL

A distinct exact indexed classification covers the flat family, the principal counts and the limiting coefficient; its proved normal form and asymptotic mechanically yield the additional size polynomial and random law. This is coverage, not an earlier-priority finding: the matching record's Oct. 26 date-key follows the audited record's Oct. 18 date-key and no provenance is inferred.

## value

FAIL

The flat family and DSC coefficient are well-motivated, but there is no independently needed exact invariant remaining in the audited claim after the indexed structural classification. Both the marked census and the high-probability binomial law follow mechanically from its explicit free-edge model and dominant-stratum count. No substantive extension beyond that overlap is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
