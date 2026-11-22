# Scientific review

## Correctness — PASS

For independent stationary two-state edge refresh processes, the conditional absence transition is exactly \(1-p(1-e^{-\Delta/\log n})\). The proof establishes the exact tagged-vertex joint probability across any fixed selection of times, followed by the uniform fixed-tag asymptotic \(n^r\Pr(\text{prescribed multiple isolation events})\to\prod_i e^{-x-\operatorname{span}(S_i)}\). Finite inclusion–exclusion determines exact isolation-support marks, and joint mixed factorial moments identify independent Poisson limits for the marks. Contiguous marks match the time signatures of stationary immigration–death individuals. The connectivity consequence invokes the known classical result that a graph at \(p=(\log n+x)/n\) is very unlikely to be disconnected without isolates. The included standard-library checker passed 347 deterministic assertions; it is a consistency check, not an infinite proof.

## Originality — PASS, with historical priority risk

The directly relevant prior theorem is Lubetzky and Steif (2013), Theorem 3.6, which proves a critical refresh threshold at \(1/\log n\) and classifies sensitivity versus stability. It does not determine the full finite-dimensional law. Penrose (2015) supplies static isolated-vertex Poisson approximation; its marginals alone do not determine temporal dependence. Clementi et al. (2011) provide results on flooding time in stationary evolving graphs. Primary public manuscripts on geometric-circle isolation and monotone bipartite edge arrival were inspected and have nonimplying objects or assumptions. Searches also considered equivalent bivariate Poisson, birth–death, Markov, and multitime formulations. The new claim is *only* the explicit time-indexed limit and temporal-signature classification, not the critical noise scale. A stronger older theorem might still imply it; historical uniqueness is not certified.

## Value — PASS

The joint law supplies persistence, reappearance, and simultaneous-no-isolate probabilities at the precise microscopic refresh scale relevant to the established noise transition. These are natural questions about time-dependent network reliability and cannot be recovered from snapshot Poisson marginals or a qualitative noise threshold. The explicit, structurally interpretable independent-block decomposition is the substantive mathematical result.

## Limitations and status

Fixed finite-dimensional observation times only, fixed real \(x\), equilibrium independent-edge dynamics, and no process-level tightness or error rates. Direct primary comparisons do not rule out all historical priority. No independent validation or certification has been performed.

Self-review: passed. Independent audit: not yet performed.
