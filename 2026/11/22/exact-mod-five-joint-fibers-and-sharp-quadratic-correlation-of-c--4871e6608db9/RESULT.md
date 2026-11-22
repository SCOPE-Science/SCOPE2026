# Exact mod-five joint fibers and sharp quadratic correlation of central trinomial and Delannoy numbers

## Finding

Let the central trinomial numbers and central Delannoy numbers be
\[
T_n=\operatorname{CT}(x+1+x^{-1})^n,\qquad
D_n=\operatorname{CT}(x+3+2x^{-1})^n\quad(n\ge0).
\]
For \(L\ge0\) and \(e,f\in\{0,1,2,3\}\), let
\[
N_L(e,f)=\#\{0\le n<5^L:T_n\equiv2^e,\ D_n\equiv3^f\pmod5\}.
\]
Put \(i^2=-1\). Every one of the sixteen counts is exactly
\[
N_L(e,f)=\frac1{16}\sum_{r,s=0}^{3}i^{-re-sf}
\left(1+(-1)^r+i^s(1+i^r+i^{-r})\right)^L.
\tag{1}
\]
In particular, for every \(L\ge0\) and \(f\in\{0,1,2,3\}\),
\[
N_L(1,f)=N_L(3,f),\qquad
N_L(0,f)-N_L(2,f)=\mathbf1_{f\equiv L\ (\mathrm{mod}\ 4)}. \tag{2}
\]
Thus the two residue rows \(T_n\equiv2,3\pmod5\) are identically distributed, and the rows \(T_n\equiv1,4\pmod5\) differ in exactly one cell, by exactly one occurrence. All sixteen pairs occur for every \(L\ge4\), whereas precisely the two pairs \((e,f)=(1,0),(3,0)\) are absent at \(L=3\). Each of the sixteen residue pairs is attained for infinitely many indices.

Writing the marginal counts \(A_L(e)=\sum_fN_L(e,f)\), \(B_L(f)=\sum_eN_L(e,f)\), define the interaction residual
\[
K_L(e,f)=N_L(e,f)-\frac{A_L(e)}4-\frac{B_L(f)}4+\frac{5^L}{16}.
\]
Then the exact nonseparable energy is
\[
\sum_{e,f}K_L(e,f)^2=\frac{9^L+2\cdot5^L+6}{16},\tag{3}
\]
and, uniformly in all sixteen pairs,
\[
K_L(e,f)=\frac{(-1)^{e+f}3^L}{16}+R_L(e,f),\qquad
|R_L(e,f)|\le\frac{2\cdot5^{L/2}+6}{16}.\tag{4}
\]
The scale \(3^L\) in the interaction is sharp. If \(\chi_5\) is the quadratic character modulo five, the related exact correlation law is
\[
\sum_{0\le n<5^L}\chi_5(T_n)\chi_5(D_n)=3^L,\qquad
\operatorname{Cov}\bigl(\chi_5(T_n),\chi_5(D_n)\bigr)
=\left(\frac35\right)^L-\frac{(-1)^L}{25^L},\tag{5}
\]
where \(n\) is uniformly distributed over the stated finite interval.

## Assumptions and scope

All variables \(n,L\) are nonnegative integers; \(e,f,r,s\) are elements of \(\mathbb Z/4\mathbb Z\), represented by 0 through 3. The character is the ordinary Legendre character on the nonzero residues modulo five, with \(\chi_5(1)=\chi_5(4)=1\), \(\chi_5(2)=\chi_5(3)=-1\). No unproved analytic equidistribution is assumed. The theorem concerns the fixed prime five, two specified sequences, complete index blocks of length \(5^L\), and exactly their residues modulo five, not higher powers.

## Proof

**1. Simultaneous Lucas factorization.** For either Laurent polynomial \(P(x)=x+b+cx^{-1}\) with \((b,c)=(1,1)\) or \((3,2)\), the coefficients are integers and exponents lie between \(-1\) and \(1\). In characteristic five, \(P(x)^5\equiv P(x^5)\pmod5\). If \(n=5q+d\), \(0\le d\le4\), then
\[
\operatorname{CT}P(x)^n\equiv\operatorname{CT}\bigl(P(x)^dP(x^5)^q\bigr)
\equiv(\operatorname{CT}P(x)^d)(\operatorname{CT}P(x)^q)\pmod5.
\]
The second congruence holds because every exponent of \(P(x)^d\) lies strictly between \(-5\) and \(5\), so the only such exponent divisible by five is zero. Iteration over all base-five digits \(d_j\) of \(n\) yields \(T_n\equiv\prod_jT_{d_j}\) and \(D_n\equiv\prod_jD_{d_j}\pmod5\). The first five residues are
\[
(T_0,\ldots,T_4)\equiv(1,1,3,2,4),\quad
(D_0,\ldots,D_4)\equiv(1,3,3,3,1)\pmod5.
\]
Since 2 and 3 each generate \(\mathbb F_5^\times\), digit \(d=0,1,2,3,4\) contributes the exponent-vector increment
\[
(e_d,f_d)=(0,0),(0,1),(3,1),(1,1),(2,0)
\quad\text{in }(\mathbb Z/4\mathbb Z)^2.\tag{6}
\]

**2. Exact Fourier inversion.** The complete block \(0\le n<5^L\) consists of all words of length \(L\) in the five digit choices, including leading zeros. Its exponent-pair count is the \(L\)-fold convolution of the five increments (6) on \(G=(\mathbb Z/4\mathbb Z)^2\). The character \((e,f)\mapsto i^{re+sf}\) has one-digit transform
\[
\lambda_{r,s}=\sum_{d=0}^4i^{re_d+sf_d}
=1+(-1)^r+i^s(1+i^r+i^{-r}).
\]
Group Fourier inversion gives (1) for every nonnegative \(L\), with the convention that a zeroth power is one.
The spectral rows simplify exactly to
\[
\lambda_{0,s}=2+3i^s,\qquad
\lambda_{2,s}=2-i^s,\qquad
\lambda_{1,s}=\lambda_{3,s}=i^s.\tag{7}
\]
For the difference \(N_L(0,f)-N_L(2,f)\), only odd \(r\) survive, giving
\[
\frac1{16}\sum_{r\in\{1,3\}}2\sum_{s=0}^3i^{-sf}(i^s)^L
=\frac14\sum_{s=0}^3i^{s(L-f)}=\mathbf1_{f\equiv L\ (\mathrm{mod}\ 4)}.
\]
For \(N_L(1,f)-N_L(3,f)\), the \(r=0,2\) terms cancel trivially, and the odd \(r\) terms cancel in pairs because (7) is identical for \(r=1,3\). This proves (2).

**3. Full support.** Convolving the five increments (6) three times yields every exponent pair except \((1,0),(3,0)\). A fourth convolution includes those missing pairs (for example, \((1,0)=(1,1)+(0,1)+(0,1)+(0,1)\pmod4\), and \((3,0)=(3,1)+(0,1)+(0,1)+(0,1)\pmod4\)). The increment \((0,0)\) preserves every attained pair when another digit is appended, so all sixteen persist for all \(L\ge4\). For infinitely many distinct indices with a prescribed pair, start with a witnessing digit word and append pairs of digit \(4\) in new highest places: \((2,0)+(2,0)=(0,0)\), so every append leaves both residues unchanged and increases the index. The support calculation for \(L=3\) is a finite enumeration of only 125 digit words and can also be reconstructed with `checker.py`.

**4. Exact energies and sharp interaction.** Fourier Parseval for the count table, with the \((0,0)\) frequency omitted, shows
\[
\sum_{e,f}\left(N_L(e,f)-\frac{5^L}{16}\right)^2
=\frac{2\cdot13^L+9^L+2\cdot5^L+10}{16}.\tag{8}
\]
Indeed, by (7) the sixteen eigenvalue squared magnitudes are 25 once, 13 twice, 9 once, 5 twice, and 1 ten times. Subtracting the two marginal contributions \(A_L/4\) and \(B_L/4\) deletes exactly the Fourier modes with \(r=0\) or \(s=0\). The remaining nine modes have squared magnitudes \(9\) once (\(r=s=2\)), \(5\) twice (\(r=2,s=1,3\)), and \(1\) six times (\(r=1,3,s=1,2,3\)); Parseval proves (3). The isolated leading mode has inverse Fourier contribution \((-1)^{e+f}3^L/16\); the triangle inequality on the remaining eight cross modes proves (4). This establishes the claimed sharp scale without a limiting heuristic.

**5. Character correlation.** Since \(\chi_5(2^e)=(-1)^e\) and \(\chi_5(3^f)=(-1)^f\), the three unnormalized character sums are precisely the Fourier modes \((r,s)=(2,0),(0,2),(2,2)\). By (7), their eigenvalues are \(1,-1,3\), respectively. Hence the sums are \(1,(-1)^L,3^L\). Divide by \(5^L\) to take expectations; subtract the product of means to obtain (5).

## Verification

Execute `python3 checker.py` from this directory (Python standard library only). The checker independently evaluates the two original integer recurrences through \(5^5\) indices, compares the first 36 entries with direct binomial sums, verifies the base-five digit products on all 3,125 indices, computes every Fourier cell for \(0\le L<25\) with Gaussian integer arithmetic, and checks support, the two exact symmetries, both Parseval identities, and all three character sums. These computations corroborate, but do not substitute for, the all-\(L\) group-character proof above.

## Relationship to prior work

The sequences and their generalized central-trinomial relationship were already established by Sun (2010). The Lucas product for central trinomial coefficients and their nonzero residues modulo five are explicitly described in Rampersad and Shallit (2021), including historical attribution to Deutsch and Sagan. The general constant-term congruence machinery is developed by Straub (2022) and Beukers (2022). This result does **not** claim any of those inputs as new; it evaluates the simultaneous, cross-sequence sixteen-class table, its exact marginal symmetries, and a sharp interaction energy. Those explicit joint results were not located in the inspected sources or research records. The calculation is elementary once the digit factorization is recognized; future priority comparison may reveal an implicit or explicit earlier equivalent.

## Limitations

Only modulus five and the specified two sequences are classified. The \(5^L\)-block energy is not a full error estimate at every arbitrary cutoff. Neither a new Lucas theorem nor a new congruence automaton is asserted. The full available mathematical literature has not been exhaustively inspected, and independent scientific validation is not yet performed.

## References

- N. Rampersad and J. Shallit, *Congruence properties of combinatorial sequences via Walnut and the Rowland–Yassawi–Zeilberger automaton*, arXiv:2110.06244, initial public posting 12 October 2021, https://arxiv.org/abs/2110.06244, Section 3, Theorems 7–9.
- Z.-W. Sun, *Congruences involving generalized central trinomial coefficients*, arXiv:1008.3887, initial public posting 23 August 2010, https://arxiv.org/abs/1008.3887.
- A. Straub, *On congruence schemes for constant terms and their applications*, arXiv:2205.09902, initial public posting 19 May 2022, https://arxiv.org/abs/2205.09902.
- F. Beukers, *p-Linear schemes for sequences modulo p^r*, arXiv:2211.15240, initial public posting 28 November 2022, https://arxiv.org/abs/2211.15240.
