# Exact three-cell Fourier observability and its half-occupancy transition

## Finding
Let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), partitioned into the three half-open cells \(I_j=[2\pi j/3,2\pi(j+1)/3)\), \(j=0,1,2\). Fix \(0<\gamma<1\). Let \(E\subset\mathbb T\) be measurable with \(|E\cap I_j|\ge 2\pi\gamma/3\) for every \(j\). Put
\[
 h=\min\{\gamma,1-\gamma\},\qquad
 \mathcal F(\gamma)=2\sin\left(\frac{\pi h}{3}\right)
 \left[1+2\cos\left(\frac\pi3+\frac{\pi h}{3}\right)\right].
\]
For every integer \(n\) and every complex \(a,b\),
\[
 \int_E\left|ae^{int}+be^{i(n+1)t}\right|^2\frac{dt}{2\pi}
 \ge \left(\gamma-\frac{\mathcal F(\gamma)}{2\pi}\right)(|a|^2+|b|^2).
\]
The constant is positive and sharp for every \(\gamma\). For sets with **exactly** \(|E\cap I_j|=2\pi\gamma/3\) in each cell, the two eigenvalues of the restriction Gram matrix are \(\gamma\pm |Z(E)|/(2\pi)\), where \(Z(E)=\int_Ee^{it}\,dt\), and its sharp possible spectral envelope is \(\gamma\pm\mathcal F(\gamma)/(2\pi)\).

The equality masks undergo a sharp change at \(\gamma=1/2\). Write \(L=2\pi/3\), \(l=L\gamma\), and \(E_\gamma=[L/2-l/2,L/2+l/2]\cup[L,L+l]\cup[3L-l,3L]\), modulo endpoints. For \(0<\gamma<1/2\), the only masks attaining the optimal moment magnitude are the three rotations \(E_\gamma+2\pi j/3\), \(j=0,1,2\). For \(1/2<\gamma<1\), the only ones are the complements of the three rotations of \(E_{1-\gamma}\). At \(\gamma=1/2\), by contrast, there is a continuous circle of distinct maximizing masks, parametrized by the direction \(\phi\in\mathbb T\) of \(Z(E)\): in each cell take, uniquely up to null sets, the length-\(\pi/3\) subset on which \(\cos(t-\phi)\) is largest. Every one of these masks has \(|Z(E)|=1\), and these are all maximizers. For any equality mask, the bound is achieved by the normalized negative-eigenvalue Fourier combination; for instance, when \(Z(E)=\mathcal F(\gamma)e^{i\phi}\), choose \((a,b)=(1,-e^{-i\phi})\).

## Assumptions and scope
The circle has unnormalized arc length \(dt\) when defining \(Z\) and normalized Haar measure \(dt/(2\pi)\) in the energy inequality. Every cell is fixed, not free to rotate independently. No regularity or connected-component restriction is imposed on \(E\). Endpoint membership is immaterial. Only **adjacent** frequency characters are considered; changing their common integer frequency does not change the Gram matrix. The density hypothesis is cellwise, not the stronger moving-window thickness condition. The equality-mask classification is for exact cell masses, which equality in the at-least-density inequality necessarily forces for a nonzero two-mode polynomial.

## Proof
**1. Spectral reduction and the occupancy constraint.** If each cell has exactly prescribed mass, \(|E|=2\pi\gamma\), the restriction Gram matrix in the orthonormal Fourier basis is
\[
 G_E=\begin{pmatrix}\gamma&Z(E)/(2\pi)\\\overline{Z(E)}/(2\pi)&\gamma\end{pmatrix}
\]
(up to conjugate placement), with eigenvalues \(\gamma\pm |Z(E)|/(2\pi)\). Thus the sharp lower energy ratio is equivalent to finding the largest \(|Z(E)|\) with these three individual mass constraints. If \(E\) has excess mass in a cell, choose a measurable subset \(E'\subset E\) with the prescribed mass in each cell (nonatomicity of arc length). Since the integrand is nonnegative, \(\int_E|p|^2\ge\int_{E'}|p|^2\), giving the inequality also under the three lower bounds. For any nonzero two-frequency polynomial the zero set has measure zero, so equality forces \(|E\setminus E'|=0\).

**2. Duality and complement symmetry.** For exact cell masses,
\[
 \sup_E|Z(E)|=\max_{\phi\in\mathbb T}\ \sup_E\int_E\cos(t-\phi)\,dt.
\]
The inner optimization is a separate bathtub rearrangement on each cell: select the prescribed length \(l=L\gamma\) where \(\cos(t-\phi)\) is greatest. Strict monotonicity of cosine with circular distance gives a unique selected subset up to null sets, for each fixed \(\phi\). Replacing \(E\) with its complement replaces \(\gamma\) by \(1-\gamma\) and \(Z(E)\) by \(-Z(E)\). It therefore suffices to treat \(0<\gamma\le1/2\).

**3. Exact three-cell support function.** Threefold rotation and reflection reduce the phase to \(0\le\phi\le L/2\). Now \(0<l\le L/2\). In the third cell \([2L,3L]\), the optimal set is always \([3L-l,3L]\). When \(0\le\phi\le l/2\), the optimal pieces in the first two cells are
\[
 [0,l],\qquad [L,L+l/2+\phi]\ \cup\ [2L-l/2+\phi,2L].
\]
Direct integration yields
\[
 H(\phi)=2\sin(L+l/2)+2(\sin l-\sin L)\cos\phi.
\]
Because \(\sin l\le\sin L\), this is nondecreasing in \(\phi\), strictly increasing in the interior when \(l<L/2\).

When \(l/2\le\phi\le L/2\), the optimal pieces in the first two cells are
\[
 [\phi-l/2,\phi+l/2],\qquad [L,L+l],
\]
with the same third-cell piece. Their integrated cosine is
\[
 H(\phi)=2\sin(l/2)\left[1+2\cos((L+l)/2)\cos(\phi-L/2)\right].
\]
Here \(0<(L+l)/2\le\pi/2\), so this is again nondecreasing, strictly increasing in the interior for \(l<L/2\). Hence its global maximum is uniquely at \(\phi=L/2\) modulo the threefold symmetry if \(\gamma<1/2\). Substituting \(l=L\gamma\) gives
\[
 H(L/2)=2\sin(l/2)\,[1+2\cos(L/2+l/2)]=\mathcal F(\gamma).
\]
At \(\gamma=1/2\), the first branch has \(\sin l=\sin L\), while the second has \(\cos((L+l)/2)=0\). Thus \(H(\phi)=1\) for every phase. The unique fixed-phase bathtub masks are then all global maximizers, and, because their real projection in their chosen phase is \(1\) while their moment modulus cannot exceed \(1\), their Fourier moment has exactly that phase. Distinct phases give distinct masks up to null sets. Complementation gives the full high-density classification.

**4. Saturation and strict positivity.** At \(\phi=L/2\) the selected sets are precisely \(E_\gamma\) in the statement; they realize \(|Z|=\mathcal F(\gamma)\). Complementation gives equality at high density; the two-by-two eigenvector realizes the spectral minimum. The lower constant is strictly positive: every admissible exact-mass mask has positive measure, and a nonzero two-mode trigonometric polynomial has only finitely many zeros, so \(G_E\) is positive definite. The maximum of \(|Z|\) is attained by the explicit masks, hence \(\mathcal F(\gamma)<2\pi\gamma\) for each fixed \(\gamma>0\). This completes the sharp proof for every \(0<\gamma<1\).

## Verification
The standard-library Python file `check_threecell.py` verifies the two exact support-function formulas against independently integrated optimal cell pieces, the stated optimizer moment and complement symmetry, the Gram eigenvalue normalization, strict numerical positivity, half-occupancy flatness in 101 sampled phases, and fixed-phase finite-grid rearrangement comparisons. Executed directly from this package, it reports `PASS 4145 supplementary assertions`. Finite checks are diagnostic only; the exact global rearrangement and uniqueness proof above supplies the continuum result.

## Relationship to prior work
Saucedo and Tikhonov (arXiv:2603.21950v1, first public March 23, 2026) prove a qualitative Logvinenko–Sereda inequality for functions with lacunary bands on the real line and thick observation sets. It does not optimize a fixed three-cell circular mask or give this exact two-mode constant. Abreu and Speckbacher (arXiv:2607.19192v1, first public July 21, 2026), particularly their circle concentration theorem, show that a single arc is extremal among all sets of a given **total** mass. Such an arc generally violates the imposed three separate occupancy constraints; the global one-arc bound does not imply the sharp constrained value or its half-occupancy equality locus.

The published result *Sharp phase-centred stability and bang–bang rigidity for two-mode circle concentration* (2026) gives an exact deficit in terms of mass exchanged from a phase-centred arc, for masks constrained only by total mass; its two-cap equality geometries are not the three independently constrained cellwise rearrangements here. The published result *Rigidity and exact inverse conditioning for perfectly balanced Fourier sampling on circular arc unions* (2026) determines isometric configurations and a local endpoint Jacobian for unions of circular arcs, not a sharp **worst** lower bound over arbitrary measurable per-cell-density masks. Likewise, results on two prescribed arcs for three modes do not imply the present three-cell, two-mode constrained extremum. The proof here is elementary and does not assert a new general rearrangement principle.

## Limitations
The sharp formula is specific to three equal fixed cells, equal local minimum density and two adjacent Fourier characters. For more harmonics, unequal cell masses, a moving-window thickness condition or fractional observation weights, no analogous formula is claimed. Priority is conditional on inspected sources: an older equivalent stratified rearrangement or Fourier-moment calculation may exist outside the located literature. The finite checker does not independently establish the continuous theorem, and no independent mathematical audit is claimed.

## References
1. M. Saucedo and S. Tikhonov, *A Logvinenko–Sereda theorem for lacunary spectra*, arXiv:2603.21950v1 (2026-03-23), Sections 1–3. https://arxiv.org/html/2603.21950v1
2. L. D. Abreu and M. Speckbacher, *Optimal concentration in the Paley–Wiener space*, arXiv:2607.19192v1 (2026-07-21), Section 2 and its circle concentration theorem. https://arxiv.org/html/2607.19192v1
3. *Sharp phase-centred stability and bang–bang rigidity for two-mode circle concentration* (2026), full result and proof. https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-sharp-phase-centred-stability-and-bang-bang-rigidity-for-two-mod--1d3091d9c873/RESULT.md
4. *Rigidity and exact inverse conditioning for perfectly balanced Fourier sampling on circular arc unions* (2026), full result and proof. https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-rigidity-and-exact-inverse-conditioning-for-perfectly-balanced-f--a288ba0aa91c/RESULT.md
