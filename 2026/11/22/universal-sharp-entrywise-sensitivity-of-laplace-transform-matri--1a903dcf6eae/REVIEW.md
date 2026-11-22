# Scientific review — Universal sharp entrywise sensitivity of Laplace-transform matrix filters

## Correctness — PASS

The theorem specifies real symmetric matrices with a fixed upper spectral edge, nonnegative finite Laplace measure with finite weighted first moment, and maximum absolute-entry norms on both inputs and outputs. The critical row lemma is proved from \(B^2\preceq B\), Cauchy–Schwarz and an exact scalar maximum. Its rank-one projection gives equality. The Duhamel identity proves the global bound for distinct endpoints without commutativity, and an interior perturbation by the all-ones matrix, followed by high spectral contrast and removal of an interior margin, gives the sharp reverse inequality. Dominated and monotone convergence hypotheses are explicitly satisfied; constant filters and dimension one are included. The proof is independent of finite tests. `CHECK.py` provided supplementary 2,100 checks; it is not an infinite certificate.

## Originality — PASS, with literature-priority risk

The closest inspected primary work is Crouzeix–Kressner (arXiv:2007.09784), whose Theorem 3.1 and Corollary 5.1 are **Frobenius/spectral-norm estimates** for matrix-function derivatives, not the entrywise maximum-norm equality on a full dissipative cone. Kandolf–Koskela–Relton–Schweitzer (arXiv:2008.12926; Wiley full text) develops approximation methods and error estimates for such derivatives, including Stieltjes functions, not the universal exact entrywise coefficient. Kandolf–Relton (2017), inspected in selected original full-text pages, concerns Krylov approximation and 2-norm conditioning. The older accessible findings on planar square roots and polar factors are neither the same map nor a dominating functional-calculus result. The theorem uses an exact positive-contraction row bound and a simultaneous rank-one limit to prove a new-looking sharp equality; a broader unindexed componentwise functional-calculus theorem might still cover it. Searches cannot establish historical uniqueness.

## Mathematical value — PASS

This is a natural sharp global robustness invariant for a large class of spectral filters used in heat evolution, shifted inverse operators and fractional inverses. The scalar boundary slope alone does **not** control componentwise matrix perturbations with a dimension-free factor: the optimal amplification is \((1+\sqrt n)^2/4\), asymptotic to \(n/4\). The result identifies a single extremizing rank-one slow eigenspace for every positive Laplace mixture and exactly characterizes the global spectral-gap dependence, not merely a sample calculation. It is substantively more informative than a generic differentiability or loose operator-norm estimate, though finite spectral-width and nonsymmetric cases remain open to separate analysis.

## Closest literature and limitations

- M. Crouzeix and D. Kressner (2020), arXiv:2007.09784, Sections 1–6 read in accessible full-text HTML; norms and sharpness objectives are distinct.
- P. Kandolf, A. Koskela, S. D. Relton and M. Schweitzer (2020), arXiv:2008.12926 / DOI 10.1002/nla.2401, relevant introduction, algorithms, bounds and conclusions inspected in open full-text HTML; not a covering result.
- P. Kandolf and S. D. Relton (2017), DOI 10.1137/16M1077969; original full-text pages 1 and 4 inspected alongside parsed introduction and methodology; selected-pages inspection does not justify an exhaustive negative claim.

The claim is finite-dimensional and restricted to real symmetric dissipative generators and nonnegative Laplace measures. Unindexed literature and translated/weighted-norm formulations are residual priority risks. Independent mathematical validation is not claimed.

Self-review: passed. Independent audit: not yet performed.
