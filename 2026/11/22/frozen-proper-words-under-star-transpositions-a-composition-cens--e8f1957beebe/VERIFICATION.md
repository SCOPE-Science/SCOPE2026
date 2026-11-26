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

With initial letters a,b, the position-1 swap is legal exactly when position 2 is not a, so a frozen word starts aba. At any other position only changing the first position and inserting a at its destination can break properness. A letter different from a,b is therefore immovable exactly when it touches an a, including at the right boundary where only one neighbor exists. Between consecutive a's only the two boundary letters can avoid this constraint; interior letters must all be b. This yields blocks of one or two proper non-a letters or a length-three c-b-d block with c,d outside {a,b}; the only length-two tail is c-b and any longer tail would force adjacent b's. Cutting at the a's is unique, so the prefix, geometric block series and tail multiply without overcounting. On equal indeterminates, their weights give the quartic denominator and the common factor (1+z); the cubic recurrence is primitive and its characteristic polynomial evaluates negatively at 1 and positively at q−1 (there it equals (q−2)^3). Thus the positive growth root is strictly below the unrestricted proper-word growth. For k occurrences of a, the maximum length is 3+4(k−2)+2, achieved by aba(cbca)^(k−2)cb. This excludes equal frequencies for q≥4 and the ternary m≤2 cases. Independently, a balanced ternary word with m≥2 needs m−1 further b's after aba; hence every one of its m−2 blocks and its tail contains exactly one b. Each block has two independent optional c slots around its b and the tail has one before its b. Choosing m of these 2m−3 slots and the six ordered initial letter pairs gives exactly 6 binomial(2m−3,m), positive iff m≥3. This verifies the threshold without finite extrapolation. The supplied script was inspected, not executed; the all-length proof is analytic.

## originality

PASS

The distinct result is the composition-refined frozen census for the combination of a proper linear word domain and first-position star swaps, including the exact balanced ternary count. The nearest indexed records and literature cover a different move, a different domain, or both.

## value

PASS

Isolated vertices obstruct any spanning Gray code on a nontrivial proper-word composition class, so the exact population by content is a natural invariant of the constrained generation problem. The all-composition grammar explains the sharp frequency barrier and the difference between balanced ternary and balanced larger alphabets; it gives actual counts, not just examples of failure. Absence of isolated vertices alone implies neither connectivity nor a Gray code.

The dated certificate retains the supplied scientific assessment, sources and limitations.
