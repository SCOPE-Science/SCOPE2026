# One-leak forcing on wheels: a complete cyclic-window polynomial and minimal-set spectrum

## Finding

For every integer \(n\ge4\), let \(W_n=K_1\vee C_n\) consist of a hub \(h\) and cyclically labelled rim vertices \(v_0,\ldots,v_{n-1}\). Let \(L_n(z)=\sum_B z^{|B|}\), where the sum is over all one-leaky ordinary zero-forcing sets \(B\subseteq V(W_n)\) (one unknown vertex, possibly initially white, may not perform forces). Set \(b_i=1\) if \(v_i\in B\) and \(b_i=0\) otherwise, with cyclic indices.

**Complete structural characterization.** The set \(B\) is one-leaky zero forcing if and only if exactly one of the following applicable conditions holds:

- If \(h\in B\), there is a cyclic adjacent pair of selected rim vertices: \(b_i b_{i+1}=1\) for some \(i\).
- If \(h\notin B\), there are at least two distinct indices \(i\) for which \(b_{i-1}b_i b_{i+1}=1\). (Overlapping triples count separately by their centers.)

Write
\[
Q(z)=\begin{pmatrix}1&z\\1&0\end{pmatrix},\qquad
T(z,u)=\begin{pmatrix}1&z&0&0\\0&0&1&z\\1&z&0&0\\0&0&1&zu\end{pmatrix},
\]
with the rows and columns of \(T\) indexed by the binary pairs \(00,01,10,11\). Then the **complete labelled cardinality polynomial** is
\[
\boxed{L_n(z)=(1+z)^{n+1}-z\,\operatorname{tr}(Q(z)^n)
-\bigl([u^0]+[u^1]\bigr)\operatorname{tr}(T(z,u)^n).}
\]
Here \([u^j]\) means the coefficient of \(u^j\), and \(Q\) counts rim sets without adjacent selected vertices while \(T\) marks cyclic occurrences of three consecutive selected rim vertices.

In particular, let \(M_n(z)\) count inclusion-minimal one-leaky forcing sets by size. Then
\[
\boxed{M_4(z)=4z^3+z^4,\qquad
M_n(z)=nz^3+nz^4+\frac{n\max\{n-7,0\}}2z^6\quad(n\ge5).}
\]
Consequently, the inclusion-minimal cardinality spectrum is \(\{3,4\}\) for \(4\le n\le7\) and \(\{3,4,6\}\) for \(n\ge8\). In particular the first size-six minimal sets occur at \(n=8\) (four configurations), while no inclusion-minimal size-five set exists for any \(n\ge4\).

The excluded-rim-word polynomial \(A_n(z)=([u^0]+[u^1])\operatorname{tr}(T(z,u)^n)\) also has an explicit rational ordinary generating function. With \(D_0(t,z)=1-t-zt^2-z^2t^3\) and \(D_1(t,z)=-zt+zt^2+z^2t^3\),
\[
\sum_{n\ge1}A_n(z)t^n=-t\frac{\partial}{\partial t}
\left(\log D_0(t,z)+\frac{D_1(t,z)}{D_0(t,z)}\right).
\]
The identity is understood formally in the power-series ring with constant term \(1\) in \(D_0\).

## Assumptions and scope

Graphs are finite, undirected and loopless. The ordinary zero-forcing rule permits a blue vertex with exactly one white neighbor to turn that neighbor blue. A *leak* is a vertex forbidden from performing forces, but it may be turned blue by another vertex; a one-leaky forcing set succeeds for every single leak location (including an initially white vertex). Both the hub and every rim vertex are distinguishable, so the polynomial counts labelled subsets. The rim length is \(n\ge4\); the triangular rim has a different small-order overlap convention and is not included.

## Proof

**1. Cycle propagation lemma.** On a cycle, any two adjacent blue vertices force the entire cycle despite one leak. To see this, regard the remaining white vertices as one interval with two boundary fronts. If neither boundary leaks, propagate from both ends; when one front is blocked by the leak, the other (which cannot encounter another leak) continues through the interval. This also handles a leak initially inside the white interval. The extra hub, when already blue, does not affect white-neighbor counts of rim vertices.

**2. Hub initially blue.** If two cyclically adjacent rim vertices are blue, the cycle lemma proves sufficiency without requiring the hub to force. If there is no such pair, each blue rim vertex has both rim neighbors white and hence cannot force. The hub can force only if exactly one rim vertex is white. For \(n\ge4\), that situation itself entails adjacent blue rim vertices. Thus no force can begin in the contrary case, proving necessity.

**3. Hub initially white.** Before the hub becomes blue, every blue rim vertex has at least the hub as a white neighbor, so it cannot force another rim vertex. Its *only* possible force is the hub, and precisely the initially blue rim vertices whose two rim neighbors are blue can perform this force. These are exactly the centers of selected cyclic \(111\) triples. If there are zero such centers, forcing never begins. If there is exactly one, declare that center the leak; forcing again never begins. If there are at least two, at least one is not the chosen leak and can force the hub. The initially selected triple also contains an adjacent rim pair, so the cycle lemma completes the propagation regardless of the same leak. This proves the characterization.

**4. Exact polynomial.** The matrix \(Q\), with states the preceding binary bit, gives weight \(z\) for a newly selected rim vertex and forbids the \(1\to1\) transition. Hence \(\operatorname{tr}(Q^n)\) counts labelled cyclic binary words with no adjacent selected rim pair. For \(T\), states are the two preceding bits; a transition \((a,b)\to(b,c)\) contributes \(z^c u^{abc}\). Closed walks of length \(n\) are in bijection with labelled cyclic binary words, and their weights record both the selected-vertex count and the number of selected \(111\) windows. Thus the hub-selected contribution is \(z((1+z)^n-\operatorname{tr}(Q^n))\), while the hub-absent contribution is \((1+z)^n-([u^0]+[u^1])\operatorname{tr}(T^n)\). Summation proves the boxed polynomial. Direct expansion of \(\det(I-tT(z,u))\) gives \(D_0(t,z)+uD_1(t,z)\). The standard identity \(\sum_{n\ge1}\operatorname{tr}(T^n)t^n=-t\partial_t\log\det(I-tT)\) and coefficient extraction through degree one in \(u\) prove the stated rational generating function.

**5. Inclusion-minimal sets.** With the hub selected, an inclusion-minimal configuration consists of the hub and exactly two adjacent selected rim vertices, giving \(n\) sets of size three. With the hub absent, minimality for the monotone property 'at least two selected \(111\) windows' means the selected rim set must be the union of two such windows, with each selected vertex essential. Two windows overlapping in two rim vertices give exactly one four-vertex consecutive block. Windows overlapping in one rim vertex give a five-vertex block that contains a four-vertex block and are not minimal. Two disjoint windows give a minimal six-set precisely when the two selected three-blocks have at least one unselected rim vertex in both cyclic gaps; otherwise the six-set includes a four-block and is not minimal. For \(n\ge5\), the number of distinct four-blocks is \(n\); for \(n=4\), it is one. For \(n\ge8\), the number of unordered pairs of disjoint length-three blocks separated in both directions is \(n(n-7)/2\): fix the first starting position, choose the second starting position at cyclic offsets \(4,\ldots,n-4\), then divide by two. No such pairs exist for \(n<8\). This proves the second boxed formula and its spectrum consequences.

## Verification

The standalone standard-library Python program `verify.py` performs independent ordinary color-change closure checks with each possible leak at each vertex, enumerating every initial set for \(4\le n\le11\). It separately checks the cyclic-window criterion, the full transfer-matrix polynomial, and the inclusion-minimal polynomial. For \(12\le n\le16\), it additionally checks the transfer counts against independent cyclic-word enumeration. The successful outputs include `TRANSFER_EXTENDED_OK` and `WHEEL_ONE_LEAK_VERIFY_OK`. These are finite regression tests; the proof for arbitrary \(n\) is the structural argument and transfer-walk bijection above.

## Relationship to prior work

Dillman and Kenter introduced leaky forcing in the public preprint arXiv:1910.00168, first posted October 1, 2019. Alameda, Dillman and Kenter, *Leaky forcing: a new variation of zero forcing*, Australasian Journal of Combinatorics 88(3) (2024), Proposition 3.6, establish the scalar equality \(Z_{(1)}(W_n)=3\) and the entire leak-number profile. The present result refines that scalar fact to a complete all-cardinality polynomial, a local criterion for every placement, and the inclusion-minimal size spectrum. Its hub-selected component parallels earlier non-leaky/connected forcing considerations, but the hub-absent two-window requirement is specific to failure tolerance. Wang, *Modular Compression of Leaky Forts and Leaky Forcing Polynomials* (2026), supplies a general fort-based exact method for arbitrary type representations; its universal procedure is not an evaluated wheel polynomial or an inclusion-minimal wheel classification. The present wheel formulas do not require a bounded-type compression assumption.

## Limitations

Only ordinary vertex-leaky zero forcing with one leak is treated. The formulas do not cover two leaks, positive-semidefinite forcing, or arbitrary wheel modifications. The primary literature comparison is substantial but not a comprehensive proof of publication priority. No independent mathematical audit has been performed.

## References

1. S. Dillman and F. Kenter, *Leaky Forcing: A New Variation of Zero Forcing*, arXiv:1910.00168, first public version October 1, 2019. https://arxiv.org/abs/1910.00168
2. J. S. Alameda, S. Dillman and F. Kenter, *Leaky forcing: a new variation of zero forcing*, Australasian Journal of Combinatorics 88(3) (2024), 308–326, especially Proposition 3.6, pp. 314–315. https://ajc.maths.uq.edu.au/pdf/88/ajc_v88_p308.pdf
3. X. Wang, *Modular Compression of Leaky Forts and Leaky Forcing Polynomials* (2026), DOI 10.5281/zenodo.20388397, relevant sections 2–6. https://doi.org/10.5281/zenodo.20388397
