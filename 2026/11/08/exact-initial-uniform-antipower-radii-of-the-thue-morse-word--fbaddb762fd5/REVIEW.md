# Scientific review of the exact uniform Thue–Morse antipower radii

## Correctness — PASS

The pointwise definition of the shortest antipower block length and its supremum over all positions are unambiguous. The finite-factor lemma is decisive: every relevant factor has length at most \(130\), and every such factor is represented among the \(2048\) symbols of \(\mu^{11}(0)\) because all four binary pairs occur in \(\mu^3(0)\). This reduces the upper bounds for infinitely many start positions to a complete, small, finite check. The eight lower bounds each have an explicit zero-based starting position verified against every smaller block size. Two distinct standalone programs confirm the factor counts, all upper tests and all lower witnesses, using independent factor generators. The computation is finite and exhaustive for the stated \(3\leq k\leq10\), not an extrapolation.

## Originality — PASS, subject to historical-priority limitations

The 2016 Fici–Restivo–Silva–Zamboni table is for \(j=0\) only. Defant and Narayanan principally treat prefix asymptotics, Gaetz treats fixed starting positions and asymptotics, and Berger–Defant prove uniform linear existence without the exact finite optimum. These do not determine the eight exact maxima of \(\gamma_j(k)\) over all \(j\). The nearest independently indexed analogous result concerns Fibonacci rather than Thue–Morse words. No accessible own earlier claim provides the present exact table. Searches cannot exclude every unindexed or independently circulated computation.

## Value — PASS

The uniform guarantee is a natural strengthening of a classical antipower existence theorem and answers an exact worst-start question rather than just its prefix-only version. The calculation identifies the first strict discrepancy (\(k=4\), uniform \(7\) against prefix \(5\)) and two early plateaus. A compact completeness lemma lets other investigations reuse the same finite-state certification method for sharp small-parameter questions. No general asymptotic improvement or result beyond \(k=10\) is claimed.

## Literature and limitations

Primary sources: *Anti-Powers in Infinite Words* (arXiv:1606.02868, first public 2016-06-09), *Anti-Power Prefixes of the Thue-Morse Word* (arXiv:1607.05825), *Functions on Antipower Prefix Lengths of the Thue-Morse Word* (arXiv:1705.06310), *Anti-power j-fixes of the Thue-Morse word* (arXiv:1808.01528), and *On Anti-Powers in Aperiodic Recurrent Words* (arXiv:1902.01291). The indexed closest comparison is the exact uniform radius of Fibonacci, which neither implies nor supplies the Thue–Morse values.

The proof covers exactly the eight indicated \(k\)'s, unrestricted positive block lengths and the one-sided binary Thue–Morse fixed point. Historical originality has not received an independent audit.

Self-review: passed. Independent audit: not yet performed.
