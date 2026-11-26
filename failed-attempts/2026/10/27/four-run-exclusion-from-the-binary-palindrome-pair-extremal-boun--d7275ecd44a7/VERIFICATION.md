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

Counting distinct factors by their run forms gives one empty factor, the two maximal monochromatic ranges, a union of two rectangles for 01 with the overlap subtracted, bc for 10, and ac+bd for three-run factors. All of these are palindrome pairs. For a four-run factor 0^i1^b0^c1^j a qualifying split must either use the initial zero run alone with j=b, or use a three-run first palindrome that ends precisely at the end of the third run with i=c. Their overlap contributes just once. For the bound write X=(n^2+2n)/3. In the region c<=a, b<=d the simplified product is at most (n+2)^2/4. In the opposite region, with s=b+c and t=a+d, use bc<=s^2/4 and ad>=t−1 and complete the square to get (n^2+n+10)/3. In the mixed region c<=a, b>d, set t=a+c, s=n−t and use P=1+n+st+c(t−1−c)+d(s−t−d). If s<=t the last term is at most s−t−1, giving (n^2+n+7)/3 after optimizing in t; if s>t complete both squares and use 2<=t<n/2, giving 5n^2/16+3n/4+5/4. Reversal followed by complement gives the remaining region. These bounds are <=X for n>=10, so P<L. For n=4..9 the independently enumerated maxima are 8,12,16,21,27,33, all strictly below L. The three-run count 1+max(x,z)+y+xy+yz+xz gives L in the three indicated residue classes. The independent conjugacy-based replay checked 1001 four-run words and the three-run witnesses for n=4..14.

## originality

FAIL

The exact factor formula is repeated term-for-term, and the strict four-run exclusion is covered by a stronger sharp theorem in a distinct Resultary record. The benchmark and three-run attainment are likewise covered. This is a decision about demonstrable coverage in the checked corpus, not about priority: the matching catalogue label is later and does not show that this frozen result was derived from it or lacked novelty when first obtained.

## value

FAIL

Excluding an entire run class in the Borchert–Rampersad problem is a meaningful restricted question. Here the frozen conclusion is already covered by an exact worst-case theorem and the same distinct-factor inventory. The frozen coarser upper inequalities do not provide a further structural or extremal result beyond that coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
