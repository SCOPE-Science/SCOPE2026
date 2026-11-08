# Log-periodic eigenbundle curvature separates compactly close Mbekhta-type shifts

## Finding

For each real \(h>0\), define the bilateral weighted forward shift \(B_h\) on the complex Hilbert space \(\ell^2(\mathbb Z)\) by
\[
 B_he_j=a_j^{(h)}e_{j+1},\qquad
 a_j^{(h)}=\begin{cases}1,&j\le 0,\\ e^{-hj},&j\ge1.\end{cases}
\]
The choice \(h=\log 2\) is the shift discussed in Aznay–Chabbabi's recent treatment of Mbekhta's example. Put \(\Omega=\{\lambda\in\mathbb C:0<|\lambda|<1\}\).

**Theorem.** All these shifts satisfy
\[
\begin{aligned}
\sigma(B_h)&=\{\lambda:|\lambda|\le1\},\\
\sigma_{\rm p}(B_h)&=\Omega,\\
\sigma_{\rm ess}(B_h)&=\{0\}\cup\{\lambda:|\lambda|=1\},
\end{aligned}
\]
where the essential spectrum is the Fredholm essential spectrum. Their quasinilpotent parts coincide as subsets of \(\ell^2(\mathbb Z)\):
\[
\mathcal H_0(B_h)=\left\{x=(x_j):\lim_{m\to\infty}|x_{-m}|^{1/m}=0\right\}.
\]
For distinct \(h,h'>0\), the difference \(B_h-B_{h'}\) belongs to every Schatten class \(S_p\), \(p>0\), yet the two shifts are **not similar**.

More precisely, \(B_h\) belongs to the rank-one Cowen–Douglas class on \(\Omega\), with the global holomorphic eigenvector
\[
 v_h(\lambda)=\sum_{m\ge0}\lambda^m e_{-m}
 +\sum_{n\ge1}e^{-hn(n-1)/2}\lambda^{-n}e_n.
\]
Write \(H_h(r)=\|v_h(\lambda)\|^2\) when \(|\lambda|=r\), and define the **positive normalized negative curvature**
\[
 Q_h(r)=r^2\,\partial_\lambda\partial_{\bar\lambda}\log H_h(|\lambda|).
\]
The usual Hermitian line-bundle curvature coefficient is \(-Q_h(r)/r^2\). For \(s\in\mathbb R\) define
\[
\Theta_h(s)=\sum_{n\in\mathbb Z}e^{-h(n-s)^2},\qquad
V_h(s)=\frac1{2h}+\frac{(\log\Theta_h)''(s)}{4h^2}.
\]
Then, **uniformly over logarithmic phase** as \(t\to\infty\),
\[
\boxed{\quad Q_h(e^{-t})=V_h\left(\frac{t}{h}+\frac12\right)+o(1).\quad}
\]
The function \(V_h\) is nonconstant, smooth, and has **least positive period exactly \(1\)**. Its period mean and the resulting radial-curvature Cesàro limit are
\[
\int_0^1V_h(s)\,ds=\frac1{2h},\qquad
\boxed{\ \lim_{T\to\infty}\frac1T\int_1^TQ_h(e^{-t})\,dt=\frac1{2h}.\ }
\]
Thus the logarithmically oscillating curvature recovers the damping coefficient \(h\) although the spectra and quasinilpotent parts do not. In particular, this normalized curvature **never has a limit** as \(r\downarrow0\).

## Assumptions and scope

The Hilbert space is complex, \(h\) is any fixed positive real number, and no bounded-below hypothesis is imposed on \(B_h\). All spectral sets and operator ideals are in the usual Hilbert-space sense. The theorem concerns the explicit exponentially damped positive tail, not arbitrary bilateral shifts. The rank-one eigenbundle is taken over the punctured open unit disk, rather than the full disk (where \(0\) is not an eigenvalue).

## Proof

**1. Spectral normal form.** Split \(\ell^2(\mathbb Z)=H_-\oplus H_+\), with \(H_-\) spanned by \(e_j\) for \(j\le0\) and \(H_+\) by \(e_j\) for \(j\ge1\). In this splitting,
\[
 B_h=\begin{pmatrix}L&0\\E&R_h\end{pmatrix},
\]
where \(L\) is the standard unilateral backward shift, \(E\) sends \(e_0\) to \(e_1\) and vanishes on the other basis vectors, and \(R_he_j=e^{-hj}e_{j+1}\) for \(j\ge1\). The operator \(R_h\) is compact, with
\[
\|R_h^n\|=e^{-hn(n+1)/2};
\]
therefore it is quasinilpotent. For \(0<|\lambda|<1\), \(L-\lambda I\) is onto with one-dimensional kernel and \(R_h-\lambda I\) is invertible, so the triangular operator \(B_h-\lambda I\) is onto with one-dimensional kernel and Fredholm index \(1\). For \(|\lambda|>1\), \(B_h-\lambda I\) is invertible because \(\|B_h\|=1\). At \(\lambda=0\), the shift is injective but not bounded below, since \(\|B_he_j\|\to0\) as \(j\to+\infty\). Finally, \(B_h\) differs by a compact operator from \(L\oplus0_{H_+}\), whose Fredholm essential spectrum is the unit circle together with \(0\). These observations yield the stated whole and essential spectra. The eigenvector recurrence gives the displayed \(v_h\) and proves that there are no point eigenvalues at \(0\) or on the unit circle.

**2. Holomorphic eigenbundle.** The two series defining \(v_h\) converge in norm, locally uniformly on \(\Omega\); the second converges for every nonzero \(\lambda\) because of Gaussian coefficient decay. Direct substitution gives \(B_hv_h(\lambda)=\lambda v_h(\lambda)\). It is a holomorphic frame of the one-dimensional kernel. If a vector is orthogonal to these eigenvectors for all \(\lambda\in\Omega\), uniqueness of the resulting Laurent series shows every coordinate is zero. Thus the eigenvectors span densely, verifying the remaining Cowen–Douglas condition.

**3. Common quasinilpotent part.** Define \(\mathcal H_0(B_h)=\{x:\|B_h^n x\|^{1/n}\to0\}\). Since all weights met by the orbit of \(e_{-n}\) through time \(n\) equal one, \(|x_{-n}|\le\|B_h^n x\|\), giving necessity. Conversely, if \(|x_{-m}|^{1/m}\to0\), the negative-coordinate tail at depths \(m\ge\lfloor n/2\rfloor\) has norm smaller than \(O(\rho^{n/2})\) for every fixed \(0<\rho<1\). For the remaining negative coordinates, the first \(n\) steps necessarily traverse at least \(\lfloor n/2\rfloor-1\) successive positive-tail weights, whose product is bounded above by \(\exp(-c_h n^2)\) for sufficiently large \(n\). The positive-coordinate part obeys \(\|B_h^n|_{H_+}\|\le e^{-hn(n+1)/2}\). Combining the three disjoint-input pieces gives \(\|B_h^n x\|^{1/n}\to0\). None of these conditions depends on \(h\).

**4. Exact curvature as a variance.** Parseval's identity gives
\[
H_h(r)=\frac1{1-r^2}+\sum_{n\ge1}e^{-hn(n-1)}r^{-2n}.
\]
View this as the partition sum \(\sum_{k\in\mathbb Z}c_k r^{2k}\), where \(c_k=1\) for \(k\ge0\) and \(c_{-n}=e^{-hn(n-1)}\) for \(n\ge1\). The normalized summands form a probability distribution \(\mu_r\) on \(\mathbb Z\). Differentiating in \(u=\log r\) yields
\[
\frac{d^2}{du^2}\log H_h(e^u)=4\operatorname{Var}_{\mu_r}(k),
\qquad Q_h(r)=\frac14\frac{d^2}{du^2}\log H_h(e^u)
       =\operatorname{Var}_{\mu_r}(k).
\]
The equalities follow from the radial Wirtinger derivative formula and local absolute convergence. In particular, normalization and curvature signs are fixed intrinsically.

**5. Discrete-Gaussian asymptotics.** Let \(t=\log(1/r)\) and \(s=t/h+1/2\). Completing the square gives the exact identity
\[
e^{-hn(n-1)}r^{-2n}=e^{hs^2}e^{-h(n-s)^2}.
\]
Consequently,
\[
e^{-hs^2}H_h(e^{-t})=\Theta_h(s)+\varepsilon_h(s),
\quad
\varepsilon_h(s)=\frac{e^{-hs^2}}{1-e^{-2h(s-1/2)}}
                 -\sum_{n\le0}e^{-h(n-s)^2}.
\]
For large \(s\), the first term and the omitted Gaussian left tail, together with their first two \(s\)-derivatives, are bounded by \(C_h(1+s)^2e^{-hs^2}\). On the other hand, \(\Theta_h(s)\ge e^{-h/4}\), since an integer lies at distance at most \(1/2\) from \(s\). Differentiating twice therefore gives, uniformly as \(s\to+\infty\),
\[
Q_h(e^{-t})=\frac1{2h}+\frac{(\log\Theta_h)''(s)}{4h^2}
       +O_h\bigl((1+s)^2e^{-hs^2}\bigr).
\]
This proves the claimed uniform-phase limit.

**6. Nonconstant least-period-one profile.** Gaussian Fourier integration and Fourier series convergence provide
\[
\Theta_h(s)=\sqrt{\frac\pi h}\sum_{k\in\mathbb Z}
  e^{-\pi^2k^2/h}e^{2\pi i k s}.
\]
Every displayed coefficient is positive, including the first nonconstant coefficient, so \(\Theta_h\) is nonconstant with least period \(1\). The identity defining \(V_h\) also shows it is periodic and that its mean is \(1/(2h)\). If \(V_h\) had a positive period \(\delta\), then \((\log\Theta_h)''\) would also have period \(\delta\). Hence \(\log\Theta_h(s+\delta)-\log\Theta_h(s)\) would be affine. Because \(\log\Theta_h\) is bounded, this affine function must be constant, and its iterates force the constant to vanish. Thus \(\Theta_h\) has period \(\delta\), so \(\delta\) is an integer. The least positive period is therefore \(1\), and \(V_h\) is nonconstant. Average the uniform asymptotic along \(t\), using period \(h\), to obtain the stated Cesàro limit. Periodic nonconstancy gives distinct phase-dependent subsequential limits as \(r\downarrow0\).

**7. No similarity despite arbitrarily regular differences.** The difference is a weighted shift supported on indices \(j\ge1\), with singular values \(|e^{-hj}-e^{-h'j}|\). Hence for every \(p>0\),
\[
\|B_h-B_{h'}\|_{S_p}^{p}=\sum_{j\ge1}|e^{-hj}-e^{-h'j}|^p<\infty.
\]
If an invertible bounded operator \(S\) intertwined \(B_h\) and \(B_{h'}\), one-dimensionality of their eigenfibers would give a nonvanishing holomorphic function \(\phi\) on \(\Omega\) with \(Sv_h(\lambda)=\phi(\lambda)v_{h'}(\lambda)\). Two-sided bounds for \(S\) imply
\[
\log H_h(r)-\log H_{h'}(r)=2\log|\phi(\lambda)|+O(1),
\]
uniformly in the argument of \(\lambda\). The angular mean of \(\log|\phi|\) is a harmonic radial function, hence affine in \(\log r\). However the Gaussian identity above gives
\[
\log H_h(e^{-t})=\frac{t^2}{h}+t+O_h(1),
\]
and similarly for \(h'\). If \(h\ne h'\), the difference has a nonzero quadratic coefficient in \(t\), incompatible with an affine function up to a bounded error. Therefore \(B_h\) and \(B_{h'}\) are not similar.

## Verification

The standalone script `verify.py` evaluates finite truncations of the eigenvector recurrence, the discrete-Gaussian variance and its period mean, and the large-log-radius curvature approximation. Running it under Python 3 (standard library only) prints `BILATERAL_CURVATURE_FINITE_CONSISTENCY_OK 272`. This is consistency evidence, **not** a proof of the infinite-dimensional, least-period, or nonsimilarity claims; those follow from the preceding arguments.

## Relationship to prior work

Aznay and Chabbabi (arXiv:2610.23229, first submitted 2026-10-16) analyze the \(h=\log2\) Mbekhta shift in pseudo-Fredholm theory and determine its analytic-core/quasinilpotent-part behavior; their relevant Section 2 has no eigenbundle curvature, theta limit or parameter recovery theorem. Cowen–Douglas geometry and the use of curvature as a rank-one unitary invariant are classical; see Cowen–Douglas (1978) and Jiang–Ji–Keshari (2019/2023). The present result concerns the **explicit logarithmic phase profile, its least period, its exact mean and similarity separation** for an operator family whose coarse spectral features coincide. Older work by Clark–Misra (1985) on weighted shifts, curvature, and similarity and by Ji–Li–Yang (2001) on bilateral Cowen–Douglas shifts is directly relevant; its full text could not be inspected, leaving a publication-priority caveat.

## Limitations

The curvature statement is a boundary asymptotic on \(\Omega\), not a curvature formula at \(\lambda=0\), which lies outside the eigenvalue domain. The asymptotic error constant depends on fixed \(h>0\); uniformity as \(h\to0\) is not claimed. There is no independent certification of novelty or independent mathematical audit. Accessible older literature does not rule out an equivalent earlier theta-asymptotic calculation; an exact previous formulation would supersede the originality assessment. Finite numerical checks do not establish the infinite results.

## References

1. Z. Aznay and F. Chabbabi, *On Mbekhta's conjecture and pseudo-Fredholm operators on Banach and Hilbert spaces*, arXiv:2610.23229 (first public 2026-10-16), https://arxiv.org/abs/2610.23229 .
2. M. J. Cowen and R. G. Douglas, *Complex geometry and operator theory*, Acta Math. 141 (1978), 187–261.
3. C. Jiang, K. Ji and D. K. Keshari, *Geometric Similarity Invariants of Cowen–Douglas Operators*, arXiv:1901.03993 (2019), https://arxiv.org/abs/1901.03993 .
4. D. N. Clark and G. Misra, *On Weighted Shifts, Curvature and Similarity*, J. London Math. Soc. s2-31 (1985), 357–368, https://doi.org/10.1112/jlms/s2-31.2.357 .
5. Y. Q. Ji, J. Li and Y. Yang, *A Characterization of Bilateral Operator Weighted Shifts Being Cowen–Douglas Operators*, Proc. Amer. Math. Soc. 129 (2001), 3205–3210, https://doi.org/10.1090/S0002-9939-01-06031-2 .
