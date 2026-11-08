# All-even sharp norms for three consecutive characters and the exact finite-order aliasing barrier

## Finding
Let \(G\) be a compact abelian group with normalized Haar probability measure, and let \(\chi:G\to\mathbb T\) be a continuous character of finite order \(q\ge3\), or of infinite order. For an integer \(h\ge2\), consider
\[
F(g)=a+b\chi(g)+c\chi(g)^2,\qquad S=|a|^2+|b|^2+|c|^2.
\]
Define the positive-coefficient polynomial
\[
P_h(x)=\sum_{j=0}^{h} A_{h,j}x^j,\qquad
A_{h,j}=2^{-j}\binom{2h}{2j}\binom{2j}{j},
\]
and the polynomial of degree \(h-1\)
\[
Q_h(x)=(1+x)P'_h(x)-hP_h(x)
=\sum_{j=0}^{h-1}\frac{A_{h,j}(h-j)(2h-3j-2)}{j+1}x^j.
\]
There is exactly one positive root \(x_h\) of \(Q_h\). Set \(C_h=P_h(x_h)/(1+x_h)^h\). If \(q=\infty\) or \(q\ge2h+1\), the exact sharp inequality is
\[
\boxed{\int_G |F(g)|^{2h}\,d\mu(g)\le C_h S^h.}
\]
Every nonzero equality case, and only those, is
\[
\boxed{(a,b,c)=\lambda(\sqrt{x_h/2},\ \omega,\ \sqrt{x_h/2}\,\omega^2),
\quad \lambda\in\mathbb C\setminus\{0\},\quad |\omega|=1.}
\]
Thus all extremizers have equal endpoint magnitudes and aligned midpoint phases. For each finite order \(3\le q\le2h\), the sharp constant for the same three-character space is **strictly larger** than \(C_h\). Therefore the smallest finite order attaining the infinite-order constant is exactly \(2h+1\), for every \(h\ge2\).

The large-moment behavior is also sharp:
\[
\boxed{x_h=2-\frac{3}{2h}+O(h^{-2}),\qquad
C_h=3^h\sqrt{\frac{3}{8\pi h}}\bigl(1+O(h^{-1})\bigr),\quad h\to\infty.}
\]
These formulas specify a continuum of optimal even-moment inequalities through a single algebraic equation at every exponent, without asserting an elementary radical formula for its root.

## Assumptions and scope
The image of a finite-order character is the group of \(q\)-th roots of unity with uniform push-forward of Haar measure; an infinite-order character has full-circle uniform push-forward. No assumption on connectedness or dimension of \(G\) is needed. The distinctness condition \(q\ge3\) ensures the three characters \(1,\chi,\chi^2\) are distinct. The input coefficient norm is unweighted \(\ell^2\), and the output is normalized \(L^{2h}\). All complex phases and coefficient magnitudes are unrestricted. We determine the constant for \(q>2h\); for \(3\le q\le2h\) we prove a strict comparison rather than the exact larger norm.

## Proof
**1. Orthogonality, phases, and endpoint symmetrization.** If \(q>2h\) or \(q=\infty\), the powers \(\chi^k\), \(0\le k\le2h\), are distinct. Parseval applied to \(F^h\) gives
\[
\int_G|F|^{2h}\,d\mu=\sum_{k=0}^{2h}|[z^k](a+bz+cz^2)^h|^2.
\]
Every coefficient on the right is a sum of monomials with positive multinomial coefficients, so its modulus cannot increase if \(a,b,c\) are replaced by \(A=|a|,B=|b|,C=|c|\). Suppose all three magnitudes are positive. The coefficient of \(z^2\) includes the nonzero terms \(\binom h2 a^{h-2}b^2\) and \(h a^{h-1}c\); their alignment requires \(\arg a+\arg c\equiv2\arg b\pmod{2\pi}\). That relation aligns every pair of monomials with the same degree, hence it is necessary and sufficient for equality in every triangle inequality.

For nonnegative \(A,B,C\), put \(p=A^2+C^2\), \(u=AC\), and \(S=p+B^2\). On \(|z|=1\),
\[
|A+Bz+Cz^2|^2=S+B(A+C)(z+z^{-1})+u(z^2+z^{-2}).
\]
The constant term of its \(h\)-th power is a polynomial with nonnegative coefficients in \(S\), \(B^2(A+C)^2=B^2(p+2u)\), and \(u\). To see this, expand each term as a walk with steps \(0,\pm1,\pm2\); a zero-displacement walk uses an even number of odd steps, and the remaining combinatorial coefficients are nonnegative. With \(p\), \(B\), and hence \(S\) fixed, the constant term is nondecreasing in \(u\), and is strictly increasing for \(p>0\) and \(0\le u<p/2\). Indeed, if \(B>0\), the two opposite unit steps yield a strictly positive term proportional to \(B^2(p+2u)\); if \(B=0\), the two opposite double steps yield a strictly positive term proportional to \(u^2\), since \(h\ge2\). As \(u\le p/2\) by arithmetic-geometric mean, every positive-energy optimizer with \(p>0\) satisfies \(A=C>0\). The case \(p=0\) is the pure midpoint term and will be ruled out by the one-variable maximization.

**2. Exact one-variable reduction.** Normalize \(S=1\). For \(B>0\), put \(x=p/B^2=2A^2/B^2\). Equality of endpoint magnitudes implies
\[
B=(1+x)^{-1/2},\qquad A=C=\sqrt{x/[2(1+x)]}.
\]
The moment becomes
\[
M_h(x)=\frac{1}{2\pi}\int_0^{2\pi}
\left|\frac{1+\sqrt{2x}\cos\theta}{\sqrt{1+x}}\right|^{2h}d\theta
=\frac{P_h(x)}{(1+x)^h}.
\]
The polynomial follows by expanding the even power and using
\(\frac1{2\pi}\int_0^{2\pi}\cos^{2j}\theta\,d\theta=4^{-j}\binom{2j}{j}\).
The limiting case \(B=0\) is the endpoint \(x=\infty\), and \(p=0\) is \(x=0\).

Differentiation shows \(M'_h(x)=Q_h(x)/(1+x)^{h+1}\). The displayed coefficients of \(Q_h\) follow from
\[
\frac{A_{h,j+1}}{A_{h,j}}=\frac{(2h-2j)(2h-2j-1)}{2(j+1)^2}.
\]
For \(j=0,\ldots,h-1\), the coefficient sign is the sign of \(2h-3j-2\). Its first nonzero sign is positive and its last is negative, with exactly one variation after zero coefficients are discarded. Descartes' rule of signs therefore bounds the number of positive roots by one, counting multiplicity. Since \(Q_h(0)>0\) and the leading coefficient is negative, the intermediate-value theorem gives exactly one positive root \(x_h\), which is simple; \(M_h\) increases before and decreases after it. In particular \(x=0\) and \(x=\infty\) are not optimizers, so all three coefficients are necessarily nonzero. This proves the sharp constant and all equality cases including the phase relation in Step 1.

**3. Exact finite-order cutoff.** For \(q\ge2h+1\), orthogonality in Step 1 applies unchanged. For \(3\le q\le2h\), take the positive optimal coefficients from Step 2 and write
\( (a+bz+cz^2)^h=\sum_{k=0}^{2h}u_k z^k\).
All \(u_k\) are strictly positive. Orthogonality on the \(q\)-th roots yields
\[
\frac1q\sum_{j=0}^{q-1}|a+b\zeta_q^j+c\zeta_q^{2j}|^{2h}
=\sum_{r=0}^{q-1}\left(\sum_{\substack{0\le k\le2h\\k\equiv r\ (\mathrm{mod}\ q)}}u_k\right)^2
>\sum_{k=0}^{2h}u_k^2=C_h S^h.
\]
The inequality is strict because degrees \(0\) and \(q\) coexist in one residue class. Thus even the continuum extremizer exceeds \(C_h\) in every smaller finite order. This establishes the exact threshold without claiming those larger constants.

**4. Large-order asymptotics.** Uniformly for \(x\) in a fixed neighborhood of \(2\), Laplace's method at the unique dominant peak \(\theta=0\) gives, with one differentiated error bound,
\[
M_h(x)=\left(\frac{(1+\sqrt{2x})^2}{1+x}\right)^h
\sqrt{\frac{1+\sqrt{2x}}{4\pi h\sqrt{2x}}}\left(1+O(h^{-1})\right).
\]
For \(x\) near \(2\), the opposite-sign trough at \(\pi\) has strictly smaller absolute height. The leading exponential rate \(\ell(x)=2\log(1+\sqrt{2x})-\log(1+x)\) has unique global maximum \(\ell(2)=\log3\). Together with uniqueness of \(x_h\), elementary uniform moment bounds away from this maximum ensure \(x_h\to2\). Write the log-prefactor (omitting the \(x\)-independent factor) as \(\alpha(x)=\tfrac12\log((1+\sqrt{2x})/\sqrt{2x})\). Direct differentiation gives \(\ell''(2)=-1/36\) and \(\alpha'(2)=-1/24\). From the differentiated Laplace expansion,
\[
0=h\ell'(x_h)+\alpha'(x_h)+O(h^{-1})
\quad\Longrightarrow\quad x_h=2-\frac{3}{2h}+O(h^{-2}).
\]
Substituting into the undifferentiated expansion gives \(M_h(x_h)=3^h\sqrt{3/(8\pi h)}\,(1+O(h^{-1}))\), as claimed.

## Verification
Run `python3 artifacts/verify.py` from the extracted package root; only the Python standard library is required. It independently checks exact multinomial expansions and the derivative coefficient formula for integers \(2\le h\le15\), reproduces the unique-positive-root coefficient sign patterns, tests exact cyclic no-alias and alias effects, and compares the large-moment optimizer drift at \(h=20,40,70\). Successful output is `THREE_MODE_EVEN_MOMENTS_PASS exact_and_grid_checks=108 h=2..15`. The finite checks do not establish the unrestricted quantifiers; Steps 1–4 do.

For reference, the first moments give \(x_2=4/3\) and \(C_2=15/7\); the eighth moment has \(x_4\approx1.6368512043\) and \(C_4\approx13.7877239672\), agreeing with independently available special-exponent results.

## Relationship to prior work
Neuwirth's trigonometric trinomial studies determine sharp supremum-norm and Sidon behavior, rather than the entire family of coefficient-optimized even Fourier norms. Madiman and Xu determine unrestricted Fourier operator norms on compact and discrete abelian groups; restricting that operator to three consecutive characters and asking for its exact \(L^2\)-to-\(L^{2h}\) constant is a different optimization. Biswas and Stovall study sharp restriction to continuous monomial curves, also distinct from the three-character compact-group problem.

Existing sharp results determine the fourth-, sixth-, and eighth-moment versions separately, including the same optimal endpoint symmetry. A more general reflection root-mean-square majorization theorem already forces symmetric endpoint magnitudes for every even moment; **that symmetry is prior work, not claimed as new here**. The contribution is the complete all-\(h\) algebraic norm formula with a proof of one unique positive maximizing root, the exact threshold \(2h+1\) for finite-order characters, and the optimizer and constant asymptotics. Neither the isolated low-order formulas nor the general symmetry statement determines all these assertions. A comprehensive historical-priority certification is not asserted.

## Limitations
The theorem addresses exactly three consecutive characters and even integer exponents. The sharp value for orders \(3\le q\le2h\) is only bounded strictly below by \(C_h\), not computed. The asymptotic remainder is an ordinary large-integer-\(h\) estimate. Other finite-spectrum inequalities, including higher-dimensional or nonconsecutive configurations, need not reduce to one polynomial. Equivalent all-even formulas may exist in older special-function or Nikolskii literature under different notation, and the literature search is necessarily nonexhaustive.

## References
1. Mokshay Madiman and Peng Xu, *The norm of the Fourier transform on compact or discrete abelian groups*, arXiv:1611.04692v1, first public 2016-11-15, https://arxiv.org/html/1611.04692v1 .
2. Stefan Neuwirth, *The maximum modulus of a trigonometric trinomial*, arXiv:math/0703236v1, first public 2007-03-08, https://arxiv.org/abs/math/0703236 .
3. Chandan Biswas and Betsy Stovall, *Sharp Fourier restriction to monomial curves*, arXiv:2302.05317v1, first public 2023-02-10, https://arxiv.org/abs/2302.05317 .
4. *Exact \(\Lambda(4)\) constants for every three-character subset of a cyclic group*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-lambda-4-constants-for-every-three-character-subset-of-a-c--5562292e7127 .
5. *Sharp sixth moments and phase localization for three consecutive Fourier cosets*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-sixth-moments-and-phase-localization-for-three-consecutive--382775ed6a3d .
6. *Sharp \(L^8/L^2\) norm for the consecutive three-frequency spectrum*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-l-8-l-2-norm-for-the-consecutive-three-frequency-spectrum--69c7d8c4e990 .
7. *Reflection root-mean-square majorization of every even Fourier moment*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-reflection-root-mean-square-majorization-of-every-even-fourier-m--ce42dcffc673 .
