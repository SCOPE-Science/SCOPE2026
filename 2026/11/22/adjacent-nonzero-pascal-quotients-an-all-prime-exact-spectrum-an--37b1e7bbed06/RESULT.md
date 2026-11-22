# Adjacent nonzero Pascal quotients: an all-prime exact spectrum and persistent quadratic dependence

## Finding

Let \(p\) be any prime and \(r\ge1\) an integer. For every pair of integers \(0\le k<n<p^r\) such that both \(\binom nk\) and \(\binom n{k+1}\) are nonzero modulo \(p\), form their ratio \(u=\binom nk\bigl(\binom n{k+1}\bigr)^{-1}\in\mathbb F_p^\times\). Let \(R_{p,r}(u)\) count these pairs with ratio \(u\), and put \(Q_p=p(p+1)/2\) and \(S_r=\sum_{j=0}^{r-1}Q_p^j=(Q_p^r-1)/(Q_p-1)\).

**Theorem (complete finite-depth ratio spectrum).** For every prime \(p\), integer \(r\ge1\), and nonzero residue \(u\) modulo \(p\),
\[
R_{p,r}(u)=\begin{cases}
(p-1)S_r,&u=-1\text{ in }\mathbb F_p,\\
\dfrac{p-1}{2}S_r,&u\ne-1\text{ in }\mathbb F_p.
\end{cases}
\]
For \(p=2\) there is only the first case. The total number of eligible adjacent pairs is \(p(p-1)S_r/2\). Hence the ratio \(-1\) has exact probability \(2/p\) and **every other nonzero ratio** has probability \(1/p\), at *every* depth \(r\), not merely in the limit.

**Quadratic-sign consequence.** For odd \(p\), let \(\chi_p\) be the Legendre character, extended by \(\chi_p(0)=0\). If a pair is selected uniformly among the eligible pairs, then
\[
\mathbb E\!\left[\chi_p\!\left(\binom nk\right)\chi_p\!\left(\binom n{k+1}\right)\right]=\frac{\chi_p(-1)}p.
\]
Each individual sign becomes balanced as \(r\to\infty\), but the two signs remain dependent. More precisely, for \(\sigma,\tau\in\{-1,1\}\),
\[
\lim_{r\to\infty}\Pr\!\left(\chi_p\!\left(\binom nk\right)=\sigma,\ \chi_p\!\left(\binom n{k+1}\right)=\tau\right)
=\frac{1+\sigma\tau\chi_p(-1)/p}{4}.
\]
The probabilities are conditional on the pair being eligible and refer to successive complete prime-power row cutoffs.

## Assumptions and scope

All binomial coefficients are ordinary integers. Only horizontally adjacent entries *in one row* are compared, with the final entry of each row excluded as it has no right-hand neighbor. Both entries must be units modulo \(p\), so the quotient is well-defined in \(\mathbb F_p^\times\). The ratio theorem includes \(p=2\); the quadratic-sign statements require an odd prime. No claims concern coefficients modulo \(p^a\) for \(a>1\), nor arbitrary incomplete row cutoffs.

## Proof

**1. The first nonterminal digit.** Write the base-\(p\) digits of \(n\) and \(k\) with exactly \(r\) positions, allowing leading zeros. Lucas's theorem says that \(\binom nk\not\equiv0\pmod p\) exactly when the digit of \(k\) does not exceed that of \(n\) in each position. The same holds for \(k+1\). Let \(t\) be the number of trailing base-\(p\) digits of \(k\) equal to \(p-1\). The case \(t=r\) is impossible for an eligible pair, since then \(k=p^r-1\) and \(k+1>n\). At all positions below \(t\), eligibility forces both digits of \(n\) and \(k\) to equal \(p-1\). At position \(t\), write \(n_t=d\) and \(k_t=e\). Eligibility is equivalent to \(0\le e<d\le p-1\). At every position above \(t\) the sole condition is \(0\le k_i\le n_i\le p-1\).

**2. Quotient reduction.** For the lower \(t\) positions, the two binomial digit factors are \(\binom{p-1}{p-1}=\binom{p-1}{0}=1\). Above position \(t\), the two digit factors coincide. Lucas's congruence therefore gives
\[
\frac{\binom nk}{\binom n{k+1}}\equiv
\frac{\binom de}{\binom d{e+1}}\equiv\frac{e+1}{d-e}\pmod p.
\]
There are \(Q_p=\sum_{d=0}^{p-1}(d+1)=p(p+1)/2\) possible digit pairs in each higher position. At the first nonterminal position set \(a=d-e\) and \(b=e+1\). Then \(a,b\ge1\), \(a+b=d+1\le p\), and the quotient is \(b/a\) in \(\mathbb F_p^\times\).

**3. A finite-field involution.** Fix any \(u\in\mathbb F_p^\times\). Among all \((a,b)\in\{1,\ldots,p-1\}^2\) with \(b\equiv ua\pmod p\), there are exactly \(p-1\) ordered pairs. The involution \((a,b)\mapsto(p-a,p-b)\) preserves their quotient and exchanges \(a+b<p\) with \(a+b>p\). If \(u\ne-1\), no pair is on the boundary \(a+b=p\), so exactly \((p-1)/2\) satisfy \(a+b\le p\). If \(u=-1\), all \(p-1\) pairs satisfy \(a+b=p\). This is the claimed local quotient spectrum. Summing \(Q_p^{r-t-1}\) over \(t=0,\ldots,r-1\) yields the complete formula and the total \(p(p-1)S_r/2\), for all \(p\), including \(p=2\).

**4. Character correlation and joint signs.** For any nontrivial multiplicative character \(\psi\) of \(\mathbb F_p^\times\), character orthogonality gives \(\sum_{u\in\mathbb F_p^\times}\psi(u)=0\). The ratio spectrum immediately implies that its conditional mean is \(\psi(-1)/p\). For the quadratic character, \(\chi_p(x/y)=\chi_p(x)\chi_p(y)\) on nonzero residues, yielding the stated exact correlation.

For the individual quadratic signs, define the *finite*, explicitly computable integer
\[
H_p=\sum_{d=0}^{p-1}\sum_{e=0}^{d}\chi_p\!\left(\binom de\right).
\]
Among eligible pairs, the signed sum in either coordinate equals
\[
(H_p-p)\sum_{j=0}^{r-1}H_p^j.
\]
Indeed, at the first nonterminal position the sum of either individual sign is the sum over all \(0\le e<d<p\), which is \(H_p-p\), since the omitted right endpoint of every row contributes \(+1\); and each higher digit contributes the common factor with signed total \(H_p\). The two coordinate sums agree by the symmetry \(\binom de=\binom d{d-e}\).

Set \(B_p=p(p-1)/2\), \(D_p=(p-1)\chi_p(-1)/2\), and \(T_r=\sum_{j=0}^{r-1}H_p^j\). The exact count of eligible sign pairs \((\sigma,\tau)\), with \(\sigma,\tau\in\{-1,1\}\), is therefore
\[
N_{\sigma,\tau}(p,r)=\frac{B_pS_r+(\sigma+\tau)(H_p-p)T_r+\sigma\tau D_pS_r}{4}.
\]
This is integer-valued since it is an inversion of four exact signed totals.

Finally \(|H_p|<Q_p\): the digit binomial coefficients include positive character values (for example \(\binom00=1\)) and negative values. When \(p\equiv3\pmod4\), \(\binom{p-1}1\equiv-1\) supplies a negative value. When \(p\equiv1\pmod4\), the values \(\binom{p-2}e\equiv(-1)^e(e+1)\pmod p\), as \(e\) runs from \(0\) to \(p-2\), include quadratic nonresidues. Consequently the individual sign means tend to zero relative to the eligible-pair count \(B_pS_r\), while the sign-product mean remains \(\chi_p(-1)/p\). Four-sign inversion proves the limiting joint distribution.

## Verification

The standalone direct-enumeration program `checker.py` uses exact Lucas digit products and field inverses to build the complete quotient histogram and compares it to the theorem for primes \(2,3,5,7,11,13\) and depths up to \(8,5,4,3,3,2\), respectively. It additionally tests the character correlation at all odd-prime depths and cross-checks Lucas evaluation against ordinary integer binomial coefficients. On the recorded package, it prints `CHECK_OK 57254`. These finite checks supplement, but cannot replace, the all-prime proof above. Run with `python3 checker.py`, using only the Python standard library.

## Relationship to prior work

Lucas's theorem supplies the digit congruence. Garfield and Wilf (1992) give multiplicative digit formulas for individual *rowwise* binomial residue counts and their quadratic-character imbalance; those formulas do not specify which entries are horizontally neighboring. Wilson (1998) and Barat and Grabner (2001) address distributions of individual Pascal entries and digital arithmetic; their general frameworks motivate examining local transitions. Lane (2023) provides another treatment of single-entry character distributions. The finding here is the **evaluated exact all-residue law for quotients of neighboring nonzero entries**, together with its persistent two-point character dependence. The possibility of an implicit earlier calculation in general digital-distribution literature is a historical-priority limitation.

## Limitations

The distribution concerns only a prime modulus, adjacent nonzero entries, and the complete initial blocks of \(p^r\) rows. It does not state equidistribution on each separate row, an unrestricted natural-density theorem for arbitrary cutoffs, or a prime-power-modulus analogue. The proof is elementary but its claimed priority is based on the specific comparisons described above; it is not an independent literature-certification claim. Access to the complete Barat--Grabner (2001) paper and Wilson (1998) paper was unavailable during comparison; neither abstract was treated as a full-text exclusion.

## References

1. R. Garfield and H. S. Wilf, *The Distribution of the Binomial Coefficient modulo p*, Journal of Number Theory 41 (1992), 1--5. https://doi.org/10.1016/0022-314X(92)90078-4 . Full text was available in a lawful public reading copy.
2. B. Wilson, *Asymptotic behavior of Pascal's triangle modulo a prime*, Acta Arithmetica 83 (1998), 105--116. https://doi.org/10.4064/aa-83-2-105-116 . Published metadata inspected; full text unavailable.
3. G. Barat and P. J. Grabner, *Distribution of Binomial Coefficients and Digital Functions*, Journal of the London Mathematical Society 64 (2001), 523--547. https://doi.org/10.1112/S0024610701002630 . Public-online record dated 30 January 2002; abstract inspected, complete text unavailable.
4. C. Lane, *Asymptotic Distribution of Residues in Pascal's Triangle mod p*, arXiv:2309.12942 (2023). https://arxiv.org/abs/2309.12942 . Complete accessible HTML manuscript inspected for comparison.
