# Four-point erasure rigidity for quadratic harmonics on type-\(D\) root configurations

## Finding
For each integer \(d\ge4\), let
\[
X_d=\{(s e_i+t e_j)/\sqrt2:1\le i<j\le d,\ s,t\in\{-1,1\}\}\subset S^{d-1}.
\]
Let \(\mathcal H_{\le2}(S^{d-1})\) be the complex space of spherical harmonics of total degree at most two, of dimension \(d(d+3)/2\). For any erased set \(E\subset X_d\), observe a function at every vertex in \(X_d\setminus E\). The following is an exact characterization of the first possible loss of unique reconstruction:

**Theorem.** The full evaluation map on \(X_d\) is injective. Every erasure of at most three vertices preserves injectivity. An erasure of exactly four vertices destroys injectivity if and only if it has one of the following forms:

1. For any \(d\ge4\), erase the complete four-vertex coordinate square \(\{(\pm e_i\pm e_j)/\sqrt2\}\), with the signs chosen independently, for some \(i<j\). There are exactly \(\binom d2\) such sets.
2. Exclusively when \(d=4\), partition \(\{1,2,3,4\}\) into two disjoint pairs \(\{i,j\}\), \(\{k,l\}\). From each coordinate square choose any *one* of its two antipodal vertex pairs, and erase the union of the chosen pairs. There are exactly \(3\cdot2\cdot2=12\) additional sets.

Thus the number of singular four-vertex erasures equals \(18\) for \(d=4\) and \(\binom d2\) for every \(d\ge5\). Equivalently, the degree-at-most-two evaluation code on \(X_d\) has minimum nonzero support size four, with precisely those supports. In the 24-cell case, all 18 supports are unions of two orthogonal antipodal pairs; the additional twelve do not extend to higher dimensions.

## Assumptions and scope
All coordinates are over \(\mathbb R\) for the sampling locations and over \(\mathbb C\) (or \(\mathbb R\)) for functions. Every antipodal vertex counts as an individual observation. The harmonic band comprises degrees zero, one *and* two rather than only degree two. A four-vertex erasure fails precisely when a nonzero polynomial in this band vanishes on all un-erased vertices. No claim is made about the optimal condition number for successful erasure patterns or about larger erasures.

On the sphere, this harmonic band is the restriction of all polynomials of total degree at most two, modulo multiples of \(\|x\|^2-1\). This has dimension \(\binom{d+2}{2}-1=d(d+3)/2\).

## Proof
**1. Edge--Walsh coordinates.** Fix coefficients \(h_i,\ell_i\in\mathbb C\) for \(1\le i\le d\), and \(\gamma_{ij}\in\mathbb C\) for \(i<j\). Every member of the harmonic band has a unique representation on \(X_d\) of the form
\[
 f((s e_i+t e_j)/\sqrt2)=h_i+h_j+\ell_i s+\ell_jt+\gamma_{ij}st.\tag{1}
\]
Indeed, write the polynomial as a constant, a linear part, a trace-free diagonal quadratic, and off-diagonal quadratic monomials. At the roots, its constant and diagonal terms are pair sums \(h_i+h_j\); the linear and mixed terms become the other three terms of (1). Conversely arbitrary \(h_i\) represent an arbitrary constant plus trace-free diagonal quadratic, and all other coefficients are arbitrary. The total parameter count is \(2d+\binom d2=d(d+3)/2\). For each edge \(ij\), the four sign patterns form a Walsh basis \(1,s,t,st\). Therefore if all vertex evaluations vanish, \(h_i+h_j=0\), \(\ell_i=\ell_j=0\), and \(\gamma_{ij}=0\) for every edge. Because \(K_d\) contains a triangle and is connected, all \(h_i\) also vanish. This proves injectivity and uniqueness of (1).

**2. The odd part cannot have four-point support.** Suppose some \(\ell_i\neq0\), and let \(r\) be the number of nonzero \(\ell_i\). A projective antipodal pair associated to the edge \(ij\) has a nonzero odd component whenever one of the values \(\ell_i+\ell_j\), \(\ell_i-\ell_j\) is nonzero. Such a pair forces at least one nonzero vertex value of \(f\), because its two antipodal values have different odd parts. Every edge with exactly one nonzero endpoint contributes two such projective pairs; every edge with two nonzero endpoints contributes at least one. Consequently
\[
 |\operatorname{supp}_{X_d} f|\ge 2r(d-r)+\binom r2.
\]
For \(1\le r<d\), the first term is at least \(2(d-1)\ge6\); for \(r=d\), the binomial term is at least six. Hence a nonzero function supported on four or fewer vertices has \(\ell_i=0\) for every \(i\). It is antipodally even, so its support is a union of full antipodal pairs.

**3. A graph with at most two deleted edges.** In the even case, the two antipodal-pair values on the coordinate square for edge \(ij\) are \(h_i+h_j+\gamma_{ij}\) and \(h_i+h_j-\gamma_{ij}\). Set \(F=\{ij:h_i+h_j\neq0\}\). Each edge of \(F\) forces at least one nonzero projective pair, hence at least two vertices in the support. If the support has size at most four, \(|F|\le2\). For every edge in \(K_d\setminus F\), the equation \(h_i+h_j=0\) holds. If that graph is connected and contains an odd cycle, these equations force all \(h_i=0\).

For \(d\ge5\), deleting at most two edges of \(K_d\) leaves a connected graph containing a triangle (each deleted edge belongs to only \(d-2\) of the \(\binom d3\) triangles, so at least one remains). For \(d=4\), the same conclusion holds except when \(F\) is a perfect matching of two disjoint edges; deleting those two edges leaves a four-cycle. Thus when \(d\ge5\), necessarily \(h_i=0\) for every \(i\); when \(d=4\), either all \(h_i=0\), or after relabelling \(F=\{ij,kl\}\) and \((h_i,h_j,h_k,h_l)=(a,a,-a,-a)\) for some nonzero \(a\).

**4. Classification and counts.** If all \(h_i=0\), every nonzero \(\gamma_{ij}\) produces four nonzero values on its coordinate square. Therefore support size at most four means exactly one nonzero \(\gamma_{ij}\), giving one of the \(\binom d2\) coordinate squares. In the exceptional four-dimensional case, the two edges of \(F\) have nonzero sums \(2a\) and \(-2a\). To achieve four-point support, each must contribute exactly one antipodal pair and no other edge can contribute. Hence \(\gamma_{ij}=\pm2a\) and \(\gamma_{kl}=\pm2a\), while all other mixed coefficients vanish. The choices yield exactly the twelve stated unions, one from each choice of perfect matching and pair orientations. Conversely each pattern is realized by the displayed coefficients. All other nonzero polynomials have support at least five (and those with a nonzero odd part at least six). This proves the theorem and the minimum distance four. In particular, any three erased vertices leave no nonzero polynomial supported entirely on them.

## Verification
The standalone standard-library script `verify_d_root_erasures.py` independently constructs the 24-cell vertices and the degree-at-most-two reproducing-kernel projection. It proves the integer matrix identity \(M^2=24M\) and \(\operatorname{tr}M=336\), then computes exact Bareiss determinants of the complementary Gram matrix for **all** \(24+276+2024+10626=12950\) erasure sets of size one through four. The only singular sets are the 18 classified four-vertex patterns. The script additionally checks the explicit polynomial witnesses for the twelve exceptional patterns and the coordinate-square witnesses in dimensions four through ten. Run `python3 verify_d_root_erasures.py` with Python 3; no third-party libraries are required. Finite checks supplement but do not replace the graph proof valid for every \(d\ge4\).

## Relationship to prior work
Zandieh, Han and Avron (2022) give near-optimal randomized recovery of bounded-degree spherical-harmonic expansions, whereas the present theorem classifies exactly which smallest deterministic erasures cause loss of identifiability on a specific natural infinite family of sampling nodes. Hirao, Nozaki and Tasaka (2023) establish exceptional spherical-design properties of the 24-cell and related root-system shells, not the degree-two evaluation code's four-point supports. Published studies of the 24-cell's individual exact-degree harmonic sampling spectrum address whole-grid eigenspaces, not this mixed degree-zero-to-two band and its deleted-row rank; published cuboctahedral degree-two erasure classification concerns a different twelve-vertex root configuration and a different rank matroid. The proof here exposes the dimension-four exception through the unique four-cycle left by deleting a perfect matching from \(K_4\).

## Limitations
The classification concerns only erasures of at most four samples and no quantitative conditioning bounds; it is not an all-erasure rank formula. It does not assert these deterministic roots are near-optimal for oversampled noisy recovery. Equivalent results under coding-theoretic or root-system nomenclature could exist outside the sources inspected. No independent audit has been performed.

## References
1. A. Zandieh, I. Han, and H. Avron, *Near Optimal Reconstruction of Spherical Harmonic Expansions*, arXiv:2202.12995, initial public version 25 February 2022, https://arxiv.org/abs/2202.12995.
2. M. Hirao, H. Nozaki, and K. Tasaka, *Spherical designs and modular forms of the \(D_4\) lattice*, arXiv:2303.09000, initial public version 16 March 2023, https://arxiv.org/abs/2303.09000.
3. H. Cohn, J. H. Conway, N. D. Elkies, and A. Kumar, *The \(D_4\) root system is not universally optimal*, arXiv:math/0607447, initial public version 19 July 2006, https://arxiv.org/abs/math/0607447.
