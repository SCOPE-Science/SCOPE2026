# Prescribed ideal products in three-layer multiple-arrow path algebras

## Finding
Let \(k=\mathbb F_q\), where \(q\) is any prime power, and let \(a,b\ge1\). Consider the ordinary path algebra \(A=kQ\) of the acyclic quiver with \(a\) parallel arrows \(1\to2\), \(b\) parallel arrows \(2\to3\), and no other arrows. Let \(J=\operatorname{rad}(A)\), and let \(\mathcal I\) be the set of all two-sided ideals contained in \(J\). Products are ordered: \(IJ\) need not equal \(JI\).

Write \(V=k^a\), \(W=k^b\). The length-two path space is \(J^2=V\otimes W\), and \(J^3=0\). For integers \(d\ge0\), define
\[
g_d(q)=\sum_{i=0}^{d}\begin{bmatrix}d\\i\end{bmatrix}_q,
\quad
A_u(q)=\sum_{z=0}^{b}\begin{bmatrix}b\\z\end{bmatrix}_q g_{(a-u)(b-z)}(q),
\quad
B_z(q)=\sum_{u=0}^{a}\begin{bmatrix}a\\u\end{bmatrix}_q g_{(a-u)(b-z)}(q).
\]
Here the Gaussian coefficient counts vector subspaces. Put
\[
N=\sum_{u=0}^{a}\begin{bmatrix}a\\u\end{bmatrix}_q A_u(q)
=\sum_{z=0}^{b}\begin{bmatrix}b\\z\end{bmatrix}_q B_z(q).
\]
Then \(N=|\mathcal I|\). For every subspace \(P\le V\otimes W\), the exact prescribed-product fiber
\(F(P)=|\{(I,K)\in\mathcal I^2:IK=P\}|\) is
\[
\boxed{
F(P)=\begin{cases}
N(A_0+B_0)-A_0B_0,&P=0,\\
A_uB_z,&P=U\otimes Z\ne0,\ \dim U=u,\ \dim Z=z,\\
0,&\text{otherwise.}
\end{cases}}
\]
Every nonzero tensor-rectangle \(U\otimes Z\), with \(U\le V\) and \(Z\le W\) both nonzero, has a **unique** pair of tensor factors; the formula is therefore unambiguous.

The number \(C\) of ordered pairs of radical ideals whose products commute is
\[
\boxed{\begin{aligned}
C={}&N^2-2(N-A_0)(N-B_0)
+(N-A_0-B_0+g_{ab})^2\\
&+\sum_{u=1}^{a}\sum_{z=1}^{b}
\begin{bmatrix}a\\u\end{bmatrix}_q
\begin{bmatrix}b\\z\end{bmatrix}_q
 g_{(a-u)(b-z)}(q)^2.
\end{aligned}}
\]
Thus the commuting probability of two independent uniformly chosen radical ideals is exactly \(C/N^2\). The attainable nonzero product dimensions are **exactly** \(\{uz:1\le u\le a,\ 1\le z\le b\}\). At \(a=b=2\), a three-dimensional subspace of the four-dimensional central path space is an ideal but never an ideal product.

## Assumptions and scope
All ideals are two-sided \(k\)-linear ideals contained in the Jacobson radical of the **ordinary, unital** path algebra. The theorem does not assert these formulas for all ideals of \(A\), nor for Leavitt path algebras. The direction of multiplication is fixed by concatenating a first-stage arrow \(1\to2\) with a second-stage arrow \(2\to3\); reversing the convention exchanges the two roles but preserves the paired count formulas. There is no restriction on the characteristic of \(k\).

The result is valid for the entire finite-field family, not only the checked small dimensions. It includes a full classification of the image and every fiber of ideal multiplication restricted to \(\mathcal I\times\mathcal I\), not merely the zero fiber.

## Proof
**1. Classify radical ideals.** The three vertex idempotents are pairwise orthogonal and sum to \(1\). Since a two-sided ideal is preserved by left and right multiplication by each vertex idempotent, every \(I\subseteq J\) splits into its three Peirce components:
\[
I=U\oplus Z\oplus T,
\quad U\le V,\quad Z\le W,\quad T\le V\otimes W.
\]
The only nonzero product between positive-length path spaces is \(VW=V\otimes W\). Hence \(I\) is a two-sided ideal if and only if
\[
U\otimes W+V\otimes Z\subseteq T.
\]
The intersection of the two summands on the left is \(U\otimes Z\); their sum has codimension \((a-u)(b-z)\) in \(V\otimes W\), where \(u=\dim U\) and \(z=\dim Z\). Consequently, for each fixed \(U,Z\), precisely \(g_{(a-u)(b-z)}(q)\) choices of \(T\) exist. Summing first over \(Z\) or first over \(U\) proves the stated formulas for \(A_u\), \(B_z\), and \(N\). In particular, \(A_0\) is the number of ideals with \(U=0\); \(B_0\) is the number with \(Z=0\); and \(g_{ab}\) counts ideals with both components zero.

**2. Classify and count products.** For \(I=U\oplus Z\oplus T\) and \(K=U'\oplus Z'\oplus T'\), path concatenation gives
\[
IK=U\otimes Z'.
\]
There are no other possible nonzero terms, since all products involving a length-two path and all reverse-length or same-length incompatible products vanish. If \(U\otimes Z'\ne0\), its left and right contraction-support spaces are
\[
\operatorname{span}_{\lambda\in W^*}(\operatorname{id}_V\otimes\lambda)(U\otimes Z')=U,
\qquad
\operatorname{span}_{\mu\in V^*}(\mu\otimes\operatorname{id}_W)(U\otimes Z')=Z'.
\]
These identities use \(U,Z'\ne0\) and show that nonzero products uniquely determine the two factors. Fixing \(U\) leaves exactly \(A_u\) choices for \(I\); fixing \(Z'\) leaves exactly \(B_z\) choices for \(K\). The nonzero-product formula follows. The product vanishes exactly when \(U=0\) or \(Z'=0\); inclusion-exclusion gives \(F(0)=NA_0+NB_0-A_0B_0\).

**3. Count commuting ideal pairs.** Set \(N_{11}=N-A_0-B_0+g_{ab}\), the number of ideals with both arrow components nonzero. The two events \(IK\ne0\) and \(KI\ne0\) each have \((N-A_0)(N-B_0)\) ordered pairs. Their intersection has \(N_{11}^2\) pairs. Thus the number with both products zero is
\[
N^2-2(N-A_0)(N-B_0)+N_{11}^2.
\]
If both products are nonzero, uniqueness of rectangular tensor factors shows \(IK=KI\) exactly when \(U=U'\ne0\) and \(Z=Z'\ne0\). For any fixed \(U,Z\) the two ideals independently have \(g_{(a-u)(b-z)}\) possible central pieces. Summing their squares over all nonzero \(U,Z\) gives the final term of \(C\). The two cases (both zero and both equal nonzero) are disjoint and exhaustive. Lastly \(\dim(U\otimes Z)=uz\), and all nonzero factors occur as components of ideals, proving the sharp product-dimension spectrum.

**4. Worked minimal and first higher-dimensional cases.** For \(a=b=1\), the radical has precisely five two-sided ideals over **every** field: two ideals have nonzero first-arrow component, two have nonzero second-arrow component, and precisely four of the \(25\) ordered pairs have nonzero product. Hence \(F(0)=21\), \(F(J^2)=4\), and \(C=19\), so the ideal product is noncommutative even in the three-vertex single-arrow chain. For \(a=b=2\), \(q=2\), the formulas give \(N=124\), \(F(0)=13695\), and \(C=12682\); the attainable positive product dimensions are \(1,2,4\), not \(3\).

## Verification
The program `check_ideal_products.py` independently enumerates all subspaces by canonical reduced row-echelon matrices, constructs all radical ideals by imposing multiplication closure, computes every ordered ideal product from the actual basis tensors, and counts commuting products. Exhaustive configurations are \((a,b,q)=(1,1,2),(1,1,3),(2,1,2),(1,2,3),(2,2,2),(2,2,3)\). It uses modular inverses and hence covers the two **prime** fields shown, not extension fields.

The separate program `check_mass_identities.py` uses a recursive Gaussian-binomial implementation and verifies total mass, swapped-dimension symmetry and commuting bounds in \(175\) parameter configurations with \(1\le a,b\le5\) and integer prime powers \(q\in\{2,3,4,5,7,8,9\}\). Its tests for nonprime powers check arithmetic identities only, not direct extension-field ideal enumeration. The recorded outputs are in the two adjacent `.out` artifacts. All reported checks completed successfully. Neither finite verification is substituted for the proof over arbitrary fields.

## Relationship to prior work
Rangaswamy's April 26, 2016 preprint on **Leavitt** path algebras establishes distributivity and product-factorization properties of their two-sided ideals, including commutativity of ideal multiplication. Those algebras contain ghost-arrow and Cuntz–Krieger relations absent here. Indeed, for the ordinary three-vertex path algebra the multiplication of radical ideals is already noncommutative, so the Leavitt theorem cannot specialize to the present statement. Its focus on multiplicative ideal theory motivates comparing the two regimes; no claim is made that the Leavitt theorem is new. The QPA documentation describes a general computational operation `ProductOfIdeals` for ordinary path algebras, but provides no closed prescribed-product or commuting-probability census for the present family. Chakraborty and Patra (2026) study zero-product probabilities of ideals in **commutative** rings and explicitly propose an extension to noncommutative rings in their Problem 2. Their results do not cover the present ordered ideal products in noncommutative path algebras; this theorem concerns only radical-contained two-sided ideals, not the full ideal lattice. The standard path concatenation and Gaussian subspace counts are also prior tools, not new claims.

## Limitations
The closed formulas describe only ideals contained in the radical; ideals involving vertex idempotents are excluded. The family has precisely three layers and freely generated length-two paths, so path relations or longer directed paths may invalidate the tensor-rectangle property. The formulas give product fibers and commuting frequencies, not a classification of isomorphism types of individual ideals or a general structure theorem for all quiver ideal semigroups. No claim of independent mathematical validation or exhaustive historical priority is made. General ideal-incidence results not identified in the literature search may supply alternative derivations.

## References
1. K. M. Rangaswamy, *The Multiplicative Ideal Theory of Leavitt Path Algebras*, arXiv:1604.07865, first version posted 2016-04-26, https://arxiv.org/abs/1604.07865. Sections 1, 4 and 6 concern Leavitt-algebra ideal multiplication, a distinct algebra family.
2. S. Chakraborty and S. K. Patra, *Ideal Zero-Product Probability in Finite Commutative Rings*, arXiv:2608.14618, first version posted 2026-07-11, https://arxiv.org/abs/2608.14618. Section 10, Problem 2, suggests study of noncommutative rings; the paper does not establish the present radical-ideal product fibers.
3. QPA documentation, *Path Algebras*, Section 4.9-1, `ProductOfIdeals`, https://oyvinso.folk.ntnu.no/QPA/qpa/doc/chap4_mj.html, accessed for the documented general ideal-product operation; undated online reference.
