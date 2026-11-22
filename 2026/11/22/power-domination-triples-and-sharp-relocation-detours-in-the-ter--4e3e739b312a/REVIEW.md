# Self-review: ternary Hamming power-domination relocation

## Correctness — PASS
For the exact 27-vertex labeled graph, the described 1296-element automorphism action yields ten disjoint triple orbits covering all 2925 triples. Three orbits, with sizes 324, 648 and 324, succeed; independent finite algorithms check all smaller sets, every orbit, and all optimum relocations. Full all-pairs shortest-path computation and a separate orbit-reduced computation agree on the graph sizes, eccentricities, antipodal pairing and exact extra-slide penalty. This is an exhaustive finite certificate, not an inference about higher dimensions.

## Originality — PASS (subject to residual search risk)
Bjorkman et al., *Power Domination Reconfiguration* (arXiv:2201.01798, 2022-01-05), establish the general reconfiguration framework and construct Hamming graphs as reconfiguration graphs of *other* base graphs, not power-domination optima **on** H(3,3). Anderson, Kuenzel and Schuerger (arXiv:2209.03930, 2022-09-08) give Cartesian-product lower bounds rather than this exact classification. Relevant published-finding corpus searches of the graph, alternative formulations and the numerical counts returned no covering result. The closest historical own claim concerns connected domination on H(3,3), a different invariant. Undiscovered historical work is a residual priority risk, and not all potential dissertations or appendices were obtainable.

## Value — PASS
The smallest nonbinary Hamming three-cube is a natural three-factor monitoring test case. The complete optimum classification and exact local-versus-global relocation metrics provide a nonroutine structural benchmark: the shortest-path eccentricities separate 3 versus 6, and the physical-movement restriction causes an extra three moves for exactly 41148 pairs. The finite theorem's scope is precise and does not claim extrapolation to general Hamming graphs.

## Sources and limitations
Primary checked sources: arXiv:2201.01798v1; arXiv:2209.03930v1; Koh and Soh, DOI 10.1016/j.akcej.2019.02.004. Two independently implemented Python 3 verification programs and ten orbit data records are included. The result is computer-assisted, there is remaining priority risk, and independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
