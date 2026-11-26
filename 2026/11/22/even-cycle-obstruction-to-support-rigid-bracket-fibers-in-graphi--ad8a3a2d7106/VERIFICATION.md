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

For the final claim in /workspace/repairs/1/RESULT.md, additive orthogonality over the second horizontal vector gives q^(2(n+m)-rank A_lambda); inversion over m edge coordinates gives q^(2n+m). The largest nonsingular principal submatrix of an alternating matrix has order equal to its rank, via 2-by-2 pivot and alternating Schur complement, also in characteristic two. A maximum matching in a support with no even cycles yields a single nonvanishing principal Pfaffian monomial, and no larger Pfaffian can be nonzero. On a fixed support the character sums separate, giving the stated t_e. Conversely choose frequencies on just the edges of a simple even cycle (zero on chords): the two Pfaffian terms cancel at exactly one nonzero choice for one edge, and a different nonzero choice exists precisely in the needed q>2 regime. The adjacent-vertex-deleted path gives rank at least 2r-2, so the chosen ranks are 2r-2 and 2r. Fourier equivariance under independent edge scalings then rules out target support-rigidity. For q=2 supports are individual vectors. The original bowtie count is mathematically correct, now given only as a credited illustration. The frozen code was inspected, not run; separate bounded replay /workspace/branches/bd120593-24bc-4ae8-a935-994db29574c3/bounded_replay.py verified 120 versus 48 horizontal pairs at two equal-support C4 targets over F3 and exactly 96 missing bowtie targets among 729. That replay does not address the general graph/field theorem.

## originality

PASS

The frozen finding separately presents the exact bowtie classification and missing-target count, already covered by a strictly stronger earlier result for friendship graphical groups. That component would not pass as a distinct finding. The actual repaired text removes it from the Finding and retains it only as an explicitly attributed example. The re-audited distinct claim is the support-rigidity iff for arbitrary graphs and the exact matching formula across the complete no-even-cycle class, not the covered forest, single-cycle or friendship subfamilies. The closest real skew-adjacency theorem proves the matching ingredient but not the finite-field word-map law.

## value

PASS

The repaired claim characterizes exactly when a geometric-looking coarse invariant, edge support, specifies every fiber size of a natural bracket word map. It yields all target fibers across a graph class larger than the known separate subclasses, covers characteristic two fields of size greater than two, and shows why even cycles with chords are also obstructions. This is useful beyond commuting-pair counts; the already known bowtie boundary is illustrative, not needed to justify the value of the surviving theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
