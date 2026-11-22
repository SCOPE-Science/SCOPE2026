---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For the n-ball birth-death observable transition E_n, the layer-cake/coarea identity and constant preservation make the exact unweighted complete-pair Gini seminorm the maximum over all indicator cuts. If a cut has s<= (n+1)/2 occupied states and b in {0,1,2} endpoints, the output mass is M=s+(2s-(n+1)b)/n and pairwise difference is at most M(n+1-M). For s>=2 this yields 1+2(n-2)/n^2. Single interior columns have precisely two nonzero entries at j-1,j+1; exact pairwise differences give [(n-1)(n+2)+|n-2j|]/n^2, attained at j=1,n-1. End columns give 1/n, and direct n=1,2 checks give norm one. Maximizing 2(n-2)/n^2 over integer n>=3 gives 1/4 at n=4. Independent complete cut scans n=1..9 returned exactly 1,1,11/9,5/4,31/25,11/9,59/49,19/16,95/81. This is one step on unweighted count states, not the binomial-weighted chain norm or all powers.

## originality

PASS

The classical Ehrenfest two-urn count Markov operator, mixing/Krawtchouk spectrum and binomial-reversible measure are established, but the inspected Mizukawa primary material compares distributional total variation and group representation; it does not state the unweighted complete-pair observable Gini norm. The result sharpens the abstract cut reduction by a model-specific endpoint-mass inequality and identifies the exact all-n maximum and sharp witnesses, which are not obtained from the published mixing results or the binomial-weighted Jensen contraction.

## value

PASS

PASS: A complete closed-form induced Gini norm for the canonical Ehrenfest count chain is a natural missing norm invariant of a benchmark Markov process. The sharp three-ball onset, maximal amplification at four balls and contrast with binomial-equilibrium Gini contraction distinguish unequal metric weightings of a reversible chain in an exact and reusable way. This is more than a small table: the full n-dependent inequality, extremizing cuts and global envelope are proved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
