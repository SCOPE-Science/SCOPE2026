---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Four-capped Hamming distance is a translation-invariant metric on (Z/qZ)^n with q composite allowed, n>=5. The unnormalized q-ary Krawtchouk shell sum gives the exact nontrivial eigenvalue lambda_k(p)=-4^p+(1-4^p)K1+(2^p-4^p)K2+(3^p-4^p)K3. I separately summed finite-group character eigenvalues for q=3 and 4, n=5 and p=1/2 and recovered this formula for all nontrivial k. For q/n→c>0, the source supplies uniform-in-codimension inequalities making K1,K2,K3 nonnegative for all sufficiently large codimensions, hence only finitely many s=n-k matter; fixed s gives K3/n^3→P_c(s) and the sharp beta*n^3 limit. The exact polynomial factor and discriminant establish transition c=1/2 (minimizers 0,4,5 at equality), while the strict gap for c<1/2 and positive full-weight root derivative prove eventual sole null k=n and q-independent root. Fixed q uses uniform cubic K3/n^3, and fixed n with q→infinity isolates s=2 and beta~1/(q^2((n-2)ln(4/3)-ln2)). Independent symbolic P_c checks at c=1/3,1/2,3/5,1,2 agreed. Endpoint n=4 is ordinary Hamming beta=1. The source does not claim exact all-finite-parameter roots or tie-breaking at c=1/2.

## originality

PASS

PASS on bounded full-text comparisons: Brouwer–Cioabă–Ihringer–McGinnis 2018 proves the q-ary Krawtchouk eigenmatrix and large-q smallest eigenvalues of individual Hamming distance-j relation graphs; its Proposition 2.6 indeed predicts k=n-2 for pure degree-three shell, but not the powered sum of degrees 1–3 with logarithmic coefficients nor c=1/2 competition. Sánchez 2011 gives general finite-space negative-type thresholds, and Dominici 2005 supplies Charlier-limit techniques. Related previously published Boolean four-cap and nonbinary three-cap results address different parameter regions/metrics and do not imply this mixed q/n phase transition or fixed-n q^2 law. No stronger equivalent four-capped q-ary theorem was found in actual bounded searches. Priority remains a best-of-knowledge judgment.

## value

PASS

Hilbert/snowflake embeddability of a natural saturated categorical Hamming metric is a motivated sharp spectral question. Three incompatible q,n growth regimes and a genuine transition at q/n=1/2 with exact stabilization of null harmonic layer give structural information not reducible to a routine calculation or selected small examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
