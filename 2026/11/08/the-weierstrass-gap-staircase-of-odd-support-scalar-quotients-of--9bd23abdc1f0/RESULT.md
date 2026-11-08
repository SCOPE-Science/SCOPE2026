# The Weierstrass gap staircase of odd-support scalar quotients of additive curves

## Finding

Let \(r=p^e\geq5\) be an odd prime power, \(h\geq2\), and \(k\) an algebraically closed field of characteristic \(p\). Let
\[
R(x)=\sum_{j=0}^h B_jx^{r^j},\qquad B_0B_h\ne0,
\]
with at least one coefficient \(B_j\ne0\) at an odd index \(j\). On the smooth projective model \(W_R\) of \(y^r-y=xR(x)\), the scalar group \(\mu_{r-1}\) acts by \((x,y)\mapsto(ax,a^2y)\). Put \(X_R=W_R/\mu_{r-1}\), and let \(P_\infty\) be the image of the unique point at infinity.

Set
\[
t=\frac{r-1}{2},\qquad S=\frac{r^{h-1}-1}{r-1},\qquad L=rS-1=\frac{r^h+1-2r}{r-1}.
\]
The **complete one-point Weierstrass semigroup** is
\[
\boxed{H(P_\infty)=\langle r,\ r+L,\ r+2L,\ldots,\ r+tL\rangle.}
\]
These \(t+1\) generators are all minimal. The Apéry set relative to \(r\) is \(\{w_0,\ldots,w_{r-1}\}\), where \(w_0=0\) and
\[
w_j=\begin{cases}r+jL,&1\le j\le t,\\ 2r+jL,&t<j\le r-1.\end{cases}
\]
In residue class \(r-j\) modulo \(r\), the gaps are precisely
\[
\boxed{r-j+kr\quad (0\le k<jS+\mathbf1_{\{j>t\}}),\qquad 1\le j\le r-1.}
\]
Consequently the genus is \(g=(r^h-1)/2\), the numerical-semigroup type is \(t\), and the pseudo-Frobenius numbers are
\[
\boxed{\operatorname{PF}(H)=\{r+jL:t<j\le r-1\}.}
\]
Its Frobenius number is \(r^h+1-r\), its conductor is \(r^h+2-r\), and the **Weierstrass weight** of the marked point is
\[
\boxed{\operatorname{wt}(P_\infty)=
\frac{r(r+1)(r^{h-1}-1)(r^h-1)}{24(r-1)}.}
\]
These invariants depend only on \((r,h)\), not on the permitted coefficients of \(R\). In particular, the pole semigroups are nonsymmetric for every \(r\ge5\), and the marked point is a positive-weight Weierstrass point.

## Assumptions and scope

All curves and valuations are geometric over \(k\). The semigroup \(H(P)\) consists of the nonnegative pole orders of rational functions regular on \(X_R\setminus\{P\}\). The type is the number of pseudo-Frobenius integers \(z\notin H\) for which \(z+H_{>0}\subset H\). The Weierstrass weight is \(\sum_{m\in\mathbb Z_{>0}\setminus H}m-g(g+1)/2\). The odd-index hypothesis is exactly the case where the scalar group selected in the construction of Bartoli--Borges--Timpanella--Zini has order \(r-1\), rather than \(2(r-1)\). The claims here concern that precise quotient and its marked point; no assertion is made about all other points or all possible quotient groups.

## Proof

**1. Affine invariant ring and pole valuations.** The affine curve \(W_R\setminus\{Q_\infty\}\) is smooth since the derivative with respect to \(y\) of its equation is \(-1\). Its coordinate ring is free over \(k[x]\), with basis \(1,y,\ldots,y^{r-1}\). The unique place \(Q_\infty\) has \(v_{Q_\infty}(x)=-r\) and \(v_{Q_\infty}(y)=-(r^h+1)\); this follows because the polynomial \(xR(x)\) has degree \(r^h+1\) prime to \(p\). The scalar action has order \(D=r-1\), is tame, and fixes \(Q_\infty\). Hence the valuation downstairs at \(P_\infty\) of an invariant function is its valuation upstairs divided by \(D\). The coordinate ring of the punctured quotient is exactly the invariant ring. A monomial \(x^iy^j\), \(i\ge0\), \(0\le j<r\), is invariant precisely when \(i+2j\equiv0\pmod D\).

**2. Exhaustive Apéry calculation.** For each \(0\le j<r\), let \(i_j\) be the least nonnegative integer congruent to \(-2j\) modulo \(D\). Invariant monomials with this \(j\) are \(x^{i_j+qD}y^j\), with pole orders
\[
\frac{ri_j+(r^h+1)j}{D}+qr\quad(q\ge0).
\]
The starting pole orders have residues \(-j\pmod r\), all distinct. Thus leading poles of different \(j\)-summands cannot cancel, and the displayed progressions exhaust \(H(P_\infty)\), not merely a subsemigroup. For \(1\le j\le t\) one has \(i_j=D-2j\), and for \(t<j<r\) one has \(i_j=2D-2j\). Substitution gives the stated \(w_j\) and the Apéry set. In particular \(w_{t+b}=w_t+w_b\) for \(1\le b<t\) and \(w_{2t}=2w_t\), proving that \(r,w_1,\ldots,w_t\) generate. Since \(L>0\) and \(L\equiv-1\pmod r\), no \(w_j\), \(1\le j\le t\), is a sum of the others and nonnegative multiples of \(r\): any such decomposition would have total coefficient index \(J\equiv j\pmod r\) but \(J<j<r\), an impossibility. Thus the generating list is minimal.

**3. Gaps, genus and conductor.** Since \(w_j\equiv r-j\pmod r\), the number of gaps in that residue is \((w_j-(r-j))/r=jS+\mathbf1_{\{j>t\}}\). Summing these counts yields
\[
\sum_{j=1}^{r-1}\left(jS+\mathbf1_{\{j>t\}}\right)
=\frac{r(r-1)}2 S+t=\frac{r^h-1}{2}.
\]
As \(L>0\), the largest Apéry element is \(w_{r-1}=r^h+1\). Its difference from the multiplicity \(r\) is the Frobenius number, giving the conductor above.

**4. Type and pseudo-Frobenius set.** An Apéry element \(w\) is maximal in the semigroup order precisely when \(w-r\) is pseudo-Frobenius. Every \(w_j\) with \(1\le j\le t\) is strictly below another Apéry element by addition of \(w_t\). For \(t<j<r\) and any \(0<k<r\), the inequality \(w_j+w_k>w_{(j+k)\bmod r}\) holds: when \(j+k<r\), its difference is \(r\); when \(j+k\ge r\), the difference is \(r(c_j+c_k-c_{j+k-r}+L)>0\), with \(c_0=0\), \(c_i=1\) for \(1\le i\le t\), and \(c_i=2\) for \(t<i<r\). Thus \(w_{t+1},\ldots,w_{r-1}\) are exactly the maximal Apéry elements, giving \(t\) pseudo-Frobenius numbers \(w_j-r=r+jL\). Their count is \(t\ge2\), so the semigroup is not symmetric.

**5. Weight.** In residue \(r-j\), write \(n_j=jS+\mathbf1_{\{j>t\}}\). The sum of gaps in that residue is \(n_j(r-j)+rn_j(n_j-1)/2\). Summation over \(1\le j\le r-1\), followed by subtracting \(g(g+1)/2\), simplifies exactly to the displayed weight formula. Its numerator is positive for \(h\ge2\); hence the marked point is Weierstrass.

## Verification

The standalone `CHECK.py` verifies the invariant-monomial Apéry formula independently from the closed staircase formula; checks residues, gaps, genus, minimal generators, pseudo-Frobenius numbers, conductor and weight; and compares with direct numerical-semigroup dynamic programming in bounded cases. It uses exact integer arithmetic only and runs without external dependencies. It passed all \(28\) tested pairs with \(r\in\{3,5,7,9,11,13,25\}\) and \(1\le h\le4\). Values with \(r=3\) or \(h=1\) are optional boundary cross-checks outside the asserted domain. The proof, not the finite checks, establishes all permitted parameters.

For illustration, \((r,h)=(5,2)\) yields \(H=\langle5,9,13\rangle\), genus \(12\), type \(2\), conductor \(22\) and weight \(30\). At \((r,h)=(7,3)\), the corresponding values are genus \(171\), type \(3\), conductor \(338\) and weight \(6384\).

## Relationship to prior work

Bartoli--Borges--Timpanella--Zini (2026, Proposition 2.1 and Section 3) construct the scalar quotients, compute genus and ramification, and establish automorphism rigidity and gonality under an additional genus bound. The present result computes the complete marked-point semigroup, its gap staircase, numerical-semigroup type and exact weight. The full relevant source text contains no corresponding semigroup formula.

Bouw--Ho--Malmskog--Scheidler--Srinivasan--Vincent (2015) treat the additive covering curves, their automorphisms, zeta functions and certain additive-subgroup quotients, rather than the tame scalar quotient's marked-point semigroup. Zhang--Zhao (2026) and Mendoza (2026) determine semigroups of *linearized Galois function-field extensions*. The natural degree-\(r\) morphism on the present scalar quotient has nonnormal scalar stabilizer in its affine Galois closure and is not such a Galois linearized extension. Their general results therefore do not directly state this semigroup. Earlier calculations for the different \(2(r-1)\)-scalar quotient do not imply the present formulas: the two quotient curves have different genera and pole semigroups. These are implication distinctions, not historical uniqueness claims.

## Limitations

The theorem concerns a single specified point and only odd prime-power parameter \(r\ge5\), height \(h\ge2\), with nonzero leading and initial coefficients and some odd-index coefficient. It does not identify all Weierstrass points, improve bounds on automorphism groups, or determine higher-point semigroups. Historical priority against all older specialized quotient literature has not been independently certified, and no independent mathematical audit has been performed.

## References

1. D. Bartoli, H. Borges, M. Timpanella, G. Zini, *Maximal curves with trivial automorphism group*, arXiv:2610.35788v1, 26 October 2026, especially Proposition 2.1 and Section 3. https://arxiv.org/html/2610.35788
2. I. Bouw, W. Ho, B. Malmskog, R. Scheidler, P. Srinivasan, C. Vincent, *Zeta functions of a class of Artin--Schreier curves with many automorphisms*, arXiv:1410.7031v2 (2015). https://arxiv.org/html/1410.7031v2
3. H. Zhang, C.-A. Zhao, *Weierstrass semigroups at totally ramified places of degree one on linearized function fields*, arXiv:2605.29311 (2026). https://arxiv.org/abs/2605.29311
4. E. Mendoza, *On generalized Weierstrass semigroups in linearized function fields*, arXiv:2606.01369 (2026). https://arxiv.org/abs/2606.01369
