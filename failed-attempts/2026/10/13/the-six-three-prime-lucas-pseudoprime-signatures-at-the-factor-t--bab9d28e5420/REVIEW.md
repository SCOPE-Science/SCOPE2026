# Independent mathematical audit

## correctness

PASS

The squarefree criterion is p−(D/p) | n−(D/n) at each prime, as in Helmreich–Webster Theorem 2. At n=3qr, reducing the q and r tests gives the two positive quotient integers j and k. Since r−c≥q+1 and 3q−ab≤3q+1, k is 1 or 2; r≤3q+2. Eliminating r gives (jk−9)(q−b)=(3−a)(3b+kc). The right side is nonzero for k=1,2, so q≤1+4(3+k)≤21 and r≤65. A separately written bounded check used trial division through √65 and tested all eight sign triples against all three original divisibilities for each prime pair, 600 cases. It returned (105,−+−), (195,++−), (255,−++), (399,−−−), (561,+++), and (2703,−++), with the listed quotient pairs and prime witnesses 41,109,89,41,157,89 (direct residue-square checks). The frozen VERIFIER.py and logged output were inspected, not executed; /workspace/replays/4.js provides the independent bounded reproduction. CRT gives the desired signs on exactly one eighth of the reduced classes that are 1 mod 4, and PNT in arithmetic progressions gives prime densities 1/8 conditional and 1/16 unconditional for each row. This is not a classification for other prime supports or discriminant families.

## originality

FAIL

The exact six rows were not found printed together, but the strongest published comparison is not merely Williams' criterion or a table for a fixed discriminant. Helmreich–Webster Theorem 4 gives the same signed two-quotient parametrization for arbitrary preproduct, and §5.2–5.3 gives its exhaustive enumeration including all four sign pairs at the last two primes. Setting the preproduct to 3 and taking both signs at 3 already gives the exact cutoff and enumeration by direct substitution. The additional prime-discriminant density is the standard independent residue-class count for any fixed sign vector, not a new implication particular to these rows.

## value

FAIL

Three is a natural first odd least factor, and mixed signatures are relevant. But in this case the published signed algorithm reduces that parameter to fourteen quotient pairs, with the claimed cutoff already immediate; the remaining density is a standard CRT and prime-progression count for any prescribed signs. The frozen result does not give a new cutoff principle, distinct phenomenon, or nonroutine consequence beyond the parameter substitution and bounded tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
