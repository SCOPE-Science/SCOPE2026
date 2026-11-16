# A uniform four-or-six sensor law for anisotropic triangular cylinders

## Finding
Fix any odd integer \(N\ge3\). On the triangular cylinder \(G_N=\mathbb Z_3\times\mathbb Z_N\), for a real anisotropy \(\gamma>0\), consider the linear operator
\[
(T_\gamma f)(x,y)=\frac{f(x+1,y)+f(x-1,y)+\gamma f(x,y+1)+\gamma f(x,y-1)}{2(1+\gamma)}.
\]
Coordinates are cyclic. A set \(S\subseteq G_N\) is a *dynamical sampling set* if the samples \(\{(T_\gamma^j f)(v):v\in S,\ j=0,1,\ldots\}\) determine every complex signal \(f\in\mathbb C^{G_N}\). Let \(m_N(\gamma)\) be the smallest possible number of fixed vertices in such a set. Put
\[
K=(N-1)/2,\qquad \mu_s=2\cos(2\pi s/N)\ (0\le s\le K),
\qquad \mathcal R_N=\left\{\frac{3}{\mu_t-\mu_s}:1\le t<s\le K\right\}.
\]
**Theorem (sharp complete sensor classification).** For every odd \(N\ge3\) and every \(\gamma>0\),
\[
\boxed{m_N(\gamma)=\begin{cases}6,&\gamma\in\mathcal R_N,\\4,&\gamma\notin\mathcal R_N.\end{cases}}
\]
At every nonexceptional coupling, the **same four physical sites**, independent of \(N\) and \(\gamma\), suffice:
\[
S_4=\{(0,0),(0,1),(1,1),(1,2)\}.
\]
For every coupling, including every exceptional one, the **same six sites** suffice:
\[
S_6=\{0,1,2\}\times\{0,1\}.
\]
In each assertion, finitely many time samples \(j=0,\ldots,N\) already suffice. The sharpness statements hold even if infinitely many time samples are permitted. Thus the minimal sensor budget jumps from four to six exactly at the finite set \(\mathcal R_N\), with no assumptions that its listed ratios are distinct. For \(N=3\) the exceptional set is empty, and for \(N=5\) it consists of \(3/\sqrt5\).

## Assumptions and scope
The system consists of all complex signals on the finite vertex set, with no bandwidth or sparsity restrictions. All weights are positive, and the relative horizontal/vertical weights are \(1:\gamma\). The operator is the normalized nearest-neighbor average, not an arbitrary graph deformation. A sensor is a point evaluation at a *fixed* vertex, repeated at each measurement time; the problem minimizes the number of distinct spatial sites, not the time horizon or numerical condition number. The oddness of \(N\) ensures that every nontrivial second-coordinate Fourier frequency has a distinct inverse frequency. All statements concern exact noiseless reconstruction at a known anisotropy.

## Proof
**1. Distinct eigenvalue branches and dimensions.** Let \(\omega=e^{2\pi i/3}\), \(\zeta=e^{2\pi i/N}\). The \(3N\) Fourier characters
\[
\chi_{r,k}(x,y)=\omega^{rx}\zeta^{ky},\quad r\in\{0,1,2\},\ k\in\{0,\ldots,N-1\},
\]
form an orthogonal basis. Since \(\omega+\omega^{-1}=-1\), their eigenvalues are
\[
\lambda_{r,k}=\frac{a_r+\gamma\mu_{\min(k,N-k)}}{2(1+\gamma)},\qquad a_0=2,\quad a_1=a_2=-1.
\]
The numbers \(\mu_0>\mu_1>\cdots>\mu_K\) are distinct. Set \(V_0=\operatorname{span}\{1\}\), \(V_s=\operatorname{span}\{\zeta^{sy},\zeta^{-sy}\}\) for \(1\le s\le K\), and \(W_0=\operatorname{span}\{1\}\), \(W_1=\operatorname{span}\{\omega^x,\omega^{-x}\}\). All eigenspaces are individual blocks \(W_b\otimes V_s\), or sums of one block from each \(b\in\{0,1\}\); **no two distinct levels within either branch can coincide**.

The two branches meet exactly when
\[
2+\gamma\mu_s=-1+\gamma\mu_t,
\quad\Longleftrightarrow\quad \gamma=\frac{3}{\mu_t-\mu_s},\quad 0\le t<s\le K.
\]
For a collision with \(t=0\), the merged eigenspace has dimension \(2+2=4\). For \(t\ge1\), it has dimension \(2+4=6\). Away from collisions, the largest eigenspace has dimension four (because \(K\ge1\)), and this remains true when only collisions with \(t=0\) occur. Consequently the maximal eigenspace dimension is exactly six if \(\gamma\in\mathcal R_N\), and four otherwise. Coincident ratios in the defining set cause collisions at **different** eigenvalues and do not produce a triple-branch eigenvalue, because each of the two branches is injectively indexed by \(s\).

**2. Universal lower bound on sensor count.** Fix an eigenvalue \(\lambda\) with eigenspace dimension \(d\). A set of \(m<d\) point evaluations has a nonzero kernel on this eigenspace. Any nonzero eigenvector in that kernel remains invisible at those vertices under all powers of \(T_\gamma\), since \(T_\gamma^j f=\lambda^j f\). Thus every sampling set must have at least the maximum eigenspace dimension found in Step 1, proving the lower bounds \(4\) and \(6\).

**3. A fixed four-site set separates every nonexceptional eigenspace.** First consider a block \(W_1\otimes V_s\), \(s\ge1\). For \(f\) in this block, suppose its four samples at \(S_4\) vanish. At \(x=0\), the values at \(y=0,1\) force both coefficients of \(\zeta^{sy}\) and \(\zeta^{-sy}\) to vanish in \(f(0,y)\), since
\[
\det\begin{pmatrix}1&1\\\zeta^s&\zeta^{-s}\end{pmatrix}=\zeta^{-s}-\zeta^s\ne0.
\]
At \(x=1\), the values at \(y=1,2\) likewise force both second-coordinate coefficients of \(f(1,y)\) to vanish; the determinant differs only by a nonzero factor. For each second-coordinate coefficient, its dependence on \(x\) lies in \(W_1\), whose values at \(x=0,1\) are independent because \(\omega\ne\omega^{-1}\). It must vanish identically. All smaller, unmerged blocks \(W_0\otimes V_s\) and \(W_1\otimes V_0\) are also injectively sampled by \(S_4\) (the same two-frequency Vandermonde tests).

There is one more four-dimensional case to check: a collision with \(t=0\). Its arbitrary element has the form
\[
f(x,y)=a\zeta^{sy}+b\zeta^{-sy}+c\omega^x+d\omega^{-x},\qquad s>0.
\]
Write \(z=\zeta^s\). If \(f\) vanishes at \(S_4\), subtracting its two samples at \(x=0\), and subtracting its two samples at \(x=1\), gives
\[
\begin{pmatrix}z-1&z^{-1}-1\\z(z-1)&z^{-1}(z^{-1}-1)\end{pmatrix}\binom ab=0.
\]
The determinant is \((z-1)(z^{-1}-1)(z^{-1}-z)\ne0\), because \(N\) is odd and \(1\le s\le K\). Hence \(a=b=0\). The remaining \(x=0\) and \(x=1\) samples then force \(c=d=0\) by the invertible two-frequency \(3\)-cycle Vandermonde. Thus \(S_4\) is injective on **every** eigenspace whenever no six-dimensional collision occurs, even if several four-dimensional collisions are present.

**4. A fixed six-site set separates every eigenspace.** On \(S_6\), the three values of \(x\) at either \(y=0\) or \(1\) give the complete discrete Fourier transform in the first coordinate. Consequently they isolate the components in \(W_0\) and \(W_1\), including when their eigenvalues coincide. On either component, at most a single \(V_s\) can occur for each eigenvalue, by the strict ordering of the \(\mu_s\). The values at \(y=0,1\) then resolve \(V_s\) by the invertible two-frequency Vandermonde from Step 3, or trivially for \(s=0\). Therefore restriction to \(S_6\) is injective on each eigenspace for every positive coupling.

**5. Finite-time reconstruction.** The operator has at most \(2(K+1)=N+1\) distinct eigenvalues; let their actual number be \(D\). At each fixed sensor \(v\), spectral decomposition gives
\[
(T_\gamma^j f)(v)=\sum_{\ell=1}^D\lambda_\ell^j f_{\lambda_\ell}(v).
\]
The \(D\times D\) Vandermonde matrix in the *distinct real eigenvalues* is invertible, hence the samples at \(j=0,\ldots,D-1\) separately recover each spectral projection's values at every sensor. By Steps 3 and 4, the resulting spatial sampling matrices are injective on their eigenspaces, and recover every projection, hence the full signal. Because \(D\le N+1\), the times \(0,\ldots,N\) suffice. In finite dimension, injectivity also implies positive lower and finite upper frame bounds. Steps 2–5 prove all assertions.

## Verification
The accompanying standalone `CHECK.py` numerically enumerates the complete Fourier spectra and all positive exceptional ratios for odd cycle lengths through \(35\), verifies maximal eigenspace dimensions, checks full rank for the fixed four/six-site matrices at every eigenspace, and checks complete time-space observability at selected small lengths. It uses Python 3 and NumPy; run `python CHECK.py` after installing the version constraint in `requirements.txt`. Numerical tests are explicitly *not* the proof for arbitrary \(N\); the dimension argument and exact Vandermonde determinants above establish the infinite family.

## Relationship to prior work
Bulai, Cabrelli, Cordero, Molter and Saliani (2026) give the general eigenspace-frame criterion for dynamical sampling on finite graphs, and study path graphs rather than the above anisotropic triangular cylinders. The general frame-of-iterations theory also appears in Cabrelli, Molter, Paternostro and Philipp and in the survey of Aldroubi and collaborators. Those criteria are inputs, not claimed as new.

The closest explicitly inspected published computation is *Sharp four-six-eight sensor resonance law for an anisotropic \(5\times7\) Fourier torus* (2026), which treats one fixed unequal-prime Cartesian product and gives an arithmetic list of exceptional couplings and several optimal sensor configurations. It does **not** assert or imply the uniform all-odd-\(N\) four/six law for \(\mathbb Z_3\times\mathbb Z_N\), or that the *same staggered four-point pattern* remains optimal at every four-dimensional resonance. The structural-observability result of Doostmohammadian instead allows generic edge weights and does not resolve the exact one-parameter exceptional set. The claim here is the uniform all-order phase diagram and explicit universal sensor geometries, not the elementary general observability criterion.

## Limitations
The characterization does not hold without possible changes for even \(N\), where the second-coordinate frequency at \(N/2\) is self-inverse. No uniform quantitative conditioning is asserted as a coupling approaches resonance, and the stated time horizon is sufficient but not necessarily minimal. The system assumes known exact coupling, fixed vertex sensors, noiseless measurements, and unrestricted complex signal data. Older equivalent formulations in graph observability or multidimensional Fourier dynamics remain a publication-priority risk pending independent external review. The result has received no independent mathematical audit.

## References
1. I. M. Bulai, C. Cabrelli, E. Cordero, U. Molter and S. Saliani, *Dynamical Sampling in Graph Paley--Wiener Spaces*, arXiv:2609.25472v1, first public September 21, 2026; see Theorem 4.1. https://arxiv.org/abs/2609.25472 .
2. C. Cabrelli, U. Molter, V. Paternostro and F. Philipp, *Dynamical Sampling on Finite Index Sets*, arXiv:1702.03384, https://arxiv.org/abs/1702.03384 .
3. A. Aldroubi, C. Cabrelli, I. Krishtal and U. Molter, *Dynamical Sampling: A Survey*, arXiv:2511.10769, https://arxiv.org/abs/2511.10769 .
4. *Sharp four-six-eight sensor resonance law for an anisotropic \(5\times7\) Fourier torus*, published-finding corpus research record (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-sharp-four-six-eight-sensor-resonance-law-for-an-anisotropic-5-t--89a42efe6679/RESULT.md .
5. M. Doostmohammadian, *Recovering the Structural Observability of Composite Networks via Cartesian Product*, arXiv:2001.04699, https://arxiv.org/abs/2001.04699 .
