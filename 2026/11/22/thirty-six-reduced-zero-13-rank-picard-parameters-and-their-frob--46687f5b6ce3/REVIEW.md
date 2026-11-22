# Review: thirty-six zero-\(13\)-rank Picard parameters

## Correctness — PASS

The claim is restricted to smooth genus-three Picard curves \(y^3=x^4+ax^2+bx+1\) in characteristic thirteen and formal marked parameter pairs. From the differential basis and Cartier coefficient extraction, the independently generated identities \(h=6(a^2+5)\) and \(\det B=4(a^2+5)\Delta^2\) locate the first-rank jump. Along \(a^2=8\), the rank-one block has stable rank zero exactly when \(B^{[13]}B=0\); a complete exact Euclidean calculation gives the common divisor \(\Delta^2Q_a(b)\). The polynomial \(Q\) is squarefree and coprime to \(\Delta\); it contributes eighteen reduced smooth points for each of two coefficient fibers. Frobenius gcd degrees produce three degree-four and two degree-twelve closed points. All proof-critical computations are recomputed by `verify.py` from the original quartic and field arithmetic, with no extrapolation.

## Originality — PASS (qualified)

The closest relevant published results include the general Picard normal-form/discriminant theory of Bouw–Koutsianas–Sijsling–Wewers (2019); the first Cartier-rank study of Nourozi–Rahmati (2023); the bielliptic subfamily of Laga–Shnidman (2023); and a published calculation of the doubled Hasse divisor for that one-parameter subfamily. Their actual statements do not yield the reduced \(36\)-point stable-rank-zero coefficient scheme or the degree-four/twelve Frobenius splitting. Earlier work on the first Cartier-rank divisor of the two-parameter family also leaves stable \(p\)-rank undecided. An apparently relevant 1991 paper by Estrada-Sarlabous was obtainable only as publisher abstract; the possibility of an equivalent older computation remains an explicitly documented priority risk. Searches do not prove novelty by themselves.

## Mathematical value — PASS

Geometric \(p\)-rank measures stable Frobenius, not initial Cartier rank, and is meaningful for the Jacobians of the natural genus-three Picard family. The finding gives a complete, reduced and arithmetically resolved finite stratum where stable rank vanishes inside the initial-rank-one divisor. The sharp field-of-definition distribution is further arithmetic content unavailable from the initial Hasse determinant alone. The theorem is deliberately about marked coefficients, not a count of isomorphism classes or an assertion about the full Newton polygon.

Self-review: passed. Independent audit: not yet performed.
