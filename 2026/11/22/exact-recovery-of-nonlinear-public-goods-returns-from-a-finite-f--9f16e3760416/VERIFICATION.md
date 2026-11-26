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

The frozen limitations overstate the data and calibration requirements: recovery uses only the labeled prefix, and the equations use only γ=βc, not both factors separately. Corrected RESULT.md and REVIEW.md distinguish inversion from checking a full candidate profile, state the known product and make the symmetric pair-encounter convention explicit. Rechecked the revised proof. Harmonicity and the ratio of Fermi logistic factors give successive fixation-increment ratio exp(−γL_i), so positive increments and the endpoint conditions uniquely specify the full harmonic profile. Pair a focal cooperator and defector with the same n−1 sampled slots, matching the N−2 common others and pairing the respective opposite-strategy identity. If that special identity is included, the two public benefits agree; otherwise, for k cooperators in the sampled slots, the difference divided by c is g_(k+1)−g_k with g_j=j r_j/n and g_0=0. The excluded-identity terms have denominator B=binom(N−1,n−1), and numerator weights binom(i−1,k)binom(N−i−1,n−1−k). This gives the stated payoff coefficients by Pascal cancellation and independently checks triangularity: only k≤i−1, and the k=i−1 term gives diagonal (i/n)binom(N−i−1,n−i)/B. This is positive through i=n<N, with last diagonal 1/B; the sensitivity is for normalized L_n, not the unscaled log increment ratio or estimation error. Recovered returns must be positive, and checking the remaining increment ratios is sufficient by uniqueness of the harmonic profile. At n=N the special identity is always included, so only the cost remains; geometric increments yield the return-independent profile. For the four-person example the three nonzero matrix coefficients on the diagonal are 1/9, 2/9, 1/3, with adjacent lower entries −1/9, −2/9; the payoff gaps for (18,9,9) give weights (1,1/2,1,1), verifying the nonneutral fixation profile and the equal endpoint-abundance example. The frozen verifier and its reported checks were inspected, not executed.

## originality

PASS

The generic inverse problem, Fermi increment-ratio apparatus, hypergeometric payoffs, and the forward public-goods model are prior. The distinct supported content is the explicit prefix reconstruction for the constrained return schedule, its positivity and consistency criterion, and the exact degeneracy and local sensitivity at the group-size boundary. Clarifying the product calibration does not rely on any additional novelty claim.

## value

PASS

The exact prefix criterion addresses a motivated difference between absorption data from a few labeled interior counts and aggregate endpoint abundance. It identifies the parameter range where all return values are recoverable, exhibits complete loss of that information when everyone plays in one group, and quantitatively locates the weak signal of the highest-order return even below the boundary. These are structural results for a standard finite game; they are not a claim about empirical precision or arbitrary inverse games.

The dated certificate retains the supplied scientific assessment, sources and limitations.
