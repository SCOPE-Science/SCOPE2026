---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and limitations

Execute `python3 check_interval.py` using Python 3 (standard library only). The exact checker enumerates every permutation of \(2n\) labelled endpoints for \(n=2,3,4\), giving 24, 720, and 40,320 orderings. For each, it compares the maximal interval coverage against an independent brute-force clique scan, and it verifies five finite rational moment identities for each size, i.e. 15 identities in total. Rational averaging over the binomial number of endpoints below \(1/2\) accounts exactly for midpoint coverage after conditioning on ranks.

The projection integrals were also calculated symbolically using the density \(2\mathbf1\{0\le l\le r\le1\}\): \(\mathbb Eh=2/3\), \(\mathbb Eh^2=22/45\), and \(\mathbb E[Zh]=5/12\). The analytic proof, not finite enumeration or a numerical experiment, establishes the convergence for arbitrary \(n\). The bound controlling the random maximum uses DKW, Bernstein's inequality, and a binomial occupancy union bound. No external or independent audit has been performed.
