# Sharp five-site stability threshold and the smallest attracting rotating Stuart–Landau ring

## Finding

For the unidirectionally coupled identical Stuart–Landau system
\[
\dot z_j=z_{j+1}-z_j+\tau^{-1}(1-|z_j|^2)z_j,\qquad j\in\mathbb Z/5\mathbb Z,\quad\tau>0,
\]
let \(\vartheta=2\pi/5\), \(c=\cos\vartheta=(\sqrt5-1)/4\), and \(s=\sin\vartheta>0\). The synchronized equilibrium circle \(z_j=e^{i\phi}\) is orbitally exponentially attracting for every \(\tau>0\).

For each sign \(\sigma\in\{+1,-1\}\), the winding-one traveling-wave circle
\[
 z_j^{\sigma}(t)=\sqrt{1-\tau(1-c)}\;e^{i\sigma(j\vartheta+st)}
\]
exists precisely for \(0<\tau<(1-c)^{-1}\). Define
\[
\begin{aligned}
H(g)={1\over2}\big[&(-160+96\sqrt5)g^5+(1300-580\sqrt5)g^4\\
&+(-3640+1620\sqrt5)g^3+(5075-2295\sqrt5)g^2\\
&+(-3600+1600\sqrt5)g+1000-450\sqrt5\big].
\end{aligned}
\]
It has a unique positive root \(g_\star\in(6/5,121/100)\). Set
\[
\tau_\star={1\over g_\star+1-c}=0.526742030488\ldots.
\]
**Both winding-one circles are orbitally exponentially attracting exactly for \(0<\tau<\tau_\star\)**, and both have a positive transverse growth exponent for \(\tau_\star<\tau<(1-c)^{-1}\). At \(\tau=\tau_\star\) the transverse spectrum has precisely one additional simple imaginary conjugate pair; the nonlinear bifurcation type is not asserted.

The remaining nonconstant-winding equal-radius traveling waves on this five-site directed cycle have windings \(\pm2\); whenever they exist they are transversely unstable. Thus the five monochromatic winding classes have exactly three orbitally exponentially attracting families for \(0<\tau<\tau_\star\) (synchrony and the two oppositely rotating winding-one circles), and only synchrony for \(\tau\ge\tau_\star\). This does **not** classify all attractors. Furthermore, among unidirectional directed rings of sizes \(N\ge2\), size five is the smallest at which a nonconstant-winding equal-radius traveling wave can be orbitally exponentially attracting.

## Assumptions and scope

All solutions take values in \(\mathbb C^N\). Indices are modulo \(N\), each site couples with unit weight to its successor, and the real parameter \(\tau\) is strictly positive. A monochromatic winding-\(q\) wave is \(z_j(t)=R e^{i(q\,2\pi j/N+\Omega t+\phi)}\) with \(R>0\). Orbital exponential attraction means one simple neutral exponent induced by global phase symmetry and strictly negative real parts for all remaining Floquet exponents. The interpretation is local and transverse, not global convergence.

## Proof

**Existence and frequency.** Substitute the winding ansatz and write \(\theta=2\pi q/N\). Separating real and imaginary parts gives
\[
R^2=1-\tau(1-\cos\theta),\qquad \Omega=\sin\theta.
\]
Thus nonzero-radius waves exist precisely while the right-hand side for \(R^2\) is positive. The synchronized circle, corresponding to \(q=0\), has \(R=1\) and \(\Omega=0\).

**Exact transverse blocks.** In the co-rotating coordinate \(w_j=e^{-i(\theta j+\Omega t)}z_j\), linearize at \(w_j=R\). Writing \(\delta w_j=u_j+iv_j\), introducing \(g=R^2/\tau=\tau^{-1}-(1-\cos\theta)>0\), and letting \(S\) denote the forward cyclic shift gives the real system
\[
\begin{pmatrix}\dot u\\\dot v\end{pmatrix}
=\begin{pmatrix}
\cos\theta(S-I)-2gI&-\sin\theta(S-I)\\
\sin\theta(S-I)&\cos\theta(S-I)
\end{pmatrix}
\begin{pmatrix}u\\v\end{pmatrix}.
\]
The complex Fourier character \(k\) has \(\eta_k=e^{2\pi i k/N}-1\) and a block
\[
M_k=\begin{pmatrix}\cos\theta\,\eta_k-2g&-\sin\theta\,\eta_k\\
\sin\theta\,\eta_k&\cos\theta\,\eta_k\end{pmatrix}.
\]
Its characteristic polynomial is
\[
P_k(\lambda)=\lambda^2+2(g-\cos\theta\,\eta_k)\lambda+\eta_k^2-2g\cos\theta\,\eta_k.
\]
For \(N=5\) and \(q=1\), the zero Fourier mode has the exponents \(0\) and \(-2g\). Each pair \(k,5-k\) contributes the **real** quartic \(Q_k=P_k\overline{P_k}=\lambda^4+A_k\lambda^3+B_k\lambda^2+C_k\lambda+D_k\), for \(k=1,2\); the bar denotes conjugating polynomial coefficients only. The opposite chirality changes the signs of the off-diagonal entries in \(M_k\), so the spectrum is identical.

For \(k=1\), direct exact expansion yields
\[
\begin{aligned}
 A_1&=(8g-5+3\sqrt5)/2,\\
 B_1&=(8g^2+(-15+9\sqrt5)g+15-7\sqrt5)/2,\\
 C_1&=(3\sqrt5-5)g^2+(15-7\sqrt5)g+5\sqrt5-10,\\
 D_1&=((10-4\sqrt5)g^2+(10\sqrt5-20)g+15-5\sqrt5)/2.
\end{aligned}
\]
The second Hurwitz determinant is
\[
 \Delta_{2,1}=A_1B_1-C_1
 ={32g^3+(-70+42\sqrt5)g^2+(135-59\sqrt5)g-70+30\sqrt5\over2},
\]
and the third is \(\Delta_{3,1}=A_1B_1C_1-A_1^2D_1-C_1^2=H(g)\).

The signs of the descending coefficients of \(H\) are \((+,+,-,-,-,-)\), rigorously using \(2.236<\sqrt5<2.237\). Hence Descartes' rule allows at most one positive root, with multiplicity. Its value is negative at \(g=6/5\) and positive at \(g=121/100\); therefore it has exactly one positive root \(g_\star\), which is simple and changes sign. For \(g\ge6/5\), the five quantities \(A_1,B_1,C_1,D_1,\Delta_{2,1}\) are strictly positive: each value at \(6/5\) is positive, and each polynomial has a strictly positive derivative on this half-line. Also \(A_1,C_1,D_1>0\) for every \(g>0\), since the quadratic \(C_1\) has negative discriminant \(10\sqrt5-30<0\) and positive leading coefficient.

For \(k=2\), the corresponding quantities are
\[
\begin{aligned}
 A_2&=4g+\sqrt5,\quad B_2=4g^2+3\sqrt5g+5+\sqrt5,\\
 C_2&=(4\sqrt5g^2+(4\sqrt5+20)g+5+5\sqrt5)/2,\\
 D_2&=((5-\sqrt5)g^2+(5\sqrt5+5)g+15+5\sqrt5)/2,\\
 \Delta_{2,2}&=(32g^3+28\sqrt5g^2+(4\sqrt5+50)g+5+5\sqrt5)/2,\\
 \Delta_{3,2}&={g\over2}\big[64\sqrt5g^4+(80\sqrt5+520)g^3\\
 &\hspace{43mm}+(360+340\sqrt5)g^2+(105\sqrt5+475)g+50+50\sqrt5\big].
\end{aligned}
\]
All are strictly positive for \(g>0\). The real-quartic Routh–Hurwitz criterion therefore says both transverse quartets are strictly stable exactly when \(g>g_\star\). Since \(g=\tau^{-1}-(1-c)\) decreases strictly as \(\tau\) increases, this is precisely \(\tau<\tau_\star\). For \(0<g<g_\star\), \(\Delta_{3,1}<0\) precludes stable spectrum; absence of imaginary-axis crossings there follows from \(D_1>0\) and the fact that a nonzero imaginary root would require \(\Delta_{3,1}=0\) (because \(A_1,C_1>0\)). Hence some eigenvalue has positive real part throughout that interval. At \(g=g_\star\), \(\lambda=\pm i\sqrt{C_1/A_1}\) is a simple conjugate pair; the other two roots of \(Q_1\) have negative real part, as do the roots of \(Q_2\). The additional pair has frequency \(0.712195392328\ldots\) in the co-rotating frame.

**Excluding the other five-site waves.** For winding \(q=2\), set \(\cos\theta=-(1+\sqrt5)/4\) and examine the real quartic from Fourier pair \(k=1,4\). Its linear coefficient is
\[
 C_{(q=2,k=1)}(g)
 ={ -4\sqrt5g^2+(20-4\sqrt5)g+5-5\sqrt5 \over2}.
\]
This quadratic has negative discriminant \(20(1-\sqrt5)\) and negative leading coefficient, so \(C_{(q=2,k=1)}(g)<0\) for every \(g>0\). Hurwitz stability is impossible. In fact the quartet has a positive-real-part root: for \(g>\sqrt5/4\), \(A=4g-\sqrt5>0\) while \(C<0\) excludes nonzero imaginary-axis roots; the constant term \(D\) is positive (its quadratic discriminant is negative), excluding a zero root; for \(g\le\sqrt5/4\), the nonnegative trace \(-A\), together with \(C\ne0\) at equality, forces a positive-real-part root. Conjugation gives the same conclusion for \(q=-2\). The synchronized circle is strictly transversely stable because its Fourier modes have real parts \(\cos(2\pi k/5)-1\) in the phase direction and an additional \(-2/\tau\) in the radial direction.

**Minimal number of sites.** The nontrivial alternating wave for \(N=2\) has a phase Fourier eigenvalue \(+2\). For \(N=3\), the real quartic associated with winding one and Fourier index one has
\[
\Delta_3=-3g(4g^2-6g+3)(8g^2-21g+18)<0
\]
for all \(g>0\), since both quadratic factors have negative discriminant and positive leading coefficient. For \(N=4\), the corresponding determinant is \(\Delta_3=-64g^2<0\) for all \(g>0\); the winding-two alternating wave again has a positive phase eigenvalue. Thus no directed ring with two, three, or four sites has an orbitally exponentially attracting nonconstant-winding equal-radius wave, whereas the five-site winding-one wave is stable for \(\tau<\tau_\star\).

## Verification

Run `python verify.py` with Python 3 and SymPy. The script independently expands all required five-site Fourier quartics, checks twelve exact coefficient and Hurwitz identities, proves the positive-root isolation and necessary sign conditions, verifies the exclusion for the other winding classes, and evaluates the minimal-site obstructions. The reported decimal root and relaxation threshold are approximations only; the defining exact polynomial and rational isolating interval constitute the specification.

## Relationship to prior work

Pouradier Duteil, Poyato and Reynolds (2026, arXiv:2607.11833v1, especially their Theorem 2 and Section 4.4) establish sufficiently small relaxation parameters for stable graph-induced rotating twisted states on a class of circulant interaction graphs, but do not evaluate the sharp five-vertex transition or classify every monochromatic winding sector. The present result specializes to the elementary one-way cycle and resolves its entire finite-parameter stability diagram, as well as minimal network size.

Yanchuk and Wolfrum (2007 WIAS preprint 1213, journal version 2008) study Eckhaus-like destabilization for unidirectionally coupled oscillator networks. Pade, Lücken and Yanchuk (arXiv:1506.03923, Sections 2 and 4) discuss the unperturbed ring and quote a size-independent Eckhaus stabilization line. Their unperturbed Stuart–Landau equation is related by the parameter conversion \(\alpha=\tau^{-1}-1\) and a uniform rescaling of amplitude. Those sources establish the general spectral mechanism and qualitative stabilization; the specific evaluated real-algebraic five-site cutoff and complete five-winding classification were not found in the inspected text. The precise scope of the 2007 preprint's general criterion remains a historical-priority risk because its complete PDF could not be accessed.

## Limitations

The theorem concerns **only** the uniform-amplitude monochromatic traveling-wave families and their local transverse spectra. It does not classify arbitrary spatially nonuniform solutions, global basins, all limit cycles, or nonlinear dynamics at the extra imaginary-pair crossing. The strict inequalities are necessary: at \(\tau=\tau_\star\) exponential attraction is lost. The cutoff is sharp for the five-site directed cycle with unit one-step coupling and zero natural frequencies, not a general graph threshold. Historical priority is provisional pending complete examination of the 2007 network-spectral preprint; self-review is not independent validation.

## References

1. N. Pouradier Duteil, D. Poyato, and D. N. Reynolds, *Graph-Induced Rotational Twisted States in Systems of Identical Oscillators*, arXiv:2607.11833v1 (first posted 2026-07-13), Sections 2–4 and Theorem 2.
2. J. P. Pade, L. Lücken, and S. Yanchuk, *The Dynamical Impact of a Shortcut in Unidirectionally Coupled Rings of Oscillators*, arXiv:1506.03923; Mathematical Modelling of Natural Phenomena 8 (2013), 173–179, doi:10.1051/mmnp/20138511.
3. S. Yanchuk and M. Wolfrum, *Destabilization Patterns in Large Regular Networks*, WIAS Preprint 1213 (2007), doi:10.20347/WIAS.PREPRINT.1213; journal version *Destabilization Patterns in Chains of Coupled Oscillators*, Physical Review E 77 (2008), 026212, doi:10.1103/PhysRevE.77.026212.
