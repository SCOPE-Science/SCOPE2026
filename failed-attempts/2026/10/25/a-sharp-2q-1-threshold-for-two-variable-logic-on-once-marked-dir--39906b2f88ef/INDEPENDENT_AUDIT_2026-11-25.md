# Independent mathematical audit

## correctness

PASS

The two unary recurrences trace a specified number of steps (modulo n) in either direction, so the disjunction marks the cyclic ball. The odd cutoff is exactly its maximal size, and the even cutoff adds a closed one-step neighborhood covering the complementary consecutive arc if and only if that arc has at most three vertices. Symmetry of S handles cutoff two and universal P handles cutoff one. For n,m≥2q+1, with t moves left, maintain labels ±1,…,±t, the mark, and the remaining class, together with the atomic pebble diagram. With a stationary pebble, relations to each designated label at t−1 are fixed by its t label; match an equal or adjacent far placement by identity or the corresponding neighbor. For any other far placement, at most three choices are forbidden and the t−1 far class has n−2t+1≥4 members. When no pebble is stationary, use identical realized labels. Self-loops are absent in the large cycles; rank 1 sees the loop/unique color in C1 and only the common marked and unmarked one-types otherwise, while rank 0 sees no vertices. The submitted checker omits S(x,x) in its initial one-variable types, so those types are not literally complete at C1; this does not falsify the finding. Independent complete-atomic-diagram replay with loops (`python -B /workspace/branches/replay_records_1_3_4_5.py`, section 1) gives 1,2,5,7,9,11,13,15,17 theories through rank 8 on sizes 1–24. The unbounded result follows from the game and formulas, not the replay.

## originality

FAIL

A distinct published catalogue record proves precisely the sharp equivalence and smallest-representative bound on the full n,m≥3 subfamily. The only additional parameter cases are the self-loop singleton and the two-cycle; marks, loops and symmetry separate those by ranks one and two. The frozen cutoff formulas are useful explicit witnesses, but do not leave a distinct nonroutine finding after the overlap. This is a judgment about equivalent existing coverage at review, not an attribution of earlier discovery; the matched record's listed date is later than the assigned source's listed date.

## value

FAIL

The sharp finite-rank invariant is a natural question, but a reader already has the exact nontrivial cutoff for all singly marked simple cycles. Adding the two elementary exceptional structures changes the count mechanically and leaves the same sharp representative bound. The explicit formulas are a pedagogically useful proof choice, not a distinct valuable scientific finding as submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
