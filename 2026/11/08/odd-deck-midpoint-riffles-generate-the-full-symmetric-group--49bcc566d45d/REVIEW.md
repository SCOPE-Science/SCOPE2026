# Review

## Correctness (PASS)

The exact midpoint comparison yields two cycles with supports overlapping in one position. The commutator argument produces every three-cycle containing that position and hence the alternating group; generator parity and a direct inversion count at cut two finish the exact group statement. The presence of an identity move and uniform stationarity then prove ergodic convergence. A standard-library exact checker passes 31,378 finite checks. Those computations are corroboration, not an infinite proof; all odd deck sizes are covered analytically.

## Originality (PASS, provisional historical priority)

The most directly relevant new source, Jiang arXiv:2611.02092v1, Section 13.3, expressly leaves odd-deck unglued interpolation without an upper theorem. Its proof constructs even-deck random matching comparisons rather than odd-deck group generators. The external equal-pile shuffle-group classification and conditional-uniform-interleaving cutoff theorem have materially different one-step support. The 2017 general two-cycle literature overlaps the group-theoretic technique; no originality is attributed to the elementary generation lemma itself. The precise model-specific three-cut support and resulting odd-deck ergodicity were not found in inspected text or semantically retrieved claims, but a historically equivalent formulation remains possible.

## Mathematical value (PASS)

For an explicit probability model whose odd-deck convergence was untreated in its introducing analysis, the result closes the basic qualitative classification of recurrent classes, and exhibits a sharp parity distinction in the smaller two-cut support. It uses only three genuinely occurring cut values and identifies the algebraic mechanism despite the absence of random midpoint ties. This is a structural reachability result, not merely a numerical experiment or a known-table recomputation. It does not claim a polynomial mixing estimate.

## Closest literature and limitations

Jiang, arXiv:2611.02092v1; Bagiński–Gromadzki (2017), DOI 10.4064/cm7090-10-2016; Xia et al., arXiv:2304.01037; Sellke et al., arXiv:2510.22783. The general two-cycle generation idea is classical. The remaining risks are historical priority, possible unseen equivalent formulations of odd-deck midpoint interleaving, and the lack of a quantitative mixing rate. Independent mathematical review has not been performed.

Self-review: passed. Independent audit: not yet performed.
