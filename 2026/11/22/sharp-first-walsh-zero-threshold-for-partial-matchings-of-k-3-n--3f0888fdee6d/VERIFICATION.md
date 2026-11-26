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

The total number of partial matchings is N=n^3+2n+1 by choosing occupied rows and injecting them into columns. A specified edge occurs in Q=n^2-n+1 matchings because its endpoints leave K_{2,n-1}. The number of matchings with odd intersection with S is at most |S|Q, proving W>=N-2|S|Q. This is at least 2n for |S|<=r=(n+1)/2 when n is odd. If n is even, every multiplier has the parity of the odd N and cannot vanish. An r-edge row star attains the union bound since a matching uses at most one edge in that row. Appending an edge in another row but a selected column flips exactly those matching contributions containing the new edge. In the residual board K_{2,n-1}, omitting the star row has n completions, and using it has signed column sum (n-1)-2(r-1)=0 with the same number of remaining completions per chosen column. Thus the new support has W=2n-2n=0. When n>=3, r>=2 distinguishes the heavy row, so the 3 choices of heavy row, binomial(n,r) column selections, 2 extra rows and r extra-edge columns give distinct supports. This proves a lower bound on multiplicity, not a classification. Counting convolution has these unnormalized multipliers on the full Boolean edge group, so invertibility and injectivity statements follow. Both frozen verifiers and reported results were inspected, not executed. A separate direct signed-count run (python3 /workspace/review_checks.py 3) exhausts frequencies at n=3,4,5 (36 first zeros, none, and 270 first zeros, respectively), and checks selected boundary stars and their extensions through n=25. The proof, not these finite tests, covers all widths.

## originality

PASS

The earlier same-operator finding 5bf177d89df5 covers the even/odd global singularity split and establishes full-spectrum minimum positive magnitudes and zero family counts. These overlap and should be credited rather than presented as a discovery here. The distinct contribution supported by the available statements is the sharp odd-width bound at bounded frequency weight, exact first-zero degree, and its explicit multiplicity bound at that degree. The available stronger global spectral statements are not bounds in frequency weight.

## value

PASS

The precise first lost degree is a motivated recovery boundary for the natural all-matchings model, not merely the already known singularity parity. The positive margin 2n and a uniform family of lost modes together distinguish low-frequency recovery from the full spectrum across all odd widths. The count is not the total number of lost modes or an exact minimum-degree census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
