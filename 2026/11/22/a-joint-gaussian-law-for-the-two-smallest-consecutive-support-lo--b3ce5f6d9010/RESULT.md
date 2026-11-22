# A joint Gaussian law for the two smallest consecutive-support loops in random meandric systems

## Finding
Let \(n\ge1\). Independently choose two uniformly distributed noncrossing perfect matchings of the linearly ordered sites \(1,\ldots,2n\); draw one above and one below the line, obtaining a uniform meandric system. Let \(X_n\) be the number of connected loop components supported by exactly two adjacent sites \(\{i,i+1\}\). Let \(Y_n\) be the number of connected loop components supported by exactly four consecutive sites \(\{j,j+1,j+2,j+3\}\). For such a four-site loop, the two matchings necessarily use, in opposite orders, the pairings \(\{(j,j+1),(j+2,j+3)\}\) and \(\{(j,j+3),(j+1,j+2)\}\). Both upper/lower orientations are included in \(Y_n\).

Put \(C_m=\frac1{m+1}\binom{2m}{m}\), and let \((z)_k=z(z-1)\cdots(z-k+1)\), with \((z)_0=1\). For all nonnegative integers \(r,s\) with \(r+2s\le n\), the **entire joint factorial-moment array** is
\[
\mathbb E[(X_n)_r(Y_n)_s]
=2^s(2n-r-3s)_{r+s}\left(\frac{C_{n-r-2s}}{C_n}\right)^2.
\]
For \(r+2s>n\), the expectation is zero. These finite arrays uniquely determine the exact joint distributions by finite factorial-moment inversion.

In particular, for every \(n\ge3\),
\[
\operatorname{Cov}(X_n,Y_n)=-\frac{n^2(n+1)^2(10n^3-41n^2+32n+11)}{32(2n-5)(2n-3)^2(2n-1)^3}<0.
\]
The mean counts satisfy \(\mathbb E X_n=\frac{(n+1)^2}{4(2n-1)}\) for \(n\ge1\) and \(\mathbb E Y_n=\frac{n^2(n+1)^2}{8(2n-3)(2n-1)^2}\) for \(n\ge2\), while \(Y_1=0\).

Most importantly, the **joint central limit theorem** holds:
\[
\frac1{\sqrt n}\begin{pmatrix}X_n-n/8\\Y_n-n/64\end{pmatrix}
\xrightarrow{\mathrm d}\mathcal N_2\!\left(\begin{pmatrix}0\\0\end{pmatrix},
\begin{pmatrix}13/128&-5/1024\\-5/1024&121/8192\end{pmatrix}\right).
\]
The limiting covariance matrix is positive definite (determinant \(387/262144\)); the limiting correlation is \(-5\sqrt{13}/143\), which is nonzero and negative.

## Assumptions and scope
The sample is uniform over all \(C_n^2\) ordered pairs of noncrossing perfect matchings; the sites are linear, not periodically identified. A component is a loop of the union of the upper and lower arcs, not an individual matching edge. The four-site statistic counts only components whose support consists of four *consecutive* sites; it does not count four-site components with gaps. Both mirror-image upper/lower configurations contribute. The finite factorial-moment identity is exact for every integer \(n\ge1\); the negative covariance is asserted for \(n\ge3\), and the Gaussian limit is as \(n\to\infty\).

## Proof
**1. Joint factorial moments.** A specified two-site component forces its sole adjacent edge in both matchings. A specified four-consecutive-site component forces one of two opposite upper/lower local pairing configurations, hence the multiplicative factor \(2\). Distinct components have disjoint supports; overlapping consecutive windows cannot both be components. For ordered selections of \(r\) two-site windows and \(s\) four-site windows, first order the \(r+s\) labeled blocks and distribute unused sites into \(r+s+1\) gaps. This gives \((2n-r-3s)_{r+s}\) possibilities. In either matching, deleting the \(r+2s\) forced arcs leaves an arbitrary noncrossing perfect matching on \(2(n-r-2s)\) ordered sites; the deletion/insertion bijection is valid even when selected windows are adjacent or nested inside an otherwise external arc. Thus each specified collection and orientation has probability \((C_{n-r-2s}/C_n)^2\), proving the displayed identity. If \(r+2s>n\), there are too many disjoint forced arcs and the corresponding falling factorial moment vanishes.

**2. Exact covariance and its sign.** Evaluating the moment identity at \((r,s)=(1,0),(0,1),(1,1)\) gives the stated means and, for \(n\ge3\),
\[
\mathbb E[X_nY_n]=2(2n-5)(2n-4)\left(\frac{C_{n-3}}{C_n}\right)^2.
\]
Substitution and cancellation yield the displayed rational covariance. Writing \(n=m+3\) makes the numerator polynomial \(10m^3+49m^2+56m+8\), strictly positive for every integer \(m\ge0\). The denominator is positive for \(n\ge3\), giving strict negative covariance.

**3. Uniform high mixed moments.** Let \(r,s\ge0\) and \(r+s\le K\sqrt n\) for any fixed \(K>0\). Set \(k=r+s\) and \(t=r+2s\). Uniformly over these indices, Stirling's formula for Catalan numbers and elementary falling-factorial expansion give
\[
\log\frac{C_{n-t}}{C_n}=-t\log4+O\!\left(\frac{t+1}{n}\right),
\]
\[
\log(2n-r-3s)_k=k\log(2n)
-\frac{k(r+3s)+k(k-1)/2}{2n}
+O\!\left(\frac{(r+s+1)^3}{n^2}\right).
\]
Consequently the *exact* factorial-moment formula implies the uniform asymptotic
\[
\mathbb E[(X_n)_r(Y_n)_s]
=(n/8)^r(n/64)^s
\exp\left[-\frac{3r^2+10rs+7s^2}{4n}+o(1)\right],
\]
where \(o(1)\to0\) uniformly for \(r+s\le K\sqrt n\). This includes the boundary cases \(r=0\) or \(s=0\).

**4. Joint Gaussian limit.** Apply the multidimensional Gao–Wormald high-factorial-moment criterion, specifically Theorem A.1 of Berzunza Ojeda, Holmgren and Janson, to \((X_n,Y_n)\), with mean normalizers \(\mu_{1n}=n/8\), \(\mu_{2n}=n/64\) and scales \(\sigma_{1n}=\sigma_{2n}=\sqrt n\). The required growth \(\sigma_{in}\ll\mu_{in}\ll\sigma_{in}^3\) holds. In the theorem's exponent, the coefficients \(-3/(4n)\), \(-5/(2n)\), \(-7/(4n)\) agree term by term with \(\frac12\sum_{i,j}(\Gamma_{ij}n-\delta_{ij}\mu_{in})k_ik_j/(\mu_{in}\mu_{jn})\) for the displayed matrix \(\Gamma\). The uniform expansion verifies the criterion, giving the claimed bivariate normal limit. The two exact mean formulas differ from the chosen centerings by \(O(1)\), so the centers are asymptotically equivalent at scale \(\sqrt n\). Taking the \((2,0),(0,2),(1,1)\) factorial moments also yields the stated limiting variances and covariance directly. The positive determinant establishes a nondegenerate limit.

## Verification
Run \(\texttt{python CHECK.py}\) in the directory containing the accompanying standalone checker. It recursively generates every Catalan noncrossing matching, exhaustively examines every ordered pair through \(n=7\) (\(184041\) pairs for \(n=7\)), and uses exact rational arithmetic to compare all feasible mixed falling-factorial moments through \(n=6\), a further nine mixed moments at \(n=7\), and the exact negative covariance formula where applicable. It reports 68 passing assertions. The infinite-size limit follows analytically from the uniform asymptotic and the cited multidimensional high-moment theorem; finite enumeration is not offered as proof of convergence.

## Relationship to prior work
Di Francesco, Golinelli and Guitter's 1996 preprint introduces the pair-of-arch-diagrams framework and its meander enumeration; the combinatorial representation is not new. Féray and Thévenin establish local convergence and a law of large numbers for the total number of components, not this joint fluctuation law. Janson and Thévenin prove central limit theorems for counts of **one fixed component shape** (including the two-site marginal) and in Section 5 explicitly list an extension to several shapes via mixed factorial moments as a direction whose details they had not checked. Their marginal central limit theorems neither identify the cross-covariance nor imply the present bivariate limit. The multidimensional factorial-moment theorem used here is due to Berzunza Ojeda, Holmgren and Janson; the specific mixed moments, covariance and resulting meandric-system specialization are the asserted contribution.

## Limitations
No result is claimed for all components of size four regardless of support, for arbitrary simultaneous families of shapes, or for fluctuations of the total loop count. This is a self-review rather than an independent audit. Historical priority may be affected by earlier or unindexed formulations of multitype meandric component statistics, although no such dominating statement was identified in the inspected literature.

## References
1. P. Di Francesco, O. Golinelli and E. Guitter, *Meanders and the Temperley–Lieb algebra*, arXiv:hep-th/9602025 (first posted 1996-02-06), https://arxiv.org/abs/hep-th/9602025.
2. V. Féray and P. Thévenin, *Components in meandric systems and the infinite noodle*, arXiv:2201.11572 (first posted 2022-01-27), https://arxiv.org/abs/2201.11572.
3. S. Janson and P. Thévenin, *Central limit theorem for components in meandric systems through high moments*, arXiv:2303.01900, *Combinatorics, Probability and Computing* 33 (2024), 597–610, https://doi.org/10.1017/S0963548324000117.
4. G. Berzunza Ojeda, C. Holmgren and S. Janson, *Fringe trees for random trees with given vertex degrees*, arXiv:2312.04243, Appendix A, Theorem A.1, https://arxiv.org/html/2312.04243v1.
