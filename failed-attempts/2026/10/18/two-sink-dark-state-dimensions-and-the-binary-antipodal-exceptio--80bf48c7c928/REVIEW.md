# Independent mathematical audit

## correctness

PASS

The local coordinate idempotents J/q and I−J/q give the weight-k projector by tensor products; its kernel is q^(−n) times the coefficient of z^k in (1+(q−1)z)^(n−d)(1−z)^d. The two-trap layer has diagonal Gram entries m_k/q^n and off-diagonal K_k(d)/q^n. Equivalently K_k(d)/m_k is E[(−1/(q−1))^H], where H is the number of differing coordinates met by a uniform k-subset. For q≥3 and k≥1, H≥1 with positive probability, so the absolute value is strictly below one. For q=2, the support of H is a consecutive integer interval: it is a singleton for antipodes and for k=0,n, and contains both parities for nonantipodes and 0<k<n. These tests give exactly the three ranks, with n=1 covered. Inverting the two-column Gram matrix, or projecting onto one normalized column when rank one, gives exactly the localized law. Both adjacency and losses reduce B and its orthogonal complement. Imaginary parts of eigenvalues on B are negative, since a real eigenvalue would require both trap overlaps zero and hence an adjacency eigenvector in the dark complement. Jordan factors decay on B, while the complement evolves unitarily. Thus rate independence, the trace/q^n formula for a mixed input, and the example conditioning on nontrap sites follow. VERIFICATION.md and check_hamming.py were inspected, not executed. The recorded 174 rank, 6366 site-projector and 12 dynamical comparisons are bounded numerical evidence; the calculation above does not require extrapolating from them.

## originality

FAIL

The frozen novelty statement credits only binary antipodal redundancy as known, then claims the combined all-distance, all-alphabet classification and source law. A distinct earlier indexed finding already establishes the entire nontrivial binary portion in the identical dissipative model, including nonantipodal rank and source-resolved survival. The nonbinary part is a real change of alphabet, but the decisive inequality is a direct strict bound in the standard normalized Krawtchouk kernel, and the source law is the same two-column projection rule. A separate later indexed finding explicitly states the same nonbinary rank and localized formula for all dimensions ≥3 and proves a further complete-capture characterization there. That is equivalent coverage, not evidence of earlier nonbinary priority. The elementary omitted dimensions and juxtaposing the two laws do not establish a distinct contribution at the frozen scope. The finding is mathematically correct; the failure is not based on unavailable literature or a claim that all nonbinary cases were published earlier.

## value

FAIL

Loss-rate-independent rank and site-resolved probabilities are motivated quantities. The full nontrivial binary answer is already available, however, and the all-alphabet synthesis adds no new observable or structural mechanism to the same two-vector projection calculation. Against the exact matching nonbinary result, the residual dimension-one and dimension-two inclusion is simply the same projector bound with smaller tensor products; no independent scientific need for that narrow remainder is established. This is not a judgment that the coherent-loss problem itself lacks value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
