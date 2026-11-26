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

Given K=k, the occupied set is a uniform k-subset, so each of the m-1 tree edges has occupancy probability k(k-1)/(m(m-1)). Forest Euler gives E[C|K=k]=k(m+1-k)/m. The first three factorial moments of the vacancy count U=m-K are (m)_j*q_j, j=1,2,3. The conditional-mean identity gives J=((2E[U]-(m-1))*Var(U)+E[(U-E[U])^3])/m; expanding in q_j gives (1), and the same algebra is valid for its real extension without a probability interpretation. With two balls, K is 2 with probability (m-1)/m and E[C|K=2]-E[C|K=1]=1-2/m, which gives the stated positive value. For m>=4, the positive ordered modes a,a^2,b,ab,c have three coefficient sign changes after omitting the zero at m=4. The real t=0 and 1 zeros, positive t=2 value and negative a^t tail force and exhaust the three distinct roots. The sign-variation proof is valid for real exponents: factoring the smallest exponent and differentiating uses Rolle between consecutive roots and also before the first root if the first two coefficient signs agree. For m=3 omit the zero-base term on t>0; two sign changes are exhausted by t=1 and the root after 2. For the load limit Var(U)/m tends to z*(1-(1+lambda)*z), z=exp(-lambda), and the third central moment is O(m), yielding (3). For bounded beta at t=m*L+beta, L=log(2), 2E[U]-(m-1)=1-beta-L/2+O(1/m), Var(U)/m=(1-L)/4+O(1/m) and the third central moment divided by m is (3L^2-2L)/8+O(1/m). The last term follows by expanding the distinct-site centered moment q3-3*q1*q2+2*q1^3 to order m^-2; repeated-site terms are lower order at z=1/2. These combine to the linear expression (6) with uniform error, first trapping the unique crossing in a bounded additive window, then giving (2). An independent enumeration of 4^n allocations with component counts by flood fill for both four-vertex paths and stars gives J=0, 0.09375, 0.041015625, -0.0457763671875 for n=1,2,3,4.

## originality

PASS

The forest identity, exchangeable subset moments and uniform occupancy moments are standard ingredients. The supported distinct claim is the exact fixed-ball sign classification for all trees and its sharp finite-size displacement, not just the existence of a component enumerator or the independent-site crossing at leading load log(2). The closest exact same-day theorem has both a different graph class and a different joint occupancy law.

## value

PASS

The sign of an occupancy–fragmentation covariance reports whether samples occupying more sites tend to create or consolidate occupied components in a precise mixed-moment sense. The exact all-tree sign transition under sampling with replacement is a useful structural classification. The finite displacement is informative rather than cosmetic: it separates the actual sampling model from independent thinning even though both have the same leading threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
