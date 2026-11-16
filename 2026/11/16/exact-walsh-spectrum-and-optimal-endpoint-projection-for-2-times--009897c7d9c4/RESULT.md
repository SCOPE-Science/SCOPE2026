# Exact Walsh spectrum and optimal endpoint projection for \(2\times3\times4\) boxed plane partitions

## Finding
Let \(P=[2]\times[3]\times[4]\) carry the componentwise order, and let \(f:\mathbb F_2^{P}\to\{0,1\}\) indicate its order ideals. There are exactly \(490\) such ideals. On the group \(G=\mathbb F_2^{24}\), define counting convolution by \((Tg)(x)=\sum_{y\in G}f(y)g(x-y)\).

The complete unnormalized Walsh multiplier distribution of \(T\) is the exact, finite table `spectrum.csv` (442 distinct signed values). In particular,
\[
\#\{t:\widehat f(t)=0\}=1{,}234{,}934,\qquad
\operatorname{rank}T=15{,}542{,}282,
\]
with smallest positive multiplier magnitude \(2\), largest magnitude \(490\), and positive-spectrum Hilbert-space condition number \(245\). The best possible \(\ell^1(G)\) and \(\ell^\infty(G)\) norms among **all** complex- or real-linear projections onto \(\operatorname{ran}T\) coincide and equal
\[
\boxed{\Lambda_1(\operatorname{ran}T)=\Lambda_\infty(\operatorname{ran}T)
=\frac{2{,}769{,}729{,}587}{4{,}194{,}304}.}
\]
The minimizing projection is the Fourier-support projector. These are exact statements about the full binary coordinate cube, not a restriction to symmetric signings.

## Assumptions and scope
Coordinates of \(P\) are triples \((i,j,k)\), with \(0\le i<2\), \(0\le j<3\), \(0\le k<4\). Their fixed bit numbering is \(\operatorname{index}(i,j,k)=12i+4j+k\). A subset \(I\subseteq P\) is an order ideal when \(p\in I\) and \(q\le p\) imply \(q\in I\). Its 24-bit membership vector is an element of \(G\). Every character is \(\chi_t(x)=(-1)^{\sum_{p\in P}t_px_p}\), and
\[
W(t)=\widehat f(t)=\sum_{I\text{ ideal}}\chi_t(\mathbf 1_I).
\]
The Fourier transform is unnormalized. Operator norms use counting measure on the finite group; a constant common normalization of the underlying \(\ell^p\) norms does not change operator norms. The term ``projection'' means an arbitrary bounded linear idempotent with precisely the stated range, with no translation-invariance assumption.

## Proof
**Exact ideal enumeration.** An ideal has heights \(h_{ij}\in\{0,1,2,3,4\}\) satisfying \(h_{i,j}\ge h_{i+1,j}\) and \(h_{i,j}\ge h_{i,j+1}\). Its membership vector has bits \((i,j,k)\) for \(0\le k<h_{ij}\). Enumerating all legal six-height arrays produces \(490\) distinct masks. Independently, start with the empty ideal and repeatedly adjoin a cube if all its immediate predecessors are present. These two algorithms generate identical 490-element sets. The number also agrees with the classical boxed-plane-partition product
\[
\prod_{i=1}^{2}\prod_{j=1}^{3}\prod_{k=1}^{4}
\frac{i+j+k-1}{i+j+k-2}=490.
\]
**Multiplier census.** Place a one at each ideal mask in a length-\(2^{24}\) array and a zero elsewhere. Twenty-four standard Hadamard butterfly stages compute every \(W(t)\) by the character formula. The packaged checker independently reproduces all coefficients by reversing butterfly order and using the independent breadth-first ideal enumeration; additionally, 8192 characters are evaluated from their defining signed sums. The certified signed-multiplier histogram (`spectrum.csv`) has 442 entries, of which 1,234,934 frequencies have multiplier zero. The rank therefore is \(2^{24}-1{,}234{,}934=15{,}542{,}282\). Inspection of all histogram entries shows the nonzero absolute extremes \(2\) and \(490\). All intermediate arithmetic is exact in signed integers.

**Support-kernel census.** Set \(E=\{t:W(t)\ne0\}\) and
\[
H(x)=\sum_{t\in E}(-1)^{\langle t,x\rangle}.
\]
A second exact 24-stage transform, independently checked in opposite butterfly order, yields the full histogram `projection_kernel.csv` and
\[
\sum_{x\in G}|H(x)|=11{,}078{,}918{,}348.
\]
The canonical Fourier projection \(Q\) onto \(\operatorname{ran}T\) is convolution with \(H/2^{24}\), so on \(\ell^1(G)\) and \(\ell^\infty(G)\),
\[
\|Q\|=2^{-24}\sum_x|H(x)|
=\frac{2{,}769{,}729{,}587}{4{,}194{,}304}.
\]
**Unrestricted minimality.** For any real- or complex-linear projection \(R\) onto this translation-invariant range, form its translation average \(R_0=|G|^{-1}\sum_{g\in G}\tau_{-g}R\tau_g\). It still maps into the range, acts as the identity on the range, commutes with all translations, and has norm at most \(\|R\|\). A translation-commuting projection is a character multiplier, necessarily one on \(E\) and zero off \(E\); hence \(R_0=Q\). This proves the claimed minimum for either endpoint norm.

**Spectral symmetry check.** Because \(P\) has a unique minimum, every nonempty ideal contains that minimum. Toggling its frequency bit changes every nonempty term's sign but leaves the empty-ideal term fixed, so \(W(t\oplus e_{\min})=2-W(t)\). The generated histogram satisfies this relation at all 442 levels.

## Verification
The `check.cpp` file is a self-contained C++17 checker; compile and run it from a writable directory:

```sh
c++ -std=c++17 -O3 check.cpp -o check
./check
```

It regenerates and compares the two ideal sets, two signed transforms, 8192 direct character sums, both transformed support arrays, and the two CSV tables. It verifies \(\sum_t W(t)=2^{24}\), \(\sum_t W(t)^2=490\,2^{24}\), \(H(0)=15{,}542{,}282\), \(\sum_x H(x)=2^{24}\), and \(\sum_xH(x)^2=15{,}542{,}282\,2^{24}\). The reported output marker is `BOXED_PLANE_PARTITION_234_WALSH_PASS`. The finite checks are exhaustive for the declared 24-dimensional group.

## Relationship to prior work
Boxed plane partitions are classical; in particular, the 490 count is a special case of MacMahon's product. Cohn, Larsen and Propp study uniform hexagon tilings and their product formulas and limit shapes. Borodin, Gorin and Rains study parameterized elliptic and related weighted tiling measures, including a multivariate-looking but parameter-restricted product formula in their appendix. Those results give the motivating ensemble and weighted generating functions but do not state the complete census over all 24 independently signed cube coordinates, nor the evaluated projection-range norm. The present theorem does not claim a new counting formula, a new general Fourier-transform algorithm, or the classical translation-averaging lemma.

## Limitations
This is an exact finite classification for the first genuinely three-dimensional box whose three side lengths are pairwise distinct and at least two. It gives no all-box formula, no asymptotic projection bounds and no claim about continuous Fourier analysis of random height fields. Computational exhaustiveness applies only to this finite box. Literature comparison is bounded and cannot establish historical priority absolutely; no independent external mathematical audit has been conducted.

## References
1. H. Cohn, M. Larsen and J. Propp, *The Shape of a Typical Boxed Plane Partition*, arXiv:math/9801059 (first submitted 1998-01-13), especially the introduction and Section 2.
2. A. Borodin, V. Gorin and E. M. Rains, *q-Distributions on Boxed Plane Partitions*, arXiv:0905.0679 (first submitted 2009-05-05), especially Sections 2--3 and Theorem 10.5.
3. NIST Digital Library of Mathematical Functions, Section 26.12, plane partitions and boxed product enumeration, https://dlmf.nist.gov/26.12.
