# Affine gap-spectrum law and second-largest gap for \(\Phi_{35p}\)

## Finding

For every prime \(p>35\), write \(p=35q+r\), where \(q\ge1\) and \(r\) is one of the 24 units modulo \(35\). If \(H_g(p)\) denotes the number of consecutive nonzero monomials of the cyclotomic polynomial \(\Phi_{35p}(X)\) with exponent separation \(g\), then, for every integer \(g\ge1\),
\[
H_g(p)=B_g(r)+(q-1)A_g(r).
\]
Both \(A_g(r)\) and \(B_g(r)\) are explicitly determined by a constant-size finite formula given below. Their complete 24-by-24 numerical table is `gap_spectrum_35.csv`, with columns `r,gap,base,slope`. Entries for \(g>24\) are zero.

Furthermore, the largest separation is \(24\), with exactly \(2q\) occurrences; the **second-largest distinct** separation is
\[
 s_r=24-\min\{r,35-r\}.
\]
In particular no gap strictly between \(s_r\) and \(24\) occurs. The exact second-largest-gap multiplicity is \(a_rq+b_r\), where the 24 values of \((r,a_r,b_r)\) are:

| \(r\) | \(a_r\) | \(b_r\) |
|:--:|:--:|:--:|
| 1, 2, 3, 4, 6 | 8 | 0 |
| 8 | 10 | 2 |
| 9, 11, 12, 13 | 8 | 2 |
| 16, 17 | 10 | 4 |
| 18, 19 | 10 | 6 |
| 22, 23, 24, 26 | 8 | 6 |
| 27 | 10 | 8 |
| 29, 31, 32, 33, 34 | 8 | 8 |

These are formulas for gaps between **nonzero coefficients**, not for coefficient magnitude or isolated zero terms.

## Assumptions and scope

Let \(\Phi_n(X)\) be the monic cyclotomic polynomial of order \(n\). Define \(C_e=[X^e]\Phi_{35}(X)\) for \(0\le e\le24\), with \(C_e=0\) outside this range. The known integer coefficient list (in increasing exponent order) is

`[1,-1,0,0,0,1,-1,1,-1,0,1,-1,1,-1,1,0,-1,1,-1,1,0,0,0,-1,1]`.

For integer \(t\), define a 35-periodic function \(h(t)\) by \(h(t)=1\) if \(t\equiv0,1,2,3,4\pmod{35}\), \(h(t)=-1\) if \(t\equiv7,8,9,10,11\pmod{35}\), and \(h(t)=0\) otherwise. For \(0\le j\le23\), \(0\le t<35\), and a unit residue \(r\), put
\[
 w_{j,r}(t)=\sum_{e=0}^{j}C_e h((j-e)r+t).
\]
For any nonzero 35-term integer word \(w\), let \(\operatorname{cyc}_g(w)\) be the number of cyclic distances of length \(g\) between successive nonzero entries, including the wraparound distance. Define
\[
 A_g(r)=\sum_{j=0}^{23}\operatorname{cyc}_g(w_{j,r}).
\]
For each unit \(r\), let \(Q_r(X)=\Phi_{35}(X^{35+r})/\Phi_{35}(X)\), an integer polynomial because \(\gcd(35+r,35)=1\). Define \(B_g(r)\) to be the ordinary noncyclic gap count in its nonzero coefficient support. These definitions give every table entry without requiring a prime search. All 24 words \(w_{j,r}\) have nonzero entries, so the cyclic distances are defined.

## Proof

The cyclotomic factor identity for a prime \(p\nmid35\) is
\[
 \Phi_{35p}(X)=\frac{\Phi_{35}(X^p)}{\Phi_{35}(X)}.
\]
Directly from the factorization \(\Phi_{35}(X)=(1-X^{35})(1-X)/((1-X^5)(1-X^7))\), its reciprocal has the formal power series
\[
 \frac1{\Phi_{35}(X)}=\frac{(1-X^5)(1-X^7)}{(1-X)(1-X^{35})}=\sum_{n\ge0}h(n)X^n.
\]
Consequently the coefficient of \(X^n\) in \(\Phi_{35p}\) equals \(\sum_{0\le e\le24,\,ep\le n}C_eh(n-ep)\). In the \(j\)-th length-\(p\) block, \(n=jp+t\), \(0\le j\le23\), \(0\le t<p\), this becomes \(w_{j,r}(t\bmod35)\). The final block is truncated at the true degree \(24(p-1)\), and its highest coefficient is one.

Increasing \(q\) by one while keeping \(r\) fixed inserts one entire period of each of these 24 coefficient words. For every nonempty cyclic word, insertion of one whole period contributes exactly its cyclic gap histogram to internal gaps; the gaps across adjacent block boundaries are unchanged because the support patterns at each boundary retain their fixed 35-periodic offsets, including at the truncated final block. Therefore the total histogram changes by exactly \(\sum_{j=0}^{23}\operatorname{cyc}_g(w_{j,r})\). Starting from \(q=1\) proves the affine law for every \(q\ge1\), and hence for every eligible prime.

For the concrete second-largest gap assertions, there remain only 24 residue cases and 24 coefficient words per case. The standard-library checker `word_gaps_verify.py` performs exact integer arithmetic: it forms the 35-periodic words, checks their supports are nonempty, evaluates cyclic histograms, and independently divides \(\Phi_{35}(X^{35+r})\) by \(\Phi_{35}(X)\) using its constant-term-one coefficient recurrence. It verifies every CSV entry, that the maximum support gap is \(24\) with \(B_{24}(r)=A_{24}(r)=2\), the claimed value of \(s_r\), absence of any intermediate gap, and \(A_{s_r}(r)=a_r\), \(B_{s_r}(r)-A_{s_r}(r)=b_r\). The 24 finite cases are **exhaustive** because they are precisely the units modulo 35; the universal dependence on \(q\) was proved separately above. The computation has no primality oracle or external-library dependency.

## Verification

Run `python3 word_gaps_verify.py` with `gap_spectrum_35.csv` in the same directory. The 576 table entries are reconstructed and compared exactly. As separate finite cross-checks (not as substitutes for the preceding infinite argument), the checker verifies division identities, full coefficient lists and gap histograms for all 24 residue classes and \(q=1,2,3\). All tests passed during preparation.

## Relationship to prior work

Al-Kateeb, Ambrosino, Hong and Lee prove the general **largest-gap** theorem \(\max g=\varphi(35)=24\) for squarefree odd \(m\) and prime \(p>m\), and develop block relations (2019); that maximum is not new here. The article *The ternary cyclotomic polynomials \(\Phi_{3pq}\)* obtains maximum-gap multiplicities for families whose **smallest prime factor is 3**, and treats \(\Phi_{15p}\) in particular; it does not contain the 5·7·p family. Cafure and Cesaratto study second-largest gaps and some complete frequency formulas for **binary** \(\Phi_{pq}\), not ternary \(\Phi_{35p}\). The OEIS entry A011634 supplies the already known coefficients of \(\Phi_{35}\), not this gap classification. The new claim is the constant-size affine formula for **every gap frequency** in the 35p family and the exact second distinct gap and its multiplicity.

## Limitations

The finite certificate establishes the concrete 24-case classifications; it does not by itself prove the infinite affine relation, for which the block-period argument is essential. This result only concerns prime \(p>35\), not arbitrary composite multipliers or all ternary cyclotomic polynomials. No global novelty or priority guarantee can be inferred from limited database coverage. Independent mathematical review has not been performed.

## References

1. A. Al-Kateeb, M. Ambrosino, H. Hong, E. Lee, *Maximum gap in cyclotomic polynomials*, 2019, https://arxiv.org/abs/1911.11667 (first public 2019-11-26).
2. *The ternary cyclotomic polynomials \(\Phi_{3pq}\)*, institutional open manuscript, https://orbilu.uni.lu/bitstream/10993/55534/1/Article_cyclotomic-preprint.pdf.
3. A. Cafure, E. Cesaratto, *Gaps in binary cyclotomic polynomials*, https://arxiv.org/abs/2507.19381.
4. O.-M. Camburu, E.-A. Ciolan, F. Luca, P. Moree, I. E. Shparlinski, *Cyclotomic coefficients: gaps and jumps*, arXiv:1507.07098, https://arxiv.org/abs/1507.07098.
5. OEIS A011634, *35th cyclotomic polynomial*, https://oeis.org/A011634.
