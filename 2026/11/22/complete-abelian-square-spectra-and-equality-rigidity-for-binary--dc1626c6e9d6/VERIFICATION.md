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

A factor must have 0, 2 or 4 ones. With 0 ones the even zero-runs contribute floor(M/2) distinct words. With 2 ones the disjoint cases are 11, flanked square 0^x110^x for 1<=x<=min(a,b) (the triple cluster cannot supply both flanks), and 10^b1 for even b. With 4 ones, two from each cluster forces 0^x11 0^b11 with x<=min(a,b) and x congruent to b mod 2 so a midpoint separates the clusters. One from the first and three from the second forces 10^b1110^b, present iff c>=b. All are literal factor contents, not occurrence or Parikh counts. For t=n-5 and m=min(a,b)>=1, t<=2M+m and the difference between the lower bound M/2+1/2+3m/2 and (2M+m+6)/4 is 5m/4-1>0. When m=0, a=0; even b gives at least floor(M/2)+3>floor((2M+6)/4), and odd b<c gives floor(c/2)+2>floor((2c+5)/4). For odd b with c<=b, equality with floor((t+6)/4) is equivalent to 0<=b-c<=4, including c=b separately where the extra factor raises the count by one. Equivalently the admissible odd b are in [t/2,(t+4)/2] with b<=t. For odd t there is exactly one, and for even t there are two iff t/2 is odd and t>=6; t=2 has only b=1. This proves the claimed existence and multiplicities and includes n=6. Reversing preserves the set sizes. The algebraic proof is all-parameter; the uploaded verification reports 8,820 direct factor tests and minimization via the formula at lengths 6..300, inspected but not rerun. No unrestricted five-one minimum follows.

## originality

PASS

Pass for the genuine five-run extension and the resulting sharp classification across the full specified family. Credit prior exact positive four-run censuses and minima, which already cover both positive four-run boundary faces, and the primary effective-word construction, which already supplies an attaining word when there are at least four zeros. Neither covers all parameters here or excludes a better or tied solution among the five-run interior.

## value

PASS

The effective four-run witness motivates exactly this extension: adding a left outer zero-run to the two-plus-three witness, while moving the same total zero count among gaps, is a natural family around a known low-count construction. The all-parameter literal census and strict cost of opening both outer gaps show why that extension produces no improvement or additional extremizers. The novel value is this rigidity in the larger family, not reproducing the four-run numerical minimum or suggesting an unrestricted result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
