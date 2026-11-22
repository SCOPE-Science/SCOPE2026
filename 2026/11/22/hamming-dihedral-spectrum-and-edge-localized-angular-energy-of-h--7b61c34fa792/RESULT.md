# Hamming dihedral spectrum and edge-localized angular energy of hypercube Laplacian simplices

## Finding
Let \(d\ge2\), \(N=2^d\), and let \(Q_d\) be the ordinary binary \(d\)-cube graph, with vertex set \(\{0,1\}^d\). Put \(L=dI-A(Q_d)\) in its full standard Euclidean coordinate space and \(P_d=\operatorname{conv}\{Le_x:x\in\{0,1\}^d\}\subset\mathbf1^\perp\). This is an \((N-1)\)-simplex. For a ridge (an intersection of two facets) whose opposite vertices are Hamming distance \(h\), let \(\theta_{d,h}\in(0,\pi)\) be its **interior** Euclidean dihedral angle. Define the exact rational numbers
\[
 c_{d,h}=\frac1{2^d}\sum_{k=1}^d\frac1{4k^2}
 \sum_{j=\max(0,k-d+h)}^{\min(h,k)}(-1)^j\binom hj\binom{d-h}{k-j},
 \qquad a_d=c_{d,0},\qquad
 b_d=\frac1{2^d}\sum_{k=1}^d\frac{\binom dk}{16k^4}.
\]
Then the complete Euclidean ridge-angle spectrum is
\[
 \boxed{\cos\theta_{d,h}=-\frac{c_{d,h}}{a_d}},\qquad
 \boxed{\#\{\text{ridges of type }h\}=2^{d-1}\binom dh}\quad(1\le h\le d).
\]
For every \(d\), \(c_{d,0}>c_{d,1}>\cdots>c_{d,d}\), so these are exactly \(d\) distinct, strictly decreasing angle levels. For \(d\ge3\), the largest level is obtuse and the smallest is acute; at \(d=2\), all levels are acute.

There is a sharp global angular-energy identity:
\[
 \boxed{\sum_{\text{ridges }R}\cos^2\theta_R
     =2^{d-1}\left(\frac{b_d}{a_d^2}-1\right).}
\]
Its fraction supported **only on ridges whose opposite cube vertices are adjacent** is
\[
 \boxed{\rho_d=\frac{d\,(c_{d,1}/a_d)^2}{b_d/a_d^2-1}
         =1-O(d^{-1})\longrightarrow1.}
\]
In particular, those \(d2^{d-1}\) ridges out of \(\binom{2^d}2\) total carry asymptotically all squared non-right-angle energy. The average over a uniformly chosen ridge satisfies
\[
 \mathbb E\cos^2\theta_R=\frac{b_d/a_d^2-1}{2^d-1}
      =\frac4{d2^d}\left(1+O(d^{-1})\right).
\]
Finally the two extreme levels have sharply different scales:
\[
 \theta_{d,1}=\frac\pi2+\frac2d+O(d^{-2}),\qquad
 \theta_{d,d}=\frac\pi2-\frac{d^2(\log d)^2}{8\,2^d}(1+o(1)).
\]
All logarithms are natural. Angles are intrinsic to the affine span equipped with the metric inherited from \(\mathbb R^N\), not the generally nonisometric lattice-coordinate reduction of a graph Laplacian simplex.

## Assumptions and scope
The claims hold for **every integer** \(d\ge2\). Every facet is opposite exactly one graph vertex, and every unordered pair of distinct facets forms a ridge because \(P_d\) is a simplex. Hamming distance is computed between their opposite graph-vertex labels. The squared angular energy is \(\cos^2\theta_R\), measuring squared deviation in cosine from the right angle; it is not a sum of angle squares, a surface-area-weighted quantity, or a claim about sampled vertices of the cube itself. Only the final asymptotic estimates require \(d\to\infty\).

## Proof
**1. Facet normals.** The connected graph Laplacian has rank \(N-1\), kernel \(\mathbf1\) and \(\sum_xLe_x=0\). If a linear dependence \(\sum_x t_xLe_x=0\) also has \(\sum_x t_x=0\), then all \(t_x\) are equal and hence zero. Thus the \(N\) columns are affinely independent. Write \(L^\dagger\) for the Moore--Penrose inverse in the **original ambient Euclidean inner product**, and \(w_x=L^\dagger e_x\). The defining identity
\[
 w_x^{\mathsf T}Le_y=\delta_{xy}-\frac1N
\]
shows that the facet opposite \(Le_x\) lies on \(w_x\cdot z=-1/N\), with interior on the greater-than side. Hence its outward normal is \(-w_x\). Since \(L\) is symmetric, the Gram matrix of the \(w_x\) is \((L^\dagger)^2\), and the interior dihedral angle satisfies \(\cos\theta_{xy}=-\langle w_x,w_y\rangle/(\|w_x\|\|w_y\|)\).

**2. Exact spectrum and counts.** The Walsh characters \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\) diagonalize \(L\), with eigenvalue \(2|S|\). Therefore the matrix \((L^\dagger)^2\) has Walsh multiplier \(1/(4|S|^2)\) for \(S\ne\varnothing\), and zero multiplier for the trivial character. Fourier inversion yields precisely \(\langle w_x,w_y\rangle=c_{d,h}\) with \(h=\operatorname{Ham}(x,y)\). Its diagonal is the common positive value \(a_d\). Each nonzero binary difference of weight \(h\) occurs for \(N/2\) unordered pairs, giving the stated multiplicity.

**3. Strict ordering and signs.** Spectral integration gives
\[
 c_{d,h}=\int_0^\infty t\Biggl[
 \left(\frac{1+e^{-2t}}2\right)^{d-h}
 \left(\frac{1-e^{-2t}}2\right)^h-\frac1N\Biggr]dt.
\]
For each \(t>0\), the first product decreases strictly with \(h\), so its integral does too. At maximal separation, the alternating binomial identity gives
\[
 c_{d,d}=-\frac{H_d^2+H_d^{(2)}}{8N}<0,
 \quad H_d=\sum_{k=1}^d\frac1k,\quad
 H_d^{(2)}=\sum_{k=1}^d\frac1{k^2}.
\]
At separation one, expanding in the first coordinate gives
\[
 4Nc_{d,1}=-1+\sum_{k=1}^{d-1}\binom{d-1}{k}
 \left(\frac1{k^2}-\frac1{(k+1)^2}\right).
\]
For \(d\ge3\), its \(k=1\) term alone is \(3(d-1)/4>1\), so \(c_{d,1}>0\). At \(d=2\), direct substitution gives \(c_{2,1}=-1/64\), and monotonicity makes both levels acute.

**4. Exact angular-energy identity.** Parseval for the normalized Walsh transform states
\[
 \sum_{z\in\{0,1\}^d}c_{d,\operatorname{wt}(z)}^2
 =\frac1N\sum_{k=1}^d\binom dk\frac1{16k^4}=b_d.
\]
The zero-difference term equals \(a_d^2\). Division by \(a_d^2\), and multiplication by \(N/2\) to count unordered facet pairs, proves the exact ridge sum. Its weight-one contribution is \((N/2)d(c_{d,1}/a_d)^2\), giving \(\rho_d\) and the exact uniform-ridge average.

**5. Controlled asymptotics.** If \(K\sim\operatorname{Bin}(d,1/2)\), and the integrands are set to zero at \(K=0\), then
\[
 a_d=\mathbb E\frac{\mathbf1_{K>0}}{4K^2},\quad
 b_d=\mathbb E\frac{\mathbf1_{K>0}}{16K^4},\quad
 c_{d,1}=\mathbb E\frac{\mathbf1_{K>0}}{4K^2}\left(1-\frac{2K}{d}\right).
\]
On \(|K-d/2|\le d/4\), Taylor expansion in \(\delta=K-d/2\), with \(\mathbb E\delta=0\), \(\mathbb E\delta^2=d/4\), and binomial fourth moments \(O(d^2)\), gives
\[
 a_d=d^{-2}\bigl(1+3d^{-1}+O(d^{-2})\bigr),\quad
 b_d=d^{-4}\bigl(1+10d^{-1}+O(d^{-2})\bigr),\quad
 c_{d,1}=2d^{-3}\bigl(1+O(d^{-1})\bigr).
\]
To justify termwise expansion, use the fourth-order Taylor remainder together with the binomial central moments and \(\Pr(|K-d/2|>d/4)\le2e^{-d/24}\). Since the cut-off integrands are at most polynomially large on the tails, the omitted contribution is exponentially small. Odd central moments of this symmetric binomial vanish, and the next nonvanishing remainder is \(O(d^{-2})\) relative in the first two estimates. Consequently \(b_d/a_d^2-1=4/d+O(d^{-2})\) and \(c_{d,1}/a_d=2/d+O(d^{-2})\). Substitution yields the asserted angular-energy concentration and mean.

Finally \(H_d=\log d+\gamma+o(1)\), \(H_d^{(2)}\to\pi^2/6\), so the exact antipodal formula and \(a_d\sim d^{-2}\) imply \(-c_{d,d}/a_d\sim d^2(\log d)^2/(8N)\). Using \(\arccos(\pm x)=\pi/2\mp x+O(x^3)\) at \(x\to0\) proves both extreme-angle expansions. This completes all integer-dimensional and asymptotic claims.

## Verification
The standalone standard-library script `checker.py` reconstructs all rational Walsh coefficients for \(2\le d\le18\), verifies strict radial monotonicity, harmonic antipodal values, all shell counts and the Parseval angular-energy identity. Independently for \(2\le d\le4\), it builds the full physical cube graph Laplacian and computes rational matrix inverses, verifying both the barycentric facet normals and every corresponding Gram entry without using the Walsh formula. Large-d numerical diagnostics at \(d=50,100,200\) check the approach to the analytic constants; these are illustrative and **not** a proof of any infinite-dimensional claim. Run with `python checker.py` from the extracted file directory.

## Relationship to prior work
Braun and Meyer introduced the graph Laplacian simplex and examined its lattice/Ehrhart properties, including trees, cycles and complete graphs; this is the original definition used here, in its explicitly specified full-column Euclidean realization. Juhnke-Kubitzke and Köhne generalized Laplacian polytopes to simplicial complexes and analyzed simplex boundaries, not this hypercube metric angle-energy law. Publicly indexed prior work on angular recognition of weighted-graph Laplacian simplices establishes general inverse reconstruction from a known facet-angle matrix; work on cycle and matching-deleted graph Laplacian simplices establishes different particular angle spectra. None of the specifically inspected, accessible materials supplies the exact hypercube Hamming angle stratification together with its angular-energy localization. Reconstruction theory alone does not state the limiting fraction on Hamming-one ridges. The standard Walsh diagonalization and Parseval identity are classical tools and are not claimed as new.

## Limitations
This is a self-review, not independent verification or a historical-priority certificate. The result concerns this canonical graph-Laplacian realization, not arbitrary affine images or orientation-dependent higher simplicial-complex Laplacian column polytopes. The energy is an **unweighted sum over ridges** of squared cosines; area-weighted curvature, full normal-cone solid angles, and a precise formula for the number of acute ridges are not claimed. A potentially relevant publicly indexed graph-reconstruction study was available as a title and summary, but its complete primary text could not be retrieved; that is a residual priority risk. Exact finite computations support rather than replace the proof.

## References
- B. Braun and M. Meyer, *Laplacian Simplices*, arXiv:1706.07085, first public version 2017-06-21. https://arxiv.org/abs/1706.07085
- M. Juhnke-Kubitzke and D. Köhne, *Laplacian polytopes of simplicial complexes*, arXiv:2301.11602, first public version 2023-01-27. https://arxiv.org/abs/2301.11602
- *Angular recognition and weighted-graph reconstruction for Laplacian-column simplices*, publicly indexed mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-angular-recognition-and-weighted-graph-reconstruction-for-laplac--49d3b46853da (only record summary accessible during comparison).
- *Complete Euclidean dihedral-angle spectrum and sharp acute–obtuse transition of cycle Laplacian simplices*, publicly indexed mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-complete-euclidean-dihedral-angle-spectrum-and-sharp-acute-obtus--e78a2f0afa5f (summary used for topic comparison).
