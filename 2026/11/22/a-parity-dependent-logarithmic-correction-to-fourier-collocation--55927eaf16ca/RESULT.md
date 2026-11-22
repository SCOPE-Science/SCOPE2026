# A parity-dependent logarithmic correction to Fourier-collocation heat positivity

## Finding

Let \(N\ge 3\) be the number of nodes in equispaced Fourier collocation for the one-dimensional periodic heat equation on a circle of length \(2\pi\), with diffusivity one. Let \(P_N(t)\) be the exact semidiscrete heat propagator described below. Define its **eventual nodal positivity time** by
\[
T_N=\inf\{s\ge0:\ P_N(t)\text{ is entrywise nonnegative for every }t\ge s\}.
\]
Then, as \(N\to\infty\) through either parity,
\[
\boxed{T_N=\frac{\pi}{N}-\frac{\kappa_N\log N}{N^2}+O(N^{-2}),\qquad
\kappa_N=\begin{cases}1,&N\text{ even},\\3,&N\text{ odd}.\end{cases}}
\]
The constants implicit in the two \(O(N^{-2})\) estimates are absolute for the specified normalization. In particular the first correction to the known leading \(\pi/N\) law is **three times larger** on odd grids. For every sufficiently large \(N\), a single near-antipodal **even-indexed** matrix entry is negative on the lower side of the stated \(O(N^{-2})\) window, while every entry is strictly positive for *all subsequent times* on its upper side.

## Assumptions and scope

The grid nodes are \(x_j=2\pi j/N\), \(j=0,\dots,N-1\). The discrete Fourier frequencies are \(k=-m,\dots,m\) when \(N=2m+1\) is odd; when \(N=2m\) is even, they are \(-m<k<m\), with one real Nyquist mode at frequency \(m\). Each Fourier mode evolves by its exact multiplier \(e^{-k^2t}\). This convention makes \(P_N(t)\) a real symmetric circulant matrix with row sums one; no time discretization, filtering, artificial viscosity, alias-averaging or floating-point truncation is included. Entrywise positivity means preservation of the cone of nonnegative *nodal vectors*, not necessarily nonnegative trigonometric interpolation between nodes. The theorem is asymptotic; no formula for exact finite-\(N\) roots is asserted.

Write \(S_{N,j}(t)=N(P_N(t))_{0j}\), \(x=2\pi j/N\). The exact formulas are
\[
S_{2m,j}(t)=1+2\sum_{k=1}^{m-1}e^{-k^2t}\cos(kx)+e^{-m^2t}(-1)^j,
\]
\[
S_{2m+1,j}(t)=1+2\sum_{k=1}^{m}e^{-k^2t}\cos(kx).
\]
All inequalities and limiting statements use real \(t\ge0\) and integer \(N\ge3\).

## Proof

**1. Periodic Gaussian and exact omitted tails.** Put
\[
\Theta(t,x)=\sum_{k\in\mathbb Z}e^{-tk^2}e^{ikx}
=\sqrt{\frac\pi t}\sum_{r\in\mathbb Z}\exp\!\left(-\frac{(x-2\pi r)^2}{4t}\right)>0
\qquad(t>0).
\]
The second identity is Poisson summation. By circulant symmetry it suffices to take \(0\le j\le\lfloor N/2\rfloor\). Let
\[
d=\frac N2-j,\qquad x=\pi-\frac{2\pi d}{N},\qquad c=Nt,\qquad
\phi(c)=\frac14\left(c-\frac{\pi^2}{c}\right).
\]
Thus \(d\) is integral for even \(N\) and half-integral for odd \(N\); \(0\le d\le N/2\). Set \(R_{N,j}=\Theta(t,x)-S_{N,j}(t)\). For \(N=2m\), direct subtraction of Fourier series gives the exact identity
\[
R_{2m,j}(t)=(-1)^j e^{-m^2t}+2\sum_{\ell\ge1}e^{-(m+\ell)^2t}\cos((m+\ell)x).
\tag{1}
\]
Since \((m+\ell)^2-m^2\ge N\ell\), for all \(t>0\),
\[
|R_{2m,j}(t)|\le e^{-N^2t/4}\left(1+\frac{2e^{-Nt}}{1-e^{-Nt}}\right).
\tag{2}
\]
For \(N=2m+1\), write \(K=m+1=(N+1)/2\). Again subtracting exactly,
\[
R_{2m+1,j}(t)=2\sum_{\ell\ge0}e^{-(K+\ell)^2t}\cos((K+\ell)x),
\tag{3}
\]
where the crucial half-grid parity identity is
\[
\cos((K+\ell)x)=(-1)^{j+\ell}\sin\!\left(\frac{2\pi d(\ell+1/2)}{N}\right).
\tag{4}
\]
Using \(|\sin y|\le|y|\), \((K+\ell)^2-K^2\ge N\ell\) and the elementary geometric series, we obtain
\[
|R_{2m+1,j}(t)|\le\frac{4\pi d}{N}e^{-K^2t}
\left(\frac1{2(1-e^{-Nt})}+\frac{e^{-Nt}}{(1-e^{-Nt})^2}\right).
\tag{5}
\]
Unlike (2), the odd-grid tail contains an additional factor \(d/N\) near the antipode, which is the source of the two different logarithmic coefficients.

**2. A uniform positive region, including all later times.** The nearest Gaussian image gives
\[
\Theta(t,x)\ge\sqrt{\frac\pi t}\exp\!\left(-\frac{(\pi-2\pi d/N)^2}{4t}\right).
\tag{6}
\]
For \(c=Nt\) in \([\pi/2,2\pi]\), combining (2) or (5) with (6) and
\[
-\frac{N^2t}4+\frac{(\pi-2\pi d/N)^2}{4t}
\le -N\phi(c)-\frac{\pi^2d}{2c}
\]
shows, with a constant \(C_0\) independent of \(N,j,c\),
\[
\frac{|R_{N,j}(t)|}{\Theta(t,x)}\le C_0 N^{-\kappa_N/2}e^{-N\phi(c)},
\qquad \kappa_N=1\ (N\text{ even}),\quad \kappa_N=3\ (N\text{ odd}).
\tag{7}
\]
For the odd case use \(\sup_{d\ge0}d e^{-\pi d/4}<\infty\). The function \(\phi\) is strictly increasing on \((0,\infty)\), satisfies \(\phi(\pi)=0\), and has \(\phi'(\pi)=1/2\). For a fixed sufficiently large \(B>0\), set
\[
c_N^+=\pi-\frac{\kappa_N\log N-B}{N}.
\]
The Taylor expansion implies
\[
N\phi(c_N^+)=-\frac{\kappa_N\log N-B}{2}+o(1),
\]
so (7) is less than one for all \(c\in[c_N^+,2\pi]\), for all sufficiently large \(N\). The same proof bounds the ratio by an exponentially small number for \(2\pi\le c\le2N\) (equivalently \(2\pi/N\le t\le2\)); here use \(\sqrt t\le\sqrt2\) in (6), bounded geometric prefactors and \(\phi(c)\ge\phi(2\pi)>0\). For \(t\ge2\), the elementary bound
\[
S_{N,j}(t)\ge1-2\sum_{k\ge1}e^{-2k^2}>0
\]
holds for both parity conventions. Thus \(P_N(t)\) is strictly entrywise positive for *every* \(t\ge c_N^+/N\), proving
\[
T_N\le\frac\pi N-\frac{\kappa_N\log N-B}{N^2}.
\tag{8}
\]

**3. An explicit negative entry on the opposite side.** Choose the even index \(j_N=2\lfloor N/4\rfloor\) and define \(d_N=N/2-j_N\). For even \(N\), \(d_N\in\{0,1\}\), and for odd \(N\), \(d_N\in\{1/2,3/2\}\). From the two nearest Gaussian images, uniformly for \(c\to\pi\),
\[
\Theta(c/N,x_{j_N})=2\sqrt{\frac{\pi N}{c}}e^{-\pi^2N/(4c)}
\left[\cosh\!\left(\frac{\pi^2d_N}{c}\right)+o(1)\right].
\tag{9}
\]
For even \(N\), (1) and dominated convergence of its geometrically bounded tail yield
\[
R_{N,j_N}(c/N)=e^{-cN/4}\left[\tanh(c/2)+o(1)\right].
\tag{10}
\]
For odd \(N\), using (3)–(4), the Taylor expansion of sine and geometric domination give
\[
R_{N,j_N}(c/N)=\frac{2\pi d_N}{N}e^{-cN/4-c/2}
\left[\frac{1-e^{-c}}{(1+e^{-c})^2}+o(1)\right].
\tag{11}
\]
Both tails are strictly positive for all sufficiently large \(N\). From (9)–(11), the ratio \(\Theta/R\) at this index equals \(C_{\mathrm{parity},d_N}(1+o(1))N^{\kappa_N/2}e^{N\phi(c)}\), where each of the finitely many constants \(C_{\mathrm{parity},d_N}\) is finite and strictly positive. For a sufficiently large *fixed* \(B>0\), choose
\[
c_N^-=\pi-\frac{\kappa_N\log N+B}{N}.
\]
Then \(N^{\kappa_N/2}e^{N\phi(c_N^-)}\to e^{-B/2}\), so \(\Theta<R\) for all sufficiently large \(N\) of either parity. Consequently \(S_{N,j_N}(c_N^-/N)<0\), implying
\[
T_N\ge\frac\pi N-\frac{\kappa_N\log N+B}{N^2}.
\tag{12}
\]
Combining (8) and (12) proves the stated expansion with an \(O(N^{-2})\) remainder. \(\square\)

## Verification

The standalone program `verify.py` requires Python 3 and `mpmath`, and evaluates the **exact finite Fourier formulas** independently of a rapidly converging periodized-Gaussian expression and omitted-tail series. At 135 decimal digits it passed **346** finite assertions, including the full positive matrix-entry census for selected grid sizes, a negative antipodal even-indexed entry below the leading recovery scale, and finite-size logarithmic brackets. These finite diagnostics are not proofs of the all-\(N\) or all-time claims; the displayed estimates and dominated-convergence argument provide that proof. Run `python verify.py` in the directory containing the script.

## Relationship to prior work

Cifani and Jakobsen (2010), especially Section 3, develop a **non-monotone** Fourier spectral viscosity scheme for periodic fractional conservation laws; their spectral truncation and viscosity-modified nonlinear equations are not the exact unmodified heat collocation propagator, and they provide no eventual nodal positivity-time asymptotic. Dong Li (2021), Appendix B, analyzes almost-sharp maximum principles for discrete Fourier heat evolution; Theorem B.1 gives \(\ell_\infty\)-norm excess bounds and small-step defects, which do not imply the sign of every exponentially small matrix entry or a parity-dependent recovery correction. The directly relevant preceding published *Fourier-collocation heat-flow positivity horizon* result (published-finding corpus, 2026) establishes \(NT_N\to\pi\) on even grids only. Its statement and proof do not quantify the logarithmic correction and explicitly leave odd grids outside its scope. The new comparison therefore concerns the **new \(\log N/N^2\) coefficient and odd/even parity law**, rather than the previously established leading constant.

## Limitations

The time constant and coefficients correspond specifically to diffusivity one on the \(2\pi\)-periodic circle, exact continuous-in-time Fourier semidiscretization, and the described even-grid Nyquist convention. The result does not provide an exact finite-size threshold, prove that one fixed separation controls *every* finite-size root, treat multidimensional grids, justify stagewise positivity of time integrators, or establish positivity between collocation nodes. The accompanying computation is illustrative rather than a machine-formal infinite proof. Unindexed spectral cutoff/partial theta-function literature could contain an equivalent second-order asymptotic; specialist publication priority remains to be independently checked.

## References

1. Simone Cifani and Espen R. Jakobsen, *On the spectral vanishing viscosity method for periodic fractional conservation laws*, arXiv:1011.3443, submitted 2010-11-15, https://arxiv.org/html/1011.3443v1 (Introduction and Section 3).
2. Dong Li, *Effective maximum principles for spectral methods*, arXiv:2107.09438, submitted 2021-07-20, https://arxiv.org/html/2107.09438v1 (Appendix B, Theorem B.1).
3. *A sharp \(N^{-1}\) positivity-recovery horizon for Fourier-collocation heat flow*, published-finding corpus record `2026/11/8/SCOPE-a-sharp-n-1-positivity-recovery-horizon-for-fourier-collocation--d4274dc28d8b`, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-n-1-positivity-recovery-horizon-for-fourier-collocation--d4274dc28d8b (RESULT.md and limitations).
