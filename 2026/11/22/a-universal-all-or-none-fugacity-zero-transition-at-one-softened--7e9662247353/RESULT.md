# A universal all-or-none fugacity-zero transition at one softened bond of a hard-core chain

## Finding

For every integer \(m\ge2\), a centered one-bond perturbation of the open one-dimensional hard-core lattice gas has a sharp and size-independent partition-zero boundary at \(a=1\). With \(d=\lfloor(m+1)/2\rfloor\), its finite-size fugacity polynomial has precisely \(2d\) simple negative real zeros for \(0<a<1\), precisely \(m\) simple negative real zeros at \(a=0\), precisely \(d\) distinct double negative zeros at \(a=1\), and no real zeros for \(a>1\). All \(d\) double roots split simultaneously into nonreal conjugate pairs immediately above the threshold. The complete statement holds at arbitrary chain length, not just at fixed finite examples.

The exact algebraic identity underlying the transition is

\[
Z_{2m}(z;a)=I_m(z)^2+(a-1)z^2I_{m-2}(z)^2.
\]

## Assumptions and scope

There are \(2m\) sites \(1,\ldots,2m\) arranged in a path, where \(m\ge2\). The occupation numbers \(\eta_j\in\{0,1\}\) obey \(\eta_j\eta_{j+1}=0\) for every \(j\ne m\). The central pair \((m,m+1)\) is unrestricted and, when simultaneously occupied, receives the relative Boltzmann factor \(a\ge0\). Each occupied site contributes fugacity \(z\); complex \(z\) is used to locate zeros, and real positive \(z\) is the physical fugacity. The grand-canonical polynomial is

\[
Z_{2m}(z;a)=\sum_{\substack{\eta\in\{0,1\}^{2m}\\\eta_j\eta_{j+1}=0\ (j\ne m)}}z^{\sum_j\eta_j}a^{\eta_m\eta_{m+1}},
\]

where the convention at \(a=0\) excludes central double occupation. Let \(I_j(z)\) denote the ordinary hard-core path polynomial with \(j\) sites, so \(I_0=1\), \(I_1=1+z\), and \(I_j=I_{j-1}+zI_{j-2}\) for \(j\ge2\). Write \(Q_m(z)=zI_{m-2}(z)\).

## Proof

**The central-bond identity.** At \(a=1\), the two halves are independent paths of length \(m\), giving \(I_m^2\). Altering the relative weight of configurations with both central sites occupied by \(a-1\) adds \((a-1)z^2 I_{m-2}^2\), since then the two adjacent sites are vacant and each remaining half is an independent path of length \(m-2\). This proves the displayed identity, including \(a=0\).

**The repulsive regime.** For \(0\le a<1\), set \(s=\sqrt{1-a}\). The recursion \(I_m=I_{m-1}+zI_{m-2}\) gives the exact factorization

\[
Z_{2m}(z;a)=\bigl(I_{m-1}(z)+(1+s)zI_{m-2}(z)\bigr)\bigl(I_{m-1}(z)+(1-s)zI_{m-2}(z)\bigr).
\]

Each factor \(F_b(z)=I_{m-1}(z)+bzI_{m-2}(z)\) is the matching-generating polynomial of a path on \(m+1\) vertices with \(m\) edges, whose final edge has weight \(b\) and whose other edges have weight one. Indeed, condition on whether that final edge is chosen. For \(b>0\), the associated symmetric Jacobi matrix has positive nearest-neighbor off-diagonal entries \(1,\ldots,1,\sqrt b\), and its characteristic polynomial is the standard alternating matching transform \(t^{m+1}F_b(-1/t^2)\). Every eigenvalue of an irreducible real symmetric tridiagonal matrix is simple. Bipartiteness makes the nonzero eigenvalues occur in \(\pm\) pairs. Consequently every zero of \(F_b\) is simple, strictly negative. At \(b=0\), the factor is \(I_{m-1}\), which has the same property by the shorter-path argument.

For \(a<1\), the two values of \(b\) are unequal. The two factors have no common zero: a common root would satisfy \(zI_{m-2}(z)=I_{m-1}(z)=0\), which is impossible because \(I_{m-1}(0)=1\) and consecutive path polynomials are coprime by the recursion. Thus all zeros are simple and negative. For \(0<a<1\), both factors have degree \(d=\lfloor(m+1)/2\rfloor\), giving \(2d\) roots. At \(a=0\), the second factor has \(b=0\) and degree \(\lfloor m/2\rfloor\), while the first has degree \(d\), giving \(m\) roots.

**The transition and attractive regime.** At \(a=1\), the identity becomes \(Z_{2m}=I_m^2\). The path matching argument gives precisely \(d\) simple negative roots of \(I_m\), hence exactly \(d\) double roots of \(Z_{2m}\). For any \(a>1\) and any real \(z\),

\[
Z_{2m}(z;a)=I_m(z)^2+(a-1)Q_m(z)^2>0.
\]

Strict positivity follows because \(I_m\) and \(Q_m\) are coprime (the same path recursion proves it). Thus no real zero exists anywhere above the threshold. The degree for every \(a>1\) remains \(2d\), so the zeros occur in conjugate nonreal pairs counted with multiplicity.

**Local departure law.** Fix any zero \(\alpha\) of \(I_m\). Its simplicity and the coprimality \(Q_m(\alpha)\ne0\) permit implicit-function expansion of \(I_m(z)\pm i\sqrt{a-1}\,Q_m(z)=0\). The two branches are

\[
z_\pm(a)=\alpha\pm i\frac{Q_m(\alpha)}{I_m'(\alpha)}\sqrt{a-1}+O(a-1),\qquad a\downarrow1\text{ from above}.
\]

The coefficient is nonzero. Every collision therefore opens transversely at square-root scale; the sign convention for the branch labels is immaterial.

**A singular zero at complete exclusion.** If \(m\) is odd, the coefficient of the highest power \(z^{m+1}\) in \(Z_{2m}\) is \(a\), while the coefficient of \(z^m\) equals \(m+1+O(a)\); all other \(m\) roots tend to the simple roots of \(I_{2m}\) as \(a\downarrow0\). Vieta's formula therefore gives a unique escaping real root

\[
z_{\mathrm{extra}}(a)=-\frac{m+1}{a}+O(1),\qquad a\downarrow0.
\]

This explains why the number of finite real roots jumps from \(m\) at \(a=0\) to \(m+1\) for every positive \(a<1\) when \(m\) is odd.

## Verification

The standalone script `verify_softlink.py` independently enumerates all admissible occupation configurations for \(m=2,\ldots,10\) and compares their bivariate partition polynomials with the exact formula. It also verifies real-root counts using exact Sturm methods for eight rational values of \(a\) and \(m=2,\ldots,9\), including both sides of the threshold and the collision itself, and checks the necessary coprimality identities for \(m=2,\ldots,19\). The script uses Python and SymPy and reports `SOFT_LINK_EXACT_VERIFICATION_PASSED 9 64 18` upon success. These finite checks support, but do not replace, the analytic all-length proof above.

For the smallest admissible size \(m=2\), the polynomial is \(Z_4(z;a)=1+4z+(a+3)z^2\), whose discriminant is \(4(1-a)\). This already exhibits the exact threshold. The higher-size result is not obtained by extrapolation from this example.

## Relationship to prior work

Vavro's exact one-dimensional lattice-gas partition analysis [1] motivates the finite-chain model, but concerns uniform nearest-neighbor interactions and does not classify zeros of a single centered soft-bond perturbation. Scott and Sokal [2] develop repulsive lattice gases, independent-set polynomials and homogeneous soft-interaction path examples. Their discussion establishes important background, not the simultaneous double-root collision and complete real-zero dichotomy for one distinguished central link across all sizes. Wagner [3] explains weighted matching-polynomial real-rootedness using the Heilmann–Lieb theorem [4]; that established theorem provides the root-location input for the new two-factor identity rather than proving the soft-bond classification on its own. The new contribution is the exact all-size one-defect factorization and the sharp, simultaneous passage of every root pair into the nonreal plane when the single bond becomes attractive.

## Limitations

This result concerns an open path of even length with one centered bond and common site fugacity. It does not treat odd or off-center paths, several soft bonds, heterogeneous site fugacities, or thermodynamic-limit singularities. The word “transition” refers only to the zero geometry of finite partition polynomials. The originality comparison is based on inspected primary sources and indexed records, not an exhaustive guarantee against unindexed equivalent earlier results.

## References

[1] J. Vavro, *An Exact Solution for the Lattice Gas Model in One Dimension* (first arXiv posting 2000-11-23), https://arxiv.org/abs/cond-mat/0011401.

[2] A. D. Scott and A. D. Sokal, *The repulsive lattice gas, the independent-set polynomial, and the Lovász local lemma* (first arXiv posting 2003-09-15), https://arxiv.org/abs/cond-mat/0309352.

[3] D. G. Wagner, *Weighted enumeration of spanning subgraphs with degree constraints* (first arXiv posting 2008-03-11), https://arxiv.org/abs/0803.1659.

[4] O. J. Heilmann and E. H. Lieb, *Theory of Monomer-Dimer Systems*, Communications in Mathematical Physics 25 (1972), 190–232, https://doi.org/10.1007/BF01877590.
