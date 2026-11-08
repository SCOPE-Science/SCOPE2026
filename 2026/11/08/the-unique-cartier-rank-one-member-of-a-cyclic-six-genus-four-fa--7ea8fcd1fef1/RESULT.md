# The unique Cartier-rank-one member of a cyclic-six genus-four family in characteristic eleven

## Finding
Work over an algebraic closure \(k=\overline{\mathbb F}_{11}\). For \((a,b)\in k^2\), consider the genus-four hyperelliptic model
\[
H_{a,b}:\quad y^2=x^{10}+x^7+a x^4+b x=x\bigl((x^3)^3+(x^3)^2+a x^3+b\bigr).
\]
Set
\[
\Delta(a,b)=a^2-4a^3+18ab-27b^2-4b,
\qquad
P(a,b)=a^5-2a^3b-3a^2b^2-3ab^2-2b^3,
\]
with coefficients interpreted in \(k\). The model is geometrically smooth precisely when \(b\Delta(a,b)\ne0\). **For every such smooth model**, its Cartier \(a\)-number is
\[
a(H_{a,b})=\begin{cases}
3,&(a,b)=(0,-2),\\
2,&P(a,b)=0,\\
1,&\text{otherwise}.
\end{cases}
\]
In particular, the locus with \(a\)-number at least three is exactly one coefficient point, \((0,-2)\); the two remaining smooth strata are the hypersurface \(P=0\) minus this point and its complement, respectively. The exceptional model has Cartier rank one and \(11\)-rank one. Among all \(101\) smooth models with \((a,b)\in\mathbb F_{11}^2\), exactly \(83\), \(17\), and \(1\) have \(a\)-numbers \(1\), \(2\), and \(3\). These are **parameter counts in the fixed normalized family**, not counts of isomorphism classes.

## Assumptions and scope
The ground characteristic is exactly \(11\); \(k\) is algebraically closed. The assertion concerns the given normalized two-parameter family, not all genus-four curves. The symbol \(a(H)\) denotes the dimension of the kernel of the Cartier operator on \(H^0(H,\Omega_H^1)\), equivalently genus minus the rank of its Cartier--Manin matrix. The polynomial \(P\) and discriminant \(\Delta\) are understood modulo \(11\). The coefficient parameter \((0,-2)\) means \((0,9)\) when expressed in \(\mathbb F_{11}\).

## Proof
**Smoothness.** Put \(Q(t)=t^3+t^2+at+b\). The branch polynomial is \(f(x)=xQ(x^3)\). Since the characteristic is different from \(2\) and \(3\), its root at \(x=0\) is simple if and only if \(b\ne0\), and its other roots are simple if and only if \(Q\) has no repeated root. The usual cubic discriminant of \(Q\) is \(\Delta\). Thus \(f\) is squarefree exactly when \(b\Delta\ne0\); its smooth hyperelliptic completion has genus four.

**Cartier matrix.** Write \(f(x)^5=\sum_j c_jx^j\), and index the standard basis of holomorphic differentials by \(x^{i-1}dx/y\), for \(1\le i\le4\). The rank of Cartier is that of the matrix \((c_{11i-j})_{1\le i,j\le4}\). Because \(f(x)^5=x^5Q(x^3)^5\), this matrix has shape
\[
M=\begin{pmatrix}
0&0&u_1&0\\
0&P&0&0\\
v_1&0&0&v_2\\
0&0&u_2&0
\end{pmatrix},
\]
where a direct fifth-power expansion in characteristic \(11\) gives
\[
\begin{aligned}
u_1&=5ab^4, &u_2&=-2a+5b-1,\\
v_1&=-a^3-3a^2+5ab+5a-b^2-2b,\\
v_2&=-2a^3-3a^2b-a^2+5ab-3b^2+5b.
\end{aligned}
\]
The three nonoverlapping blocks contribute independent ranks; consequently
\[
\operatorname{rank}M=
\mathbf1_{(u_1,u_2)\ne(0,0)}+
\mathbf1_{P\ne0}+
\mathbf1_{(v_1,v_2)\ne(0,0)}.
\]

**The two outer blocks.** On the smooth locus \(b\ne0\), the equations \(u_1=u_2=0\) give \(a=0\) and \(b=-2\). To analyze the second outer block, the following polynomial identity holds modulo \(11\):
\[
v_2-3v_1=aL,
\qquad L=a^2-3a-3ab+b-4.
\]
For \(a=0\), the equation \(v_1=0\) becomes \(-b(b+2)=0\), so the only possibility in the smooth locus is \((0,-2)\). For \(a\ne0\), simultaneous vanishing forces \(L=0\). If \(a=4\), then \(v_1=-(b+2)^2\) and \(v_2=-3(b+2)^2\) modulo \(11\). Their only common root is \((4,-2)\), which is excluded because \(\Delta(4,-2)=0\). If \(a\ne4\), put
\[
d=1-3a\ne0,\qquad n=-a^2+3a+4.
\]
The equation \(L=0\) gives \(db=n\). Substitution, with denominators cleared, yields
\[
 d^2v_1\big|_{b=n/d}=2(a-4)^5,
 \qquad d^2v_2\big|_{b=n/d}=-5(a-4)^5.
\]
Since both \(2\) and \(5\) are units in characteristic \(11\), no such \(a\ne4\) can give simultaneous vanishing. Thus, on the smooth locus, **each of the two outer blocks vanishes exactly at \((0,-2)\)**.

**Rank and strata.** At \((0,-2)\), the discriminant is \(10\ne0\), while \(P(0,-2)=5\ne0\), so \(M\) has rank exactly one. Elsewhere on the smooth locus both outer blocks have rank one, and the middle block contributes rank one precisely when \(P\ne0\). Since the genus is four, subtracting from four proves the claimed three-case formula. At the exceptional point the sole nonzero matrix entry is the middle diagonal entry \(5\), so its semilinear Cartier action has a one-dimensional stable invertible summand and a nilpotent complementary summand. Consequently the \(11\)-rank of the Jacobian is one.

**Finite ground-field counts.** The exact count over \(\mathbb F_{11}\) is made by enumerating all \(121\) coefficient pairs, filtering using \(b\Delta\ne0\), and applying the proven expression for \(a(H_{a,b})\). This leaves \(101\) smooth pairs with the stated counts \(83,17,1\). For examples, \((0,1)\), \((1,4)\), and \((0,-2)\) represent the three respective strata. The supplied independent verifier also computes the entire matrix by expanding \(f(x)^5\) and row-reducing it over \(\mathbb F_{11}\), without using the symbolic sparse-block formulas.

## Verification
Two complete Python 3 programs accompany this result and require only the standard library. Running `python3 verify_symbolic.py` reproduces all five needed coefficient identities and the elimination identities as exact polynomial equalities over \(\mathbb F_{11}\). Running `python3 verify_finite.py` independently expands \(f(x)^5\), forms its four-by-four Cartier matrix, calculates the rank by modular elimination for each smooth parameter pair, and verifies the \(83,17,1\) distribution. The identities are exact algebraic certificates, not a finite-sample extrapolation to algebraically closed parameters.

## Relationship to prior work
Kudo, Nakagawa and Takagi introduced and studied precisely this order-six-automorphism genus-four hyperelliptic family, including a general Cartier--Manin method and a classification algorithm for **superspecial** curves. Their computational enumeration concentrates on characteristics at least \(17\), whereas this result determines the complete positive-rank stratification in characteristic \(11\) and isolates the unique rank-one point. Frei studies hyperelliptic curves with \(a\)-number one less than the genus, providing the broader geometric context for the \(a=3\) extreme but not this characteristic-eleven two-parameter locus. The standard Cartier coefficient formula, cubic discriminant, and the cyclic automorphism family itself are prior tools, not new claims here.

## Limitations
No claim is made that the \(101\) smooth rational parameter pairs give distinct isomorphism classes, or that all genus-four hyperelliptic curves of characteristic \(11\) lie in this family. No zeta functions or complete Newton polygons are computed. The novelty comparison is limited by the possibility that older genus-four curve tables or general rank-stratification formulas imply the same specialization under another coordinate model; absence from targeted searches is not a proof of priority. The \(11\)-rank assertion is confined to the single exceptional curve.

## References
1. M. Kudo, T. Nakagawa, and T. Takagi, *Efficient search for superspecial hyperelliptic curves of genus four with automorphism group containing* \(\mathbb Z_6\), first publicly posted 2022-10-26, arXiv:2210.14822v1. https://arxiv.org/abs/2210.14822
2. S. Frei, *The a-number of hyperelliptic curves*, arXiv:1703.03516v2 (2017). https://arxiv.org/abs/1703.03516
3. M. Kudo and S. Harashita, *Superspecial Hyperelliptic Curves of Genus 4 over Small Finite Fields*, WAIFI 2018, DOI:10.1007/978-3-030-05153-2_3. This paper treats the rank-zero problem; its inaccessible full text is a residual priority risk rather than evidence of noncoverage.
