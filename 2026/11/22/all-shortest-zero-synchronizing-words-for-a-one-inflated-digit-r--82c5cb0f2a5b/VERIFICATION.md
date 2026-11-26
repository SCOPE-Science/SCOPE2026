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

For b>=3, k>=2 the carry recurrence leaves [-M,0] invariant, and the prefix digits of any complete-residue expansion are unique modulo the corresponding radix power. Thus resetting every carry to zero is equivalent to representing every integer of [A-M,A]. For k>=3 the residue prescribed by the two exceptional digits at positions k-2 and k-3 has a least possible nonnegative representative Q=(b^k-1)(b^(k-2)+b^(k-3))>b^(2k-2); an interval of M+1 integers cannot avoid that residue modulo b^(k-1). For k=2, the represented integers below b^2 are the two-digit ordinary restricted grid plus the isolated b^2-1, whose runs are too short. At length 2k-1 use the unique signed-digit block n=BV+e, -M<=e<=(b-2)M. In regular blocks the top digit -1 is impossible. Over the rest of a block the lower mask has digits 0 or 1, and membership requires V minus that mask to have digits 0 through b-2. An interior V accepts all masks; any digit b-1 excludes the zero mask and any zero digit excludes the mask concentrated on that digit. The lower signed digits repeat every b^(k-1) values, bounding runs in noninterior blocks. One endpoint detail implicit in the decomposition: at the start of the truncated final block V=b^(k-1), e=-M has all signed digits -1, so the mask E=M exceeds V and this integer is absent. That single gap prevents joining the preceding block, and this truncated block has at most M integers. Each interior run has (b-1)b^(k-1) integers, hence exactly (b-1)b^(k-1)-M admissible right endpoints. This proves the full interval and count, including b=3. An independent direct carry replay enumerated all words at lengths 2k-2 and 2k-1 for (3,2), (3,3), (4,2), (4,3), (5,2), (5,3), (6,2); no shorter candidate at the tested length reset, and the exact lists matched (counts 2, 5, 14, 108, 42, 621, 92). Zero-padding preserves zero reset. The supplied verify.py and its 32-check output were inspected, not run; finite checks do not establish the unlimited result.

## originality

PASS

Credit the earlier ternary minimum length, interval criterion, signed-digit construction and all the ternary words it constructs. The supported distinct result is necessity (no other ternary words), and a uniform minimal-length and complete interval theorem for all larger bases in the family.

## value

PASS

The family changes a single residue representative in the ordinary radix alphabet and is a natural test of shortest-length questions left open by the qualitative theory. The complete minimizing input census is a useful exact invariant, not merely the already known ternary length or a larger finite table: it shows how local borrow obstructions govern all shortest words and gives every admissible prefix value in every base in scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
