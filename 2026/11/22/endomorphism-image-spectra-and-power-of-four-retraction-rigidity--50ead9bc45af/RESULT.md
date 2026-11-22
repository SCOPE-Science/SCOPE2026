# Endomorphism image spectra and power-of-four retraction rigidity in exponent-four core quandles

## Finding
For each integer \(r\geq1\), let \(Q_r\) be the Takasaki (core) quandle of the additive group \((\mathbb Z/4\mathbb Z)^r\), with \(x\triangleright y=2y-x\). The following formulas determine, simultaneously, the number of **all** quandle endomorphisms with each image cardinality and the number of **idempotent** quandle endomorphisms with each image cardinality.

Put \(V=\mathbb F_2^r\), and for \(0\leq k\leq r\) define
\[
G_{r,k}=\prod_{i=0}^{k-1}\frac{2^r-2^i}{2^k-2^i},\quad
N_{r,k}=G_{r,k}\prod_{i=0}^{k-1}(2^r-2^i),\quad B_k=2^k,\quad C_k=2^{r-k}.
\]
Empty products are one. Let \(S(n,t)\) denote the Stirling number of the second kind, and \((a)_t=a(a-1)\cdots(a-t+1)\) the falling factorial. Define
\[
F_{r,k}(z)=2^{kC_k}\sum_{t=1}^{C_k}(C_k)_t S(C_k,t)z^{B_k t}.
\]
The endomorphism image-size polynomial is exactly
\[
\boxed{E_r(z)=2^r\sum_{k=0}^{r}N_{r,k}F_{r,k}(z)^{B_k}.}
\]
The idempotent-endomorphism, or retraction, image-size polynomial is exactly
\[
\boxed{I_r(z)=\sum_{k=0}^{r}G_{r,k}\,2^{k(r-k)+(r-k)+k2^r+(r-2k)2^k}\,z^{4^k}.}
\]
Every exponent in this last integer power of two is understood as the complete sum; the total is nonnegative. In particular, every embedded quandle retract has cardinality \(4^k\) for a unique \(0\leq k\leq r\), and is isomorphic to \(Q_k\) (where \(Q_0\) is the one-element quandle). Conversely, all such cardinalities occur.

For \(r=2\), the complete polynomials are
\[
E_2(z)=16z+336z^2+576z^3+2400z^4+4608z^6+2304z^8+6144z^{16}
\]
and
\[
I_2(z)=16z+192z^4+z^{16}.
\]
Thus the quandle admits endomorphism images of cardinalities \(2,3,6,8\) but none of these cardinalities admits a retraction image.

## Assumptions and scope
The parameter \(r\) is any positive integer; all arithmetic in \(V\) is binary. Write each element of \(Q_r\) uniquely as \((p,u)\in V\times V\), meaning the vector \(p+2u\) modulo four, where the bits of \(p\) are chosen from \(\{0,1\}\). In these coordinates,
\[
(p,u)\triangleright(q,v)=(p,u+p+q).
\]
The image-size polynomials sum over distinct functions, not over isomorphism classes or conjugacy orbits. Idempotence means equality of functions \(f\circ f=f\).

## Proof
**Normal form.** Every quandle endomorphism, uniquely, has the form
\[
f_{L,c,b}(p,u)=(Lp+c,Lu+b_p),
\]
where \(L:V\to V\) is an arbitrary binary linear map, \(c\in V\), and \(b=(b_p)_{p\in V}\) is an arbitrary function \(V\to V\). To prove necessity, write \(f(p,u)=(a(p,u),h(p,u))\). Preservation of \(\triangleright\) and the displayed multiplication shows that \(a(p,u+p+q)=a(p,u)\) for all \(p,u,q\), so the first coordinate depends only on \(p\). It also gives
\[
h(p,u+t)+h(p,u)=a(p)+a(p+t)\quad(t\in V).
\]
At \(p=0\), increments of \(h(0,\cdot)\) show that the map \(L(t)=a(t)+a(0)\) is linear. Therefore \(a(p)=Lp+c\) for \(c=a(0)\), and the same equation forces \(h(p,u)=Lu+b_p\). Conversely, direct substitution establishes the quandle identity for every such triple. Uniqueness follows from evaluation at \(u=0\) and the first-coordinate map.

**All image sizes.** Fix a linear map \(L\) of rank \(k\). For each of the \(B_k\) possible output first coordinates \(Lp+c\), the input first coordinates \(p\) form a fiber of cardinality \(C_k\). The second-coordinate images from each such input fiber are cosets \(b_p+\operatorname{im}L\), each of size \(B_k\). If exactly \(t\) different cosets occur, this output first-coordinate fiber contributes \(B_k t\) image points. There are \((C_k)_tS(C_k,t)\) assignments of the \(C_k\) source labels onto exactly \(t\) different quotient cosets in \(V/\operatorname{im}L\), and \(B_k^{C_k}=2^{kC_k}\) independent choices of lifts \(b_p\). These possibilities are independent across the \(B_k\) output first-coordinate fibers, yielding \(F_{r,k}(z)^{B_k}\). The number of rank-\(k\) maps \(L\) is \(N_{r,k}\), and \(c\) has \(2^r\) choices. This proves the formula for \(E_r\). At \(z=1\), it also verifies the total \(E_r(1)=2^{r^2+r+r2^r}\), independently obtained by counting normal-form triples.

**Idempotent endomorphisms.** The equation \(f_{L,c,b}^2=f_{L,c,b}\) is equivalent to
\[
L^2=L,\qquad Lc=0,\qquad b_{Lp+c}=(I+L)b_p\quad\text{for every }p\in V.
\]
For a projection \(L\) of rank \(k\), write \(U=\operatorname{im}L\), \(K=\ker L\), so \(V=U\oplus K\), and \(I+L\) projects onto \(K\). For each \(x\in U\), the distinguished source label \(p_0=x+c\) satisfies \(Lp_0=x\). Its value \(b_{p_0}\) must belong to \(K\) and has \(2^{r-k}\) choices. For the remaining \(C_k-1\) labels in this same fiber, the \(K\)-component of \(b_p\) is fixed as \(b_{p_0}\), while the \(U\)-component may be chosen in \(2^k\) ways. Hence the \(b\)-count per fiber is \(2^{r-k+k(C_k-1)}\), and across all \(B_k\) fibers is
\[
2^{k2^r+(r-2k)2^k}.
\]
There are \(G_{r,k}\) possible images \(U\) and \(2^{k(r-k)}\) complementary kernels \(K\), hence this many rank-\(k\) projections \(L\). For each, \(c\in K\) has \(2^{r-k}\) choices. Multiplication yields the coefficient in \(I_r(z)\).

For each such idempotent, its image over each of the \(B_k\) output first coordinates is exactly a single full coset of \(U\) in the second coordinate, hence has \(B_k\) elements. The total image has \(B_k^2=4^k\) elements. Re-indexing its first coordinates by \(x\in U\) and its second coordinates by their offsets in \(U\) identifies this image with \(Q_k\). Nonzero coefficients in the formula show existence at every \(k\). This finishes the proof.

## Verification
The included standalone `checker.py` performs direct quandle multiplication for all \(16\) endomorphisms at \(r=1\) and all \(16{,}384\) normal-form endomorphisms at \(r=2\), checking the polynomial image-size coefficients and idempotent image sizes. It also enumerates every one of the \(256\) set maps on the four-point quandle and confirms that precisely \(16\) preserve the operation. The symbolic \(r=3\) polynomial evaluation gives \(E_3(1)=68{,}719{,}476{,}736\) and \(I_3(z)=64z+114688z^4+229376z^{16}+z^{64}\). These are finite corroborations; the parameter-uniform proof above is the basis of the result. Run with `python3 checker.py` under standard Python 3.

## Relationship to prior work
Elhamdadi, MacQuarrie and Restrepo establish the affine description of automorphisms of a single dihedral quandle; this is a proper bijective subcase and does not count the noninvertible image-size fibers. Bardakov, Dey and Singh establish Takasaki automorphisms for groups without two-torsion and other fixed-point-free Alexander actions; their hypothesis excludes the present exponent-four groups. Earlier work on affine symmetries of even dihedral powers identifies the invertible stratum in this same family. Singh proves residual finiteness of endomorphism monoids for finitely generated residually finite quandles, but that structural theorem does not enumerate finite endomorphisms by image size. Related work on semisimple Alexander-quandle retractions assumes a semisimple prime-field module action and does not cover the operator \(-I\) over exponent-four groups, where the displacement \(2I\) is noninvertible. The present image and retraction enumerators concern singular maps and the possible images of idempotents.

## Limitations
This result concerns the fixed family \(Q_r\), not arbitrary finite abelian groups or arbitrary Alexander quandles. It counts endomorphism functions and their image cardinalities, not automorphism-conjugacy classes of endomorphisms. It does not classify all subquandles; many subquandles are not retract images. Historical-priority uncertainty remains, particularly possible unindexed descriptions of singular homomorphisms for nonconnected Alexander quandles. No independent external mathematical audit has been performed.

## References
- M. Elhamdadi, J. MacQuarrie, R. Restrepo, *Automorphism groups of Quandles*, arXiv:1012.5291, first public version 2010-12-23, https://arxiv.org/abs/1012.5291 .
- V. G. Bardakov, P. Dey, M. Singh, *Automorphism groups of quandles arising from groups*, arXiv:1608.05178, first public version 2016-08-18, https://arxiv.org/abs/1608.05178 .
- M. Singh, *Endomorphism monoid and automorphism group of residually finite and profinite quandles*, arXiv:2311.03708, first public version 2023-11-07, https://arxiv.org/abs/2311.03708 .
- *Automorphisms and inner symmetries of 4-torsion Takasaki quandles*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-automorphisms-and-inner-symmetries-of-4-torsion-takasaki-quandle--849a303ddc25 .
- *Semisimple Alexander-quandle retractions: a transformation–affine factorization and exact image ranks*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-semisimple-alexander-quandle-retractions-a-transformation-affine--117335b68a3e .
