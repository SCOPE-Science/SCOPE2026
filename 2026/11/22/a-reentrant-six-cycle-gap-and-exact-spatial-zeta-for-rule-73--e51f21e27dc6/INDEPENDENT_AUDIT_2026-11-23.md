# Independent mathematical audit

## correctness

PASS

For the three one-output neighborhoods 000, 011 and 110, a trace walk with a distinguished first site has exactly one valid time history for each state fixed by F^t; neither spatial shifts nor temporal starts are quotiented in that trace. Periods dividing six are 1,2,3,6, so subtraction of the two proper maximal-divisor fixed sets and addition of their intersection, followed by division by six, gives the primitive orbit number. The formal log-determinant derivative therefore has the stated signs and factor of 1/6. Independently built the time-column graph by mask arithmetic and recomputed every determinant with exact characteristic polynomials (`python3 /workspace/checks/rule73.py`, SymPy 1.14). Cyclic sizes matched [4], [8,1,1], [19], [23,8,8,8,1,1]; exact matrix powers recovered c_8=4, zeros at 1–7 and 9–11, and 12,13,14,45,116 at 12–16. A separate reachability calculation confirms a return from pair (0,21) of each length 12–23 visiting a least-period-three column; the start contains a period-two column. Their coexistence forbids every proper divisor of six, and concatenation with length-12 returns fills all larger n. Checked the indicated length-3 and length-4 cycles in the strongly connected 23-component, giving primitivity. Its determinant is (1+z²)(1+z+z²)²(1−z+z³)²E(z); exact positive-vector ratios enclose its radius in (1.61574,1.61576), hence its positive reciprocal in (.61,.63) where the other factors are nonzero. All other six-return cyclic components have radius one and the lower-time maxima are below 1.546. Trace asymptotics thus have coefficient one before division by six. The arithmetic certificates establish the finite graph facts; the bijection, concatenation and Perron argument establish the infinite claims. Frozen code and logs were read as evidence, not run.

## originality

PASS

Qualified for the explicit all-circumference primitive-six census, exact infinite support and growth base. Arbitrary fixed-time transfer methods and ultimately periodic existence spectra are prior; the early gap is within the scale of earlier finite cycle-spectrum work and is not credited by itself.

## value

PASS

Six is the first return time combining the previously studied two and three clocks. Counting their genuinely mixed primitive orbits rather than all fixed states is a natural invariant. An explicit generating series with a separate growth exponent gives counts on every indexed ring, and the mixed-clock return walks explain precisely why the four-orbit first appearance is followed by a gap before permanent support. The result is more than replaying finite spectrum tables and does not claim anything about basins or other periods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
