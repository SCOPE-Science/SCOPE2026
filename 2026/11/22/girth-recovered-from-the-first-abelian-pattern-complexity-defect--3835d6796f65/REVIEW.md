# Independent mathematical audit

## correctness

PASS

A defect selects q=f(k)-1 distinct rows of degrees at least 2,...,q+1. The induced graph on these rows and the k columns has cycle rank at least T_q-k+1 and any simple cycle uses at most q rows. This proves the lower endpoint for K and excludes all earlier defects in the unicyclic case. At T_r, an excess beyond r+2 would force cycle rank at least r+2. For the needed lower bound at T_r, Zeng–Xue–Zeng Theorem 6.4 has exactly the required hypotheses. Independently, a shortest cycle gives r rows of degree two on its r columns, with no chord. For r>=3 each selected row has infinitely many private columns, since pairs of rows have at most one common column. For r=2, an eventual inclusion between the neighbor sets of the two shifted rows would make the characteristic sequence eventually monotone on each residue class of their difference, hence eventually periodic, which is impossible. Thus one can add 0,...,r-1 private columns to the respective rows. Long gaps give count zero and also count one by aligning the last pattern position with the first support element after a sufficiently long gap. In the witness D_r, the two positive prefix sums r-1 and r form an alternating path, and L_0 R_0 closes a 2r-cycle. Each new sum greater than twice the previous largest cannot lie on any new cycle: both its endpoint indices would be bounded by the previous largest sum. The bundled traversal and witness checks are finite evidence; they are not needed for the proof and were not executed.

## originality

PASS

The prior paper already proves the cycle-to-defect direction, the forest equivalence, and the arity-three Sidon case. Its Proposition 5.7 already selects distinct degree rows and counts edges in the forest case, and its Proposition 6.9 uses the maximal-sum argument underlying the tail. Credit those premises and methods. The distinct supported contribution is the quantitative converse at every arity band and the exact unicyclic endpoint and complexity attained for all r. The prior full statements do not give bounds for these cyclic graphs in terms of the number of rows that can support a cycle or the rank of that finite certificate.

## value

PASS

The first nonminimal arity locates the shortest cycle of an infinite incidence graph, refining a qualitative forest criterion. The exact rank-one case explains the largest possible delay and shows that this delay is realized at every even girth, making the triangular cutoff sharp.

The dated certificate retains the supplied scientific assessment, sources and limitations.
