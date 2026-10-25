---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Correct for q>=2, n>=1 in the exactly-one-symbol tandem-duplication model. Duplication preserves the run-root and raises one run-excess coordinate; a common output of different parents forces one legal unit transfer. Any clique of size s>=3 in the fixed nonnegative integer-composition layer is either b+e_i or c-e_i, uniquely by coordinatewise extrema; only the lower form has one common output. Stars-and-bars over q(q-1)^{r-1} roots gives K_up=q sum_{r=s}^n (q-1)^{r-1} binom(r,s)binom(n-2,r-1) and K_low=q sum_{r=s}^n (q-1)^{r-1}binom(r,s)binom(n-s,r-1). Binomial differentiation yields the triple closed form and q/(q+1) limit; max clique n-1 for n>=3 vs parent-set bound floor((n+1)/2). Direct letter-level independent q-ary enumeration reproduced (q,n,K_up,K_low)=(2,5,14,2),(2,6,64,14),(3,4,12,0). The infinite conclusion is proved by the graph/composition lemma, not these checks.

## originality

FAIL

FAIL: Brouwer et al. arXiv:1408.5615v1 Lemma 8.1 supplies a strictly broader exact classification of the fixed-sum composition clique geometries; the established exact-one tandem duplication run-excess transfer correspondence restricts it to the two claimed shapes, and weak-composition enumeration immediately supplies the advertised counts. Core structure is a corollary, notwithstanding nonmatching titles and unprinted q-ary numbers.

## value

FAIL

FAIL: The higher-clique classification is a direct unit-step specialization of Brouwer et al. 2014 Lemma 8.1 in simplicial rook graphs; the tandem-duplication-to-run-coordinate and pairwise common-output framework is already known. The advertised two enumerators and asymptotics are mechanical stars-and-bars/binomial sums and do not supply a further motivated structural gap beyond this covered classification. Pairwise-vs-common-read remains an interesting pedagogical illustration but lacks independently research-valuable new content under the natural-invariant/non-implied test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
