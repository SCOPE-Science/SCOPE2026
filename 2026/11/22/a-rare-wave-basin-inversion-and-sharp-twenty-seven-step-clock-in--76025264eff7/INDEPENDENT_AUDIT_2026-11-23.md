# Independent mathematical audit

## correctness

PASS

Independently enumerated all 16,777,216 states from the frozen edge list with the synchronous bit-plane update; checked its transition on a separate scalar implementation and verified the 18-edge relabelling to LCF. The full image of F^32 contains exactly 4,159 states and I verified that F permutes this image, proving that it consists precisely of all periodic states. Cycle tracing on the image gives least periods and orbit labels. The F^32 image of each start determines its basin; iterative preimages of the periodic set give exact first-entry layers. The replay matches all 72 nonempty histogram cells, orbit counts (1,1024,10,2) at periods (1,4,5,6), all period basin totals and maximum entry times, the listed individual sizes at periods 5 and 6, and the range from 9 to 373631 at period 4. The strict comparison is 385193>373631. Exactly 18 starts first enter at 27, all with period 4; witness 5999879 first repeats at step 31, returning to state 3222501 first reached at 27. The lcm of the periods is 60, so F^87=F^27 follows. This exhaustive method does not use either supplied C++ enumerator or its output to construct the census.

## originality

PASS

No inspected result contains the same four-state Frucht map census or implies its sharp transient and strict per-orbit separation. The exact catalogue match is the assigned record itself. Same-graph results use a different refractory chain; same-rule results on other canonical graphs have demonstrably different directed state graphs and observables. The update rule and use of exhaustive functional-graph enumeration are prior methods, not novel claims.

## value

PASS

The canonical asymmetric cubic graph is a motivated finite test of excitable dynamics without nontrivial graph automorphisms. The full entry-time/period law and sharp uniform cutoff are useful exact benchmarks. More specifically, period counts favor four-cycles 1024 to 10 while every period-five orbit individually beats every period-four orbit in basin weight. This is a structural separation about uniformly sampled starts that could not be read off from recurrent-state counts or an aggregate comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
