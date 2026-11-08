# Arbitrary positive edge weights preserve Morse–Smale dynamics on a three-clock path

## Finding
For every \(a,b>0\), put \(\Lambda=a+b+\sqrt{a^2-ab+b^2}\) and consider the two-dimensional torus map
\[
F(x,y)=\left(x+h(2a\sin x-b\sin y),\quad y+h(-a\sin x+2b\sin y)\right)\pmod{2\pi}.
\]
**Theorem.** For every \(0<h<1/\Lambda\), the map \(F\) is a Morse–Smale diffeomorphism, with exactly one source \((0,0)\), two index-one saddles \((0,\pi)\) and \((\pi,0)\), and one sink \((\pi,\pi)\). The nonwandering set consists of these four points. Every nontrivial branch of either saddle's unstable manifold tends to the sink; in particular there is no saddle-to-saddle heteroclinic connection. The sink has a full-Lebesgue-measure basin. For \(h\geq1/\Lambda\) the map is not a local diffeomorphism, so this interval is optimal for the Morse–Smale diffeomorphism conclusion.

The claim holds for all positive weight ratios, including \(a>2b\) and \(b>2a\), which are excluded by the published weighted diagonal-dominance criterion for paths.

## Assumptions and scope
The full model has three identical clocks on the open path with edge weights \(a\) and \(b\), reciprocal repulsive sine interactions, and one simultaneous discrete update of strength \(h>0\):
\[
\theta_i^+=\theta_i+h\sum_{j:\{i,j\}\in\{\{1,2\},\{2,3\}\}}w_{ij}\sin(\theta_i-\theta_j)\pmod{2\pi},\quad w_{12}=a,\quad w_{23}=b.
\]
The coordinates are the independent differences \(x=\theta_1-\theta_2\) and \(y=\theta_2-\theta_3\) modulo \(2\pi\). The common phase is factored out; the full three-clock map has a neutral common-rotation direction and is not claimed to be Morse–Smale. The theorem assumes positive weights, no delays, no forcing, and the strict step bound. It is not an assertion about the continuous-time oscillator flow.

## Proof
**1. Descent, invertibility, and the fixed-point skeleton.** Let
\[
K=\begin{pmatrix}2&-1\\-1&2\end{pmatrix},\qquad A=\operatorname{diag}(a,b),\qquad V(x,y)=a\cos x+b\cos y.
\]
Then \(F(z)=z+hKA\sin z=z-hK\nabla V(z)\) on the periodic lift. The two eigenvalues of \(A^{1/2}KA^{1/2}\) are \(a+b\pm\sqrt{a^2-ab+b^2}\), hence its maximal eigenvalue is \(\Lambda\). If \(w=A\sin z\), Taylor's theorem and \(D^2V\preceq A\) give
\[
V(Fz)-V(z)\le-hw^{\mathsf T}Kw+\tfrac12h^2w^{\mathsf T}KAKw
\le-h(1-h\Lambda/2)w^{\mathsf T}Kw.
\]
Thus \(V\) decreases strictly outside the four points with \(\sin x=\sin y=0\). The derivative \(DF=I+hKA\operatorname{diag}(\cos x,\cos y)\) has only positive eigenvalues for \(h<1/\Lambda\): its nonidentity part is similar to the symmetric matrix \(K^{1/2}A\operatorname{diag}(\cos x,\cos y)K^{1/2}\), bounded in the Loewner order between \(-K^{1/2}AK^{1/2}\) and \(K^{1/2}AK^{1/2}\). Consequently \(F\) is a local diffeomorphism. The homotopy \(z\mapsto z+thKA\sin z\) has degree one, so the local diffeomorphism of the compact torus is a one-sheeted covering and hence a global diffeomorphism.

Strict descent rules out all nonfixed recurrent and periodic points; compactness and the finite fixed set imply that every forward orbit converges to a fixed point. At each fixed point, the derivative has no multiplier on the unit circle: the symmetric conjugate has nonzero eigenvalues with signs determined by the corresponding diagonal cosine signs. Hence \((0,0)\) is a source, \((\pi,\pi)\) a sink, and \(p=(0,\pi)\), \(q=(\pi,0)\) are saddles. The stable manifolds of the other three points have zero area, giving the full-measure sink basin.

**2. A common forward-invariant triangle for both saddles.** In the fundamental square define
\[
\mathcal K=\{(x,y):0\le x\le\pi,\ 0\le y\le\pi,\ x+y\ge\pi\}.
\]
The spectral formula implies \(\Lambda>2\max\{a,b\}\), so \(2ha<1\), \(2hb<1\), \(ha<1\), and \(hb<1\). For \((x,y)\in\mathcal K\), the inequalities \(\sin y\le\pi-y\le x\) and \(\sin x\le\pi-x\le y\) yield
\[
x^+\ge(1-hb)x\ge0,\qquad y^+\ge(1-ha)y\ge0.
\]
Moreover \(x^+\le x+2ha\sin x\le x+2ha(\pi-x)\le\pi\), and similarly \(y^+\le\pi\). Finally,
\[
x^++y^+=x+y+h(a\sin x+b\sin y)\ge\pi.
\]
Therefore \(F(\mathcal K)\subseteq\mathcal K\). Every nonvertex point on a side enters the interior, and all interior points stay in the interior. The involution \(\iota(x,y)=(-x,-y)\pmod{2\pi}\) commutes with \(F\); thus \(\iota(\mathcal K)\) is forward invariant too.

**3. Both saddle unstable branches enter the same triangles, while their stable directions do not.** Set \(E=\sqrt{a^2+ab+b^2}\). Note that
\[
0<r=\frac{a+b-E}{b}<1<R=\frac{a+b+E}{b}.
\]
Near \(p=(0,\pi)\), use positive corner coordinates \(u=x\), \(v=\pi-y\). The linear part of \(F-I\), divided by \(h\), is
\[
J_p=\begin{pmatrix}2a&-b\\a&-2b\end{pmatrix},
\]
with eigenvalues \(a-b\pm E\). Its unstable eigendirection into \(u,v>0\) has slope \(v/u=r<1\), so it lies in the interior of \(\mathcal K\), which locally is the sector \(u\ge v\ge0\). Its stable eigendirection has slope \(v/u=R>1\), strictly outside that sector.

Near \(q=(\pi,0)\), take \(u=\pi-x\), \(v=y\). The corresponding matrix is
\[
J_q=\begin{pmatrix}-2a&b\\-a&2b\end{pmatrix},
\]
with eigenvalues \(b-a\pm E\). The unstable eigendirection into \(u,v>0\) has slope \(v/u=R>1\), so lies inside \(\mathcal K\) (locally \(v\ge u\ge0\)), whereas its stable eigendirection has slope \(r<1\), strictly outside. The local stable-manifold theorem therefore gives neighborhoods \(U_p,U_q\) such that
\[
W^s_{\mathrm{loc}}(p)\cap\mathcal K=\{p\},\qquad W^s_{\mathrm{loc}}(q)\cap\mathcal K=\{q\}.
\]
The other unstable branch at each saddle is the image under \(\iota\) of the branch just described, and hence enters \(\iota(\mathcal K)\); the corresponding reflected local stable manifolds meet that triangle only at their fixed point.

**4. Transversality and sharpness.** Every nontrivial unstable branch of either saddle lies, after a backward-local segment, in one of these forward-invariant triangles. A trajectory starting in \(\mathcal K\) cannot converge to \(p\) or \(q\) unless it is the fixed point itself: convergence would put its tail in the corresponding local stable manifold inside \(\mathcal K\), forbidden by Step 3. The same holds in the reflected triangle. Since all trajectories converge to fixed points and strict descent excludes approach to the source from a lower potential level, every saddle unstable branch converges to \((\pi,\pi)\). Thus no unstable manifold of one saddle meets the stable manifold of the other; homoclinic connections are also ruled out by strict descent. Every remaining possible heteroclinic intersection involves a source (full-dimensional unstable tangent space) or a sink (full-dimensional stable tangent space), and is automatically transverse. The four-point nonwandering set is hyperbolic. This is precisely the Morse–Smale property.

For sharpness, along \((x,y)=(t,t)\) the Jacobian is \(I+h\cos t\,KA\). Its multiplier associated with \(\Lambda\) vanishes whenever \(\cos t=-1/(h\Lambda)\). Such a point exists for every \(h\ge1/\Lambda\); hence beyond the stated interval the map is not a local diffeomorphism. \(\square\)

## Verification
The self-contained Python script `verify.py` tests the triangle inequalities and strict Lyapunov descent on 60,000 reproducibly sampled states, including strong weight imbalances and steps close to the boundary; it also checks the saddle eigendirection slopes and loss of a positive multiplier at the endpoint. Run it with `python3 verify.py`. Its successful output begins `VERIFY_OK triangle_samples=60000`. These computations are finite consistency checks only. The universal assertions rest on the four analytic proof steps above and on the standard local stable-manifold and compact covering theorems.

## Relationship to prior work
Buescu, D'Aniello and Oliveira (2026, arXiv:2610.10993v1) establish the gradient/graph-Laplacian framework, the global descent and fixed-point skeleton, and Morse–Smale dynamics for unit-weight paths and weighted paths subject to \(2a\ge b\) and \(2b\ge a\) in the two-edge case (Corollaries 5.4 and 5.6). Their near-unit-weight structural stability result gives another local weight regime, not every positive ratio. The theorem here supplies the missing *global weight-ratio transversality statement* for the smallest nontrivial path, via a triangular barrier rather than diagonal dominance. In particular, no claim is made to rediscover the source's Lyapunov or hyperbolicity results.

Buescu, D'Aniello and Oliveira (2025, arXiv:2502.15371v1) study the equally weighted aligned three-clock map; Buescu and Oliveira (2025, arXiv:2503.13230v1) analyze identical-clock ring and path settings with small perturbations. Those results do not assert the full arbitrary-ratio theorem. General abstract structural stability near a particular weight vector cannot establish the uniform union of all positive ratios, nor does a full-measure sink basin itself imply Morse–Smale transversality. The available sources do not settle absolute historical priority.

## Limitations
The theorem is only for three identical clocks on the open two-edge path, reciprocal sinusoidal coupling, and the quotient by common phase, within the strict invertible-step interval. It does not extend by this proof to longer weighted paths, arbitrary trees, phase lags, different interaction laws, or heterogeneous intrinsic frequencies. For those systems saddle connections can be more complicated. The endpoint noninvertibility statement does not classify post-endpoint attractors. Historical novelty is assessed against identified research, not established by absence of search results; no independent mathematical audit has been performed.

## References
1. J. Buescu, E. D'Aniello, H. M. Oliveira, *Morse–Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1 (first public October 7, 2026), https://arxiv.org/html/2610.10993v1, Sections 2–5, especially Theorem 4.6 and Corollaries 5.2–5.6.
2. J. Buescu, E. D'Aniello, H. M. Oliveira, *A Lyapunov function for a Synchronisation diffeomorphism of three clocks*, arXiv:2502.15371v1 (February 21, 2025), https://arxiv.org/abs/2502.15371, Section 2.
3. J. Buescu, H. M. Oliveira, *Lyapunov functions for Morse-Smale synchronisation diffeomorphisms*, arXiv:2503.13230v1 (March 17, 2025), https://arxiv.org/abs/2503.13230, Introduction and main results.
