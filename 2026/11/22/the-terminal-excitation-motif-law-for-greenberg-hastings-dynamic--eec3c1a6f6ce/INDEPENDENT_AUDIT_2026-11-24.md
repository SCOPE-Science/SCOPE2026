# Independent mathematical audit

## correctness

PASS

With no excited hub at update t−1, any rim vertex excited at t required two excited path neighbors at t−1, both now refractory, so no resting rim vertex can see an excited rim neighbor at t. This excludes rim excitation at t+1 even if the hub is then providing one input at t. For H0 not 1 this kills R2 and hence all later rim excitations and prevents hub excitation from time 3 onward, giving rest by time 4. For H0=1 the hub is refractory and then resting at times 1 and 2, R3 and later are empty, and only a firing of the hub at time 3 can delay first rest to time 5. A resting center at time 1 with two excited rim neighbors then requires both of those neighbors initially 0, the center initially 0 or 2, and both distance-two sites initially 1. If a required site is beyond the boundary, the condition fails: an endpoint has only one path neighbor, and an excited-at-1 neighbor of a resting-at-1 center cannot have used that center as its initially excited input. Thus the necessary and sufficient time-two motif count and the two-input hub test are exact. For an independent OGF derivation, split a word at all its 1s. Initial and final binary runs each contribute E=1/(1−2z); each interior gap together with its closing 1 contributes good weight A=2z^4 or bad weight B=zE−A. The at-least-two condition has unique decomposition at the first two good gaps, giving z E^2 A^2/[(1−B)^2(1−A−B)], which simplifies to the claimed rational function. Two good gaps need length at least 9 and the stated shared-endpoint witness pads to every greater length. Independent disjoint blocks imply the conditional probability tends to one, so the unconditional limit is 1/3. A separate bitmask implementation compared the criterion and first-hit time for all 265,716 states at n=1–10; series arithmetic checked the given seven nonzero coefficients. Replay: python -B /workspace/branches/independent_checks.py 4.

## originality

PASS

The closely related cyclic clock and rim-exclusion mechanism, the analogous multicolor wheel motifs, and the general word-counting method are existing tools or precedents. The distinct finding is the complete three-state open-fan fifth-shell criterion together with its exact count at all lengths. Inspected alternatives do not supply this joint conclusion or the OGF. The pass is bounded by the actual inspected statements, not a historical-priority assertion.

## value

PASS

The natural object is the open-boundary version of a hub-and-rim excitable graph with a sharp universal clock. Its extreme first-hit shell is not fixed by the fact of extinction. The specific two-pulse mechanism and exact counts describe which initial states attain that clock, explain the delayed sharp onset relative to the wheel, and quantify its nonvanishing frequency in large random states. This is a useful complete exact invariant of the stated dynamics without presuming a full earlier-time census or claiming novelty for the cluster method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
