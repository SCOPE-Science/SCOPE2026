# Independent mathematical audit

## correctness

PASS

The exact-two operation includes a second operation on a new symbol, so the canonical labels are P(i,j), A(i), B(i), with n(n+3)/2 labels. For equal outputs with different first marked sites, let i be the earlier site and c the complement of x_i. Equality forces a following run c^v with v≥1. The later-marked output has at most v consecutive c's after x_i. The earlier B(i) has v+2 and is impossible. An earlier P(i,j) can match only if j is inside the run but not at its end (otherwise the c-prefix exceeds v); replace it by A(j+1). An earlier A(i) can be replaced by A(i+1). These moves strictly advance the first marked site. At a common first site, A and B differ immediately, and P cannot match either: equality of a single suffix duplication with prepending a letter c would require the unchanged prefix through the marked letter and its inserted complement to both equal c. Two P labels with a shared first mark match only if their second marks agree, by the same single-insertion comparison. Thus the stated collisions exhaust the possibilities. A-to-A edges are a subpath and P vertices attach as leaves; the number of edges lost is the weighted complementary-run sum. Independent run sums give the rational series and extrema, including the n=1 base case. A fresh direct sequential-output enumeration plus a per-letter two-state histogram verified 35,268 words, including the reported q=4, n=6 coefficients.

## originality

FAIL

A distinct published Resultary record states the same theorem and distribution under the same assumptions. Both catalogue records are dated the same day, so exact coverage is established but precedence, dependence, and independent discovery are not inferred. This failure does not dispute the mathematics.

## value

FAIL

The exact per-source spectrum is a useful combinatorial object, but in this submission its invariant and complete distribution are already covered; the alternate proof and finite q=4 example do not add a distinct valuable mathematical fact. No actual surviving repair is justified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
