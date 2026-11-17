# Radix-arithmetic sampling spikes and Lorentzian boundary layers for a diagonal semigroup

## Finding
Fix any integer \(b\ge 2\), exponent \(0<\alpha<1\), and real \(\lambda>0\). For the diagonal contraction semigroup defined below, the normalized operator-norm error of its trapezoid-corrected sampled resolvent at \(T_N=\tau b^{-N}\) has an exact pointwise limit for **every** \(1\le\tau<b\). Define
\[
r_b(\tau)=\min\{r\in\mathbb N_0:\tau b^r\in\mathbb Z\},
\]
with value \(+\infty\) when the set is empty. Then
\[
\lim_{N\to\infty}T_N^{-\alpha}\left\|Q^\natural_{T_N}-(\lambda-B)^{-1}\right\|
=F_{b,\alpha}(\tau):=
\begin{cases}
(2\pi\tau b^{r_b(\tau)})^{-\alpha},&r_b(\tau)<\infty,\\
0,&r_b(\tau)=\infty.
\end{cases}
\tag{1}
\]
The limit function is continuous at every nonresonant parameter and discontinuous at every resonant parameter: its positive spikes occur at the dense set of rationals whose denominator divides a power of \(b\).

Moreover, for each resonant \(\tau_0=m/b^r\in(1,b)\), where \(r=r_b(\tau_0)\), every real \(\xi\), and \(h_N=b^{-(1-\alpha)N}\), the perturbed meshes \(T_N(\xi)=b^{-N}(\tau_0+\xi h_N)\) obey
\[
\lim_{N\to\infty}T_N(\xi)^{-\alpha}
\left\|Q^\natural_{T_N(\xi)}-(\lambda-B)^{-1}\right\|
=\frac{(2\pi m)^{-\alpha}}{\sqrt{1+(\xi/w)^2}},
\qquad w=\tau_0(2\pi)^{\alpha-1}b^{(\alpha-1)r}.
\tag{2}
\]
Thus the spikes have an explicit universal Lorentzian profile on the exact mesh-ratio scale \(b^{-(1-\alpha)N}\).

## Assumptions and scope
Let \(H=\ell^2(\mathbb N_0)\) over \(\mathbb C\), with canonical orthonormal basis \((e_j)_{j\ge0}\). Put \(a_j=2\pi b^j\), and define the densely defined maximal diagonal operator
\[
Be_j=-(a_j^\alpha+i a_j)e_j,
\quad D(B)=\big\{x:\sum_{j\ge0}(a_j^{2\alpha}+a_j^2)|x_j|^2<\infty\big\}.
\]
Its strongly continuous contraction semigroup acts by \(S_t e_j=e^{-t(a_j^\alpha+i a_j)}e_j\). Fix a real Laplace parameter \(\lambda>0\), and define for \(T>0\)
\[
R=(\lambda-B)^{-1},\qquad
Q_T=T(I-e^{-\lambda T}S_T)^{-1},\qquad
Q_T^\natural=Q_T-\tfrac T2 I.
\]
All norms in (1)--(2) are the operator norm on \(H\). The result makes no claim for \(\alpha=0\), \(\alpha=1\), general normal generators, or uniform convergence in \(\tau\).

## Proof
**1. Exact scalar model.** Write \(p_j=\lambda+a_j^\alpha+i a_j\), so \(\operatorname{Re}p_j>0\). The operator \(Q_T^\natural-R\) is diagonal with entries
\[
e_j(T)=\frac{T}{1-e^{-Tp_j}}-\frac T2-\frac1{p_j},
\qquad\|Q_T^\natural-R\|=\sup_{j\ge0}|e_j(T)|.
\tag{3}
\]
The expression \(Q_T\) is well-defined because \(\|e^{-\lambda T}S_T\|<1\). On every finite coordinate vector the semigroup is continuous at zero, and contractions extend this strong continuity to all of \(H\). The maximal diagonal generator follows by the standard difference-quotient characterization, or by taking Laplace transforms of each coordinate and using the closedness of the diagonal operator.

**2. Uniform frequency localization.** Set \(T=\tau_N b^{-N}\), where \(\tau_N\to\tau_*>0\) and the \(\tau_N\) remain in a fixed compact positive interval; both (1) and (2) have this form. For a fixed integer \(K\) sufficiently large, the indices \(0\le j\le N-K\) satisfy \(|Tp_j|\le Cb^{-K}\) for all large \(N\). The function
\[
\phi(z)=\frac1{1-e^{-z}}-\frac12-\frac1z
\]
extends holomorphically to \(z=0\), with \(\phi(0)=0\). It follows that \(|e_j(T)|=T|\phi(Tp_j)|\le CTb^{-K}\) throughout this lower tail, so its contribution multiplied by \(T^{-\alpha}\) tends to zero.

For the upper tail \(j\ge N+K\), positivity of \(\operatorname{Re}(Tp_j)\) and \(|1-e^{-z}|\ge1-e^{-\operatorname{Re}z}\) give
\[
\left|\frac{T}{1-e^{-Tp_j}}\right|
\le\frac{T}{1-e^{-Ta_j^\alpha}}
\le a_j^{-\alpha}+T,
\quad |p_j|^{-1}\le a_j^{-1}.
\]
Consequently,
\[
T^{-\alpha}|e_j(T)|\le(a_jT)^{-\alpha}+T^{1-\alpha}\bigl(\tfrac32+(a_jT)^{-1}\bigr)
\le Cb^{-\alpha K}+o(1),
\tag{4}
\]
uniformly in \(j\ge N+K\). Because \(K\) may be increased arbitrarily, the limiting norm is completely determined by the finitely many offsets \(k=j-N\) between these tails. The bounds also establish norm convergence at order \(O(T^\alpha)\) for this model.

**3. Fixed-ratio limits.** For each fixed offset \(k\in\mathbb Z\), whenever \(j=N+k\ge0\),
\[
Tp_j=i2\pi\tau b^k+\lambda\tau b^{-N}
 +(2\pi)^\alpha\tau b^{\alpha k}b^{-(1-\alpha)N}.
\tag{5}
\]
If \(\tau b^k\notin\mathbb Z\), the denominator \(1-e^{-Tp_j}\) tends to a nonzero complex number, and both terms in (3) are \(o(T^\alpha)\). If \(\tau b^k\in\mathbb Z\), the exponential has a first-order zero with real part given by the last term of (5), so
\[
T^{-\alpha}e_{N+k}(T)\longrightarrow (2\pi\tau b^k)^{-\alpha}.
\tag{6}
\]
Here the complex limit is positive and real. For \(1\le\tau<b\), resonance cannot occur at a negative offset \(k\), because \(0<\tau b^k<1\) for \(k\le-1\). At a nonnegative offset, the first possible resonance is precisely \(k=r_b(\tau)\), and every later offset also resonates. The modulus in (6) strictly decreases with increasing \(k\), yielding (1) by (4). If there is no resonant offset, (4) instead yields zero.

The stated continuity classification follows because finite-depth resonance sets are finite in compact intervals, while heights at depth at least \(K\) are bounded by \((2\pi b^K)^{-\alpha}\); near any nonresonant point the finitely many larger-height resonances can be excluded. Every resonant point is a discontinuity since nonresonant points are dense and have limit zero.

**4. Resonance boundary layer.** Fix \(\tau_0=m/b^r\in(1,b)\) of minimal depth \(r\), put \(h_N=b^{-(1-\alpha)N}\), and set \(\tau_N=\tau_0+\xi h_N\). Then for each fixed \(k\)
\[
Tp_{N+k}=i2\pi\tau_0 b^k
 +h_N\bigl[\tau_0(2\pi)^\alpha b^{\alpha k}+i2\pi b^k\xi\bigr]+o(h_N).
\tag{7}
\]
At every nonresonant offset \(k<r\), the normalized error vanishes. At each \(k\ge r\), the integer-phase factor in (7) cancels, yielding
\[
\lim_{N\to\infty}T^{-\alpha}|e_{N+k}(T)|
=\frac{\tau_0^{1-\alpha}}
{\sqrt{[\tau_0(2\pi)^\alpha b^{\alpha k}]^2+[2\pi b^k\xi]^2}}.
\tag{8}
\]
Both positive squared terms in the denominator strictly increase with \(k\), so the largest value occurs uniquely at \(k=r\). The uniform tails (4) again permit taking the supremum. Simplifying (8) at \(r\) gives exactly (2), including \(\xi=0\). This completes the proof.

## Verification
The companion script `check_phase.py` evaluates the **exact finite-coordinate scalar symbol** (3) with a stable exponential difference and tests finite meshes at radices \(2,3,4\), exponents \(1/2,3/5,7/10\), resonant and nonresonant ratios, and five offsets around each selected boundary layer. It passed 78 assertions when executed from the packaged source. These finite checks validate constants and signs numerically; the infinite supremum, arithmetic classification, and asymptotic limits rest on the analytical proof above, not the tests.

## Relationship to prior work
Castillo's 2026 dyadic-resolvent study develops sampled propagation identities and spectral reconstruction for self-adjoint operators. Castillo, Costin and Costin's earlier work supplies the foundational dyadic resolvent identity. A subsequent manuscript of Castillo (publicly posted 11 November 2026) gives general \(O(T^\alpha)\) estimates on Crandall–Pazy semigroups, and for the **dyadic** instance of precisely the same damped diagonal spectrum proves a lower bound of order \(T^\alpha\) on the exactly aligned mesh \(T=2^{-N}\) (Theorem 5.9 and Proposition 5.10(b)). Its results neither specify the constant in (1) across every fixed mesh ratio nor the Lorentzian scale and profile (2). The latter two quantitative assertions, not the general sampling identity or sharp rate, are the contribution here. The continuous-frequency Fourier-multiplier analogue has a smooth spectral band and cannot imply a discrete-grid radix discontinuity by restriction.

## Limitations
The model is a normal diagonal generator with a fixed geometrically spaced spectrum and power-law damping. Only \(0<\alpha<1\) is addressed. Convergence of the normalized error is pointwise in the mesh ratio, emphatically not locally uniform near a resonance. The Lorentzian limit is for fixed rescaled displacement \(\xi\), with no claimed global error bound uniform in that displacement. No originality claim is made for general Crandall–Pazy rates, the standard scalar quadrature formula, or their generic aliasing interpretation. Historical bibliography may contain an equivalent fine-phase computation not found in the inspected sources. The numerical checks are finite and use floating point arithmetic.

## References
1. N. Castillo, *Dyadic Resolvent Representations of Self-Adjoint Operators: Propagator Expansions, Spectral Measures, and Zeta Functions*, arXiv:2607.21278 (first public version 23 July 2026), https://arxiv.org/abs/2607.21278.
2. N. Castillo, *Sampled resolvents of \(C_0\)-semigroups: aliasing and sharp rates on the Crandall–Pazy scale*, arXiv:2611.15563v1 (public version 11 November 2026), especially Theorem 5.9 and Proposition 5.10(b), https://arxiv.org/html/2611.15563v1.
3. N. Castillo, O. Costin, and R. D. Costin, *Global rational approximations of functions with factorially divergent asymptotic series*, arXiv:2210.17502 (first public version 31 October 2022), https://arxiv.org/abs/2210.17502.
