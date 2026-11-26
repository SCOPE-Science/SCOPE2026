# Independent mathematical audit

## correctness

FAIL

The numerical and all-length conclusions are correct with a corrected transfer matrix; the frozen proof contains a false pivotal matrix identity. In RESULT.md lines 38–52 the B_0 row omits B_0→U_1, which must be permitted by overlap and odd parity. The printed M violates row symmetry and gives (M^3)_{ZZ}=10, not a_2=11. The corrected row is (0,0,1,0,1,1,0), as in checker.py; it gives exactly the printed reduced matrix B. Independently, with d=1−z, the Z cofactor of I−zB is R=d^3−z^2(1+z)^2 and the determinant is dR−2z^2. Thus (R/det−1)/z is the asserted generating function. B^2 is positive; zero extension and one-cell parity repair at a suitable end for each even boundary component give a_n ≤ L_n ≤ a_{n+2}, including a trivial empty case. The entropy is per column. Independent flood-fill exhausted 87,381 patterns at lengths 0–8 and obtained 1,3,11,37,127,445,1559,5451,19061. Replay: /workspace/branches/8fc74a14-0ccb-4c37-ac46-589ccd7264f5/independent_odd_ladder.py and independent_odd_ladder.out. This confirms finite cases, not the asymptotic. The failed item is the displayed proof identity, not the corrected theorem.

## originality

FAIL

A distinct indexed result proves the identical entropy for the same strip rule and supplies the labelled parity matrix that directly gives the entire open-ladder series. There is demonstrated coverage of both parts; neither calendar-date ordering nor dependence is inferred.

## value

FAIL

Entropy of a natural strip and finite odd-component enumeration are meaningful invariants, but this frozen contribution adds only evaluation of a standard resolvent entry of the already-available exact presentation. Fixing the matrix transcription would not leave a genuinely distinct valuable claim to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
