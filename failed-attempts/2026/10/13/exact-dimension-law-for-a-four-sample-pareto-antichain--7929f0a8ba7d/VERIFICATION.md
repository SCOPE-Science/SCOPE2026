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

Independent atomless coordinate marginals and i.i.d. observations give independent uniform strict permutations of the four labels. After fixing the first permutation, incomparability of each pair is equivalent to its reversal in at least one of the remaining d−1 orders. For a subset S of the six pairs, the probability that none of its pairs ever reverses is (e(S)/24)^(d−1), where e(S) counts permutations respecting S. Inclusion–exclusion then gives the claimed law. The independent bounded reproduction `python3 /workspace/checks/finite.py 1` calculated e(S) for all 64 subsets by a predecessor-set recurrence on four vertices, reproducing the signed sums 1,−5,1,8,−6,1 at e=4,5,6,8,12,24, and zero at e=1,2,3. A separate intersection-of-unanimous-pairs count agreed through dimension 12; the finite coefficient computation plus inclusion–exclusion is exact for all d. At d=1 no pair reverses and the probability is zero. In the independent permutation coupling the event is increasing, and strict increase has a witness of positive probability when the first d orders coincide and the next is their reverse. The exact values 151/576<1/2 and 7207/13824>1/2 settle the threshold. In the complement the two largest bases are 1/2 and 1/3, and all remaining bases are at most 1/4, giving the stated asymptotic.

## originality

FAIL

Barndorff-Nielsen and Sobel (1966) already treat i.i.d. vectors with independent coordinates whose distribution functions are continuous; this is the same atomless product-marginal scope, not just a uniform-cube case. Their exact maxima-count distribution in §3.2, Eq. (3.30), has an explicit table for n=2,3,4,5 and arbitrary d≥2. The n=4, a=4 entry is exactly the probability that all four are maximal, equivalently the antichain probability. This is prior exact coverage, not inference from a similar title. The trivial d=1 endpoint, elementary dimension coupling, numerical half-threshold and two leading exponential terms do not supply a distinct substantial law.

## value

FAIL

The four-point probability is a natural exact invariant, but the prior table already solves it for arbitrary dimension under the same marginals. The half-threshold is an elementary specialization of that law plus monotonicity, and the asymptotic is read off from the largest bases. Recomputing the known cell and naming these immediate consequences does not establish a worthwhile distinct result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
