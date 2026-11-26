# Paley-shell correlations for exponential local squares and the seven-adic Mersenne lag spectrum

## Finding
Let \(p\equiv3\pmod4\) be prime and \(a\ge2\) an integer coprime to \(p\). Set \(d=\operatorname{ord}_p(a)\) and assume \(\nu_p(a^d-1)=1\). For \(m\ge1\), set \(E(m)=1\) exactly when \(a^{dm}-1\) is a square in \(\mathbb Z_p\), and set \(E(m)=0\) otherwise. Define
\[
K_p(t)=\lim_{N\to\infty}\frac1N\sum_{m=1}^{N}E(m)E(m+t)\qquad(t\ge0).
\]
The limit exists. With \(\mu_p=1/(2(p+1))\) and \(b_p=(p-3)/(4p^2)+\mu_p/p^2\), its complete formula, independent of \(a\), is
\[
K_p(t)=\begin{cases}
\mu_p,&t=0,\\
0,&\nu_p(t)=0,\\
\mu_p(1-p^{-2j}),&\nu_p(t)=2j\ge2,\\
\mu_p(1-p^{-2j})+b_p p^{-2j},&\nu_p(t)=2j+1\ge1.
\end{cases}
\]
Every fixed-shift count equals \(NK_p(t)+O_{p,a,t}(\log(2N))\).

In particular, let \(I(n)\) indicate that the binary Mersenne number \(2^n-1\) is a square in \(\mathbb Z_7\) for \(n\ge0\). Its density is \(\rho=17/48\). The joint density
\[
J(h)=\lim_{N\to\infty}\frac1N\sum_{n=0}^{N-1}I(n)I(n+h)
\]
exists for every \(h\ge0\) and satisfies
\[
J(h)=\begin{cases}
1/48,&3\nmid h,\\
(1+K_7(h/3))/3,&3\mid h.
\end{cases}
\]
Thus the covariance \(J(h)-\rho^2\) is negative precisely when \(3\nmid h\), positive when \(3\mid h\). For positive lags, the complete distribution of the values of \(J(h)\) is: \(1/48\) with natural lag frequency \(2/3\), \(1/3\) with frequency \(2/7\), and, for each \(v\ge1\), the distinct value \((1+K_7(7^v))/3\) with frequency \(2/7^{v+1}\). These are all the values at positive lags. The sole accumulation point of the exceptional values is \(17/48=J(0)\).

## Assumptions and scope
A square in \(\mathbb Z_p\) means an element of the form \(z^2\) for some \(z\in\mathbb Z_p\), including zero. The prime and order hypotheses are essential; the theorem does not assert a formula for \(p\equiv1\pmod4\), a Wieferich pair with \(\nu_p(a^d-1)>1\), or arbitrary exponent shifts unrelated to \(d\). All natural densities are with respect to nonnegative integer indices; one exceptional zero exponent has no effect on a density. The singular valuation \(\nu_p(0)\) is never used in a finite-shift formula except through the explicitly defined case \(t=0\). For \(p=7,a=2\), the order is \(d=3\), and \((2^3-1)/7=1\).

## Proof
**1. Exponential square criterion.** Let \(c\equiv(a^d-1)/p\pmod p\), so \(c\not\equiv0\pmod p\). The lifting-the-exponent lemma yields, for every integer \(m\ge1\),
\[
\nu_p(a^{dm}-1)=1+\nu_p(m),\qquad
p^{-1-\nu_p(m)}(a^{dm}-1)\equiv c\,m/p^{\nu_p(m)}\pmod p.
\]
For odd primes, a nonzero \(p\)-adic integer is a square if and only if its valuation is even and its unit residue is a quadratic residue. Consequently
\[
E(m)=1\iff\nu_p(m)=2j+1\quad(j\ge0),\qquad
\chi_p\!\left(c\,m/p^{2j+1}\right)=1,
\]
where \(\chi_p\) denotes the Legendre character. This identity holds for all positive indices, not just a finite precision.

**2. The shell model.** Let \(\mathcal S\subset\mathbb Z_p\) be the union of the disjoint clopen balls from the criterion; zero is excluded. Define
\[
Q_c=\{u\in\mathbb F_p^\times:\chi_p(cu)=1\},\quad
A=\bigcup_{u\in Q_c}(pu+p^2\mathbb Z_p).
\]
Then \(\mathcal S=A\sqcup p^2\mathcal S\). Haar probability \(\mu(\mathbb Z_p)=1\) gives \(\mu(\mathcal S)=\frac{p-1}{2p^2}(1-p^{-2})^{-1}=1/(2(p+1))=\mu_p\). The character formula of step 1 says that \(E(m)=1_\mathcal S(m)\) for all \(m\ge1\).

**3. Difference-set input and mixed shells.** For every nonzero \(w\in\mathbb F_p\),
\[
|Q_c\cap(Q_c-w)|=\frac{p-3}{4}.
\]
To verify this, expand \(1_{Q_c}(x)=(1+\chi_p(cx)-1_{\{0\}}(x))/2\), use \(\sum_x\chi_p(x(x+w))=-1\), and use \(\chi_p(-1)=-1\) to cancel the two endpoint terms. Equivalently, the nonzero quadratic residues form a Paley difference set, and multiplication by \(c^{-1}\) does not change intersection multiplicities.

Write \(K_p(t)=\mu(\mathcal S\cap(\mathcal S-t))\). If \(\nu_p(t)=0\), the intersection is empty because every element of \(\mathcal S\) is divisible by \(p\). If \(\nu_p(t)=1\), the \(A\)-to-\(A\) overlap has measure \((p-3)/(4p^2)\). For the two mixed branches \(A\) against \(p^2\mathcal S\), exactly one is possible because \(\chi_p(-1)=-1\); its measure is \(\mu_p/p^2\). The deep-to-deep intersection is empty at this shift. Thus \(K_p(t)=b_p\) whenever \(\nu_p(t)=1\).

**4. Recursive shifts.** If \(\nu_p(t)\ge2\), the shift preserves each residue ball making up \(A\). It cannot mix \(A\) with \(p^2\mathcal S\), and translation by \(t\) on the latter scales to translation by \(t/p^2\) on \(\mathcal S\). Hence
\[
K_p(t)=\frac{p-1}{2p^2}+\frac1{p^2}K_p(t/p^2).
\]
Iterating until the shift becomes a unit (even valuation) or has valuation one (odd valuation) yields the stated cases. At \(t=0\), the intersection is \(\mathcal S\), giving \(K_p(0)=\mu_p\). All formulas depend only on \(p\), not on \(c\).

**5. Natural densities and discrepancy.** For a fixed positive integer shift, the pair indicator is the restriction to integers of two locally constant \(p\)-adic square-status indicators away from finitely many singular valuation centers. Truncate each valuation tower after \(r\) shells. The resulting function is periodic modulo a power of \(p\) and is a disjoint union of at most \(O_p(r)\) residue classes after intersections are grouped by the valuation of the two centers. Every residue class contributes its expected count within an additive error at most one. With \(r\) proportional to \(\log_p(2N+2t)\), any omitted shell contains at most \(O_{p,t}(1)\) sampled integer indices, by elementary divisibility. This establishes the asserted \(O_{p,a,t}(\log(2N))\) discrepancy, and the same argument for \(t=0\) gives the individual density.

**6. The Mersenne specialization.** Reduction modulo seven gives
\[
I(n)=\begin{cases}1,&n\equiv1\pmod3,\\0,&n\equiv2\pmod3,\\E(n/3),&n\equiv0\pmod3,\ n>0.\end{cases}
\]
At \(n=0\), \(I(0)=1\), an isolated exception. Since \(\mu_7=1/16\), averaging the three residue classes gives \(\rho=(1+\mu_7)/3=17/48\). If \(3\nmid h\), exactly one residue class can contribute, with density \(\mu_7/3=1/48\). If \(h=3t\), the class \(1\pmod3\) always contributes \(1/3\), and the class \(0\pmod3\) contributes \(K_7(t)/3\). Finally, among positive \(h\), \(2/3\) are nonmultiples of three, while the density for \(h=3t\) with \(\nu_7(t)=v\) is \((1/3)(6/7^{v+1})=2/7^{v+1}\). The formulas give the stated spectrum, covariance signs, and unique accumulation point. Distinctness follows by substituting \(\mu_7=1/16\) and \(b_7=17/784\): the even-valuation values lie below \(1/16\), the odd-valuation values lie between successive even ones, and their deviations from \(1/16\) are distinct. 

## Verification
The standalone `verify.py` performs direct modular-square checks using prime-power modular exponentiation and independent Legendre tests for several primes and thousands of exponents, all nonzero Paley-translate intersections, direct sampled block-pair counts, and the full Mersenne specialization at multiple shifts. Executing it prints `verify_output.txt`; these are finite consistency checks, not substitutes for the universal proof above. In particular, the exact values \(\mu_7=1/16\), \(K_7(7)=17/784\), \(J(1)=1/48\), \(J(3)=1/3\), and \(J(21)=267/784\) are independently checked.

## Relationship to prior work
The square-residue difference-set identity is classical and is used as an input, not claimed as new; Davenport (1932) treats distribution of power residues. Bennett and Levin's 2013 public preprint investigates the global perfect-power equation for geometric repunits and does not determine fixed-lag three-adic or seven-adic local-square indicators. Zaharescu (2003) proves Poissonian spacing/pair correlations for sequences of squares in local fields and in Section 3 counts ordered solutions of differences of squares; that weighted representation problem is not the indicator intersection of two valuation-shell unions arising from the same exponential exponent. The new assertion is the complete all-lag shell correlation, the \(O(\log N)\) cutoff, and its exact Mersenne sign/spectrum consequence. A more general existing theorem on intersections of \(p\)-adic square-indicator translates could imply the universal shell formula, and an equivalent digital-correlation presentation remains a historical-priority risk.

## Limitations
The result is a theorem about local squares, **not** ordinary integer squares of Mersenne numbers. Only non-Wieferich bases at primes \(p\equiv3\pmod4\) are covered; the p-adic density formula is not extended to other characteristics or the exceptional Wieferich case. No independent mathematical audit has been performed. The contribution uses classical LTE, Hensel's lemma, and a Paley difference-set identity; originality is asserted for their complete combination into an all-lag exponential-square law, not for those ingredients.

## References
- M. A. Bennett and A. Levin, *The Nagell–Ljunggren equation via Runge's method*, arXiv:1312.4037v1, first submitted December 14, 2013. https://arxiv.org/abs/1312.4037
- A. Zaharescu, *Pair Correlation of Squares in p-Adic Fields*, Canadian Journal of Mathematics **55** (2003), 432–448. https://doi.org/10.4153/CJM-2003-019-6
- H. Davenport, *On the Distribution of \(l\)-th Power Residues (mod \(p\))*, Journal of the London Mathematical Society **7** (1932), 117–121. https://doi.org/10.1112/jlms/s1-7.2.117
