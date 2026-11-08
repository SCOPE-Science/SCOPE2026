# Review of the complete RRSC(2) graph-degree law

## Correctness — PASS

The attachment rule implies that every old degree-\(k\) vertex has exactly \(k+1\) favorable old faces; vertex-selected newborns have degree one and edge-selected newborns degree two. Exact linear conditional drifts follow. A bounded-noise stochastic approximation lemma, proved using products and Abel summation rather than unproved independence of weights, establishes the edge-density strong law and a simultaneous degree-class strong law by induction. The gamma ratio determines the tail; cancellation of degree fluxes proves total mass and total-variation convergence. The supplied `VERIFY.py` independently enumerates all reachable labeled histories through seven vertices and compares transition expectations as rational numbers. Simulation provides a separate finite sanity check, not an asymptotic proof.

## Originality — PASS (subject to independent historical assessment)

Krapivsky and Lucas, *Random Recursive Simplicial Complexes* (arXiv:2608.26547, Section VI), give the leaf fraction and leave the two-degree and higher classes uncomputed. Their predicted tail exponent is credited, not claimed new. Fountoulakis et al., *Dynamical Models for Random Simplicial Complexes* (arXiv:1910.12715, Section 1.4 and Remark 3), give fixed-face-dimensional growth distributions; the mixed vertex/edge face selection with degree-one and degree-two births is outside the theorem's stated hypotheses. Published-record searches for the mixed-model law, its degree-two radical and the gamma form found no direct coverage. An unknown reparameterized general preferential-attachment law is a residual risk.

## Mathematical value — PASS

A model's complete vertex-degree law quantifies the local geometry across a macroscopic population. The exact degree-two frequency and the closed law for all higher degrees answer a specifically motivated gap, while the almost-sure normalized law and exact positive tail prefactor make the heuristic scale-free prediction fully quantitative. This value does not rely on downstream applications or a moving-degree result.

## Limits

There is no assertion about degree classes scaling with system size, a central limit theorem for counts, the maximum degree, or higher-dimensional models. Historical novelty is provisional; independent assessment has not taken place.

Self-review: passed. Independent audit: not yet performed.
