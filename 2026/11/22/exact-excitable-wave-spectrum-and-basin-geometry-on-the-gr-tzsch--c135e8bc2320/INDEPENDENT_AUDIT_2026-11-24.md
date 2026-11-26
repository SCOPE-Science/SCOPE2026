# Independent mathematical audit

## correctness

PASS

The 20-edge Mycielski graph and simultaneous resting/excited/refractory updates define a total map on exactly 3^11 labelled states. Indegree pruning leaves precisely directed cycles; reverse assignment of removed vertices gives the same attractor as the successor and depth one greater. A separate path-walk replay evaluated all 177147 states, without executing the supplied code, and matched every field of COUNTS.json (including the complete basin-size histograms and period-by-depth table). It found orbit counts 1,700,190,330,70 at periods 1,3,4,7,10 and a unique fixed basin of 13887. Exactly 120 states have depth 9, all of least period 4. State code 1985 first reaches cycle state 96363 at step 9 and returns at step 13. The period lcm is 420, giving F^429=F^9, while this witness is still transient at step 8 and cannot repeat after 420 more updates. The finite certificate covers this graph and this map, not a graph family.

## originality

PASS

The distinct claim is the complete spectrum and relaxation/basin data for threshold-one GHM on the Grötzsch graph. General quiescence and drift criteria are antecedents; the same-day comparisons include the same graph with another map and the same map on other graphs, not this census.

## value

PASS

Mycielski lifting preserves triangle-freeness while raising chromatic number; the lift of C5 is a canonical small graph on which to test how the graph change affects excitation. The full spectrum shows loss of the base cycle's period 5 and appearance of periods 3,4,7,10, with a major reduction in the extinguishing fraction. The basin and transient statistics supply an exact benchmark beyond a yes/no synchronization test and characterize period selection under uniform labelled initial states.

The dated certificate retains the supplied scientific assessment, sources and limitations.
