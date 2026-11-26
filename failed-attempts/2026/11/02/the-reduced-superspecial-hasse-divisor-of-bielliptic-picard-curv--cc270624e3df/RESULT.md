# The reduced superspecial Hasse divisor of bielliptic Picard curves at inert primes

## Finding

Let \(p=6m+5\) be any prime (\(m\geq0\)), let \(k\) be algebraically closed of characteristic \(p\), and let
\[
 C_{a,b}:\quad y^3=x^4+a x^2+b,
 \qquad b(a^2-4b)\ne0,
\]
denote the smooth projective genus-three curve. Define
\[
 H_m(a,b)=[z^{3m+2}](z^2+az+b)^{2m+1}
 =\sum_{h=0}^{\lfloor m/2\rfloor}
 \frac{(2m+1)!}{(m+1+h)!(m-2h)!h!}\,a^{m-2h}b^h
 \quad\text{in }\mathbb F_p[a,b].
\]
(The case \(m=0\) means \(H_0=1\).) The Jacobian has **exactly two possible arithmetic strata**:
\[
 (f_p(C_{a,b}),a(C_{a,b}))=
 \begin{cases}
 (2,1),& H_m(a,b)\ne0,\\
 (0,3),& H_m(a,b)=0.
 \end{cases}
\]
Here \(f_p\) is the geometric \(p\)-rank and \(a\) the \(a\)-number. Hence the zero locus is **precisely the superspecial genus-three Jacobian locus** of this family. There is no intermediate \(p\)-rank or \(a\)-number. The elliptic quotient by \((x,y)\mapsto(-x,y)\) is supersingular throughout, while the associated Prym abelian surface is ordinary off the divisor and superspecial on it.

For every \(m\geq1\), the normalized Hasse polynomial \(H_m(a,1)\) has degree \(m\) and exactly \(m\) distinct roots over \(k\), none equal to \(2\) or \(-2\). The superspecial locus therefore lies entirely in the smooth parameter space and is geometrically reduced on the normalized coefficient line. Under **marked** coefficient isomorphisms
\[
 (a,b)\sim(t^6a,t^{12}b),\qquad t\in k^\times,
\]
there are exactly \(\lceil m/2\rceil\) superspecial classes. Precisely one of these has \(a=0\) when \(m\) is odd; none has \(a=0\) when \(m\) is even. The classification is for marked curves, not an asserted classification of all unmarked isomorphism classes.

The critical nontrivial polynomial identity, valid in \(\mathbb F_p[a,b]\), is
\[
 [z^{3m+2}](z^2+az+b)^{4m+3}
 =c_m\,b^{m+1}(a^2-4b)^{m+1}H_m(a,b),
 \quad c_m=\frac{\binom{4m+3}{m+1}}{\binom{2m+1}{m}}\in\mathbb F_p^\times.
\]
All denominators are invertible since their factorial arguments are below \(p\).

## Assumptions and scope

The prime is congruent to \(5\) modulo \(6\); this is disjoint from the split-prime congruence considered in other work. The field is algebraically closed, and the smoothness hypothesis is exactly \(b(a^2-4b)\ne0\): the quartic \(x^4+ax^2+b\) then has four simple roots. The cyclic degree-three map to the \(x\)-line ramifies at these four roots and infinity, so Riemann–Hurwitz gives genus \(3\). The \(p\)-rank is the stable rank of the semilinear Cartier operator on holomorphic differentials, while the \(a\)-number is the dimension of its kernel. Superspeciality of a Jacobian is equivalent to vanishing of the Cartier operator on all holomorphic differentials. Marked isomorphisms are required to preserve the distinguished \(\mu_6\)-action.

## Proof

**1. The exact Cartier matrix.** Set \(f(x)=x^4+ax^2+b=g(x^2)\), with \(g(z)=z^2+az+b\). A basis of regular differentials is
\[
 \omega_1=dx/y,\qquad \omega_2=dx/y^2,\qquad \omega_3=x\,dx/y^2.
\]
For \(p=6m+5\), put \(r=4m+3\), \(s=2m+1\), and \(d=3m+2=(p-1)/2\). Because \(3r=2p-1\) and \(3s=p-2\), the Cartier rules \(\mathcal C(u^p\omega)=u\mathcal C(\omega)\) and \(\mathcal C(x^{pi+p-1}dx)=x^i dx\), together with the fact that \(f\) contains only even powers, give
\[
 \begin{aligned}
 \mathcal C(\omega_1)&=A^{1/p}\omega_2,
 &A&=[z^d]g(z)^r,\\
 \mathcal C(\omega_2)&=B^{1/p}\omega_1,
 &B&=[z^d]g(z)^s=H_m(a,b),\\
 \mathcal C(\omega_3)&=0.
 \end{aligned}
\]
Indeed, the only possible source exponent is \(p-1=2d\) in the first two rows. In the third, \(xf(x)^s\) has only odd powers and degree \(8m+5<2p-1\), so no exponent congruent to \(p-1\) occurs. This also verifies the row and column normalization of the Cartier matrix; coefficients are understood with inverse Frobenius on \(k\).

**2. A coefficient differential equation.** For nonnegative integers \(r,j\), let \(F_{r,j}(u)=[z^j](z^2+uz+1)^r\). Direct multinomial coefficient comparison yields
\[
 (u^2-4)F_{r,j}''(u)-(2r-1)u F_{r,j}'(u)
 +j(2r-j)F_{r,j}(u)=0.
 \tag{1}
\]
For completeness, the coefficient \(c_i\) of \(u^i\) in \(F_{r,j}\) satisfies
\[
 (i-j)(i-(2r-j))c_i=4(i+2)(i+1)c_{i+2},
\]
which is precisely the coefficient equation of (1), including both boundary parities. Apply this first to \(B_1(u)=H_m(u,1)=F_{2m+1,d}(u)\). It obeys
\[
 (u^2-4)B_1''-(4m+1)u B_1'+m(3m+2)B_1=0.
 \tag{2}
\]
The leading coefficient of \(B_1\) is \(\binom{2m+1}{m}\ne0\), hence \(\deg B_1=m\).

**3. The discriminant divisibility.** Put \(A_1(u)=F_{4m+3,d}(u)\). For \(0\le j\le m\), differentiating at \(u=2\) yields
\[
 A_1^{(j)}(2)=(4m+3)_{\underline j}
 \binom{8m+6-2j}{3m+2-j}.
\]
Since \(8m+6-2j=p+(2m+1-2j)\) and \(3m+2-j<p\) is strictly greater than \(2m+1-2j\), Lucas' congruence makes this binomial zero modulo \(p\). The same argument at \(u=-2\) gives vanishing through derivative order \(m\) there. Because \(m<p\), this proves
\[
 (u^2-4)^{m+1}\mid A_1(u).
\]
Write \(A_1=(u^2-4)^{m+1}R(u)\). Its degree is at most \(3m+2\), so \(\deg R\le m\).

**4. Identification of the quotient.** The differential equation (1) for \(A_1\) has coefficients \(-(8m+5)u\) and \((3m+2)(5m+4)\). On substituting \(A_1=(u^2-4)^{m+1}R\), the extra term proportional to \(u^2/(u^2-4)\) has coefficient \(-2(m+1)(6m+5)\), hence vanishes in characteristic \(p\); the remaining equation reduces to (2) for \(R\), because
\[
 4(m+1)-(8m+5)=-(4m+1),\quad
 2(m+1)+(3m+2)(5m+4)\equiv m(3m+2)\pmod p.
\]
Among polynomials of degree at most \(m\), equation (2) has a one-dimensional solution space. In fact, its coefficient recurrence is
\[
 (i-m)(i-3m-2)c_i=4(i+2)(i+1)c_{i+2};
\]
for every \(i<m\) the product on the left is nonzero modulo \(p\), so the leading coefficient determines every lower coefficient, and the opposite parity vanishes. As \(B_1\) is one nonzero solution, \(R=c_m B_1\). Comparing leading coefficients of \(u^{3m+2}\) in \(A_1\) and \((u^2-4)^{m+1}B_1\) gives the stated scalar \(c_m\). Weighted homogeneity, or the substitution \(z=\sqrt b\,w\), \(u=a/\sqrt b\), extends the identity to all \(a,b\) with \(b\ne0\), and polynomiality extends it to \(\mathbb F_p[a,b]\).

**5. Cartier ranks and geometric strata.** On the smooth locus \(b(a^2-4b)\ne0\), step 4 shows \(A=0\iff B=0\). If both vanish, the full Cartier operator is zero, so the Jacobian has \(p\)-rank zero and \(a\)-number three, hence is superspecial. Otherwise Cartier is invertible on \(\langle\omega_1,\omega_2\rangle\) and zero on \(\omega_3\); its stable rank is exactly two and its kernel dimension one. The involution \(x\mapsto-x\) is \(-1\) on \(\omega_1,\omega_2\) and \(+1\) on \(\omega_3\). It yields a genus-one quotient with zero Cartier operator, and the complementary Prym factor, under an isogeny of degree a power of two prime to \(p\), inherits precisely the two-dimensional Cartier block. This proves the asserted elliptic/Prym statements.

**6. Squarefreeness and counting marked classes.** At either \(u=2\) or \(u=-2\), \(g(z)=(z\pm1)^2\), so
\[
 B_1(\pm2)=(\pm1)^m\binom{4m+2}{m}\ne0\pmod p.
\]
If a root \(u_0\notin\{\pm2\}\) were multiple, equation (2), differentiated repeatedly, would force every derivative of \(B_1\) to vanish at \(u_0\), contrary to \(\deg B_1=m<p\). Thus all \(m\) roots are simple and smooth. The formula for \(H_m\) has only powers of \(u\) of parity \(m\); moreover, its constant coefficient is nonzero when \(m\) is even. Therefore the roots pair under \(u\mapsto-u\), with one fixed root \(u=0\) exactly when \(m\) is odd. The marked scaling equivalence, after choosing \(b=1\), is precisely \(u\sim-u\), proving \(\lceil m/2\rceil\).

## Verification

Run the included standalone standard-library script with `python3 verify_picard_inert.py`. It constructs the exact bivariate coefficient tables and checks the identity in step 4, squarefreeness, nonvanishing at the smooth boundary, and coefficient ranks for 23 primes \(p\equiv5\pmod6\), from \(5\) through \(197\). The final emitted marker is `PICARD_INERT_PRIME_CARTIER_CHECKS_PASS`. The script tests only finitely many characteristics; the all-prime theorem follows from the symbolic arguments above. No claim about the full Newton polynomial, finite-field point frequencies, or unmarked curve-isomorphism classes is made.

## Relationship to prior work

Laga and Shnidman (2023 preprint, §2) establish the bielliptic Picard family, its marked scaling law, Prym construction, and quaternionic multiplication. Those results, the smoothness criterion, and the genus-one quotient are not claimed as new. Nourozi and Rahmati (2023 preprint, §3) give a general Cartier-matrix setup for Picard curves and state a uniform \(a\)-number conclusion for \(p\equiv2\pmod3\); that conclusion does not give this exceptional divisor and is incompatible with the previously known special Fermat example at \(p\equiv11\pmod{12}\). Kazemifard and Tafazolian (2015, theorem on \(y^3=x^4-1\)) classify the single special coefficient \(a=0\) in residue classes modulo \(12\), including its superspeciality for \(p\equiv11\pmod{12}\). The present claim excludes novelty for that isolated special curve and instead concerns the uniform *complete, reduced, all-inert-prime superspecial locus* on the entire marked bielliptic pencil. A separate split-prime coefficient theorem for \(p\equiv1\pmod6\) has disjoint prime scope; it does not imply this inert-prime result.

## Limitations

The classification assumes an algebraically closed field, primes \(p\equiv5\pmod6\), and the smooth locus. It counts marked isomorphism classes only. It does not determine full Newton polygons off the superspecial locus beyond their \(p\)-ranks, nor finite-field distributions of roots by extension degree. Literature comparisons cannot exclude every unindexed or differently parametrized calculation; independent mathematical validation has not been performed.

## References

1. J. Laga and A. Shnidman, *The geometry and arithmetic of bielliptic Picard curves*, arXiv:2308.15297v1 (29 August 2023); see §§2–4 in the accessible expanded arXiv v3. https://arxiv.org/abs/2308.15297
2. V. Nourozi and F. Rahmati, *The Rank of the Cartier operator on Picard Curves*, arXiv:2306.07823v1 (13 June 2023), §3. https://arxiv.org/abs/2306.07823
3. A. Kazemifard and S. Tafazolian, *A note on some Picard curves over finite fields*, Finite Fields and Their Applications 34 (2015), 107–122, doi:10.1016/j.ffa.2014.12.002 (fixed Fermat model only). https://doi.org/10.1016/j.ffa.2014.12.002
