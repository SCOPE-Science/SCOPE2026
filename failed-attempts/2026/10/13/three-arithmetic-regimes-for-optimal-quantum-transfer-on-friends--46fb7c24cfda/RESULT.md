# Three arithmetic regimes for optimal quantum transfer on friendship graphs

## Finding
For each integer \(m\ge2\), consider the friendship graph \(F_m=K_1\vee(mK_2)\), consisting of \(m\) triangles sharing exactly one common central vertex. Fix the two endpoints \(u,v\) of any one peripheral edge, use the **unweighted adjacency Hamiltonian** \(A_m=A(F_m)\) and the convention \(U_m(t)=\exp(itA_m)\), and define the **unrestricted optimal transfer probability**
\[
P_m=\sup_{t\ge0}|U_m(t)_{uv}|^2.
\]
Let \(D_m=\sqrt{8m+1}\) and define three positive constants
\[
\begin{aligned}
c_{\mathrm{irr}}&=1-\frac1{\sqrt2},\\
c_+&=\min_{z\in\mathbb R}\left(1+\frac{z^2}{2}-\frac{\cos(\pi/4+z)}{\sqrt2}\right),\\
c_-&=\min_{z\in\mathbb R}\left(1+\frac{z^2}{2}-\frac{\cos(3\pi/4+z)}{\sqrt2}\right).
\end{aligned}
\]
Then \(m(1-P_m)\) has three different limiting values:
\[
\boxed{
\begin{array}{ll}
 c_{\mathrm{irr}},&8m+1\text{ nonsquare},\\
 c_+,&m=k(k+1)/2,\ \ k\equiv0,3\pmod4,\\
 c_-,&m=k(k+1)/2,\ \ k\equiv1,2\pmod4.
\end{array}}
\]
Here every limit is taken as \\(m\\to\\infty\\) *within the indicated infinite subsequence*. Numerically, the constants are \(0.292893218813452\), \(0.419296833428176\), and \(1.305301344446716\), respectively. The optimal probability approaches one in all three regimes but its leading infidelity is genuinely sensitive to an arithmetic property of the number of triangles.

## Assumptions and scope
The graph is finite, connected, simple, unweighted, and has \(2m+1\) vertices. All amplitudes use \(\exp(itA_m)\) with \(t\ge0\); changing the sign of time does not affect probabilities. The chosen vertices are partners in the *same* peripheral edge, not vertices from different triangles and not the hub. The three limits concern *global suprema over arbitrarily long observation times*, not bounded-time optimization or typical-time behavior. For irrational \(D_m\), the supremum may not occur at a finite time; no assertion of attainment is made.

## Proof
**Step 1 (exact spectral reduction).** Label the shared hub \(h\), and the peripheral pairs \(u_j,v_j\) for \(1\le j\le m\), taking \(u=u_1,v=v_1\). The vector \(e_{u_j}-e_{v_j}\) has eigenvalue \(-1\). Pair sums with total coefficient zero form an eigenspace with eigenvalue \(+1\). The remaining two-dimensional subspace, spanned by \(e_h\) and the normalized uniform outer vector, has adjacency matrix
\[
\begin{pmatrix}0&\sqrt{2m}\\\sqrt{2m}&1\end{pmatrix},
\quad\text{with eigenvalues}\quad \lambda_\pm=\frac{1\pm D_m}{2}.
\]
Spectral projectors at the two specified peripheral vertices give the identity, for all real \(t\),
\[
\boxed{U_m(t)_{uv}=-\frac12e^{-it}+\frac{m-1}{2m}e^{it}+\frac{e^{it/2}}{2m}\left(\cos\frac{D_mt}{2}+\frac{i}{D_m}\sin\frac{D_mt}{2}\right).}
\tag{1}
\]
It can be reconstructed directly from the two peripheral eigenspaces and the symmetric block above. Put \(x=t/2\), \(\epsilon=1/(2m)\), \(\alpha=1/2-\epsilon\), and \(D=D_m\). Multiplying (1) by a unit complex number leaves its modulus unchanged, so its modulus equals that of
\[
\mathcal A_m(x)=B_m(x)+\epsilon C_D(Dx),\qquad
B_m(x)=\alpha e^{ix}-\frac12e^{-3ix},\qquad
C_D(\phi)=\cos\phi+\frac{i}{D}\sin\phi.
\tag{2}
\]
The base term obeys
\[
|B_m(x)|^2=\alpha^2+\frac14-\alpha\cos(4x),
\quad \max_x|B_m(x)|=1-\epsilon.
\tag{3}
\]
Its maxima are precisely \(x_j=\pi/4+j\pi/2\), \(j=0,1,2,3\), modulo \(2\pi\). If \(\delta\) is the signed distance to a nearest \(x_j\),
\[
(1-\epsilon)^2-|B_m(x)|^2
=\alpha(1-\cos4\delta)
=2\alpha\sin^2(2\delta).
\tag{4}
\]

**Step 2 (irrational discriminant).** If \(D\notin\mathbb Q\), the positive-time orbit \(x\mapsto(x\bmod2\pi,Dx\bmod2\pi)\) is dense in the two-torus by Kronecker's theorem. Hence the physical supremum equals the maximum of \(|B_m(x)+\epsilon C_D(\phi)|^2\) over independent phases \(x,\phi\). At each \(x_j\), \(B_m(x_j)=(1-\epsilon)e^{ix_j}\), and the maximum projection of \(C_D(\phi)\) onto this direction is
\[
\rho_D=\max_\phi\operatorname{Re}\big(e^{-ix_j}C_D(\phi)\big)
=\sqrt{\cos^2x_j+D^{-2}\sin^2x_j}
=\sqrt{\frac{1+D^{-2}}2}.
\tag{5}
\]
Since \(D\to\infty\), this yields \(\limsup m(1-P_m)\le 1-1/\sqrt2\). Conversely, any maximizing torus phases \((x_m,\phi_m)\) must have \(\operatorname{dist}(x_m,\{x_j\})\to0\): otherwise the base loss in (4) stays uniformly positive, whereas the candidate (5) gives probability \(1-O(m^{-1})\). Expanding (2) uniformly, the first-order correction at such phases obeys
\[
2m\epsilon\operatorname{Re}(\overline{B_m(x_m)}C_D(\phi_m))
\le\frac1{\sqrt2}+o(1).
\]
The nonnegative base loss in (3) may be discarded when lower-bounding the infidelity. It follows that \(\liminf m(1-P_m)\ge1-1/\sqrt2\), proving the first limit. In particular, a finite-time numerical search is not used in place of the dense-torus supremum.

**Step 3 (square discriminant).** If \(D\) is an integer, it is necessarily odd. Write \(D=2k+1\), equivalently \(m=k(k+1)/2\); then \(\mathcal A_m\) is periodic and its maximum is attained. At a peak \(x_j\), (2) gives \(1-|\mathcal A_m(x_j)|^2=O(m^{-1})\). If \(x_m\) is a global maximizer, (2)-(4), the triangle inequality and this competitor force
\[
\operatorname{dist}(x_m,\{x_j\})=O(m^{-1/2})=O(D^{-1}).
\tag{6}
\]
Consequently write \(x=x_j+z/D\) with bounded \(z\). Since \(D^2=8m+1\), Taylor expansion of (2)-(4), **uniformly for bounded \(z\)**, gives
\[
m\left(1-|\mathcal A_m(x_j+z/D)|^2\right)
=1+\frac{z^2}{2}-\cos x_j\cos(Dx_j+z)+o(1).
\tag{7}
\]
For each of the four \(j\), the last term is, after possibly replacing \(z\) by \(-z\), either \(2^{-1/2}\cos(\pi/4+z)\) when \(D\equiv1,7\pmod8\), or \(2^{-1/2}\cos(3\pi/4+z)\) when \(D\equiv3,5\pmod8\). There are no other square-discriminant residue classes. Because maximizing sequences have bounded \(z\) by (6), taking the minimum on both sides of the locally uniform limit (7) is legitimate: a maximizing subsequence furnishes the lower bound, and testing a fixed minimizing \(z\) furnishes the upper bound. Finally, \(D=2k+1\) turns the two congruence classes into the asserted conditions on \(k\pmod4\).

**Step 4 (distinct, well-defined constants).** For either \(\beta\in\{\pi/4,3\pi/4\}\), let \(g_\beta(z)=1+z^2/2-2^{-1/2}\cos(\beta+z)\). Its second derivative satisfies
\[
g_\beta''(z)=1+2^{-1/2}\cos(\beta+z)\ge1-2^{-1/2}>0.
\]
Thus the minimum is unique and is found by the equation \(z+2^{-1/2}\sin(\beta+z)=0\), with numerical roots approximately \(-0.318366325403\) and \(-0.704812002001\), respectively. The three constants are strictly ordered: \(c_+>1-2^{-1/2}\), because equality would require simultaneously \(z=0\) and \(\cos(\pi/4+z)=1\); while \(c_+\le g_{\pi/4}(0)=1/2\) and \(c_->1/2\), the latter following for \(|z|\ge1\) from \(g_{3\pi/4}(z)\ge3/2-1/\sqrt2>1/2\), and for \(|z|<1\) from \(\cos(3\pi/4+z)\le\cos(3\pi/4-1)<1/\sqrt2\) and \(g_{3\pi/4}(z)>1/2\). This proves the trichotomy. \(\square\)

## Verification
The included standalone `verify.py` reconstructs the adjacency matrix, checks exactly that the peripheral symmetric and antisymmetric vectors and the symmetric hub block have the prescribed action, and independently compares the formula (1) to the matrix exponential evaluated by a finite Taylor series for small graph orders. It also solves the one-variable convex minimizations and checks numerical large-discriminant examples in each residue class. Run it with `python3 verify.py` (Python standard library only). The reproduced output is given in `VERIFICATION.md`.

The numerical examples and finite exact matrix checks are corroboration only. The unrestricted global suprema and all three limits follow from the analytic spectral, torus-density, localization, and convex-minimization arguments in the proof.

## Relationship to prior work
Coutinho, Baptista, Godsil, Spier and Werner (2022/2023, arXiv:2208.08971) develop spectral-arithmetic tools and Kronecker methods for quantum walks. Kirkland and Monterde (2023, arXiv:2312.06906) give the general adjacency join transition formula (their Lemma 2) and an \(O(m^{-1})\) *amplitude* comparison for a graph of \(2m\) vertices joined to a singleton; these earlier results supply context and are not claimed as novel. The new result computes three **sharp constants for the globally optimized squared transfer infidelity**, distinguishing integral- from irrational-frequency regimes within one graph family.

Kimmerling's 2023 dissertation directly studies continuous-time walks on Dutch windmill graphs, emphasizing long-time average mixing-matrix ranks. Its indexed abstract is available, but the complete 100-page thesis could not be examined; any transfer-fidelity statements in its unseen sections remain a substantive overlap risk. Coutinho, Guo and Schmeits (arXiv:2505.11986) provide a separate spectral framework for peak state transfer and study different graph families; the relevant full text does not state the present three-limit classification. The literature comparisons are not an assertion of global uniqueness.

## Limitations
The calculation concerns partner vertices of a triangle in a *homogeneous, unweighted* friendship graph. It does not optimize transfer involving the hub or nonpartner peripheral vertices, nor establish an optimal finite readout time or waiting-time bound. Irrational-discriminant cases use a supremum that need not be attained. The theorem provides asymptotic limits, not finite-\(m\) closed formulas for every optimum. An earlier equivalent asymptotic classification might exist, especially in inaccessible full-text treatments of Dutch windmills.

## References
1. Gabriel Coutinho, Pedro Ferreira Baptista, Chris Godsil, Thomás Jung Spier, Reinhard Werner, *Irrational quantum walks*, arXiv:2208.08971v1 (first posted 2022-08-18), https://arxiv.org/abs/2208.08971 ; SIAM J. Appl. Algebra Geom. 7 (2023), 567–584, DOI 10.1137/22M1521262.
2. Steve Kirkland, Hermie Monterde, *Quantum walks on join graphs*, arXiv:2312.06906v1 (2023), https://arxiv.org/abs/2312.06906 .
3. Paula Rachael Kimmerling, *Continuous-Time Quantum Walks on Windmill Graphs*, PhD thesis, Washington State University (2023), DOI 10.7273/000006322; full text not examined.
4. Gabriel Coutinho, Krystal Guo, Vincent Schmeits, *Peak state transfer in continuous quantum walks*, arXiv:2505.11986 (first posted 2025), https://arxiv.org/abs/2505.11986 .
