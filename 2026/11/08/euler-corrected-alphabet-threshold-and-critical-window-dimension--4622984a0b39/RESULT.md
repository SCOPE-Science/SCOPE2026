# Euler-corrected alphabet threshold and critical-window dimension in Zipf expanding maps

## Finding
Fix a retained-length fraction \(0<\lambda<1\). Set \(q=1+\varepsilon\), where \(\varepsilon>0\), and define the inverse-branch similarity ratios
\[
 r_n=\frac{\lambda n^{-q}}{\zeta(q)},\qquad n\ge1.
\]
Let \(s_N\) be the Hausdorff dimension of the survivor of the corresponding expanding interval map using only the first \(N\ge2\) branches. Put \(a=(\lambda/\zeta(q))^{1/q}\), and let \(\gamma\) denote Euler's constant.

**Sharp threshold and its polynomial prefactor.** The smallest integer \(N_*(\varepsilon)\ge2\) for which \(s_N>1/q\) is characterized exactly by
\[
 N_* =\min\{N\ge2:aH_N>1\},\qquad H_N=\sum_{n=1}^N\frac1n.
\]
It satisfies
\[
 \boxed{\frac{N_*(\varepsilon)}{\exp(1/(\lambda\varepsilon))(\lambda\varepsilon)^{1/\lambda}}
 \longrightarrow \exp\!\left(\gamma\left(\frac1\lambda-1\right)\right).}
\]

**Universal critical window.** For fixed real \(t\), let
\[
 N_{\varepsilon,t}=\left\lfloor\exp\!\left(a^{-1}-\gamma+t\right)\right\rfloor.
\]
Then
\[
 \boxed{\lim_{\varepsilon\downarrow0}
 \frac{q s_{N_{\varepsilon,t}}-1}{a^2}=2t.}
\]
The convergence is uniform for \(t\) in compact intervals. In particular, for each fixed nonzero \(t\), the sign of \(s_{N_{\varepsilon,t}}-1/q\) eventually agrees with the sign of \(t\).

**Resolution at the unshifted exponential cutoff.** For
\[
 M_{\varepsilon}=\left\lfloor\exp\!\left(\frac1{\lambda\varepsilon}\right)\right\rfloor,
\]
we have the strict positive-side asymptotic
\[
 \boxed{s_{M_{\varepsilon}}-\frac1q
 \sim 2\lambda\varepsilon^2\log(1/\varepsilon)>0.}
\]
This resolves the sign and its magnitude at the exact first-order phase boundary of the previously studied exponential-alphabet crossover; the result is a *second-scale* statement, not a repetition of the known first-order crossover.

## Assumptions and scope
The explicit map uses \(p_n=n^{-q}/\zeta(q)\), \(P_n=\sum_{k\le n}p_k\), and separated intervals \(I_n=[P_n-\lambda p_n,P_n]\subset[0,1]\). On \(I_n\) define \(T(x)=(x-(P_n-\lambda p_n))/(\lambda p_n)\). The survivor with alphabet \(\{1,\dots,N\}\) consists of points admitting an infinite forward \(T\)-itinerary using only these intervals. All dimensions refer to the Euclidean metric and unchanged, not renormalized, branch lengths. The constants \(\lambda\) and \(t\) are fixed as \(\varepsilon\to0^+\). The profile at \(t=0\) specifies a vanishing scaled difference but does not claim a finite-\(\varepsilon\) sign.

## Proof
**1. Exact dimensional equation and sign criterion.** The intervals are disjoint with positive gaps and the inverse branches are similarities with ratios \(r_n\). The finite open-set-condition similarity dimension theorem gives the unique \(s_N\in(0,1)\) satisfying
\[
 F_N(s_N):=\left(\frac{\lambda}{\zeta(q)}\right)^{s_N}\sum_{n=1}^N n^{-qs_N}=1.
\]
Since \(F_N\) is strictly decreasing, evaluating it at \(s=1/q\) yields
\[
 F_N(1/q)=aH_N,\qquad
 \operatorname{sgn}(s_N-1/q)=\operatorname{sgn}(aH_N-1).
\]
Thus the threshold integer is exactly as claimed. This pressure identity is classical and is not itself asserted as new.

**2. Location of the integer threshold.** The Euler–Maclaurin harmonic expansion gives \(H_N=\log N+\gamma+O(1/N)\). At the first strict crossing, \(aH_{N_*-1}\le1<aH_{N_*}\). Since the increment \(H_{N_*}-H_{N_*-1}=1/N_*\), this implies
\[
 \log N_*=a^{-1}-\gamma+o(1).
\]
Next \(\zeta(1+\varepsilon)=\varepsilon^{-1}+\gamma+O(\varepsilon)\), so
\[
 a=\lambda\varepsilon\left[1-\varepsilon(\log(\lambda\varepsilon)+\gamma)
 +O(\varepsilon^2\log^2\varepsilon)\right]
\]
and therefore
\[
 a^{-1}=\frac1{\lambda\varepsilon}
 +\frac{\log(\lambda\varepsilon)+\gamma}{\lambda}
 +O(\varepsilon\log^2\varepsilon).
\]
Exponentiating the resulting expression for \(\log N_*\) proves the first boxed limit. In particular the multiplicative polynomial factor is essential; omitting it changes the location by an unbounded factor.

**3. Critical-window expansion.** Use the normal coordinate \(e=qs-1\). The pressure equation becomes \(P_N(e)=1\), where
\[
 P_N(e)=a^{1+e}\sum_{n=1}^N n^{-1-e}.
\]
For \(N=N_{\varepsilon,t}\), uniformly for bounded \(t\),
\[
 H_N=a^{-1}+t+o(1),\qquad
 \log P_N(0)=a t+o(a).
\]
Write \(B_N=\sum_{n\le N}(\log n)/n\). Integral comparison implies \(B_N=\tfrac12(\log N)^2+O(1)\); consequently
\[
 \left.\frac{d}{de}\log P_N(e)\right|_{e=0}
 =\log a-\frac{B_N}{H_N}
 =-\frac1{2a}+O(|\log a|+1)
\]
uniformly on the window. The second derivative of \(\log P_N(e)\) is a weighted variance of \(\log n\), bounded by \(O(a^{-2})\) for \(|e|\le C a^2\) with fixed \(C\). The pressure is strictly decreasing as a function of \(e\), and the expansion
\[
 \log P_N(e)=a t-\frac{e}{2a}+o(a)
\]
holds uniformly for \(e=O(a^2)\) and bounded \(t\). Bracket its unique root between \(e=a^2(2t-\eta)\) and \(e=a^2(2t+\eta)\) for any fixed \(\eta>0\); this proves \(e/a^2\to2t\), uniformly for bounded \(t\).

**4. Magnitude at the unshifted cutoff.** For \(N=M_{\varepsilon}\), its centered window coordinate satisfies
\[
 t_{\varepsilon}=\log M_{\varepsilon}-(a^{-1}-\gamma)
 =\frac{\log(1/\varepsilon)}\lambda+O(1).
\]
In this moderate-deviation window \(t_{\varepsilon}=O(\log(1/a))\), the same harmonic and derivative estimates give
\[
 \log P_N(0)=a t_{\varepsilon}(1+o(1)),\quad
 (\log P_N)'(0)=-\frac1{2a}(1+o(1)).
\]
The variance remainder remains negligible at \(e=O(a^2t_{\varepsilon})\), since \(a t_{\varepsilon}\to0\). Hence \(qs_{M_{\varepsilon}}-1\sim2a^2t_{\varepsilon}\), which, using \(a\sim\lambda\varepsilon\) and \(q\to1\), gives the third boxed result.

## Verification
The standalone `verify_cutoff.py` evaluates the exact pressure using Hurwitz-zeta subtraction at enormous finite integer cutoffs, checks both sides of the critical sign criterion, and reproduces finite-parameter approximations to the critical-window coefficient. It uses `mpmath` at 95 decimal digits and reports `VERIFY_OK finite_pressure_roots=18 threshold_signs=12 high_precision=95`. This finite computation neither proves the \(\varepsilon\to0\) limits nor certifies originality. The analytic derivations above cover the stated parameter quantifiers.

## Relationship to prior work
Cunha, Novaes and Ponce (2026) give general conformal-IFS and invariant-set results for infinitely many expanding branches; the affine family is within that setting. A published result *Exponential-alphabet crossover for Zipf-normalized expanding maps* (2026) already gives this very same affine model's first-order crossover with \(N=\lfloor\exp(\tau/\varepsilon)\rfloor\), and places its boundary at \(\tau=1/\lambda\). It explicitly leaves the signed boundary behavior unresolved. Here the claim is deliberately limited to the previously unquantified **Euler-corrected threshold, second-scale critical window and strict log-enhanced boundary displacement**, not the known first-order crossover or general pressure formula. The classical finite similarity-dimension identity and harmonic-number expansions are used as known tools, not claimed as independent discoveries. The cited older dimension-spectrum literature addresses different questions about subsystem dimensions and does not visibly supply this exact cutoff expansion.

## Limitations
The coefficient and polynomial prefactor rely on the exact Zipf normalization and affine branch slopes. Perturbations of branch ratios can modify the constants. At the precisely centered \(t=0\) window no definite finite-parameter sign is asserted. The model does not address nonlinear distortions, box dimension, mixing rates or truncated-alphabet measures. Full historical priority cannot be guaranteed by the searches performed, and independent mathematical validation has not occurred.

## References
1. M. G. C. Cunha, D. D. Novaes and G. Ponce, *Infinite-Piecewise Expanding Maps: Chaos, Ergodicity and Invariant-Set Complexity*, arXiv:2608.00398v1, first public 2026-08-01. https://arxiv.org/abs/2608.00398
2. *Exponential-alphabet crossover for Zipf-normalized expanding maps*, published research record 2026-10-11, full mathematical statement and proof at https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-exponential-alphabet-crossover-for-zipf-normalized-expanding-map--9738a052e9b1/RESULT.md
3. R. D. Mauldin and M. Urbański, *Dimensions and Measures in Infinite Iterated Function Systems*, Proc. Lond. Math. Soc. 73 (1996), 105–154; DOI:10.1112/plms/s3-73.1.105.
4. T. Das and D. Simmons, *On the dimension spectra of infinite iterated function systems*, J. Fractal Geom. 9 (2022), 73–87; arXiv:1910.10259.
