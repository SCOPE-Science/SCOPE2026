---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For fixed m>=1, write a=rx, b=ry with gcd(x,y)=1 and x<y. Since gcd(x+y,xy)=1, a+b|mab iff x+y|mr, giving the exact sum E_m(X)=sum_(x<y,coprime) floor(X gcd(m,x+y)/(y(x+y))). A nonzero summand has y<sqrt(mX), so replacing floors has only O_m(X) total error. Möbius inversion converts the primitive condition into sum of reciprocal arithmetic progressions with inner sum log(2)/e+O(1/v) uniformly for e=d/gcd(d,r). Absolute convergence yields the logarithmic main term with A_d=1/zeta(2) product_(p^j||d)1/(p^(j-1)(p+1)); divisor expansion gcd(m,s)=sum_(d|m,d|s)phi(d) yields C_m=(3 log2/pi^2) product_(p^alpha||m)(1+alpha(p-1)/(p+1)). The m=1,2 constants have exact ratio 4/3. Independently enumerated direct ordered-positive pairs and coprime-parameter sum for m=1..5 and X=12,30,90; no inference to infinite asymptotic from experiments.

## originality

PASS

Best-of-knowledge PASS. Historical OEIS A362931 tabulates ordered integral-harmonic-mean pairs exactly, related by a(X)=X+2 E_2(X), so the finite counts and primitive parametrization are not newly original. Korsky 2026 harmonic-triple study has O(X log X) style bounds in a different restricted setting, not the precise unrestricted leading constant. Sawin 2026 addresses positive-density independent sets for a graph derived from these divisibility pairs, not their total edge asymptotic. No covering fixed-m Euler product / linear-error leading coefficient was found in the scientific comparisons. Sawin full text inaccessible via arxiv/OA then Oxford VPN; this creates residual historical risk, not a scientific FAIL.

## value

PASS

E_m(X) is the natural first-moment edge-count invariant of Erdős–Graham reciprocal-sum/mean divisibility graphs; its exact logarithmic mean degree and the 4/3 change between m=1 and m=2 provide useful benchmarks for extremal/independence questions without purporting to solve independence itself. The m-local Euler product and O_m(X) remainder represent a genuinely structured all-fixed-m result, not just known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
