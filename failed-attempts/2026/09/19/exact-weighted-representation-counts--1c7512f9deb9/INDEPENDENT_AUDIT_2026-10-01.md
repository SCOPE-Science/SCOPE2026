# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260919-1c7512f9deb9`

## Correctness — PASS

The multivariate local limit is correct. Li--Xu--Yan's full primary proof gives the exact finite boundary system and unique tail recurrence. With Bernoulli variables the count is exactly \(2^{T+k}\Pr\{S_T=\mu_T-c(T)\}\). The normalized Gram matrix tends to \(G_k=k^{-1}I+(k+2)k^{-2}J\), and linearly many standard-basis columns force full lattice span and exponential decay away from the origin. Scaling Fourier inversion by \(T^{-1/2}\) gives covariance \(G_k/4\), determinant \((k+3)/k^k\), exponent \(-2\lambda^TG_k^{-1}\lambda\), and the displayed constant. The assigned dynamic program correctly checks scalar instances but is not needed for the vector theorem.

### Correctness sources

- assigned RESULT.md
- artifacts/verify_counts.py
- Li--Xu--Yan arXiv:2609.20385 full text
- two earlier 2026-09-18 SCOPE local-limit theorems

### Correctness risks

- The theorem keeps \(k\) fixed and does not cover larger-than-diffusive deviations.

## Originality — FAIL

Two earlier 2026-09-18 published SCOPE records already prove the same leading constant, fixed-offset asymptotic, scalar diffusive Gaussian profile, \(f_k/f_\ell\) ratio, and the Yan--Shan corollary. More decisively, the earlier exact-local-limit proof already performs the full \(k\)-dimensional Fourier local-limit analysis with the identical covariance matrix. Replacing its target vector \(2c_T\mathbf 1\) by an arbitrary integer vector with \(c(T)/\sqrt T	o\lambda\) changes only the Fourier phase and yields the present exponent mechanically. Under the required implication rule, the residue-dependent vector extension is therefore a direct corollary of an already published multivariate proof.

### equivalent_formulations

Searches:
- Resultary semantic search for weighted-representation local limits and Gaussian profiles
- direct comparison with 2026/09/18 exact-local-limit and exact-asymptotic SCOPE records

Evidence:
- Both earlier records contain the identical scalar constant and Gaussian profile.
- The exact-local-limit proof already has the full matrix \(G_k\) and multidimensional Fourier inversion.

Reasoning:
The current vector statement is the same local CLT evaluated at a general diffusive target vector.

### broader_coverage

Searches:
- 2026/09/18/exact-local-limit-weighted-representation-counts--4e870c1cf2eb
- 2026/09/18/exact-asymptotic-weighted-representation-partitions--fb5b8dfd89f0
- Li--Xu--Yan arXiv:2609.20385

Evidence:
- The first earlier SCOPE result supplies the strongest covering proof mechanism; the second independently duplicates the scalar theorem and \(g_{k,m}\) corollary.
- Li--Xu--Yan supplies only order bounds, not the local-limit constant.

Reasoning:
Current coverage is broader in proof machinery than the printed scalar statement because its Fourier argument already handles arbitrary target phases.

### exact_database_or_table

Searches:
- published SCOPE weighted-representation findings
- Yang--Chen/Li--Xu--Yan counting literature

Evidence:
- The exact constants are already present in two published records, so this is not a missing table value.

Reasoning:
The originality failure is theorem implication, not a database lookup.

### claim_vs_prior_implication

Searches:
- phase replacement in the earlier multidimensional Fourier integral

Evidence:
- The earlier integrand has phase \(e^{-i(2c_T\mathbf1)\cdot	heta}\); replacing it by \(e^{-i(2c(T))\cdot	heta}\) leaves all covariance, major-arc, domination, and lattice arguments unchanged.

Reasoning:
That single substitution produces exactly \(\exp(-2\lambda^TG_k^{-1}\lambda)\), so the only nominal extension is mechanically implied.

### source_inspections

- **Exact local-limit asymptotics for weighted representation partitions** — 2026/09/18/exact-local-limit-weighted-representation-counts--4e870c1cf2eb. Trigger: Earlier semantic match with the same constant and local limit. Material read: Complete RESULT.md at the audited repository snapshot. Method: Full proof implication comparison. Assessment: DECISIVE PRIOR COVERAGE of the scalar theorem and the multivariate proof machinery. Evidence: It computes the same \(k\)-dimensional covariance and Fourier major arcs; only its target is restricted to the all-ones direction.
- **Exact asymptotics for eventual weighted-representation balance** — 2026/09/18/exact-asymptotic-weighted-representation-partitions--fb5b8dfd89f0. Trigger: Second earlier exact asymptotic match. Material read: Complete RESULT.md. Method: Statement/proof comparison. Assessment: Covers all principal scalar consequences and the \(g_{k,m}\) asymptotic. Evidence: It gives the identical constant and scalar diffusive factor one day earlier.
- **A problem of Yang and Chen on weighted representation functions** — https://arxiv.org/abs/2609.20385. Trigger: Primary source of the finite boundary system. Material read: Complete ten-page primary paper obtained through authorized access. Method: Full-text inspection of Lemmas 2.1--2.6 and Theorem 1.2 proof. Assessment: Provides the exact finite sign reduction and order bounds, but not the sharp local limit. Evidence: Theorem 1.2 is only \(symp 2^T/T^{k/2}\).

### checked_sources

- 2026/09/18/exact-local-limit-weighted-representation-counts--4e870c1cf2eb
- 2026/09/18/exact-asymptotic-weighted-representation-partitions--fb5b8dfd89f0
- https://arxiv.org/abs/2609.20385
- artifacts/verify_counts.py
- Resultary semantic searches

### residual_risks

- No residual originality survives the direct corollary comparison.

## Scientific value — FAIL

A multivariate residue-dependent Gaussian profile is natural, but here it requires no new structural lemma or difficult extension beyond an earlier fully multidimensional local-limit proof: it is obtained by changing the target phase vector. The rest of the record repeats already-published constants and corollaries. Under the required value bar this is a routine substitution/generalization rather than an independently valuable new boundary.

### Value sources

- earlier exact local-limit proof
- earlier exact asymptotic theorem

### Value risks

- The mathematics is correct and may be a useful reformulation, but correctness and convenience do not establish new scientific value.

## Limitations

- Correctness passes; originality and scientific value fail due decisive earlier coverage and mechanical implication.
- The original package must be preserved as failed evidence.
- The finite dynamic program is only corroboration.

## Disposition

**FAILED**
