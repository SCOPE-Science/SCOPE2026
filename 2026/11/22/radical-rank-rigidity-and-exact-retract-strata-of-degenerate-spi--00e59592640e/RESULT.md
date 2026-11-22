# Radical-rank rigidity and exact retract strata of degenerate spin-factor Jordan algebras

## Finding
For any field \(k\) with \(\operatorname{char}k\ne2\), any nondegenerate symmetric \(m\)-space \((W,B)\) with \(m\ge2\), and any radical space \(R\) of dimension \(r\ge0\), consider the spin-factor Jordan algebra \(J=k1\oplus W\oplus R\) with radical form \(B\oplus0\). Every Jordan algebra endomorphism, with no assumption that it preserves the identity, is either zero or uniquely
\[
F_{G,S,U}(a,w,v)=(a,Gw,Sw+Uv),
\]
where \(G\in O(W,B)\), \(S\in\operatorname{Hom}_k(W,R)\), and \(U\in\operatorname{End}_k(R)\). The nonzero maps have rank \(1+m+\operatorname{rank}U\); the automorphisms are exactly those with \(U\) invertible. Composition is
\[
F_{G,S,U}\circ F_{H,T,P}=F_{GH,\,SH+UT,\,UP}.
\]

A nonzero map is composition-idempotent (a Jordan algebra retraction) precisely when \(G=I_W\), \(U^2=U\), and \(US=0\). Over \(k=\mathbb F_q\), \(q\) odd, write \(\begin{bmatrix}r\\j\end{bmatrix}_q\) for the Gaussian binomial coefficient, and \(O(W,B)\) for the rational isometry group. The **complete labeled rank polynomials** of all endomorphisms and of retractions are respectively
\[
\mathcal E_{m,r}(X)=1+|O(W,B)|q^{mr}\sum_{j=0}^r
\begin{bmatrix}r\\j\end{bmatrix}_q^2 |\mathrm{GL}_j(\mathbb F_q)|X^{m+1+j},
\]
\[
\mathcal R_{m,r}(X)=1+\sum_{j=0}^r
\begin{bmatrix}r\\j\end{bmatrix}_q q^{(r-j)(m+j)}X^{m+1+j}.
\]
In particular, **retraction counts and rank spectra are independent of the Witt type of the nondegenerate quotient**, although counts of arbitrary endomorphisms retain the \(|O(W,B)|\) factor. There are exactly \(r+2\) conjugacy classes of retractions under \(\operatorname{Aut}(J)\), including the zero map; each nonzero rank occurs in one orbit. The geometric retraction locus, reduced and base-changed to an algebraic closure, consists of the isolated zero point and exactly \(r+1\) further smooth irreducible closed components. The component whose maps have rank \(m+1+j\) has dimension
\[
(r-j)(m+2j),\qquad 0\le j\le r.
\]

**Intermediate-rank concentration.** For fixed odd \(q\) and fixed quotient dimension \(m\), as the radical dimension \(r\) grows, the rank index \(j\) of a uniformly chosen nonzero retraction remains within a bounded distance (with uniformly Gaussian-decaying tails) of
\[
j_*=\frac r2-\frac m4.
\]
The asymptotically typical retraction therefore has neither the smallest nor the largest nonzero rank. More precisely, for \(r\ge m/2\), if \(c_q=\prod_{h\ge1}(1-q^{-h})\), then for every \(t\ge0\),
\[
\Pr(|j-j_*|\ge t)\le c_q^{-1}q^{1/2}
\sum_{\substack{a\in\mathbb Z\\|a-j_*|\ge t}}q^{-2(a-j_*)^2}.
\]

## Assumptions and scope
The algebra is the commutative unital Jordan algebra with product
\[
(a,w,v)\circ(b,x,u)=\big(ab+B(w,x),\;ax+bw,\;au+bv\big).
\]
Here \(a,b\in k\), \(w,x\in W\), \(v,u\in R\). The dimension is \(1+m+r\). A homomorphism is \(k\)-linear and product-preserving, but need not be unital. The rank of a homomorphism means its ordinary linear rank. Endomorphism and retraction polynomials count **labeled maps on the fixed algebra**, not isomorphism types. The geometric assertion concerns the *reduced* variety, not an unproved assertion about scheme-theoretic multiplicities of the unrestricted homomorphism equations. For \(r=0\), the only retractions are zero and identity, and the only endomorphisms are zero and the orthogonal automorphisms.

## Proof
**1. Idempotent images force the unit.** Let \(F\) be a multiplicative \(k\)-linear map and \(e=F(1)\). Then \(e^2=e\) and \(e\circ F(x)=F(x)\) for all \(x\). An idempotent \(e=(a,w,v)\) satisfies \(a^2+B(w,w)=a\), \(2aw=w\), \(2av=v\). Thus \(e=0\), \(e=1\), or \(e=(1/2,w,v)\) with \(B(w,w)=1/4\); the final case allows any radical component \(v\), and the Peirce-one space is exactly \(J_1(e)=ke\). Indeed, \(e\circ(b,x,u)=(b,x,u)\) implies \(x=2bw\), \(u=2bv\), and the scalar equation then holds by \(B(w,w)=1/4\). Thus the vector is \(2be\). If \(e=0\) then \(F=0\). If \(e\notin\{0,1\}\), every value lies on \(ke\); consequently \(F(x)=\chi(x)e\) for a multiplicative linear functional \(\chi\) with \(\chi(1)=1\). On pure vectors \(W\oplus R\), the relation \(\chi(x)\chi(y)=B(x,y)\) would express a form of rank \(m\ge2\) as a rank-at-most-one tensor, impossible. Therefore every nonzero endomorphism is unital.

**2. Unital maps preserve the scalar and radical splitting.** For \(V=W\oplus R\) write \(F(v)=\varphi(v)1+T(v)\), where \(\varphi\in V^*\) and \(T\in\operatorname{End}(V)\). Applying \(F\) to \(v\circ w=B(v,w)1\) yields
\[
B(Tv,Tw)+\varphi(v)\varphi(w)=B(v,w),\qquad
\varphi(v)Tw+\varphi(w)Tv=0.
\]
If \(\varphi\ne0\), select \(v\) with \(\varphi(v)\ne0\). The second identity with \(w=v\) gives \(Tv=0\), since \(2\ne0\); with \(w\in\ker\varphi\), it gives \(Tw=0\). Hence \(T=0\), contradicting \(\operatorname{rank}B=m\ge2\). Thus \(\varphi=0\), and \(B(Tv,Tw)=B(v,w)\). The induced map on \(V/R\cong W\) is an isometry, hence invertible; pairing against its image shows \(T(R)\subseteq R\). Relative to \(W\oplus R\), this is exactly \(T(w,v)=(Gw,Sw+Uv)\) with \(G\in O(W,B)\) and arbitrary \(S,U\). Conversely all such maps respect the defining multiplication, proving the classification and composition law.

**3. Idempotents, ranks and orbits.** Squaring the block form gives \(G^2=G\), \(US+SG=S\), \(U^2=U\). Since \(G\) is invertible, \(G=I\), so the middle equation becomes \(US=0\). Its linear rank is \(m+1+\operatorname{rank}U\). A rank-\(j\) projection \(U\) corresponds to an ordered splitting \(R=\operatorname{im}U\oplus\ker U\), and there are \(\begin{bmatrix}r\\j\end{bmatrix}_q q^{j(r-j)}\) such splittings. Once \(U\) is fixed, \(S(W)\subseteq\ker U\) gives \(q^{m(r-j)}\) choices. For conjugacy, an invertible radical change of basis conjugates \(U\) to \(\operatorname{diag}(I_j,0)\). Conjugating by a block shear \(F_{I,T,I}\) changes \(S\) to \(S+(I-U)T\). Since \(US=0\), take \(T=-S\) to kill it. Therefore precisely one automorphism orbit occurs at each allowed nonzero rank.

**4. All-endomorphism counts.** For rank-\(j\) arbitrary \(U\), independently choose its image, its kernel, and the induced isomorphism \(R/\ker U\to\operatorname{im}U\). This gives \(\begin{bmatrix}r\\j\end{bmatrix}_q^2|\mathrm{GL}_j(\mathbb F_q)|\). The choices of \(G\) and \(S\) are independent and number \(|O(W,B)|q^{mr}\). Adding the zero map proves \(\mathcal E_{m,r}\). To obtain the concentration estimate, use the standard product formula for Gaussian coefficients to bound \(q^{j(r-j)}\le\begin{bmatrix}r\\j\end{bmatrix}_q\le c_q^{-1}q^{j(r-j)}\). Thus the positive retraction weight in index \(j\) lies between \(q^{f(j)}\) and \(c_q^{-1}q^{f(j)}\), with \(f(j)=(r-j)(m+2j)=f(j_*)-2(j-j_*)^2\). The denominator of the normalized distribution is at least \(q^{f(j_*)-1/2}\), from an integer nearest \(j_*\), proving the uniform tail bound.

**5. Geometric components.** Over the algebraic closure, rank-\(j\) projections are the homogeneous variety of ordered complementary \(j\)- and \((r-j)\)-subspaces, smooth irreducible of dimension \(2j(r-j)\). The allowable shears form the vector bundle \(\operatorname{Hom}(W,\ker U)\), of fiber dimension \(m(r-j)\). The rank-\(j\) idempotent-matrix orbit is closed because its elements are semisimple with fixed eigenvalue multiplicities, so the associated vector bundle gives a closed irreducible component of the reduced retraction locus. These \(r+1\) components are disjoint, while the zero homomorphism is isolated by the idempotent equation for \(F(1)\) and the unit relation. Dimensions and the component count follow.

## Verification
The accompanying standard-library script `verify.py` exhausts all unital linear maps on a four-dimensional example over \(\mathbb F_3\) after a logically necessary square constraint, checks the original Jordan homomorphism equations, verifies the absence of scalar characters, and counts retractions by independently enumerating all radical matrices. With \(m=2,r=1\) and \(B|_W=\operatorname{diag}(1,1)\), there are \(72\) endomorphisms of rank three and \(144\) of rank four, plus zero. With \(m=2,r=2\), the nonzero retraction rank counts over \(\mathbb F_3\) are \(81,108,1\). Run `python3 verify.py`; it prints `DEGENERATE_SPIN_RETRACTIONS_VERIFIED`. The finite checks corroborate, but do not replace, the arbitrary-dimensional proof.

## Relationship to prior work
Fideles and Martino (2023, 2024 journal volume) analyze polynomial identities and the Specht property for the same class of degenerate bilinear-form Jordan algebras; their decomposition into a nondegenerate spin-factor part and a degenerate part is prior. Martino (2013) studies the group gradings and identities of these algebras. Fidelis, Diniz and Koshlukov (2018) treat embeddings and trace identities for nondegenerate form Jordan algebras, including their orthodox orthogonal symmetry. Those results motivate the question but were not found to furnish the full endomorphism-monoid normal form, the nonunital exclusion, or the labeled retraction rank and orbit formulas. The 2026 paper by Fideles, Salomão and Riva concerns finite-field graded identities, not an enumerative retraction classification. A directly relevant 2023 author preprint was identified but its full text was inaccessible for final comparison; absence of an exact indexed match is not proof of publication priority.

## Limitations
The theorem requires \(\operatorname{char}k\ne2\) and nondegenerate quotient dimension at least two. If the quotient form has rank one, character-type nonunital maps can appear and the normal form fails. The geometric statement is for the reduced locus. Full conjugacy classification of arbitrary non-idempotent endomorphisms, deformations of the homomorphism scheme and characteristic-two analogues are not claimed. Prior-art confidence is provisional because the plausible author preprint could not be examined in full, and general radical-extension treatments may contain an equivalent implication.

## References
1. C. Fideles and F. Martino, *Jordan algebras of a degenerate bilinear form: Specht property and their identities*, Journal of Algebra **637** (2024), 193–229. DOI: https://doi.org/10.1016/j.jalgebra.2023.09.032. Earliest verified public record: 2023-11-08.
2. F. Martino, *Polynomial identities for the Jordan algebra of a degenerate symmetric bilinear form*, Linear Algebra and its Applications **439** (2013), 4080–4089. https://doi.org/10.1016/j.laa.2013.10.013.
3. C. Fidelis, D. Diniz and P. Koshlukov, *Embeddings for the Jordan algebra of a bilinear form*, Advances in Mathematics **337** (2018), 294–316. https://doi.org/10.1016/j.aim.2018.08.014.
4. C. Fideles, M. E. Salomão and E. Riva, *Graded identities for the Jordan algebra of the symmetric matrices of order two over finite fields*, Finite Fields and Their Applications **113** (2026), article 102826. https://doi.org/10.1016/j.ffa.2026.102826.
