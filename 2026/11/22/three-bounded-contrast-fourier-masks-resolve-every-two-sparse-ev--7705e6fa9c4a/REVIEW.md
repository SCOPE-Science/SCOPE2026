# Mathematical review

## Correctness — PASS

Correctness: Fourier inversion exactly supplies three cyclic autocorrelations. Zero-lag Hankel determinant separates 0/1/2-sparse strata; the nonantipodal ratio supplies the ordinary support sum and a quadratic recovers both support weights; the antipodal half-period chirp reads the missing imaginary phase. For two possible antipodal supports, exact factorization of distinct candidate squared chirped-lag magnitudes proves they cannot coincide. Positive weights and all phase boundary cases, including zero real product, are treated. Symbolic identity independently verified with SymPy and standard-library checker passed 3678 two-sparse cases plus 18 exact rational identities. Finite checks are supplementary, not all-N proof.

## Originality — PASS relative to inspected evidence

Originality: the closest fully inspected published Fourier statement proves two positive masks only in odd dimensions and explicitly says that its real-mask even impossibility does not rule out complex masks. Here three bounded-contrast masks, including a half-Nyquist phase-coded mask, identify every complex two-sparse vector in every even dimension uniformly, overcoming that exact missing parity case. The 2026 probabilistic full-signal O(log N)-mask PhaseLift theorem does not imply a uniform deterministic three-mask guarantee, as its own Theorem 1 notes its nonuniform fixed-signal quantifier. Older works use random many-mask or continuous-space three-mask settings. Absence of indexed matching text alone is not novelty proof; earlier unindexed equivalent special-case designs remain possible.

## Mathematical value — PASS

Value: complex two-sparse Fourier phase retrieval is the first nontrivial unknown-support phaseless recovery case. Real masks intrinsically lose the imaginary component of antipodal correlations in every even cycle; an explicit all-N fixed-cardinality, bounded-gain complex design removes that structural blind spot and supplies a completely constructive decoder. The nontrivial two-candidate weighted-moment factorization gives a meaningful guarantee rather than a routine reparametrization. No optimal count or larger-sparsity claim is made.

## Closest literature and scientific limits

Most directly related: *Sharp two-mask Fourier recovery of complex two-sparse signals on odd cycles*, full theorem and limitations; G. Huang and S. Li, arXiv:2608.02450, Theorem 1 and its nonuniform-guarantee remark; H. Li and S. Li, DOI:10.3934/ipi.2021028, abstract and mask comparison table; P. Jaming and M. Rathmair, arXiv:2205.08753, continuous-domain theorem and finite-dimensional undersampling warning. The primary result is limited to even cyclic sizes and the two-sparse class. The closest older journal and continuous-space manuscripts were not fully inspected and an equivalent unindexed two-sparse construction could exist. These are bibliographic risks, not independent mathematical review.

Self-review: passed. Independent audit: not yet performed.
