# The 393 Zariski chambers of a quartic del Pezzo surface separate all eighteen Frobenius types

## Finding
Let \(X\) be any smooth degree-four del Pezzo surface over a finite field \(\mathbb F_q\), of arbitrary prime-power order. The set \(\mathcal Z_X\) of its geometric Zariski chambers (including the nef chamber) has \(393\) elements and is Galois-stable. Endow it with its canonical finite etale scheme structure over \(\mathbb F_q\), determined by the Frobenius permutation of this finite set. Then the full zeta function \(Z_{\mathcal Z_X}(T)\) **uniquely determines the conjugacy class of geometric Frobenius in \(W(D_5)\)**. Equivalently, the permutation action on the \(393\) chambers distinguishes all \(18\) Weyl conjugacy classes; their complete distinct cycle types are listed in `spectra.csv`.

There are exactly \(10\) possible base-field chamber counts, namely \(1,3,5,7,11,21,27,33,107,393\). By contrast, Frobenius acting only on the sixteen exceptional curves has just \(12\) different cycle types among these \(18\) classes. In particular, the same exceptional-curve cycle type \(2^8\) occurs with \(1\), \(7\), or \(21\) rational chambers, and cycle type \(4^4\) occurs with \(1\), \(3\), or \(5\) rational chambers. For every \(q\ge4\), every one of the eighteen Frobenius types occurs on a smooth degree-four del Pezzo surface, by Trepalin's existence theorem; thus these are genuine arithmetic distinctions.

## Assumptions and scope
A smooth degree-four del Pezzo surface means a smooth projective geometrically integral surface over \(\mathbb F_q\) with ample anticanonical class and self-intersection \(K_X^2=4\). There is no assumption of a rational plane blowdown. Over an algebraic closure, choose a blowdown to five general points of the plane, with Picard basis \(H,E_1,\ldots,E_5\), where \(H^2=1\), \(E_i^2=-1\), and all remaining pairings between distinct basis classes vanish.

A geometric Zariski chamber is a chamber of the big cone of \(X_{\overline{\mathbb F}_q}\), indexed by the support of the negative part of the Zariski decomposition; the distinguished nef chamber has empty support. These chambers form a finite canonical Galois set through their negative-curve supports. The associated finite etale scheme is the scheme corresponding to this Galois set; the assertion is about this configuration scheme, **not** a claim that the chamber regions themselves are a zero-dimensional moduli scheme. Frobenius acts on divisor classes preserving intersections, and the group of such geometric actions is \(W(D_5)\). The theorem identifies its element conjugacy class, not a marked matrix or the isomorphism class of \(X\).

## Proof
**1. Sixteen negative curves and the chamber supports.** The sixteen exceptional curves are the five \(E_i\), ten strict transforms \(H-E_i-E_j\) for \(i<j\), and one conic \(2H-\sum_{i=1}^5E_i\). These are all the geometric negative curves. Every curve in this list has self-intersection \(-1\), and pairwise intersection is either \(0\) or \(1\). A subset's intersection matrix is negative definite if and only if its members are pairwise disjoint: for an intersecting pair the principal matrix \(\left(\begin{smallmatrix}-1&1\\1&-1\end{smallmatrix}\right)\) is singular, while a disjoint set has matrix \(-I\). By the negative-definite-support correspondence of Bauer--Funke--Neumann (Proposition 1.1), each such subset gives exactly one nonnef chamber; add the empty set for the nef chamber. This correspondence is canonical under field automorphisms. The independence-set enumeration is \(1+16u+80u^2+160u^3+120u^4+16u^5\), so there are \(393\) chambers.

**2. Explicit Weyl action.** Let \(V\) consist of the sixteen even subsets of \(\{1,2,3,4,5\}\). Label the conic by \(\varnothing\), a strict transform \(H-E_i-E_j\) by \(\{i,j\}\), and the exceptional divisor \(E_i\) by the four-subset omitting \(i\). A direct intersection calculation gives for distinct labeled curves \(C_v,C_w\):
\[
C_v\cdot C_w=1\quad\Longleftrightarrow\quad |v\mathbin\triangle w|=4.
\]
The resulting \(5\)-regular, sixteen-vertex graph is the folded five-cube, also called the Clebsch graph in its \(5\)-regular convention. Its independent sets are the chamber supports. The affine transformations
\[
v\longmapsto \sigma(v)\mathbin\triangle t,
\qquad \sigma\in S_5,\quad |t|\equiv0\pmod2
\]
act as \(W(D_5)\cong (\mathbb Z/2)^4\rtimes S_5\) on the sixteen curve labels and preserve their intersections. This action contains all \(16\cdot 120=1920\) graph automorphisms: the stabilizer of the empty vertex can only permute its five neighbors, and the remaining ten nonneighbor vertices are uniquely determined by their pairs of neighbors. It therefore describes the full Weyl action on chambers.

**3. Finite, exhaustive class calculation.** An element is given by \((\sigma,t)\) with \(t\) even. Partition the permutation cycles of \(\sigma\) into positive and negative according to the parity of \(t\) on each cycle. There are \(18\) resulting signed cycle types; `check.py` verifies by explicit conjugation that these are exactly the eighteen conjugacy classes. For each of all \(1920\) elements the code computes the induced permutation on all \(393\) independent subsets, decomposes it into cycles, and checks that all members of each class share the same spectrum. All eighteen complete chamber spectra in `spectra.csv` are pairwise distinct. For a second check, the number of fixed chamber supports of each cardinality is computed independently by enumerating unions of cycles in the element's sixteen-vertex action. These numbers agree with the fixed points of the full \(393\)-permutation. All claimed counts, class sizes, and exceptional-curve comparison cases follow by exact enumeration; no random sampling or unverified search bounds enter this step.

**4. Arithmetic interpretation.** The canonical geometric chamber-support bijection is Frobenius-equivariant, so the computed spectrum is the Frobenius spectrum of \(\mathcal Z_X\). If \(c_d\) is the number of length-\(d\) cycles in its row, then
\[
Z_{\mathcal Z_X}(T)=\prod_{d\ge1}(1-T^d)^{-c_d},
\qquad \#\mathcal Z_X(\mathbb F_{q^n})=\sum_{d\mid n}d\,c_d.
\]
These point counts for all extensions determine the cycle spectrum by Mobius inversion. The computed eighteen pairwise distinct spectra therefore reconstruct the Weyl conjugacy class. The occurrence of all classes for \(q\ge4\) is independently supplied by Trepalin, Theorem 1.4, not by the finite-group enumeration.

## Verification
With Python \(3\) and its standard library, from the directory containing the two embedded artifacts run `python3 check.py spectra.csv` and compare the resulting CSV with the supplied `spectra.csv`. The verifier independently forms the curve-intersection graph from geometric divisor classes and from even-subset Hamming distances; checks \(40\) intersection edges and all \(393\) independent subsets; constructs all \(1920\) Weyl elements; verifies signed types against complete conjugation orbits; checks every group member's induced chamber cycle type; and independently counts invariant supports from unions of sixteen-curve permutation cycles. It asserts \(18\) distinct chamber spectra, \(12\) distinct line spectra, \(10\) base-field chamber counts and both non-reconstruction examples. The generated \(18\)-row certificate is deterministic.

## Relationship to prior work
Bauer--Funke--Neumann [1] prove the correspondence between Zariski chambers and negative-definite subsets and establish the absolute count \(393\) for degree-four del Pezzo surfaces. Trepalin [2] classifies the eighteen arithmetic Weyl types and their finite-field existence restrictions. Brodie--Constantin [3] explain the geometric chamber cohomology significance and again give the absolute count \(393\). These known results supply the geometric objects and the allowable Frobenius types. The new statement is the **injectivity of the single 393-chamber Frobenius permutation spectrum** on all eighteen Weyl conjugacy classes, including the exact arithmetic fixed-chamber and non-reconstruction profiles. It is not implied by any prior geometric total count or by the Picard-space eigenvalues alone. The prior full automorphism representation of Clebsch-graph independence **homology** concerns the nine-dimensional reduced homology module, not the 393-element face permutation representation and its full cycle spectra.

## Limitations
The theorem is a finite-etale arithmetic invariant of the geometric chamber index set, not a statement about classifying surfaces up to isomorphism or about counting rational divisor classes in each chamber. A Frobenius-stable geometric support corresponds to a rational invariant chamber, but individual negative curves in that support need not be rational. The 18-class separation rests on a reproducible finite exhaustive computation, not a compact symbolic closed formula for the full spectra. The group computation applies over all finite fields; the claim that every type is actually realized is asserted only for \(q\ge4\) as in [2]. Similar constructions in other del Pezzo degrees, and any independent literature confirmation of the 393-chamber arithmetic table, are beyond scope.

## References
[1] T. Bauer, M. Funke, S. Neumann, *Counting Zariski chambers on Del Pezzo surfaces*, first public 2009-12-04, [arXiv:0912.0958](https://arxiv.org/abs/0912.0958), Proposition 1.1 and main theorem.

[2] A. Trepalin, *Del Pezzo surfaces over finite fields*, first public 2018-03-17, [arXiv:1803.07421](https://arxiv.org/abs/1803.07421), Theorem 1.4, Section 6 and Table 4.

[3] C. R. Brodie and A. Constantin, *Cohomology Chambers on Complex Surfaces and Elliptically Fibered Calabi--Yau Three-folds*, first public 2020-09-02, [arXiv:2009.01275](https://arxiv.org/abs/2009.01275), Section 4.2.
