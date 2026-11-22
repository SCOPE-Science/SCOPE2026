# A unique antiferromagnetic mixing optimum for two-particle Kawasaki dynamics on balanced bicliques

## Finding
For every integer \(r\ge2\), the two-particle, fixed-magnetization Ising Kawasaki chain on the balanced complete bipartite graph \(K_{r,r}\) has an exact continuous-time relaxation gap, and antiferromagnetic coupling produces a **unique optimal positive inverse temperature**. Let
\[
a=\frac{1}{1+e^{-4\beta J}},\qquad c_r=r(3r-2).
\]
For \(r\ge3\), the gap of the **entire** \(\binom{2r}{2}\)-state chain is
\[
g_r(a)=r-1+a-\sqrt{(r-1+a)^2-c_r a(1-a)}.
\]
For \(r=2\), it is \(g_2(a)=\min\{4a,2(1-a)\}\). At \(\beta=0\), every \(r\) has \(g_r=r/2\).

For any antiferromagnetic \(J<0\), put
\[
t_r=\frac{2r-1-\sqrt{r(r-2)}}{3r^2-2r+1},\quad
\beta_r^*=\frac{\operatorname{artanh}(t_r)}{2|J|}.
\]
Then \(\beta_r^*\) is the unique global maximizer over \(\beta\ge0\), with
\[
g_r(\beta_r^*)=\frac{r(3r-2)t_r}{2}>\frac r2.
\]
For \(r=2\), \(\beta_2^*=\log 2/(4|J|)\) and \(g_2(\beta_2^*)=4/3\); the optimum is a cusp. For \(r\ge3\), it is smooth. As \(r\to\infty\),
\[
\beta_r^*=\frac{1}{6r|J|}+O\bigl((|J|r^2)^{-1}\bigr),\qquad
 g_r(\beta_r^*)=\frac r2+\frac{1}{12r}+O(r^{-2}).
\]
For \(J>0\), the gap is strictly decreasing in positive inverse temperature. For \(J=0\), it is constant \(r/2\).

## Assumptions and scope
The graph has two labeled shores of size \(r\) and every cross-shore edge. Exactly two vertices have spin \(+1\), all others have spin \(-1\); hence total magnetization is fixed. Every edge with unlike endpoints exchanges its spins at unit attempt rate multiplied by the heat-bath acceptance probability
\[
q(\sigma,\sigma^{uv})=\frac1{1+\exp\{\beta[H(\sigma^{uv})-H(\sigma)]\}},\quad
H(\sigma)=-J\sum_{uv\in E}\sigma_u\sigma_v.
\]
Equal-spin exchanges do nothing. The generator acts on functions by \((Lf)(\sigma)=\sum_{\tau}q(\sigma,\tau)[f(\tau)-f(\sigma)]\). The spectral gap is the smallest positive eigenvalue of \(-L\). All finite \(\beta\ge0\) yield irreducible, reversible chains. The result concerns this edge-clock normalization, **not** global random-pair proposals or a rate per particle.

## Proof
An occupation configuration belongs to one of three sectors: two occupied vertices in the first shore (AA), one in each shore (AB), or two in the second shore (BB). The Hamiltonian is equal on the AA and BB sectors; moving from either to AB changes the energy by \(-4J\). Thus every AA-to-AB or BB-to-AB exchange occurs at rate \(a\), and the reverse at rate \(b=1-a\). The outgoing total rates are \(2ra\), \(2(r-1)b\), and \(2ra\), respectively.

For \(r\ge3\), decompose the functions on unordered pairs within a shore into: constants; the standard subspace \(g(i)+g(j)\) for \(\sum_i g(i)=0\); and the kernel of the pair-to-vertex incidence matrix (dimension \(r(r-3)/2\), zero for \(r=3\)). Decompose functions on cross-shore pairs into constants, the two standard subspaces \(g(i)\) and \(h(j)\), and products \(g(i)h(j)\) with both sums zero. These mutually orthogonal-in-sector invariant spaces exhaust \(\binom{2r}{2}\) dimensions.

The three constant-sector eigenvalues of \(-L\) are \(0\), \(2ra\), and \(2ra+2(r-1)b\). The two standard sectors each reduce to the same \(2\)-by-\(2\) matrix, with respect to incidence-compatible coordinates,
\[
B_r=\begin{pmatrix}2ra&-ra\\-(r-2)b&2(r-1)b\end{pmatrix}.
\]
Its eigenvalues are \(\lambda_-(a)=g_r(a)\) and \(\lambda_+(a)\), the roots of
\[
\lambda^2-2(r-1+a)\lambda+r(3r-2)a(1-a)=0.
\]
Each occurs with multiplicity \(2(r-1)\). The mixed standard tensor has eigenvalue \(2(r-1)b\), multiplicity \((r-1)^2\); the pair-incidence kernels each have eigenvalue \(2ra\), total multiplicity \(r(r-3)\). The listed multiplicities sum to \(r(2r-1)\), the state-space dimension. Because \(r>2\), the nonzero off-diagonal product in \(B_r\) gives \(0<\lambda_-<\min\{2ra,2(r-1)b\}\), so \(\lambda_-\) is the full spectral gap.

For \(r=2\), the incidence-standard pair spaces are absent, giving full spectrum \(0\), \(4a\), \(2(1+a)\), and \(2(1-a)\) with multiplicity three. Therefore \(g_2(a)=\min\{4a,2(1-a)\}\).

For \(r>2\), write \(\Delta(a)=(r-1+a)^2-c_r a(1-a)\). Direct differentiation yields
\[
\frac{d^2}{da^2}\sqrt{\Delta(a)}=
\frac{r^2(r-2)(3r-2)}{4\Delta(a)^{3/2}}>0.
\]
Hence \(g_r(a)=r-1+a-\sqrt{\Delta(a)}\) is strictly concave. Its derivative is positive at \(a=0\) and negative at \(a=1/2\). The unique stationary maximum in \((0,1/2)\) satisfies \(2g_r(a)=c_r(1-2a)\). With \(t=1-2a\), its characteristic equation becomes
\[
(c_r+1)t^2-2(2r-1)t+1=0.
\]
The smaller root is \(t_r\) given above; it is the one yielding the **smaller** eigenvalue, since \((c_r+1)t_r<2r-1\). The larger root pertains to the upper branch. In antiferromagnetic dynamics, \(t=\tanh(2\beta|J|)\) rises strictly from zero to one; thus this maximum is unique in \(\beta\). For \(r=2\), the two linear gap branches intersect uniquely at \(a=1/3\), which gives the same \(t_2\) and maximum but a cusp. For \(J>0\), \(a>1/2\) and the derivative of the smaller eigenvalue is strictly negative, since its implicit derivative has numerator \(2g_r-c_r(1-2a)>0\) and denominator \(2(g_r-r+1-a)<0\); the \(r=2\) branch is likewise decreasing. Finally, Taylor expansion of the displayed exact radical produces the stated large-\(r\) asymptotics.

## Verification
The accompanying executable `verify_spectrum.py` constructs the **full** generator from the exchange definition (not the representation blocks) and compares exact characteristic polynomials for each \(r=2,3,4\) and rational \(a\in\{1/3,1/2,2/3\}\). It also compares full numerical spectra for \(r=5,6,7,8\) and rational \(a\in\{1/4,1/2,3/4\}\). It passed 9 exact full-characteristic-polynomial checks and 12 further full-spectrum numerical comparisons. These finite checks are supplemental; the invariant-space proof above covers every integer \(r\ge2\) and every finite temperature.

## Relationship to prior work
Mendonça, *Exact eigenspectrum of the symmetric simple exclusion process on the complete, complete bipartite, and related graphs* (first public 2012-07-17, arXiv:1207.4106), treats the constant-rate symmetric exclusion model on precisely these graph families and supplies the key noninteracting spectral baseline. That work's generator has no nonconstant Gibbs energy and does **not** imply the heat-bath interaction-dependent eigenvalue branches, antiferromagnetic speedup, or optimizing temperature. Grynberg (2010, arXiv:1009.4511) studies interacting Kawasaki dynamics and temperature-dependent gaps on one-dimensional Ising chains, not on dense bicliques or this two-particle sector. Caputo–Liggett–Richthammer (2009, arXiv:0906.1238) prove the uniform-conductance exclusion/interchange spectral-gap comparison; the configuration-dependent heat-bath rates used here are outside that result's premise. Prior exact symmetric representations inform the block decomposition but do not supply the nonlinear optimum.

## Limitations
The theorem is restricted to exactly two positive spins on balanced complete bipartite graphs, with the stated edge-clock heat-bath exchange normalization. The gain above infinite-temperature gap is \(O(r^{-1})\) in absolute terms and therefore does **not** indicate a macroscopic phase transition. The formulas do not classify arbitrary fixed magnetizations, unequal shore sizes, Metropolis rates, or mixing times beyond the spectral relaxation rate. Earlier equivalent calculations absent from the inspected sources cannot be excluded; independent mathematical auditing has not been performed.

## References
1. J. R. G. Mendonça, *Exact eigenspectrum of the symmetric simple exclusion process on the complete, complete bipartite, and related graphs*, arXiv:1207.4106, originally posted 2012-07-17. https://arxiv.org/abs/1207.4106
2. M. D. Grynberg, *Revisiting Kawasaki dynamics in one dimension*, arXiv:1009.4511, originally posted 2010-09-23. https://arxiv.org/abs/1009.4511
3. P. Caputo, T. M. Liggett and T. Richthammer, *Proof of Aldous' spectral gap conjecture*, arXiv:0906.1238, originally posted 2009-06-06. https://arxiv.org/abs/0906.1238
