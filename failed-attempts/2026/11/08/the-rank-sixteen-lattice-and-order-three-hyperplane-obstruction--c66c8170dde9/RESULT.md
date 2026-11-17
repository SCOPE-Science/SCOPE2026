# The rank-sixteen lattice and order-three hyperplane obstruction of Schur's twenty-four lines

## Finding
Let \(X\subset\mathbb P^3_{\mathbb C}\) be the smooth Schur quartic
\[
X=\{x_0^4-x_0x_1^3-x_2^4+x_2x_3^3=0\}.
\]
Number the twenty-four lines \(L_1,\ldots,L_{24}\) as in Table 3 of Naskręcki–Pokora [1], and let \(H=\mathcal O_X(1)\) be the hyperplane class. Define the *actual integral line lattice*
\[
M=\langle [L_1],\ldots,[L_{24}]\rangle_{\mathbb Z}
\subset\operatorname{NS}(X),
\]
with the intersection pairing inherited from the Néron–Severi lattice. Then \(M\) is a nondegenerate even lattice of rank \(16\) and signature \((1,15)\). Its discriminant group and absolute discriminant are
\[
M^\vee/M\cong (\mathbb Z/2\mathbb Z)^4\oplus
\mathbb Z/6\mathbb Z\oplus\mathbb Z/18\mathbb Z,
\qquad |\operatorname{disc}M|=1728.
\]
Although \(H\) belongs to the rational span of the twenty-four lines, it does not belong to \(M\). Its class in the saturation \((M\otimes\mathbb Q)\cap\operatorname{NS}(X)\), modulo \(M\), has **exact order three**. More concretely, with
\[
T=\{1,3,4,7,8,10,11,12,13,14,16,22\},
\]
the two complementary twelve-line effective divisors satisfy
\[
\sum_{i\in T}L_i\sim3H,
\qquad \sum_{i\notin T}L_i\sim3H.
\]
Here \(\sim\) denotes linear equivalence on \(X\). The integral conclusion is stronger than the previously established identity \(\sum_{i=1}^{24}L_i\sim6H\) [1].

## Assumptions and scope
The ground field is \(\mathbb C\), the twenty-four lines are the specific labeled half of the forty-eight second-kind lines in [1], and all divisor-class statements are integral. No assertion is made for an arbitrary abstract \((24_4,32_3)\) configuration or for an arbitrary quartic surface. The proof takes the existence, geometry, and precise triple-incidence table of these lines, together with \(\sum_iL_i\sim6H\), from [1], but computes the new lattice and hyperplane facts separately.

## Proof
**1. The intersection form.** As \(X\) is a smooth complex quartic K3 surface, adjunction gives \(L_i^2=-2\). For distinct lines, \(L_i\cdot L_j=1\) precisely when they meet and is zero otherwise. Proposition 3.5 and Table 3 of [1] prove that all intersections arise from thirty-two ordinary triple points; no pair occurs in two triples. Define the symmetric integral matrix \(G\) by
\[
G_{ii}=-2,\qquad
G_{ij}=\begin{cases}1&\text{if }i,j\text{ occur together in a Table 3 triple},\\0&\text{otherwise.}\end{cases}
\]
This is exactly the Gram matrix of the twenty-four divisor classes. Table 3 gives ninety-six unordered adjacent pairs, with each row of the adjacency matrix having sum eight. The complete thirty-two triples are encoded verbatim in `verify_schur_half_lattice.py`.

**2. Exact integral matrix calculation.** Exact polynomial arithmetic and Smith reduction of \(G\) yield
\[
\det(tI-G)=t^8(t-6)(t+2)^9(t+6)^6
\]
and nonzero Smith invariants
\[
\underbrace{1,\ldots,1}_{10},\;2,2,2,2,\;6,\;18.
\]
The arithmetic is reproducible without relying on any previous computation: the accompanying checker constructs \(G\) from all thirty-two labeled triples and performs the characteristic-polynomial, rank, and Smith calculations over the integers. Thus the real form has one positive eigenvalue, fifteen negative eigenvalues, and an eight-dimensional kernel; its rank is sixteen.

**3. Passing from a Gram matrix to the divisor lattice.** Write \(F=\mathbb Z^{24}\) for the free group on the labeled lines and \(p:F\to\operatorname{NS}(X)\) for the natural class map. By [1, Theorem 1.2(iii)] the sum of the twenty-four classes equals \(6H\); hence \(H\in p(F)\otimes\mathbb Q\). The Hodge index theorem therefore makes the intersection pairing nondegenerate on \(p(F)\otimes\mathbb Q\): a positive multiple of the ample class is in that space, and its perpendicular in that space is negative definite. Consequently, the rational kernels of \(G\) and \(p\) agree. The Néron–Severi group of a complex K3 surface is torsion-free, so they also have the same integral kernel.

It follows that \(M\cong F/\ker G\) as an integral lattice, that its rank is sixteen and that its signature is \((1,15)\). Since \(\ker G\subset F\) is primitive, choose a basis of \(F\) adapted to the kernel. In that basis \(G\) has a nonsingular block giving the form on \(M\) and an eight-dimensional zero block. Hence the torsion of \(\operatorname{coker}(G)\) is exactly \(M^\vee/M\). The displayed Smith invariants give the claimed discriminant group and its order \(2^4\cdot6\cdot18=1728\).

**4. Two complementary cubic sections.** Let \(u\in\mathbb Z^{24}\) be the indicator vector of the explicit set \(T\). Direct multiplication with the exact \(G\) gives
\[
Gu=3\mathbf1,\qquad G(\mathbf1-u)=3\mathbf1.
\]
For \(C=\sum_{i\in T}L_i\), this says \((C-3H)\cdot L_j=0\) for all \(j\), since \(H\cdot L_j=1\). But \(C-3H\) itself belongs to \(M\otimes\mathbb Q\), on which the form is nondegenerate by Step 3. Therefore \(C-3H=0\) in \(\operatorname{NS}(X)\otimes\mathbb Q\). Torsion-freeness upgrades equality to \(\operatorname{NS}(X)\), and \(\operatorname{Pic}(X)=\operatorname{NS}(X)\) for a K3 surface gives the asserted linear equivalence. The complementary divisor follows identically or by subtracting from the previously known \(6H\).

**5. A direct modular obstruction to \(H\in M\).** In the order of the twenty-four line labels, define
\[
w=(0,-1,2,4,-2,0,0,0,2,2,-4,2,0,0,-1,0,-1,-1,0,-3,0,0,2,2)^\mathsf T.
\]
Exact integer multiplication gives \(Gw\in9\mathbb Z^{24}\) and \(\sum_iw_i=3\). If \(H\) were an integer combination of the line classes, say \(H=\sum_i a_i L_i\) for integral \(a_i\), intersection with each \(L_j\) would force \(Ga=\mathbf1\). Then
\[
3=w^\mathsf T\mathbf1=w^\mathsf TGa=(Gw)^\mathsf Ta
\]
would be divisible by nine, a contradiction. Thus \(H\notin M\). Step 4 puts \(3H\) in \(M\), so the order of the hyperplane class modulo \(M\) is exactly three. This completes the proof.

## Verification
The accompanying `verify_schur_half_lattice.py` is a standalone exact-arithmetic checker requiring Python 3 and SymPy as specified in `requirements.txt`. Run `python verify_schur_half_lattice.py` in the extracted artifact directory. It reproduces all thirty-two input triples, the ninety-six adjacent pairs, the matrix characteristic polynomial, rank and Smith invariants; independently checks both cubic-section vectors and the modular nonmembership certificate; and checks the hyperplane order by an integral Hermite normal form computation. It does not assume any prior artifact or result.

The exact output on the stated inputs includes `SCHUR24_LATTICE_OK rank=16 signature=(1,15) discriminant=1728` and `SCHUR24_MOD9_NONMEMBERSHIP_CERTIFICATE_OK`. The infinite geometric conclusion rests on Steps 1, 3, 4, and 5, not merely on matrix output. This is a finite exact matrix certificate, not a statistical or finite-field extrapolation.

## Relationship to prior work
Naskręcki and Pokora [1] discovered and verified the precise twenty-four lines, their thirty-two triple points, their geometric equivalence to the other twenty-four-line half, and the complete divisor relation \(D\sim6H\). Those are inputs here, not claimed new. The new results concern the *integral lattice generated by this half*, its finite discriminant group, and the exact order-three obstruction for the hyperplane class, together with an explicit decomposition into two effective cubic sections.

Bauer and Schmitz [2, Remark 2.4] had earlier found **different** twenty lines spanning the complete Néron–Severi group, of rank twenty and discriminant \(-48\). This does not determine the rank-sixteen, discriminant-\(1728\) sublattice of the newly selected twenty-four lines. Höhn [3] identifies the \(D_4\)-root automorphism structure of the configuration, a strong combinatorial comparison. The available abstract does not state the present integral lattice invariant, but its full text could not be inspected and historical priority remains provisional. The known full sixty-four-line spectrum likewise does not by itself determine this particular subgroup's integral discriminant or hyperplane index.

## Limitations
The result does not assert that \(M\) is primitive in \(\operatorname{NS}(X)\); it only determines the order of the particular hyperplane class in its saturation quotient. It does not determine the entire primitive closure of \(M\), the complete orthogonal complement in \(\operatorname{NS}(X)\), or all possible twelve-line decompositions. The primary geometric incidence data are credited to [1]. A potentially relevant later preprint [3] could not be checked beyond its abstract, so independent historical-priority and mathematical reviews remain necessary.

## References
[1] Bartosz Naskręcki and Piotr Pokora, *A \(24_4,32_3\)-configuration on the Schur quartic with logarithmic Chern slope \(14/5\)*, arXiv:2607.07898v1 (first public 2026-07-08), Theorem 1.2, Proposition 3.5 and Appendix B, Table 3. https://arxiv.org/abs/2607.07898

[2] Thomas Bauer and David Schmitz, *Zariski chambers on surfaces of high Picard number*, LMS Journal of Computation and Mathematics 15 (2012), 219–230, Remark 2.4. DOI: 10.1112/S1461157012001040.

[3] Gerald Höhn, *Automorphisms of a \(24_4,32_3\)-configuration on the Schur quartic*, arXiv:2607.10090v1 (2026-07-11). https://arxiv.org/abs/2607.10090
