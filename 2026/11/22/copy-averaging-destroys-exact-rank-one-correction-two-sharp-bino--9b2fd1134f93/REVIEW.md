# Scientific review

## Correctness — PASS

The claim is an exact identity for a specified random two-dimensional approximate inverse. The digital correction is the orthogonal residual projector because the target is the identity. The smallest eigenvalue of the error Gram matrix is exactly the residual under optimal rank-one projection; the signed count reduction therefore has no hidden optimization assumption. In the centered case the two rotated signed-count walks are independent, yielding the exact mean of the minimum of two squares; in the one-sided case a binomial count gives the parallel exact identity. The absolute simple-walk moment is derived by a telescoping recurrence, and central-binomial Stirling asymptotics give the two limiting regimes. Direct exact-rational enumeration is supplemental only. The matrices are SPD for every permitted \(\alpha\), and all quantifiers, endpoint \(D=1\), strict positivity for \(D\ge2\), and the positive-noise bias are explicit.

## Originality — PASS, with limitations

The relevant primary article gives the residual projection identity and *already cautions* that averaging programmed copies need not monotonically improve the learned-correction residual. Those facts are credited. The assessed mathematical addition consists of the **paired closed finite-copy binomial laws and their distinct sharp limits**, including strict deterioration from one perfectly corrected copy to two. The classical Eckart–Young/Rayleigh principle and random-walk absolute moment are credited as inputs. Searches for random rank-one projection averaging, matrix-copy ensemble corrections, and exact error laws found no statement covering this combination. The closest public mathematical records concern rank-one corrections to deterministic equicorrelated kernels or stochastic rounding, not this two-regime programmed-copy risk. These searches do not prove uniqueness: equivalent unindexed or unpublished two-dimensional calculations remain possible.

## Value — PASS

The motivating hardware method explicitly trades independently programmed copies against low-dimensional digital correction. The theorem isolates a genuine conflict in that design: raw mean-square error strictly improves with more copies, yet a one-dimensional correction loses exact recoverability already at the second copy. The exact moment sequence, sharp centered decay constant, and one-sided irreducible floor distinguish transient sampling noise from persistent bias and provide a small reproducible benchmark for testing such design tradeoffs. The result is structurally motivated by rank inflation under averaging rather than an arbitrary numerical slice. No extrapolation to full solver convergence is asserted.

## Closest literature and remaining risks

The strongest comparison is Shah et al., arXiv:2611.17251v1, especially the exact residual projection formula and the copy-averaging identity in Sections 2.3 and 3.1–3.2. These formulas imply the existence of the present proof ingredients but do not state or directly imply the two exact evaluated binomial laws without a new distributional calculation. More broadly, classical best rank-one approximation and symmetric-walk moments cover the building blocks, not the coupled finite-copy risk. Search-based comparisons have incomplete coverage of uncatalogued notes and of some specialist full texts; formal independent peer evaluation has not occurred.

Self-review: passed. Independent audit: not yet performed.
