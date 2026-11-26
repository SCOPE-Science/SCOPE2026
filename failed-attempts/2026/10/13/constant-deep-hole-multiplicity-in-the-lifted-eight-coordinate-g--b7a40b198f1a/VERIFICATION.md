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

The base code has rank-two parity checks, no zero columns, and a dual of minimum distance 6. For each of the four ternary directions, a nonzero row combination killing it has at most two zero coordinates. All four directions therefore occur twice among the eight columns. Distinct directions remain independent in F_Q. Deep syndromes are precisely those outside the four extended lines, since each pair of different lines spans the whole syndrome space. There are (Q−1)(Q−3)>0 such syndromes for m≥2, including 48 at m=2. For any one deep syndrome, each of six line pairs has four choices of coordinate pair with one uniquely determined pair of nonzero error values, and a same-line pair gives none. Thus the count of errors, equivalently nearest codewords, is 24. The finite F_9 checker was inspected, not run; the closed count proves the extension statement.

## originality

FAIL

The same authors genuinely pose this numerical conjecture and do not display its all-m value as a theorem. Nevertheless their published exact dual-weight set {6,8} for every m≥2 and their UPWS identity for the same [8,6] lift already fix the covering constant by the elementary Hamming character transform and quadratic interpolation. This is a verified corollary of stronger results, not a claim that Remark 5.5 already states it as proved or that the finite table extrapolates.

## value

FAIL

The conjectured count is well motivated and the short projective argument is correct. But its only claimed new precise invariant is already a direct numerical consequence of the existing uniform-packing and dual-spectrum theorems for D5. The indicator-line argument supplies an alternate explanation, not a surviving unknown invariant or a new structural theorem of independent scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
