# Independent mathematical audit

## correctness

PASS

Read the frozen RESULT.md plus actual packaged check_pappus_projection.py and check_pappus_full.cpp source. Independently rebuilt the incidence lines (0,a),(1,b),(2,a+b mod3), all 512 shore transitions Φ,Ψ, P=ΨΦ, Q=ΦΨ, and the full P²/Q² fibers. Verified P³=P², Q³=Q², 92-core images, odd-time im(ΨΦΨ)=R, core inverse bijection and im Φ/im P/im P² of sizes 182/110/92. This proves all F³ images periodic, F⁵=F³ and number of fixed/two-cycle orbits via symbol swap; im F²=110² exceeds 92², so time three is sharp. Exact complete fiber multiplicities 54 of two, 36 of four, two of 130 produce basin fixed {4:54,16:36,16900:2} and two-cycle {8:1431,16:1944,32:630,520:108,1040:72,33800:1}. The provided independent full 262144-state C++ census specifies first-entry counts and agrees with the shore proof. Separately verified the graph chords match MathWorld standard Pappus LCF notation. Exhaustive finite domains here are the entire claimed graph, not limited samples of an infinite family.

## originality

PASS

Best-of-knowledge originality concerns the Pappus-specific 512-shore recurrence, three-step entry cutoff and exact basins, not the classical period-at-most-two theorem or published general bipartite swap mechanism. Full Heawood proof gives a different 58-symbol finite geometry. Cannings 2009 remains a significant named source-inspection risk because its cubic-network study could not be read in full; lack of access alone does not fail the substantive comparison.

## value

PASS

The Pappus graph is a classical natural 18-vertex cubic symmetric incidence graph. Its exact synchronous-majority transient depth, recurrent-core geometry, orbit-level basin classification and unequal basin sizes give a complete, mathematically motivated invariant set for a natural finite dynamical system; such an exact finite result can be valuable without extrapolation to an infinite graph family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
