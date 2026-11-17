# Independent mathematical audit

## correctness

PASS

C: For the extra ballot A>B>C, first-round Borda increments are (2,1,0) and pairwise margins change by one toward the added ballot. Case splitting all before/after lowest sets yields only old singleton A -> new tied lowest {A,B}, with s_B=s_A+1, s_C>=s_A+3 and margin B>C positive; or old tied {B,C} -> new singleton C, with s_B=s_C<s_A and margin B>A at least 2. All other singleton/pair transitions have a weakly preferred new winner or are excluded by nonunique winners. Independent exhaustive enumeration of 74,256 profile/added-ballot comparisons for n=0..11 confirmed iff; exactly six adverse n=11 cases, none earlier. The 12-voter type-II witness was independently rechecked at score level.

## originality

PASS

O: PASS best-of-knowledge for the complete two-mechanism necessity/sufficiency and first-boundary orbit, not the known 12-total-voter minimum. Brandt–Matthäus–Saile (2022) uses simultaneous tied-lowest elimination and proves the first witness/minimum but does not give the inspected arbitrary-electorate iff or six-orbit classification. The 2019 Lepelley–Smaoui comparison and 2016 BER analyses concern monotonicity changes, and full relevant publisher text was unavailable, retained as risk.

## value

PASS

V: PASS. Exact behavioral classification isolates both tie-creation and tie-breaking causes of a no-show violation for every electorate; the six minimal directed examples provide a sharp enumeration boundary. This is a motivated structural strengthening of a known witness, not a mere parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
