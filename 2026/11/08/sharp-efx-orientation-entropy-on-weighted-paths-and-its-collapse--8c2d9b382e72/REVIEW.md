# Scientific review: Sharp EFX orientation entropy on weighted paths and its collapse under monotone perturbations

## Correctness — PASS

The claim is for a fixed, explicitly defined positive symmetric additive graphical valuation on a simple path and uses the all-removals (zero-inclusive) EFX definition. The proof first isolates the only potentially envied agents (two-incoming-edge sinks), proves necessity and sufficiency of their two flanking edges and weight comparisons, and obtains the universal count bounds. The run decomposition counts exactly the maximal equal-weight language; the rational generating function yields the coefficient formula, recurrence and residue asymptotic. Strictly increasing positive weights exclude every sink and attain the lower bound. Independent direct-definition enumeration in `verify.py` agreed with the local criterion on 397,362 weighted orientation states from 3,343 configurations. Uncertainty: the computations do not establish the general theorem; the written proof does.

## Originality — PASS, qualified by priority risk

The closest exact graphical-valuation literature proves existence of EFX orientations for bipartite graphs (Zeng–Mehta, Lemma 4.1) or studies general existence/complexity (Christodoulou et al.; Deligkas et al.; Afshinmehr et al.). These facts do not imply the complete census, sharp extremal value range, or asymptotic fragility. A locally recorded earlier cycle calculation counted a cycle with one exceptional edge, but its cyclic boundary problem does not supply the path theorem or arbitrary-path weight extrema. Searches for weighted path EFX counts, path Fibonacci formulae and fair-orientation perturbation rates did not uncover a covering source. The multigraph work was only partially accessible, and independently unindexed equivalent enumerations cannot be excluded.

## Value — PASS

A path is the first spatial network with both degree-one boundary agents and interior two-edge recipients. The theorem quantifies not just existence, but the entire range of fair allocation prevalence, and demonstrates an exponential collapse from a vanishingly small coherent change in valuations. The sharp extremizers, finite-alphabet criterion and explicit generating function make the result useful for sensitivity analysis and exact counting in graphical fair-division models. The regular-language coefficient calculation by itself is elementary; the substantive object is the fairness prevalence and stability boundary.

## Limitations and related literature

The assumptions exclude asymmetric endpoint preferences, nonpositive edges, cycles, multiedges and allocation outside endpoints. The main sources are Christodoulou et al. (2023, EC, doi:10.1145/3580507.3597764), Zeng–Mehta (2024, arXiv:2404.13527), Deligkas et al. (2024, arXiv:2409.13616), and Afshinmehr et al. (2024, arXiv:2410.17002). The last source was inspected only to the extent of the accessible abstract, not exhaustively.

Self-review: passed. Independent audit: not yet performed.
