# A sharp 65-coincidence plateau for Padovan and Perrin residues

## Finding
Let \(P_0=P_1=P_2=1\) and \(R_0=3,R_1=0,R_2=2\), with both sequences satisfying \(X_{n+3}=X_{n+1}+X_n\). For every integer \(k\ge1\), their difference sequence has least period \(T_k=7\cdot2^{k-1}\) modulo \(2^k\). The number of indices in one period where the two terms agree is exactly
\[
C_k=\#\{0\le n<T_k:P_n\equiv R_n\pmod{2^k}\}=
\begin{cases}
3,&k=1,\\
1+2^{\lfloor(k-1)/2\rfloor},&2\le k\le11,\\
65,&k\ge12.
\end{cases}
\]
There exists a **unique** \(\alpha\in\mathbb Z_2\) with \(\alpha\equiv32\pmod{64}\) such that, for every nonnegative integer \(t\),
\[
\nu_2(P_{7t+5}-R_{7t+5})=1+\nu_2(t+1)+\nu_2(t+1-\alpha).
\]
Here \(\nu_2(0)=+\infty\), though for nonnegative \(t\) the terms in the displayed equality are finite. The second 2-adic root accounts for the stabilization: for all \(k\ge13\), the 64 coincidences from the index class \(5\pmod7\) form two disjoint 32-element groups, one lifting the ordinary negative-index equality \(P_{-2}=R_{-2}\), the other lifting the genuinely 2-adic equality at index parameter \(\alpha-1\). A separate exact integer equality \(P_4=R_4=2\) contributes the remaining one index in every period.

## Assumptions and scope
All indices defining \(C_k\) are nonnegative. The prime is two; no result for odd prime moduli is asserted. The recurrence may be extended uniquely to negative indices because its companion matrix has determinant one. The 2-adic root \(\alpha\) is defined by an explicitly convergent function below, rather than by an unproved integer equation. The result counts congruences at matching indices, not all pairs of independent indices.

## Proof
Write \(D_n=P_n-R_n\), \(w=(-2,1,-1)^\mathsf T\), and
\[
M=\begin{pmatrix}0&1&0\\0&0&1\\1&1&0\end{pmatrix},\quad
M^7=I+2B,\qquad B=\begin{pmatrix}0&1&1\\1&1&1\\1&2&1\end{pmatrix}.
\]
Then \(D_n=e_1^\mathsf T M^n w\). Squaring yields \(M^{14}=I+4(B+B^2)\). Consequently, if \(d>0\), \(h=\nu_2(d)\), and \(s\ge0\), then
\[
\frac{D_{7(s+d)+r}-D_{7s+r}}{2^{h+1}}\equiv
\begin{cases}
e_1^\mathsf T M^rBw,&h=0,\\
e_1^\mathsf T M^r(B+B^2)w,&h\ge1
\end{cases}\pmod2.
\]
This follows from \((M^7)^d\equiv I+2B\pmod4\) for odd \(d\), and \((M^7)^d\equiv I+2^{h+1}(B+B^2)\pmod{2^{h+2}}\) for even \(d\); \(M^{7s}\equiv I\pmod2\). Direct multiplication shows both right-hand sides are odd for \(r=4\). Since \(D_4=0\), we obtain \(\nu_2(D_{7t+4})=1+\nu_2(t)\) for every positive integer \(t\). The seven initial parities are \((0,1,1,1,0,0,1)\), and \(D_{7t}\equiv2\pmod4\). Thus for \(k\ge2\), congruence zero is possible only for indices \(4\) or \(5\pmod7\), and the former class contributes exactly one index per full period.

For the latter class put \(u=t+1\) and \(w'=M^{-2}w=(0,1,-2)^\mathsf T\). The matrix binomial series converges on \(\mathbb Z_2\) and defines
\[
F(u)=e_1^\mathsf T(I+2B)^u w'=\sum_{j\ge0}2^j c_j\binom uj,
\qquad c_j=e_1^\mathsf T B^j w'.
\]
Since \(c_0=0\), \(F(u)=2uH(u)\), where
\[
H(u)=\sum_{j\ge1}\frac{2^{j-1}c_j}{j}\binom{u-1}{j-1}
=\sum_{j\ge1}\frac{2^{j-1}c_j}{j!}\prod_{i=1}^{j-1}(u-i).
\]
Uniform convergence holds because \(\nu_2(2^{j-1}/j)=j-1-\nu_2(j)\to\infty\), while the generalized binomial coefficients are 2-adic integers. The first four exact coefficients are \(c_1=-1,c_2=-1,c_3=-5,c_4=-14\). The first two terms of \(H\) equal \(-u\). The coefficients of the third and fourth polynomial terms are even 2-adic integers; every later coefficient \(2^{j-1}c_j/j!\) is integral. For \(j\ge5\), the polynomial \(Q_{j-1}(u)=\prod_{i=1}^{j-1}(u-i)\) has at least two even factors for every \(u\in\mathbb Z_2\). Hence \(Q_{j-1}\) takes even values and has even derivative. If \(u-v\) is odd, both values are even; if \(u-v\) is even, Taylor expansion with integral coefficients shows \(Q_{j-1}(u)-Q_{j-1}(v)\in2(u-v)\mathbb Z_2\). It follows by summation that
\[
H(u)-H(v)\equiv-(u-v)\pmod{2^{\nu_2(u-v)+1}}
\]
for all distinct \(u,v\in\mathbb Z_2\). Thus \(H\) is an exact 2-adic isometry; its reductions modulo every \(2^m\) are permutations, so it has one root \(\alpha\in\mathbb Z_2\) and \(\nu_2(H(u))=\nu_2(u-\alpha)\).

Evaluating \(H(0)=\sum_{j\ge1}(-1)^{j-1}2^{j-1}c_j/j\) modulo 64 needs only \(j\le8\), since every subsequent summand is divisible by 64. The exact coefficients \(c_1,\ldots,c_8=(-1,-1,-5,-14,-44,-135,-416,-1281)\) give \(H(0)\equiv32\pmod{64}\). Since \(H\) is an isometry and \(H(\alpha)=0\), \(\nu_2(\alpha)=5\). Finally, \(F(t+1)=D_{7t+5}\), proving the two-root valuation formula.

The parities have least period seven. Matrix lifting gives \(M^{7\cdot2^{k-1}}\equiv I\pmod{2^k}\). Conversely any period of \(D_n\) modulo \(2^k\) must be a multiple of seven; applying it to \(D_4=0\) and using the exact \(4\pmod7\) valuation forces the multiple to be divisible by \(2^{k-1}\). Hence the claimed least period is exact.

To count zeros, put \(m=k-1\) and let \(u\) range over a complete residue set modulo \(2^m\). The \(5\pmod7\) condition is \(\nu_2(u)+\nu_2(u-\alpha)\ge m\). Because \(\nu_2(\alpha)=5\), for \(1\le m\le10\) this is exactly \(u\equiv0\pmod{2^{\lceil m/2\rceil}}\), giving \(2^{\lfloor m/2\rfloor}\) solutions. At \(m=11\) it is \(u\equiv0\pmod{32}\), giving 64 solutions. For every \(m\ge12\), it is the disjoint union \(u\equiv0\pmod{2^{m-5}}\) and \(u\equiv\alpha\pmod{2^{m-5}}\); each contains exactly 32 residue classes modulo \(2^m\). Add the unique \(4\pmod7\) zero. For \(k=1\), the three even entries in the initial parity period establish \(C_1=3\).

## Verification
The standalone file `check.py` verifies the exact seventh matrix power, the relevant derivative parity identities, parity and mod-four exclusions, the explicit auxiliary coefficients, the root certificate \(H(0)\equiv32\pmod{64}\), all complete congruence counts for \(1\le k\le12\), and finite exact valuation/isometry comparisons. The infinite theorem rests on the preceding convergence, derivative and 2-adic-counting proof, not on finite enumeration. Run `python3 check.py` in the directory containing this document.

## Relationship to prior work
Bravo's 2023 open-access work determines actual integer common values of Padovan and Perrin sequences; it does not establish the frequency of same-index congruences modulo powers of two. Bravo and Irmak (2024), especially Lemmas 3.5–3.6, determine first-order dyadic congruences for the individual sequences and valuations of \(P_n-1\) and \(R_n+1\). These results provide related lifting background, but do not evaluate the second-order cancellation of \(P_n-R_n\), its second 2-adic zero, or the eventual 65-count. The present result is limited to this simultaneous same-index invariant. The prior general period \(7\cdot2^{k-1}\) is credited rather than claimed as new.

## Limitations
This is a self-reviewed mathematical argument, not an independent audit. Novelty comparison cannot exclude unindexed implicit evaluations of the exact same simultaneous congruence problem. The second root \(\alpha\) is 2-adic and is not asserted to be an ordinary integer; no assertion is made about different-index equality or odd primes.

## References
- Eric Fernando Bravo, *Common Values of Padovan and Perrin Sequences*, Mediterranean Journal of Mathematics 20, article 268 (published 17 July 2023), https://doi.org/10.1007/s00009-023-02467-2 .
- Eric Bravo and Nurettin Irmak, *The 2-adic valuation of shifted Padovan and Perrin numbers and applications*, Turkish Journal of Mathematics 48 (2024), 1183–1196, https://doi.org/10.55730/1300-0098.3568 .
