---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

RESULT.md lines 5–30 and 32–88. Since t is not in F5, none of t=±2 or t=−1 can hold. One nonzero coordinate gives a nonzero derivative; with exactly two, the partials give a square-coordinate system of determinant 4−t²; with three, its determinant is (2−t)²(2+2t). Thus the projective gradient has no common zero over the algebraic closure. Bézout then excludes reducibility of the smooth plane quartic and gives the four-point line bound; adjunction gives genus three. Independently enumerated all 651 points and all 651 dual lines in a last-nonzero-coordinate normalization, with pair-valued field arithmetic. This gave 56 points and the spectrum (63,168,196,0,224), and converting only for comparison to the given certificate's index order recovered all four entries of each displayed line block and a disjoint cover of 0 through 55. No smaller cover is possible. The count attains 26+2·3·5. Tafazolian's Theorem 1.1(ii) identifies the unique F25-maximal genus-three isomorphism class with the Klein quartic's S4-model. In addition, independent computation obtained transitivity explicitly: signed permutations have point orbit sizes 8,24,24; adjoining the projective matrix with rows (2u,2u,3+u), (3u,3u,3+u), (3+4u,2+u,0) acts transitively and preserves all 56 points. Its image curve is the same curve by Bézout (56>4·4). Replay: python3 /workspace/branches/independent_quartic_check.py. The bundled script was read, not executed. This is a finite exhaustive verification and explicit certificate, not a claim at other fields or about all minimum covers.

## originality

FAIL

Distinct Resultary record 1573c6a78ddb gives the identical exhaustive spectrum, partition into fourteen four-secants and sharp covering number for the identical homogeneous model under an explicit field isomorphism. It also gives more pointwise incidence data. A change in presentation of F25 or a different successful witness to the same existence assertion does not supply a distinct result. The catalogue path labels are not needed to prove scientific equivalence and do not by themselves establish historical priority.

## value

FAIL

The chosen curve and exact invariant are natural: a perfect partition saturates Bézout on a distinguished maximal plane quartic. But the frozen contribution merely re-establishes that same known spectrum and minimum cover under a field renaming. The alternative witness is not shown to differ by a mathematically significant property, such as lying in a new orbit or having a distinct incidence structure. No independently useful new exact fact remains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
