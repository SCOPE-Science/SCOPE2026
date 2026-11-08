# An exact broadband-transmission law for incommensurate quantum-graph resonator arrays

## Finding

Consider a scattering channel with \(N\geq1\) equally spaced, identical side resonators of length \(\ell>0\), attached at channel spacing \(h>0\) through the *type-I scale-invariant* vertex conditions of Buhrii–Golovaty–Hryniv [1]. The pendant tips have Neumann boundary conditions, the two channel coupling strengths agree, \(\theta_1=\theta_2=t>0\), and the resonator coupling \(\theta_3\) is nonzero. Set
\[
b=\frac{\theta_3^2}{2t^2}>0,\qquad \frac{\ell}{h}\notin\mathbb Q.
\]
For the physical transmission probability \(T_N(k)\) at positive wavenumber \(k\), define its broadband (wavenumber-Cesàro) transmission
\[
G_N(b)=\lim_{K\to\infty}\frac1K\int_0^K T_N(k)\,dk.
\]
Every limit exists. The first two are exactly
\[
G_1(b)=\frac1{1+b},\qquad G_2(b)=\frac1{1+\sqrt2\,b}.
\]
The long-array limit exists and is strictly positive at every finite \(b>0\):
\[
\boxed{G_\infty(b):=\lim_{N\to\infty}G_N(b)=1-\frac2\pi L(b),}
\]
where
\[
L(b)=\begin{cases}
\displaystyle\frac{b}{\sqrt{1-b^2}}\operatorname{arsinh}\left(\frac{\sqrt{1-b^2}}b\right),&0<b<1,\\[5pt]
1,&b=1,\\[5pt]
\displaystyle\frac{b}{\sqrt{b^2-1}}\arcsin\left(\frac{\sqrt{b^2-1}}b\right),&b>1.
\end{cases}
\]
This explicitly resolves the two successive limits: first average over arbitrarily high wavenumbers at each finite array length, *then* increase the array length. It yields the nonanalytic weak-coupling and inverse-coupling laws
\[
1-G_\infty(b)=\frac{2b}{\pi}\log\frac2b+O\left(b^3\log\frac2b\right)\quad(b\downarrow0),
\]
\[
G_\infty(b)=\frac2{\pi b}-\frac1{2b^2}+O(b^{-3})\quad(b\to\infty).
\]
In particular \(G_\infty(1)=1-2/\pi\), whereas \(G_1(1)=1/2\) and \(G_2(1)=1/(1+\sqrt2)\). These are dimensionless *wavenumber* averages, not energy-weighted averages, incoherent transmission coefficients, or pointwise limits of the scattering probability.

## Assumptions and scope

The differential operator is the negative second derivative on every edge. Both leads are semi-infinite, attachment vertices are at positions \((j-1)h\) for \(j=1,\ldots,N\), and all pendant edges have common length \(\ell\). The local self-adjoint type-I matching conditions and the normalization of \(\theta_j\) are precisely those in [1, §§2–4]; thus the underlying scattering formula is not claimed to be new. Boundary conditions at the pendant tips are Neumann. No absorptive potentials or disorder are introduced. The irrational ratio assumption concerns exactly \(\ell/h\); its role is to make the resonator and propagation phases jointly equidistributed. It must not be dropped or replaced by a limit through rational ratios without further analysis.

Writing \(U_n\) for the Chebyshev polynomial of the second kind, the established scattering formula [1, Theorem 1(i)] specializes, away from the isolated resonator poles, to
\[
T_N(k)=\left[1+b^2\tan^2(k\ell)\,U_{N-1}\big(\cos(kh)-b\tan(k\ell)\sin(kh)\big)^2\right]^{-1}.
\]
The physical continuous-in-wavenumber assignment at isolated poles is immaterial to the integrals. The average \(G_N\) is taken at fixed \(N,b,\ell,h\). Only after it exists is \(N\) sent to infinity. The limits are not asserted to be uniform in \(b\) or in \(\ell/h\).

## Proof

**1. The two-phase reduction.** Put \(\varphi=k\ell\bmod\pi\), \(\psi=kh\bmod\pi\). By Kronecker–Weyl equidistribution for the irrational ratio \(\ell/h\), the mean over \(k\) of any bounded Riemann-integrable function of the two phases equals its mean over the two-torus. For fixed \(N\), the above scattering expression is bounded by one, continuous away from the pole lines and, at worst, a discrete set of phase-pair singularities; it is therefore Riemann-integrable. Hence
\[
G_N(b)=\frac1{\pi^2}\int_0^\pi\int_0^\pi
\frac{d\psi\,d\varphi}{1+b^2\tan^2\varphi\,U_{N-1}\big(\cos\psi-b\tan\varphi\sin\psi\big)^2}.
\tag{1}
\]
As a function of \(\psi\) at a fixed \(\varphi\), the Chebyshev argument is a phase-shifted cosine of amplitude \(\sqrt z\), with
\[
z=1+b^2\tan^2\varphi\geq1.
\]
By shift invariance of Lebesgue measure on a phase circle, define
\[
I_N(z)=\frac1\pi\int_0^\pi\frac{d\psi}{1+(z-1)U_{N-1}(\sqrt z\cos\psi)^2}.
\tag{2}
\]
Then \(G_N(b)=\pi^{-1}\int_0^\pi I_N(1+b^2\tan^2\varphi)\,d\varphi\), with \(0\le I_N\le1\).

**2. Exact one- and two-cell broadband responses.** Since \(U_0(x)=1\), \(I_1(z)=1/z\). Since \(U_1(x)=2x\), the classical cosine integral gives
\[
I_2(z)=\frac1\pi\int_0^\pi\frac{d\psi}{1+4z(z-1)\cos^2\psi}=\frac1{2z-1},
\]
using \(1+4z(z-1)=(2z-1)^2\) and \(z\ge1\). Finally, for \(a\ge0\),
\[
\frac1\pi\int_0^\pi\frac{d\varphi}{1+a^2\tan^2\varphi}=\frac1{1+a}.
\]
Substitute \(a=b\) and \(a=\sqrt2 b\) to obtain the first two exact formulas.

**3. The long-array Chebyshev-phase lemma.** For every \(z>1\),
\[
\lim_{N\to\infty}I_N(z)=1-\sqrt{1-z^{-1}}.\tag{3}
\]
Indeed, split the phase integral into \(|\sqrt z\cos\psi|>1\) (the gap) and \(|\sqrt z\cos\psi|<1\) (the band). In the open gap, \(|U_{N-1}(x)|\to\infty\) exponentially for each \(|x|>1\), so the integrand tends to zero and dominated convergence applies. Inside the band set
\[
q=\arccos(\sqrt z\cos\psi),\quad 0<q<\pi.
\]
Then \(U_{N-1}(\cos q)=\sin(Nq)/\sin q\) and
\[
d\psi=\frac{\sin q}{\sqrt{z-\cos^2q}}\,dq.
\]
For each interior \(q\), the integrand is \(\big[1+a(q)\sin^2(Nq)\big]^{-1}\), with \(a(q)=(z-1)/\sin^2q\). On a compact subinterval of \((0,\pi)\), the average over rapidly oscillating \(Nq\) converges in the integral to its phase average \((1+a(q))^{-1/2}\). To justify this without a pointwise convergence claim, approximate the periodic dependence in the fast phase uniformly by trigonometric polynomials on that compact subinterval; all nonzero Fourier modes vanish on integration by the Riemann–Lebesgue lemma. The small omitted endpoint intervals contribute arbitrarily little because the integrand lies in \([0,1]\) and the measure density above is integrable. Consequently the band contribution tends to
\[
\frac1\pi\int_0^\pi\frac{\sin^2q}{z-\cos^2q}\,dq
=1-\frac{z-1}{\sqrt{z(z-1)}}=1-\sqrt{1-z^{-1}},
\]
where the last equality uses \(\pi^{-1}\int_0^\pi(z-\cos^2q)^{-1}dq=[z(z-1)]^{-1/2}\). Formula (3) also holds at \(z=1\), because the integrand in (2) is identically one there.

**4. Outer phase integral and its elementary evaluation.** Dominated convergence in \(\varphi\), using \(0\le I_N\le1\), gives
\[
G_\infty(b)=1-\frac1\pi\int_0^\pi
\frac{b|\tan\varphi|}{\sqrt{1+b^2\tan^2\varphi}}\,d\varphi.
\tag{4}
\]
By symmetry and the substitution \(u=\cos\varphi\),
\[
G_\infty(b)=1-\frac{2b}{\pi}\int_0^1\frac{du}{\sqrt{b^2+(1-b^2)u^2}}.
\tag{5}
\]
Integrating (5) gives the stated \(\operatorname{arsinh}\), equality and \(\arcsin\) branches. The integral proves strict positivity for each finite \(b>0\) and strict decrease in \(b\); the integrand in (4) is strictly below one for almost every \(\varphi\). Standard real expansions of \(\operatorname{arsinh}\) at infinity and \(\arccos(1/b)\) at \(b=\infty\) give the two endpoint laws.

## Verification

The accompanying standalone `CHECK.py` uses only the Python standard library. It reconstructs the Chebyshev-integral formula (2) independently by midpoint quadrature, checks the exact \(N=1,2\) averages at several couplings, compares finite arrays with the long-array limit, and verifies the analytical endpoint expansions. It evaluates the exact formulas from the same normalized physical parameter \(b\); no symbolic algebra or large-\(N\) experiment is treated as proof of (3).

## Relationship to prior work

Buhrii–Golovaty–Hryniv [1] obtain the scattering probability for the scale-invariant quantum-graph array, its two-phase representation, irrational-length quasiperiodicity, antiresonances and large-array pass/gap distinction. All of those are used as inputs. Their large-\(N\) analysis addresses transmission peaks and gaps, whereas the present statement computes the *sequential broadband mean* and its logarithmic weak-coupling boundary. The exact phase average in (3), its outer evaluation (5), and the \(N=1,2\) broadband benchmarks are the additional claim.

The finite-periodic superlattice work [2] discusses miniband-averaged transmission and antireflection coatings, but concerns a different potential and energy-window weighting; its reported average transmission does not provide formula (5). Rughunanan and collaborators [3] give general waveguide transfer/phase methods and pass/stop-band bounds. Those structural tools could, after a dedicated identification and integration, yield a broader transfer-matrix derivation of aspects of the present result. No directly dominating incommensurate two-phase broadband formula was identified in the accessible material. Absence from indexed results is not proof of absolute historical novelty.

## Limitations

The order of limits is essential. The statement does **not** claim a pointwise limit of \(T_N(k)\) in the pass bands, an energy-weighted transmission mean, uniform convergence near rational geometry, dissipation/decoherence robustness, or a rate of convergence in \(N\). The source transfer formula remains the necessary model input. Earlier general Fabry–Pérot/periodic-transfer methods could imply the result as a specialized application; formal publication-priority review would need access to all potentially dominating full texts. The exact broadband function is a model-specific, self-contained mathematical result rather than a new general scattering formalism.

## References

[1] K. Buhrii, Y. Golovaty and R. Hryniv, *Scattering in Quantum Graphs with Scale-Invariant Vertex Couplings: Resonances, Gaps and (Quasi-)Periodic Transmission*, arXiv:2606.14931, first version June 12, 2026, https://arxiv.org/abs/2606.14931, especially Theorem 1(i), Proposition 2, Property 6 and Section 6.

[2] C. N. Veenstra, W. van Dijk, D. W. L. Sprung and J. Martorell, *Time dependence of transmission in semiconductor superlattices*, arXiv:cond-mat/0411118, 2004, https://arxiv.org/abs/cond-mat/0411118.

[3] L. Rughunanan, B. R. Mace, V. Sorokin and D. du Toit, *On the behaviour of infinite, periodic, mono-coupled waveguides using a transmission coefficient phase method*, Mechanical Systems and Signal Processing **135** (2020), 106409, https://doi.org/10.1016/j.ymssp.2019.106409.
