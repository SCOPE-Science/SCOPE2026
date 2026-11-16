# Scientific review

## Correctness — PASS
The claimed five ranks follow from the exact characteristic polynomials of the matrices \(B_r=H_rH_r^{\mathsf T}\) evaluated over all 90 row/column-margin-two binary matrices; the quadratic nonzero spectrum and normalization are stated without ambiguity. The proof of the Krawtchouk distance formula is combinatorial, and the conversion to graded orbit-harmonics dimensions uses the invertible squarefree-monomial/Walsh basis change. `verify_krawtchouk.py` and `verify_direct.py` reconstruct the sample space independently and check exact claims. The latter checks rank over a prime field as a lower-bound cross-check, not as a substitute for the rational characteristic-polynomial computation. Limit: only the finite \(4\times4\) case is proved.

## Originality — PASS, bounded comparison
Canfield–Greenhill–McKay (arXiv:math/0606496), Blanchet–Stauffer (arXiv:1007.1214), and Barvinok (arXiv:1010.5706) address fixed-margin enumeration, sampling, and limit behavior. None of the substantively inspected statements supplies the finite Walsh rank hierarchy or six quadratic spectral levels. Oh–Rhoades (arXiv:2503.19694), Section 7.4, explicitly poses the **binary** fixed-margin orbit-harmonics locus as a further direction after its results for all nonnegative-integer tables; their broader orbit-harmonics construction is credited. Searches of public mathematical records and public mathematical records did not identify a covering calculation. Risk: unindexed small-case tables and related association-algebra work could predate these numbers.

## Mathematical value — PASS
The smallest nontrivial half-density square binary table fiber is a canonical example with nontrivial row/column constraints. It gives a fully computed case of an explicitly proposed orbit-harmonics direction, with graded Hilbert series, a sharp minimal interpolation degree, and exact singular-value information needed to quantify quadratic Fourier reconstruction. The spectrum is not inferred from sample size, standard linear constraints, or generic interpolation theory. The result is finite and is not marketed as a general theorem.

Self-review: passed. Independent audit: not yet performed.
