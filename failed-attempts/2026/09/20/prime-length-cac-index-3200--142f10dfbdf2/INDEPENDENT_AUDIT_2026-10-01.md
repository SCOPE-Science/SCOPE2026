# Independent mathematical audit — 2026-10-01

## Final claim assessed

Prime-length weight-three conflict-avoiding codes through subgroup index 3200

## Correctness — PASS

PASS. The published analytic bound reduces every new case to finitely many primes \(p=1+\ell m\) with \(2^{30}<p<B(\ell)\). Recomputing the 3001--3200 range leaves exactly twenty uncovered indices and 165 candidate gap primes. A fresh independent implementation reproduced the per-index counts and the certificate SHA-256 `edbab2e80086c6b2231061e9b0e1d1c3b7590cd99690696826735ad05f16dcc7`. For every candidate, exact primitive-root/coset arithmetic finds a witness to the required twisted Fermat equation. This is an exhaustive finite verification, not an inference from sampling.

## Originality — PASS

PASS to the best of current knowledge. Hsia--Li--Sun's complete 2023 text proves the uniform consecutive range only through subgroup index 3000 and records the earlier \(p\le2^{30}\) computation. Their 2024 cyclotomic paper covers a different class of prime lengths and does not dominate the twenty four-prime-factor indices treated here. Published-record searches found no later consecutive-index extension through 3200.

### equivalent_formulations

Searches: conflict-avoiding codes prime length subgroup index 3200; twisted Fermat equation CAC index 3001 3200

Evidence: The 2023 source stops at 3000; no exact later extension was located.

Reasoning: The finite witness formulation and the CAC construction criterion are equivalent through the published subgroup/cyclotomic reduction.

### broader_coverage

Searches: Hsia Li Sun 2023 Theorem 5.1 and Theorem 5.2; Hsia Li Sun 2024 cyclotomic numbers CAC prime lengths

Evidence: Theorem 5.2 gives the consecutive range \(\ell\le3000\); the 2024 paper handles another prime-index class rather than all composite indices up to 3200.

Reasoning: No inspected theorem covers all twenty new residual indices.

### exact_database_or_table

Searches: Resultary semantic search CAC index 3200; published CAC computational ranges

Evidence: No prior table or published certificate containing these 165 witnesses was found.

Reasoning: The originality of the finite computation is plausible, but value is separately insufficient.

### claim_vs_prior_implication

Searches: 2023 full text around Theorem 5.2; 2024 prime-length cyclotomic result

Evidence: The prior method reduces the new interval to a finite verification but does not itself assert the outcomes for the 165 gap primes.

Reasoning: The finite extension is not mechanically stated by the prior theorem; exact computation is needed, so originality passes to the best of current knowledge.

## Scientific value — FAIL

FAIL. The new scientific content is a finite extension from the published cutoff 3000 to the arbitrarily chosen cutoff 3200, obtained by checking 165 residual primes with the existing method. No structural reason singles out 3200, no new analytic bound or infinite family is obtained, and the twenty exceptional indices do not form a natural complete class. Under the stated value bar, this is an unmotivated finite slice rather than a meaningful cutoff theorem.

## Source inspections

- **Certain diagonal equations and conflict-avoiding codes of prime lengths** — https://doi.org/10.1016/j.ffa.2023.102298. Material read: Primary full text around Theorems 5.1 and 5.2 and the computational reduction. Assessment: PRIOR_METHOD_AND_CUTOFF_3000. Evidence: Theorem 5.2 states the conjecture for subgroup index at most 3000; the paper records 423 checked primes in the earlier residual range.
- **Conflict-Avoiding Codes of Prime Lengths and Cyclotomic Numbers** — https://doi.org/10.1109/TIT.2024.3439714. Material read: Primary bibliographic record and abstract describing the cyclotomic-number criterion and new class of prime lengths. Assessment: RELATED_DIFFERENT_COVERAGE. Evidence: The paper supplies a different class of prime lengths rather than a consecutive all-index extension through 3200.

## Limitations and residual risks

The computation correctly extends the verified consecutive index range from 3000 to 3200, but the endpoint 3200 is an arbitrary computational cutoff rather than a natural mathematical boundary. The result relies on previously published analytic bounds and the earlier \(p\le2^{30}\) verification.

- The 2014 computational source behind the \(p\le2^{30}\) statement was not independently re-run; the 2023 primary paper explicitly records that published computational premise.
- The value rejection does not dispute the correctness or reproducibility of the finite certificate.

## Disposition

**failed**
