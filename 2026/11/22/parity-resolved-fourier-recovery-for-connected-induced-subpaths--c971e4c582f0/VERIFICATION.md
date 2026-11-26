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

The operators act on labelled paths for n≥2, with parity counted in vertices and with no convolution normalization. An interval with endpoints i<j in {0,…,n} has sign ε_iε_j for the prefix signs anchored by ε_0=1. Every assignment of the other signs occurs once, since adjacent sign ratios recover the frequency. Even vertex counts use within-parity endpoint pairs, giving ((a−2j)^2+(b−2k)^2−N)/2; odd counts use cross pairs, giving (a−2j)(b−2k). The binomial factors count independent sign choices in the two classes, with only a−1 free even-index signs. Zero indicators thus give both exact nullities, summing across coincident eigenvalues; the real Walsh basis proves the rank result over either scalar field. In the even case a zero implies a sum of two squares. For the converse, mod-four residues of the squares match the parities of a,b up to swapping (none when N≡3), and each magnitude is at most sqrt(N)≤floor(N/2) for N≥6. For N=4 and 5 use (0,2) and (1,2), respectively. Take nonnegative coordinates so the excluded anchored value −a never occurs. In the odd case an even block allows sum zero, including an even anchored block of size two; both blocks are odd exactly when N≡2 mod 4. The classical sum-of-two-squares theorem gives the prime-exponent equivalence. Independent exact sums reproduced the six ranks 4,10,96,226,312,3466. The frozen code was inspected rather than executed.

## originality

PASS

The known interval sum, the Krawtchouk factors, and the unfiltered prefix-sign calculation are credited. The distinct claim is the exact paired recovery classification and nullities for the two vertex-parity restrictions. Neither the unfiltered spectrum and rank nor the general weighted-subtree and Hamming-sphere formulas state that every arithmetic resonance is reachable in the constrained blocks; the reduction and converse give the specific two-square versus modulo-four distinction. This conclusion is confined to the inspected comparisons.

## value

PASS

Vertex parity is a natural filter on connected path subsets. It produces exact, genuinely different recovery diagnostics from the same family: a prime-exponent condition for even orders, a modulus-four condition for odd orders, and neither agrees in general with the unfiltered square criterion. For example, at n=4 the unfiltered operator is invertible while both filtered operators are singular; at n=6 only the odd operator is singular. Exact sizes of the lost Walsh spaces are also available. The value is the complete arithmetic recovery distinction, not rederiving familiar hypercube polynomials or recomputing a few ranks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
