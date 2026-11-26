# Parity-dependent flux-detuning lifetime on a lossy quantum ring

## Finding
For a finite coherent quantum ring with a single irreversible absorber, a weak magnetic flux changes infinitely long-lived dark modes into very slowly decaying modes. The inverse-square divergence of the **mean integrated survival time** has a universal explicit, parity-dependent coefficient:
\[
\lim_{\phi\to0}\phi^2T_{n,a}(\phi,\gamma)=
\begin{cases}
\dfrac{\gamma a(n-a)}4,&n\text{ odd},\\[4pt]
\dfrac{\gamma b(m-b)}2,&n=2m\text{ even},\quad b=a\bmod m,\ 0\le b<m.
\end{cases}
\]
The source at the absorber and, on even rings, its antipode are the only source positions with bounded mean lifetime near zero flux.

## Assumptions and scope
Fix integers \(n\ge3\), \(0\le a<n\), and a real loss strength \(\gamma>0\). Label ring vertices by \(\mathbb Z/n\mathbb Z\). Define the Hermitian matrix \(H_\phi\) by
\[
\langle j|H_\phi|j+1\rangle=e^{i\phi/n},\qquad
\langle j+1|H_\phi|j\rangle=e^{-i\phi/n},
\]
with indices modulo \(n\) and all other entries zero. The phase around the entire ring is \(\phi\). Let \(K_\phi=H_\phi-i\gamma|0\rangle\langle0|\), and set
\[
T_{n,a}(\phi,\gamma)=\int_0^\infty\big\|e^{-itK_\phi}|a\rangle\big\|^2dt.
\]
The survival is unnormalized after absorption. Every asymptotic statement fixes \(n,a,\gamma\) and takes real \(\phi\to0\) through nonzero values. For such sufficiently small flux all the modes decay and the integral is finite. For \(a=0\), and for \(a=n/2\) when \(n\) is even, the integral stays \(O(1)\); elsewhere it diverges at the displayed strictly positive inverse-square rate.

## Proof
**1. Dark modes at zero flux.** The eigenvalues of the unthreaded cycle adjacency operator are \(E_k=2\cos(2\pi k/n)\). For \(1\le k\le r=\lfloor(n-1)/2\rfloor\), their sine eigenvectors
\[
 d_k(j)=\sqrt{\frac2n}\sin\frac{2\pi kj}{n}
\]
are normalized, vanish at the absorbing vertex, and hence satisfy \(K_0d_k=E_kd_k\). These are all the real eigenmodes of \(K_0\): if \(K_0u=zu\) and \(\operatorname{Im}z=0\), the dissipativity identity \(\operatorname{Im}\langle u,K_0u\rangle=-\gamma|u(0)|^2\) forces \(u(0)=0\). Each eigenvalue \(E_k\) is isolated and simple within \(K_0\) (only one vector in its two-dimensional Fourier pair can vanish at the trap). The complementary spectrum has strictly negative imaginary parts.

**2. Weak-flux resonances.** The eigenvalues of \(H_\phi\) are \(\epsilon_j(\phi)=2\cos((2\pi j+\phi)/n)\). For sufficiently small nonzero \(\phi\) their values are pairwise distinct; every Fourier eigenvector is nonzero at vertex zero. Consequently every eigenvalue of \(K_\phi\) has strictly negative imaginary part and absorption is certain. The determinant lemma gives the scalar secular equation
\[
1+i\gamma g_\phi(z)=0,\qquad g_\phi(z)=\frac1n\sum_{j=0}^{n-1}\frac{1}{z-\epsilon_j(\phi)}.
\]
For each \(k\in\{1,\ldots,r\}\), write the colliding pair energies as \(\mu_k(\phi)\pm\Delta_k(\phi)\), where \(\mu_k(0)=E_k\) and \(\Delta_k(\phi)=v_k\phi+O(\phi^3)\) up to sign, with \(v_k=2\sin(2\pi k/n)/n\). Splitting off this pair gives
\[
 g_\phi(z)=\frac{2(z-\mu_k)}{n((z-\mu_k)^2-\Delta_k^2)}+h_k(z,\phi),
\]
where \(h_k\) is analytic and real at \((E_k,0)\). The branch \(z_k(\phi)\) issuing from the dark eigenvalue satisfies \(z_k-\mu_k=O(\phi^2)\). Substitution into the secular equation yields
\[
 z_k(\phi)-\mu_k(\phi)
 =\frac n2\Delta_k(\phi)^2\left(h_k(E_k,0)-\frac{i}{\gamma}\right)+O(\phi^3).
\]
In particular,
\[
-\operatorname{Im}z_k(\phi)
=\frac{2}{\gamma n}\sin^2\frac{2\pi k}{n}\,\phi^2+O(\phi^3).
\]
The expansion is justified by analytic perturbation of the simple isolated zero-flux eigenvalue. It also shows that all remaining modes retain a uniform positive decay rate.

**3. Integrated survival.** The analytic spectral projection onto the \(k\)-th slow branch satisfies
\[
 \|P_k(\phi)|a\rangle\|^2=\frac2n\sin^2\frac{2\pi ka}{n}+O(\phi).
\]
The integral of its diagonal exponential contribution is the displayed weight divided by twice its decay rate. Different slow branches have distinct limiting real energies, so their oscillatory cross-term time integrals remain bounded even though their damping tends to zero. Terms involving the complementary fast sector are also bounded, by the uniform spectral gap and finite-dimensional semigroup estimates. Thus
\[
\lim_{\phi\to0}\phi^2 T_{n,a}(\phi,\gamma)
=\frac\gamma2\sum_{k=1}^{r}\frac{\sin^2(2\pi ka/n)}{\sin^2(2\pi k/n)}.
\]
If the sine numerator vanishes for every \(k\), the corresponding slow spectral amplitudes are \(O(\phi)\) and all contributions are \(O(1)\), proving the bounded-source assertion.

**4. Evaluation of the spectral sum.** For \(q\ge2\) and \(0\le c<q\), orthogonality of the nontrivial \(q\)-th roots of unity yields the elementary identity
\[
\sum_{k=1}^{q-1}\frac{\sin^2(\pi kc/q)}{\sin^2(\pi k/q)}=c(q-c).
\]
Indeed, \(\sin(\pi kc/q)/\sin(\pi k/q)\) has squared magnitude equal to that of the length-\(c\) geometric sum, and Parseval gives \(qc-c^2\) after deleting the zero Fourier mode. For odd \(n\), multiplying Fourier indices by two permutes the nonzero residue classes; the relevant half-sum is \(a(n-a)/2\). For \(n=2m\), the sum runs over precisely \(k=1,\ldots,m-1\) with argument \(\pi k/m\), so it is \(b(m-b)\), where \(b=a\bmod m\). Substitution proves both cases. The sum vanishes only at the stated source positions. \(\square\)

## Verification
The standalone program `verify.py` evaluates the exact sine-sum identity and independently solves a finite-dimensional continuous Lyapunov equation for the integrated survival time. Run `python verify.py` after installing the packages named in `requirements.txt`. A successful checked run produced 674 finite/spectral checks. The computed values substantiate the formula in finite samples; the all-size claim relies on the analytic proof above.

## Relationship to prior work
Krapivsky, Luck and Mallick [1] establish dark-sector survival for unthreaded quantum rings with local traps; they do not derive the leading flux-detuned mean lifetime. Agliari, Mülken and Blumen [2] study finite quantum walks with trapping, including unthreaded rings. Finocchiaro and collaborators [3] treat chiral rings with repeated projective measurements, not the continuous imaginary local absorber used here. Gou and collaborators [4] investigate a dissipative Aharonov–Bohm ring experimentally, in a different lattice transport arrangement. The zero-flux dark-mode existence and general spectral method are known; the claimed contribution is the quantitative two-sided weak-flux lifetime law, including its parity and source-position coefficient. General observability or non-Hermitian perturbation results might imply parts of this specialization; historical priority is not conclusively certified.

## Limitations
The statement assumes a single absorber, uniform hopping amplitudes, spatially uniform flux, fixed positive loss strength and fixed finite ring size. The coefficient is not uniform in ring size or absorption strength. No claim is made about nonlinear environments, decoherence, distinct absorber arrangements, higher order flux terms, or a full absorption-time distribution. Independent validation has not been performed.

## References
[1] P. L. Krapivsky, J. M. Luck and K. Mallick, *Survival of classical and quantum particles in the presence of traps*, arXiv:1311.6298 (first public 2013-11-25), particularly section 4.2.

[2] E. Agliari, O. Mülken and A. Blumen, *Continuous-time quantum walks and trapping*, arXiv:0903.3288.

[3] S. Finocchiaro et al., *Optimal quantum transport on a ring via locally monitored chiral quantum walks*, arXiv:2507.10669 (a later comparison source).

[4] W. Gou et al., *Tunable non-reciprocal quantum transport through a dissipative Aharonov–Bohm ring in ultracold atoms*, arXiv:2001.01859.
