# Scientific review

## Correctness — PASS

A complete self-contained proof derives the core singleton from coalition inequalities, the exact Shapley–core gap from a unanimity decomposition, a spanning-out-tree balance identity via a reversible cycle-exchange bijection, and the necessity of zero inter-component arcs via a condensation-DAG cut. The uniqueness argument uses a positive harmonic maximum principle; all quantifiers require a finite loopless digraph with indegree at least two and strictly positive target-homogeneous weights. A standalone exact-rational checker directly enumerates coalitions and permutations, checks 1,528 graph/parameter cases (including 369 calibrated strongly connected cases), and verifies 257 separate arborescence identities. Finite testing corroborates but does not establish the infinite theorem.

## Originality — PASS (with residual uncertainty)

The closest inspected primary papers are Bandhana–Kroupa–García (AAMAS 2024) and Ryzák–Kroupa (arXiv:2605.18157v1). They introduce the trust game and derive general Shapley/core formulas; neither provides the all-topologies positive-calibration existence theorem, its complete parameterization, or the spanning-out-arborescence construction. The latter formulas can be specialized to obtain the initial discrepancy identity, so that component is not claimed independently novel. The new conclusion is the structural inverse characterization and its graph-theoretic proof. Searches of scholarly sources and mathematical research records returned no covering statement; this is not a guarantee of priority. Additional risk: an equivalent result could appear under Markov-chain balance or cooperative network-game terminology.

## Mathematical value — PASS

The motivating primary paper explicitly emphasizes a tension between fair Shapley payoffs and stable core payoffs. The theorem characterizes precisely when topology permits removing that tension by positive target-specific trust intensities, proves a complete uniqueness law, and gives a directly computable integer spanning-arborescence certificate. A single inter-SCC arc is a sharp obstruction. This is more than a new numerical example or a parameter insertion into a known formula: it solves a natural inverse-existence and classification question over an unbounded family of directed networks.

## Limits and closest comparisons

The work is restricted to target-homogeneous positive scores and indegree at least two. It neither establishes a general-weight characterization nor strategic truthfulness, and the verifier is finite. The 2026 general Shapley formula is broader in the forward calculation sense, but does not settle the stated inverse question or classify all positive calibrations. The 2024 paper focuses on the cooperative model and Shapley-based reputation; the related arborescence conservation identity is explicitly proved here, rather than imported as a new claim from elsewhere.

Self-review: passed. Independent audit: not yet performed.
