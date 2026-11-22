# Universal affine gap profiles of cyclotomic substitution quotients

## Finding

For every integer \(m\ge2\), let \(d=\varphi(m)\) and define the integral, monic *cyclotomic substitution quotient*
\[
H_{m,t}(X)=\frac{\Phi_m(X^t)}{\Phi_m(X)}\qquad(t\ge1,\ \gcd(t,m)=1).
\]
For each nonzero coefficient of this polynomial, list its exponent in increasing order; write \(G_{m,t}(z)\) for the generating polynomial of the differences between adjacent listed exponents, counted with multiplicity. For every reduced residue \(r\in\{1,\ldots,m-1\}\), there is an explicitly computable polynomial \(A_{m,r}(z)\in\mathbb Z_{\ge0}[z]\), depending **only** on \(m,r\), such that for every integer \(Q\ge1\),
\[
\boxed{G_{m,mQ+r}(z)=G_{m,m+r}(z)+(Q-1)A_{m,r}(z).}
\]
This determines **the number of gaps of every possible length**, for prime *and composite* multipliers. Moreover, every gap length is at most \(d\), this maximum is attained when \(t>m\), and
\[
\sum_{\ell\ge1}\ell\,[z^\ell]A_{m,r}(z)=md.
\]
For prime \(t=p\), the quotient is \(\Phi_{mp}\), so the theorem supplies the complete gap-frequency law along every reduced congruence class of primes.

An explicit example is \(m=15\). For a prime \(p=15Q+r>15\), write \(N_\ell\) for the number of adjacent nonzero coefficient exponents in \(\Phi_{15p}\) separated by \(\ell\). The following is a complete certificate: the entry in the second column is the eight-component slope vector \(([z^\ell]A_{15,r})_{\ell=1}^{8}\), and the third is the intercept vector \((N_\ell-Q[z^\ell]A_{15,r})_{\ell=1}^{8}\).

| \(r\) | slopes for lengths \(1,\ldots,8\) | intercepts for lengths \(1,\ldots,8\) |
|---:|:---|:---|
| 1 | (10, 4, 10, 2, 4, 0, 4, 2) | (0, 0, 0, 0, 0, 0, 0, 0) |
| 2 | (42, 16, 2, 0, 0, 4, 0, 2) | (4, 2, 0, 0, 0, 0, 0, 0) |
| 4 | (58, 12, 2, 4, 0, 0, 0, 2) | (16, 4, 0, 0, 0, 0, 0, 0) |
| 7 | (50, 6, 14, 0, 0, 0, 0, 2) | (22, 4, 6, 0, 0, 0, 0, 0) |
| 8 | (50, 6, 14, 0, 0, 0, 0, 2) | (28, 2, 8, 0, 0, 0, 0, 0) |
| 11 | (58, 12, 2, 4, 0, 0, 0, 2) | (42, 8, 2, 4, 0, 0, 0, 0) |
| 13 | (42, 16, 2, 0, 0, 4, 0, 2) | (38, 14, 2, 0, 0, 4, 0, 0) |
| 14 | (10, 4, 10, 2, 4, 0, 4, 2) | (10, 4, 10, 2, 4, 0, 4, 0) |

The *second-largest* gap in \(\Phi_{15p}\) therefore has length \(7,6,4,3\) when \(p\equiv\pm1,\pm2,\pm4,\pm7\pmod{15}\), respectively. The already-known maximum length \(8\), occurring \(2Q\) times, is recovered but is **not** presented as new.

## Assumptions and scope

All polynomial coefficients are integers, and a *gap* is the difference between successive exponents having nonzero coefficients; gaps of length one are included. The variable \(z\) is formal. The fixed modulus \(m\) is any integer at least two (not necessarily squarefree or odd), and the multiplier \(t=mQ+r\) may be composite, provided \(Q\ge1\) and \(\gcd(r,m)=1\). We make **no assertion** that the same affine identity extends to \(Q=0\).

To compute the slope without expanding a high-degree quotient, write
\[
\Phi_m(X)=\sum_{j=0}^{d}a_jX^j,\qquad
U_m(X)=\frac{1-X^m}{\Phi_m(X)}=\sum_{s=0}^{m-1}b_sX^s.
\]
Here \(a_0=a_d=1\), \(b_0=1\), \(b_{m-d}=-1\), and \(b_s=0\) for \(m-d<s<m\). For each \(0\le i<d\), form a circular length-\(m\) coefficient word
\[
W_{i,r}(s)=\sum_{j=0}^{i}a_j b_{(s+(i-j)r)\bmod m},\qquad 0\le s<m.
\]
Let \(S_{i,r}=\{s:W_{i,r}(s)\ne0\}\). If \(s\in S_{i,r}\), define \(\delta_{i,r}(s)\) as the positive forward circular distance to the next member of \(S_{i,r}\), so \(1\le\delta_{i,r}(s)\le m\). The fully explicit finite slope formula is
\[
\boxed{A_{m,r}(z)=\sum_{i=0}^{d-1}\ \sum_{s\in S_{i,r}} z^{\delta_{i,r}(s)}.}
\]
No unknown coefficients, conjectural inputs, or infinite computation occur in this formula. To compute \(G_{m,m+r}\), concatenate \(d-1\) full blocks each of length \(m+r\), and a final block of length \(m+r-d+1\), taking coefficients in every block from the corresponding periodic word \(W_{i,r}\).

## Proof

**1. Integrality, coefficient blocks and nonvanishing.** Since \(\gcd(t,m)=1\), every primitive \(m\)-th root \(\zeta\) remains primitive after raising to the power \(t\); hence \(\Phi_m(X)\) divides \(\Phi_m(X^t)\) over \(\mathbb Z[X]\). The quotient is monic of degree \(D=d(t-1)\), with constant coefficient one, and reciprocal because \(\Phi_m\) is reciprocal for \(m>1\).

The identity
\[
\frac1{\Phi_m(X)}=\frac{U_m(X)}{1-X^m}=\sum_{h\ge0}X^{hm}U_m(X)
\]
shows that for \(0\le i<d\) and \(0\le s<t\), the coefficient at exponent \(it+s\) is \(W_{i,r}(s\bmod m)\), provided \(it+s\le D\). Hence the polynomial consists of \(d-1\) blocks of length \(t\), followed by a last block of length \(t-d+1\); each uses one fixed \(m\)-periodic word.

No word vanishes identically. Indeed, with \(P_i(Y)=\sum_{j=0}^i a_jY^j\), the word, interpreted modulo \(X^m-1\), is \(U_m(X)X^{-ir}P_i(X^{r})\). At every primitive \(m\)-th root \(\zeta\), the value \(U_m(\zeta)\ne0\) because the roots of \(X^m-1\) are simple. If the word were zero, substitution would give \(P_i(\zeta^{r})=0\): yet \(\zeta^{r}\) has minimal polynomial \(\Phi_m\) of degree \(d\), while \(P_i(0)=1\) and \(\deg P_i\le i<d\). This is impossible.

**2. Period insertion and boundary control.** Fix \(m,r\) and increase \(Q\) by one. In each of the first \(d-1\) coefficient blocks, this inserts exactly one full period of its nonzero circular word before an unchanged ending fragment. Because at least one period was already present, the distances between the first and last nonzero coefficients and the boundaries of that block stay unchanged. Its internal gap histogram increases by precisely the cyclic histogram \(\sum_{s\in S_{i,r}}z^{\delta_{i,r}(s)}\).

The last block requires one boundary check. If \(r\ge d-1\), its length \(mQ+r-d+1\) already contains a full word for \(Q=1\), so the preceding argument applies. If \(1\le r<d-1\), at \(Q=1\) the last block is shorter than \(m\), of length \(L=m+r-d+1\). Reciprocity identifies its first nonzero coefficient with the last nonzero coefficient of the *first* block in degrees \(0,\ldots,m+r-d\). These initial coefficients are those of \(U_m\), whose last nonzero coefficient in this range is exactly at \(m-d\). Thus the first nonzero coefficient in the last block is at offset \(r\) (which is less than \(L\)). In particular, \(W_{d-1,r}\) has its first nonzero position at \(r\). Adding a complete period before the final short fragment therefore contributes exactly one cyclic histogram and does not change the gap crossing into this last block. Subsequent period insertions behave identically.

Every inter-block gap remains unchanged, because the first nonzero offset of each block and the distance from its last nonzero position to its endpoint stay fixed. Therefore the total gap polynomial increases by exactly \(A_{m,r}(z)\) whenever \(Q\) increases by one. Induction starting from \(Q=1\) gives the boxed identity.

**3. Sharp support bound.** Suppose two consecutive nonzero coefficients of \(H_{m,t}\) occur in degrees \(a<b\), with \(b-a>d\). Let \(C(X)\) be the truncation of \(H_{m,t}\) strictly below \(X^b\), so \(\deg C=a\). Since \(\Phi_m(X)H_{m,t}(X)=\Phi_m(X^t)\), both sides below degree \(b\) give
\[
\Phi_m(X)C(X)=\sum_{j=0}^{h}a_jX^{jt},\qquad h=\lfloor(b-1)/t\rfloor<d.
\]
The congruence is equality because both polynomials have degree strictly less than \(b\). Evaluation at a primitive root \(\zeta\) yields \(P_h(\zeta^t)=0\), contradicting the minimal polynomial degree. Thus every gap has length at most \(d\). Since \(t>m\), the initial coefficients of the quotient agree with \(U_m/(1-X^m)\) through degree \(m\); consecutive nonzeros at degrees \(m-d\) and \(m\) give a gap of length exactly \(d\).

Finally, the sum of the lengths of *all* gaps is the difference between the leading and constant exponents, \(D=d(t-1)\). Increasing \(Q\) by one increases \(D\) by \(md\), yielding \(\sum_{\ell}\ell[z^\ell]A_{m,r}=md\). This completes the proof.

## Verification

The included `verify.py` is standalone, uses only Python's standard library, constructs cyclotomic polynomials by exact monic integer division, and compares independently formed substitution quotients with the periodic-word formula. It verifies the entire affine histogram identity over 631 exact polynomial-division instances, including composite multipliers and moduli beyond squarefree ternary cases; it verifies all 64 slope/intercept entries in the \(m=15\) certificate and the degree-mass relation. These computations test the algebra and finite tables; the proof above, not the tests, establishes the result for unbounded parameters.

To reproduce: `python3 verify.py`.

## Relationship to prior work

Cafure and Cesaratto [1] give the second gap of *binary* cyclotomic polynomials and the full gap multiplicities in two special binary congruence classes; their work motivates a distributional question but does not state an arbitrary-modulus affine gap-polynomial identity. Al-Kateeb and Dagher [2] present exact coefficient block formulas and the *total* Hamming weight as a linear function in the prime parameter; those facts provide strong antecedents but do not distinguish gap lengths or address composite multipliers. Benoist and Perucca [3] determine coefficient patterns and maximum-gap multiplicities in important ternary families and tabulate coefficient *values* for \(\Phi_{15p}\); those coefficient patterns can be used to recompute the example above, but no general affine theorem for every gap length and every modulus is stated. Zheng [4] determines the maximum gap and its multiplicity for odd squarefree cofactors, and develops periodic words for extremal runs; the general full-histogram formula and composite-multiplier law are not stated there. The maximum gap of \(\Phi_{15p}\) is therefore **prior work**, not part of the novelty claim.

## Limitations

The theorem assumes \(t>m\) and \(\gcd(t,m)=1\). No claim is made for noncoprime multipliers or for the possible extension of the affine formula to smaller positive multipliers. The affine theorem supplies finite formulas for each fixed modulus, not a uniformly simplified expression in an *unbounded* modulus. The \(m=15\) table is an illustrative consequence rather than the sole contribution. Published full coefficient blocks imply that related aggregate statistics are in principle computable; an earlier unstated equivalent aggregation cannot be excluded without an independent priority audit. No independent mathematical audit has been performed.

## References

[1] A. Cafure and E. Cesaratto, *Gaps in binary cyclotomic polynomials*, arXiv:2507.19381 (first public version July 25, 2025). https://arxiv.org/abs/2507.19381

[2] A. Al-Kateeb and A. Dagher, *On the number of terms of some families of the ternary cyclotomic polynomials*, arXiv:2207.07393 (2022), especially the block and Hamming-weight laws. https://arxiv.org/html/2207.07393v2

[3] A. Benoist and A. Perucca, *The ternary cyclotomic polynomials* \(\Phi_{3pq}\), author preprint publicly available since July 2023; *Involve* 19 (2026), 51–72. https://orbilu.uni.lu/handle/10993/55534

[4] Q.-Y. Zheng, *The totient bound and extremal gaps in cyclotomic polynomials*, arXiv:2611.22795, first public November 17, 2026; used here as later supporting literature, not as the dated motivating source. https://arxiv.org/html/2611.22795v1
