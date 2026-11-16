# Run-factor Möbius rigidity and sharp Walsh gaps for forbidden-one-run words

## Finding

For every pair of integers \(k\ge 2\) and \(n\ge 1\), let \(A_{n,k}\subseteq\mathbb F_2^n\) consist of all binary words containing no run of \(k\) consecutive ones. Define the unnormalized Walsh multipliers
\[
W_{n,k}(s)=\sum_{x\in A_{n,k}}(-1)^{\langle s,x\rangle},\qquad s\in\mathbb F_2^n.
\]
Write \(r=n\bmod(k+1)\), with \(0\le r\le k\), and set
\[
\delta_{n,k}=\begin{cases}1,&r\in\{0,k\},\\2^r,&1\le r\le k-1.\end{cases}
\]
Then the exact greatest common divisor of the Walsh multipliers and their sharp least nonzero absolute value coincide:
\[
\gcd_{s\in\mathbb F_2^n}W_{n,k}(s)
=\min_{W_{n,k}(s)\ne0}|W_{n,k}(s)|=\delta_{n,k}.
\]
More structurally, the unique integral multilinear expansion of the indicator \(f_{n,k}=\mathbf1_{A_{n,k}}\) has coefficients only in \(\{-1,0,1\}\). The coefficient on a coordinate subset \(J\) is nonzero **if and only if every maximal run of consecutive positions in \(J\)** has length congruent to \(0\) or \(k\) modulo \(k+1\); it is the product of \(-1\) over the runs congruent to \(k\). The empty-set coefficient is one.

Consequently, counting convolution \(T_{n,k}g=\mathbf1_{A_{n,k}}*g\) on \(\ell^2(\mathbb F_2^n)\) has exact Moore–Penrose inverse-on-range norm
\[
\|T_{n,k}^{\dagger}\|_{2\to2}=\delta_{n,k}^{-1}
\]
and positive-spectrum condition number \(|A_{n,k}|/\delta_{n,k}\). The convolution is invertible whenever \(n\bmod(k+1)\in\{0,k\}\), since then every Walsh multiplier is odd. No converse invertibility characterization is asserted.

## Assumptions and scope

All lengths are positive integers \(n\ge1\), all forbidden runs have \(k\ge2\), and adjacency is **linear**, not cyclic. The forbidden factor is \(1^k\); bit complementation gives the equivalent result for \(0^k\). Frequencies and word coordinates are indexed \(1,\ldots,n\). Walsh transform and convolution use counting measure, without Fourier normalization. The gcd is taken as the positive gcd of all integer coefficients, including any zeros. The Moore–Penrose inverse is zero on the kernel and inverts nonzero modes.

For \(n<k\), every word is allowed, so the formula correctly yields the single nonzero multiplier \(2^n\); this is not an exceptional omitted boundary. At \(n=k\), exactly one word is excluded and the least multiplier is one.

## Proof

**1. Integer multilinear coefficients.** Every function on the Boolean cube has a unique integer multilinear expansion
\[
f_{n,k}(x)=\sum_{J\subseteq[n]}c_{n,k}(J)\prod_{j\in J}x_j,
\qquad c_{n,k}(J)=\sum_{H\subseteq J}(-1)^{|J|-|H|}f_{n,k}(\mathbf1_H).
\]
For a fixed \(J\), decompose its selected positions into maximal consecutive runs of lengths \(\ell_1,\ldots,\ell_t\). Every subset \(H\subseteq J\) avoiding \(1^k\) is uniquely the union of independently admissible subsets inside these runs; no forbidden factor crosses a missing coordinate. Thus
\[
c_{n,k}(J)=\prod_{i=1}^{t}q_{\ell_i},\qquad q_m=\sum_{H\subseteq[m]}(-1)^{m-|H|}f_{m,k}(\mathbf1_H).
\]
The product over zero runs is one.

**2. Exact one-run generating function.** Let \(P_m(u)=\sum_{x\in A_{m,k}}u^{|x|}\), also defining \(A_{0,k}=\{\varnothing\}\). Every avoiding word uniquely decomposes into zero or more blocks \(1^j0\), \(0\le j<k\), followed by a terminal block \(1^j\), \(0\le j<k\). With \(R(z,u)=\sum_{j=0}^{k-1}(uz)^j\), this gives an identity of formal power series
\[
\sum_{m\ge0}P_m(u)z^m=\frac{R(z,u)}{1-zR(z,u)}.
\]
Since \(q_m=(-1)^mP_m(-1)\), substitute \(u=-1\) and \(z\mapsto-z\) to obtain
\[
\sum_{m\ge0}q_mz^m
=\frac{1+z+\cdots+z^{k-1}}{1+z(1+z+\cdots+z^{k-1})}
=\frac{1-z^k}{1-z^{k+1}}.
\]
Therefore \(q_0=1\), \(q_m=-1\) when \(m\ge1\) and \(m\equiv k\pmod{k+1}\), \(q_m=1\) when \(m\ge1\) and \(m\equiv0\pmod{k+1}\), and \(q_m=0\) otherwise. Combining this with step 1 proves the complete coefficient classification.

**3. Sharp maximum monomial degree.** Let
\[
D=\max\{|J|:c_{n,k}(J)\ne0\}.
\]
If \(r\in\{0,k\}\), the full selected run \(J=[n]\) has nonzero coefficient, so \(D=n\). Suppose \(1\le r\le k-1\). In any nonzero monomial, let \(t\) be the number of selected runs and \(q\le t\) the number having length congruent to \(k\) modulo \(k+1\). The total selected length is congruent to \(-q\) modulo \(k+1\). Hence for \(g=n-|J|\) unselected coordinates,
\[
g-q\equiv r\pmod{k+1},\qquad g\ge t-1\ge q-1.
\]
If \(g<r\), then \(-1\le g-q\le r-1\), an interval containing no integer congruent to \(r\) modulo \(k+1\) since \(1\le r\le k-1\). Thus \(g\ge r\) and \(D\le n-r\). Equality is attained by \(J=\{1,\ldots,n-r\}\): it is empty if \(n<k\), otherwise its single run has length divisible by \(k+1\). Therefore \(D=n-r\) in this case.

**4. All Walsh coefficients and a sharp witness.** Expanding the indicator and summing each Boolean coordinate independently yields, for \(S=\operatorname{supp}(s)\),
\[
W_{n,k}(s)=(-1)^{|S|}\sum_{J\supseteq S}c_{n,k}(J)\,2^{n-|J|}.
\]
Because all nonzero \(c_{n,k}(J)\) have \(|J|\le D\), every multiplier is divisible by \(2^{n-D}\). Choose any \(J_*\) with \(|J_*|=D\) and \(c_{n,k}(J_*)=\pm1\). At the frequency \(S=J_*\), all strictly larger supersets have coefficient zero, leaving
\[
W_{n,k}(\mathbf1_{J_*})=(-1)^D c_{n,k}(J_*)\,2^{n-D}.
\]
The bound is attained, proving both the gcd and the exact minimum. For \(r=0\) or \(r=k\), the full-degree coefficient is odd, and all lower-degree terms contribute even integers, so **every** Walsh multiplier is odd.

**5. Convolution.** Walsh characters diagonalize counting convolution on the finite abelian group \(\mathbb F_2^n\). Its eigenvalues are exactly \(W_{n,k}(s)\). By step 4 its smallest nonzero singular value is \(\delta_{n,k}\); its largest is \(W_{n,k}(0)=|A_{n,k}|\), since each character sum is bounded in absolute value by the number of summands. This proves the inverse-on-range norm and positive-spectrum condition number. The zero-free residue classes follow from the oddness proved above.

## Verification

Two standard-library Python programs independently check the infinite-proof boundaries: `verify_walsh.py` computes complete integer Walsh transforms by the butterfly algorithm for every \(2\le k\le7\) and \(1\le n\le15\) (90 parameter pairs). It checks the gcd, least nonzero multiplier, explicit sharp witness, Parseval's identity and zero-free residue classes. `verify_mobius.py` computes each multilinear coefficient by Boolean-lattice integer Möbius inversion, compares it with the stated maximal-run classification for \(2\le k\le7\), \(0\le n\le11\) (72 pairs), and separately checks 6,138 character values by direct signed enumeration versus the multilinear formula. Both are diagnostic finite tests; the all-parameter theorem rests on the formal-series and degree proof above. Run `python3 verify_walsh.py` and `python3 verify_mobius.py` in the directory containing this text.

## Relationship to prior work

The class of binary strings avoiding \(k\) consecutive ones is the established family of generalized Fibonacci strings, counted and Gray-coded by Bernini, Bilotta, Pinzani and Vajnovszki. Kurmaev studies enumerative weight and bipolar-charge statistics for run-length-limited codes. Cowell studies the uniform-probability reliability polynomial of consecutive-run failure systems. Gupta and Sarkar develop general algebraic-normal-form techniques for Fourier–Walsh evaluation. These works motivate the objects and supply general enumeration/transform frameworks; the present claim is the **simultaneous full run-factor classification of integral multilinear coefficients and exact minimum across all coordinate Walsh characters for arbitrary \(k,n\)**. It is not a claim that generating functions, Möbius inversion, Walsh diagonalization or run-limited coding are new. Special short forbidden-run cases are subsumed rather than counted as separate results.

## Limitations

The theorem does not enumerate the full Walsh zero set, establish invertibility or singularity for **every** remaining residue class, or address cyclic forbidden runs, multiple forbidden factors, nonbinary symbols, normalized probability convolution, or other operator norms. Historical priority is assessed against accessible, relevant published literature and mathematical records, not independently certified; unindexed work on reliability functions and signed enumerators is a residual risk. Finite checker runs do not independently certify the analytic proof.

## References

1. A. Bernini, S. Bilotta, R. Pinzani, V. Vajnovszki, *A trace partitioned Gray code for q-ary generalized Fibonacci strings*, arXiv:1308.3619, first publicly posted 2013-08-16, https://arxiv.org/abs/1308.3619 .
2. O. Kurmaev, *Constant-Weight and Constant-Charge Binary Run-Length Limited Codes*, arXiv:0902.4246, first publicly posted 2009-02-24, https://arxiv.org/abs/0902.4246 .
3. S. Cowell, *A Formula for the Reliability of a d-Dimensional Consecutive-k-out-of-n:F System*, International Journal of Combinatorics (2015), https://doi.org/10.1155/2015/140909 .
4. K. C. Gupta and P. Sarkar, *Computing Partial Walsh Transform from the Algebraic Normal Form of a Boolean Function*, Cryptology ePrint 2003/040, https://eprint.iacr.org/2003/040 .
