# Independent mathematical audit

## correctness

PASS

The finite certificate covers labelled states, not automorphism classes. Independent exact replay used Cartesian products of all ten ternary coordinates, checked one-to-one ternary coverage, used two matched pentagons for the prism and disjoint two-subsets for the Petersen graph, and checked the latter's GP(5,2) isomorphism u_i -> {i,i+2}, v_i -> {i+3,i+4} mod 5. Four synchronous updates per state gave rest for all 59,049 initial states of each graph; the first-hit rows were (1,1023,25415,29230,3380) and (1,1023,25205,31300,1520). Last-wave coefficients by initial excitation count 3–7 were (640,1240,1040,400,60) and (0,420,720,320,60), with no others. Sizes 1,2 of the time-two excitation set occurred with frequencies (3340,40) and (1460,60). The prism witness 0000101010 -> 0001202121 -> 0012000202 -> 0020000000 -> 0000000000 was also checked. All-rest at time four implies A3 is empty, because any excitation at time three would still be refractory at time four. With no earlier nonrest state possible after hitting rest, the last-wave event is then exactly A2 nonempty. If |A0|<=3, the two distinct A1 neighbors of any A2 vertex draw two initial neighbors apiece from at most three, hence share one; A2 and A0 are disjoint because the latter sites were refractory at time one. These facts make the four vertices distinct and force a four-cycle, yielding the claimed obstruction. Reproducer: /workspace/branches/511167c6-5b6f-454f-83ed-3387901a3ada/reproduce_excitation.py; frozen verifiers and outputs were inspected, not executed. No exact data are extrapolated to other graphs.

## originality

PASS

Best-of-knowledge pass for the threshold-two labelled comparative census and its minimal-seed explanation. The contact-threshold model itself is not new, and changing the threshold alone would not suffice without the exact and structural conclusions.

## value

PASS

The two natural graphs have the same order and degree and are the two generalized Petersen possibilities of that order. The labelled extinction law is an exact benchmark for the same threshold dynamics, resolving what is and is not retained when one-contact recurrence is replaced by two-contact excitation. The seed-stratified last wave connects a precise observable to a simple four-cycle obstruction and differs by more than a factor of two between the graphs. This is informative beyond a raw table, but does not imply that girth alone determines the full counts in cubic graphs generally.

The dated certificate retains the supplied scientific assessment, sources and limitations.
