# Independent audit — 2026-10-01

## Final claim

Equality in the weighted chromatic Kemeny bound holds exactly for degree-factorized complete multipartite graphs with equal weighted volume in every color class.

## Correctness — PASS

The classification is correct given the published weighted partition inequality and its equality criterion. Equality in the chromatic Cauchy step forces all non-Perron quotient eigenvalues to -1/(r-1). Equality in the compression bound makes the color-indicator subspace reducing and forces the orthogonal complement to zero; the trace-of-squares block calculation then gives M=SBS^T. Zero diagonal fixes equal color-class volumes, and the cross entries give w_uv=d_u d_v/((r-1)A). The converse factorization has spectrum {1, -1/(r-1)^(r-1), 0^(n-r)} and attains the bound. The singleton-part boundary r=n is handled separately and consistently.

## Originality — FAIL

The weighted classification is a direct corollary of the primary paper's general weighted partition theorem with complete equality characterization, followed by equality in Cauchy--Schwarz and elementary spectral factorization. Because the prior theorem already supplies the exact equality condition needed, the final structural formula is mechanically implied under the audit's corollary/special-case rule even though the source paper only prints the chromatic equality classification in the unweighted case.

### Equivalent formulations

Searches: Abiad et al. arXiv:2609.17481; weighted chromatic Kemeny equality; reversible-chain complete multipartite factorization

Evidence: The primary abstract explicitly says the main weighted partition theorem has complete equality characterizations and yields the chromatic bound.

Reasoning: The record specializes that equality criterion to a color partition and solves the resulting elementary spectral equations.

### Broader coverage

Searches: General partition equality theorem versus chromatic specialization

Evidence: The general theorem applies to arbitrary weighted partitions, strictly broader than proper color partitions.

Reasoning: The final theorem is a family-specific corollary of the broader prior equality theorem.

### Exact database or table

Searches: Exact weighted degree-factorized complete multipartite formula

Evidence: No independent source printing the exact formula was located.

Reasoning: Exact wording is unnecessary where the stronger theorem mechanically implies it.

### Claim versus prior implication

Searches: Primary partition equality criterion plus Cauchy equality

Evidence: Those ingredients determine the quotient spectrum and invariant subspace; the displayed weight formula then follows by reading entries.

Reasoning: This is decisive implication-level coverage.

### Source inspections

- **Kemeny's constant via matrix compression and eigenvalue interlacing** (arXiv:2609.17481): The abstract confirms the broader weighted partition theorem with complete equality characterizations and says only the final chromatic equality list is printed for unweighted graphs. Material read: Primary abstract and bibliographic material; full paper retrieval was unavailable in this run. Evidence: The paper advertises the general equality framework from which the record derives the weighted color-partition case.

Checked sources: A. Abiad et al., Kemeny's constant via matrix compression and eigenvalue interlacing, arXiv:2609.17481; Ciardo--Dahl--Kirkland bipartite Kemeny equality theory; Published-record semantic search for weighted Kemeny chromatic equality

Residual risks: The failure is based on implication from the general equality theorem, not on finding the exact displayed weight formula elsewhere.

## Scientific value — PASS

The structural parameterization is mathematically useful: it identifies stationary-mass balance as the correct weighted rigidity condition, parameterizes all equality weights, and gives a rank-one bipartite criterion. It is valuable as an explicit classification even though it is not original under the strict implication test.

## Limitations

- Finite connected undirected graphs with strictly positive present-edge weights.
- Scientific rejection is originality-only; correctness and value survive.

## Conclusion

The final claim is not accepted because all three axes must pass; the surviving correctness/value evidence is retained.
