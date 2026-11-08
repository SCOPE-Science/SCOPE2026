# Self-review

## Correctness — PASS

The proof starts from the actual two-row Gaussian sketch of the symmetric three-dimensional input, derives the bivariate Cauchy law for the oblique coefficient vector, and transforms the two-by-two characteristic discriminant into a three-variable Gaussian quadratic form. Every principal two-minor of its symmetric coefficient matrix vanishes, forcing the two positive and one negative eigenvalues to obey the identity \(u+v=1\). A sharp Gaussian ellipse-to-disk rearrangement then proves \(1-\sqrt{2/3}\), with equality only for coincident positive quadratic-form eigenvalues. A determinant comparison and exact AM–GM equality characterize the residual couplings; the displayed SPD example attains the maximum. All degeneracies and quantifiers are treated. The source-code checker reproduces exact rational identities and numerical consistency checks, but those are not substitutes for the proof.

## Originality — PASS, qualified

The sharp universal nonreal-pair probability, its equality configurations, and the entire finite-case probability integral for the minimally sketched symmetric Rayleigh–Ritz matrix were compared with the inspected relevant primary literature, published research search records and accessible historical claim summaries. Nakatsukasa–Tropp (2024, §6.8) and Liu–Liu (2026, method and introduction) identify complex-valued sRR Ritz estimates but do not establish the sharp three-dimensional Gaussian probability within the material inspected. Relevant historical claims instead concern one-dimensional ratios or a different higher-dimensional repeated-Ritz-value limit. Kozhan's non-Hermitian perturbation distribution is not an sRR Gaussian pencil. Remaining risks include an inaccessible portion of the Liu–Liu article and earlier specialized small-matrix probability identities. No failed search is considered proof of unique priority.

## Value — PASS

Unexpected nonreal Ritz eigenvalues from symmetric data are an explicitly identified algorithmic difficulty in real-arithmetic sketched eigensolvers. The exact \(18.35\%\) worst-case benchmark, its conditions for attainability even by SPD matrices, and its explicit smaller-case probability integral give a calibrated failure-mode benchmark for a minimally oversampled sketch. The quantified event concerns nonreal pairs, not eigenvalue-accuracy or stability of a full solver; that distinction is essential.

## Limitations and closest literature

Only fixed independent search planes, three-dimensional symmetric matrices and exactly two Gaussian sketch rows are covered. Repeated ordinary Ritz values and either zero off-plane coupling yield zero probability. Relevant comparisons are Liu and Liu (arXiv:2610.22261v1, 2026), Nakatsukasa and Tropp (DOI 10.1137/23M1565413, §6.8, 2024), and Kozhan (DOI 10.1007/s10955-017-1792-0, 2017). The relevant main methodological portions of Liu–Liu were read in accessible HTML, but some other sections were inaccessible, leaving a qualified residual literature risk.

Self-review: passed. Independent audit: not yet performed.
