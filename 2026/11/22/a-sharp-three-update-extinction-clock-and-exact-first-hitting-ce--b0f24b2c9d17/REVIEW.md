# Independent mathematical audit

## correctness

PASS

For the labelled book and synchronous absolute threshold two, any page vertex excited at time one has degree two and forces both its neighbors to have been excited at time zero. Those neighbors are refractory, not resting, at time one. Thus a vertex that can become excited at time two cannot use any excited page vertex as a trigger; it has at most one remaining nonpage neighbor, so none can fire. Time-two refractory states clear at time three. The specified witness starts u at rest with v and a₁ excited, forcing u to pass through 1 and 2 before it clears at update three. All states in {0,2}^(2m+2), and only those, clear by update one. With time-two excitation ruled out, clearing by two is equivalent to no update-one excitations. I reconstructed the nine counts: nonresting hubs (2,2),(1,1),(1,2),(2,1) leave 9,7,8,8 choices per page by excluding the relevant page trigger states. For (0,1) the resting hub must have no excited a_i, which already precludes the page trigger due to the excited opposite hub, leaving six choices per page; the mirror has the same count. In (0,2), there are six page choices with a_i not excited and three with a_i excited, and at most one of the latter may occur; (2,0) is symmetric. For (0,0), each side independently allows none or one initially excited page vertex, for (2^m+m·2^(m−1))². Summation gives S_m; subtraction yields the four first hitting counts and 9^m uniquely controls the limiting law. I inspected the direct C++ and symbolic Python verifiers and their recorded outputs under code/ and evidence/. The replays are specified in VERIFICATION.md (C++17 direct m=1,…,6 and Python convolution m=1,…,30), not executed in this review. The all-m proof is independent of these finite checks.

## originality

PASS

Eventual extinction is already implied by the density criterion and is not credited as original. The identified results do not cover the uniform sharp three-step clock together with the labelled first-hitting law on all quadrilateral books. The conclusion is limited to the compared sources, with the remaining literature-access risk noted.

## value

PASS

For a natural family already studied under one contact, the new question is how fast threshold two eliminates activity, not whether it eventually dies. A size-independent sharp bound and a complete labelled law resolve that question more strongly than a density budget. The exact count distinguishes the dominant time-three population from a nonvanishing time-two fraction, a feature not visible from the extremal bound or small simulations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
