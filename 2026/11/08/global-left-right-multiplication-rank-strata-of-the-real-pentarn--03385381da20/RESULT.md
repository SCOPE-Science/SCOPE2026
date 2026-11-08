# Global left–right multiplication rank strata of the real Pentarnion algebra

## Finding

Let \(\mathbb P\) be the canonical five-dimensional real Pentarnion algebra, with multiplication specified below. For \(p=a+bI+cJ+dK+eL\), set
\[
S=b+c+d,\qquad Q=b^2+c^2+d^2,\qquad R=Q-\frac{S^2}{3},
\]
\[
N(p)=a^2+2(Q+e^2),\qquad
F(p)=(a+2e)\left((a-e)^2+\frac{S^2}{3}\right)+(a+3S-e)R.
\]
Write \(L_p(x)=px\), \(R_p(x)=xp\), and \(\bar p=a-bI-cJ-dK-eL\). The complete determinant formulas are
\[
\det L_p=N(p)F(p),\qquad \det R_p=N(p)F(\bar p).
\]
For every \(p\ne0\), the left multiplication ranks are exactly
\[
\operatorname{rank}L_p=
\begin{cases}
5,&F(p)\ne0,\\
3,&p=t(1+L)\text{ for some }t\in\mathbb R\setminus\{0\},\\
4,&F(p)=0\text{ and }p\notin\mathbb R(1+L).
\end{cases}
\]
The right multiplication ranks obey the reflected criterion, with \(F(\bar p)\) in place of \(F(p)\) and \(\mathbb R(1-L)\) in place of \(\mathbb R(1+L)\). At \(p=0\), both ranks are zero.

The real projective cubic hypersurface \(\{F=0\}\subset\mathbb P^4(\mathbb R)\) has precisely one real singular point, \([1:0:0:0:1]\). Its corresponding left multiplication has corank two, while right multiplication there is invertible. The reflected cubic has its unique real projective singular point at \([1:0:0:0:-1]\), with the roles reversed.

## Assumptions and scope

The field is \(\mathbb R\), and only the canonical endpoint \(\gamma=1\) of the recently introduced five-dimensional real quadratic-algebra family is considered. The basis is \((1,I,J,K,L)\), with \(I=\sqrt2\,i\), \(J=\sqrt2\,j\), \(K=\sqrt2\,k\), and \(L=\sqrt2\,\ell\), where \((1,i,j,k,\ell)\) is the canonical basis in Poshtkohi–Pumplün. The unit is \(1\). The defining squares are \(I^2=J^2=K^2=L^2=-2\). Distinct imaginary basis products are anticommutative, with
\[
IJ=K+L,\quad JK=I+L,\quad KI=J+L,\quad LI=J+K,\quad LJ=I+K,\quad LK=I+J.
\]
These rules, bilinearity, and the unit specify the full nonassociative algebra. The polynomial \(F\) is homogeneous cubic and \(N\) is positive definite. All ranks are ranks of real-linear endomorphisms of the five-dimensional underlying vector space. In this paper, a nonzero left zero divisor means an element having nonzero right annihilator (\(px=0\)); similarly for a right zero divisor.

## Proof

**1. Exact multiplication matrix and factorization.** Multiplication by \(p=a+bI+cJ+dK+eL\) on the left has matrix
\[
[L_p]=\begin{pmatrix}
a&-2b&-2c&-2d&-2e\\
b&a&e-d&c+e&-c-d\\
c&d+e&a&e-b&-b-d\\
d&e-c&b+e&a&-b-c\\
e&d-c&b-d&c-b&a
\end{pmatrix}.
\]
Expansion gives the explicitly factored determinant \(N(p)F(p)\). For a second reproducible form of the identity, the cubic expands to
\[
F=a^3+a(Q-3e^2)+S(3Q-S^2)+e(S^2-Q)+2e^3.
\]
Both expressions agree after collecting coefficients; the attached checker independently reconstructs the multiplication table, then symbolically verifies both determinant identities. The quadratic factor has a structural origin: for every \(p\), the quadratic-algebra identity \(p^2-2ap+N(p)1=0\) shows that \(\operatorname{span}_{\mathbb R}\{1,p\}\) is invariant under \(L_p\), and its determinant is \(N(p)\) whenever \(p\) is nonscalar. The full polynomial equality also covers scalar \(p\) by continuity, with no need to infer multiplicativity of the norm.

**2. Right multiplication by conjugation.** The linear involution \(C\) sends \(1\) to itself and changes the signs of the four imaginary basis vectors. Since the algebra conjugation reverses products, \(R_p=C L_{\bar p} C\). Therefore \(\det R_p=N(p)F(\bar p)\), and corresponding ranks are equal.

**3. Unique real singular direction of the cubic.** Set orthogonal real coordinates
\[
x=\frac{b+c+d}{\sqrt3},\qquad y=\frac{b-c}{\sqrt2},\qquad z=\frac{b+c-2d}{\sqrt6}.
\]
Then \(Q-S^2/3=y^2+z^2\), and
\[
F=(a+2e)\bigl((a-e)^2+x^2\bigr)
 +(a+3\sqrt3\,x-e)(y^2+z^2).
\]
At a real singular point of this cubic, the derivatives with respect to \(a\) and \(e\) both vanish, so
\[
0=\partial_aF+\partial_eF=3((a-e)^2+x^2).
\]
Over \(\mathbb R\) this forces \(a=e\) and \(x=0\). At these values, \(\partial_aF=y^2+z^2\), which forces \(y=z=0\). Thus every nonzero real singular point is a scalar multiple of \((a,b,c,d,e)=(1,0,0,0,1)\). Conversely all first derivatives vanish there. Homogeneity ensures that this identifies precisely one singular *projective* point. This statement is specifically about real points, not the complex singular locus.

**4. Rank classification.** For any nonzero \(p\), \(N(p)>0\); hence \(\det L_p=0\) exactly when \(F(p)=0\). If \(\operatorname{rank}L_p\le3\), all its \(4\times4\) cofactors vanish. The adjugate derivative formula for a matrix linear in \(p\) therefore gives \(\nabla_p(\det L_p)=0\). On \(F=0\), positivity of \(N(p)\) forces \(\nabla F(p)=0\), so the preceding step confines rank at most three to the line \(\mathbb R(1+L)\). Substitution into the displayed matrix gives \(\operatorname{rank}L_{1+L}=3\); scaling by any nonzero real number preserves rank. Every other nonzero point of \(F=0\) consequently has rank exactly four, and the complement has rank five. Conjugating gives the right-hand classification.

**5. Exceptional one-sided asymmetry.** Substitution gives \(F(1-L)=-4\) and \(N(1-L)=3\), so \(\det L_{1-L}=-12\). As \(R_{1+L}=C L_{1-L} C\), \(R_{1+L}\) is invertible even though \(L_{1+L}\) has rank three. The same argument with sides exchanged handles \(1-L\).

## Verification

Run `python check_pentarnion.py` with Python and SymPy installed. The program builds the full bilinear multiplication tensor from the stated defining relations, constructs both multiplication matrices independently, proves the two polynomial determinant identities symbolically, checks the gradient identity, evaluates the exceptional rank-three cases and their nonsingular opposites, and checks 405 integer parameter vectors using exact matrix ranks and determinants. The provided `verification_output.txt` records its successful execution:

`VERIFY_OK polynomial_factorizations=2 gradient_identity=1 exact_integer_vectors=405 exceptional_left_rank=3 exceptional_right_rank=3`

Exact symbolic matrix identities are finite polynomial identities. The classification at all real points follows from the analytic-algebraic singular-point argument in the proof, **not** from the finite integer sample.

## Relationship to prior work

Poshtkohi and Pumplün introduce the underlying family in *From Quaternions to Pentarnions I* (2026), with canonical multiplication matrices in Appendix A. Their Section 5.3 defines the left and right zero divisors and computes determinant zero curves on the restricted three-dimensional slice \(\operatorname{span}\{1,j,k\}\). The present theorem instead factors both determinants on the full five-dimensional space and determines all possible multiplication ranks and the unique real corank-two directions. Their companion *A Five-Dimensional Nonassociative Algebra* studies functional calculus, nuclei, and differential equations, rather than providing this global rank stratification. The matrix presentation and the restricted zero-divisor observations are prior work, not novel here.

## Limitations

The theorem concerns only the canonical real algebra at the endpoint \(\gamma=1\); it does not classify all parameter values \(\gamma\), all coefficient fields, or all algebra isomorphism classes. The singular-point uniqueness is over \(\mathbb R\), not asserted over \(\mathbb C\). A nonzero algebra element's one-generated complex slice is distinct from the invertibility of global left or right multiplication in a nonassociative algebra. The source comparison cannot exclude every unindexed equivalent calculation; independent expert validation has not been performed.

## References

1. A. Poshtkohi and S. Pumplün, *From Quaternions to Pentarnions I: Algebra, geometry, and a spin model*, arXiv:2610.31485v1 (first publicly available 2026-10-22), especially Section 5.3 and Appendix A. https://arxiv.org/abs/2610.31485
2. A. Poshtkohi and S. Pumplün, *A Five-Dimensional Nonassociative Algebra: elliptic integrability and bracketing-dependent dynamics*, arXiv:2610.34202v1 (2026-10-25), especially Section 3. https://arxiv.org/abs/2610.34202
3. A. Poshtkohi and S. Pumplün, *From Quaternions to Pentarnions II: quadratic differential equations*, arXiv:2610.34201v1 (2026-10-25), a related dynamics-focused companion, inspected at the abstract level. https://arxiv.org/abs/2610.34201
