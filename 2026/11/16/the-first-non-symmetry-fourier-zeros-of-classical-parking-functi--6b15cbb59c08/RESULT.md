# The first non-symmetry Fourier zeros of classical parking functions

## Finding
For each integer \(1\le n\le5\), let \(q=n+1\) and let \(P_n\subseteq(\mathbb Z/q\mathbb Z)^n\) comprise the *zero-based classical parking functions*: vectors \(a=(a_1,\ldots,a_n)\) with entries in \(\{0,\ldots,n-1\}\) whose increasing rearrangement \(b_1\le\cdots\le b_n\) satisfies \(b_i\le i-1\). Let \(\zeta_q=\exp(2\pi i/q)\) and define the unnormalized Fourier transform
\[
W_n(k)=\sum_{a\in P_n}\zeta_q^{\sum_{j=1}^n k_ja_j},\qquad k\in(\mathbb Z/q\mathbb Z)^n.
\]
The exact zero-set classification through five cars is as follows.

1. In every size, \(W_n(k)=0\) for all nonzero *balanced* frequencies, meaning \(\sum_jk_j\equiv0\pmod q\) and \(k\ne0\). There are \(q^{n-1}-1\) such frequencies, and \(W_n(0)=q^{n-1}\).
2. For \(1\le n\le4\), **these are all the Fourier zeros**.
3. For \(n=5\), there are precisely \(360\) additional zeros at unbalanced frequencies. They form exactly five coordinate-permutation orbits, with sorted frequency representatives
\[
(1,2,3,4,5),\quad(1,2,3,3,4),\quad(1,2,3,3,5),\quad(1,3,3,4,5),\quad(2,3,3,4,5).
\]
The first orbit has \(120\) members and each remaining orbit has \(60\). In particular, no extra zero has a frequency coordinate equal to zero.

Consequently, for counting convolution \(T_nf=1_{P_n}*f\) on the entire finite abelian group, the ranks in increasing order \(n=1,2,3,4,5\) are respectively \(2,7,49,501,6121\). At \(n=5\), the full \(7776\)-dimensional operator has nullity \(1655=1295+360\), with \(1295\) symmetry-forced null directions and \(360\) additional null directions.

## Assumptions and scope
All groups are additive finite groups; characters are indexed by all \(q^n\) frequency vectors. A nonzero balanced frequency is one whose coordinate sum is zero modulo \(q\), excluding the zero vector. A frequency orbit means its orbit under coordinate permutations (not under a permutation of the residue labels). The sign convention in the exponent does not affect the zero set. The statement is exactly for \(1\le n\le5\), not an asymptotic or all-order claim. Ordinary one-based parking functions are obtained by adding one to every coordinate, which only multiplies a Fourier coefficient by a nonzero phase; hence they have the same zeros.

## Proof
**1. Forced null directions.** Pollak's circular-parking argument shows that the diagonal subgroup \(H=\{t(1,\ldots,1):t\in\mathbb Z/q\mathbb Z\}\) acts freely and every coset of \(H\) contains exactly one element of \(P_n\). (With \(n\) cars in \(n+1\) circular positions there is one empty position; exactly one diagonal rotation puts it in the extra position.) For \(k\ne0\) with \(\sum k_j=0\) modulo \(q\), the character \(\chi_k\) is constant on diagonal cosets and nontrivial on the quotient. Thus
\[
qW_n(k)=\sum_{x\in(\mathbb Z/q\mathbb Z)^n}\chi_k(x)=0.
\]
The same transversal gives \(|P_n|=q^{n-1}\), so \(W_n(0)=q^{n-1}\).

**2. Exact exhaustive reduction for the remaining directions.** Coordinate-permutation invariance means \(W_n(k)\) depends only on the sorted frequency tuple. Exactly \(\binom{2n}{n}\) sorted tuples must be tested, namely \(2,6,20,70,252\) for \(n=1,2,3,4,5\). Their coefficients have a finite, explicit integer description: enumerate all weakly increasing \(b=(b_1,\ldots,b_n)\) with \(0\le b_i\le i-1\), take each distinct permutation \(a\) of \(b\) once, and form
\[
N_r(k)=\#\{a:\sum_i k_ia_i\equiv r\pmod q\},\qquad
Q_k(z)=\sum_{r=0}^{q-1}N_r(k)z^r.
\]
Then \(W_n(k)=Q_k(\zeta_q)\), which is zero *if and only if* the integer polynomial \(Q_k(z)\) is divisible by the cyclotomic polynomial \(\Phi_q(z)\). The relevant polynomials are \(\Phi_2=z+1\), \(\Phi_3=z^2+z+1\), \(\Phi_4=z^2+1\), \(\Phi_5=z^4+z^3+z^2+z+1\), and \(\Phi_6=z^2-z+1\). This test is exact integer division, not floating-point thresholding.

The complete nested-loop certificate in `check_orbits.py` tests every such sorted tuple. It yields no unbalanced zero for \(n\le4\), and exactly the five listed tuples for \(n=5\). For the last case, with \(\zeta_6^2=\zeta_6-1\), every coefficient has the unique form \(A+B\zeta_6\), where
\[
A=N_0-N_2-N_3+N_5,\qquad B=N_1+N_2-N_4-N_5.
\]
The additional independent certificate `ORBIT_CERTIFICATE.tsv` explicitly lists these two integers at **all 252** sorted five-car frequencies; its only zero rows consist of the balanced representatives and the five exceptional unbalanced representatives. The covering enumeration is complete because every frequency vector has exactly one sorted representative and the residue tuple symmetry preserves the coefficient. The five orbit sizes are calculated by multinomial coefficients: \(5!=120\) for five distinct entries and \(5!/2!=60\) whenever the residue three is repeated.

**3. Rank.** The character basis diagonalizes finite-group convolution, with eigenvalues \(W_n(k)\) (or their conjugates, according to transform convention). Hence the rank equals the number of nonzero Fourier coefficients. Subtracting the forced zeros and the proved additional zeros from \(q^n\) gives the stated ranks.

## Verification
Run `python3 check_orbits.py` and `python3 check_tensor.py` from the directory containing these files. Both use only the Python standard library. The first reconstructs the \(\binom{2n}{n}\) coordinate-permutation orbits from Catalan-sorted preference words, tests exact cyclotomic divisibility, and checks all 252 rows of `ORBIT_CERTIFICATE.tsv`. The second independently enumerates each \(P_n\), applies an integer-valued tensor Fourier transform in the cyclotomic integer quotient \(\mathbb Z[z]/\Phi_q(z)\), and checks **every** one of the \(q^n\) Fourier frequencies. Each checker asserts the five exceptional representatives, the exact orbit count \(360\), and all symmetry-forced counts. The supplied outputs were obtained by executing these packaged programs; none relies on approximate numerical zeros.

## Relationship to prior work
The circular-parking transversal and \((n+1)^{n-1}\) count are classical and are **not** claimed as new. Stanley's *Parking Functions and Noncrossing Partitions* establishes the coset-transversal property and studies the symmetric-group Frobenius characteristic. Thomas and Williams study cyclic symmetry of a related affine-combinatorial realization. Diaconis and Hicks give the exact probabilistic parking-function ensemble and several equidistribution principles. These works explain the symmetry-forced zeros, but the specific extra 360 zeros, their five frequency orbits, and the first recoverability failure were not identified in the examined sections and indexed comparisons. The claim is the **complete first finite exception**, not a new proof of Pollak's lemma.

## Limitations
The frequency classification is proved only through five cars. No nonvanishing theorem for prime palette orders, higher car counts, or arbitrary parking-function generalizations is inferred. The exact finite certificate is substantial evidence for this bounded result but does not imply an infinite-family theorem. The indexed literature search cannot rule out all unpublished or poorly indexed older calculations; the related probabilistic literature treats additional statistics not exhausted here. No independent expert audit has been performed.

## References
- R. P. Stanley, *Parking Functions and Noncrossing Partitions*, *Electronic Journal of Combinatorics* (published 1996-11-12), https://doi.org/10.37236/1335 . Relevant especially Section 2 and the coset-transversal argument.
- H. Thomas and N. Williams, *Cyclic Symmetry of the Scaled Simplex*, arXiv:1207.5240 (first posted 2012-07-22), https://arxiv.org/abs/1207.5240 .
- P. Diaconis and A. Hicks, *Probabilizing Parking Functions*, arXiv:1611.09821 (first posted 2016-11-29), https://arxiv.org/abs/1611.09821 . In particular the circular-shift sampling argument and Section 4's equidistribution results.
