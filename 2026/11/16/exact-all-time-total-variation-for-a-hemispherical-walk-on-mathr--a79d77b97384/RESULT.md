# Exact all-time total variation for a hemispherical walk on \(\mathrm{SU}(2)\)

## Finding
Let \(G=\mathrm{SU}(2)\), identified isometrically with the unit quaternions \(S^3\), and let \(m\) denote normalized Haar measure. Set \(H=\{q\in G:\operatorname{Re}q>0\}\), let \(\mu=2\mathbf1_Hm\), and write \(f_t=d\mu^{*t}/dm\) for integers \(t\ge1\). Put \(\theta(q)=\arccos(\operatorname{Re}q)\in[0,\pi]\) and define total variation distance by \(\|\nu-m\|_{\mathrm{TV}}=\sup_E|\nu(E)-m(E)|=\tfrac12\int|d\nu/dm-1|\,dm\).

For **every** integer \(t\ge1\), the conjugation-invariant density \(f_t\) is nonincreasing in \(\theta\), and \(f_t(q)+f_t(-q)=2\) almost everywhere. In particular the same hemisphere is an optimal total-variation distinguishing set at every time:
\[
\boxed{\|\mu^{*t}-m\|_{\mathrm{TV}}=\mu^{*t}(H)-\tfrac12.}
\]
More precisely, with \(\lambda_k=(-1)^k4/[\pi(2k+1)(2k+3)]\),
\[
\boxed{\|\mu^{*t}-m\|_{\mathrm{TV}}=\frac12\sum_{k=0}^{\infty}(2k+2)^2\lambda_k^{\,t+1},\quad t=1,2,3,\ldots.}
\]
The series is absolutely convergent even for \(t=1\). At two steps the full density and total variation have the elementary closed forms
\[
\boxed{f_2(q)=2\left(1-\frac{\theta(q)}{\pi}\right),\qquad\|\mu^{*2}-m\|_{\mathrm{TV}}=\frac14-\frac1{\pi^2}.}
\]
The sharp mixing asymptotic is
\[
\|\mu^{*t}-m\|_{\mathrm{TV}}\sim\frac8{3\pi}\left(\frac4{3\pi}\right)^t.
\]

## Assumptions and scope
The group multiplication is quaternion multiplication, the steps are independent and distributed according to normalized Haar measure **conditioned on positive real part**, and \(t\) is a positive integer. The open/closed hemisphere distinction is immaterial because the boundary is Haar-null. Angles are in radians. The theorem concerns total variation with the probability-metric convention (half the \(L^1\) difference); a convention using the total variation norm of a signed measure doubles every distance displayed here.

## Proof
**1. Radial monotonicity is preserved under convolution.** Write \(d(u,v)=\arccos\langle u,v\rangle\) for geodesic distance on \(S^3\). Quaternion multiplication is an isometry, so \((a*b)(x)=\int_{S^3}a(d(e,y))b(d(y,x))\,dm(y)\) for nonnegative radial functions \(a,b\). For caps \(C_a(u)=\{y:d(u,y)\le a\}\) and \(C_b(v)\), their overlap area is nonincreasing in the center separation \(d(u,v)\in[0,\pi]\). Here is a direct geometric argument: fix the two-plane through \(u,v\) and disintegrate the spherical measure over the length of the orthogonal projection onto this plane. Conditional on a nonzero projection length, its angle is uniform on a circle, and each cap condition is a centered circular arc (possibly empty or full). The overlap length of two centered circular arcs is nonincreasing as the angular separation of their centers increases from zero to \(\pi\); this follows by interval intersection, including long arcs by taking complements. Integrating the conditional overlap proves the claim. The layer-cake representation of nonnegative nonincreasing radial functions as positive mixtures of centered-cap indicators now implies that the convolution of any two such functions is radial nonincreasing. Since \(f_1=2\mathbf1_H\) has this property, induction gives radial monotonicity of \(f_t\) for every \(t\ge1\).

**2. Antipodal complementarity and the maximizing event.** Let \(h=f_1-1\). The central involution \(-e\) sends \(h\) to \(-h\), and convolution with the constant density one annihilates every mean-zero function. Consequently \(f_t=1+h^{*t}\); since multiplication by \(-e\) may be applied to any one convolution factor, \(h^{*t}(-q)=-h^{*t}(q)\). Therefore \(f_t(\theta)+f_t(\pi-\theta)=2\). Because \(f_t\) is radial nonincreasing, \(f_t\ge1\) almost everywhere on \(H\), and \(f_t\le1\) on its antipodal complement. By the characterization of total variation as the integral of the positive part, \(H\) is an optimal event and \(\|\mu^{*t}-m\|_{\mathrm{TV}}=\int_H(f_t-1)\,dm\).

**3. Exact Fourier expression.** The irreducible \(\mathrm{SU}(2)\) representations are indexed by \(n\ge0\), with dimension \(d_n=n+1\) and real-valued character \(\chi_n(\theta)=\sin((n+1)\theta)/\sin\theta\). Haar measure on central functions is \(2\sin^2\theta\,d\theta/\pi\). Centrality makes the Fourier transform scalar. For \(n\ge1\), its eigenvalue is
\[
\alpha_n=\frac{4}{\pi(n+1)}\int_0^{\pi/2}\sin\theta\sin((n+1)\theta)\,d\theta.
\]
Elementary sine integration yields \(\alpha_{2j}=0\) for every \(j\ge1\), and \(\alpha_{2k+1}=(-1)^k4/[\pi(2k+1)(2k+3)]\) for every \(k\ge0\). The trivial representation has eigenvalue one. Peter--Weyl inversion in \(L^2\) thus gives \(f_t=1+\sum_{k\ge0}(2k+2)\lambda_k^t\chi_{2k+1}\), interpreted in \(L^2\) for \(t=1\) and with absolute uniform convergence for \(t\ge2\). Since \(\int_H\chi_n\,dm=(d_n/2)\alpha_n\), integrating over the optimal event \(H\) gives the claimed absolutely convergent total-variation series.

**4. Two steps and exact asymptotics.** In the convolution integral, \(f_2(x)=4m(H\cap xH)\). For two hemispheres of \(S^3\) whose normals are separated by \(\theta\), the angular projection onto their normals' plane is uniform, and the intersection has normalized measure \((\pi-\theta)/(2\pi)\). Therefore \(f_2=2(1-\theta/\pi)\). Direct integration of the positive part against \(2\sin^2\theta\,d\theta/\pi\) on \([0,\pi/2]\) gives \(1/4-1/\pi^2\). Finally, \(|\lambda_0|=4/(3\pi)\), every later multiplier is smaller in modulus, and \(|\lambda_1/\lambda_0|=1/5\). Factoring the first term from the absolutely convergent total-variation series proves the sharp asymptotic; indeed,
\[
\|\mu^{*t}-m\|_{\mathrm{TV}}=2\left(\frac4{3\pi}\right)^{t+1}\left[1+4\left(-\frac15\right)^{t+1}+O\left(\left(\frac3{35}\right)^{t+1}\right)\right].
\]

## Verification
The standalone \(verify.py\) reconstructs multipliers by numerical integration, checks the two-step density and total variation by independent quadrature, and compares direct integration of truncated Fourier densities with the series for selected positive times. It is a numerical consistency check, **not** a replacement for the geometric and analytic proof above. The formulas involve a convergent infinite series; finite computation alone does not certify its convergence or the all-time maximizing event.

## Relationship to prior work
General total-variation convergence of compact-group random walks and its Fourier spectral-rate characterization are treated by Borda (2019, first-public version) and earlier work cited there. The individual hemispherical harmonic multipliers on the three-sphere can also be obtained from standard geodesic-cap averaging formulas; **those multipliers alone are not asserted to be new**. The present claim is the simultaneously valid optimal total-variation event at every step, the resulting exact all-time \(L^1\) mixing series, the two-step density, and its sharp leading constant for this specific absolutely continuous walk. General compact-group mixing theorems do not state these evaluated identities or the optimizer event for this law.

## Limitations
The result is restricted to the Haar-conditioned hemisphere law on \(\mathrm{SU}(2)\), not arbitrary central step measures or arbitrary caps. The claimed historical novelty is provisional because an equivalent specialized calculation might exist outside the literature examined. The code checks finite truncations; only the supplied proof covers all positive integers and the infinite spectral series. No independent audit has been carried out.

## References
1. B. Borda, *Equidistribution of random walks on compact groups*, arXiv:1906.09432, first public 2019-06-22, https://arxiv.org/abs/1906.09432.
2. Mathematics Subject Classification MSC2020, code 43A75 (harmonic analysis on specific compact groups), https://mathscinet.ams.org/mathscinet/msc/msc2020.html.
