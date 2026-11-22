# Sharp pair-sum fibers and singular \(11\)-adic convolution of Apéry nondivisibility indices

## Finding

Define the classical Apéry numbers
\[
\operatorname{Ap}(n)=\sum_{j=0}^{n}\binom nj^2\binom{n+j}{j}^2,
\]
and, for every integer \(r\ge1\), the set
\[
\mathcal N_r=\{0\le n<11^r:11\nmid\operatorname{Ap}(n)\}.
\]
For every residue \(t\in\mathbb Z/11^r\mathbb Z\), count **ordered** pairs by
\[
R_r(t)=\#\{(a,b)\in\mathcal N_r^2:a+b\equiv t\pmod{11^r}\}.
\]
Then \(\mathcal N_r\) consists exactly of the length-\(r\) base-eleven words with no digit \(5\); consequently \(|\mathcal N_r|=10^r\). Every residue is a sum of two members of \(\mathcal N_r\), and the sharp fibers are
\[
9^r\le R_r(t)\le10^r.
\]
The minimum is attained at precisely \(10\cdot9^{r-1}\) targets: their least significant digit belongs to \(\{0,1,\ldots,9\}\), and their remaining digits, if any, belong to \(\{1,\ldots,9\}\). The maximum occurs uniquely at \(t\equiv-1\pmod{11^r}\).

Every individual fiber is determined by the finite digit product below. The complete additive energy
\[
E_r=\sum_{t\bmod11^r}R_r(t)^2
\]
satisfies
\[
E_0=1,\quad E_1=910,\quad E_{r+2}=923E_{r+1}-12150E_r\qquad(r\ge0).
\]
In particular, \(E_2=827780\) and \(E_3=752984440\).

Let \(X,Y\) be independent random elements of \(\mathbb Z_{11}\) whose base-eleven digits are independent and uniform on \(D=\{0,1,2,3,4,6,7,8,9,10\}\). Their sum distribution \(\mu\) has **full support and no atoms but is singular with respect to Haar measure**. Its exact correlation dimension is
\[
D_2(\mu)=\log_{11}\!\left(\frac{10000}{\lambda_+}\right)
=0.9997467611569999\ldots<1,\qquad
\lambda_+=\frac{923+\sqrt{803329}}2.
\]
Here correlation dimension is defined by the limit of logarithmic cylinder-square masses, not by Euclidean intervals.

## Assumptions and scope

All indices are nonnegative integers; all congruences and digital additions are taken modulo \(11^r\). Leading zeros are permitted in a word of length \(r\). The sum representation is ordered and is not a count of Apéry values. There is no assertion that the Apéry numbers themselves add to a prescribed residue. Finite-dimensional energy uses equality *modulo* \(11^r\), not equality of ordinary integers. The limiting measure is on the additive compact group \(\mathbb Z_{11}\), and Haar measure is normalized to one.

## Proof

**1. Arithmetic input and digit characterization.** Gessel's Lucas congruence for Apéry numbers, documented in the sources, gives
\[
\operatorname{Ap}(n)\equiv\prod_i\operatorname{Ap}(n_i)\pmod{11}
\]
when \(n=\sum_i n_i11^i\) with \(0\le n_i\le10\). Direct evaluation of the displayed binomial sum at the eleven single digits gives the complete residue vector
\[
\bigl(\operatorname{Ap}(0),\ldots,\operatorname{Ap}(10)\bigr)
\equiv(1,5,7,4,1,0,1,4,7,5,1)\pmod{11}.
\]
Thus exactly the digit \(5\) is excluded.

**2. Every fiber and its sharp extrema.** Let
\[
f(s)=\#\{(a,b)\in D^2:a+b=s\},\qquad f(s)=0\text{ outside }0\le s\le20.
\]
For a target digit \(d\in\{0,\ldots,10\}\), define the two-state carry matrix, with incoming and outgoing carries \(c,c'\in\{0,1\}\), by
\[
M_d(c,c')=f(d+11c'-c).
\]
If \(t=\sum_{i=0}^{r-1}d_i11^i\), then the exact fiber product is
\[
R_r(t)=(1,0)M_{d_0}M_{d_1}\cdots M_{d_{r-1}}\binom11.
\]
This is a complete all-target formula. The output carry is unrestricted, because equality is modulo \(11^r\).

For fixed incoming carry \(c\), a digit count modulo eleven is a convolution of \(D\) with itself in \(\mathbb Z/11\mathbb Z\). Among the eleven possible first summands only \(5\) is absent, and the same holds for the second. Inclusion-exclusion therefore yields the *exact* row-sum law
\[
\sum_{c'=0}^1M_d(c,c')=9+\mathbf1_{\{d\equiv c-1\pmod{11}\}}.
\]
Thus every step multiplies total path weight by a factor between \(9\) and \(10\). Initially the carry is zero, so the exceptional digit is \(10\). Every first digit \(0,\ldots,9\) produces both carry states with strictly positive weight: this follows from \(f(d)>0\) and \(f(d+11)>0\) for these digits. At all later steps, the only digits avoiding the additional unit in *both* carry states are \(1,\ldots,9\). This proves exactly the stated minimum and its multiplicity. The initial digit \(10\) gives total weight \(10\), all in outgoing carry zero, because the digit sum cannot be \(21\). Retaining the upper bound at every later step forces digit \(10\) again, proving unique maximal target \(11^r-1\). All other target fibers lie between the bounds, in particular they are positive.

**3. Exact modular additive energy.** Set
\[
H(h)=\sum_{z\in\mathbb Z}f(z)f(z-h).
\]
Enumerating \(f\) from the ten allowed digits gives
\[
\bigl(H(0),H(1),H(10),H(11),H(12)\bigr)
=(590,576,208,160,125).
\]
To count \(a+b\equiv c+d\pmod{11^r}\), propagate the signed carry \(q_i\in\{-1,0,1\}\) under
\[
a_i+b_i-c_i-d_i+q_i=11q_{i+1},\qquad q_0=0.
\]
Every final signed carry is allowed. In the state order \((-1,0,1)\) the exact one-digit transition matrix is
\[
W=\begin{pmatrix}208&576&125\\160&590&160\\125&576&208\end{pmatrix}.
\]
Consequently \(E_r=(W^r\mathbf1)_{q=0}\). Reflection exchanges the outer states, so its action on the symmetric subspace (coordinates \(s,c,s\)) is
\[
\binom{s'}{c'}=
B\binom{s}{c},\qquad B=\begin{pmatrix}333&576\\320&590\end{pmatrix}.
\]
The initial column is \((1,1)^{\mathsf T}\). The characteristic polynomial of \(B\) is \(z^2-923z+12150\); Cayley--Hamilton and \(E_1=320+590=910\) give the displayed recurrence for *every* \(r\ge0\).

**4. The limiting measure.** The first \(r\) digits of \(X+Y\) have probabilities \(R_r(t)/100^r\). Hence every residue cylinder has positive probability, so \(\mu\) has full support; the maximal fiber bound yields \(\mu(t+11^r\mathbb Z_{11})\le10^{-r}\), proving it is non-atomic.

For singularity, the addition carry \(c_i\in\{0,1\}\) is a finite irreducible aperiodic Markov chain. By symmetry of the allowed digit set about \(5\), its transition probabilities from zero to one and from one to zero are both \(45/100\). Its unique stationary distribution is \((1/2,1/2)\). Given carry zero, each output digit has probability \(9/100\), except digit \(10\), which has probability \(10/100\); given carry one, the exceptional output digit is \(0\). The Markov-chain ergodic theorem therefore gives, for \(\mu\)-almost every output, long-run frequency \(19/200\) for each of digits \(0\) and \(10\), and \(9/100\) for each of the other nine digits. Haar-almost every \(11\)-adic integer has frequency \(1/11\) for each digit. Since \(19/200\ne1/11\), the two measures are mutually singular.

Finally,
\[
\sum_{t\bmod11^r}\mu(t+11^r\mathbb Z_{11})^2=\frac{E_r}{10000^r}.
\]
The positive matrix \(B\) has largest eigenvalue \(\lambda_+=(923+\sqrt{803329})/2\); by the Perron--Frobenius theorem, \(E_r\) grows as a positive constant times \(\lambda_+^r\). The defining limit thus equals \(\log_{11}(10000/\lambda_+)\). The strict inequality below one follows without floating point: the polynomial \(z^2-923z+12150\) takes value \(-59850/121\) at \(z=10000/11\), forcing \(\lambda_+>10000/11\). The decimal is for orientation only.

## Verification

Run `python3 CHECK.py` using a Python 3 standard-library interpreter. The code independently evaluates Apéry numbers through index \(120\) for their Lucas residues, constructs every digit-transition count from the allowed digits, compares digit products against direct ordered pair enumeration for bases \(5,7,11,13\) at depths one and two, tests the complete eleven-adic spectra through depth four (including direct ordered pairs through depth three), and verifies the exact energy entries, recurrence and critical rational inequality. It also checks small general odd-base analogues of the extremal-digit argument. This is finite supporting evidence, **not** a substitute for Gessel's infinite Lucas congruence or the proofs above.

## Relationship to prior work

Gessel's 1982 Lucas congruence gives the multiplicative digit law for Apéry values; Luca and Shparlinski (2008) study global arithmetic properties using Lucas-type input, and Malik and Straub (2015/2016) investigate Lucas congruences and nondivisibility by primes. These sources establish the arithmetic input but do not state this exact two-sum representation spectrum, its sharp target fibers, the all-level energy recurrence, or the singular full-support \(11\)-adic convolution. Rowland, Yassawi and Krattenthaler (2021) establish stronger Apéry congruences modulo prime squares; their statements concern Apéry *values* rather than the additive structure of nondivisibility *indices*.

For comparison, the published result *Exact correlation dimension and an \(L^2\) obstruction for a three-digit four-adic convolution* concerns a real-line convolution of base-four digit sets and ordinary-integer equality; its carry boundary and digit set differ, and it does not imply the modular, Apéry-index calculation here. Exact carry matrices as a technique are standard and are not claimed as invented. A general hidden formulation in broader finite-type convolution literature is a residual priority risk.

## Limitations

This theorem is specific to nondivisibility indices at the prime eleven; it does not classify the residues of Apéry values modulo prime powers or their primality. The energy concerns modular equality, not exact integer equality, and the measure is \(11\)-adic rather than a real Cantor convolution. The correlation dimension is a square-cylinder dimension; no multifractal spectrum, Fourier decay or optimal \(L^p\) classification is asserted. Historical priority of an implicit equivalent transfer calculation is not fully excluded by the inspected sources.

## References

1. I. M. Gessel, *Some congruences for Apéry numbers*, Journal of Number Theory 14 (1982), 362–368, DOI: 10.1016/0022-314X(82)90071-3. Exact first-publication day not established here.
2. F. Luca and I. E. Shparlinski, *Arithmetic properties of Apéry numbers*, Journal of the London Mathematical Society 78 (2008), 545–562, DOI: 10.1112/jlms/jdn031; first online 2008-07-08.
3. A. Malik and A. Straub, *Divisibility properties of sporadic Apéry-like numbers*, arXiv:1508.00297, first submitted 2015-08-03; Research in Number Theory 2 (2016), article 5.
4. E. Rowland, R. Yassawi and C. Krattenthaler, *Lucas congruences for the Apéry numbers modulo \(p^2\)*, Integers 21 (2021), A20; freely accessible manuscript https://ericrowland.github.io/papers/Lucas_congruences_for_the_Apery_numbers_modulo_p%5E2.pdf.
5. *Exact correlation dimension and an \(L^2\) obstruction for a three-digit four-adic convolution*, published 2026-11-08, record 0a6383f8b10e, https://github.com/published-finding corpus/2026 (record identifier 0a6383f8b10e).
