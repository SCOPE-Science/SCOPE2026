# Exact two-site maximin modal-energy design for three and four Dirichlet harmonics

## Finding
Let \(m\in\{3,4\}\) and \(\phi_k(x)=\sin(k\pi x)\), for \(k=1,\ldots,m\) and \(0\le x\le1\). For two arbitrary sites \(x,y\in[0,1]\), repetitions and endpoints included, define the worst-mode spatial sensitivity
\[
\Gamma_m(x,y)=\min_{1\le k\le m}\bigl(\phi_k(x)^2+\phi_k(y)^2\bigr).
\]
Then
\[
\boxed{\max_{x,y\in[0,1]}\Gamma_3(x,y)
=\max_{x,y\in[0,1]}\Gamma_4(x,y)=\frac54.}
\]
For **both** values of \(m\), the complete set of unordered optimal pairs is
\[
\boxed{\{x,y\}=\{u,v\},\qquad
u\in\{1/5,4/5\},\quad v\in\{2/5,3/5\}.}
\]
Thus there are exactly four unordered optimal designs; each has *equal* sensitivity \(\phi_k(x)^2+\phi_k(y)^2=5/4\) for all \(1\le k\le4\). For three modes, any design repeating the same site twice has sensitivity at most \(1\), so placing two distinct sites improves the sharp repeated-site baseline by \(25\%\).

## Assumptions and scope
These are the first four **unnormalized** Dirichlet sine harmonics of the interval; multiplying every harmonic by \(\sqrt2\) doubles the modal energies without changing the maximizing sites. The maximin theorem for \(\Gamma_m\) itself needs no measurement distribution. For its Fisher-information interpretation, take a *spectrally resolved Gaussian model*: for each mode \(k\), observe \(Y_{1,k}=\theta_k\phi_k(x)+\varepsilon_{1,k}\) and \(Y_{2,k}=\theta_k\phi_k(y)+\varepsilon_{2,k}\), with independent \(\varepsilon_{j,k}\sim N(0,\sigma^2)\), \(\sigma^2>0\). The Gaussian log-likelihood separates across measurements, and its negative Hessian is \(\sigma^{-2}\operatorname{diag}(S_1,\ldots,S_m)\), where \(S_k=\phi_k(x)^2+\phi_k(y)^2\). Therefore \(\Gamma_m\) is the least Fisher information eigenvalue in units of \(\sigma^{-2}\), and the design is E-optimal for this model. Equality of noise variances alone does not determine Fisher information for other noise laws.

Temporal demixing of distinct modes is one potential way to obtain resolved channels, but the theorem **does not** assert that demixing yields the stated independent Gaussian noise with a common variance. In particular it is **not** an E-optimality theorem for the raw \(2\times m\) spatial sampling matrix, whose \(m\times m\) Gram matrix has rank at most two and therefore has zero least eigenvalue for \(m>2\). Sites may coincide, and both are freely optimized over the full closed interval.

## Proof
Write \(a=\cos(2\pi x)\), \(b=\cos(2\pi y)\), \(s=a+b\) and \(p=ab\). The Chebyshev identity \(\cos(k\theta)=T_k(\cos\theta)\) gives
\[
S_k=1-\frac12 C_k,\qquad C_k=T_k(a)+T_k(b).
\]
The first three sums, by \(T_1(z)=z\), \(T_2(z)=2z^2-1\), and \(T_3(z)=4z^3-3z\), are
\[
 C_1=s,\qquad C_2=2s^2-4p-2,\qquad C_3=4s^3-12sp-3s.
\]
We claim \(\max(C_1,C_2,C_3)\ge-1/2\) for all real \(a,b\in[-1,1]\). If \(s\ge-1/2\), this follows from \(C_1=s\). If \(s<-1/2\) and all three \(C_k\le-1/2\), the second inequality forces
\[
 p\ge L(s):=\frac{s^2-3/4}{2},
\]
whereas the third (as \(s<0\)) forces
\[
 p\le U(s):=\frac{1/2+4s^3-3s}{12s}.
\]
But the **strict** inequality
\[
24s\,[U(s)-L(s)]=(1-s)(2s+1)^2>0
\]
for \(s<-1/2\) contradicts \(U(s)\ge L(s)\), because the multiplier \(24s\) is negative. Thus \(\max_{k\le3}C_k\ge-1/2\), proving \(\Gamma_3\le5/4\) and hence \(\Gamma_4\le5/4\).

To classify equality, \(\Gamma_3=5/4\) forces \(C_1,C_2,C_3\le-1/2\). The strict argument above excludes \(s<-1/2\), and \(C_1\le-1/2\) excludes \(s>-1/2\). Therefore \(s=-1/2\). At this value \(C_2\le-1/2\) gives \(p\ge-1/4\), while \(C_3\le-1/2\) gives \(p\le-1/4\). Hence \(p=-1/4\). The two roots of \(z^2-sz+p\) are consequently
\[
\{a,b\}=\left\{\frac{\sqrt5-1}{4},-\frac{\sqrt5+1}{4}\right\}
=\{\cos(2\pi/5),\cos(4\pi/5)\}.
\]
The inverse cosine images on \([0,1]\) give precisely the four stated unordered pairs. This also proves that \(\Gamma_3=5/4\) at each pair, since all three Chebyshev sums then equal \(-1/2\).

For any integer \(k\in\{1,2,3,4\}\), the four nontrivial fifth roots of unity sum to \(-1\), so
\[
 2\left[\cos\frac{2\pi k}{5}+\cos\frac{4\pi k}{5}\right]
 =\sum_{j=1}^{4}\exp\left(\frac{2\pi i j k}{5}\right)=-1.
\]
Thus every optimal three-mode pair has \(S_4=5/4\), proving attainment for \(m=4\). Conversely any maximizer for \(m=4\) must also attain the three-mode upper bound, so no further optimizers are possible.

Finally, for a repeated site \(x=y\), reflection permits \(0\le x\le1/2\). If \(x\le1/4\), then \(\sin^2(\pi x)\le1/2\); if \(3/8\le x\le1/2\), then \(\sin^2(2\pi x)\le1/2\); if \(1/4\le x\le3/8\), then \(\sin^2(3\pi x)\le1/2\). Therefore \(\Gamma_3(x,x)\le1\) for every site, with equality at \(x=1/4\) or \(3/4\), establishing the repeated-site comparison.

## Verification
The standalone pure-Python `CHECK.py` numerically evaluates all four fifth-grid equality pairs for both \(m=3\) and \(m=4\), probes the polynomial identity at finitely many points, tests \(31{,}626\) unordered grid pairs and \(18{,}000\) fixed-seed random pairs for each band, and evaluates the repeated-site benchmark on \(5{,}001\) sites. The recorded run printed `MODAL_ENERGY_CHECKS_PASS 104334`. Numerical tests are corroboration only: the global bound, complete equality classification, and sharp comparison are proved by the displayed analytic identities, with no dependence on finite enumeration.

## Relationship to prior work
Optimal sensor placement using mode-shape energy and Fisher information is standard motivation. Hassani–Dackermann (2023, Section 3) survey effective independence, modal kinetic energy, eigenvector-product and Fisher methods. Aarset (2024, Theorem 3) studies dominant and redundant weights in relaxed/binary A-optimal experimental design.

The four-mode bound also follows from the classical Fejér kernel. With \(F_5(\theta)=|\sum_{j=0}^4 e^{ij\theta}|^2/5\), the sum \(F_5(2\pi x)+F_5(2\pi y)=2+2\sum_{k=1}^4(1-k/5)C_k\) is nonnegative. Since the weights sum to two, \(\max_{k\le4}C_k\ge-1/2\); equality forces both sites to be nontrivial fifth roots and all four \(C_k\) to be \(-1/2\). The first cosine sum then selects one point from each conjugate pair. This argument uses the fourth harmonic, whereas the global upper bound here already holds with just three harmonics.

Related exact two-sensor results for heat sampling on a finite cycle use raw observations at two times or paired conjugate-frequency frame bounds. They differ from this continuous interval and the objective on independent one-dimensional sine channels. Undiscovered equivalent small-design results remain possible.

## Limitations
The Fisher-information interpretation is limited to the independent common-variance Gaussian resolved-channel model. No robustness to temporal demixing noise correlations or general spatial-matrix E-optimality is claimed. There is no claim for five or more modes, unequal mode weights, arbitrary eigenfunctions, non-sine boundary conditions, or optimal time selection. The priority comparison is nonexhaustive.

## References
- S. Hassani and U. Dackermann, *A Systematic Review of Optimization Algorithms for Structural Health Monitoring and Optimal Sensor Placement*, Sensors 23(6):3293 (2023), first public 2023-03-20, https://doi.org/10.3390/s23063293.
- C. Aarset, *Global optimality conditions for sensor placement, with extensions to binary A-optimal experimental designs*, first public 2024-10-22, https://arxiv.org/abs/2410.16590.
- *Sharp two-time heat sampling stability on the first Fourier band*, https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-sharp-two-time-heat-sampling-stability-on-the-first-fourier-band--92a81f643ed8/RESULT.md.
- *Sharp spectral-demixed two-sensor frame bounds on finite cycles*, https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-sharp-spectral-demixed-two-sensor-frame-bounds-on-finite-cycles--b03d8e4c7818/RESULT.md.
