# Scientific review

## Correctness — PASS
The two-step Kaczmarz norm-squared operator equals a positive weighted sum of the first projection matrices with coefficient \((a_i^\mathsf Ta_j)^2\). Taking the cheapest conditional second row produces a Loewner lower bound; reflecting first-row probabilities produces a diagonal matrix with two competing affine modes. Minimizing their maximum proves the full continuum formula. Equality cases require the specified conditionals, balanced leaf weights, and at \(u=1/2\) an orthogonal pair. All three boundary regimes and the exact sample comparisons were rechecked. The local standalone verifier passed 22 finite checks; it is supporting evidence only, while the analytic argument supplies the universal proof.

## Originality — PASS, qualified
A search for three-row planar joint Kaczmarz laws, two-step minimax projection coupling, independent-row alternatives, and angular thresholds found related work on independent sampling, sampled residual-greedy rules, and two-row relaxed coupling. Selected primary-paper results and methods were inspected, particularly Haddock--Ma (2019/2020) and Sun--Gu--Tang (2020); they do not state the exact unrestricted joint-law two-step result. The 2014 Agaskar--Wang--Lu exact-MSE article remains a plausible historical source whose available abstract and metadata do not settle the equivalence question. The full published public records for the most similar indexed results were not independently retrievable, and equivalent earlier formulas could exist. Absence from retrieved results is not a proof of publication priority.

## Value — PASS
The problem is the smallest symmetric overdetermined planar frame on which one can jointly design two Kaczmarz labels. Its full minimax classification is not an arbitrary isolated coefficient: the two structural changes separately control the successor row and whether the center row is included at all. At \(u=3/8\), using a locally worse pair with positive probability improves the sharp worst-direction mean-square factor from the best deterministic \(1/16\) to \(3/80\); at \(u=3/4\), correlated sampling yields \(3/16\) versus \(11/18\) for two IID uniform draws. These exact finite-horizon benchmarks clarify what independent sampling and locally most-orthogonal scheduling each overlook. No actual computational speedup is claimed.

## Scope and risks
The statement covers precisely two fixed-law unrelaxed updates, not arbitrary adaptive methods or long-run rates. The remaining originality risk is earlier exact work phrased as experimental design or projection coupling, especially inaccessible detailed parts of 2014 optimal-sampling work.

Self-review: passed. Independent audit: not yet performed.
