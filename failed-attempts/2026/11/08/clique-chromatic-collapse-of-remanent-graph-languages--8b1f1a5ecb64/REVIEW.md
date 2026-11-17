# Independent mathematical audit

## correctness

PASS

For every finite simple nonempty G with chi(G)=omega(G)=k, any tournament orientation of a fixed k-clique either is transitive, in which a bounded-run signed path maps to the k-level transitive tournament by maximal incoming-path height, or has a directed triangle, which reads every signed word by forward/backward traversal. Therefore each orientation of G reads all words avoiding k identical consecutive signs. Orienting G by a proper k-coloring prohibits every +^k and -^k. The canonical trailing-run DFA has one initial state, 2(k-1) run states and a sink, all 2k Myhill-Nerode-distinct; alternating run decomposition yields (1+S_k(z))/(1-S_k(z)). k=1 gives empty word only and 2 states. Formula and finite k=2,3,4 algebraic equivalence independently checked. The general proof is mathematical, not numerically certified.

## originality

FAIL

Decisive prior coverage: the 2026-10-26 published full RESULT.md proves a strictly stronger sharp survivor-endpoint theorem for arbitrary k-tournaments and explicitly concludes the EXACT same clique=chromatic complete remanent language, the rational length-generating function and minimal complete DFA of 2k states for k>=2. The submitted k=1 boundary case is trivial. This is a covered special case, not a distinct original theorem.

## value

FAIL

FAIL: full language, exact length enumerator and minimal-state complexity already appear as consequences of the strictly stronger published October 26 endpoint theorem. Merely reproving the known conclusion with a simpler tournament argument, or adding trivial k=1, does not furnish an independently valuable new mathematical fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
