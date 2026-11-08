# Exact 3-rank strata and finite-field counts for genus-three hyperelliptic curves with an extra involution

## Finding
Let \(k\) be an algebraically closed field of characteristic \(3\). In the marked family
\[
C_{a,b,c}:\quad y^2=x^8+a x^6+b x^4+c x^2+1,
\]
let \(U\subset\mathbb A_k^3\) be the open subset on which \(g(u)=u^4+a u^3+b u^2+c u+1\) is squarefree, so \(C_{a,b,c}\) is smooth of genus \(3\). Its Jacobian has 3-rank \(f\) given by
\[
 f=\begin{cases}
 3,&b\ne0,\ ac\ne1,\\
 2,&(b=0,\ ac\ne1)\ \text{or}\ (b\ne0,\ ac=1,\ a^4+1\ne0),\\
 1,&b\ne0,\ ac=1,\ a^4+1=0.
 \end{cases}
\]
In particular, no smooth member has 3-rank zero. The nonordinary divisor in \(U\) is \(V(b(ac-1))\); it is a reduced disjoint union of two smooth irreducible divisors. Its 3-rank-one locus consists, over \(k\), of four disjoint punctured affine lines, parametrized by \(a^4=-1\), \(c=a^{-1}\), and \(b\in k^\times\). The \(a\)-number equals \(3-\operatorname{rank}(H)\), hence is \(0\) at ordinary members and \(1\) at every nonordinary smooth member.

For every \(q=3^n\), \(n\ge1\), define \(r_q=0\) if \(n\) is odd and \(r_q=4\) if \(n\) is even. The numbers \(N_f(q)\) of smooth **marked coefficient triples** \((a,b,c)\in\mathbb F_q^3\) with 3-rank \(f\) are exactly
\[
\begin{aligned}
N_0(q)&=0,\\
N_1(q)&=r_q(q-1),\\
N_2(q)&=2q^2-4q+3-r_q(q-2),\\
N_3(q)&=q^3-3q^2+5q-5-r_q.
\end{aligned}
\]
Their sum is \(\#U(\mathbb F_q)=q^3-q^2+q-2\). These counts distinguish marked equations and are not counts of curve isomorphism classes.

## Assumptions and scope
All curves are smooth projective completions of the indicated affine hyperelliptic equations, with squarefree degree-eight right-hand side and leading and constant coefficient equal to \(1\). The characteristic is exactly \(3\), so the sign involution \((x,y)\mapsto(-x,y)\) is tame and distinct from the hyperelliptic involution. The parameter-space statements concern the indicated affine coefficient coordinates, with no quotient by coordinate changes. The 3-rank is \(\dim_{\mathbb F_3}J(C)[3](\overline{k})\); the \(a\)-number is \(\dim_k\operatorname{Hom}(\alpha_3,J(C)[3])\). The rank-one geometric decomposition of the locus is after base change to an algebraically closed field; over \(\mathbb F_{3^n}\) it has rational points only when \(n\) is even.

## Proof
**(1) Cartier/Hasse–Witt calculation.** For odd-degree differentials \(\omega_i=x^i\,dx/y\), \(i=0,1,2\), the Cartier–Manin matrix in characteristic \(3\), before taking inverse Frobenius roots, is obtained by taking the coefficients of \(x^{3i-j}\) in \(f(x)^{(3-1)/2}=f(x)\), where \(f(x)=x^8+a x^6+b x^4+c x^2+1\). As all odd coefficients vanish, this gives (in the indicated row/column convention, up to transpose, which does not affect the ensuing rank claims)
\[
H=\begin{pmatrix}c&0&1\\0&b&0\\1&0&a\end{pmatrix}.
\]
The semilinear Frobenius-stable rank, equivalently the 3-rank, is the eventual rank of \(H H^{(3)}\cdots H^{(3^{s-1})}\), for sufficiently large \(s\). The middle summand is a one-dimensional semilinear map with multiplier \(b\): its stable rank is \(1\) if \(b\ne0\), otherwise \(0\). The other two coordinates form \(T=\left(\begin{smallmatrix}c&1\\1&a\end{smallmatrix}\right)\), with determinant \(ac-1\). If the determinant is nonzero, this summand has stable rank \(2\). If \(ac=1\), write \(T=v w^{\mathsf T}\), where \(v=(c,1)^{\mathsf T}\) and \(w=(1,a)^{\mathsf T}\). Then
\[
TT^{(3)}=(a+c^3)\,v(w^{(3)})^{\mathsf T}.
\]
For \(ac=1\), the vanishing of \(a+c^3\) is equivalent to \(a^4+1=0\). Otherwise every semilinear power has rank one; when it vanishes the block is nilpotent of index two under Frobenius and has stable rank zero. This proves the claimed cases, provided their parameters belong to the smooth locus.

**(2) Smoothness and disjoint divisors.** The degree-eight polynomial \(f(x)=g(x^2)\) is squarefree exactly when \(g(u)\) is squarefree, because \(x\mapsto x^2\) is separable away from \(x=0\) and \(g(0)=1\). If \(b=0\), then \(g'(u)=u^3+c\). At its unique geometric critical point \(s\), where \(s^3=-c\), one obtains \(g(s)=1-ac\). Consequently \(b=0\) meets \(U\) precisely when \(ac\ne1\). In particular, \(b=0=ac-1\) never lies in \(U\).

When \(ac=1\) (so \(a,c\ne0\)), factor
\[
g(u)=(u+a)(u^3+c)+bu^2.
\]
For \(b\ne0\), a common root of \(g\) and \(g'=u^3+c-bu\) must satisfy \(u=a\), and such a common root exists precisely when \(b=a^2+c^2\). Thus the smooth locus on \(ac=1\) is
\[
a\in k^\times,\quad c=a^{-1},\quad b\notin\{0,a^2+a^{-2}\}.
\]
This is a smooth irreducible open subset of \(\mathbb G_m\times\mathbb A^1\). The other nonordinary component, \(b=0,ac\ne1\), is smooth and irreducible. Their disjointness makes \(b(ac-1)=0\) a reduced smooth divisor with two connected components. If \(a^4+1=0\), then \(a^2+a^{-2}=0\), so every \(b\ne0\) is smooth; there are four distinct roots of \(a^4+1\) over \(k\), giving four disjoint \(\mathbb G_m\)'s. Finally \(H\) has rank \(3\) if \(b(ac-1)\ne0\), and rank \(2\) otherwise on \(U\), proving the \(a\)-number assertion. No smooth point can satisfy \(b=0\) and \(ac=1\), so the 3-rank cannot be zero.

**(3) Squarefree marked-polynomial count.** Let \(Q=q\), and sum over monic polynomials with nonzero constant coefficient the multiplicative character of their constant term. For the trivial character, the generating series over *all* monic nonzero-constant polynomials is \(L_1(T)=(1-T)/(1-QT)\); for each nontrivial character, the generating series is \(L_\chi(T)=1\). The squarefree series is \(F_\chi(T)=L_\chi(T)/L_{\chi^2}(T^2)\), by unique factorization into a squarefree factor times a square. Extracting degree four yields: for the trivial character, \([T^4]F_1=(Q-1)^2(Q^2+1)\); for the quadratic character, \([T^4]F_\chi=1-Q\); for all other nontrivial characters, the coefficient is \(0\). Character orthogonality for the nonzero constant coefficient \(1\), dividing by \(Q-1\), therefore gives
\[
\#U(\mathbb F_Q)=\frac{(Q-1)^2(Q^2+1)+(1-Q)}{Q-1}=Q^3-Q^2+Q-2.
\]
This is the number of monic squarefree quartics with constant \(1\), in bijection with the marked smooth triples.

**(4) Stratum counts.** The smooth points with \(b=0\) number \(q^2-(q-1)=q^2-q+1\). On \(ac=1\), for each \(a\ne0\), the forbidden values of \(b\) are \(0\) and \(a^2+a^{-2}\), coinciding exactly when \(a^4=-1\). Hence the smooth points on this divisor number \((q-1)(q-2)+r_q\), and exactly \(r_q(q-1)\) of them have rank one. Since the divisors are disjoint on \(U\), subtracting those two divisor counts from \(\#U\) gives \(N_3\); the remainder of the nonordinary locus gives \(N_2\). Explicitly, the number of fourth roots of \(-1\) in \(\mathbb F_{3^n}\) is \(4\) if \(n\) is even, and \(0\) if \(n\) is odd, since \(\mathbb F_q^\times\) is cyclic. These computations give exactly the four formulas in the Finding.

## Verification
The standalone pure-Python file `verify_octic.py` constructs finite fields of sizes \(3\), \(9\), and \(27\), enumerates each coefficient triple, determines quartic squarefreeness by polynomial greatest common divisors, constructs the semilinear Hasse–Witt matrices, checks stable ranks, and compares independent enumerations with the symbolic formulas. Re-running `python3 verify_octic.py` produces the recorded text `verification_output.txt` and ends in `ALL_CHECKS_PASSED`. Counts of smooth triples and ranks \((N_0,N_1,N_2,N_3)\) are respectively \(19;(0,0,9,10)\), \(655;(0,32,101,522)\), and \(18979;(0,0,1353,17626)\). The finite checks are corroborative only; infinite-field statements follow from the proof above.

## Relationship to prior work
Gutierrez–Shaska, *Hyperelliptic curves with extra involutions* (arXiv:math/0601456), gives the normalized even-polynomial form and its involution quotients; these foundational facts are not claimed as novel. Gutierrez–Sevilla–Shaska, *Hyperelliptic curves of genus 3 with prescribed automorphism group* (arXiv:1209.2938), studies automorphisms and coefficients, not the characteristic-three strata counted here. Elkin–Pries, *Hyperelliptic curves with a-number 1 in small characteristic*, proves the broader genus-three characteristic-three bound that the \(a\)-number is at most one and gives general 3-rank-zero criteria in another model; neither the general bound nor general Cartier computations are claimed as new. The present addition is the exact marked extra-involution subfamily's 3-rank stratification, geometric rank-one locus, and all-extension finite-field counts. Literature on arbitrary double elliptic covers allows different objects and does not imply this restricted hyperelliptic coefficient-space calculation. Historical priority against other unindexed or inaccessible specialized literature is not independently certified.

## Limitations
These are counts of equations with fixed normalization, not moduli-space isomorphism classes or an unmarked automorphism quotient. In particular, coordinate transformations can identify different counted triples. The result holds in characteristic three for the squarefree family; singular equations are deliberately excluded. The assertion about geometric components uses an algebraically closed field. Only 3-rank and \(a\)-number are classified; the full Ekedahl–Oort and Newton-polygon stratifications are not asserted here. The mathematical result has undergone only self-review, not independent auditing or external priority certification.

## References
1. J. Gutierrez and T. Shaska, *Hyperelliptic curves with extra involutions*, arXiv:math/0601456, version first publicly posted 2006-01-18, https://arxiv.org/abs/math/0601456.
2. J. Gutierrez, D. Sevilla and T. Shaska, *Hyperelliptic curves of genus 3 with prescribed automorphism group*, arXiv:1209.2938, https://arxiv.org/abs/1209.2938.
3. A. Elkin and R. Pries, *Hyperelliptic curves with a-number 1 in small characteristic*, Algebra & Number Theory (2007), especially Lemmas 3.2–3.3.
