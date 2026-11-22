# Scientific assessment

## Correctness — PASS

The claim is an exact all-order 2-adic statement about the Walsh transform of the count of mappings by their vacant image sets. Inclusion-exclusion converts the character sum to \(\sum_{j=0}^k\binom kj(-2)^j(n-j)^n\). For even orders \(n\ge4\), the \(j=1\) term has valuation \(1+\nu_2(k)\), while every other term has strictly larger valuation, using the identity \(j\binom kj=k\binom{k-1}{j-1}\) and the evenness of \(n-j\) for even \(j\). For odd orders the constant term is odd. The exceptional case is checked directly. Character diagonalization then proves all stated rank, multiplicity and determinant consequences. Direct map enumeration and exact arithmetic in `verify.py` pass 15,137 assertions. The finite tests are corroborative, not the basis of the general proof.

## Originality — PASS under bounded comparison

The vacancy-count distribution itself is established occupancy theory; it is not claimed as novel. Soria's 1996 image-point seminar, Hwang–Janson's 2006 finite-urn model and Bogachev–Gnedin–Yakubovich's 2006 occupancy analysis address counting and distributional questions. The publicly published joint-law and pruning results for zero-indegree vertices actually supply the factorial moments and hence, by transform, the raw character-sum formula; they are explicitly credited. The present assessment is limited to the 2-adic valuation, nonvanishing and exact determinant laws, which the inspected statements do not cover. A prior unindexed or implicit signed-arithmetic evaluation remains a historical-priority risk. The search was semantic and finite; absence of a matching record does not certify priority.

## Value — PASS

The kernel is a canonical finite-group encoding of the occupancy set of a uniform self-map. Its complete integer Fourier spectrum has a structured dyadic stratification and is invertible over characteristic zero at every size except one; this cannot be inferred from the distribution's ordinary occupancy variance or marginal asymptotics. The theorem gives exact nullity, all spectral 2-adic multiplicities and determinant divisibility in a single infinite-family classification. No downstream or general-prime result is claimed.

## Limits and evidence

The classification uses uniform independent target choices and square domain/target size. It does not determine spectral signs or ordinary condition numbers, and no independent external scientific validation is claimed. Exact checks cover all maps through six vertices and all degree multipliers through order 120. The preceding literature and the two published mapping results are the closest sources; historical priority beyond inspected material remains unresolved.

Self-review: passed. Independent audit: not yet performed.
