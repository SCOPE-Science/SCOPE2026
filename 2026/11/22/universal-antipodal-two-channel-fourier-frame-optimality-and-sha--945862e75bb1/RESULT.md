# Universal antipodal two-channel Fourier-frame optimality and sharp cyclic heat bounds

## Finding

Let \(N=2R\ge2\). Let \(g\in\mathbb C^N\) have strictly radially decreasing, strictly positive **Fourier energy**: for the unitary discrete Fourier transform, there are numbers
\[
a_0>a_1>\cdots>a_R>0,\qquad N|\widehat g(k)|^2=a_{d(k)},\quad d(k)=\min\{k,N-k\},\quad 0\le k<N.
\]
For any two distinct modulation channels, use **every cyclic translation**, and allow positive channel powers with fixed sum \(2\). Among all channel gaps and all such power allocations, the **unique** design up to channel relabeling and common modulation shift with the smallest squared-analysis condition number uses antipodal modulations and equal powers. Stronger: at this design the sharp lower frame bound is strictly larger and the sharp upper frame bound strictly smaller than those of every different channel gap, even if that competing gap is allowed arbitrary positive powers. At fixed antipodal gap, any unequal powers strictly worsen at least one of the two bounds.

The conclusion holds simultaneously for **every** strictly radially decreasing positive Fourier-energy profile. For the cyclic graph-heat window
\[
g_t=e^{-t\Delta_N}\delta_0,\qquad (\Delta_N f)(x)=2f(x)-f(x-1)-f(x+1),\qquad t>0,
\]
the unique design is explicit. At equal powers and antipodal gap its sharp frame bounds are
\[
B_{N,t}=2e^{-4t}\cosh(4t),\qquad
A_{N,t}=2e^{-4t}\begin{cases}
1,&N\equiv0\pmod 4,\\
\cosh\bigl(4t\sin(\pi/N)\bigr),&N\equiv2\pmod 4,
\end{cases}
\]
and therefore its optimal squared-analysis condition number is
\[
\boxed{\kappa_{N,t}^{\mathrm{opt}}=\begin{cases}
\cosh(4t),&N\equiv0\pmod4,\\
\cosh(4t)/\cosh\bigl(4t\sin(\pi/N)\bigr),&N\equiv2\pmod4.
\end{cases}}
\]
For \(N=2\) this is \(1\) at every \(t>0\). For all even \(N\ge4\) it is strictly greater than \(1\). The optimal separation and equal-power allocation do not depend on \(t\).

The selection also has an explicit **robustness margin**. If a different gap has representative \(1\le r<R\), then for every permitted pair of positive powers,
\[
\frac{\kappa_{r,w}}{\kappa_{R,1}}>
\frac{1+\exp[-8t\sin^2(\pi r/N)]}{1+\exp(-8t)}>1.
\]
At the optimal gap, unbalanced power \(w=1+\varepsilon\), \(\varepsilon\ne0\), obeys
\[
\frac{\kappa_{R,w}}{\kappa_{R,1}}\ge1+|\varepsilon|\tanh(4t)>1.
\]

## Assumptions and scope

The ambient Hilbert space is \(\mathbb C^N\) with the standard Euclidean inner product; indices belong to \(\mathbb Z_N\). Define \((T_jg)[x]=g[x-j]\), \((M_\ell g)[x]=e^{2\pi i\ell x/N}g[x]\), and \(\widehat g(k)=N^{-1/2}\sum_{x=0}^{N-1}g[x]e^{-2\pi i kx/N}\). Each channel \(\ell\) of power \(w>0\) contains the \(N\) atoms \(\sqrt w M_\ell T_jg\), \(j\in\mathbb Z_N\). The two powers \(w_0,w_1\) satisfy \(w_0,w_1>0\) and \(w_0+w_1=2\). The sharp lower and upper frame bounds \(A,B\) are the extreme eigenvalues of the frame operator; \(\kappa=B/A\) is the squared-analysis condition number. A common modulation shift merely relabels Fourier coordinates; reversing the channel order reverses the signed gap.

For the heat-window corollary, \(\delta_0\) is the unit impulse and \(\Delta_N\) is the nonnegative graph Laplacian of the cyclic nearest-neighbor graph, counted with its natural two directed neighbors also when \(N=2\). This convention gives multiplier \(\lambda_k=4\sin^2(\pi k/N)\), including \(\lambda_1=4\) for \(N=2\). The heat-window norms are not rescaled to one; rescaling all atoms changes both frame bounds by a common positive factor but never changes their ratio or their optimal design.

## Proof

**1. Complete frame spectrum (the standard full-translation Gabor identity).** Fourier transforming all translated atoms and using character orthogonality yields a diagonal frame operator in Fourier coordinates. After shifting the first modulation index to zero and writing the other as \(r\), its entries are
\[
F_{r,w}(k)=w\,a_{d(k)}+(2-w)\,a_{d(k-r)},\qquad k\in\mathbb Z_N,
\]
where \(w=w_0\in(0,2)\), \(w_1=2-w\). The factor \(N\) in the definition of \(a\) is essential: summing over \(N\) translations contributes exactly \(N\). The positivity of \(a_R\) makes every design a frame. Since \(a_{d(k)}\) is reflection symmetric, one may represent an unordered nonzero channel gap by \(1\le r\le R\).

**2. Balanced powers dominate both spectral extremes.** Write \(F_r=F_{r,1}\). Reflection across the two frequency centers exchanges weights:
\[
\frac{F_{r,w}(k)+F_{r,w}(r-k)}2=F_r(k).
\]
At an index minimizing or maximizing \(F_r\), at least one member of the reflected pair for \(F_{r,w}\) lies on the appropriate side of its average. Consequently
\[
\min_k F_{r,w}(k)\le\min_k F_r(k),\qquad
\max_k F_{r,w}(k)\ge\max_k F_r(k).
\]
Thus balancing never worsens either sharp frame bound.

**3. Strict cyclic two-arc interlacing.** At the antipodal gap \(r=R\), the unordered distance pairs are exactly \((j,R-j)\), so
\[
A_R=\min_{0\le j\le R}(a_j+a_{R-j}),\qquad
B_R=\max_{0\le j\le R}(a_j+a_{R-j}).
\]
Fix any shorter gap \(1\le r<R\). Choose \(j_+\) attaining \(B_R\). There exist integers \(u\le j_+\), \(v\le R-j_+\) with \(u+v=r\): for example \(u=\min\{r,j_+\}\), \(v=r-u\). The point \(k=u\) on the short arc between the two channel centers has distance pair \((u,v)\), so strict monotonicity and \(r<R\) give
\[
B_r\ge a_u+a_v>a_{j_+}+a_{R-j_+}=B_R.
\]
For the lower bound, choose \(j_-\) attaining \(A_R\). Put \(E=R-r\), \(\delta_1=\min\{E,R-j_-\}\), \(\delta_2=E-\delta_1\). Then \(0\le\delta_2\le j_-\), and the integers \(u=j_-+\delta_1\), \(v=R-j_-+\delta_2\) lie in \([0,R]\), satisfy \(u+v=N-r\), and have \(u\ge j_-\), \(v\ge R-j_-\). The point \(k=r+v\) on the long arc has cyclic distances exactly \((u,v)\) to the centers \((0,r)\). Therefore
\[
A_r\le a_u+a_v<a_{j_-}+a_{R-j_-}=A_R.
\]
The strict inequalities prove simultaneous optimization of both bounds by antipodal separation at equal powers, and Step 2 extends their strict dominance to all powers at every non-antipodal gap.

**4. Uniqueness of the powers.** At the antipodal gap write \(w=1+\varepsilon\). At the reflected indices \(j,R-j\), the two eigenvalues are
\[
(a_j+a_{R-j})\pm\varepsilon(a_j-a_{R-j}).
\]
If \(\varepsilon\ne0\), an extremizer for either \(B_R\) or \(A_R\) with \(j\ne R/2\) makes the corresponding sharp bound strictly worse. Such an extremizer must exist: otherwise both maximum and minimum occur only at \(j=R/2\), forcing the entire finite sequence \(a_j+a_{R-j}\) to be constant, in which case all indices (including \(j=0\)) are extremizers. Strict radial monotonicity gives \(a_j\ne a_{R-j}\) whenever \(j\ne R/2\). This proves uniqueness of equal powers and, with Step 3, uniqueness of the joint design.

**5. Exact heat-window bounds.** The eigenvectors of \(\Delta_N\) are the Fourier characters with eigenvalues \(4\sin^2(\pi k/N)\), whence \(N|\widehat g_t(k)|^2=e^{-8t\sin^2(\pi k/N)}=e^{-4t}e^{4t\cos(2\pi k/N)}\). For antipodal channels the identity \(\cos(2\pi(k-R)/N)=-\cos(2\pi k/N)\) gives
\[
F_R(k)=2e^{-4t}\cosh\bigl(4t\cos(2\pi k/N)\bigr).
\]
Its maximum occurs at \(k=0,R\), and equals \(2e^{-4t}\cosh(4t)\). Its minimum occurs where \(|\cos(2\pi k/N)|\) is smallest. This absolute cosine minimum is \(0\) if \(4\mid N\) and \(\sin(\pi/N)\) if \(N\equiv2\pmod4\). Substitution gives the displayed sharp bounds and their ratio. The case \(N=2\) is exactly tight. For \(N\ge4\), the ratio exceeds one because \(\sin(\pi/N)<1\) in the latter case and \(t>0\).

**6. Quantitative design margins.** For each \(r<R\), the Fourier eigenvalue at \(k=0\) is \(F_r(0)=1+\exp[-8t\sin^2(\pi r/N)]\). Since \(B_r\ge F_r(0)\), \(A_r<A_R\) and unequal powers can only worsen both extremes, division by \(B_R=1+e^{-8t}\) gives the first ratio bound. At the antipodal gap, the two entries \(k=0,R\) have values \(B_R\pm\varepsilon(1-e^{-8t})\). Hence \(B_{R,w}\ge B_R+|\varepsilon|(1-e^{-8t})\) while \(A_{R,w}\le A_R\). Their quotient gives the second ratio bound using \(\tanh(4t)=(1-e^{-8t})/(1+e^{-8t})\).

## Verification

The standalone `CHECK.py` requires Python 3 and NumPy. Execute `python CHECK.py` from its containing directory. It checks: (a) the strict max/min two-arc inequalities on independently generated strictly decreasing radial spectra; (b) weighted versus balanced bounds; (c) the parity-dependent heat formulas at multiple cycle sizes and diffusion times; (d) the unique best heat gap and power choice; and (e) the eigenvalues of explicitly constructed \(2N\)-atom frame matrices against the Fourier formula. A successful deterministic run prints `CHECK_OK assertions=161085`. The finite checks support the algebra but do not establish the universal theorem; Steps 1–5 prove all quantified assertions.

## Relationship to prior work

Asipchuk, De Carli and Rodriguez, *Block-equivalent finite Gabor frames* (arXiv:2605.16139v1, May 15, 2026), Corollary 1.2(b) and Section 5.2, establish Fourier diagonalization when all translations are included. Their general identity is explicitly used in Step 1 and is **not** claimed as new. It does not optimize two channel positions, power allocation or the two extreme frame bounds under strictly radial spectral profiles. The general 2026 characterization by de Dios Pont, Gröchenig, Liehr, Shafkulovska and Taylor concerns Gabor-frame existence for continuous totally positive functions on \(\mathbb R\), not this finite cyclic design problem. Published finite three-tap two-channel Gabor work gives a phase-frequency optimization for **frame potential**, not the worst-case spectral condition number for an arbitrary strictly radial Fourier-energy profile, nor the heat-kernel parity formula.

The distinctive contribution is the **strict simultaneous two-extreme ordering** for every strictly decreasing radial spectrum, together with the unique joint power/gap minimizer and explicit graph-heat specialization. Finite Gabor diagonalization alone gives none of these optimizers. A more general classical circular-polarization or rearrangement theorem might imply the two-arc interlacing lemma; no such implication was located in the inspected sources.

## Limitations

Only even cycle order, all cyclic translations, exactly two distinct modulation channels and strictly positive radially decreasing Fourier-energy profiles are covered. No assertion is made for odd order, more channels, arbitrary nonmonotone profiles, partially observed translation sets, noncyclic groups, phase retrieval or reconstruction from intensity-only measurements. For a general radial profile the antipodal frame can be tight exactly when \(a_j+a_{R-j}\) is independent of \(j\); the heat window is tight only at \(N=2\) for positive diffusion time. The formulas concern the **frame operator**, not an unnormalized analysis-matrix singular value. The scientific comparison is not an independent audit, and unindexed earlier circle-rearrangement results remain a residual originality risk.

## References

1. O. Asipchuk, L. De Carli, L. Rodriguez, *Block-equivalent finite Gabor frames*, arXiv:2605.16139v1 (May 15, 2026), updated v2 (October 24, 2026). https://arxiv.org/abs/2605.16139
2. J. de Dios Pont, K. Gröchenig, L. Liehr, I. Shafkulovska, M. A. Taylor, *Gabor Frames of Totally Positive Functions: A Complete Characterization*, arXiv:2608.04992v1 (August 5, 2026). https://arxiv.org/abs/2608.04992
3. *Exact phase–frequency design and tightness transition for three-tap cyclic Gabor frames*, published mathematical result, November 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-phase-frequency-design-and-tightness-transition-for-three--9d47ac973e0f
4. G. E. Pfander, *Finite Gabor Frames*, reference chapter (finite-dimensional time-frequency conventions and frame operators). https://www.mathematik.uni-marburg.de/~pfander/pubs/FiniteGaborFramesChapter.pdf
