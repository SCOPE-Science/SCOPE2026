# Self-review

## Correctness — PASS

The tested Rule \(45\) truth table is equivalent to \(f(a,b,c)=a\oplus(b\lor\neg c)\). Explicit separate treatment of the first and last updated cells yields three boundary equations. Consecutive equality marks in the output would require incompatible interior inputs, and the reverse construction supplies actual preimages for every permitted mark word. The Fibonacci decomposition counts every output once because its starting bit, equality marks and final XOR bit determine the output uniquely. All hypotheses and the \(n=3\) boundary case are covered. Direct exhaustive checks through \(n=20\) and a separately implemented existential-preimage solver through \(n=11\) matched the full characterization. The infinite result rests on the proof, not the finite tests.

## Originality — PASS, with residual priority risk

Macauley, McCammond and Mortveit's *Order Independence in Asynchronous Cellular Automata* (arXiv:0707.2360; full text inspected, especially definitions and theorems on periodic-state invariance) classifies independence of recurrent sets from update order; it does not assert the specific one-sweep Rule \(45\) image language or its Lucas count. Goles and collaborators' *Block Invariance in Elementary Cellular Automata* (2015; available author-posted full text inspected, especially introduction and classification) addresses block-update invariance of periodic points, not exact one-sweep image size. Donoso-Leiva and collaborators' *On the Convergence of Elementary Cellular Automata under Sequential Update Modes* (arXiv:2509.07797; full text inspected, especially Rule \(45\) subsection and conjecture) gives fixed points and an open convergence question, neither of which implies the image classification.

Searches for sequential Rule \(45\) Lucas/Fibonacci image ranks, Garden-of-Eden language, and exact forward-image size found no matching theorem. Nearby published image enumerations concern **synchronous, different** elementary rules (for example Rule \(54\) and Rule \(126\)), so their propositions neither include nor imply this statement. Sequence coincidence with classical Lucas numbers is not a prior identification of these images. Full historical priority cannot be guaranteed, particularly for materials not indexed by search engines.

## Mathematical value — PASS

The one-sweep image is a natural finite-state dynamical invariant: it measures how much state information a prescribed deterministic updating schedule discards before recurrent behavior begins. The result is an exact **all-circumference reachability test**, an exact image count and entropy, and a complete count of one-step Garden-of-Eden configurations. The left-to-right update of Rule \(45\) is singled out in the recent sequential-convergence literature. Knowing that a single sweep has the Lucas-number image provides a concrete regular-language reduction for further analysis, without pretending to resolve the still-separate question of repeated-sweep convergence. Its significance does not rely on a conjectured downstream theorem.

## Limits and residual risks

The theorem does not count inverse multiplicities, classify attractors, or prove convergence for any unspecified circumference. Finite experiments are corroboration only. Historical coverage by an unindexed source is a residual risk; a negative search result is not novelty proof. External independent review has not been performed.

Self-review: passed. Independent audit: not yet performed.
