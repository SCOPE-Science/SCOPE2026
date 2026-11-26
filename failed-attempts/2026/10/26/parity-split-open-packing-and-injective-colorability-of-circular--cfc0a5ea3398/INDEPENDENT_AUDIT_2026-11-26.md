# Independent mathematical audit

## correctness

PASS

Two prism vertices conflict exactly at same-layer displacement ±2 or opposite-layer displacement ±1; n=3 correctly retains the triangle-induced same-layer edges and n=4 just duplicates the step of size two. The orbit of (i,t) -> (i+1,1-t) has length lcm(n,2); across its one or two orbits the conflict graph joins positions one or two steps apart. For a j-set in a cycle square the gaps are ≥3, and choosing a marked selected position counts each labeled set j times. This yields the claimed polynomial and its leading coefficient. Three colors force period three; the blocks 123 and 1234 give four colors in the other even cycle-square lengths, including the cyclic joins. The inequalities n/2 ≤ rho^o < 2n/3 for 3 not dividing n force exactly four equally sized maximum classes, hence n=4 or 8 by the stated size formulas. The repeated 1234 words realize these cases. Separate exhaustive tests of the equivalent condition |N(v) intersect S| ≤ 1 for every v checked all 21,824 subsets for n=3–7 against every coefficient (python /workspace/independent_checks.py 3); they supplement, not establish, the all-n argument.

## originality

FAIL

Two distinct earlier catalogue records demonstrably cover the main finding, even though catalogue dates alone do not settle historical priority. In particular, 27f63f2dbcd5 gives the same all-size polynomial, maximum and counts, and the exact perfect partition classification; caf3fe2c4a63 also gives the identical conflict graph and enumeration. The separately displayed injective chromatic number is immediate from the already identified even cycle-square components and does not supply a distinct substantive claim.

## value

FAIL

Exact enumerators and maximum-class partitions for this natural family are intrinsically useful, but already available in the matching records. The only separately displayed number, chi_i, requires just the short coloring observation on the already known components, not an additional independently useful unknown invariant. No distinct valuable remainder was found to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
