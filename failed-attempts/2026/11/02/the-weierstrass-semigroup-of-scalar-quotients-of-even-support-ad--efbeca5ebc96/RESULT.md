# The Weierstrass semigroup of scalar quotients of even-support additive curves

## Finding
Let \(k\) be algebraically closed of odd characteristic \(p\), let \(r=p^e\ge3\), and let \(h\ge2\) be even. Suppose
\[
R(X)=\sum_{j=0}^{h}b_jX^{r^j},\qquad b_j=0\text{ for odd }j,\quad b_0b_h\ne0.
\]
Let \(W\) be the smooth projective curve with affine equation \(Y^r-Y=XR(X)\). Let \(G\) be the cyclic group of order \(D=2(r-1)\) acting through \((X,Y)\mapsto(\zeta X,\zeta^2Y)\), where \(\zeta\) has order \(D\). Put \(C=W/G\), and let \(P_\infty\in C(k)\) be the image of the unique infinite point on \(W\). Define
\[
L=\frac{r^h+1-2r}{2(r-1)}=\frac{r^h-1}{2(r-1)}-1.
\]
Then the complete one-point Weierstrass semigroup is
\[
\boxed{H(P_\infty)=\langle r,\ r+L,\ r+2L,\ldots,\ r+(r-1)L\rangle.}
\]
Its Apéry set relative to \(r\) is exactly \(\{0,r+L,\ldots,r+(r-1)L\}\). All displayed generators are minimal. In particular, the semigroup has multiplicity and embedding dimension both \(r\), and is therefore of maximal embedding dimension. Its pseudo-Frobenius numbers, type, Frobenius number, conductor, and number of gaps are, respectively,
\[
\{L,2L,\ldots,(r-1)L\},\quad r-1,\quad(r-1)L,\quad (r-1)L+1,\quad\frac{r^h-1}{4}.
\]
It is almost symmetric and is not symmetric. These formulas are independent of the allowed nonzero coefficients of \(R\).

For every integer \(m\ge0\), an explicit \(k\)-basis of \(\mathcal L(mP_\infty)\) consists of the invariant monomials
\[
X^{i_j+kD}Y^j\quad(0\le j\le r-1,\ k\ge0,\ a_j+kr\le m),
\]
where \(i_0=a_0=0\) and \(i_j=2(r-1-j)\), \(a_j=r+jL\) for \(1\le j<r\). Consequently,
\[
\ell(mP_\infty)=1+\lfloor m/r\rfloor+
\sum_{j=1}^{r-1}\max\left\{0,1+\left\lfloor\frac{m-r-jL}{r}\right\rfloor\right\}.
\]
In particular, the formulas apply to the prime-field automorphism-free maximal curves \(\mathcal X_{p,n}\) of Bartoli--Borges--Timpanella--Zini (2026), with \(r=p\) and \(h=2n\) for \(n\ge2\).

## Assumptions and scope
The characteristic is odd, \(k\) is algebraically closed, \(r\) is a power of that characteristic, the additive polynomial has nonzero lowest and highest coefficients, and only its even Frobenius exponents appear. We work with the quotient of the *smooth projective* model. For a rational point \(P\), \(H(P)\) means the set of possible pole orders of rational functions whose only pole is \(P\), including zero. Every expression and basis in this result is geometric, over \(k\); a descent assertion about the displayed functions over a smaller field requires their coefficients and the quotient structure to be defined there.

## Proof
**1. Smooth affine curve, one infinite point, and pole valuations.** The affine polynomial \(Y^r-Y-XR(X)\) has \(Y\)-derivative \(-1\), so its affine curve is nonsingular. The polynomial \(XR(X)\) has degree \(s=r^h+1\), prime to \(p\) and \(r\). The additive extension has a unique point \(Q_\infty\) above the pole of \(X\) and is totally ramified there with degree \(r\): if its local ramification index were less than \(r\), the equality \(Y^r-Y=XR(X)\) and \(\gcd(r,s)=1\) would contradict integrality of the normalized valuation of \(Y\). Thus \(-v_{Q_\infty}(X)=r\) and \(-v_{Q_\infty}(Y)=s\). The affine coordinate ring is
\[
A=k[X,Y]/(Y^r-Y-XR(X))=\bigoplus_{j=0}^{r-1}k[X]Y^j.
\]
This ring equals the functions regular away from \(Q_\infty\), since the affine model is smooth and has exactly that one point at infinity.

**2. Tame scalar quotient and its full affine invariant ring.** Because \(h\) and every supported exponent \(j\) are even, \(r^{j}\equiv1\pmod{D}\). Also \(2r\equiv2\pmod D\). Hence \((X,Y)\mapsto(\zeta X,\zeta^2Y)\) preserves the equation, and \(G\) acts faithfully with order \(D\) prime to \(p\). It fixes \(Q_\infty\), so \(C=W/G\) has a unique marked point \(P_\infty\) below it; the ramification index there is \(D\). The affine quotient has coordinate ring \(A^G\). Since the displayed \(k[X]\)-decomposition is unique and the action is diagonal on monomials, a \(k\)-basis of \(A^G\) is precisely
\[
\{X^iY^j:i\ge0,\ 0\le j<r,\ i+2j\equiv0\pmod D\}.
\]
These monomials span every rational function on \(C\) regular away from \(P_\infty\), not just a subalgebra of such functions.

**3. No pole-order cancellation and an Apéry basis.** Upstairs \(X^iY^j\) has pole order \(ir+js\). These orders are pairwise distinct for different \((i,j)\) with \(i\ge0\), \(0\le j<r\): reducing an equality modulo \(r\) gives \(j\equiv j'\pmod r\) because \(s\equiv1\pmod r\), hence \(j=j'\) and then \(i=i'\). Therefore sums of basis monomials cannot cancel their highest poles. Since \(Q_\infty/P_\infty\) has ramification index \(D\), the downstairs pole order of an invariant monomial is \((ir+js)/D\).

For each \(0\le j<r\), the smallest admissible nonnegative exponent is \(i_j=(-2j)\bmod D\), represented in \([0,D-1]\). Explicitly \(i_0=0\) and \(i_j=2(r-1-j)\) for \(j\ge1\). Every other exponent is \(i_j+kD\). Its pole order equals \(a_j+kr\), where \(a_0=0\) and
\[
a_j=\frac{2(r-1-j)r+j(r^h+1)}{2(r-1)}=r+jL\qquad(1\le j<r).
\]
As \(\gcd(r,L)=1\) (indeed \(2(r-1)L=r^h+1-2r\equiv1\pmod r\)), the numbers \(a_j\) run once through the residues modulo \(r\). Their translates by nonnegative multiples of \(r\) therefore give the full Weierstrass semigroup and the complete indicated \(\mathcal L(mP_\infty)\) basis. Counting these translates gives the Riemann--Roch dimension formula.

**4. Minimal generators, gaps, and type.** The Apéry representatives \(a_j=r+jL\), \(j\ge1\), are minimal generators in addition to \(r\). To prove irreducibility of \(a_j\), suppose it is a sum of two positive semigroup elements. If one summand is a positive multiple of \(r\), reduction modulo \(r\) forces the other summand to have Apéry index \(j\), so their sum is strictly greater than \(a_j\). Otherwise the summands are \(a_i+kr\) and \(a_l+k'r\), with \(1\le i,l<r\) and \(k,k'\ge0\). Reduction modulo \(r\) forces \(i+l=j\) or \(i+l=j+r\). In the first case their sum is at least \(2r+jL>a_j\); in the second it is at least \(2r+(j+r)L>a_j\). Both contradict the proposed decomposition. The integers \(a_j-r=jL\) are all gaps and are pseudo-Frobenius numbers: adding \(r\) gives \(a_j\); adding any \(a_i\) gives \(r+(i+j)L\), equal to another Apéry representative or to one plus a nonnegative multiple of \(r\). Conversely the largest gap in each nonzero residue class is its Apéry representative minus \(r\), and every pseudo-Frobenius number must be among them. Thus the type is \(r-1\), with the stated pseudo-Frobenius set and Frobenius number.

The Apéry genus formula yields
\[
\#(\mathbb N_0\setminus H)=\frac1r\sum_{j=0}^{r-1}a_j-\frac{r-1}{2}=\frac{r-1}{2}(L+1)=\frac{r^h-1}{4}.
\]
The Frobenius number is \((r-1)L\), the conductor one greater. Since \(2g=F+(r-1)\), the numerical semigroup is almost symmetric (standard numerical-semigroup characterization \(2g=F+\mathrm{type}\)), and it cannot be symmetric as \(r\ge3\). This concludes the proof.

## Verification
`verify_semigroup.py` performs exact integer checks of invariant monomial orders, residue representatives, the full finite gap set through the conductor, minimal generators, pseudo-Frobenius numbers, and genus for \(r\in\{3,5,7,9,11,13\}\), \(h\in\{2,4\}\), plus \((r,h)=(3,6),(5,6)\). It prints `VERIFY_OK`. These calculations test nontrivial cases but are not used to infer the theorem for infinitely many parameters. The preceding valuation and invariant-ring proof establishes the universal statement.

## Relationship to prior work
Bartoli, Borges, Timpanella and Zini (2026, arXiv:2610.35788v1) construct these quotients, prove their genera and geometric automorphism rigidity in a high-genus range, and exhibit the prime-field maximal subfamily; their statements do not provide the complete semigroup or all one-point Riemann--Roch bases. Zhang and Zhao (2026, arXiv:2605.29311v1) study totally ramified rational places of **Galois linearized function fields**; the present curve \(C\), when automorphism-free and of degree-\(r\) gonality, is not such a Galois extension of \(k(u)\). General numerical-semigroup Apéry and pseudo-Frobenius machinery is used as standard theory and is not claimed as new. Earlier Weierstrass-semigroup treatments of Kummer and additive covering curves concern other function fields; a historically equivalent quotient computation under different terminology remains possible.

## Limitations
Only the point \(P_\infty\) on the specified scalar quotient is classified; the Weierstrass semigroups of other points, full multipoint gap arrays, designed-distance improvements, and smaller-field descent are not established. The supplied formulas do not assert a new geometric automorphism classification, maximality criterion, or genus formula beyond the original construction. Independence and universal historical priority have not been established.

## References
1. D. Bartoli, H. Borges, M. Timpanella and G. Zini, *Maximal curves with trivial automorphism group*, arXiv:2610.35788v1 (2026), https://arxiv.org/abs/2610.35788.
2. H. Zhang and C.-A. Zhao, *Weierstrass semigroups at totally ramified places of degree one on linearized function fields*, arXiv:2605.29311v1 (2026), https://arxiv.org/abs/2605.29311.
3. S. Yang and C. Hu, *Weierstrass semigroups from Kummer extensions*, Finite Fields and Their Applications 45 (2017), 264--284, https://doi.org/10.1016/j.ffa.2016.12.005.
4. A. Sepúlveda and G. Tizziotti, *Weierstrass semigroup and codes over the curve \(y^q+y=x^{q^r+1}\)*, Advances in Mathematics of Communications 8 (2014), 67--72, https://doi.org/10.3934/amc.2014.8.67.
