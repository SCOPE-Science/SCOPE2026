# A Cartier-square criterion for the Hermitian curve among characteristic-two cyclic-quintic genus-six covers

## Finding
Let \(k\) be any algebraically closed field of characteristic \(2\). For every monic squarefree quartic
\[
f(x)=x^4+a x^3+b x^2+c x+d\quad (a,b,c,d\in k),
\]
let \(X_f\) be the smooth projective curve \(y^5=f(x)\), and let \(\mathcal C\) denote Cartier on \(H^0(X_f,\Omega^1)\). Then \(X_f\) has genus \(6\), every Jacobian has geometric \(2\)-rank \(0\) and \(a\)-number \(3\), and the **entire sequence** of Cartier-power ranks is
\[
\big(\operatorname{rank}\mathcal C^0,\operatorname{rank}\mathcal C,
\operatorname{rank}\mathcal C^2,\operatorname{rank}\mathcal C^3,\ldots\big)
=\begin{cases}
(6,3,0,0,\ldots),&a=b=0,\\
(6,3,1,0,0,\ldots),&(a,b)\ne(0,0).
\end{cases}
\]
In particular, \(\mathcal C^2=0\) **if and only if** \(X_f\) is geometrically isomorphic to the Hermitian curve \(v^5=u^4+u\), **if and only if** its five branch points on \(\mathbf P^1_k\) form a projective image of \(\mathbf P^1(\mathbb F_4)\). The square-zero locus on the marked coefficient space is exactly the smooth codimension-two locus \(a=b=0,\ c\ne0\); its entire geometric family consists of one isomorphism class.

The normalized Hermitian representative is maximal over \(\mathbb F_{16}\), with exactly \(65\) rational points. Maximality is stated for that normalized model, not for every arithmetic twist of the geometric isomorphism class.

## Assumptions and scope
The base field is algebraically closed of characteristic \(2\); all coefficients range over this field subject to the quartic being squarefree. The equation gives a tame cyclic degree-five map \(X_f\to\mathbf P^1\), totally ramified over the four distinct finite roots and over infinity. The branch exponent is \(1\pmod 5\) at each of these five points. The geometric result concerns all such covers, not a finite-field sample. The distinguished affine chart places one branch point at infinity and normalizes the leading quartic coefficient to \(1\). All ranks refer to the semilinear Cartier operator on regular one-forms; they are dimensions of images over \(k\).

## Proof
**1. Smoothness and a basis.** Homogenize the affine equation to the degree-five plane curve
\[
F(X,Y,Z)=Y^5+X^4Z+aX^3Z^2+bX^2Z^3+cXZ^4+dZ^5=0.
\]
At its unique point at infinity \([1:0:0]\), \(F_Z=1\), so this point is smooth. At a finite point \(F_Y=Y^4\); simultaneous vanishing of \(F_Y\) and \(F_X\) would give a multiple root of \(f\), excluded by squarefreeness. Hence \(X_f\) is a smooth plane quintic and has genus \(6\). Adjunction gives the complete basis
\[
\omega_{ij}=x^iy^j\,dx/y^4,\qquad i,j\ge0,\quad i+j\le2.
\]
The six basis elements are \(\omega_{00},\omega_{10},\omega_{20},\omega_{01},\omega_{11},\omega_{02}\).

**2. Cartier calculation.** In characteristic two, the standard plane-curve Cartier formula gives, for \(h=x^iy^j\) of total degree at most two,
\[
\mathcal C(h\,dx/F_y)
=\left(\partial_x\partial_y(Fh)\right)^{1/2}\,dx/F_y,
\qquad F=y^5+f(x),\quad F_y=y^4.
\]
Every monomial surviving the mixed derivative has even exponents, so the indicated square root is a polynomial over the perfect field \(k\). Direct expansion, with the positive square roots denoting the unique Frobenius-inverse roots in \(k\), yields
\[
\begin{aligned}
\mathcal C(\omega_{00})&=0,&
\mathcal C(\omega_{10})&=\omega_{02},&
\mathcal C(\omega_{20})&=0,\\
\mathcal C(\omega_{01})&=c^{1/2}\omega_{00}+a^{1/2}\omega_{10},&
\mathcal C(\omega_{11})&=d^{1/2}\omega_{00}+b^{1/2}\omega_{10}+\omega_{20},&
\mathcal C(\omega_{02})&=0.
\end{aligned}
\]
Squarefreeness entails \((a,c)\ne(0,0)\), as \(f'=ax^2+c\). Thus the three nonzero displayed images, with inputs \(\omega_{10},\omega_{01},\omega_{11}\), are independent: respectively their new \(\omega_{02}\), nonzero \((\omega_{00},\omega_{10})\), and \(\omega_{20}\) components show it. Therefore \(\operatorname{rank}\mathcal C=3\), and \(a(X_f)=6-3=3\).

**3. Every iterate.** Cartier is Frobenius-inverse-semilinear. Applying it again to the preceding identities gives
\[
\mathcal C^2(\omega_{01})=a^{1/4}\omega_{02},\qquad
\mathcal C^2(\omega_{11})=b^{1/4}\omega_{02},
\]
with \(\mathcal C^2\) vanishing on the other four basis vectors. Consequently \(\operatorname{rank}\mathcal C^2\) is \(0\) when \(a=b=0\) and \(1\) otherwise. Since \(\mathcal C(\omega_{02})=0\), the cube \(\mathcal C^3\) vanishes identically. The stable image of Cartier therefore has dimension zero, equivalent to Jacobian geometric \(2\)-rank zero. This establishes both rank profiles for every squarefree quartic.

**4. Identifying the exceptional curve and its branch set.** If \(a=b=0\), squarefreeness is equivalent to \(c\ne0\). Choose \(\beta\in k\) solving \(\beta^4+c\beta+d=0\) and \(\alpha\in k^\times\) with \(\alpha^3=c\). Substituting \(x=\alpha u+\beta\) yields \(f(x)=\alpha^4(u^4+u)\); rescale \(y\) by a fifth root of \(\alpha^4\) to obtain \(v^5=u^4+u\), which, with \(u,v\) interchanged, is the standard Hermitian equation \(Y^4+Y=X^5\) over characteristic two. Its five branch points are \(\{\infty\}\cup\mathbb F_4\) in the normalized \(u\)-coordinate, because \(u^4+u\) has exactly the four roots of \(\mathbb F_4\). Conversely, any projective five-point branch set equivalent to \(\mathbf P^1(\mathbb F_4)\) can be transported so that a branch point lies at infinity and the four others are an affine image of \(\mathbb F_4\). The unique tame degree-five Kummer cover having branch exponent \(1\) at all five points is then, up to a fifth-power change of \(y\), defined by \(v^5=u^4+u\). Indeed the ratio of two defining rational functions with the same branch exponents has divisor divisible by five; on \(\mathbf P^1\) it is a constant times a fifth power, and the constant has a fifth root in \(k\). Therefore branch equivalence implies Hermitian isomorphism; this implies \(\mathcal C^2=0\) by invariance and the explicit calculation on the Hermitian model. This completes the equivalence. The coefficient equations \(a=b=0, c\ne0\) define a nonempty smooth codimension-two locus in the squarefree locus, and both Cartier profiles occur (e.g. \(f=x^4+x\) and \(f=x^4+x^2+x\)).

**5. Arithmetic property of the exceptional representative.** Over \(\mathbb F_{16}\), \(u\mapsto u^4+u\) is the trace to \(\mathbb F_4\) and has four preimages for each target. The map \(v\mapsto v^5\) is the norm to \(\mathbb F_4\), having one preimage of zero and five preimages of each of the three nonzero targets. There are therefore \(4(1+3\cdot5)=64\) affine points, plus the single point at infinity: \(65=16+1+2\cdot6\cdot4\), exactly the Hasse--Weil upper bound for genus six over \(\mathbb F_{16}\).

## Verification
The accompanying standalone Python 3 script `verify_cartier.py` independently constructs the semilinear Cartier matrix from the mixed-partial formula on the plane quintic, without hardcoding the six displayed Cartier images. It exhausts all \(256\) monic quartics over \(\mathbb F_4\), finds the \(192\) squarefree ones, and confirms that the \(180\) generic and \(12\) special smooth coefficient tuples have rank triples \((3,1,0)\) and \((3,0,0)\), respectively. It separately counts all points of the Hermitian representative over \(\mathbb F_{16}\) and obtains \(65\). The symbolic derivation in the proof establishes the infinite-field theorem; these finite computations are cross-checks, not an extrapolation.

Run `python3 verify_cartier.py` using the Python 3 standard library alone.

## Relationship to prior work
Bouw's *The p-Rank of Ramified Covers of Curves* derives general generalized Hasse--Witt coefficient formulas for tame cyclic covers of \(\mathbf P^1\), notably Section 5 and Lemma 5.1, and provides the broad arithmetic context. It does not state the complete Cartier-power stratification or the equivalence between Cartier-square vanishing and the Hermitian five-branch-point geometry for this characteristic-two family. Its general machinery can in principle be specialized to compute Hasse--Witt matrices, so the contribution here is the **completed uniform rank-and-geometric-locus classification**, not a new general Cartier formula.

Pries and Weir's *The Ekedahl--Oort Type of Jacobians of Hermitian Curves* determines the much stronger \(2\)-torsion group-scheme type for the Hermitian member; their result subsumes previously known invariants of that one member. No new Hermitian Ekedahl--Oort type, maximality property, or automorphism-group classification is claimed. Their result does not determine which members of the full five-branch-point cyclic-quintic family are characterized by \(\mathcal C^2=0\), or the complement's Cartier-power ranks. The exact geometric characterization and the two-stratum full-family statement are the contribution assessed here.

## Limitations
Only cyclic degree-five covers with five distinct branch points of equal Kummer exponent \(1\) in characteristic two are covered. The generic family is not asserted to be supersingular, nor is the complete Ekedahl--Oort type of its Jacobian determined. Over a non-algebraically-closed base field, geometric isomorphism to the Hermitian curve does not imply that every twist is maximal over \(\mathbb F_{16}\). Historical originality is provisional: an unindexed worked specialization of general cyclic-cover formulae may already encode the same two strata. Independent review is not asserted here.

## References
1. I. I. Bouw, *The p-Rank of Ramified Covers of Curves*, Compositio Mathematica **126** (2001), 295--322, DOI: https://doi.org/10.1023/A:1017513122376. Public full-text online presentation dated 2007-12-04: https://www.cambridge.org/core/journals/compositio-mathematica/article/prank-of-ramified-covers-of-curves/6D1BEC9200F6849339665AC4371AB7AF. Relevant Sections 4--5.
2. R. Pries and C. Weir, *The Ekedahl--Oort Type of Jacobians of Hermitian Curves*, arXiv:1302.6261, initially submitted 2013-02-25: https://arxiv.org/abs/1302.6261. Relevant Sections 1--2 and the \(n=2\) Hermitian case.
