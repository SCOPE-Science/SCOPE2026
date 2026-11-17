# Coupling-independent onset and exclusion of diffusion-driven instability in the ideal-storage cellular automaton

## Finding
For the ideal-storage cellular automaton defined below, any finite symmetric nonnegative row-stochastic coupling leaves the **entire local-stability boundary of the homogeneous equilibrium unchanged**. More precisely, put \(b=5c\), \(r=(1+\exp(C_r-b))^{-1}\), and \(\delta=b(1-r)\). The homogeneous equilibrium is locally asymptotically stable if \(\delta<1\) and is unstable if \(\delta>1\), for **every** such coupling and any network size. At \(\delta=1\), every mode with coupling eigenvalue \(w<1\) remains strictly Schur stable; only the \(w=1\) modes can be marginal. Thus no nonuniform spatial mode can destabilize a linearly stable homogeneous state, and a connected genuinely coupled system first becomes marginal through its homogeneous oscillatory mode.

For \(c>0\) and \(C_r\geq0\), the boundary is exactly \(C_r=b-\log(b-1)\), \(b>1\). If \(C_r<2\), the equilibrium is stable for all \(c>0\). At \(C_r=2\) a single marginal tangency occurs at \(c=2/5\). For every \(C_r>2\) there are exactly two boundaries
\[
b_- = 1-W_0(-\exp(1-C_r)),\qquad b_+ = 1-W_{-1}(-\exp(1-C_r)),
\]
where \(W_0,W_{-1}\) are the two real branches of Lambert's \(W\)-function. The equilibrium is unstable exactly for \(b_-<5c<b_+\), and stable on both sides. These are **linear and local** conclusions, not existence or stability claims about spiral waves or invariant circles.

## Assumptions and scope
Let \(N\geq1\), let \(c>0\) and \(C_r\geq0\), and let \(W\) be an \(N\times N\) real symmetric nonnegative row-stochastic matrix. Each vertex carries storage \(S_i>0\) and rate \(0<R_i<1\). Update synchronously:
\[
S_i^+=(1-R_i)S_i+c,\qquad R_i^+=\frac{1}{1+\exp\big(C_r-5S_i\sum_jW_{ij}R_j\big)}.
\]
The original periodic Moore-neighborhood model has \(W=(1-p)I+(p/8)A\), where \(A\) is the adjacency matrix of the eight distinct Moore neighbors on a periodic rectangular torus with both dimensions at least three and \(0\leq p\leq1\). Such \(W\) satisfies the hypotheses. Linear stability means that all eigenvalues of the Jacobian have modulus less than one. Instability means at least one eigenvalue has modulus greater than one. The equality case is explicitly distinguished.

## Proof
**Equilibrium and spectrum.** A spatially homogeneous equilibrium must obey \(rS=c\) and \(r=(1+\exp(C_r-5rS))^{-1}\), giving the unique homogeneous pair
\[
(S_*,R_*)=\big(c/r,r\big),\qquad r=\frac1{1+\exp(C_r-5c)}\in(0,1).
\]
Write \(a=1-r\in(0,1)\) and \(\delta=5ca>0\). Differentiation at this equilibrium gives the block Jacobian
\[
J=\begin{pmatrix}
aI&-(c/r)I\\ 5r^2a I&\delta W
\end{pmatrix}.
\]
A real symmetric stochastic matrix has an orthonormal eigenbasis and all eigenvalues \(w\in[-1,1]\), including \(w=1\). Thus the full Jacobian decomposes into the two-by-two blocks
\[
J_w=\begin{pmatrix}a&-c/r\\5r^2a&\delta w\end{pmatrix},
\quad T_w=a+\delta w,\quad D_w=\delta(r+aw).
\]
Here the determinant identity uses \(5cr a=\delta r\).

**Strict stability.** The real quadratic \(\lambda^2-T_w\lambda+D_w\) is strictly Schur stable if and only if its three Jury expressions \(1-T_w+D_w\), \(1+T_w+D_w\), \(1-D_w\) are positive. Direct algebra yields
\[
\begin{aligned}
1-T_w+D_w&=r[1+\delta(1-w)],\\
1+T_w+D_w&=2-r+\delta[r+(2-r)w],\\
1-D_w&=1-\delta[r+(1-r)w].
\end{aligned}
\]
If \(0<\delta<1\) and \(-1\leq w\leq1\), the first expression is positive, the second is at least \(2-r-2\delta(1-r)>r>0\), and the third is at least \(1-\delta>0\). So every block, and hence the complete equilibrium, is strictly stable. This is stronger than testing the homogeneous mode only.

**Sharpness and critical modes.** For the inevitable uniform eigenvalue \(w=1\), \(D_1=\delta\). If \(\delta>1\), the product of the two multipliers exceeds one, so at least one has modulus greater than one. If \(\delta=1\) and \(w<1\), then \(1-D_w=(1-r)(1-w)>0\), while the first two Jury expressions remain strictly positive using the inequalities above with \(\delta=1\). Thus every nonuniform eigenspace is still strictly stable at the boundary whenever the eigenspace has \(w<1\). On \(w=1\), \(T_1=2-r\in(1,2)\) and \(D_1=1\), giving a nonreal conjugate pair on the unit circle. If \(W\) is irreducible, Perron–Frobenius makes \(w=1\) simple. This includes connected Moore tori with \(p>0\), even at \(p=1\).

**Complete parameter boundary.** As \(b=5c\), the stability parameter is
\[
\delta(b,C_r)=\frac{b}{1+\exp(b-C_r)}.
\]
The equation \(\delta=1\) is equivalent to \(b>1\) and \(C_r=b-\log(b-1)\). The latter function decreases from infinity to its unique minimum 2 at \(b=2\), then increases to infinity. Therefore it has no solutions when \(C_r<2\), a single tangent solution when \(C_r=2\), and exactly two when \(C_r>2\). Since \(\delta\) vanishes at \(b\downarrow0\) and \(b\to\infty\), it exceeds one exactly between the two roots. Solving \((b-1)\exp(-(b-1))=\exp(1-C_r)\) yields the two Lambert-\(W\) formulas in the Finding.

## Verification
The accompanying standard-library Python script `verify.py` checks all three polynomial Jury identities with exact fractions at 23,351 admissible triples, including 760 boundary-mode cases. It separately checks 21,780 Fourier-mode instances on genuine Moore tori of sizes \(3\) through \(8\) in both dimensions, for four diffusion strengths and five interior parameter pairs, and brackets the two parameter roots for six \(C_r>2\) choices. Execute `python verify.py` from the extracted directory. These finite checks are corroborative: the above algebra proves the infinite statements for every \(N\), \(c\), \(C_r\), and symmetric stochastic \(W\).

## Relationship to prior work
Hordijk's 2026 study [1] documents bifurcation diagrams of the isolated ideal-storage map and observes spiral waves in the coupled cellular automaton. Dress, Hordijk, Lin and Serocka [2] introduced and explored the coupled model, chiefly computationally. Dress and Lin [3] analyzed equilibrium stability and the Neimark–Sacker bifurcation of the **isolated two-dimensional map**. The uniform-mode stability test is therefore not new. The contribution here is the **all-mode, all-network** Schur classification showing that spatial diffusion cannot produce an earlier heterogeneous instability, as well as the exact uniform-onset parameter diagram within that conclusion. The reviewed sources do not report this coupled spectral exclusion. General master-stability/Jury tools are standard; no novelty is claimed for those techniques themselves.

## Limitations
This is a local linear-stability theorem for the homogeneous equilibrium. It does not establish global attraction, stability of spatial patterns, existence of invariant curves, spiral formation, or nonlinear behavior at the unit-circle boundary. Symmetry and nonnegative stochasticity of \(W\) matter: the stated proof does not apply to directed or signed couplings with nonreal spectrum. On disconnected networks, the eigenvalue 1 can be multiple; at \(p=0\), all sites are uncoupled and critical simultaneously. Historical priority outside the inspected source set is not independently certified.

## References
[1] W. Hordijk, *Spontaneous Spirals in Spatial Systems*, arXiv:2610.38710v1, first posted 2026-10-28; https://arxiv.org/html/2610.38710v1.

[2] A. Dress, W. Hordijk, W. Lin, and P. Serocka, *The Ideal Storage Cellular Automaton Model*, Dagstuhl Seminar Proceedings 10231 (2010), https://doi.org/10.4230/DagSemProc.10231.8.

[3] A. W. M. Dress and W. Lin, *Dynamics of a Discrete-Time Model of an Ideal-Storage System Describing Hetero-Catalytic Processes on Metal Surfaces*, International Journal of Bifurcation and Chaos 21 (2011), 1331–1339, https://doi.org/10.1142/S0218127411029197.
