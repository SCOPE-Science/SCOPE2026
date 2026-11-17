# Exact power-law residence spectrum at the parabolic tropical-mutation boundary

## Finding

Let \(p,q>0\) satisfy \(pq=4\). For the tropical rank-two mutation
\[
M_{p,q}(s,t)=\bigl(-s+q[t+p[s]_+]_+,\ -t-p[s]_+\bigr),\qquad [a]_+=\max\{a,0\},
\]
fix any \(R>0\) and define the parabolic switching wedge
\[
W_{p,R}=\left\{(s,t):0<\frac{ps}{2}<R,\quad -ps<t<-\frac{ps}{2}\right\}.
\]
For any real \(\beta>-1\), sample the initial point from \(W_{p,R}\) with a density proportional to \(d^\beta\) with respect to two-dimensional Euclidean area, where \(u=ps/2\) and \(d=-u-t>0\) is the transverse distance coordinate from the fixed ray. Define its **first exit** \(J=\min\{j\ge1:M_{p,q}^j(s,t)\notin W_{p,R}^{\infty}\}\), where
\[
W_{p,R}^{\infty}=\left\{(s,t):s>0,\quad -ps<t<-\frac{ps}{2}\right\}.
\]
The residence event concerns the *unbounded* angular wedge \(W_{p,R}^{\infty}\); \(R\) bounds only the initial sampling window. For every integer \(n\ge0\), the survival law is exactly
\[
\boxed{\Pr_\beta(J>n)=(2n+1)^{-(\beta+1)}.}
\]
Consequently, for every integer \(j\ge1\),
\[
\boxed{\Pr_\beta(J=j)=(2j-1)^{-(\beta+1)}-(2j+1)^{-(\beta+1)}.}
\]
The first exit is finite for every initial point in the wedge, yet the moments have a **sharp phase transition**: for any fixed \(\alpha>0\), \(\mathbb E_\beta[J^\alpha]<\infty\) exactly when \(\alpha<\beta+1\). In particular the mean is infinite for \(-1<\beta\le0\), while for \(\beta>0\) it is precisely
\[
\boxed{\mathbb E_\beta J=\bigl(1-2^{-(\beta+1)}\bigr)\zeta(\beta+1).}
\]
At uniform sampling \(\beta=0\), the exact inverse-linear law and its critical logarithmic growth are
\[
\boxed{\Pr_0(J>n)=\frac1{2n+1},\qquad \mathbb E_0\min(J,N)=H_{2N}-\tfrac12H_N=\tfrac12\log N+\log 2+\tfrac12\gamma+o(1),}
\]
where \(N\ge1\), \(H_N=\sum_{j=1}^N1/j\) and \(\gamma\) is Euler's constant.

There is also an **exact conditional shape law at every horizon**. Put \(U=ps/2\), \(d=-U-t\), and \(Z_n=(2n+1)d/U\). Conditional on \(J>n\), \(U\) and \(Z_n\) are independent: \(U\) has density \( (\beta+2)u^{\beta+1}/R^{\beta+2}\) on \((0,R)\), while \(Z_n\) has the beta density \((\beta+1)z^\beta\) on \((0,1)\). The residence law and the conditional distribution of \(U/R\) are independent of the individual parameters \(p,q\) and of the sampling scale \(R\), subject to \(pq=4\).

## Assumptions and scope

The map is the *tropical piecewise-linear* map, not the corresponding positive rational mutation. The parameters are arbitrary positive real numbers with product exactly four. The sampling density is the normalized power \(C_\beta d^\beta\) with respect to Euclidean planar area, where \(C_\beta=(p/2)(\beta+1)(\beta+2)/R^{\beta+2}\) in the original \((s,t)\) coordinates; at \(\beta=0\) this is ordinary uniform Euclidean area. The power law is the natural family describing depletion or enrichment of initial states near the stationary parabolic ray, with its integrability condition \(\beta>-1\). Only initially sampled points in the specified bounded triangular wedge are considered. The residence time ends on first exit from the **unbounded** parabolic wedge, not from the bounded initial triangle and not from the entire phase plane. Switching-line equality is treated as exit; these lines have zero sampling measure, but the strict inequalities determine individual-point boundaries. No claim is made about the global itinerary after exit.

The lines \(t=-ps\) (switching line) and \(t=-ps/2\) (stationary ray at the critical parameter) give the two intrinsic boundaries of the wedge; it is not an arbitrarily selected angular slice. The cutoff \(R\) merely defines a finite-area population of initial conditions.

## Proof

**1. Normalize the critical family.** Set \(u=ps/2\), \(v=t\). Because \(pq=4\), the original mutation is linearly conjugate to
\[
F(u,v)=\bigl(-u+2[v+2[u]_+]_+,\ -v-2[u]_+\bigr).
\]
The original area element is \(ds\,dt=(2/p)\,du\,dv\), a constant factor that cancels from normalized probabilities. The unbounded residence wedge becomes
\[
E=\{(u,v):u>0,\ -2u<v<-u\}.
\]
Set \(w=u+v\) and \(d=-w\). Then \((u,v)\in E\) precisely when \(u>0\) and \(0<d<u\). Both max-functions have known signs there: \([u]_+=u\) and \([v+2u]_+=v+2u\). Hence a step that starts in \(E\) is exactly
\[
(u,v)\longmapsto(u+2w,v-2w),\qquad w\longmapsto w.
\]
The boundary ray \(w=0,u>0\) consists of fixed points, while \(w<0\) points move transversely toward the switching boundary.

**2. Determine every finite-horizon survivor.** Fix any initial \((u,v)\) with \(0<u<R\), \(0<d<u\). As long as the orbit stays in \(E\), its coordinates after \(k\) steps are
\[
u_k=u-2kd,\qquad v_k=v+2kd,\qquad u_k+v_k=-d.
\]
At that step the exact wedge condition is \(u_k>d\), i.e. \(u>(2k+1)d\). The right side increases with \(k\), so *all* visits numbered \(0,1,\ldots,n\) stay in \(E\) if and only if
\[
0<u<R,\qquad 0<d<\frac{u}{2n+1}.
\]
In particular the pointwise first-exit time is the smallest integer \(j\ge1\) with \(u\le(2j+1)d\); it is finite because \(d>0\). The shear formula was used only before exit, so the argument does not assume any behavior after the branch changes.

**3. Evaluate the whole power-density family.** The linear change \((u,v)\mapsto(u,d)=\bigl(u,-u-v\bigr)\) has Jacobian magnitude one. For \(\beta>-1\), the normalization integral in these coordinates is
\[
Z_{\beta,R}=\int_0^R\int_0^u d^\beta\,dd\,du=\frac{R^{\beta+2}}{(\beta+1)(\beta+2)}.
\]
The survivor polygon after \(n\) steps is the exact triangle \(0<u<R\), \(0<d<u/(2n+1)\). Integrating the same weight over it gives \(Z_{\beta,R}/(2n+1)^{\beta+1}\), proving the exact survival law. Successive differences yield the exit-time mass function. As the survival mass tends to zero, finite exit occurs almost surely, as well as pointwise. For \(\alpha>0\), the difference of powers has the asymptotic order \(\Pr_\beta(J=j)\sim 2(\beta+1)(2j)^{-(\beta+2)}\), and hence \(\mathbb E_\beta[J^\alpha]\) is finite if and only if \(\alpha<\beta+1\). Summing the survival tails gives, for \(\beta>0\), the convergent odd-integer zeta sum
\[
\mathbb E_\beta J=\sum_{n=0}^\infty (2n+1)^{-(\beta+1)}=\bigl(1-2^{-(\beta+1)}\bigr)\zeta(\beta+1).
\]
For the critical uniform case \(\beta=0\), \(\mathbb E_0[J\wedge N]=\sum_{n=0}^{N-1}(2n+1)^{-1}=H_{2N}-H_N/2\), giving the claimed logarithmic growth.

**4. Exact conditional profile.** Conditional on survival through \(n\), define \(z=(2n+1)d/u\in(0,1)\). The Jacobian magnitude of \((u,z)\mapsto(u,d)\) is \(u/(2n+1)\). Dividing the joint weighted density by the survivor probability produces
\[
\frac{(\beta+1)(\beta+2)}{R^{\beta+2}}\,u^{\beta+1}z^\beta\mathbf1_{0<u<R}\mathbf1_{0<z<1}.
\]
This factors into the asserted \(u\)- and \(z\)-densities, proving independence at every integer horizon. Neither a limiting argument nor an approximation is used.

## Verification

The standard-library script `check.py` reconstructs the normalized map for multiple rational critical parameter pairs, checks the exact affine branch and pointwise first-exit formula using rational arithmetic, verifies finite-horizon area and probability identities, and checks the exact truncated-mean harmonic sum for integer horizons. It prints `PARABOLIC_TROPICAL_RESIDENCE_EXACT_OK` when all assertions pass. These finite checks support reproducibility but do not replace the infinite analytic proof above.

## Relationship to prior work

Machacek and Ovenhouse [1] define the tropical map, establish its symplecticity and piecewise quadratic first integral, and analyze motion at and above the critical product \(pq=4\). In particular, their Section 3.5 explicitly derives the critical branch's linear motion; neither that motion nor the critical threshold is claimed as new. Gekhtman and Nakanishi [2] give exact Chebyshev-polynomial expressions controlling rank-two mutation sign patterns, which can likewise encode *individual* crossing times. The new statement takes a natural full-area ensemble in the parabolic trapping wedge and computes the exact all-horizon power-density residence spectrum, the sharp mean-finiteness transition and the horizon-conditioned spatial laws. A published result for the same map at \(0<pq<4\) [3] gives elliptic-oval rotation numbers, and does not include the degenerate critical wedge. Related results for parabolic branches of a different piecewise toral map [4] exhibit inverse-linear residence tails but have different branch geometry and do not imply this formula for tropical mutation.

## Limitations

The theorem is an exact first-exit result for the angular wedge on one side of the stationary ray. It does **not** classify later itineraries, global basins, or all initial distributions. The power-law transverse density is essential to the exact full-time formula; a generic initial density can have a different coefficient or tail exponent. Only the critical product \(pq=4\) is included. Known pointwise linearity means the main originality is the measure-theoretic residence and conditioned-distribution calculation; related asymptotics for generic parabolic shears and any unindexed equivalent derivation remain publication-priority risks. No independent mathematical validation has been performed.

## References

[1] J. Machacek and N. Ovenhouse, *Discrete Dynamical Systems From Real Valued Mutation*, first posted 2021-09-14, arXiv:2109.06927, https://arxiv.org/abs/2109.06927 ; *Experimental Mathematics* 33 (2024), 261–275. Relevant sections: 1 and 3.1–3.5.

[2] M. Gekhtman and T. Nakanishi, *Asymptotic sign coherence conjecture*, first posted 2019-04-01, arXiv:1904.00971, https://arxiv.org/abs/1904.00971 ; *Experimental Mathematics* 31 (2022), 497–505. Relevant section: 3.

[3] *Exact rotation number and full orbit classification for tropical rank-two mutations*, published-finding corpus, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-rotation-number-and-full-orbit-classification-for-tropical--7d107b663bc7 .

[4] *Exact parabolic-branch survival laws for the orthogonal tents toral map*, published-finding corpus, 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-parabolic-branch-survival-laws-for-the-orthogonal-tents-to--fa18f62401f4 .
