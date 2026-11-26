# Independent mathematical audit

## correctness

PASS

For a binary cross-cut adjacency matrix B, summing the graph-state phases over the opposite shore gives reduced-matrix entries 2^(-|E|) exactly when the two indices differ by an element of ker B, and zero otherwise. Coset blocks give 2^rank(B) equal nonzero eigenvalues, establishing all stated entropy consequences. With the displayed odd-shore relabeling the factorization B=(I+U)(I+V) is exact even at m=2. Each shift has m orbits; their subgroups generate the even shore and intersect at 0 and (m,m). Thus every U-orbit indicator is even on every V-orbit and lies in im(I+V); the nullity is 2m. Distinct sites off the subgroup intersection are separated by a U- or V-orbit indicator. For separation across (m,m), lift one U-orbit indicator through I+V; summing the resulting difference along m V-steps gives 1, since they visit each U-orbit once. Constant one makes each evaluation nonzero. A one-step lattice translation swaps shores and gives the same assertion for the transpose kernel. For an update UV̄, surjectivity of V̄ on ker B implies im(U) is in the updated image; independence of the columns of U modulo im B then gives exactly rank(B)+rank(U). Disjoint omissions have two such coordinates on each side; shared endpoints give a rank-one update with a nonzero sum of two evaluations on one side. Fresh exact elimination on actual parity blocks reproduced all singles and pairs on C₄×C₄ and C₆×C₆ (496 and 2556 pairs), all singles and six pairs on C₈×C₈, and (10,11,11,10) on the two specified disjoint C₄×C₆ deletions. Reproduce the finite check by listing the four modulo-coordinate nearest neighbors for every odd row, clearing the listed retained-graph entries for each deletion set, and XOR-eliminating columns over F₂; compare each rank to the baseline plus 1 for a single/shared pair or 2 for a disjoint pair on the squares.

## originality

PASS

The intact rectangular baseline, the universal single-bond gain and the entropy-to-cut-rank identity are known. The supported distinct claim is the all-position classification for two distinct omitted edges on every even square torus, including ruling out cancellation for every disjoint pair, with an explicit 2D nonsquare contrast. No inspected result covers that combination.

## value

PASS

Multiple omitted preparation gates need not add their individual entanglement gains. The theorem resolves the first interaction regime for every position and circumference in a natural periodic grid family; the rectangular counterexample makes the distinction nontrivial. The kernel separation criterion explains the rigidity beyond finite examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
