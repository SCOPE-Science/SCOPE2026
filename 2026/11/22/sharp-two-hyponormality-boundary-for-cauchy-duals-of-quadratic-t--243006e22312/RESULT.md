# Sharp two-hyponormality boundary for Cauchy duals of quadratic three-isometric shifts

## Finding

For each \(a>0\) and \(b\ge0\), consider the polynomial and positive unilateral weighted shift

\[
P_{a,b}(x)=\frac{(x+a)^2+b^2}{a^2+b^2},\qquad
W_{a,b}e_n=\sqrt{\frac{P_{a,b}(n+1)}{P_{a,b}(n)}}\,e_{n+1}
\quad(n\ge0).
\]

The operator \(W_{a,b}\) is a bounded expansive **strict three-isometry**. Its Cauchy dual \(V_{a,b}=W_{a,b}(W_{a,b}^*W_{a,b})^{-1}\) is a contraction with moments

\[
m_n=\|V_{a,b}^{n}e_0\|^2
=\frac{a^2+b^2}{(n+a)^2+b^2}\quad(n\ge0).
\]

Define the explicit polynomial

\[
\begin{aligned}
F(u,y)={}&3u^3-12u^2+9u-2\\
&+(-15u^2+24u-9)y+(9u-12)y^2-5y^3.
\end{aligned}
\]

For every \(a>0\), there exists **exactly one** \(Y(a)>0\) with

\[
F((a+2)^2,Y(a))=0.
\]

The complete two-hyponormality classification is

\[
\boxed{\ V_{a,b}\text{ is two-hyponormal}
\quad\Longleftrightarrow\quad 0\le b^2\le Y(a).\ }
\]

At the equality boundary, its initial \(3\times3\) moment Hankel block is positive semidefinite of rank two; every later shifted \(3\times3\) block is positive definite. The sharp one-hyponormality boundary is strictly larger:

\[
\boxed{\ V_{a,b}\text{ is hyponormal}
\quad\Longleftrightarrow\quad
b^2\le(a+1)^2-\tfrac12,\qquad
0<Y(a)<(a+1)^2-\tfrac12.\ }
\]

The Cauchy dual is subnormal **exactly when** \(b=0\). Consequently the entire open parameter region \(a>0\), \(0<b^2<Y(a)\) consists of two-hyponormal, non-subnormal Cauchy duals of strict three-isometries. In particular, \(a=b=1\) gives the simple moments \(m_n=2/((n+1)^2+1)\) and lies strictly inside this region, since \(F(9,1)=350>0\).

There is also a sharp large-displacement scaling law

\[
\lim_{a\to\infty}\frac{Y(a)}{a^2}=r_*=0.227023580871\ldots,
\]

where \(r_*\) is the unique positive root of \(3-15r+9r^2-5r^3=0\). Thus the ratio between the two-hyponormal and one-hyponormal critical values of \(b\) tends to \(\sqrt{r_*}=0.4764699\ldots\), strictly below one.

## Assumptions and scope

The underlying Hilbert space is \(\ell^2(\mathbb N_0)\) with standard basis \((e_n)\). All parameters satisfy \(a>0\), \(b\ge0\); there are no integrality assumptions. Two-hyponormal means the standard operator-matrix condition involving \(V\) and \(V^2\), not weak quadratic hyponormality. A bounded unilateral weighted shift with moments \((m_n)\) is \(k\)-hyponormal if and only if every \((k+1)\times(k+1)\) shifted Hankel matrix \((m_{n+i+j})_{0\le i,j\le k}\) is positive semidefinite, for every integer \(n\ge0\) [1]. We use that standard criterion.

The degree-two moment polynomial makes \(W_{a,b}\) a strict three-isometry: for every \(n,j\ge0\), the squared norm \(\|W_{a,b}^{j}e_n\|^2=P_{a,b}(n+j)/P_{a,b}(n)\) is quadratic in \(j\), so its third forward difference vanishes and its second does not. The weights are strictly greater than one and tend to one; thus \(W_{a,b}\) is bounded below, and its Cauchy dual is well-defined and contractive.

## Proof

**1. Exact Hankel minors.** Put \(x=n+a>0\), \(y=b^2\ge0\), and \(r_j=((x+j)^2+y)^{-1}\). The common positive multiplier \(a^2+b^2\) in the moments does not affect Hankel positivity. Elementary rational determinant expansion gives

\[
\det\begin{pmatrix}r_0&r_1\\r_1&r_2\end{pmatrix}
=\frac{2(x+1)^2-2y-1}{(x^2+y)((x+1)^2+y)^2((x+2)^2+y)}
\]

and

\[
\det(r_{i+j})_{i,j=0}^2
=\frac{8F((x+2)^2,y)}{
\prod_{j=0}^4\big((x+j)^2+y\big)^{d_j}},
\qquad(d_0,d_1,d_2,d_3,d_4)=(1,2,3,2,1).
\]

Every denominator is strictly positive. The first formula and the positivity of the leading diagonal entries give exactly the stated one-hyponormality boundary. For the size-three blocks, the leading first and second principal minors, together with the determinant, determine positive semidefiniteness whenever the leading second minor is strictly positive (by a Schur complement).

**2. Existence and uniqueness of the cubic boundary.** For \(u\ge4\), \(F(u,0)>0\): it has value \(34\) at \(u=4\) and strictly positive derivative on \([4,\infty)\). On the other hand, \(F(u,y)\to-\infty\) as \(y\to\infty\). The discriminant of the quadratic derivative \(\partial_y F\), regarded as a polynomial in \(y\), equals

\[
\operatorname{disc}_y(\partial_y F)
=-36(16u^2-16u-1)<0\quad(u\ge4),
\]

and the quadratic's leading coefficient is \(-15\). Therefore \(\partial_y F(u,y)<0\) for all real \(y\), and \(F(u,y)=0\) has exactly one positive root in \(y\), denoted \(Y(a)\) at \(u=(a+2)^2\).

**3. The first shift is the decisive one.** For fixed \(y\ge0\), the discriminant of the cubic \(F(u,y)\) in \(u\) is

\[
\operatorname{disc}_u F
=-108(4y+1)^3(4y^3+9y^2+6y+2)<0.
\]

Hence this cubic has precisely one real root. Since \(F(0,y)=-2-9y-12y^2-5y^3<0\) and the coefficient of \(u^3\) is \(3>0\), it follows that \(F(u,y)\) is nonnegative exactly on a terminal interval of positive \(u\)-values. The shifted arguments \(u=(n+a+2)^2\) increase strictly with \(n\), so nonnegativity of **every** size-three Hankel determinant is equivalent to the single inequality \(F((a+2)^2,y)\ge0\).

For the leading size-two minors, evaluate at their initial critical value \(y_1=(a+1)^2-\tfrac12\):

\[
F((a+2)^2,y_1)
=-\frac{(2a+1)^2(2a+3)^2(4a^2+20a+33)}8<0.
\]

Since \(F((a+2)^2,0)>0\) and it is strictly decreasing in \(y\), the sharp boundary obeys \(0<Y(a)<y_1\). In particular every leading size-two Hankel minor is strictly positive throughout \(0\le y\le Y(a)\). The determinant formulas and the Schur complement now establish the two-hyponormality equivalence, including equality. At equality, only the initial \(3\times3\) determinant vanishes; all later determinants are strictly positive by the unique-root-in-\(u\) argument, proving the asserted ranks.

**4. Strict separation from subnormality.** The exact moment identity is

\[
m_n=\int_0^1 t^n\,d\nu_{a,b}(t),\qquad
\frac{d\nu_{a,b}}{dt}(t)=
\begin{cases}
\displaystyle \frac{a^2+b^2}{b}\,t^{a-1}\sin\big(b\log(1/t)\big),& b>0,\\[5pt]
\displaystyle a^2t^{a-1}\log(1/t),& b=0.
\end{cases}
\]

Both expressions are integrable finite densities because \(a>0\). When \(b=0\), the density is nonnegative, has total mass one, and gives a Berger probability measure; hence \(V_{a,0}\) is subnormal. For every \(b>0\), the density changes sign infinitely often on \((0,1)\). Since \(V_{a,b}\) is a contraction, any Berger measure for a subnormal \(V_{a,b}\) must lie on \([0,1]\). Polynomial density in \(C[0,1]\) gives uniqueness of finite signed measures from their full moment sequences. No positive Berger measure can therefore have these moments, proving the non-subnormality assertion. The general link between rational reciprocal sequences and signed Hausdorff densities is established in [2]; the explicit density here also follows directly by a one-dimensional Laplace integral.

**5. The large-parameter scaling.** Write \(u=(a+2)^2\) and \(y=ru\). Dividing \(F(u,ru)\) by \(u^3\) and letting \(u\to\infty\) yields

\[
3-15r+9r^2-5r^3.
\]

Its derivative \(-15+18r-15r^2\) is strictly negative for all real \(r\), and the polynomial changes sign between \(0\) and \(1\). By the uniqueness of the positive root of \(F(u,\cdot)\) and two-sided sign comparison at \(r_*\pm\varepsilon\), \(Y(a)/(a+2)^2\to r_*\). Since \((a+2)^2/a^2\to1\), the stated limit follows.

## Verification

A standalone script `checker.py` reproduces the two rational Hankel determinant identities, both cubic discriminants, the exact evaluation at the one-hyponormal boundary, and several exact rational shifted-block tests. Execute with `python checker.py` in a Python 3 environment containing SymPy. The checker outputs successful symbolic identities and finite diagnostics. Its finite tests are not offered as proof for arbitrary parameters: the infinite-range conclusions follow from the two discriminant arguments and the Schur-complement proof above. The exact example \(a=b=1\) and the large-parameter cubic are also checked.

## Relationship to prior work

The weighted-shift Hankel criterion for \(k\)-hyponormality is classical [1]. **Chavan and Stochel [6, Example 4.5] study exactly the same complex-root quadratic polynomial family** and establish a weak-concavity criterion based on a log-concavity inequality at shifted indices. Their weaker operator condition neither states nor implies the new three-by-three Hankel positivity cutoff; the overlap in the object and in a one-step two-by-two computation is explicitly credited. Reza and Zhang [2] analyze complete Hausdorff positivity of reciprocal rational and polynomial sequences; in particular their degree-two complex-root case covers the fact that \(b>0\) prevents complete subnormality, but does not supply the **sharp finite-order two-hyponormal region**, the polynomial \(F\), the equality ranks, or the asymptotic ratio. Anand, Chavan, Jabłoński, and Stochel [3] study subnormality of Cauchy duals of cyclic **two-isometries** constructed through weighted composition operators, not this strict three-isometric polynomial-shift family or finite-order Hankel cutoffs. Benhida, Curto, and Exner [4] study signed Berger charges and \(k\)-hyponormality restrictions for **countably atomic** measures, rather than the present oscillatory absolutely continuous densities. Nailwal [5] classifies **joint subnormality** for toral three-isometric two-variable shifts, which does not establish these one-variable finite two-hyponormality boundaries. These earlier results and the shared quadratic model are credited, not claimed as new ingredients. No covering statement was identified in the sources examined, but historical novelty has not been independently certified.

## Limitations

The claim is confined to normalized quadratic positive moment polynomials \(P_{a,b}\) with \(a>0\), \(b\ge0\), to one-variable unilateral weighted shifts, and to **two-hyponormality** (plus the stated one-hyponormality and subnormality comparisons). It does not classify higher finite hyponormality orders or analogous polynomials of degree three and above. Numerical root values are illustrative, not substitute analytical proofs. Prior-literature search and mathematical review are non-exhaustive; no independent audit or independent validation is claimed.

## References

[1] Scott McCullough and Vern Paulsen, *k-Hyponormality of Weighted Shifts*, Proceedings of the American Mathematical Society 116 (1992), 95–99, DOI: https://doi.org/10.2307/2159309. The exact shifted Hankel characterization is also restated in subsequent treatments.

[2] Md. Ramiz Reza and Genkai Zhang, *Hausdorff moment sequences induced by rational functions*, first public 1 March 2019, https://arxiv.org/abs/1903.00116.

[3] Akash Anand, Sameer Chavan, Zenon Jan Jabłoński, and Jan Stochel, *The Cauchy dual subnormality problem for cyclic 2-isometries*, first public 9 March 2020, https://arxiv.org/abs/2003.04090.

[4] Chafiq Benhida, Raúl E. Curto, and George R. Exner, *Signed representing measures (Berger-type charges) in subnormality and related properties of weighted shifts*, first public 23 May 2024, https://arxiv.org/abs/2405.15000.

[5] Rajkamal Nailwal, *A complete solution to the Cauchy dual subnormality problem for torally expansive toral 3-isometric weighted 2-shifts*, first public 7 October 2023, https://arxiv.org/abs/2310.04785.

[6] Sameer Chavan and Jan Stochel, *Weakly concave operators*, first online 18 January 2023, Example 4.5 and Proposition 4.3, https://doi.org/10.1017/prm.2022.85.
