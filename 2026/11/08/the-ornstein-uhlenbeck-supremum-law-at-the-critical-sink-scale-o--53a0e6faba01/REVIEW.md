# Review of the critical sink-scale Ornstein–Uhlenbeck occupancy law

## Correctness

**PASS (self-review).** For fixed \(p\in(0,1)\) and \(q_n\sqrt n\to c\in(0,\infty)\), the theorem concerns only convergence in distribution of the normalized stationary sleeping-particle count. The exact stationary representation is Proposition 5 of Junge–Kaufman–Meisel (arXiv:2604.04747). Its coordinate-resampling drift is \(-(1-q_n)(Y_n-np)/n\), and its normalized local process has drift \(-x\) and diffusion coefficient \(\sqrt2\). The centered sink count at the boundary's deterministic crossing center has a Gaussian fluctuation independent of the local stationary OU process. The proof explicitly includes an early-hitting localization argument, late-hitting tightness, and Brownian immediate-crossing continuity; without these, a compact-window functional CLT alone would not suffice. The Gaussian boundary offset cancels in law only after conditional stationary time shift and OU reversibility. The 69,812 exact-rational tests in `check_finite.py` confirm the finite transition algebra and no-overshoot premise, but do not establish any infinite limit.

## Originality

**PASS, subject to historical-priority risk.** Junge–Kaufman–Meisel explicitly identify \(1/q_n=n^{1/2+o(1)}\) as the anticipated Gaussian-to-Gumbel transition, but their stated fluctuation theorem assumes \(1/q_n\gg n^{1/2+\varepsilon}\); their paper does not state the limiting OU supremum law at \(q_n\sqrt n\to c\). Járai–Mönch–Taggi analyze a different effective sink scale near \(1/n\). Known OU first-hitting/maximum methods may provide standard ingredients, not the specific stationary occupancy asymptotics for this model. Search comparisons against related published mathematical findings did not identify this exact model-and-scale result. The 2023 paper's theorem and OU heuristic were inspected, but a complete line-by-line inspection of every earlier source was not performed. Thus priority cannot be certified universally.

## Mathematical value

**PASS.** The result fills a parameter window expressly singled out as unresolved in the motivating preprint, replacing a qualitative transition prediction by a precise, reproducible distributional family. A single OU supremum functional simultaneously captures the Gaussian endpoint, strict upward finite-parameter shift and monotone dependence on sink strength. The cancellation of the separately nondegenerate sink-count Gaussian offset is a non-obvious mechanism particular to the stationary moving-boundary problem. No claims of moment convergence, rates or global phase diagrams beyond the fixed finite-constant critical window are made.

## Closest literature and limitations

The key source is Junge, Kaufman and Meisel, *Scaling limit and density conjecture for activated random walk on the complete graph*, arXiv:2604.04747, especially Theorem 3, Proposition 5, Section 1.5 and the boundary-process construction. Járai, Mönch and Taggi, *The number of particles in activated random walk on the complete graph*, arXiv:2304.10169, establish the older large-shift regime and discuss OU heuristics. Reed, Ward and Zhan, *On the generalized drift Skorokhod problem in one dimension*, DOI:10.1239/jap/1363784421, concern related OU hitting distributions, not this particle model. Residual risk is a broader moving-boundary or OU approximation theorem that, with the exact representation, might immediately imply the result; this was not located in the inspected sources.

Self-review: passed. Independent audit: not yet performed.
