# The first two extremal correlations of Pascal-row nondivisibility counts at odd primes

## Finding

For any odd prime \(p\), let \(F_p(n)\) be the number of entries of row \(n\) in Pascal's triangle not divisible by \(p\). For every integer \(L\ge1\), let \(X_L\) be uniform on \(\{0,\ldots,p^L-1\}\). For each fixed integer \(h\ge0\), let \(\rho_{p,L}(h)\) be the Pearson correlation between \(F_p(X_L)\) and \(F_p((X_L+h)\bmod p^L)\). Then the limit \(C_p(h)=\lim_{L\to\infty}\rho_{p,L}(h)\) exists and is rational for every fixed \(h\).

Writing
\[
B_p=\frac{p(p+1)(2p+1)}6,\qquad
U_{p,a}=\sum_{j=0}^{p-a-1}(j+1)(j+a+1),\qquad
V_{p,a}=\sum_{j=p-a}^{p-1}(j+1)(j+a+1-p)
\]
for \(0\le a<p\), its **exact recurrence** is
\[
C_p(0)=1,\quad C_p(1)=\frac{2(p+1)}{2p+5},\quad
C_p(a+pt)=\frac{U_{p,a}C_p(t)+V_{p,a}C_p(t+1)}{B_p}
\]
for \(a+pt\ge2\), \(0\le a<p\), \(t\ge0\). Every value is therefore given by a terminating rational calculation.

There are two strict extremal tiers over positive shifts:
\[
\max_{h\ge1}C_p(h)=\frac{2(p+1)}{2p+5},
\qquad\text{attained exactly when }h=p^k\text{ for }k\ge0,
\]
\[
\max_{\substack{h\ge1\\h\ne p^k\ (k\ge0)}} C_p(h)
=\frac{4p^4+4p^3+11p^2+11p+18}{p(p+1)(2p+1)(2p+5)},
\qquad\text{attained exactly when }h=2p^k\text{ for }k\ge0.
\]
Moreover \(C_p(h)>0\) for all \(h\ge1\), but \(\inf_{h\ge1}C_p(h)=0\).

For \(p=3\), the two levels are respectively \(8/11\) and \(97/154\); for \(p=5\), they are \(4/5\) and \(186/275\).

## Assumptions and scope

The prime \(p\) is any fixed odd rational prime; the displacement \(h\) is a fixed nonnegative integer when the cutoff \(L\) tends to infinity. The second variable is shifted **cyclically** modulo \(p^L\). Correlations are centered and divided by the respective variances. Since both cyclically shifted samples have the same distribution, the denominator is the positive variance of \(F_p(X_L)\). The maximum statements compare the resulting limits over all fixed positive integer displacements, not the finite-\(L\) correlations or displacements growing with \(L\).

## Proof

**1. Digit identity and finite cyclic convolution.** If \(n=\sum_{j\ge0}d_jp^j\) with \(0\le d_j<p\), Lucas's theorem (equivalently Fine's formula) gives \(F_p(n)=\prod_j(d_j+1)\). Leading zero digits contribute one. Put \(A_p=\sum_{j=0}^{p-1}(j+1)=p(p+1)/2\), and for \(L\ge0\) define
\[
H_L(h)=\sum_{n=0}^{p^L-1}F_p(n)F_p((n+h)\bmod p^L).
\]
Here \(H_0(h)=1\), since the only residue modulo one is zero. Writing \(h=a+pt\), the last digit \(j\) of \(n\) causes no carry if \(j+a<p\) and one carry if \(j+a\ge p\). Summing the two cases proves the exact finite identity
\[
H_L(a+pt)=U_{p,a}H_{L-1}(t)+V_{p,a}H_{L-1}(t+1).
\]
In particular \(H_L(0)=B_p^L\), \(\mathbb EF_p(X_L)=(A_p/p)^L\), and \(\mathbb E[F_p(X_L)^2]=(B_p/p)^L\). Thus with \(K_L(h)=H_L(h)/B_p^L\) and \(r_p=A_p^2/(pB_p)=3(p+1)/[2(2p+1)]\in(0,1)\), the **exact Pearson identity** is
\[
\rho_{p,L}(h)=\frac{K_L(h)-r_p^L}{1-r_p^L}.
\]

**2. Rational limiting kernel.** We have \(K_L(0)=1\). Since \(U_{p,1}=p(p^2-1)/3\), \(V_{p,1}=p\), and \(B_p>V_{p,1}\), the recursion
\[
K_L(1)=U_{p,1}/B_p+(V_{p,1}/B_p)K_{L-1}(1)
\]
converges to \(C_p(1)=U_{p,1}/(B_p-V_{p,1})=2(p+1)/(2p+5)\). For every \(h\ge2\), write \(h=a+pt\). Both \(t\) and \(t+1\) are strictly less than \(h\), except that for \(a=0\) the second coefficient is \(V_{p,0}=0\). Hence induction on \(h\) gives convergence of \(K_L(h)\) and the stated terminating recurrence. The Pearson limit is the same since \(r_p^L\to0\).

For a finite base-\(p\) digit string \(h=\sum_{i=0}^{m}a_ip^i\), rational evaluation can alternatively use \((C_p(h),C_p(h+1))^T=M_{a_0}\cdots M_{a_m}(1,C_p(1))^T\), where
\[
M_a=B_p^{-1}\begin{pmatrix}U_{p,a}&V_{p,a}\\ U_{p,a+1}&V_{p,a+1}\end{pmatrix}
\quad(0\le a\le p-2),\qquad
M_{p-1}=B_p^{-1}\begin{pmatrix}U_{p,p-1}&V_{p,p-1}\\0&B_p\end{pmatrix}.
\]

**3. Sharp first and second tiers.** All coefficients in the recurrence are positive where present, so \(C_p(h)>0\). Also, direct summation gives
\[
U_{p,a}+V_{p,a}=B_p-\frac{pa(p-a)}2,
\]
strictly less than \(B_p\) for \(1\le a<p\). For every \(h\ge1\), recursively removing zero base-\(p\) digits leaves the same \(C_p(h)\), because \(C_p(pt)=C_p(t)\).

For a single nonzero digit \(1\le a<p\),
\[
C_p(a)=[U_{p,a}+V_{p,a}C_p(1)]/B_p.
\]
Let \(C_1=C_p(1)\) and \(C_2=C_p(2)\). Direct evaluation yields
\[
C_2=\frac{4p^4+4p^3+11p^2+11p+18}{p(p+1)(2p+1)(2p+5)},\qquad
C_1-C_2=\frac{3(p-2)(2p^2+3p+3)}{p(p+1)(2p+1)(2p+5)}>0.
\]
For \(3\le a\le p-1\),
\[
C_2-C_p(a)=\frac{3(a-2)E_p(a)}{p(p+1)(2p+1)(2p+5)},
\quad E_p(a)=2p^3+p^2-p-3-a^2-2a(p^2+p+1).
\]
The polynomial \(E_p(a)\) decreases in \(a\ge0\), and \(E_p(p-1)=p-2>0\), making the difference strict. (The range is empty when \(p=3\).)

Finally, let \(h=a+pt\) with \(1\le a<p\) and \(t\ge1\). Induction on \(h\), using \(C_p(t),C_p(t+1)\le C_1\), gives
\[
C_p(h)\le\frac{U_{p,a}+V_{p,a}}{B_p}C_1
\le\frac{U_{p,1}+V_{p,1}}{B_p}C_1<C_2,
\]
because \(a(p-a)\ge p-1\) and the last strictly positive gap is
\[
C_2-C_1\frac{U_{p,1}+V_{p,1}}{B_p}
=\frac{3(p^2+p+6)}{p(p+1)(2p+1)(2p+5)}>0.
\]
Thus the only maximizing shifts at the first level are \(p^k\), and the only maximizing shifts among the remainder are \(2p^k\), for \(k\ge0\).

**4. Zero infimum.** For \(m\ge1\), take \(h_m=1+p+\cdots+p^{m-1}\). Set \(v_m=(C_p(h_m),C_p(h_m+1))^T\). Since \(p\ge3\),
\[
v_m=B_p^{-1}\begin{pmatrix}U_{p,1}&V_{p,1}\\U_{p,2}&V_{p,2}\end{pmatrix}v_{m-1},
\qquad v_0=(1,C_1)^T.
\]
Both row sums are strictly below one, by the preceding cyclic-dot-product identity. Thus \(\|v_m\|_\infty\le\theta_p^m\|v_0\|_\infty\), where \(\theta_p=\max_{a\in\{1,2\}}(U_{p,a}+V_{p,a})/B_p<1\). In particular \(C_p(h_m)\to0\), proving the infimum zero without attainment.

## Verification

The standalone `check.py` reconstructs cyclic mixed moments in two different ways: by direct integer digit products over complete base-\(p\) blocks and by the two-branch carry recursion. It also constructs small Pascal triangles modulo \(p\) by repeated addition, independently checking the Fine/Lucas digit formula, and uses exact rational arithmetic to test the limiting extremal classifications over bounded shift ranges. Running `python check.py` with Python 3's standard library produces a PASS line for each of \(p=3,5,7,11\). These finite checks are diagnostic, not a substitute for the all-prime argument above.

## Relationship to prior work

Fine's classical formula, as set out in Rowland's 2017 article, supplies the marginal digit product \(F_p(n)=\prod(d_i+1)\); it does not give two-row Pearson correlations. Lane's 2023 article studies character-weighted row totals and distribution of residues across Pascal's triangle; its full accessible HTML does not state a two-point shifted-correlation kernel or the two extremal tiers. Mathonet, Rigo, Stipulanti and Zénaïdi (2022) study **integers whose digits encode the complete Pascal row**, rather than the rowwise number of nonzero entries. An indexed binary-only result concerns \(p=2\); it neither implies the odd-prime second tier nor contains the odd-prime constants. The present claim is specifically the odd-prime hierarchy, not a reassertion of that binary case.

## Limitations

No uniform convergence in a shift growing with \(L\), no finite-cutoff extremal theorem, and no independence of row counts is asserted. The source and database comparisons establish originality only relative to the material inspected; an unindexed equivalent or a derivation hidden in broader digital-correlation work remains possible. Independent scientific review has not been performed.

## References

1. E. Rowland, *A matrix generalization of a theorem of Fine*, arXiv:1704.05872 (first posted 19 April 2017), https://arxiv.org/abs/1704.05872 .
2. C. Lane, *Asymptotic Distribution of Residues in Pascal's Triangle mod p* (arXiv:2309.12942; first posted 22 September 2023), https://arxiv.org/abs/2309.12942 .
3. P. Mathonet, M. Rigo, M. Stipulanti, N. Zénaïdi, *On digital sequences associated with Pascal's triangle*, arXiv:2201.06636 (first posted 17 January 2022), https://arxiv.org/abs/2201.06636 .
4. N. Fine, *Binomial coefficients modulo a prime*, Amer. Math. Monthly **54** (1947), 589–592; classic digit identity as stated in Reference 1.
