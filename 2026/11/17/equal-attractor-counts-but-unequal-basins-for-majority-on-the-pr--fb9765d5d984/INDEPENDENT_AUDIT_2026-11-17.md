# Independent mathematical audit

## correctness

PASS

For odd k=1,3, GP(10,k) is cubic bipartite with the displayed A/B shores. The exact 1024-to-1024 maps U and V give F(a,b)=(U(b),V(a)), hence F^2=(UV,VU). Independent direct implementation from the graph neighborhoods confirmed on all 1024 masks that (UV)^3=(UV)^2 and (VU)^3=(VU)^2, and both have 124 fixed shores, giving F^6=F^4, 124 equilibria, and ((124)^2-124)/2=7626 primitive temporal two-cycles. The terminal maps s_A=(UV)^2 and s_B=(VU)^2 imply a full state eventually fixes iff s_A(a)=U(s_B(b)). Counting shore-fiber products yields fixed basins 36,784 (prism) and 107,224 (Desargues), with complementary two-cycle basins 1,011,792 and 941,352. Independent enumeration of all 1,048,576 ordered shore pairs for both k reproduced every first-entry table entry: for prism period-one [124,8710,14750,8560,4640], period-two [15252,485710,366590,108320,35920]; for Desargues period-one [124,2940,24480,32640,47040], period-two [15252,129140,442720,169920,184320]. Positive t=4 populations certify sharpness. This is genuinely exhaustive finite proof for the two 20-vertex graphs, not a general n extrapolation.

## originality

PASS

PASS best-of-knowledge, but substantial overlap is acknowledged: a fully inspected separately published Desargues double-cover result has *exactly* the 124, 7626, 107224 and Desargues entry counts. The published all-prism Lucas recurrence covers prism fixed/two-cycle totals. However neither inspected theorem gives the prism fixed-attraction basin 36784, its full entrance-time vector and fixed-weight contrast, or the matched two-graph equal-attractor/different-basin comparison, which remain mathematically substantive. The Desargues half and common recurrent counts are not called new.

## value

PASS

A natural pair of highly symmetric cubic 20-vertex graphs have identical periodic-orbit totals yet sharply different attraction basins. The exact finite complete-basin distinction is a motivated dynamical counterexample to inferring transient global behavior from attractor counts, with a reproducible sharp entry clock and weight spectrum; does not need an infinite-family theorem to be useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
