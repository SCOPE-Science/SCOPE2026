# Sharp-pair rigidity for even-signed permutation actions and the exceptional fourth rank

## Finding
For \(d\ge3\), let \(G_d=W(D_d)\) consist of all signed permutation matrices with an even number of negative signs. This is *even-sign parity*, not a restriction on permutation parity. Put
\[
M_d(u,v)=\max_{g\in G_d}\langle gu,v\rangle,\qquad
\mu_d=\min_{u,v\in S^{d-1}}M_d(u,v).
\]
The exact values are \(\mu_3=1/3\) and \(\mu_d=d^{-1/2}\) for \(d\ge4\). More importantly, **every** minimizing ordered pair \((u,v)\) belongs to exactly the following kinds, where 'flat' means that every coordinate has modulus \(d^{-1/2}\), 'axis' means a signed standard basis vector, and 'opposite product parity' means \(\prod_i u_i\prod_i v_i<0\):

* \(d=3\): flat--flat with opposite product parity;
* \(d=4\): axis--flat, flat--axis, or flat--flat with opposite product parity;
* \(d\ge5\): axis--flat or flat--axis, and no others.

For the real Hilbert space \(\mathbb R^d\), represent each norm-one rank-one operator as \(T x=\langle x,v\rangle u\) with \(u,v\in S^{d-1}\). Then
\[
\min_{\operatorname{rank}T=1,\,\|T\|=1}\max_{g\in G_d}\|I+gT\|
=\frac{1+\sqrt{5+4\mu_d}}2.
\]
The minimizing rank-one operators are precisely those arising from the pair classification above. The value formula also follows from established spherical-design bounds and rank-one norm algebra; the global equality classification is the additional assertion.

## Assumptions and scope
All vector spaces and operators are real; the Euclidean inner product and induced operator norm are used. The integers range over \(d\ge3\). Every minimum is over both ordered unit vectors, not over one fixed orbit. A signed permutation is admitted exactly when the product of its coordinate signs is \(+1\), regardless of the permutation's sign. All statements concern the canonical reflection representation of \(W(D_d)\); no analogous result is claimed for arbitrary orthogonal representations or Banach norms.

## Proof
**Orbit moments.** Fix unit \(u,v\), let \(g\) be uniformly distributed over \(G_d\), and write \(X=\langle gu,v\rangle\). Coordinate permutation averaging and even-sign averaging imply \(\mathbb EX=0\) and \(\mathbb EX^2=1/d\) for every \(d\ge3\). For \(d\ge4\), \(\mathbb EX^3=0\) as well: on the even-sign subgroup each nonempty sign character supported on fewer than \(d\) coordinates has average zero, and every odd-degree monomial of degree at most three contains such a character.

**Sharp lower bounds.** Write \(b=\max_g\langle gu,v\rangle\), which is positive by the first two moments. For \(d\ge4\), the nonnegative polynomial \((b-X)(X+d^{-1/2})^2\), together with the three moment identities, gives
\[
0\le\mathbb E[(b-X)(X+d^{-1/2})^2]
=2d^{-1}(b-d^{-1/2}).
\]
Thus \(b\ge d^{-1/2}\). For \(d=3\), use \(-1\le X\le b\) and the nonnegative polynomial \((b-X)(1+X)\):
\[
0\le\mathbb E[(b-X)(1+X)]=b-1/3.
\]
For \(d\ge4\), an axis vector and a flat vector give \(b=d^{-1/2}\), since the axis orbit is all signed coordinate vectors. For \(d=3\), take flat \(u\) and \(v=-u\): the orbit of \(u\) comprises the four even-parity signs, giving \(b=1/3\).

**Equality rigidity in dimensions at least four.** If \(b=d^{-1/2}=h\), equality in the nonnegative expectation forces \(X\in\{-h,h\}\) for *every* group element. Fix a permutation \(\pi\) and abbreviate \(a_i=u_{\pi(i)}v_i\). Consequently
\[
\left(\sum_{i=1}^{d}\varepsilon_i a_i\right)^2=h^2
\quad\text{for all }\varepsilon_i\in\{-1,1\}
\text{ with }\prod_i\varepsilon_i=1.
\]
When \(d\ge5\), the Walsh characters \(\varepsilon_i\varepsilon_j\), for \(i<j\), are mutually distinct nonconstant characters on the even-sign group. Fourier uniqueness therefore forces \(a_i a_j=0\) for all distinct \(i,j\). If both \(u\) and \(v\) had at least two nonzero coordinates, a permutation could align two of them, contradicting this. Hence one vector is axis. Since the orbit of an axis is all signed axes, equality then forces the other vector to be flat. Conversely these pairs attain the bound.

For \(d=4\), complementary pairs give the same Walsh character; Fourier uniqueness instead yields the three identities
\[
a_1a_2+a_3a_4=a_1a_3+a_2a_4=a_1a_4+a_2a_3=0.
\]
For any fixed permutation, these equations exclude precisely two or three nonzero \(a_i\): with fewer than four nonzero entries, they permit at most one. Thus if neither vector is axis, a permutation aligning two nonzero coordinates forces both vectors to have full support. With all four products nonzero, the three identities imply that \(|a_1|=|a_2|=|a_3|=|a_4|\). Repeating after arbitrary coordinate permutations forces both \(u\) and \(v\) to have constant coordinate modulus \(1/2\). The equations then reduce to the condition that \(\prod_i a_i<0\), equivalently that \(u\) and \(v\) have opposite product parity. Conversely, for flat vectors of opposite product parity, every even sign-permutation gives an odd number of negative coordinate products, so each inner product is either \(+1/2\) or \(-1/2\). Axis--flat and flat--axis also attain the value. This exhausts the cases.

**Equality in dimension three.** At \(b=1/3\), equality in \(\mathbb E[(b-X)(1+X)]\ge0\) forces every orbit pairing to be either \(-1\) or \(1/3\). Since the first two moments are \(0\) and \(1/3\), the value \(-1\) occurs, so \(v=-g_0u\) for some \(g_0\). Translating by the group then shows that any distinct orbit vectors have inner product \(-1/3\). Their Gram matrix and zero barycenter force an orbit of exactly four points, forming a regular tetrahedron. Within the even-signed permutation action in dimension three, an orbit has four points only when all coordinates of \(u\) have equal modulus: otherwise permutations and sign variations give at least six distinct points. Thus \(u\) is flat; since \(v\) is the negative of an orbit point, \(v\) is flat with opposite product parity. Conversely these pairs yield the tetrahedral equality described above.

**Rank-one norm correspondence.** For unit vectors \(a,v\) with \(c=\langle a,v\rangle\), the trace and determinant of \((I+a\otimes v)^*(I+a\otimes v)\) on \(\operatorname{span}\{a,v\}\) are \(3+2c\) and \((1+c)^2\), respectively. The remaining singular values are one, if any. Hence \(\|I+a\otimes v\|=(1+\sqrt{5+4c})/2\), a strictly increasing function of \(c\in[-1,1]\). The classified minimizing pairs therefore give all minimizing rank-one operators and the asserted constant.

## Verification
The lower bounds are infinite-dimensional quantifier-free finite-group arguments valid for *every* prescribed integer dimension; they do not rely on numerical extrapolation. Direct exhaustive sign-and-permutation checks at \(d=3,4,5\) give respectively \(1/3,1/2,1/\sqrt5\) on the explicitly described pairs. The standalone `check.py` tests these normalizations and the rank-one singular-value formula. The finite tests are diagnostics, not a substitute for Walsh character orthogonality and the equality arguments.

## Relationship to prior work
Dantas, del Río and Raunig (arXiv:2606.20429, first public 2026-06-18, primary MSC 46B04) introduced the group Daugavet equation and proved a qualitative Hilbert-space transitivity characterization; they did not classify the type-\(D\) worst-case rank-one pairs. Boyvalenkov and Stoyanova (arXiv:2007.05599) describe the classical Fazekas--Levenshtein covering-radius bound for spherical designs; their general inequality already explains the numerical lower bound \(1/\sqrt d\) for the type-\(D\) orbits of strength three. The separate new content here is the *complete equality set* in all dimensions, particularly the additional flat--flat equality orbit confined to dimension four. General rank-one norm reductions are likewise standard and are not claimed as a new universal principle.

## Limitations
The statement is for the standard real type-\(D\) signed-permutation representation and the infimum over both unit input and output vectors. It does not determine the complete optimizers for other Weyl groups, infinite group actions, or non-Hilbert Banach norms. The broad design inequality and some special contact faces of spin-weight polytopes predate this result; further literature could conceivably contain an equivalent complete equality classification. No independent mathematical validation has been performed.

## References
1. S. Dantas, H. del Río, T. Raunig, *A group action approach to the Daugavet property*, arXiv:2606.20429 (initial public submission 2026-06-18), especially Sections 2, 3 and 5.
2. P. Boyvalenkov and M. Stoyanova, *Linear programming bounds for covering radius of spherical designs*, arXiv:2007.05599, especially Definition 1.3 and the cited Fazekas--Levenshtein bound for odd-strength designs.
3. J. Delsarte, J.-M. Goethals and J. J. Seidel, *Spherical codes and designs*, Geom. Dedicata 6 (1977), 363–388 (background on spherical designs).
