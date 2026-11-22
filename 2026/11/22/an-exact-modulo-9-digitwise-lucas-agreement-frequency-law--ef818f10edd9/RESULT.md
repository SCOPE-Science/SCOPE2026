# An exact modulo-\(9\) digitwise Lucas-agreement frequency law

## Finding

For every integer \(L\geq0\), let \(W_L\) be the number of pairs of integers \(0\leq k\leq n<3^L\) for which \(3\nmid\binom nk\) and the digitwise Lucas product remains correct modulo \(9\):
\[
\binom nk\equiv\prod_{i=0}^{L-1}\binom{n_i}{k_i}\pmod 9,
\]
where \(n_i,k_i\in\{0,1,2\}\) are the padded base-three digits. Then \(W_0=1\), and \(D_L=3W_L-6^L\) satisfies, for every \(L\geq0\),
\[
D_{L+6}=6D_{L+5}-45D_{L+3}+45D_{L+2}+81D_{L+1}-243D_L.
\]
The initial values \((D_0,\ldots,D_5)=(2,12,39,153,549,2079)\), and hence \((W_0,\ldots,W_5)=(1,6,25,123,615,3285)\), determine every count exactly. Equivalently,
\[
\sum_{L\geq0}D_Lz^L=\frac{2-33z^2+9z^3+81z^4-162z^5}{1-6z+45z^3-45z^4-81z^5+243z^6}.
\]
Among all \(6^L\) nonzero-modulo-three entries of the triangular block, the agreement fraction tends to exactly
\[
\lim_{L\to\infty}\frac{W_L}{6^L}=\frac13.
\]
As a consequence, the number \(E_L\) of **all** positions \(0\leq k\leq n<3^L\), without the nondivisibility restriction, where the same congruence modulo \(9\) holds is, for every \(L\geq2\),
\[
E_L=\frac{3^L(3^L+1)}2-6^L-9(L-1)6^{L-2}+W_L.
\]
The boundary counts are \(E_0=1\) and \(E_1=6\).

## Assumptions and scope

The digits are read from least to most significant; all leading zeros are allowed up to length \(L\). Binomial coefficients have their ordinary integer meanings, including \(\binom00=1\). The principal count \(W_L\) concerns positions with \(3\nmid\binom nk\), equivalently all digit pairs obeying \(k_i\leq n_i\). All claims hold for every nonnegative integer \(L\), not only for computed ranges. The source direction is Rowland's first publicly available 2020 treatment of Lucas congruences modulo prime squares, with primary MSC 11B65.

## Proof

**Local correction.** For an admissible base-three digit pair \((r,s)\) with \(0\leq s\leq r\leq2\), Rowland's harmonic congruence (Theorem 4 of the cited paper) states
\[
\binom{3a+r}{3b+s}\equiv\binom ab\binom rs\bigl(1+3a(H_r-H_{r-s})+3b(H_{r-s}-H_s)\bigr)\pmod9.
\]
Here \(H_0=0\), \(H_1=1\), and \(H_2\equiv0\pmod3\). Order the six permissible pairs as
\[
Q=((0,0),(1,0),(1,1),(2,0),(2,1),(2,2)).
\]
For \(q=(r,s)\in Q\), put \(A_q=H_r-H_{r-s}\pmod3\) and \(B_q=H_{r-s}-H_s\pmod3\). The corresponding vectors in the displayed order are
\[
A=(0,0,1,0,2,0),\qquad B=(0,1,2,0,0,0).
\]
Iterating the local congruence and multiplying the factors \(1+3x\) gives
\[
\binom nk\equiv\left(\prod_{i=0}^{L-1}\binom{n_i}{k_i}\right)
\left(1+3\sum_{i=0}^{L-2}(A_{q_i}n_{i+1}+B_{q_i}k_{i+1})\right)\pmod9.
\]
Because the Lucas product is prime to three, agreement modulo nine occurs precisely when the displayed sum vanishes modulo three.

**Finite-state count.** Index the \(18\) states by \((q,c)\in Q\times\{0,1,2\}\). Define the integer \(18\)-by-\(18\) matrix \(M\) so that from \((q,c)\), appending \(q'=(r',s')\in Q\) advances to
\[
(q',\ c+A_qr'+B_qs'\pmod3).
\]
Each such transition has multiplicity one. Let \(v\) be the row vector equal to one at states \((q,0)\) and zero elsewhere, and \(u\) its transpose. Then
\[
W_L=vM^{L-1}u\quad(L\geq1),\qquad W_0=1.
\]
This is an exact bijection between admissible digit strings and paths ending with accumulated correction zero.

**A finite algebraic certificate of the recurrence.** Define the \(19\)-by-\(19\) integer matrix \(T=\operatorname{diag}(M,6)\), row \(\alpha=(3v,-6)\) and column \(\beta=(u,1)^\mathsf T\). Then
\[
D_L=\alpha T^{L-1}\beta\quad(L\geq1).
\]
For the polynomial
\[
P(t)=t^6-6t^5+45t^3-45t^2-81t+243,
\]
the recurrence residual for \(L\geq1\) is \(\alpha T^{L-1}P(T)\beta\). By the Cayley–Hamilton theorem, these residuals obey a monic recurrence of order \(19\) (the dimension of \(T\)). Therefore exactly \(19\) consecutive zero residuals, for \(L=1,\ldots,19\), imply zero for every \(L\geq1\). The standalone program `verify.py` constructs the integer transfer matrix without external packages and checks those \(19\) residuals exactly, plus the separate \(L=0\) residual. Thus the finite calculation closes the universal proof; it is not a finite-sampling extrapolation. Expanding the resulting rational generating function gives the numerator and initial values displayed above.

**Limiting fraction.** Let \(\omega\) be a primitive cube root of unity. For each of the two nontrivial additive characters \(\omega^{\pm c}\), the corresponding six-state complex transfer has entries \(\omega^{\pm(A_qr'+B_qs')}\), with every entry of absolute value one. Its spectral radius is strictly less than \(6\). Indeed, an eigenvalue of modulus \(6\) would force equality in every row's triangle inequality, and thus the same diagonal phase in every row. But the diagonal entries for states \((0,0)\) and \((2,1)\) are respectively \(1\) and \(\omega^{\pm1}\). The Fourier-root filter therefore gives \(W_L=(6^L+o(6^L))/3\), proving the limit.

**All triangular entries.** Kummer's theorem identifies \(\nu_3\binom nk\) with the number of ternary borrows in subtracting \(k\) from \(n\). Zero-borrow positions number \(6^L\) and contribute \(W_L\). Positions with exactly one borrow number \(9(L-1)6^{L-2}\) for \(L\geq2\): choose the one adjacent start/end digit position, three start pairs, three termination pairs, and six pairs at every other digit. At these positions the true binomial has valuation one but the digit Lucas product is zero, so they never agree modulo nine. At two or more borrows both sides are zero modulo nine, hence all remaining positions agree. Subtracting from the triangular count gives the stated \(E_L\).

## Verification

Run `python3 verify.py` with Python 3 (standard library only). It recreates \(M\), computes the twenty exact Cayley–Hamilton recurrence residuals, checks the first six initial values, and independently enumerates every entry of the first six triangular blocks using Pascal addition modulo nine. There are \(299{,}481\) independently compared triangular entries in total across \(L=1,\ldots,6\). The pairs \((W_L,E_L)\) for these levels are
\[
(6,6),(25,25),(123,177),(615,1668),(3285,17379),(18162,179271).
\]
The exact linear-algebra argument—not the finite enumeration—is responsible for the all-level assertion.

## Relationship to prior work

Rowland's *Lucas' theorem modulo* \(p^2\) (arXiv:2006.11701, first posted 21 June 2020) proves the local harmonic congruence and classifies digit pairs for which that local congruence holds for **all** higher indices. For \(p=3\), exactly three of the six individual pairs are universally safe; global equality can nevertheless arise by cancellations among consecutive digit-pair corrections. The present count incorporates these cancellations over every complete ternary block and is not the universal digit-pair classification. Huard, Spearman and Williams (1997) derive per-row residue counts modulo nine, using Granville's overlapping-digit formula. Those are stronger basic residue data but concern \(N_n(t,9)\) with a **fixed target residue** rather than coincidence with a digit-dependent Lucas product; the closed all-block coincidence recurrence was not identified there. The local correction formula, Lucas theorem and Kummer theorem are established inputs and are not claimed to be new.

## Limitations

This theorem concerns modulus nine and complete blocks of triangular indices, not arbitrary moduli, prime squares, or arbitrary interval cutoffs. It is a combinatorial count, not an assertion about an individual binomial congruence at every position. The recurrence is certified by a small finite-state linear-algebra calculation with a supplied fully executable certificate; independent human review has not been performed. A bibliographically unindexed equivalent counting formula could change priority.

## References

1. Eric Rowland, *Lucas' theorem modulo* \(p^2\), arXiv:2006.11701 (first posted 2020-06-21), especially Theorem 4. https://arxiv.org/abs/2006.11701
2. J. G. Huard, B. K. Spearman and K. S. Williams, *Pascal's triangle (mod 9)*, Acta Arith. 78 (1997), 331–349, especially Section 2. https://people.math.carleton.ca/~williams/papers/pdf/212.pdf
3. Andrew Granville, *Binomial coefficients modulo a prime power*, in *Organic Mathematics* (1997); overlapping-digit congruence quoted in Huard–Spearman–Williams, Section 1.
