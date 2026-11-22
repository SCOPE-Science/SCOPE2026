# Reentrant real spectra and a tunable third-order exceptional point in a triangle-closed quantum star

## Finding
For each integer \(m\geq3\), a unit-spoke quantum star with a real hopping link between its two balanced gain/loss leaves has a nonempty interval of closing-link strengths with **three distinct positive exceptional-point thresholds** in gain/loss magnitude. The spectrum is entirely real at low gain/loss, becomes nonreal, returns to an entirely real window, and ultimately becomes nonreal again. For every \(m\ge3\), another exact choice of the link strength creates a genuine third-order exceptional point at nonzero energy and positive gain/loss.

Let \(k=m-2\), and set
\[
y_k=-k+\sqrt{\frac{k(4k+2)}3},\qquad t_*(k)=4y_k^{3/2}.\]
Here \(0<y_k<k\). For every
\[
\boxed{\sqrt{k}<t<\min\{t_*(k),\sqrt{k+1}\}},
\]
there are exactly three positive, pairwise different gain/loss thresholds \(0<\gamma_1<\gamma_2<\gamma_3\). The entire spectrum is real for \(0\le\gamma<\gamma_1\) and for \(\gamma_2<\gamma<\gamma_3\). Exactly one complex-conjugate pair occurs for \(\gamma_1<\gamma<\gamma_2\) and for \(\gamma>\gamma_3\). Each threshold is an order-two defective eigenvalue. At
\[
\boxed{t=t_*(k),\quad \gamma=\gamma_*(k)=\sqrt{16y_k^3+k+2-6y_k},}
\]
there is instead a genuine order-three exceptional point at energy \(-\sqrt{y_k}\). The other bright energy is \(3\sqrt{y_k}\). The \(m-3\) dark eigenvalues, if present, remain at zero.

## Assumptions and scope
The Hamiltonian \(H\) is the \((m+1)\times(m+1)\) complex-symmetric matrix indexed by two marked leaves \(a,b\), a hub \(h\), and \(k=m-2\) additional neutral leaves. It has \(H_{aa}=i\gamma\), \(H_{bb}=-i\gamma\), \(H_{ab}=H_{ba}=t>0\), \(H_{hj}=H_{jh}=1\) for every leaf \(j\), and every other entry zero. Here \(m\ge3\) is an integer and \(\gamma\ge0\) is real. Parity swaps the two marked leaves and fixes the hub and other leaves; complex conjugation acts as time reversal. This is a non-Hermitian single-excitation Hamiltonian, not a Lindblad generator. A spectrum is called *entirely real* if all algebraic eigenvalues are real, whether or not the matrix is diagonalizable at a boundary.

## Proof
**Symmetry reduction.** The normalized sum of the \(k\) neutral leaves couples to the hub with amplitude \(\sqrt{k}\). Its orthogonal complement is an \((m-3)\)-dimensional zero-energy dark space. In the basis of marked leaves, hub and normalized neutral sum, the bright matrix is
\[
B=\begin{pmatrix}i\gamma&t&1&0\\t&-i\gamma&1&0\\1&1&0&\sqrt{k}\\0&0&\sqrt{k}&0\end{pmatrix}.
\]
A determinant expansion gives the full characteristic polynomial
\[
\det(xI-H)=x^{m-3}P(x),\qquad
P(x)=x^4+(\gamma^2-t^2-k-2)x^2-2tx+k(t^2-\gamma^2).
\]
In particular its cubic coefficient vanishes and its linear coefficient is strictly negative.

**Exhaustion of the repeated roots.** Every nonreal root of a real quartic has its conjugate. If the quartic had a repeated nonreal root, the conjugate would also be repeated, so it would be the square of a real quadratic. Vanishing cubic coefficient would then force its linear coefficient to vanish, contradicting \(-2t\ne0\). Thus all multiple bright roots are real. Eliminating \(\gamma^2\) from \(P(-u)=P'(-u)=0\), with \(u>0\), gives
\[
t=T_k(u):=\frac{u[(u^2-k)^2+2k]}{u^2+k},\qquad
\gamma^2=G_k(u):=\frac{u^2(u^2-k-1)^2[(u^2-k)^2+2k+2u^2]}{(u^2+k)^2}.
\]
The same elimination with a positive repeated root forces \(t<0\), so it is excluded. Every \(u>0\) satisfying \(t=T_k(u)\) and \(\gamma^2=G_k(u)\) conversely produces a repeated root. Further, \(G_k(u)>0\) except when \(u^2=k+1\), at which point \(t=\sqrt{k+1}\).

**Three crossings and reentrance.** Direct differentiation gives
\[
T_k'(u)=\frac{(u^2-k)[3u^4+6ku^2-k(k+2)]}{(u^2+k)^2}.
\]
Its positive stationary points are \(\sqrt{y_k}\) (a strict local maximum) and \(\sqrt{k}\) (a strict local minimum). They have heights \(4y_k^{3/2}\) and \(\sqrt{k}\), respectively. Therefore every \(t\) in the displayed open interval is attained at precisely three positive points \(u\), one on each monotonic branch. The corresponding \(\gamma^2\) values are positive. They are pairwise distinct: if two negative double roots occurred at the same gain, \(P\) would be a product of two squared negative-root factors and have a nonzero cubic coefficient. At each of the three crossings \(P''(-u)\ne0\) (the stationary-root condition is exactly \(t=4u^3\)), and \(\partial P(-u)/\partial(\gamma^2)=u^2-k\ne0\). Thus each is a transverse square-root collision between two real roots and a nonreal conjugate pair. At \(\gamma=0\), the Hamiltonian is Hermitian with four simple bright eigenvalues in this parameter interval. For large \(\gamma\), there are two real bright roots approaching \(\pm\sqrt{k}\), and one nonreal pair asymptotic to \(\pm i\gamma\). As exactly three transverse collisions occur, the real-root count alternates \(4,2,4,2\), giving the claimed windows. The zero-energy dark modes are always real.

**Third-order point and defectiveness.** At a triple bright root \(-u\), the additional condition \(P''(-u)=0\) gives \(t=4u^3\). Substituting into the double-root parameterization yields
\[
3u^4+6ku^2-k(k+2)=0,
\]
whose unique positive solution is \(u^2=y_k\). With the claimed \(t_*,\gamma_*\), direct substitution gives
\[
P(x)=(x+\sqrt{y_k})^3(x-3\sqrt{y_k}).
\]
The triple root is not quadruple because \(P^{(3)}(-\sqrt{y_k})\ne0\). Every repeated negative bright root at strictly positive \(\gamma\) is defective: the three-by-three minor of \(B+uI\) indexed by the two marked leaves and the neutral collective mode equals
\[
u(u^2+\gamma^2-t^2)=-\frac{2u^3(u^2-k-1)}{u^2+k}\ne0.
\]
Hence its eigenspace has dimension one. At the triple point its unique Jordan block has size three, which proves an actual exceptional point rather than merely an eigenvalue coincidence. The dark subspace has energy zero and does not affect the nonzero triple root.

## Verification
The standalone script `verify_symbolic.py` uses exact SymPy arithmetic to check elimination, the factorization at the order-three point, the derivative identity, and the complete Hamiltonian characteristic polynomial for leaf counts three through seven. The independent `verify_numeric.py` constructs the entire matrix directly for leaf counts three through sixteen, checks the four alternating spectral regimes and confirms the one-dimensional kernel of the triple-root eigenspace. Both scripts can be run from the package directory with Python, SymPy, NumPy and SciPy. Finite checks supplement, but do not replace, the all-size algebraic proof.

## Relationship to prior work
Duanmu et al. (2012, arXiv:1210.3871v1) study parity-time-symmetric two- and three-site oligomers, not a closed triangle with arbitrarily many neutral pendant leaves. Downing and Saroka (2021, DOI below) analyze open chains and next-nearest-neighbor trimer couplings, including a previously known **reentrant real-spectrum interval in a triangle trimer**. That pre-existing phenomenon is expressly not claimed as new. The present claim instead concerns the exact all-size three-positive-threshold law after attaching neutral pendants, and the exceptional point of order three at a nonzero triangle-closing link strength. The general matrix approach is standard; explicit priority for this particular family is provisional.

## Limitations
The result requires one hub, identical unit real spokes, a single real closing link connecting the two marked gain/loss leaves, and strictly balanced onsite imaginary potentials. The reentrant interval stated here is a sufficient complete three-threshold interval, not a classification of every link strength outside it. Eigenvalue reality does not imply bounded time evolution at exceptional points. There is no assertion for disorder, many-particle quantum dynamics, noisy physical implementation or historical uniqueness. Independent verification and a definitive priority determination have not been performed.

## References
1. M. Duanmu, K. Li, R. L. Horne, P. G. Kevrekidis and N. Whitaker, “Linear and Nonlinear PT-symmetric Oligomers: A Dynamical Systems Analysis”, arXiv:1210.3871v1, first posted 2012-10-15. https://arxiv.org/abs/1210.3871
2. C. A. Downing and V. A. Saroka, “Exceptional points in oligomer chains”, *Communications Physics* **4**, 254 (2021). https://doi.org/10.1038/s42005-021-00757-3
