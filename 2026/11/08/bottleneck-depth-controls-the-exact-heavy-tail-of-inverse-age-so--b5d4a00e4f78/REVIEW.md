# Review: bottleneck depth and inverse-age cascade tails

## Correctness: PASS

The claim is for a specified continuous-time finite progressive threshold process, with common physical-time intensity \(a/(t+2)\). Time change gives a homogeneous pure-birth chain with eligible-state exit rates equal to positive integers. The exact Laplace transform is an all-adoption-order sum; its pole at \(-1\) has strictly positive coefficient \(A\) and order \(b\). Rational partial-fraction inversion gives the asserted positive asymptotic and its sharp moment criterion, including divergence at the boundary. The last transient state forces \(b\ge1\). Full path/star laws follow from Erlang and independent exponential holding times, respectively. The provided standard-library verifier gives 408 exact combinatorial comparisons, 816 exact rational Laplace comparisons, and independent finite-state checks. Risks: the calculation can grow exponentially for large graphs, and the conclusion is not for the original discrete asynchronous simulation schedule.

## Originality: PASS, with residual priority uncertainty

The motivating Abella–San Miguel–Ramasco paper [arXiv:2209.05990, §§II–V and Appendix A] introduces inverse-age endogenous threshold aging and gives approximate network dynamics, not the finite-graph completion-time order expansion, sharp singleton-eligible bottleneck coefficient, or moment criterion. The alternative Richter–Henkel–Böttcher contagion [arXiv:2006.05937, §§II–VI] allows recovery and does not share the irreversible dynamics or physical-time inverse-age hazard. Established phase-type theory [Bladt–Nielsen (2017), as summarized in the ETH PhaseTypeR vignette] supplies the general finite Markov absorption matrix exponential; that generic representation is not novel and is explicitly credited. The proposed distinct claim is the model-specific positive coefficient and maximal singleton-eligibility chain rule, with graph examples that separate serial from parallel adoption. Targeted searches did not reveal a covering finite-network specialization, but a general spectral or Markov-chain treatment might implicitly recover it and remains a priority risk. This is a self-review, not independent validation.

## Value: PASS

The motivating work highlights missing exact stochastic finite-size analysis. The present result identifies not only an inverse-power completion tail but a topology-sensitive logarithmic modifier with an exact computable coefficient. A path and a star with equally many nonseeds have qualitatively different logarithmic powers, and every moment threshold depends only on the aging exponent; the infinite-mean yet almost-surely complete regime at \(a=1\) makes a practical distinction between sample average completion times and typical completion times. This is an exact finite-network benchmark for studying age-dependent social diffusion. It does not assert that exact closure-time distributions or the main result extend to heterogeneous rates, reset rules or finite discrete asynchronous experiments.

## Literature and limitations

- D. Abella, M. San Miguel, J. J. Ramasco, *Aging in binary-state models: The Threshold model for Complex Contagion*, arXiv:2209.05990, original 2022-09-13, https://arxiv.org/html/2209.05990v2.
- P. Richter, M. Henkel, L. Böttcher, *Aging and equilibration in bistable contagion dynamics*, arXiv:2006.05937, https://arxiv.org/abs/2006.05937.
- M. Bladt and B. F. Nielsen, *Matrix-Exponential Distributions in Applied Probability* (2017), via https://www.stat.ethz.ch/CRAN/web/packages/PhaseTypeR/vignettes/PhaseTypeR.html.

Self-review: passed. Independent audit: not yet performed.
