# Independent mathematical audit

## correctness

PASS

A rainbow blade advances all three residues, and no rainbow can be created: a new rainbow has a 2 from an old 1, and if its old triangle had two zeros then both were adjacent to that 1 and advance together. With an active blade the hub rotates. For unordered pairs (00,01,02,11,12,22), direct application of the wing rule gives first times to the phase-appropriate passive pair as (1,4,1,4,-,0), (0,3,-,3,3,3), and (2,-,2,0,2,2) for initial hub 0,1,2 respectively; dashes denote rainbow types. Swapping the peripheral labels commutes with evolution. Without rainbow blades an initial hub 2 yields no 1 after one update (01 is prohibited), then all zero; a hub at 1 leads to this situation at hub 2. A hub at 0 with any 1 advances to 1; with none it rests and all vertices rest after at most one update. This proves the uniform four-step bound. The frozen sharp witness has passive additional blades going 00,00,11,22,00, and a single triangle's ten unordered color multisets give maximum three (001 and 011 attain it). The recurrent active labels fix the periodic state at each hub phase; per phase there are seven choices per inactive blade and one per prescribed orientation, giving all counts and the binomial law. Independent adjacency-based enumeration with first-repeat orbit detection for r=1,2,3,4 confirmed maxima 3,4,4,4, all basin sizes, and counts by active number. Replay: frozen RESULT.md Proof Steps 1–5 and verify.py lines 30–101 are exact finite reductions and supplementary finite-graph checks; the supplied verification_output.txt for r through 5 was inspected, not rerun. The argument applies only to the stated deterministic labelled rule and topology.

## originality

FAIL

Distinct indexed results prove the same sharp cutoff and identify the exact recurrent configurations. The allegedly additional oriented basin count is then a direct product count using the known conservation of contour integrals for three-state GHM. Thus the missing formula in an abstract or finding does not establish a distinct theorem; this is a coverage comparison, not a claim about historical priority.

## value

FAIL

A sharp transient cutoff and an oriented basin census on a natural graph family would be useful. But the exact cutoff is already covered by stronger entrance classifications, and the split by orbit is the immediate product count of conserved labels once the recurrent skeleton is known. No distinct worthwhile remainder is established by the frozen finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
