# Frobenius descent and rational-node profiles of the sixty Göpel tetrads

## Finding

Let \(k=\mathbb F_q\) have odd characteristic and let \(C/k\) be any smooth genus-two curve. On the singular quartic Kummer surface of its Jacobian, let \(\mathcal G\) be the finite étale set of the 60 geometric Göpel tetrads: unordered four-node sets for which no three nodes lie on a trope. Let \(\lambda\) be the partition of six given by Frobenius acting on the geometric Weierstrass points of \(C\). The Frobenius cycle profile of \(\mathcal G\), and the number of individually \(k\)-rational nodes inside each Frobenius-invariant tetrad, depend only on \(\lambda\) and are exactly:

| Frobenius type on the six branch points | Göpel-tetrad cycle profile | Rational-node distribution among rational tetrads |
|---|---|---|
| \(1^6\) | \(1^{60}\) | 60 with 4 |
| \(2,1^4\) | \(1^{12}2^{24}\) | 6 with 0; 6 with 4 |
| \(3,1^3\) | \(3^{20}\) | none |
| \(2^2,1^2\) | \(1^8 2^{26}\) | 3 with 0; 4 with 2; 1 with 4 |
| \(4,1^2\) | \(1^2 2^3 4^{13}\) | 1 with 0; 1 with 2 |
| \(3,2,1\) | \(3^4 6^8\) | none |
| \(5,1\) | \(5^{12}\) | none |
| \(2^3\) | \(1^{16} 2^{22}\) | 3 with 0; 12 with 2; 1 with 4 |
| \(4,2\) | \(1^2 2^3 4^{13}\) | 1 with 0; 1 with 2 |
| \(3^2\) | \(1^3 3^{19}\) | 3 with 1 |
| \(6\) | \(1^1 2^1 3^5 6^7\) | 1 with 1 |

Here \(1^{12}2^{24}\), for example, denotes twelve fixed tetrads and twenty-four two-cycles, not a count of rational points. In the right column, 'with \(r\)' means that precisely \(r\) of the tetrad's four constituent nodes are \(k\)-rational. Thus a tetrad rational *as an unordered set* need not contain any rational node. In type \((2,1^4)\), precisely six of the twelve rational tetrads have no rational node. In type \((3^2)\), all three rational tetrads have exactly one rational node.

If the cycle profile is \(\prod_d d^{c_d}\), then the associated zero-dimensional finite étale scheme has
\[
Z(\mathcal G/k,T)=\prod_d(1-T^d)^{-c_d},\qquad
\#\mathcal G(\mathbb F_{q^m})=\sum_{d\mid m}d\,c_d\quad(m\geq1).
\]
The least degree of an extension splitting all Göpel tetrads is the order of the six-point Frobenius permutation (the least common multiple of the parts of \(\lambda\)).

## Assumptions and scope

The field has odd characteristic; no ordinarity, genericity, or restriction on the Jacobian endomorphism algebra is assumed. The curve and its principally polarized Jacobian are defined over \(k\). In characteristic different from two, the 16 nodes of its singular Kummer quartic are the 16 geometric two-torsion points \(J(C)[2](\bar k)\), and the 16 tropes form the classical \((16_6)\) incidence structure. The Göpel tetrads constitute a canonical Galois-stable finite set; we do **not** assert any descent of a corresponding Cremona transformation as a rational map over \(k\).

## Proof

**1. Galois model of the nodes.** Write the geometric Weierstrass points as \(B=\{1,\ldots,6\}\). The classical hyperelliptic two-division description gives
\[
V=\{A\subseteq B:|A|\equiv0\pmod2\}/(A\sim B\setminus A)
\cong J(C)[2](\bar k)\cong\mathbb F_2^4.
\]
Addition is symmetric difference modulo complement; the Weil symplectic pairing is \(\langle A,D\rangle=|A\cap D|\bmod2\). This is well-defined because all sets in the model are even. Every class has a unique representative of size zero or two, giving the identity and fifteen two-element classes. Galois permutes the six labels and therefore acts through the corresponding element \(\sigma\in S_6\cong\operatorname{Sp}_4(\mathbb F_2)\).

**2. Intrinsic description of the tetrads.** A Göpel tetrad is exactly an affine translate \(a+W\) of a totally isotropic two-dimensional subspace \(W\subset V\). There are fifteen such subspaces: for each nonzero \(u\in V\), there are six choices of \(v\in u^\perp\setminus\langle u\rangle\), and six ordered bases per plane, so \(15\cdot6/6=15\). Each has four distinct cosets; hence there are exactly 60. The classical characterization as four nodes with no triple on a trope agrees with this description (Dolgachev–Keum and Kumar). It is unaffected by special genus-two moduli, since this finite incidence structure is determined by \(J(C)[2]\) and the principal polarization.

**3. Frobenius and rational nodes.** Frobenius sends \(a+W\) to \(\sigma(a)+\sigma(W)\). A tetrad is \(k\)-rational as an unordered set precisely when \(\sigma(W)=W\) and \(\sigma(a)+a\in W\). For a fixed isotropic \(W\), the number of fixed cosets is
\[
\#(V/W)^\sigma=2^{\dim_{\mathbb F_2}(V/W)^\sigma}.
\]
If such a coset contains one \(\sigma\)-fixed node \(a\), then all fixed nodes in it form \(a+W^\sigma\) and their count is \(2^{\dim W^\sigma}\). If it contains none, the count is zero. This proves that the node distribution in the table is exhaustive and that its possible positive values are \(1,2,4\).

**4. The eleven conjugacy types.** There are eleven partitions of six and every permutation with the same partition is conjugate. For each representative, act on all 16 even-subset/complement classes, on the 15 totally isotropic planes, and on their 60 cosets, then enumerate cycles. The exhaustive standalone verifier constructs all sets directly and checks *every one of the 720 permutations*, proving the eleven profiles in the table rather than relying on sampled fields. It additionally constructs the 16 classical six-node trope sets independently and verifies that exactly those 60 four-node subsets with no three collinear-on-a-trope are the affine isotropic planes. As a hand check, a transposition fixes exactly three perfect matchings of the six labels, hence three isotropic planes; each has four fixed cosets, giving twelve fixed tetrads. Exactly six of those have all four nodes fixed and six have none.

**5. Zeta and splitting extension.** A Frobenius orbit of length \(d\) contributes \((1-T^d)^{-1}\) and exactly \(d\) rational points over \(\mathbb F_{q^m}\) iff \(d\mid m\). The table has least common multiple of orbit lengths equal to the order of \(\sigma\) for each of the eleven rows; this yields the asserted minimal splitting extension degree.

## Verification

Run `python3 gopel_verify.py` using Python 3 and only the standard library. The script constructs all 16 group elements and checks the symplectic relation, enumerates all fifteen isotropic planes and sixty cosets, reconstructs the sixteen trope node sets as an independent incidence test, and computes the complete orbit and rational-node tables for every permutation in \(S_6\). It asserts 60 distinct four-element tetrads and all orbit-degree totals. Successful execution prints `GOPEL_FROBENIUS_720_PERMUTATIONS_VERIFIED_OK`. This finite exhaustive calculation verifies the 720-element permutation reduction; the mathematical proof in Steps 1–3 justifies why that finite reduction covers **every** smooth genus-two curve over **every** odd finite field, not only the finite fields tested.

## Relationship to prior work

Dolgachev–Keum (2001 preprint, Section 4) already give the six-Weierstrass-point model of two-torsion and identify the classical sixty affine isotropic Göpel tetrads. Kumar (2011 preprint, Sections 2–3) establishes the sixteen-node, sixteen-trope geometry and the sixty Cremona-associated tetrads. Dolgachev (2024, Section 5) restates the odd-characteristic isotropic-plane model. None of these geometric identifications is claimed as new. The claim here is the complete eleven-type *arithmetic* Frobenius spectrum, its refinement by rational vertices of invariant tetrads, the rational point counts of the 60-point scheme over all extensions, and the splitting-degree classification.

A published arithmetic spectrum for sixty incidence flags on the trace Segre cubic concerns a **different** \(S_6\)-set: a transposition fixes no Segre node–plane flags but fixes twelve Göpel tetrads, so that existing 60-object table cannot be transferred by an equivariant identification. A published integral Göpel-tetrad lattice calculation concerns a lattice cokernel, not Frobenius descent. Searches did not establish exhaustive historical priority; see limitations.

## Limitations

Historical originality is provisional: obscure tables of classical finite configurations or further arithmetical consequences of the established symplectic action might overlap. The explicit arithmetic spectrum is a finite permutation-theoretic refinement of a known underlying action, not a new geometric construction. The table classifies conditionally on the Weierstrass Frobenius partition; it neither counts curves realizing each type over a fixed field nor classifies all rational Kummer automorphisms. Characteristic two is excluded, as the ordinary sixteen-node and symplectic two-torsion model changes. No independent audit has been conducted.

## References

1. I. Dolgachev and J. Keum, *Birational automorphisms of quartic Hessian surfaces*, arXiv:math/0103186v1 (public 2001-03-27), Section 4. https://arxiv.org/abs/math/0103186
2. A. Kumar, *Elliptic fibrations on a generic Jacobian Kummer surface*, arXiv:1105.1715 (public 2011-05-09), Sections 2–3. https://arxiv.org/abs/1105.1715
3. I. Dolgachev, *K3 surfaces of Kummer type in characteristic two*, *Bull. London Math. Soc.* 56 (2024), Section 5, https://doi.org/10.1112/blms.13033 (odd-characteristic comparisons).
