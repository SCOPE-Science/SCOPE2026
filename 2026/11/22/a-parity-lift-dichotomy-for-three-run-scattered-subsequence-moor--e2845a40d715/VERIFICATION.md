---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The target is the parity of positional embeddings after every binary prefix, including the empty input. Lucas gives P=2^(1+floor(log₂a)) as a period of f(z)=binom(z,a) mod 2. A smaller period would give a proper period dividing P, hence also period P/2, contradicted by f(a)=1 and f(a−P/2)=0. Updating the prefix counts uses only old coordinates. On phase zero, the action on the middle counters is M=I+N; shifting to phase a for the one-letter update and shifting back adds e₁ to M. The actions are finite permutations, so inverse powers are realizable by words. Composing and conjugating gives translations by M^t e₁, whose first b columns form the invertible triangular Pascal basis. Thus every base state occurs. For a≥2,b≥2, the stem 0^a1^(b−1)0^(P−a) gives B_(b−1)=1 and f(P+1)+f(P)=binom(P,a−1)=0; swapping the last two letters therefore holds the base fixed and flips C. For a=1,b≥2, with r the least power of two at least b, the displayed words have equal B_j because binom(r,j−1) vanishes for 1≤j−1<b≤r, and opposite C because binom(r−1,b) is odd for b<r and zero for b=r, while binom(r+1,b) does the reverse. For b=1,a even, the last-letter swap compares the odd binom(a+1,a) and binom(a,a) and changes C by one. Opposite lifts then propagate together by a common suffix to every base. In the exceptional case b=1,a odd, contributing one-positions see an odd number of preceding zeros by Lucas, so each final-zero factor is congruent to z−1, giving C=(z−1)B₁. Distinguishability is proved, not inferred from reachability: the empty suffix fixes C, the b+1 outputs after 1^t0 extract the middle coordinates and f(z) in triangular order, and the shifts 0^r1^b0 recover the rotation of f and thus z. The same triangular tests for B_b with the final 0 omitted distinguish base states when viewing the two-run counter by itself. No extrapolation is needed.

## originality

PASS

The audited contribution is the exact parity lift on the family with two arbitrary initial runs and last run of length one. The entire two-run base count and the alternating-triple specialization are prior or contemporaneous overlapping results; they are not credited as new here. The inspected sources do not determine the exceptional last-bit relation for arbitrary a,b. Inaccessible plausible general works are left unresolved rather than classified as noncovering.

## value

PASS

This supplies exact deterministic memory for a natural returning-letter extension of a two-run pattern. The full family classification identifies when a new output bit is genuinely independent and when a pointwise parity invariant removes it. Its Θ(a·2^b) states compared to a naive prefix bit for every pattern position, and its explicit necessary-and-sufficient boundary, describe a structural effect not captured by a list of examples. The result is limited to parity and a final run of length one.

The dated certificate retains the supplied scientific assessment, sources and limitations.
