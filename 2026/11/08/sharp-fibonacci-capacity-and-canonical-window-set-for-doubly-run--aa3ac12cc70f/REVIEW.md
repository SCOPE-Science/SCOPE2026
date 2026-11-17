# Independent mathematical audit

## correctness

PASS

The directed length-n overlap graph of words avoiding 000 and 111 has 2F_(n+1) edges. Degree imbalance +1 occurs at 2F_(n−3) vertices with doubled first pair and undoubled last pair, obliging at least that many deletions for a closed trail with distinct windows. Deleting precisely the edges doubled at BOTH ends cancels all imbalances. Alternating extensions prove the retained graph is strongly connected, so it has an Euler tour of length 2(F_(n+1)−F_(n−3)). At equality an alternative deleted outgoing edge would terminate at a zero-imbalance vertex without outgoing deletion, so all deletions are forced, proving canonical window-set rigidity. Independent graph enumeration, Euler cycle and actual cyclic windows checked n=4..13. Infinite proof uses graph balance, not extrapolation.

## originality

PASS

PASS qualified: Chee et al. maximum-length RLL work restricts only runs of zeros, allowing arbitrarily many ones, whereas this forbids BOTH 000 and 111. Published two-sided Lucas/Fibonacci results concern shortest cycles COVERING all admissible factors, repeated windows allowed, not longest distinct-window cyclic trails and unique retained edge set. No general source inspected directly implies that rigidity.

## value

PASS

A natural two-sided run-length-limited synchronization constraint on de Bruijn cycles has a sharp infinite-family Fibonacci capacity and a uniquely forced set of windows, not merely a table of small examples. The balance/Euler obstruction and rigidity may be reused for constrained coding constructions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
