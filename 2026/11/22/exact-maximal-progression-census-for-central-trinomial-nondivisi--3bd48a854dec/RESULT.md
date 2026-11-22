# Exact maximal-progression census for central trinomial nondivisibility modulo seven

## Finding

Let \(T_n=[x^n](1+x+x^2)^n\), and let
\[
E=\{n\in\mathbb Z_{\ge0}:7\nmid T_n\}.
\]
For each integer \(r\ge0\), let \(a_r\) be the number of ordered pairs of integers \((u,d)\) satisfying \(u\ge0\), \(d\ge1\), \(u+5d<7^r\), and \(u,u+d,\ldots,u+5d\in E\). Define
\[
B(z)=1-27z+193z^2-556z^3+616z^4+136z^5-346z^6-720z^7+928z^8.
\]
Then the complete enumeration of maximal six-term arithmetic progressions is
\[
\boxed{\sum_{r\ge0}a_rz^r
=\frac{z^2(9-32z-2z^2+153z^3-302z^4+462z^5-608z^6)}{(1-6z)B(z)}.}
\]
The initial values \((a_r)_{r=0}^{12}\) are
\[
0,0,9,265,5548,104588,1900204,34072486,608111004,10835595088,
192964239764,3435708845956,61168378718848.
\]
No arithmetic progression of seven distinct elements exists in \(E\), while \(4,5,6,7,8,9\in E\). Hence six is the maximal nonconstant progression length. The maximal-length statement follows also from the general theorem of Walker and Walker; the result here is the exact census across *all* steps and all base-seven truncations.

## Assumptions and scope

Only the standard central trinomial sequence and the modulus seven are used. All indices and common differences are nonnegative and positive, respectively, and upper cutoffs are strict. A six-term progression is counted once by its first term \(u\) and positive common difference \(d\). No primitiveness or coprimality condition is imposed on \(d\). The enumerator holds for every \(r\ge0\); there is no asymptotic or sufficiently-large exception.

The known Lucas product for central trinomial coefficients is
\[
T_n\equiv\prod_i T_{n_i}\pmod7,
\quad n=\sum_i n_i7^i,\quad 0\le n_i<7.
\]
The seven one-digit residues are \((1,1,3,0,5,2,1)\). Consequently
\[
E=\{n\ge0:\text{no base-seven digit of }n\text{ is }3\}.
\]
This digit characterization is established prior work, not an original component of this finding.

## Proof

The seven-term exclusion follows directly from the digit rule: for any \(d>0\), write \(d=7^t e\) with \(7\nmid e\). In a progression \(u+jd\), \(0\le j\le6\), the digit in position \(t\) runs through all seven residues, hence one term has digit three. The six-term example \(4,5,6,7,8,9\) avoids digit three in base seven.

It remains to enumerate all six-term progressions. Temporarily allow \(d=0\). Fix a digit length \(r\), write \(u\) and \(d\) in base seven with exactly \(r\) digits, allowing leading zeros, and process the positions from right to left. For \(j=0,1,2,3,4,5\), let \(c_j\) be the carry into the current column for \(u+jd\). Initially \(c=(0,0,0,0,0,0)\). At each column choose \(a,b\in\{0,1,\ldots,6\}\), the digits of \(u,d\), respectively, and form
\[
v_j=a+jb+c_j,\qquad x_j=v_j\bmod7,\qquad c'_j=\lfloor v_j/7\rfloor.
\]
The choice is admissible precisely when \(x_j\ne3\) for every \(j\). Thus each admissible pair of digit choices defines a weighted transition from carry vector \(c\) to \(c'\). Breadth-first exploration from the zero vector produces exactly 24 distinct states; repeated choices leading to the same pair of states are included with integer multiplicity. Let \(M\) be the resulting \(24\times24\) transition matrix with \(M_{c,c'}\) equal to this multiplicity.

After \(r\) columns, all six indexed values are less than \(7^r\) exactly when the final carry vector is zero. Therefore, for \(F_r\) counting also the degenerate choice \(d=0\),
\[
F_r=(M^r)_{0,0}.
\]
There are exactly \(6^r\) zero-step choices, one for each index with digits avoiding three, so \(a_r=F_r-6^r\).

For an explicit finite algebra certificate, put
\[
P(z)=1-27z+202z^2-588z^3+614z^4+289z^5-648z^6-258z^7+320z^8,
\]
\[
Q(z)=(1-6z)B(z).
\]
The exact integer computation described in the attached standalone checker verifies
\[
\sum_{r\ge0}F_rz^r=e_0^{\mathsf T}(I-zM)^{-1}e_0=\frac{P(z)}{Q(z)}.
\]
This is an identity of formal power series, not a fit to an initial segment: the checker constructs every reachable state and all 49 possible digit choices per state, computes \(\det(tI-M)\) by exact integer arithmetic using Faddeev--LeVerrier, obtains the exact adjugate numerator using the first 24 coefficients, and verifies the full polynomial cross-multiplication identity. Cayley--Hamilton guarantees that the numerator computed this way is complete. Subtracting \(\sum_{r\ge0}6^rz^r=(1-6z)^{-1}\) gives
\[
\sum_{r\ge0}a_rz^r
=\frac{P(z)-B(z)}{(1-6z)B(z)}
=\frac{9z^2-32z^3-2z^4+153z^5-302z^6+462z^7-608z^8}{(1-6z)B(z)},
\]
which proves the result for every \(r\).

## Verification

Run `python3 checker.py` with the standard Python library. The checker recreates the complete 24-state transition matrix from the displayed digit rule, verifies exact Cayley--Hamilton and rational-function polynomial identities, compares the first four enumerated values with an independent brute-force six-progression count, and independently computes central trinomial coefficients through index 149 modulo seven against the digit rule. The verified output includes \((a_0,\ldots,a_{12})\) as displayed above. The matrix identity, rather than the finite brute-force comparisons, establishes the unrestricted enumeration.

## Relationship to prior work

Deutsch and Sagan, and later Noe, established central-trinomial congruence and digit-divisibility properties. In particular Noe's 2006 digit product directly supplies the base-seven support description. Rowland and Yassawi give a general finite-automaton framework and explicitly discuss central trinomial Lucas products. Walker and Walker's 2018 theorem shows that the maximal progression length in any proper missing-digit base-seven set is six or less, and that some such sets attain six. Their work covers the length bound, not the displayed all-difference, full-block progression-count generating function. Sun's study concerns generalized central-trinomial congruences and does not supply this enumerator in the inspected material.

Thus the new claim is precisely the *evaluated complete rational generating function* for the number of maximal six-term progressions, not the Lucas property, digit exclusion, generic transfer-matrix methodology, or maximal-length bound.

## Limitations

No general formula is claimed for other primes, other excluded-digit sets, or progressions of lengths below six. The computation of the 24-state matrix and its exact characteristic certificate is finite, deterministic and supplied in full; it does not constitute an independent audit. A stronger uninspected general theorem giving the same rational enumerator might exist, so literature priority remains subject to wider review.

## References

- E. Deutsch and B. E. Sagan, *Congruences for Catalan and Motzkin numbers and related sequences*, arXiv:math/0407326 (first posted July 19, 2004), Section 4.
- T. D. Noe, *On the Divisibility of Generalized Central Trinomial Coefficients*, Journal of Integer Sequences 9 (2006), Article 06.2.7, especially equations (12)--(13) and Section 8. https://cs.uwaterloo.ca/journals/JIS/VOL9/Noe/noe35.pdf
- Z.-W. Sun, *Congruences Involving Generalized Central Trinomial Coefficients*, arXiv:1008.3887 (first posted August 23, 2010).
- E. Rowland and R. Yassawi, *Automatic Congruences for Diagonals of Rational Functions*, arXiv:1310.8635 (first posted October 31, 2013), Section 5.
- A. Walker and A. Walker, *Arithmetic Progressions with Restricted Digits*, arXiv:1809.02430 (first posted September 7, 2018), Theorem 1.1 and Proposition 2.2.
