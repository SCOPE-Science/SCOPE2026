# Independent mathematical audit

## correctness

PASS

The independent replay used only adjacency.txt and a new transition implementation. On all 531,441 ternary states it found F^11=F^8 and failure of F^10=F^7; the first equality makes every recurrent period divide three. The minimum t with F^(t+3)(x)=F^t(x) is exactly first periodic entry, with F^(t+1)(x)=F^t(x) distinguishing fixed points. The full histogram agrees: period-1 counts at t=0,...,8 are 1, 4095, 66091, 206142, 176472, 64900, 10440, 1620, 420, and the period-3 counts at t=0,...,3 are 600, 540, 60, 60, zero later. Canonicalizing phases yielded 200 cycles with 100, 40 and 60 basins of sizes 3, 6 and 12. Enumerating all 120 spatial automorphisms and acting on phase-canonical cycles gave seven classes of sizes 5, 5, 20, 30, 40, 40, 60, matching the representative codes and per-cycle basin sizes. The 600 successor-color states with at least two successor-color neighbors at every vertex were exactly the nonconstant recurrent states. The explicit orbit of code 2824 is at code 2 at update 7 and 0 at update 8, so sharpness concerns extinction; the oscillating basin enters by update 3.

## originality

PASS

The supported distinction is the threshold-two dynamical census: which states reach each attractor and the sharp relaxation time for this graph. The threshold-two phase colorings can be recovered by a local filter of the known threshold-one phase-coloring catalog, so the static count and geometric quotient are less independent than the dynamics. The inspected distinct records and primary passages do not give the two-contact attraction basins or its global iterate identity.

## value

PASS

The regular icosahedral graph is a natural common benchmark for comparing the two local rules. The full transition census provides information not available from phase-coloring data: raising the threshold prunes the recurrent waves from 48,400 to 200 but increases maximum first periodic entry from six to eight. It isolates the slow extinction tail from the small oscillating basin with an exact sharp identity and supplies per-orbit basin sizes. This supports a concrete comparison of persistence versus transient duration, without suggesting a monotonicity or a general theorem for other graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
