# The isolated binary almost-inner derivation of a free class-four Lie algebra

## Finding

For any field \(K\), let \(L_K\) be the free metabelian nilpotent Lie algebra of class four on two generators. Its eight-dimensional basis and bracket are given below. Write \(\operatorname{AID}(L_K)\) for the derivations \(D\) satisfying \(D(w)\in[L_K,w]\) for **every** \(w\in L_K\), and \(\operatorname{Inn}(L_K)\) for inner derivations.

**Theorem.** There is an exact field-cardinality dichotomy:
\[
\dim_K\bigl(\operatorname{AID}(L_K)/\operatorname{Inn}(L_K)\bigr)
=\begin{cases}1&K=\mathbb F_2,\\0&|K|>2.\end{cases}
\]
More explicitly, \(\dim_K\operatorname{Inn}(L_K)=5\) for every field. For \(K=\mathbb F_2\) there are precisely \(64\) almost-inner derivations, of which \(32\) are inner; for any finite field \(\mathbb F_q\) with \(q>2\), there are exactly \(q^5\) almost-inner derivations, all inner. The nontrivial quotient class over \(\mathbb F_2\) has a central representative \(T(x)=a\), \(T(y)=c\), and \(T\) vanishes on the commutator ideal. Thus the exceptional behavior depends on the **number of field elements**, not merely on characteristic two: it disappears over \(\mathbb F_4\).

## Assumptions and scope

Work with ordinary alternating Lie brackets, including in characteristic two. Let \(L_K\) have \(K\)-basis \(x,y,z,u,v,a,b,c\) with precisely the following nonzero brackets, together with their antisymmetric counterparts:
\[
[x,y]=z,\quad[z,x]=u,\quad[z,y]=v,\quad
[u,x]=a,\quad[u,y]=[v,x]=b,\quad[v,y]=c.
\]
All unlisted basis brackets vanish; in characteristic two the bracket is still alternating, so \([w,w]=0\) for all \(w\). The Jacobi identity is immediate on generators and follows on the remaining triples by the displayed equality \([u,y]=[v,x]\). This is the free two-generated class-four Lie algebra: its homogeneous dimensions in degrees one through four are \(2,1,2,3\), and its derived ideal is abelian (brackets of elements of degrees at least two vanish). It is therefore also the free two-generated metabelian class-four algebra. Its center is \(Z(L_K)=\langle a,b,c\rangle_K\).

## Proof

**1. Remove the noncentral part.** Consider the five-dimensional class-three quotient \(Q=L_K/Z(L_K)\), with basis \(x,y,z,u,v\) modulo the center. Every almost-inner derivation of \(Q\) is inner, over **any** field. Indeed, pass first to the three-dimensional Heisenberg quotient \(Q/Z(Q)\). An almost-inner derivation there must be inner: its values on \(x\) and \(y\) are multiples of the central element \(z\), and the two coefficients can be reproduced by an inner derivation. After subtracting a lift of that inner derivation, the map on \(Q\) has central image. It kills \([Q,Q]\) by the derivation rule, and its values have the form \(E(x)=\lambda u\), \(E(y)=\mu v\). The condition at \(x+y\), since \([Q,x+y]\cap Z(Q)=\langle u+v\rangle_K\), forces \(\lambda=\mu\); hence \(E=\operatorname{ad}(\lambda z)\). This proves \(\operatorname{AID}(Q)=\operatorname{Inn}(Q)\) without any infinite-field hypothesis.

Any \(D\in\operatorname{AID}(L_K)\) preserves the center and descends to \(Q\). Subtract an inner derivation of \(L_K\) lifting its inner image on \(Q\). The remainder \(E\) has central image; because it is a derivation, it kills \([L_K,L_K]\). The almost-inner conditions at \(x\) and \(y\) imply uniquely
\[
 E(x)=p a+h b,\qquad E(y)=r b+s c,
 \qquad p,h,r,s\in K.
\]
Every such central map is a derivation since all brackets lie in the derived ideal and every value is central.

**2. Apply the pointwise commutator condition.** For \(\alpha,\beta\in K\) and \(t\in[L_K,L_K]\), set \(w=\alpha x+\beta y+t\). Since \(E(t)=0\),
\[
 E(w)=\alpha p a+(\alpha h+\beta r)b+\beta s c.
\]
For \((\alpha,\beta)\ne(0,0)\), the commutator space \([L_K,w]\) always contains the following degree-four subspace:
\[
 \langle\alpha a+\beta b,\;\alpha b+\beta c\rangle_K.
\]
This is obtained by bracketing \(w\) with \(u\) and \(v\); contributions from \(t\) have no effect on these brackets. For \(t=0\), this is **exactly** the intersection \([L_K,\alpha x+\beta y]\cap Z(L_K)\). Therefore this span gives a necessary condition by testing \(t=0\), and a sufficient condition for all \(t\) since the subspace is always contained in \([L_K,w]\). The cases \(\alpha=0\) or \(\beta=0\) impose no extra restriction, and \((\alpha,\beta)=(0,0)\) is automatic. For \(\alpha\beta\ne0\), the determinant criterion for the three vectors to be dependent gives the exact condition
\[
 \alpha\beta\bigl(\alpha(s-h)+\beta(p-r)\bigr)=0.
\]
Thus \(E\) is almost inner precisely when \(\alpha(s-h)+\beta(p-r)=0\) for every pair of nonzero scalars \(\alpha,\beta\). If \(|K|>2\), fixing \(\beta=1\) and choosing two distinct nonzero \(\alpha\)'s forces \(s=h\), then \(p=r\). If \(K=\mathbb F_2\), there is only one pair \((\alpha,\beta)=(1,1)\), giving the single equation \(p-r+s-h=0\).

**3. Quotient by the central inner maps.** For \(h=\lambda u+\mu v\),
\[
 \operatorname{ad}(h)(x)=\lambda a+\mu b,
 \qquad\operatorname{ad}(h)(y)=\lambda b+\mu c.
\]
Therefore the central inner maps are exactly the two-dimensional subspace with \(p=r\), \(h=s\). It is all of the central almost-inner space if \(|K|>2\). Over \(\mathbb F_2\), the latter has dimension three, so the quotient has dimension one. A representative is \(T(x)=a\), \(T(y)=c\): it satisfies the single binary equation but is not inner, as its parameters are \((p,h,r,s)=(1,0,0,1)\).

Finally, \(\operatorname{Inn}(L_K)\cong L_K/Z(L_K)\) has dimension five. Adding the one-dimensional binary quotient yields the cardinalities stated above. The same reduction applied to class three (or the direct calculation for \(Q\)) shows that class four is the first class within the two-generator free metabelian nilpotent series where this binary exception can occur.

## Verification

A standalone standard-library program, `verify.py`, builds the eight-dimensional bracket independently from its seven defining structure constants. It checks alternating brackets, all basis Jacobi identities, the derivation rule for all central maps over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), and directly computes membership in the commutator subspace for every possible nonzero generator direction. It recovers central almost-inner counts \(8,9,16\), versus central-inner counts \(4,9,16\). Over \(\mathbb F_2\) it additionally checks all \(256\) algebra elements against the explicit exceptional derivation, checks all \(16\) central derivations against every element, and enumerates precisely \(32\) distinct inner derivations. The program finishes with `VERIFY_OK`.

These finite computations corroborate the structural proof; the assertion for arbitrary fields follows from the symbolic determinant argument, not finite enumeration.

## Relationship to prior work

Burde, Dekimpe and Verbeke [1, Proposition 6.3] establish \(\operatorname{AID}=\operatorname{Inn}\) for free two-generated metabelian nilpotent Lie algebras over **infinite** fields. Their proof explicitly uses the fact that a polynomial vanishing at all field elements has zero coefficients. The finite-field exception above falls outside those hypotheses and explains sharply why that infinitude assumption matters already in class four. Their Theorem 5.2 also covers the free class-three quotient, consistent with the elementary argument above.

The same authors [2, Theorem 2.2] treat free nilpotent Lie algebras over fields of **characteristic zero**. Kunyavskii and Ostapenko [3] introduce the Tate–Shafarevich interpretation and provide other nonzero examples; the specific class-four binary free-algebra quotient is not given there. Dietrich and de Graaf [4] develop computational tools and describe different examples, including examples in positive characteristic; they do not state the exact field-cardinality dichotomy for this free algebra. Claims of priority should remain conditional on further specialist review.

## Limitations

The result concerns the exact eight-dimensional free two-generator class-four algebra, not arbitrary nilpotent Lie algebras, and does not classify higher nilpotency classes. No statement is made about associative algebras or group analogues. The proof provides a universal field-cardinality dichotomy; finite computations verify only fields of orders two, three and four. No independent mathematical audit has been performed.

## References

[1] D. Burde, K. Dekimpe, B. Verbeke, *Almost inner derivations of Lie algebras* (2017), arXiv:1704.06159v1, https://arxiv.org/abs/1704.06159, especially Sections 5–6.

[2] D. Burde, K. Dekimpe, B. Verbeke, *Almost inner derivations of Lie algebras II* (2019), arXiv:1905.08145v1, https://arxiv.org/abs/1905.08145, Theorem 2.2.

[3] B. Kunyavskii, V. Z. Ostapenko, *Tate–Shafarevich groups and algebras* (2022), arXiv:2211.05406v2, https://arxiv.org/abs/2211.05406, Section 2.

[4] H. Dietrich, W. A. de Graaf, *A computational approach to almost-inner derivations* (2024), arXiv:2403.05905, https://arxiv.org/abs/2403.05905, Sections 2–4.
