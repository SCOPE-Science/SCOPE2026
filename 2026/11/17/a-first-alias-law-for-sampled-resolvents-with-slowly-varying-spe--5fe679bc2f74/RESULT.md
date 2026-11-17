# A first-alias law for sampled resolvents with slowly varying spectral damping

## Finding
For a nondecreasing continuous damping profile \(a:[0,\infty)\to[0,\infty)\), let \(H=L^2(\mathbb R)\) and let \(B\) multiply by \(-a(|\xi|)+i\xi\) on its maximal domain. Write \(S_t=e^{tB}\), fix \(\lambda>0\), and set
\[
Q_T=T(I-e^{-\lambda T}S_T)^{-1},\qquad E_T=Q_T-\frac T2 I-(\lambda-B)^{-1},\qquad T>0.
\]
Then the following two assertions hold.

**(i) Exact convergence criterion and norm limit.** With \(a_\infty=\lim_{r\to\infty}a(r)\), allowing \(a_\infty=+\infty\),
\[
\lim_{T\downarrow0}\|E_T\|=
\begin{cases}
(\lambda+a_\infty)^{-1},&a_\infty<\infty,\\
0,&a_\infty=\infty.
\end{cases}
\]
In particular, corrected resolvent samples converge in operator norm if and only if the high-frequency damping tends to infinity.

**(ii) Sharp first-alias asymptotic.** If \(w(r):=\lambda+a(r)\) is regularly varying at infinity with index \(\rho\in[0,1)\), then
\[
\boxed{\displaystyle\|E_T\|\sim\frac{1}{\lambda+a(2\pi/T)}\quad(T\downarrow0).}
\]
The first temporal alias, rather than a low-frequency Taylor term, fixes the exact leading constant. For example, if \(a(r)=(\log(1+r))^\beta\) with \(\beta>0\), the norm is asymptotic to \(\bigl(\log(1/T)\bigr)^{-\beta}\). This includes arbitrarily slow logarithmic norm convergence. If instead \(a(r)=c r^\rho\) with \(c>0\) and \(0<\rho<1\), the sharp equivalent is \(c^{-1}(T/(2\pi))^\rho\).

## Assumptions and scope
The underlying Hilbert space is complex \(L^2(\mathbb R,d\xi)\); the multiplier domain is \(D(B)=\{f\in H:(-a(|\xi|)+i\xi)f(\xi)\in H\}\). The semigroup \(S_t\) is the multiplication semigroup with symbol \(e^{-t a(|\xi|)}e^{it\xi}\). Dominated convergence gives strong continuity and \(\|S_t\|\le1\). The positive Laplace parameter \(\lambda\) remains fixed. The convergence statements concern the **trapezoid-corrected** sampled resolvent, not \(Q_T\) alone. Since \(\|Q_T-(\lambda-B)^{-1}\|\) differs by at most \(T/2\), the same leading equivalents in (ii) apply to the uncorrected error when the equivalent dominates \(T\).

Regular variation means \(\lim_{r\to\infty}w(cr)/w(r)=c^\rho\) for every fixed \(c>0\). The restriction \(\rho<1\) guarantees \(T w(2\pi/T)\to0\); no smoothing, differentiability, or completeness beyond the ambient Hilbert structure is imposed on \(a\).

## Proof
**Step 1: exact scalar reduction.** Put \(r=|\xi|\), \(u=T w(r)\), \(x=T\xi\), and \(z=u-ix\). The multiplier of \(E_T\) is \(T h(z)\), where
\[
h(z)=\frac{1}{1-e^{-z}}-\frac12-\frac1z.
\]
The apparent singularity of \(h\) at zero is removable (indeed \(h(z)=z/12+O(z^3)\)). The remaining poles are at \(2\pi i k\) for nonzero integers \(k\). All operator norms below equal essential suprema of this continuous multiplier; pointwise values provide lower bounds by continuity.

**Step 2: uniformly small off-alias frequencies.** Fix \(\eta\in(0,\pi)\). On the closed region \(u\ge0\), \(|x|\le2\pi-\eta\), the function \(h(u-ix)\) is bounded by a constant \(C_\eta\). To see this, compactness handles bounded \(u\) since no nonremovable pole lies in the region, and \(h(u-ix)\to1/2\) uniformly in the bounded \(x\)-range as \(u\to\infty\). Consequently
\[
\sup_{|T\xi|\le2\pi-\eta}|T h(T w(|\xi|)-iT\xi)|\le C_\eta T.
\]

**Step 3: a global upper bound past the first alias.** For \(|x|\ge2\pi-\eta\), monotonicity gives \(w(|\xi|)\ge w((2\pi-\eta)/T)\). Since \(|1-e^{-u+ix}|\ge1-e^{-u}\) and \((1-e^{-u})^{-1}\le1+u^{-1}\) for \(u>0\),
\[
\begin{aligned}
|T h(u-ix)|
&\le\frac{T}{1-e^{-u}}+\frac T2+\frac{T}{|u-ix|}\\
&\le\frac{1}{w((2\pi-\eta)/T)}
+T\left(\frac32+\frac{1}{2\pi-\eta}\right).
\end{aligned}
\]
Combining the two frequency regions yields the global, all-profile estimate
\[
\|E_T\|\le\frac{1}{w((2\pi-\eta)/T)}+C'_\eta T.
\tag{1}
\]

**Step 4: exact first-alias lower bound.** Evaluate at \(\xi_T=2\pi/T\), where \(x=2\pi\) and \(u_T=T w(2\pi/T)\). Since \(e^{i2\pi}=1\),
\[
T h(u_T-2\pi i)=\frac{T}{1-e^{-u_T}}-\frac T2-\frac{T}{u_T-2\pi i}.
\tag{2}
\]
This is a valid operator-norm lower bound. If \(a_\infty<\infty\), then \(u_T\to0\), and (2) converges to \(1/(\lambda+a_\infty)\). Together with (1), it proves the finite-limit case of (i). If \(a_\infty=\infty\), (1) tends to zero, proving the remaining case of (i).

**Step 5: regular variation gives the exact constant.** With index \(\rho<1\), regular variation implies \(T w(2\pi/T)\to0\) and
\[
\frac{w(2\pi/T)}{w((2\pi-\eta)/T)}\to
\left(\frac{2\pi}{2\pi-\eta}\right)^\rho.
\]
Multiplying (2) by \(w(2\pi/T)\) therefore yields \(1+o(1)\) in modulus: the principal term is \(u_T/(1-e^{-u_T})\to1\), and both corrections have modulus \(O(u_T)\). From (1),
\[
1\le\liminf_{T\downarrow0}w(2\pi/T)\|E_T\|
\le\limsup_{T\downarrow0}w(2\pi/T)\|E_T\|
\le\left(\frac{2\pi}{2\pi-\eta}\right)^\rho.
\]
Letting \(\eta\downarrow0\) proves (ii). For the logarithmic and power examples substitute their elementary regular-variation equivalents. This completes the proof.

## Verification
The identity for the multiplier follows directly from the resolvent functional calculus and the geometric series \(Q_T=T\sum_{m\ge0}e^{-\lambda mT}S_{mT}\), convergent in norm for each fixed \(T>0\). The proof requires no numerical approximation or finite-dimensional surrogate. A self-contained, standard-library numerical cross-check is supplied as `verify.py`; it probes the first alias and a frequency grid, but **does not certify** the universal theorem. In particular, the exact numerical constant and the all-profile quantifiers are established by Steps 1–5, not by sampling.

## Relationship to prior work
Castillo's *Dyadic Resolvent Representations of Self-Adjoint Operators* (first public version 23 July 2026) develops resolvent reconstruction from propagator samples and establishes a strong-operator limit for the sampled expression in the self-adjoint/unitary setting. It does not provide the damping-dependent norm criterion or this regular-variation first-alias constant for normal nonunitary multiplier semigroups.

The later *Sampled resolvents of \(C_0\)-semigroups: aliasing and sharp rates on the Crandall–Pazy scale* (first public version 11 November 2026) derives general Crandall–Pazy norm upper rates for positive power exponents and a discrete sharpness construction. Its results do not imply logarithmic decay at the zero-power boundary, nor the exact leading constant along an entire class of continuous normal spectra. The present analysis is a specialized complementary result, not a replacement for the general semigroup theory. Classical spatial-grid norm-resolvent approximation and long-time semigroup decay are different questions.

## Limitations
The classification is proved only for a normal multiplication generator whose damping is continuous, even and nondecreasing in frequency. The explicit sharp equivalent additionally assumes regular variation of index below one. No result is asserted for nonnormal generators, arbitrary spectral supports, oscillatory damping, or the critical regular-variation index one. A bibliographically unindexed earlier treatment of this exact Fourier-multiplier quadrature remains possible; independent mathematical validation and priority verification have not been performed.

## References
1. N. Castillo, *Dyadic Resolvent Representations of Self-Adjoint Operators: Propagator Expansions, Spectral Measures, and Zeta Functions*, arXiv:2607.21278, initial public version 2026-07-23, https://arxiv.org/abs/2607.21278.
2. N. Castillo, *Sampled resolvents of \(C_0\)-semigroups: aliasing and sharp rates on the Crandall–Pazy scale*, arXiv:2611.15563, initial public version 2026-11-11, https://arxiv.org/html/2611.15563v1.
3. H. D. Cornean, H. Garde, A. Jensen, *Norm resolvent convergence of discretized Fourier multipliers*, arXiv:2010.16215, https://arxiv.org/abs/2010.16215 (spatial discretization, distinct setting).
