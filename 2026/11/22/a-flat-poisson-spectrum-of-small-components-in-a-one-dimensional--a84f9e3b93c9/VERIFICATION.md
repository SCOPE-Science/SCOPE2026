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

Sorting the iid points yields uniform measure on the simplex of n+1 nonnegative spacings with dimension n. A gap exceeding r disconnects all pairs across it, and otherwise adjacent points are joined; only the n−1 internal spacings matter. Because the gap exceedance indicators are exchangeable, conditional on c−1 cuts each cut subset has probability 1/binom(n−1,c−1), and the ordered sizes are its positive spacings between ranks 0 and n. To count the factorial moments, mark the ordered distinct slots of each required size (a_j at size j); distinct sizes cannot share a slot, so there are (c)_A marked injections, each with J(n−S,c−A) completions. This proves the identity also when c=n, A=c, A=0, or the requested marks are infeasible. At c~a√n the ratio is (c)_A(c−1)_A(n−c)_(S−A)/(n−1)_S→a^(2A). All moments of the total of the K selected counts are bounded at any fixed order, by expansion in the mixed factorial moments; this gives tightness and uniform integrability of each fixed mixed moment along subsequences. The product-Poisson law is moment determinate, giving the conditional joint limit. Translating specified simplex coordinates by r gives P(D_i>r all i in a given t-set)=(1−tr)_+^n. For t=1,2 this gives the claimed mean and negative pair-covariance variance bound, and L² convergence of C_n/√n to e^(−x/2). For every bounded continuous test function the deterministic conditional limit is uniform over feasible c in any shrinking rescaled neighborhood of this limit (otherwise select a violating sequence). Choose a shrinking neighborhood whose probability tends to one to decondition. The mean assertion follows separately: for n>j and c≥2 the conditional mean is c(c−1)/(n−1) times (n−c)_(j−1)/(n−2)_(j−1), at most the first factor and asymptotically equal to it in probability; if c=1 the mean is zero for n>j. The bound in the asymptotic proof is used only for n>j, not for j=n,c=1. L² convergence of the rescaled C_n gives L¹ convergence of its square and uniform integrability of the bound. The packaged check was inspected as finite evidence; all claims above follow by the analytic reconstruction.

## originality

PASS

Best of knowledge, confined to the joint equal-intensity fixed-cardinality spectrum and its quantitative conditional calibration. Han–Makowski already gives the exact simplex cut machinery and stronger estimates of the number of cuts alone, from which the concentration assertion follows. Godehardt–Jaworski provides same-model precedence at least for Poisson approximation of the isolated count, as indicated by the abstract. The conditional uniform composition is an immediate classical symmetry consequence. None of the comparably relevant accessible statements or broader inspected results establishes or directly specializes to the joint census of every fixed finite set of component cardinalities at the isolation window. Historical priority for that distinction remains qualified by the unavailable full text of Godehardt–Jaworski and older discrete allocation work.

## value

PASS

At the natural isolation scale, knowing either that isolated vertices have a Poisson count or that the total number is of order √n leaves the fragment-size profile undetermined. The equal intensity for every fixed size and their joint independence quantify that profile, while exact conditional moments supply finite-radius calibration. The value is the joint structure rather than rederiving the known isolated-node marginal or proving another connectivity threshold; it does not extend to growing K or nonuniform positions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
