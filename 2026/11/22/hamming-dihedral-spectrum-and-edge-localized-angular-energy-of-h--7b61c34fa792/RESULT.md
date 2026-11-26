# Edge localization and extreme scales of dihedral-angle deviations in hypercube Laplacian simplices

## Finding

Let \(d\ge2\) be an integer, \(N=2^d\), and \(L=dI-A(Q_d)\) be the graph Laplacian of the ordinary binary cube. Give the column simplex \(P_d=\operatorname{conv}\{Le_x:x\in\{0,1\}^d\}\) the Euclidean metric inherited from its full coordinate space. For a ridge \(R\), let \(\theta_R\) be its **interior** dihedral angle, and call it a Hamming-one ridge if the two vertices opposite its defining facets are adjacent in \(Q_d\).

The Hamming-one ridges carry asymptotically all the unweighted squared-cosine energy. Precisely,
\[
 \frac{\sum_{R:\,\text{Hamming-one}}\cos^2\theta_R}{\sum_R\cos^2\theta_R}
 =1-O(d^{-1}),\qquad
 \frac{1}{\binom{N}{2}}\sum_R\cos^2\theta_R
 =\frac{4}{d\,2^d}\bigl(1+O(d^{-1})\bigr).
\]
Only \(d/(2^d-1)\) of all ridges are Hamming-one. The angle levels strictly decrease with the Hamming distance \(h\) between opposite labels. The two extreme levels, at \(h=1\) and \(h=d\), satisfy
\[
 \theta_{d,1}=\frac{\pi}{2}+\frac2d+O(d^{-2}),\qquad
 \theta_{d,d}=\frac{\pi}{2}-\frac{d^2(\log d)^2}{8\,2^d}(1+o(1)).
\]
Thus local and antipodal angles have different scales of departure from a right angle. All logarithms are natural.

The exact pairwise angle formula is **not** claimed as a new spectrum calculation. As described below, it follows from the known cube biharmonic distance and the general simplex angle relation. The results here quantify energy localization and extreme-angle deviations using this kernel.

## Scope

All angle comparisons are in the original metric on \(\mathbf1^\perp\); arbitrary lattice-coordinate reductions need not preserve them. The energy is a sum of squared cosines, with each ridge counted once and no weights from facet or ridge areas. Only the limit statements require \(d\to\infty\).

## Proof

**1. Starting identities.** Because \(Q_d\) is connected, the kernel of \(L\) is exactly \(\mathbb R\mathbf1\). Its columns are therefore affinely independent: a linear dependence with coefficients summing to zero lies in the kernel and must vanish. Thus unordered pairs of distinct opposite vertices index the ridges of this \((N-1)\)-simplex. For each \(x\), put \(w_x=L^\dagger e_x\). The defining identity
\[
 w_x\cdot Le_y=\delta_{xy}-1/N
\]
makes \(-w_x\) an outward normal of the facet opposite \(Le_x\). Let \(c_{d,h}=((L^\dagger)^2)_{xy}\) when \(x,y\) have Hamming distance \(h\), and \(a_d=c_{d,0}\). The interior angle then obeys \(\cos\theta_{d,h}=-c_{d,h}/a_d\). This is also Devriendt's general simplex angle relation applied to vertex Gram matrix \(L^2\).

The squared cube biharmonic distance with orthonormal Fourier conventions is \(D(x,y)=\|L^\dagger(e_x-e_y)\|^2=2(a_d-c_{d,h})\). Since \(\sum_y((L^\dagger)^2)_{xy}=0\), the angle formula can also be written
\[
 \cos\theta_{d,h}=-1+\frac{D(x,y)}{N^{-1}\sum_{z}D(x,z)}.
\]
Any global Fourier normalization factor in the biharmonic distance cancels in this expression. Wei, Li and Yang give its cube Walsh sum in Corollary 5.6 of arXiv:2110.02656v2. For clarity, in our normalization the input kernel is
\[
 c_{d,h}=\frac1N\sum_{k=1}^d\frac1{4k^2}
  \sum_{j=\max(0,k-d+h)}^{\min(h,k)}(-1)^j\binom hj\binom{d-h}{k-j}.
\]
Indeed the Walsh mode indexed by a subset \(S\) has Laplacian eigenvalue \(2|S|\) and multiplier \(1/(4|S|^2)\) for \((L^\dagger)^2\), with multiplier zero at the trivial mode. Counting the subsets of size \(k\) by the size \(j\) of their intersection with the differing coordinates gives the displayed form. There are \(N\binom dh/2\) ridges of level \(h\): each nonzero difference of weight \(h\) occurs in \(N/2\) unordered pairs.

**2. Strict order and the antipodal entry.** Using \(1/\lambda^2=\int_0^\infty t e^{-\lambda t}\,dt\) and the product cube heat kernel,
\[
 c_{d,h}=\int_0^\infty t\left[
 \left(\frac{1+e^{-2t}}2\right)^{d-h}
 \left(\frac{1-e^{-2t}}2\right)^h-\frac1N\right] dt.
\]
The subtraction removes the constant mode, so the integral converges. For every \(t>0\) the product strictly decreases in \(h\). Thus \(c_{d,h}\) and the interior angle \(\arccos(-c_{d,h}/a_d)\) strictly decrease with \(h\). At \(h=d\), compare the coefficient of \(u\) near \(u=0\) in
\[
 \int_0^1 x^{u-1}(1-x)^d\,dx
 =\frac1u+\sum_{k=1}^d \frac{(-1)^k\binom dk}{u+k}
 =\frac1u\prod_{k=1}^d(1+u/k)^{-1}.
\]
The product equality follows by integration by parts for \(u>0\) and then expansion at zero. With \(H_d=\sum_{k=1}^d k^{-1}\) and \(H_d^{(2)}=\sum_{k=1}^d k^{-2}\), the coefficient gives
\[
 c_{d,d}=-\frac{H_d^2+H_d^{(2)}}{8N}.
\]
In particular the antipodal level is acute. The weight-one entry satisfies
\[
 4Nc_{d,1}=-1+\sum_{k=1}^{d-1}\binom{d-1}{k}\left(k^{-2}-(k+1)^{-2}\right).
\]
Its first summand after \(-1\) is \(3(d-1)/4>1\) when \(d\ge3\), so the highest level is then obtuse. At \(d=2\), \(c_{2,1}=-1/64\) and both levels are acute.

**3. Energy and localization.** Put \(b_d=N^{-1}\sum_{k=1}^d\binom dk/(16k^4)\). Parseval gives \(\sum_{h=0}^d\binom dh c_{d,h}^2=b_d\); the \(h=0\) term is \(a_d^2\). Consequently the exact normalized energy and its Hamming-one share are
\[
 \sum_R\cos^2\theta_R=\frac N2\left(\frac{b_d}{a_d^2}-1\right),\qquad
 \rho_d=\frac{d(c_{d,1}/a_d)^2}{b_d/a_d^2-1}.
\]
The denominator is positive since \(c_{d,d}<0\). These identities are algebraic consequences of the input kernel; the task is to identify their asymptotic sizes.

Let \(K\sim\operatorname{Bin}(d,1/2)\), \(X=(2K-d)/d\), and set the integrands to zero at \(K=0\). After factoring out \(d^{-2},d^{-4},d^{-2}\), the expectations for \(a_d,b_d,c_{d,1}\), respectively, are those of \((1+X)^{-2},(1+X)^{-4},-X(1+X)^{-2}\). For the last identity the average Walsh sign of a fixed coordinate at fixed weight \(K\) is \(1-2K/d\). We have \(\mathbb E X=\mathbb E X^3=0\), \(\mathbb E X^2=1/d\), and \(\mathbb E X^4=(3d^2-2d)/d^4\); the latter follows by expanding a fourth power of a sum of independent fair signs. On \(|X|\le1/2\), the cubic Taylor polynomials have uniform remainders \(O(X^4)\). The first two polynomials have quadratic coefficients 3 and 10, while the last starts with \(-X+2X^2\). On \(|X|>1/2\), the probability is at most \(2e^{-d/8}\) by the binomial Hoeffding bound, and the cut-off integrands for \(K>0\) grow at most polynomially in \(d\). Thus the contributions from this tail, and the differences between full and truncated moments, are exponentially small up to polynomial factors. This proves
\[
 a_d=d^{-2}(1+3/d+O(d^{-2})),\quad b_d=d^{-4}(1+10/d+O(d^{-2})),\quad
 c_{d,1}=d^{-2}(2/d+O(d^{-2})).
\]
Hence \(b_d/a_d^2-1=4/d+O(d^{-2})\) and \(d(c_{d,1}/a_d)^2=4/d+O(d^{-2})\). Their ratio is within \(O(d^{-1})\) of one and cannot exceed one. Dividing the total by \(\binom N2\) gives the stated mean.

**4. Extreme scales.** From the preceding expansion \(c_{d,1}/a_d=2/d+O(d^{-2})\). At the antipode \(-c_{d,d}/a_d\sim d^2(\log d)^2/(8N)\), since \(H_d\sim\log d\) and \(H_d^{(2)}\) is bounded. Expanding \(\arccos v=\pi/2-v+O(v^3)\) at zero gives the claimed expansions and their signs.

## Reproducibility

The companion `radial_inverse_check.py` solves two exact radial Poisson equations for the inverse-square Laplacian without obtaining the solution by diagonalization. It compares every entry and checks the order, signs, harmonic antipodal formula and Parseval normalization for \(2\le d\le30\). The finite range corroborates the identities and conventions; the proof, not the script, establishes the all-dimension order and asymptotic results.

## Relationship to prior work and limitations

Braun and Meyer introduced the Laplacian simplex and studied its lattice properties. For our Euclidean realization the general normalized inverse-Gram angle formula is prior (Devriendt, §2.2, Property 1); the exact cube input is prior as the biharmonic distance (Wei–Li–Yang, §5.3, Corollary 5.6). The earlier *Angular recognition and weighted-graph reconstruction for Laplacian-column simplices* also uses the normalized inverse-square Laplacian to characterize and reconstruct weighted graph column simplices. Neither exact angle extraction from these sources nor the standard cube mode counts or Parseval are new claims here. Angle spectra for cycles and matching-deleted complete graphs concern different graph families. The quantitative result is that essentially all squared-cosine energy lies on an exponentially small fraction of ridges, with explicit scales both for the mean and for local and antipodal deviations. Historical priority for the quantitative asymptotics remains qualified by the scope of available literature. This does not give area-weighted localization, solid-angle information, or an exact count of acute ridges.

## References

- B. Braun and M. Meyer, *Laplacian Simplices*, [arXiv:1706.07085](https://arxiv.org/abs/1706.07085), §3.1.
- K. Devriendt, *Effective resistance is more than distance: Laplacians, simplices and the Schur complement*, [arXiv:2010.04521](https://arxiv.org/abs/2010.04521), §2.2, Property 1.
- Y. Wei, R. Li, W. Yang, *Biharmonic distance of graphs*, [arXiv:2110.02656v2](https://arxiv.org/abs/2110.02656v2), §5.3, Corollary 5.6.
- [*Angular recognition and weighted-graph reconstruction for Laplacian-column simplices*](https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-angular-recognition-and-weighted-graph-reconstruction-for-laplac--49d3b46853da), Finding and Proof.
- [*Complete Euclidean dihedral-angle spectrum and sharp acute–obtuse transition of cycle Laplacian simplices*](https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-complete-euclidean-dihedral-angle-spectrum-and-sharp-acute-obtus--e78a2f0afa5f), Finding.
- [*An angular fingerprint and a two-scale dihedral law for matching-deleted Laplacian simplices*](https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-an-angular-fingerprint-and-a-two-scale-dihedral-law-for-matching--aea66d1fe696), Finding.
