# Exact simultaneous local-square counts for adjacent tetrahedral numbers

## Finding

Let \(B(n)=\binom n3=n(n-1)(n-2)/6\), and let \(p\ge5\) be a rational prime. For each \(k\ge1\), define
\[
N_{p,k}=\#\{0\le n<p^k:B(n),B(n+1)\text{ are squares modulo }p^k\},
\]
where **zero counts as a square**. Set \(\chi=\chi_p\), the Legendre character extended by \(\chi(0)=0\), and let \(a_p=p+1-\#E(\mathbb F_p)\) be the Frobenius trace of the smooth elliptic curve
\[
E:Y^2=X(X-1)(X-2).
\]
Define
\[
R_p=\frac{p-6-\chi(-1)-2\chi(-2)-2\chi(6)a_p}{4},\qquad
u_p=\frac{1+\chi(-1)}2,\qquad
v_p=\frac{1+\chi(-2)}2,
\]
and the nonnegative integer
\[
Q_{p,k}=\frac{p-1}{2}\sum_{\substack{m\ge1\\2m<k}}p^{k-2m-1}.
\]
(The empty sum is zero.) Then the **exact simultaneous square count at every prime-power depth** is
\[
\boxed{N_{p,k}=R_pp^{k-1}+3+u_p+(1+u_p+2v_p)Q_{p,k}.}
\]
In particular, \(R_p\) is always a positive integer.

The corresponding one-point count \(M_{p,k}=\#\{0\le n<p^k:B(n)\text{ is a square modulo }p^k\}\) is
\[
\boxed{M_{p,k}=\frac{p-3-\chi(6)a_p}{2}p^{k-1}+3(1+Q_{p,k}).}
\]
The natural densities of simultaneous and individual square membership in \(\mathbb Z_p\) therefore exist and are respectively
\[
\delta_p=\frac{R_p}{p}+\frac{1+u_p+2v_p}{2p(p+1)},\qquad
\mu_p=\frac{p-3-\chi(6)a_p}{2p}+\frac{3}{2p(p+1)}.
\]
For every \(N\ge1\), the counts over \(0\le n<N\) equal \(\delta_pN+O_p(\log(2N))\) and \(\mu_pN+O_p(\log(2N))\), respectively.

A particularly explicit **mod-eight dependence reversal** occurs for primes \(p\equiv3\pmod4\). In that case \(a_p=0\) and \(\mu_p=(p-2)/(2(p+1))\). If \(I(n)\) indicates \(B(n)\in(\mathbb Z_p)^2\), then
\[
\operatorname{Cov}(I(n),I(n+1))=\delta_p-\mu_p^2=
\begin{cases}
-\dfrac{p^2+11p+1}{4p(p+1)^2}<0,&p\equiv3\pmod8,\\[3pt]
\dfrac{3p^2-7p-1}{4p(p+1)^2}>0,&p\equiv7\pmod8.
\end{cases}
\]
The covariance refers to the limiting natural density of indices, not a probability distribution on primes.

## Assumptions and scope

All indices are nonnegative integers; the polynomial \(B\) extends to \(\mathbb Z_p\) for every \(p\ge5\) because six is a unit. The polynomial \(B(n+1)\) is exactly the adjacent tetrahedral term. A square modulo \(p^k\) is a residue of \(z^2\pmod{p^k}\), including zero. A square in \(\mathbb Z_p\) is a square of a \(p\)-adic integer; away from zero this means even valuation and a square leading unit. The theorem is limited to primes at least five; it makes no claim about primes two and three. The coefficients of \(E\) are integral and its discriminant is nonzero for these primes.

## Proof

**1. Regular prime-field classes.** Put \(f(X)=B(X)\) and \(g(X)=B(X+1)\). Away from the four distinct residues \(S=\{-1,0,1,2\}\), both values are nonzero. The number \(R_p\) of indices where both values are quadratic residues is
\[
4R_p=\sum_{x\notin S}(1+\chi(f(x)))(1+\chi(g(x))).
\]
The first term is \(p-4\). Translation by one shows that each of the complete character sums \(\sum_x\chi(f(x))\) and \(\sum_x\chi(g(x))\) equals \(-\chi(6)a_p\), by the elliptic-curve point-count identity. On excluding \(S\), the two sums jointly lose \(\chi(f(-1))=\chi(-1)\) and \(\chi(g(2))=1\). Furthermore, for \(x\notin S\),
\[
\chi(f(x)g(x))=\chi((x-2)(x+1)).
\]
The complete sum of the right side is \(-1\), since the two roots are distinct: the substitution \(t=(x-2)/(x+1)\) sends \(x\ne-1\) bijectively onto \(\mathbb F_p\setminus\{1\}\) and preserves the character after removing a square factor. Omitting \(x=0,1\) subtracts \(2\chi(-2)\). Combining the four terms yields exactly
\[
4R_p=p-6-\chi(-1)-2\chi(-2)-2\chi(6)a_p.
\]
The number of nonzero quadratic-residue values of \(f(x)\) in nonsingular classes is \((p-3-\chi(6)a_p)/2\), because the three roots of \(f\) are simple.

**2. Four singular residue balls.** The four exceptional balls around \(-1,0,1,2\) do not overlap modulo \(p\). Near zero, the two polynomials have linear leading terms \(n/3\) and \(-n/6\); near one, their leading terms are \(-(n-1)/6\) and \((n-1)/3\). Hence in either ball the ratio of their leading units is square precisely when \(\chi(-2)=1\). Near two, only \(f\) vanishes, with a simple zero; \(g(2)=1\), so the unit companion is always a square. Near minus one, only \(g\) vanishes simply; the unit companion \(f(-1)=-1\) is a square precisely when \(\chi(-1)=1\). The analytic unit factors on each ball have fixed square characters (their reductions at the center), so no further restrictions arise by Hensel lifting.

In an allowed ball centered at \(r\), consider indices satisfying \(\nu_p(n-r)=j\), with \(1\le j<k\). Simultaneous squareness modulo \(p^k\) requires \(j\) even; for each such \(j\), exactly \((p-1)p^{k-j-1}/2\) indices work, because half the leading units modulo \(p\) have the required quadratic character. Thus each allowed ball contributes \(Q_{p,k}\) noncentral indices. The permitted balls are: the ball at two; the ball at minus one if \(u_p=1\); and both balls at zero and one if \(v_p=1\). This gives exactly \(1+u_p+2v_p\) copies of \(Q_{p,k}\). At an exact center modulo \(p^k\), the zero values are squares: zero, one, and two always qualify; minus one qualifies precisely if \(u_p=1\). These contribute \(3+u_p\) further indices. Each regular prime-field class contributes \(p^{k-1}\) indices by Hensel's lemma. This proves the claimed \(N_{p,k}\).

For the marginal count there are three simple root balls at \(0,1,2\); every central index contributes one, and each contributes \(Q_{p,k}\) further indices. All other square statuses lift freely. This proves \(M_{p,k}\).

**3. Limits and effective integer cutoffs.** Dividing by \(p^k\), the central terms disappear and
\[
\lim_{k\to\infty}\frac{Q_{p,k}}{p^k}
=\frac{p-1}{2}\sum_{m\ge1}p^{-2m-1}=\frac{1}{2p(p+1)}.
\]
It follows that the limits equal the asserted \(\delta_p\) and \(\mu_p\). These are also natural densities for ordinary positive indices: each regular residue class is periodic modulo \(p\), and an allowed singular annulus of order \(2m\) comprises \((p-1)/2\) progressions modulo \(p^{2m+1}\). Each of these contributes its expected fraction to \([0,N)\) with discrepancy at most one. Only \(O(\log_p(2N))\) annular levels can contain more than one index in that interval; the remaining tails contain only the few exact centers. Summing the discrepancies gives \(O_p(\log(2N))\). Translation by one leaves the limiting marginal density unchanged.

**4. Explicit mod-eight covariance.** The map \(x\mapsto2-x\) sends \(x(x-1)(x-2)\) to its negative. Hence \(a_p=0\) for \(p\equiv3\pmod4\). In this case the above formulas simplify to
\[
\mu_p=\frac{p-2}{2(p+1)},\qquad
\delta_p=\begin{cases}
\dfrac{p^2-6p-1}{4p(p+1)},&p\equiv3\pmod8,\\[3pt]
\dfrac{p^2-2p-1}{4p(p+1)},&p\equiv7\pmod8.
\end{cases}
\]
Subtracting \(\mu_p^2\) yields the two displayed covariance identities. Both inequalities are strict for the allowed primes.

**5. Positivity at every eligible prime.** By Hasse's bound \(|a_p|\le2\sqrt p\),
\[
R_p\ge\frac{p-9-4\sqrt p}{4}>0\qquad(p\ge37).
\]
For the remaining primes \(p=5,7,11,13,17,19,23,29,31\), direct application of the character-sum formula gives respectively \(R_p=1,1,1,5,3,3,5,11,7\). This finite list exhausts all smaller eligible primes. Therefore \(R_p>0\) for every \(p\ge5\), and the simultaneous \(p\)-adic square density is strictly positive.

## Verification

Run the standard-library-only `python3 verify.py` in the extracted package. It constructs the quadratic-residue set modulo each tested prime power, evaluates both integer tetrahedral polynomials independently for all indices in a complete period, and compares the direct marginal and joint counts against the closed formulas. It separately recomputes the elliptic character sum, the regular-class character count, and both covariance identities using exact rational arithmetic. The completed run checked 24 primes through 101 and 65 full prime-power moduli, plus all nine small-prime positivity cases. These finite tests are consistency checks; the preceding proof supplies all unrestricted statements.

## Relationship to prior work

Classical square criteria in odd \(p\)-adic fields determine when a *given* number is a square; they do not evaluate the two-point distribution of a cubic figurate sequence. Earlier modular-class studies of tetrahedral numbers concern individual terms and small rings. A published exact fiber theorem for \(\binom n3\) at all prime powers determines one-point output multiplicities, not the aligned joint events at \(n\) and \(n+1\). Classical consecutive-quadratic-residue counts concern the integers \(n,n+1\), rather than two neighboring cubic-polynomial values, and do not yield the singular-ball corrections. The present result evaluates that correlation, its all-depth counts, and the strict mod-eight covariance sign reversal.

## Limitations

No classification is asserted for primes two or three, and no simultaneous *ordinary integer-square* existence theorem follows from local positive density. The finite-field expression for primes congruent to one modulo four retains the Frobenius trace of a specified elliptic curve instead of expressing it through a chosen sum-of-two-squares representation. Classical general character-sum and \(p\)-adic lifting principles supply the method, so historical publication of an equivalent explicit specialization is a genuine residual originality risk. No independent mathematical audit or external certification is claimed.

## References

1. J. M. Casas, B. A. Omirov, U. A. Rozikov, *Solvability criteria for the equation* \(x^q=a\) *in the field of* \(p\)*-adic numbers*, arXiv:1102.2156 (first posted 2011-02-10), https://arxiv.org/abs/1102.2156. Theorem 2.9 discusses the classical local-square criterion.
2. J. V. Leyendekkers and A. G. Shannon, *The structure of geometric number sequences*, Notes on Number Theory and Discrete Mathematics 17(3) (2011), 31–37, https://nntdm.net/papers/nntdm-17/NNTDM-17-3-31-37.pdf.
3. *Exact residue fibers of tetrahedral numbers at every modulus*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-residue-fibers-of-tetrahedral-numbers-at-every-modulus--50d5c75c2d6e (one-point fibers, not aligned adjacent-square events).
4. X. Wang and H. Fang, *The Distribution Properties of Consecutive Quadratic Residue Sequences*, 2023, DOI:10.1155/2023/5253261, https://doi.org/10.1155/2023/5253261 (ordinary consecutive residue patterns, not tetrahedral values).
5. *Tetrahedral Number*, Wolfram MathWorld, https://mathworld.wolfram.com/TetrahedralNumber.html (definitions and classical ordinary-square context).
