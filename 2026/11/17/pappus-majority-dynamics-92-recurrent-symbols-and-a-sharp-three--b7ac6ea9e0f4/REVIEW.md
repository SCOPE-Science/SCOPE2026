# Self-review

## Correctness — PASS
The defined Pappus Levi graph is explicitly generated in two independent ways, whose 27 edges match under the provided permutation. The nine-bit incidence checker exhaustively evaluates all 512 shore inputs, checks the recurrent phase-core identities, inverse restricted shore maps, core cardinalities and fiber weights; these statements directly imply the orbit and basin tables. The independent graph-level C++ checker enumerates all 262,144 initial states, verifies the temporal identity on each, and reproduces all first-entry depths and orbit basin counts. The finite domain is exhausted, so these certificates prove the fixed-graph claim; no finite experiment is extrapolated to an infinite family.

## Originality — PASS, with historical-priority uncertainty
The closest specific incidence-majority calculation concerns the **Heawood** graph, whose 58-symbol core, two-step sharp entry bound and different fiber weights do not imply the 92-symbol Pappus census. The published arbitrary cross-coupled-system normal form implies only the swap consequences **conditional on computing this graph's core and fibers**. The present exact 92-symbol core, shore 54/36/2 fiber partition, 4,186 cycles, sharp third step, and complete basin histogram are not present in those inspected sources. General convergence literature bounds periods but not these numbers. Cannings's 2009 study of regular-network majority dynamics is potentially relevant; its accessible abstract is not evidence of complete noncoverage. Historic unpublished or poorly indexed studies remain a risk. Searches are documented in the structured scientific review.

## Mathematical value — PASS
The Pappus Levi graph is a canonical cubic symmetric incidence graph, not a selected arbitrary finite network. The result supplies a full natural dynamical invariant—every attractor, exact basin and time-to-attractor population—and sharply contrasts the canonical Heawood case: 92 rather than 58 phase symbols, three rather than two transient updates, and no isolated recurrent configurations. The basin weights 2/4/130 give conceptual compression of the 262,144-state phase portrait; the derivation can inform incidence-based threshold dynamics. The result does not purport to generalize to all cubic graphs.

## Limitations and closest literature
The core-specific finite proof uses an exact exhaustive, transparent 512-subset certificate and an independent full-state checker; it is a finite classification, not a symbolic parameterized theorem. The Goles–Olivos general period bound, the 2014 majority work, the 2009 Cannings abstract, the Heawood census and the arbitrary cross-map swap theorem were compared. The complete Cannings and Goles–Olivos texts were unavailable. No independent external audit has taken place.

Self-review: passed. Independent audit: not yet performed.
