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

For the prefix ending at zero-based index j, overlap-freeness reduces curling number to detection of a square suffix. Brown et al.'s Theorem 4.1 and Lemma 4.2 supply the four base squares and exact morphism alignment. The unscaled squares start odd and end even; the scaled ones start even and desubstitute at every odd endpoint, giving U(2m+1)=U(m). At 2m the length-two condition is t_(m-1) != t_m. The length-six window is (1-a,b,1-b,c,1-c,d), where (a,b,c,d) are the four desubstituted letters ending at m; period three is equivalent to a=b != c=d. This is disjoint from the length-two condition and is absent for m<3. Thus 1+Q(M)-J(M) counts square-free suffix endpoints of even index among the first M such endpoints, where Q counts equal adjacent letters and J counts 0011 or 1100 in the length-M word. For complete dyadic blocks Q_s=2^(s-1)-1-Q_(s-1). The factors counted by J_s correspond to alternating triples in the half word, of which there are two per equal adjacent pair in the quarter word, with both shifts fitting. Hence J_s=2Q_(s-2). Together with A(4)=3 this gives increments (2^(r-1)+10)/6 for even r and (2^(r-1)+8)/6 for odd r, proving the formula for all r>=2. Arbitrary-prefix Q obeys the even/odd halving recurrences, giving Q(M)=M/3+O(1+log M). Rounding J to a multiple of four changes it by at most three occurrences; hence J(M)=M/6+O(1+log M). After subtracting N/6, halving the endpoint sum costs O(1+log N) per step, proving the discrepancy and the limit. The uploaded script and output were inspected, not executed. An independent exhaustive square-suffix search at endpoints 0 through 255 reproduced the dyadic counts 3,5,8,12,19,31,54 for exponents 2 through 8. Replay: /workspace/branches/f8934f42-98ff-430a-b784-669e569ba607/direct_small_check.py and direct_small_check.txt in that directory.

## originality

PASS

The supported claim is the exact parity-sensitive dyadic count and quantitative arbitrary-prefix law for direct-prefix curling numbers. The frequency 1/6 is not credited as a new prediction; it was explicitly suggested in OEIS. The closest structural result classifies and counts squares by starting index in the infinite word, not suffixes constrained to lie in each prefix. The searched Resultary match is the bound result itself. The comparisons are bounded and do not establish absolute priority.

## value

PASS

The classic curling transform already motivated a concrete frequency question. Counting the square-free suffix endpoints resolves it and quantifies the discrepancy. Powers of two are the intrinsic scales of the substitution rather than an arbitrary subsequence, and the parity-dependent correction describes a precise finite-scale obstruction to exact density on those scales.

The dated certificate retains the supplied scientific assessment, sources and limitations.
