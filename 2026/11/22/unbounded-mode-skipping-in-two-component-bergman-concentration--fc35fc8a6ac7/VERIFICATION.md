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

Angular orthogonality and normalized radial integration with t=|z|^2 give the eigenvalue a^(n+1)+mu_n on the normalized nth monomial, where mu_n=c^(n+1)-b^(n+1); the eigenvalues are nonnegative and decay geometrically. For b=3/4,c=7/8 the sign of 2(6/7)^(n+1)-1 gives the unique shell peak n=4. Hence degrees n>=5 are strictly dominated for every a. H(a)=a-a^5 crosses the difference mu_4-mu_0=4935/32768 once before 3/4 by strict concavity, H(0)<d<H(3/4), and the rational sign changes at 3/20 and 151/1000. For n=1,2,3 the shell differences from mu_0 are 5/64, 63/512, 593/4096, each below 3/20-(3/20)^(n+1). This excludes them at the tie. Below the tie lambda_n-lambda_4 is increasing (derivative strictly positive for a>0 there, zero at a=0); above the tie lambda_0-lambda_n is concave and positive at both alpha and 3/4. For the large-M construction c/b=2^(1/(M+1/2)), so the shell peak is exactly M and the adjacent factors 2(b/c)^M-1 and 1-2(b/c)^(M+1) are each asymptotic to h_M/2. Since c^M tends to 1/2, both adjacent gaps are asymptotic to h_M^2/4, giving an eventual h_M^2/8 bound at every other index by unimodality. Also h_M is asymptotic to log(2)/M, mu_M tends to 1/4, and the crossing equation is strictly increasing on [0,1/3] for large M, giving a_M tending to 1/4. For 1<=n<J_h the eigenvalue is at most 1/9+O(h log(1/h)); for n>=J_h other than M the inner power is at most h^3, too small to close the shell gap. This gives exactly the two claimed top modes at the tie. Uniform geometric decay locally in a and the positive slope of lambda_0-lambda_M give the strict local switch, with the M-dependent annulus held fixed. The arguments can be replayed in RESULT.md lines 31–79. The bounded fraction/decimal check.py was inspected, not executed, and is not the all-index proof.

## originality

PASS

Best-of-knowledge pass for the exact unweighted Bergman disk-plus-annulus degree-4-to-0 diagram and the eventual arbitrarily remote 0-to-M top-mode ties and direct switches. General radial diagonalization, connected-annulus adjacency, and nonadjacent Fock crossing are prior or related results, not the claimed comparisons of global Bergman maxima.

## value

PASS

The maximizing degree determines both the sharp concentration norm and its optimizers. A growing central disk produces a direct change between modes with arbitrarily large index separation, although the observation mask has only two radial components. The concrete diagram gives an exact norming threshold on an entire parameter interval, and the second construction establishes a structural distinction from single-annulus behavior rather than an isolated numerical crossover.

The dated certificate retains the supplied scientific assessment, sources and limitations.
