# The degree-151420 locus of quartic surfaces with a double plane conic

## Finding
Let \(k=\mathbb C\), let \(V\) be four-dimensional, and put \(\mathbb P^{34}=\mathbb P(\operatorname{Sym}^4 V^*)\). Define \(\mathcal D\) to be the Zariski closure of quartic forms \([F]\) for which there exists a smooth plane conic \(C\subset\mathbb P(V)\) with \(F\in H^0(\mathbb P(V),\mathcal I_C^2(4))\). Then \(\mathcal D\) is irreducible of dimension \(21\), has codimension \(13\) and projective degree
\[
\deg(\mathcal D)=151420.
\]
Equivalently, there are exactly \(151420\) quartic surfaces over \(\mathbb C\) that are singular along a (not prescribed) plane conic and pass through \(21\) sufficiently general points of \(\mathbb P^3\), counted with the usual intersection-theoretic multiplicities. The generic surface in \(\mathcal D\) is irreducible and has a unique smooth conic as the one-dimensional component of its singular locus.

## Assumptions and scope
All varieties and degrees are over \(\mathbb C\). The expression \(F\in\mathcal I_C^2(4)\) means ordinary squared ideal, which here is equivalent to first-order vanishing along the smooth conic. The closure includes degenerations with reducible or nonreduced conics. The degree refers to the reduced projective image, not to a projective bundle counted with a hypothetical extra mapping degree. General-point enumeration is interpreted as a transverse general linear section of the image variety.

## Proof
**1. The conic parameter space and incidence rank.** Write \(B=\mathbb P(V^*)\cong\mathbb P^3\), with tautological line bundle \(L=\mathcal O_B(-1)\) and rank-three quotient \(U=(V^*\otimes\mathcal O_B)/L\). The smooth projective parameter compactification of plane conics is
\[
T=\mathbb P_B(\operatorname{Sym}^2 U),\qquad\dim T=3+5=8,
\]
with tautological line \(R=\mathcal O_T(-1)\). Here projectivization parametrizes one-dimensional subspaces. For each \((\ell,Q)\in T\), the conic subscheme is the complete intersection \((\ell,Q)\), with \(Q\) a plane quadratic defined modulo \(\ell\). Even when \(Q\) is reducible or nonreduced, \(\ell,Q\) is a homogeneous regular sequence of degrees \(1,2\).

The degree-four part of the squared ideal \((\ell,Q)^2=(\ell^2,\ell Q,Q^2)\) has dimension \(10+4+1-1=14\): the only degree-four syzygy is \(Q\ell^2=\ell(\ell Q)\). Thus these spaces form a rank-\(14\) vector subbundle \(E\subset\operatorname{Sym}^4V^*\otimes\mathcal O_T\). The projective incidence bundle \(\mathbb P_T(E)\) has dimension \(8+13=21\), and its image is \(\mathcal D\). The smooth-conic locus is dense, hence the image closure is irreducible.

**2. The incidence map has generic degree one.** Outside the universal conic \(C\), the system \(H^0(\mathcal I_C^2(4))\) is base-point free: if \(\ell\ne0\), use \(\ell^2 A_2\); if \(\ell=0\) and \(Q\ne0\), use \(Q^2\). A general member is smooth away from \(C\) by Bertini. Its linear system is not composed with a pencil and contains no fixed divisor; Bertini irreducibility therefore gives an irreducible general member. Along \(C\), every partial derivative of \(F\) vanishes. Hence the reduced positive-dimensional singular support of the general member is exactly \(C\), uniquely recovering it. Therefore \(\mathbb P_T(E)\to\mathcal D\) is generically one-to-one, and \(\deg\mathcal D\) equals the top self-intersection of the pulled-back ambient hyperplane class. The divisors of quartic forms vanishing at a point of \(\mathbb P^3\) form a base-point-free family on \(\mathcal D\): for each nonzero form there is a point at which it does not vanish. Successive Bertini applied to \(21\) general such evaluation divisors therefore gives a proper, generically transverse zero-dimensional section of degree \(\deg\mathcal D\), justifying the general-point count.

**3. The Chern and Segre classes.** Put \(h=c_1(L^*)\) and \(k=c_1(R^*)\) on \(T\). The generators \(\ell^2\operatorname{Sym}^2V^*\), \(\ell Q V^*\) and \(Q^2\), together with the single syzygy \(Q\ell^2=\ell(\ell Q)\), give the following class in \(K^0(T)\):
\[
[E]=[L^{\otimes2}\otimes\operatorname{Sym}^2V^*]+[L\otimes R\otimes V^*]+[R^{\otimes2}]-[L^{\otimes2}\otimes R].
\]
The identity is independent of a choice of lift of \(Q\), since changing \(Q\) by \(\ell\) times a linear form gives upper-triangular changes of generators. It follows that
\[
c(E)=\frac{(1-2h)^{10}(1-h-k)^4(1-2k)}{1-2h-k},\qquad
s(E)=\frac{1-2h-k}{(1-2h)^{10}(1-h-k)^4(1-2k)}.
\]
The pushforward formula for the projective bundle of lines gives
\[
\deg\mathcal D=\int_{\mathbb P_T(E)}\!c_1(\mathcal O_{\mathbb P(E)}(1))^{21}=\int_T s_8(E).
\]

**4. Evaluation on the conic base.** The exact sequence \(0\to L\otimes V^*\to\operatorname{Sym}^2 V^*\otimes\mathcal O_B\to\operatorname{Sym}^2 U\to0\) implies
\[
s(\operatorname{Sym}^2 U)=(1-h)^4.
\]
Writing \(\pi:T\to B\), the projective-bundle pushforward is
\[
\pi_*(k^{5+j})=(-1)^j\binom4j h^j\quad(0\le j\le3).
\]
Truncating the displayed rational series \(s(E)\) in total degree eight gives the four terms capable of contributing to the integral:
\[
[s_8(E)]_{k\ge5}=579040h^3k^5+139412h^2k^6+22992hk^7+1981k^8.
\]
Hence
\[
\deg\mathcal D=579040-4(139412)+6(22992)-4(1981)=151420.
\]
This is an exact intersection-theoretic count. As the incidence map is generically birational, no divisibility correction is required.

## Verification
Run `python3 verify_degree.py` using Python 3.9 or later; no external packages are needed. The program computes the four Segre coefficients by truncated polynomial arithmetic and independently applies equivariant torus localization at the \(24\) fixed points of \(T\) for the weights \((0,1,7,23)\). At a fixed conic \((\ell,Q)\) it constructs directly the \(14\) quartic monomials in \((\ell,Q)^2\) and sums the exact rational localization contributions. Both calculations return \(151420\), ending with `ALL_CHECKS_PASSED`. The code checks the numerical intersection, whereas the geometric proof above establishes generic degree one and applies Bertini; the computation alone would not prove those assertions.

## Relationship to prior work
The geometry of irreducible quartic surfaces with a double conic is classical, as is the identification of this family among nonnormal quartic surfaces. Slavov studies the parameter spaces of hypersurfaces with positive-dimensional singular locus and distinguishes the linear and quadric-support components, but does not state the enumerative degree calculated here. Ducat's modern survey (following Urabe and Jessop) describes the double-conic quartics by their equation \(Q^2+\ell Q A_1+\ell^2 B_2\), yet does not compute the projective degree of their parameter-space component. Carmeli–Radzivilovsky compute enumerative degrees for surfaces double along **lines**, which are a different incidence base (a Grassmannian), not for conics. Kazarian–Kerner–Némethi study the discriminant of transverse singularity type along a fixed singular support, not the degree of the locus obtained by allowing the supporting conic to vary.

## Limitations
The exact degree is not a statement about the degrees of other components of the positive-dimensional-singular-locus space, or the scheme-theoretic multiplicity of its defining determinantal ideals. Genericity of the \(21\) point constraints is essential. Historical priority remains provisional: unindexed classical enumerative treatments of double-conic quartics might contain the same number, and no claim of independent external validation is made.

## References
- K. Slavov, *The moduli space of hypersurfaces whose singular locus has high dimension*, arXiv:1208.1118, first posted 2012-08-06; full text https://arxiv.org/html/1208.1118v2.
- T. Ducat, *Quartic surfaces up to volume preserving equivalence*, Selecta Mathematica 30 (2024), article 2; first posted as open-access article 2023-11-14, https://doi.org/10.1007/s00029-023-00890-7 (especially Proposition 3.3 and section 5.5).
- S. Carmeli and L. Radzivilovsky, *Counting surfaces singular along a line in* \(\mathbb P^3\), arXiv:1812.02413, https://arxiv.org/html/1812.02413v3.
- M. Kazarian, D. Kerner and A. Némethi, *Discriminant of the ordinary transversal singularity type. The global equivalence class*, arXiv:1308.6045, https://arxiv.org/abs/1308.6045.
