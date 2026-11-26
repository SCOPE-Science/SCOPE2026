# Independent mathematical audit

## correctness

PASS

A shattered support cannot have two distinct color tests at one position because the two yes answers are incompatible. For a larger-than-2m support, answering no to every A test and yes to all B/C tests forces more than 2m distinct non-A positions, an impossible trace. For the 2m distinct B/C tests split m and m, any trace is realized by putting the queried color at yes positions and A at no positions; this leaves nonnegative deficits of total 2m, exactly the number of free positions. The result's seed table uses a well-defined second test at each child of the root, and independent replay confirms all eight answer paths with distinct AABC witnesses. Depth four has 16 mutually incompatible paths, more than the 12 seed hypotheses. The m-fold construction concatenates the depth-three trees on disjoint four-position blocks, with exactly (2m,m,m) content across all blocks, so every depth-3m path is realized. This is a lower bound for the full class, not an equality beyond the seed. The independent replay /workspace/branches/2104168b-0132-418e-9e5e-b0da4746d807/seed_replay.py also enumerates all seed static supports and checks product paths for m=1,…,5; the product argument, not the finite check, gives the unbounded result. Supplied code was read, not executed: the online script checks the tree and seed-count obstruction, not a fresh computation of the VC number in its printed label.

## originality

PASS

Credits earlier exact-quota feasibility and static structure and does not claim tree concatenation as a novel operation. The particular depth-three tree on the exact AABC class and the resulting all-m adaptive gap for the full fixed-content class are not covered by the inspected statements.

## value

PASS

Exact multiplicity is a natural global constraint on a categorical assignment, distinct from proper coloring or surjectivity. The result gives a 50% or greater increase in shatterable depth over the exact static benchmark, uniformly for a natural full parametric class, not just an artificially juxtaposed finite example. It provides a reusable depth-three witness and a gap of at least m without overstating the unrestricted online dimension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
