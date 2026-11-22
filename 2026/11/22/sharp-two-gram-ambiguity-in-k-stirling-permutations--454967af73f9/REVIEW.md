# Self-review

## Correctness — PASS

The full claim is for integer \(k\ge2\), \(n\ge1\), with inverse fibers restricted to the labeled \(k\)-Stirling source. Every nonloop oriented bigram can occur at most once because a second occurrence would force a prohibited interlacing of two labels. A loop \(aa\) can occur at most \(k-1\) times, with equality exactly for one whole run \(a^k\). Removing the largest forced-consecutive block creates one uniquely determined smaller profile, and reinsertion has a number of possible gaps depending only on that smaller profile. Induction proves the exact fiber product and sharp maximum; the equality case forces a unique nested construction when \(k\ge3\). The first splitting of a homogeneous block has multiplicity \(k-1\ge2\), proving that singleton sources are precisely the permutations of whole blocks. The classical class-size product and gamma-function ratio give the stated probability. Exhaustive finite verification is consistent with every step, though not used in place of induction.

Risks and limits: no claim is made for competitors outside the constrained source, nor for unlabeled or cyclic observations; the algorithm can return an exponentially large fiber. The source-size product and the general two-Abelian definitions are prior mathematics.

## Originality — PASS (qualified)

The precise contribution is a constrained inverse-fiber classification, sharp worst-case ambiguity and singleton reconstruction law, not the existing largest-block insertion recurrence. The 2008 generalized-Stirling paper supplies the insertion and tree statistics but not the observed pair-count equivalence classes in its inspected central definitions/theorems. The 2013 two-Abelian paper supplies the general word observation, endpoint result and complexity framework but does not impose this increasing-nesting source. The 2016 tree-Eulerian article studies selected adjacent-pair statistics, not complete joint pair counts. Targeted mathematical-result and publication searches for equivalences and broader prior coverage found adjacent but non-dominating results concerning unrestricted two-gram fibers, restricted double-occurrence rigidity, and Stirling permutation statistics. The previously known double-occurrence singleton theorem already covers the \(k=2\) boundary, which is not claimed novel.

Residual priority risk: the result is a relatively direct but nontrivial refinement of known largest-label insertion once the full two-gram observation is introduced; unindexed older treatments of multipermutations by transition matrices or Euler trails could cover the exact same restricted fibers. No independent literature audit has been performed.

## Mathematical value — PASS

This solves an exact inverse problem on a well-established nested multipermutation family for *all* multiplicities and orders. Beyond an ad hoc collision, it reconstructs every inverse fiber, gives the sharp exponential worst-case information loss, proves a unique extremal observation for nontrivial multiplicity and identifies exactly which sources decode without ambiguity. The exact probability of singleton decoding shows exponential decay for every fixed \(k\ge3\). The facts are relevant to restricted-source two-gram sequencing or zero-error source identification without making claims about noisy channels or unrestricted words. Finite examples merely check the theorem rather than constitute its value.

Self-review: passed. Independent audit: not yet performed.
