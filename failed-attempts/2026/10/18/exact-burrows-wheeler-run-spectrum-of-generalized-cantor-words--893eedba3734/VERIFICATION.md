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

The recursion C_{b,k}=C_{b,k−1}0^{(b−2)b^{k−1}}C_{b,k−1} gives circular gap g_i=(b−2)b^{ν₂(i)} for 1≤i<2^k and g_{2^k}=0. The unique largest gap ensures distinct cyclic rotations. Descending leading-zero groups have one row per gap long enough; each row's predecessor is one exactly when the gap length equals the leading-zero count. In the group h_j=(b−2)b^j, eligible gap indices are multiples of 2^j; the gap sequence agrees through the first 2^j−1 offsets. At the next offset the nonterminal odd multiples have a longer gap, the even multiples have gap h_j, and the terminal odd multiple has the zero wrap gap. These order classes have sizes 2^{k−j−1}−1, 2^{k−j−1}−1 and 1, with predecessors 1, 0 and 1. At j=k−1 only the last class exists. Distinct special groups are separated by at least one all-zero group; the final one-start group has one 1 and, for k≥2, a zero at each end. Thus there are 2k one-runs with the stated lengths, each followed by a zero-run, and the original word has 2^{k+1}−1 runs. Direct rotation sorts confirmed examples at (b,k)=(3,2),(3,4),(5,4),(7,3), including 101010100 at (3,2) and the identical spectrum [1,1,1,3,1,7,1,1] at both tested bases at k=4. At level one the exact transform is 1 0^{b−3} 1 0, giving the stated exceptions.

## originality

FAIL

The exact indexed ternary Cantor case includes the full special-group strings and final block property, not merely the run count 4k. All the asserted statistics for general b are mechanistically transported by the strictly increasing relabeling of gap lengths 0↦0 and 3^j↦(b−2)b^j. It changes the number or widths of all-zero groups without changing the ordered special strings, their separation, or the final block. Thus the broader base quantifier does not supply independent content at the claimed run and group resolution. The comparator's displayed date is later than the frozen date; this is demonstrable mathematical coverage, not historical priority.

## value

FAIL

An exact ordered spectrum for growing nonprimitive words is intrinsically informative, and is sharper than an asymptotic count. But relative to the exact supported ternary result, the audited base extension merely changes the magnitudes of ordered gaps and the lengths of zero padding. The claimed one-run statistics already follow without new case analysis, and the record does not claim an additional nontrivial zero-run invariant or a theorem for gap families of different order type.

The dated certificate retains the supplied scientific assessment, sources and limitations.
