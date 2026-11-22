# Independent mathematical audit

## correctness

PASS

The source specifies 20 labelled bits in row-major order on Z/4 x Z/5, eight distinct Moore neighbours, B3/S23 synchronous update, and first-entry depth to a functional-graph cycle. Both complete C++ programs construct all 2^20 transitions (one via bit masks and forward chains, the other via coordinate loops plus indegree stripping); cycle and reverse-pruning logic classifies each state exactly once and the 80 spatial affine sign/translation maps commute with the update. I separately compiled and ran an independently written C++ exhaustive indegree-pruning enumerator and separate symmetry-action enumeration. It gave 461 orbits with primitive periods 1:313, 2:32, 4:20, 5:8, 6:60, 8:20, 10:8; exactly 1,097 recurrent configurations, sharp depth 21 realized by 80 states, 23 geometric classes, an empty fixed-state basin of 884,500, and period-5 basin 40 versus period-10 basin 9,340. Period/basin totals independently sum to 1,048,576. Exhaustiveness is for precisely this finite 4x5 torus, not arbitrary boards.

## originality

PASS

Best-of-knowledge PASS for the complete 4x5 labelled Life temporal/entry/basin/geometric census, excluding the previously known 313 one-step fixed states. Related transfer-trace results, three-row Life oscillator theorems and a 4x4 Life basin census do not imply the stated 461 cycles, seven periods, 21-step entry histogram or 23 spatial classes.

## value

PASS

A complete natural finite dynamical system classification can have value without extrapolation to all sizes: 2^20 states, multiple unexpected periods, a sharp maximum entry depth 21, 80 extremal states, isolation of all period-five cycles yet nontrivial period-ten basins, and 23 geometric classes. These precise structural distinctions are neither routine consequences of Life’s update rule nor mere recomputation of its known fixed-point count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
