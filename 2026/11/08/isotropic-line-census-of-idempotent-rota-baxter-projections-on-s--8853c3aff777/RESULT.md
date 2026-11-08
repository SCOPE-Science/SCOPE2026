# Isotropic-line census of idempotent Rota–Baxter projections on short local algebras

## Finding
Let \(k\) be any field, \(V\) a two-dimensional \(k\)-vector space, and \(B:V\times V\to k\) a **nonzero symmetric bilinear form** (degeneracy is allowed). Set
\[
 A_B=k1\oplus V\oplus kz,\qquad uv=B(u,v)z,\qquad z(V\oplus kz)=0.
\]
This is a commutative associative local algebra with radical \(\mathfrak m=V\oplus kz\), radical square \(\mathfrak m^2=kz\), and \(\mathfrak m^3=0\). Consider \(k\)-linear operators \(P:A_B\to A_B\) satisfying
\[
 P^2=P,\qquad P(a)P(b)=P(P(a)b+aP(b)-ab)\quad(a,b\in A_B).
\]
Write \(\mathcal Q_B(k)=\{[v]\in\mathbb P(V)(k):B(v,v)=0\}\). Every such operator is obtained *uniquely* from one of the two orientations of a direct-sum decomposition
\[
 \mathfrak m=U\oplus W,
\]
where \(U,W\) are (possibly zero) subalgebras of \(\mathfrak m\): project onto \(k1\oplus U\) along \(W\), or project onto \(W\) along \(k1\oplus U\). Apart from \((U,W)=(0,\mathfrak m),(\mathfrak m,0)\), all decompositions arise from an isotropic direction \([v]\in\mathcal Q_B(k)\), a line \(L=k(v+cz)\) lifting it, and a plane \(H=kz\oplus kw\) with \([w]\ne[v]\), with \((U,W)=(L,H)\) or \((H,L)\). Here \(v\) is any fixed representative of the direction and \(c\in k\). In particular the classification is valid over arbitrary fields, including characteristic two and imperfect fields.

For any finite field \(k=\mathbb F_q\), let \(h_B=|\mathcal Q_B(k)|\) and \(N_B=h_Bq^2\). The **complete rank polynomial** (counting labeled linear operators, not conjugacy classes) is
\[
 \boxed{\mathscr R_{B,q}(T)=1+(1+N_B)T+2N_BT^2+(1+N_B)T^3+T^4.}
\]
Consequently the exact number is \(4+4h_Bq^2\). The nontrivial operators exist if and only if the quadratic function \(v\mapsto B(v,v)\) has a nonzero isotropic vector.

For odd \(q\), \(h_B=0\) for an anisotropic nondegenerate form, \(h_B=2\) for a split nondegenerate form, and \(h_B=1\) for a rank-one form. For even \(q\), \(h_B=q+1\) when \(B\) is alternating and \(h_B=1\) when \(B\) is nonalternating. Thus the census detects arithmetic isotropy even though every algebra in the family has the same radical Hilbert dimensions \((1,2,1)\). For example \(k[x,y]/(x^2,y^2)\) has \(h_B=2\) in odd characteristic and \(h_B=q+1\) in characteristic two, giving totals \(4+8q^2\) and \(4+4q^2(q+1)\), respectively.

## Assumptions and scope
All subalgebras in this statement are \(k\)-linear, multiplicatively closed, and may be nonunital. The form \(B\) is symmetric and not identically zero; no claim is made for \(B=0\), where the radical is square-zero and the plane classification changes. The operator identity is for **weight minus one** with the explicit normalization written above. Rank is linear-algebraic rank over the base field. No passage to an algebraic closure is made when counting \(\mathbb F_q\)-rational operators.

## Proof
**1. Projection–splitting equivalence.** If \(P^2=P\), the Rota–Baxter identity of weight minus one is equivalent to both \(\operatorname{im}P\) and \(\ker P\) being subalgebras. To see necessity, substitute respectively two elements of the image or two elements of the kernel. Conversely, for the direct sum \(A_B=A_+\oplus A_-\) of subalgebras, projection onto \(A_+\) gives
\[
 P(P(a)b+aP(b)-ab)=P(a_+b_+-a_-b_-)=a_+b_+=P(a)P(b).
\]
This classical equivalence is prior literature, not part of the originality claim.

**2. The unit occurs in exactly one summand.** Any subalgebra \(S\subseteq A_B\) containing \(s\) with nonzero scalar residue contains \(1\). Indeed \(s\) is invertible, so its minimal polynomial over \(k\) has nonzero constant coefficient. Rearranging that relation expresses \(1\) as a linear combination of positive powers of \(s\), all belonging to \(S\). Two complementary subalgebras cannot both contain \(1\), and they cannot both lie in the radical. Hence exactly one contains \(1\), and writing it \(k1\oplus U\), the other is \(W\subseteq\mathfrak m\), with \(\mathfrak m=U\oplus W\). Both \(U\) and \(W\) are subalgebras. The two orientations yield distinct projections.

**3. Subalgebras of the radical.** Let \(\pi:\mathfrak m\to V\) be projection with kernel \(kz\). Every line \(L\subset\mathfrak m\) is closed under multiplication exactly when it is \(kz\) or has the form \(L=k(v+cz)\) with \(v\ne0\) and \(B(v,v)=0\). This follows from \((v+cz)^2=B(v,v)z\) and \(z\notin L\) in the latter case. Every plane containing \(kz\) is a subalgebra. No plane excluding \(kz\) is a subalgebra: its image under \(\pi\) is all of \(V\), and since \(B\ne0\), the products of lifts of suitable \(v,w\in V\) give a nonzero multiple of \(z\) outside the plane. The zero space and the entire radical are also subalgebras.

**4. Complement classification.** A decomposition of the three-space \(\mathfrak m\) either has dimensions \((0,3)\), \((3,0)\), \((1,2)\), or \((2,1)\). In the last two cases the plane must contain \(kz\), and the complementary line cannot be \(kz\). Therefore the line is a lift of an isotropic projective direction \([v]\), and the plane corresponds to a different direction \([w]\) in \(\mathbb P(V)\). Conversely every such choice is a decomposition into subalgebras. A nonzero representative \(v\) fixed for each \([v]\) makes the coefficient \(c\) unique. No extra multiplicative restrictions occur across complementary subalgebras.

**5. Finite-field enumeration and ranks.** Each isotropic direction has precisely \(q\) lifting lines and \(q\) complementary projective plane-directions, so there are \(N_B=h_Bq^2\) line–plane complementary pairs. Each occurs in two orders, and each ordered decomposition produces two complementary projections. The two trivial radical decompositions contribute exactly one rank-zero, one rank-four, and one each of rank one and rank three. The \((1,2)\) decompositions contribute two rank-two projections apiece. The \((2,1)\) decompositions contribute one rank-one and one rank-three projection apiece. Hence the stated polynomial.

**6. Isotropy counts.** If \(\operatorname{char}k\ne2\), the binary homogeneous quadratic polynomial \(B(v,v)\) has \(0,1,2\) rational projective roots over \(\mathbb F_q\), according to its anisotropic nondegenerate, rank-one, or split nondegenerate type. In characteristic two, its mixed term cancels. Over a finite (hence perfect) field it is the square of a linear form, so it has one rational projective zero if nonzero; if \(B\) is alternating, it is identically zero and all \(q+1\) projective directions occur. These cases exhaust nonzero symmetric binary forms.

## Verification
The standalone script `check_short_local_rb.py` constructs all subspaces of the three-dimensional radical over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\), checks closure using actual algebra multiplication, constructs each complementary projection, tests the Rota–Baxter identity on every ordered pair of basis vectors, checks uniqueness, and compares observed ranks with the theorem. For each of three bilinear forms in \(\mathbb F_2\), it **also independently enumerates all \(2^{16}=65,536\) linear endomorphisms** of the four-dimensional algebra and tests idempotence and the Rota–Baxter identity directly. All tests passed; exact output is in `check_results.txt`.

Representative checked counts: for alternating \(B\) over \(\mathbb F_2\), ranks \((0,1,2,3,4)\) have counts \((1,13,24,13,1)\); for anisotropic diagonal \(B\) over \(\mathbb F_3\), they have \((1,1,0,1,1)\); for alternating \(B\) over \(\mathbb F_4\), they have \((1,81,160,81,1)\). Finite tests corroborate but do not replace the all-field proof.

## Relationship to prior work
An and Bai (2007) classify weight-one Rota–Baxter operators on complex associative algebras of dimension at most three, not this four-dimensional all-field local family. Jian (2013), especially Remark 2.5, describes projections arising from a decomposition into subalgebras; this general correspondence is the starting point, not a new contribution. Benito, Gubarev and Pozhidaev (2018) show that nonzero-weight operators on the exterior algebra of two generators are splitting, but work in characteristic different from two and on a noncommutative exterior product; they do not count the idempotent operators on the commutative \(A_B\) family. Farooq (2026) classifies operators on algebras with \(\mathfrak m^2=0\), whereas the family here has \(\mathfrak m^2=kz\ne0\). Neither the general splitting criterion nor these inspected special classifications specifies the present isotropic-line rank enumerator. An independent priority review has not been performed.

## Limitations
The result concerns idempotent weight-minus-one operators only. It does not classify non-idempotent Rota–Baxter operators, arbitrary four-dimensional local algebras, or the nonreduced scheme of all operator equations. The field-count statements require finite fields; over general fields the classification is set-theoretic in terms of rational projective isotropic directions. The classification is claimed as a proved result, not as a certificate of independent originality or independent audit.

## References
1. H. An and C. Bai, *From Rota-Baxter Algebras to Pre-Lie Algebras*, arXiv:0711.1389, first public 2007-11-09; full preprint especially Abstract and Sections 1 and 4.
2. R.-Q. Jian, *Construction of Rota-Baxter algebras via Hopf module algebras*, arXiv:1307.6966, first public 2013-07-26; Remark 2.5 and Section 2.
3. P. Benito, V. Gubarev, A. Pozhidaev, *Rota–Baxter Operators on Quadratic Algebras*, arXiv:1801.07037, first public 2018-01-22; Section 2 and Section 4.4.
4. A. Farooq, *Rota Baxter Operators on Truncated Polynomial Algebras*, arXiv:2605.15670, first public 2026-05-15; Sections 2–4, with square-zero radical hypothesis.
