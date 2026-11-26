# Independent mathematical audit

## correctness

PASS

A palindrome in this binary class crosses an even number of transitions and thus meets one, three, or five runs. The unary counts are the per-bit maxima. For three runs the entire middle run is forced, with the radius bounded by neighboring run lengths; the two possible families of each bit overlap exactly when their middle runs have equal lengths. The five-run family for a given outside bit then exists and restores exactly the positive-part deficit for that bit. Pairing max(x,z) with y gives x+y+z-max(x,y,z)-min(x,y)-min(y,z)=(min(x,z)-y)_+, verifying both formulas. With at most four runs the same counts use only max+min. Independently, in the six-run word every palindrome is in one of the two five-run windows, since it cannot touch both extreme runs of different letters. A palindrome in both inventories but not in their common central window would have to start with two different bits, so inclusion-exclusion and central richness also prove additivity. Only a longest palindromic suffix can be new on extending by one letter, so defect is monotone under extension at either end. Removing one letter at either end of a non-rich five-run word gives richness exactly for a=e=c+1 with b!=d; a non-rich six-run word already contains a non-rich five-run factor. Multiplying the geometric sum over c by the ordered unequal (b,d) series and by two for the initial bit yields the generating function. The seven-run witness has eight nonempty palindromic factors and its immediate proper factors are rich, giving sharpness. The uploaded checker's code and recorded evidence were read, not executed. The independent longest-suffix replay /workspace/branches/replay_frozen.py passed 19530 run profiles, obstruction counts for all binary words with at most six runs through length 12, and the explicit seven-run witness; the classification does not rely on finite extrapolation.

## originality

PASS

The exact five-run formula is shared with the distinct indexed five-run spectrum record. PASS is for the surviving six-run numerical decomposition, complete minimal-obstruction enumeration through six runs, and sharp seven-run failure as a package, not for the shared five-run law, short obstruction example, or factoriality of richness. The inspected prior statements do not supply the six-run inventory interaction or the general bounded-run obstruction list and its sharp boundary.

## value

PASS

Beyond the shared five-run calculation, this gives a local-to-global numerical test for the first run count where two candidate defects can coexist. It makes a complete bounded-run forbidden-factor classification possible, and the seven-run witness pinpoints why testing overlapping shorter windows is insufficient without the run-count hypothesis. This is a useful structural boundary, not merely a length-eight example or rewording of the five-run formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
