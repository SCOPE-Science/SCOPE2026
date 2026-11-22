# Independent mathematical audit

## correctness

PASS

For all rim lengths n>=4 the map is a product of involutory binary local shears, hence an automorphism. Inspecting RESULT.md and checks/verify.py at the returned exact blob paths confirms (I+L)y=(I+U)x, the polynomial determinant det((z+1)I+zL+U), the interior geometric-sum recurrence and the four-residue 3-by-3 determinant. Nonunit-eigenvalue eigenspaces have dimension at most one; at eigenvalue one the exceptional three chains occur exactly for 4|n, with lengths (1,1,1) if 8|n and (3,1,1) if n≡4 (mod8). Therefore cyclic invariant factor P_n when 4∤n, and two (z+1) summands plus P_n/(z+1)^2 when 4|n. On each cyclic binary module ker(F^d-I) has dimension deg gcd(R,z^d+1), with two additional dimensions when 4|n; Möbius inversion gives primitive cycles for EVERY d. The reciprocal polynomial has correct n=4 empty-sum boundary; all states are periodic due to invertibility. Independently constructed sweep and GF(2) charpoly computations for n=4..16 matched the stated formula and eigenvalue-one nullities [3,0,1,0,3,0,1,0,3,0,1,0,3]. The exact package checks further test n<=80 but are finite, not substitutes for algebraic general proof.

## originality

PASS

Best-of-knowledge original all-size ordered wheel binary module defect: key prior papers classify update-order equivalences or circular Rule 150, not the eigenvalue-specific wheel spectrum. A synchronous wheel XOR census uses a different noninvertible map. Earlier character polynomials under Coxeter terminology remain a residual risk.

## value

PASS

The fixed hub-first sweep is a natural asynchronous extension of binary Rule 150 from a ring to its wheel join. Its all-size exact four-residue transition in minimal number of F2[z] module generators (1 vs 3) is a structural Jordan phenomenon, not a small finite experiment. The characteristic polynomial and invariant-factor decomposition compute every temporal period population without period cutoff, and the five/eight-rim examples illustrate genuinely different dynamical regimes. These are motivated reusable invariants of ordered graph parity dynamics, beyond elementary general facts about shears.

The dated certificate retains the supplied scientific assessment, sources and limitations.
