---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

At fixed content only the scattered 01 count varies independently. Rotation changes it by n−k for a leading one and −k for a leading zero. After division by d these are a and −b, congruent modulo L=a+b; since b is invertible modulo L, the first L heights are distinct. Equality at L forces equal heights at all pairs of starts separated by L, so consecutive differences give period L, and the converse is immediate from the number of literal rotations. The counts of ones in consecutive length-L circular windows average b and change by at most one, forcing an exactly balanced window. It is a closed segment of the height walk. For d>1, removing it retains both endpoint levels and can lose at most L−1 interior levels. The shortened word has content ((d−1)a,(d−1)b) and the same normalized steps; induction starting at d=1 proves the upper bound. The two monotone runs of the clustered walk share exactly d−1 interior return heights, because b divides ta exactly when b divides t. This attains the upper endpoint, including a=1 or b=1. Coprime content gives n distinct signatures for every word. Inspected frozen verify.py and VERIFICATION.md without executing the script; its reported exhaustive length-2-to-12 diagnostic does not establish the proof or classify every upper-bound maximizer.

## originality

PASS

The distinct contribution is the exact binary upper endpoint n−d+1 over all content pairs. The lower endpoint and complete power equality criterion are already implied verbatim by the alphabet-independent proof in the earlier multiletter record, despite its nominal restriction to at least three letters. The same-day exact-moments record also gives the collision count for d=2, which together with a balanced-window argument yields the upper bound in that stratum. These do not supply the general binary deletion bound and sharp endpoint for arbitrary d.

## value

PASS

There is a natural binary-versus-multiletter distinction: fixed content forces collisions in every binary orbit when d>1 even though higher alphabets can realize full support. The exact binary deficit d−1 and the deletion mechanism explain this obstruction uniformly and give a useful benchmark for future profile or reconstruction results. The already known lower endpoint alone would not justify acceptance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
