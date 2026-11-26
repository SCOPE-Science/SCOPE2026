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

The contracted weighted Cayley count gives n^(−e)∏s_i for any prescribed forest and zero for a cycle. The weighted Laplacian edge-count generating function gives Bin(k−1,k/n), also valid at k=1 and k=n. The comparison binomial has the same mean; the sum of the two Poisson approximation costs is [k²(k−1)+2k(k−1)]/n². Given the coupled counts, draw matching flags with the correct conditional probabilities in each model; when both flags indicate matchings and counts agree, permutation invariance permits the same uniformly chosen matching. The wedge costs are at most (9+12) binom(k,3)/n². For ordered distinct wedge tuples the leading vertex-disjoint count is (k)_(3r)/2^r, with inclusion probabilities (3/n²)^r and (4/n²)^r. Each connected overlap component has e≥3 edges and v≤e+1, giving order n^((2−e)/3) or smaller; isolated wedge components contribute bounded factors. Thus every fixed factorial moment converges to its Poisson counterpart, giving the claimed matching-event liminf. At k=⌊b√n⌋ the TV error is O_b(n^(−1/2)); the Bernoulli point-process Laplace functional is a Riemann sum with intensity 2 on the triangle. Ties at the first later endpoint imply a wedge, negligible in any such bounded prefix; tail control comes from the exact no-edge probability, and the first-point density is intensity times the void probability, 2e^(−v²). Inspection of checker.py and VERIFICATION.md corroborates the finite checks' stated scope, not a proof of the limit; neither script was executed.

## originality

PASS

The edge-count marginal and scalar onset are treated as already known. Neither the related marked-extremal result nor the closest published count/dependence results supply the whole labeled TV comparison and its unequal Poisson wedge obstruction on the critical prefix. The marked prefix result uses standard point-process transfer and is secondary to that sharp comparison.

## value

PASS

Using independent edges to replace a constrained tree prefix is a natural approximation problem, and the whole-law rather than count guarantee decides when every labeled statistic may safely use it. The differing first local collision intensities identify where that guarantee breaks, with an explicit positive critical separation and a simple observable. The marked early-edge law is a useful secondary consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
