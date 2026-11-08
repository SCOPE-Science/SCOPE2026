# The degree-fifteen six-double-fibre discriminant and its bielliptic reconstruction

## Finding

Let \(U\subset\mathbb P(\operatorname{Sym}^6\mathbb C^2)\cong\mathbb P^6\) denote the open set of squarefree binary sextics. For \(f=\prod_{i=1}^6\ell_i\), with linear forms \(\ell_i\), let \(\mathfrak M\) be the fifteen partitions of \(\{1,\ldots,6\}\) into three unordered pairs. For a partition \(\pi=\{\{i,j\},\{k,l\},\{m,n\}\}\), write \(q_1=\ell_i\ell_j\), \(q_2=\ell_k\ell_l\), \(q_3=\ell_m\ell_n\), and set
\[
\Delta_\pi(f)=\det\begin{pmatrix}
[q_1]_{X^2}&[q_1]_{XZ}&[q_1]_{Z^2}\\
[q_2]_{X^2}&[q_2]_{XZ}&[q_2]_{Z^2}\\
[q_3]_{X^2}&[q_3]_{XZ}&[q_3]_{Z^2}
\end{pmatrix},\qquad
\mathcal B(f)=\prod_{\pi\in\mathfrak M}\Delta_\pi(f).
\]
The choice of an order for the three rows determines the sign of an individual determinant, but the product, with a consistent root-label convention, is well defined up to a nonzero universal sign. Its zero set is intrinsic.

**Theorem (over \(\mathbb C\)).** On \(U\), the following conditions are equivalent:

1. The six zeros of \(f\) occur as the six singular-fibre parameters of a rational elliptic surface with section whose six singular fibres all have Kodaira type \(I_2\).
2. \(\mathcal B(f)=0\).
3. The genus-two curve \(Y_f:\ y^2=f(t,1)\) admits a degree-two map to a genus-one curve (equivalently, its Jacobian is geometrically \((2,2)\)-split).

Moreover, \(\mathcal B\) is a nonzero, irreducible, homogeneous polynomial of degree \(15\) in the seven coefficients of \(f\), up to nonzero scalar. Thus the **reduced** closure of the six-\(I_2\) branch-position locus in \(\mathbb P^6\) is an irreducible degree-fifteen hypersurface, identified on the squarefree locus with the genus-two bielliptic (Humbert-discriminant-four) divisor. The branch-position map from the two-dimensional moduli space of the above elliptic surfaces to that divisor modulo \(\operatorname{PGL}_2\) is birational, and an explicit inverse is given below.

The degree-fifteen hypersurface is not everywhere smooth on \(U\). Along a dense open part of the family with six roots \(\{1,-1,a,-a,a^{-1},-a^{-1}\}\), where these are pairwise distinct, it has an ordinary two-branch transverse crossing. This is a statement about the hypersurface in \(\mathbb P^6\), not about the analytic singularity of its coarse moduli quotient.

## Assumptions and scope

The ground field is \(\mathbb C\). The sextic is squarefree; all roots and the three quadratic factors of any selected pairing are distinct. Elliptic surfaces are relatively minimal rational elliptic surfaces equipped with a zero-section; their fibre configurations consist of exactly six \(I_2\) fibres. Their isomorphisms may act on the base \(\mathbb P^1\). The claim concerning the hypersurface uses the reduced structure. No statement is made about its full singular locus at special automorphism configurations or about binary sextics on the discriminant boundary.

## Proof

**1. Equivalence with a dependent triple of quadratic forms.** The split Weierstrass normal form established for six-\(I_2\) rational elliptic surfaces in Ciliberto–Grassi–Miranda–Verra–Zanardini, Section 2.4, is
\[
y^2=(x-Q_1(t))(x-Q_2(t))(x-Q_3(t)),\qquad Q_i\in H^0(\mathbb P^1,\mathcal O(2)),\quad Q_1+Q_2+Q_3=0.
\]
Its discriminant, up to a nonzero constant depending on convention, is
\[
\prod_{1\le i<j\le3}(Q_i-Q_j)^2.
\]
Because the six fibre positions are distinct, the three quadratic differences have two simple, pairwise disjoint zeros. They are linearly dependent since \((Q_1-Q_2)+(Q_2-Q_3)+(Q_3-Q_1)=0\). Consequently one of the fifteen determinants vanishes.

Conversely suppose \(\Delta_\pi=0\). The three quadratic forms \(q_1,q_2,q_3\) for that partition are pairwise independent and have disjoint root sets, so the unique linear relation can be written \(A+B+C=0\) after rescaling each \(q_i\) by a nonzero scalar. Put
\[
Q_1=(2A+B)/3,\quad Q_2=(B-A)/3,\quad Q_3=-(A+2B)/3.
\]
Then \(Q_1-Q_2=A\), \(Q_2-Q_3=B\), \(Q_3-Q_1=C\), and \(\sum Q_i=0\). The split Weierstrass cubic above has discriminant a nonzero scalar multiple of \(f^2\). Its only singular fibres are precisely six type-\(I_2\) fibres: at each simple zero of a difference, exactly two of the three distinct \(x\)-roots coalesce transversely. The short Weierstrass coefficients are homogeneous of degrees four and six, and the minimal smooth elliptic surface with this discriminant of degree twelve is rational. This proves the equivalence of conditions 1 and 2, including existence and reconstruction.

**2. Equivalence with the bielliptic locus.** Since the quadratics in a dependent triple span a basepoint-free pencil \(W\subset H^0(\mathbb P^1,\mathcal O(2))\), the associated map \(\phi:\mathbb P^1\to\mathbb P(W^*)\cong\mathbb P^1\) has degree two. Its deck involution exchanges the two roots of every member of \(W\), hence exchanges the three pairs of branch points. Conversely, if an involution of \(\mathbb P^1\) exchanges three pairs of the six branch points, conjugate it to \(t\mapsto-t\); each pair is the zero set of a quadratic in \(\langle X^2,Z^2\rangle\). These three quadratics are dependent. A fixed-point-free-on-the-branch involution of the hyperelliptic base lifts to an involution on \(Y_f\) whose quotient has genus one: in the even sextic coordinates one lift is \((t,y)\mapsto(-t,y)\), with two fixed points, and Riemann–Hurwitz gives quotient genus one. Conversely, a degree-two elliptic quotient provides this base involution and the three exchanged branch pairs. Thus conditions 2 and 3 are equivalent. The standard identification of this genus-two locus with the degree-two elliptic-subcover locus is reviewed in Shaska–Völklein, Sections 2–4.

**3. A reduced degree-fifteen coefficient equation.** Each \(\Delta_\pi\) is multilinear of degree one in each of the six root linear forms, so their product has degree fifteen in each root linear form. A transposition of two root labels fixes exactly three partitions (those pairing the transposed labels), where the determinant remains unchanged; it interchanges the remaining twelve partitions in six pairs, whose determinant-sign contributions cancel. Thus \(\mathcal B\) is symmetric in the six labelled roots. It descends from \((\mathbb P^1)^6\) to the symmetric product \(\operatorname{Sym}^6\mathbb P^1\cong\mathbb P^6\) as a global section of \(\mathcal O(15)\), hence a homogeneous polynomial of coefficient degree fifteen. Under \(g\in\operatorname{GL}_2\), it transforms by \(\det(g)^{45}\), consistent with the binary-sextic invariant weight. The polynomial is nonzero: for distinct affine roots \((0,1,2,3,5,7)\), all fifteen determinants are nonzero.

For any fixed pairing, the divisor \(\Delta_\pi=0\) in the ordered squarefree root space is irreducible: it is parametrized by a degree-two involution together with three distinct orbits of that involution. The fifteen such divisors are distinct and permuted transitively by \(S_6\). Their image in the unordered squarefree locus is therefore irreducible. They occur with multiplicity one, as is seen at the six roots \((1,-1,2,-2,3,-3)\): precisely one pairing determinant vanishes and its gradient in those six root coordinates is \((-5,-5,8,8,-3,-3)\), which is nonzero. No discriminant-boundary divisor divides \(\mathcal B\): at the sextic with affine root list \((1,1,2,3,5,8)\), the product is nonzero. Therefore \(\mathcal B\) itself, not merely its radical or a square, is an irreducible degree-fifteen polynomial up to a scalar.

**4. Birational moduli reconstruction.** Given a squarefree sextic and a pairing with vanishing determinant, the relation \(A+B+C=0\) is unique up to a common scalar. The displayed formulas then determine the unordered triple of quadratic roots of the Weierstrass cubic. Permuting that triple or multiplying all three forms by the same scalar gives an isomorphic elliptic surface. Conversely its three rational two-torsion sections give the same pairing. For a generic bielliptic genus-two curve the reduced automorphism group has just one nonidentity element (Shaska–Völklein, Theorem 1 and Section 3, generic \(V_4\) automorphism stratum), so there is only one admissible pairing. Both constructions respect base coordinate changes. Hence the map between the two two-dimensional coarse moduli spaces is birational.

**5. Generic transverse crossing along the two-pairing stratum.** Take ordered affine roots \((2,-2,1/2,-1/2,1,-1)\). Exactly two of the fifteen determinants vanish, corresponding to pairings \((12)(34)(56)\) and \((14)(23)(56)\). Their gradients in the six root coordinates have an exact two-by-two minor equal to \(9/8\), so are independent. Since the labelled-root map to the squarefree coefficient locus is étale, the local equation is a unit times the product of two transverse smooth equations. The family \(\{\pm1,\pm a,\pm a^{-1}\}\) is irreducible as \(a\) and the projective coordinate change vary. Being exactly two-branch and transverse is open along it; the exhibited point proves the asserted generic ordinary crossing.

## Verification

The included `verify.py` is self-contained Python 3 code using only the standard library. Executing `python3 verify.py` returned `CERTIFICATE_OK`. It generated all fifteen pairings and evaluated exact determinants, checked a nonzero generic sextic and an even sextic with exactly one vanishing determinant, verified permutation invariance on 120 reorderings, checked that a repeated-root witness does not force vanishing, and established the two vanishing determinants and independent gradients at the transverse-crossing witness. It also reconstructed the six-\(I_2\) Weierstrass cubic for \(f(t)=(t^2-1)(t^2-4)(t^2-9)\), checking its exact discriminant as a square. These are exact rational checks of illustrative witnesses; the statements for all sextics follow from the geometric arguments in the proof.

## Relationship to prior work

Ciliberto, Grassi, Miranda, Verra and Zanardini (arXiv:2602.11725v1, Sections 2.4 and 2.7, especially Remark 24 and Question 25) classify the six-\(I_2\) elliptic surfaces, give the quadratic-root Weierstrass form and ask for the equation of the resulting six-branch-point hypersurface and its genus-two moduli characterization. Their classification and parameter count are inputs, not contributions claimed here. Shaska and Völklein (arXiv:math/0107142, Sections 2–4) establish the classical elliptic-involution genus-two locus and its Igusa invariant equation; its existence is also not claimed as new. The present claim is the exact bridge, the root-pairing degree-fifteen reduced equation, the explicit inverse surface reconstruction, and the transverse two-pairing boundary geometry. The general Humbert-discriminant-four identification is classical.

## Limitations

The polynomial is given by an exact product over factorizations into linear forms rather than an expanded expression in seven coefficient variables. Its vanishing defines the reduced closure, not an asserted normalization or a complete singularity-scheme classification. The transversal-crossing statement applies to a generic specified four-dimensional stratum, not every point with extra automorphisms. The result is over \(\mathbb C\); no claim is made in characteristics two or three or about singular sextics. The strongest priority risk is that the classical Clebsch–Bolza equation and the 2026 quadratic-root classification may already be regarded as jointly implying the principal identification; the additional geometric reconstruction and local branch analysis are stated explicitly to delimit the claim.

## References

1. C. Ciliberto, A. Grassi, R. Miranda, A. Verra, A. Zanardini, *Rational elliptic surfaces with six singular double fibres*, arXiv:2602.11725v1 (first public 2026-02-12), Sections 2.4, 2.7 and Question 25. https://arxiv.org/abs/2602.11725
2. T. Shaska, H. Völklein, *Elliptic subfields and automorphisms of genus 2 function fields*, arXiv:math/0107142 (2001), Sections 2–4. https://arxiv.org/abs/math/0107142
3. T. Shaska, *Degrees of Genus-Two Split-Jacobian Loci and Humbert-Form Reconstruction*, arXiv:2608.16426 (2026). The available abstract discusses Humbert-locus equations but not the six-singular-fibre reconstruction; its full text was not accessible during this comparison. https://arxiv.org/abs/2608.16426
