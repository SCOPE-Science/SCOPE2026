# Independent mathematical audit

## correctness

PASS

The complete language, automaton and enumerator are correct under the frozen assumptions. A k-clique in any orientation either contains a directed cycle (read arbitrary signs by walking forward/backward around it) or is a transitive tournament. This gives the lower language inclusion. Orienting edges increasingly in a proper k-colouring gives a signed-walk map to the transitive tournament and the upper inclusion. A length-k monochromatic run is impossible there by strict rank changes; each shorter run can go from one extreme rank to the other in its prescribed number of steps, and alternating runs concatenate. The complete DFA has a start, two sets of k-1 run counters and a dead state. Every state is reachable; a same-sign continuation that just fills a forbidden run distinguishes different run counters and separates each from the start and opposite counters; the empty continuation distinguishes the dead state. This works also for k=1, with start and dead states only. The two choices of starting sign and the compositions into allowable run lengths yield the displayed generating function. The independent bounded replay in /workspace/branches/ba5b573b-c697-4755-b510-70c88a0b7b9e/replay.py checked every orientation of six small graphs on words through length 7, DFA comparisons through length 9 and state/enumerator checks for k=1 through 5. The C5 witness reached {1,3,4}, {3}, {2,4}, {1,3}, then the empty set, as claimed. All supporting files including the supplied checker and its output were inspected; the uploaded checker was not executed. Bounded checks corroborate, not replace, the argument.

## originality

FAIL

A distinct inspected Resultary record, 49fc4cd7aaaa, explicitly gives the same equality-class language, complete DFA size 2k, and algebraically identical enumerator for every k>=2. This is verified equivalent coverage, not an inference from a title, date, or coincident parameters. The relation and historical priority of the two records are not established by their catalogue dates. The excluded k=1 branch is just a nonempty edgeless graph recognizing the empty word alone. The C5 boundary word is already recorded in 09ce4599f6de. No genuinely distinct substantive remainder merits repair.

## value

PASS

As a mathematical statement, the collapse is a useful structural characterization: it replaces an intersection over all orientations by a small complete recognizer and exact length counts for a natural graph class, including nonbipartite examples. This is the value of the mathematical theorem, not credit for the duplicate or for its trivial k=1 extension. Originality independently fails.

The dated certificate retains the supplied scientific assessment, sources and limitations.
