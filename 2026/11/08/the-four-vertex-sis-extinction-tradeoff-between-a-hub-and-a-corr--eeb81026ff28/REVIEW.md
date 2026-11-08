# Scientific assessment: four-vertex SIS hub--corridor comparison

## Correctness — PASS

The claim is restricted to exactly two specified undirected trees on four vertices, unit recovery, positive common transmission rate, and a uniformly chosen initial infected set conditional on size. A complete 16-state row generator has been constructed directly from the transition rules; its 15-state transient inverse yields four exact mean-time gaps with positive-coefficient numerators and denominators. Independently, the first nonzero term of each survival-probability difference is obtained by exact powers of the full generator, not finite-time numerical extrapolation. For one, three, and four initial infections, continuity and the tail-integral formula prove the existence of a later reversal. `verify.py` reproduces all symbolic identities and uses a separate fraction-based elimination for twelve independent exact rational comparisons. No uniqueness or all-time stochastic ordering is claimed.

## Originality — PASS within inspected sources, provisional

The 2012 Mountford--Mourrat--Valesin--Yao work concerns long-time, large-graph extinction regimes, not a four-vertex exact objective disagreement. The 2015 van de Bovenkamp--Van Mieghem work supplies the same SIS model and exact star-graph methods; its explicit graph-type comparisons use a different normalization or a fixed metastable infected fraction, predominantly at 64 nodes. The inspected source's star/path simulations and formulas do not imply or state the uniformly initiated four-vertex, same-absolute-rate classification. Searches for path--star SIS survival-curve crossings and related finite-graph exact comparisons did not find a matching theorem. Search absence does not prove novelty; a possibly stronger uninspected finite-state reliability calculation remains a priority risk.

## Value — PASS

The four-vertex star and path are the first pair of nonisomorphic trees, with the same four sites and three contacts. Their complete all-rate, all-four-count expected-persistence comparison and their opposing short-deadline signs provide an exact, minimal counterexample to using mean outbreak lifetime to rank finite-horizon persistence. The initial-count dependence (one, three and four versus two) is not visible from the mean and illustrates an operationally motivated distinction between detecting a short-lived outbreak and expected time to elimination. A minimal, exhaustive topology comparison is a motivated finite benchmark, not an arbitrary parameter slice. No broader empirical significance is claimed.

## Closest literature and limitations

Mountford et al. (2012, arXiv:1203.2972), pp. 1--3, and van de Bovenkamp & Van Mieghem (2015, DOI:10.1103/PhysRevE.92.032806), especially Secs. II--III and Figure 10. The result does not classify the number of deadline crossings or generalize to other tree sizes. Further specialist priority searches and an independent audit remain appropriate.

Self-review: passed. Independent audit: not yet performed.
