# The complete five-adic image and exact fibers of Morita's gamma function

## Finding

Let \(\Gamma _5:\mathbb Z_5\longrightarrow\mathbb Z_5^\times\) be Morita's continuous five-adic gamma function. Its entire value set is the disjoint union

\[
\boxed{\Gamma _5(\mathbb Z_5)=(1+5\mathbb Z_5)\sqcup(3+5\mathbb Z_5)\sqcup(-1+25\mathbb Z_5).}
\]

Consequently, for each integer \(k\ge2\), exactly \(11\cdot5^{k-2}\) residue classes modulo \(5^k\) occur. The normalized Haar measure on \(\mathbb Z_5\) of the image is \(11/25\).

More precisely, for each \(k\ge2\) and \(y\in\mathbb Z/5^k\mathbb Z\), the number of residues \(x\pmod{5^k}\) satisfying \(\Gamma _5(x)\equiv y\pmod{5^k}\) is

\[
\boxed{r_k(y)=2\mathbf1_{y\equiv1\,(5)}+\mathbf1_{y\equiv3\,(5)}+5\mathbf1_{y\equiv1\,(25)}+5\mathbf1_{y\equiv-1\,(25)}.}
\]

At level \(k=1\) the multiplicities for residues \(0,1,2,3,4\) are respectively \(0,3,0,1,1\). At every level \(k\ge1\), the least positive period in the input variable of \(\Gamma_5(x)\pmod{5^k}\) is exactly \(5^k\).

## Assumptions and scope

For an integer \(n\ge1\), define

\[
\Gamma _5(n)=(-1)^n\!\prod_{1\le j<n,\;5\nmid j}j,
\]

with \(\Gamma_5(0)=1\), extending to \(\mathbb Z_5\) by continuity. Here \(\nu_5(0)=\infty\), \(\mathbb Z_5\) denotes the five-adic integers, and \(\mathbf1_E\) is one or zero according as condition \(E\) holds or does not hold. Each asserted number of preimages concerns a complete residue period of length \(5^k\), not all nonnegative integer representatives. Haar measure is normalized by \(\mu(\mathbb Z_5)=1\). No assertion is made about other primes or about unrelated gamma analogues.

## Proof

**1. Periodicity and branch polynomials.** The standard functional equation is

\[
\frac{\Gamma_5(x+1)}{\Gamma_5(x)}=\begin{cases}-x,&x\in\mathbb Z_5^\times,\\-1,&x\in5\mathbb Z_5.\end{cases}
\]

For every positive integer \(m\), the product of all units modulo \(5^m\) is \(-1\); this follows by pairing a unit with its inverse, leaving just the solutions of \(u^2\equiv1\pmod{5^m}\). The \((-1)^{5^m}\) sign cancels it. Hence \(\Gamma_5(n+5^m)\equiv\Gamma_5(n)\pmod{5^m}\) for integers \(n\ge0\), and then for all five-adic inputs by continuity. In particular, reduction of the function modulo \(5^m\) depends only on the input residue.

For \(a=0,1,2,3,4\), put \(H_a(t)=\Gamma_5(a+5t)\) and \(U_a(t)=H_a(t+1)/H_a(t)\). The functional equation gives

\[
U_a(t)=-\!\prod_{\substack{0\le j\le4\\5\nmid a+j}}(a+j+5t).
\]

The five resulting polynomials, expanded over the integers, are

\[
\begin{aligned}
U_0(t)=U_1(t)&=-24-250t-875t^2-1250t^3-625t^4,\\
U_2(t)&=-144-900t-2000t^2-1875t^3-625t^4,\\
U_3(t)&=-504-2250t-3625t^2-2500t^3-625t^4,\\
U_4(t)&=-1344-4600t-5750t^2-3125t^3-625t^4.
\end{aligned}
\]

For \(a=0,1\), set \(\lambda_a=2\); for \(a=2,3,4\), set \(\lambda_a=1\). With \(c_a=-1,-1,1,-1,1\), respectively, direct inspection shows

\[
U_a(t)\equiv 1+c_a5^{\lambda_a}\pmod{5^{\lambda_a+1}}.
\]

Moreover, \(U_a(t)\equiv1\pmod5\). The five-adic logarithm therefore exists. The restricted power series

\[
L_a(t)=5^{-\lambda_a}\log U_a(t)\in\mathbb Z_5\langle t\rangle
\]

satisfies, for a polynomial \(P_a\in\mathbb Z_5[t]\) of degree at most two,

\[
L_a(t)\equiv c_a+5P_a(t)\pmod{25}.
\]

Indeed the displayed integer polynomials show that \((U_a-1)/5^{\lambda_a}\pmod{25}\) has degree at most two. Expanding the logarithm gives the same degree bound: when \(\lambda_a=1\), its quadratic-log term divided by five is five times a polynomial constant modulo five, and all higher terms vanish modulo \(25\); when \(\lambda_a=2\), all nonlinear-log terms vanish modulo \(25\).

**2. A complete-block logarithm lemma.** Let \(L(t)=c+5P(t)+25G(t)\), where \(c\in\mathbb Z_5\), \(P\) has degree at most two and \(G\in\mathbb Z_5\langle t\rangle\). For each \(s\ge1\) and \(t\in\mathbb Z_5\),

\[
\sum_{j=0}^{5^s-1}L(t+j)\equiv c5^s\pmod{5^{s+1}}.
\]

To see this, the sums of the constant, linear, and quadratic polynomials over any \(5^s\) consecutive integers are divisible by \(5^s\) (the denominators two and six in the usual formulas are units modulo five). Also, \(\sum_{j=0}^{5^s-1}G(t+j)\in5^{s-1}\mathbb Z_5\). The last assertion follows by induction: for \(s=1\) it is immediate; for larger \(s\), group \(j=j_0+h5^{s-1}\), with \(0\le j_0<5^{s-1}\) and \(0\le h<5\). Since a restricted integral power series is one-Lipschitz, the grouped sum is congruent to \(5\sum_{j_0=0}^{5^{s-1}-1}G(t+j_0)\pmod{5^{s-1}}\). This proves the assertion and the logarithm lemma.

**3. Exact five-adic distances on each input branch.** Apply the lemma to \(L_a\). For \(s\ge1\),

\[
\log\frac{H_a(t+5^s)}{H_a(t)}
=5^{\lambda_a}\sum_{j=0}^{5^s-1}L_a(t+j)
\equiv c_a5^{s+\lambda_a}\pmod{5^{s+\lambda_a+1}}.
\]

The same leading congruence holds for \(s=0\) directly from \(U_a\). Since five-adic logarithm and exponential preserve the first nonzero digit on \(1+5\mathbb Z_5\),

\[
\frac{H_a(t+5^s)}{H_a(t)}\equiv1+c_a5^{s+\lambda_a}\pmod{5^{s+\lambda_a+1}}.
\]

Taking products gives, first for any positive integer \(w\) not divisible by five and then for every \(w\in\mathbb Z_5^\times\) by continuity,

\[
\nu_5\big(H_a(t+5^sw)-H_a(t)\big)=s+\lambda_a.
\]

Thus for all distinct \(t,u\in\mathbb Z_5\),

\[
\boxed{\nu_5(H_a(t)-H_a(u))=\nu_5(t-u)+\lambda_a.}
\]

Each normalized branch \(t\mapsto(H_a(t)-H_a(0))/5^{\lambda_a}\) is therefore an isometry \(\mathbb Z_5\to\mathbb Z_5\). Every isometry of \(\mathbb Z_5\) into itself is surjective: for every \(m\), it induces an injective map on the finite set \(\mathbb Z/5^m\mathbb Z\), hence a bijection, and compactness supplies a compatible inverse. Consequently

\[
H_a(\mathbb Z_5)=H_a(0)+5^{\lambda_a}\mathbb Z_5.
\]

**4. Image, individual fibers, and sharp period.** The five branch centers are \((H_0(0),\ldots,H_4(0))=(1,-1,1,-2,6)\). Hence branches \(a=0,1\) cover the two disjoint balls \(1+25\mathbb Z_5\) and \(-1+25\mathbb Z_5\), while \(a=2,3,4\) cover \(1+5\mathbb Z_5\), \(3+5\mathbb Z_5\), and \(1+5\mathbb Z_5\), respectively. This proves the image decomposition.

Within an input branch modulo \(5^k\), the variable \(t\) runs over \(5^{k-1}\) residues. A branch with \(\lambda_a=1\) covers every output in its image once; a branch with \(\lambda_a=2\) covers every output in its image five times. Adding their contributions proves the fiber formula for \(k\ge2\), and direct reduction gives the level-one counts. There are \(2\cdot5^{k-1}+5^{k-2}\) distinct outputs and the limit of this proportion is \(11/25\).

The period \(5^k\) was established above. Conversely, a period modulo \(5^k\) must be divisible by five because the level-one output pattern is not constant, and every period modulo five has to be a multiple of five. Writing \(T=5q\), the isometry on the branch \(a=2\) gives \(\nu_5(\Gamma_5(2+T)-\Gamma_5(2))=\nu_5(T)\); thus a period modulo \(5^k\) must be a multiple of \(5^k\). This proves minimality.

## Verification

Execute `python3 gamma5_check.py`. It independently computes the reduced gamma sequence from the one-step recurrence and compares every output fiber with the formula for \(1\le k\le5\). It also checks the branch distance valuations and representative block products, using exact integer arithmetic. This diagnostic verifies finitely many residues; it does **not** certify the infinite theorem. The proof of all levels is Steps 1–4 above.

## Relationship to prior work

Morita introduced \(\Gamma_p\) and its continuous extension in 1975. Barsky's 1977 seminar describes local analyticity, including a radius, while Li–Reiter–Tang–Wang–Yi (2022) records the standard one-Lipschitz estimate for \(\Gamma_p\). The latter estimate gives an upper bound on distances, not the exact equality with the distinct \(\lambda_a\) for all five branches. Finat's distribution identity concerns the five-adic logarithmic gamma analogue rather than complete value sets of \(\Gamma_5\). The present result identifies the exact global codomain image and every finite-level multiplicity, neither of which follows merely from continuity, general local analyticity, or the one-Lipschitz inequality.

## Limitations

Only the prime five and Morita's normalization are treated. The new computation is exact at each prime-power level, but no assertion of historical uniqueness is made: Morita's original 1975 full text was not retrievable for full inspection, and broader treatments of \(p\)-adic gamma functions may contain implicit specializations. This should be checked before asserting historical priority. No independent mathematical audit or formal-machine proof has been performed.

## References

1. Y. Morita, *A p-adic analogue of the Γ-function*, Journal of the Faculty of Science, University of Tokyo, 22 (1975), 255–266, https://doi.org/10.15083/00039754 . Catalog publication date July 30, 1975.
2. D. Barsky, *On Morita's p-adic Γ-function*, Groupe d'étude d'analyse ultramétrique, 5 (1977–1978), talk dated November 7, 1977. https://www.numdam.org/article/GAU_1977-1978__5__A1_0.pdf .
3. E. Finat, *A distribution formula for Kashio's p-adic log-gamma function*, Journal of Number Theory 162 (2016), 463–482. https://doi.org/10.1016/j.jnt.2015.11.001 .
4. X. Li, J. Reiter, S. Tang, N. Wang and J. Yi, *P-adic incomplete gamma functions and Artin-Hasse-type series*, arXiv:2207.11806 (2022), especially Proposition 2.2. https://arxiv.org/abs/2207.11806 .
5. E. Adamus, *On the differential transcendentality of the Morita p-adic gamma function*, European Journal of Mathematics 9 (2023), article 7. https://doi.org/10.1007/s40879-023-00602-7 .
