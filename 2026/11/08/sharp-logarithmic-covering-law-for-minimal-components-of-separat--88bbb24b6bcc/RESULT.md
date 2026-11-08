# Sharp logarithmic covering law for minimal components of separated equal-slope interval maps

## Finding

Let \(f\) be a piecewise-affine contracting map of a compact nondegenerate interval, with \(r\ge2\) ordered continuity pieces, a common absolute slope \(0<\lambda<1\), and pairwise disjoint closed branch images. Assume the one-sided branch-limit images of every discontinuity have well-defined forward itineraries, as specified below. For every minimal basic component \(K\) of the attractor, define \(N_K(\varepsilon)\) to be the least number of closed real intervals of diameter at most \(\varepsilon\) covering \(K\).

For an itinerary \(\theta\) of any point in \(K\) with well-defined forward orbit, the established eventually affine symbolic-complexity law reads \(p_\theta(n)=\alpha_K n+\beta_K\) for all sufficiently large integers \(n\), with \(\alpha_K\in\{0,1,\dots,r-1\}\). Then **the exact logarithmic covering law** is

\[
\boxed{N_K(\varepsilon)=\frac{\alpha_K}{\log(1/\lambda)}\log(1/\varepsilon)+O_f(1)\quad(\varepsilon\downarrow0).}
\]

Consequently, the limit \(\lim_{\varepsilon\downarrow0}N_K(\varepsilon)/\log(1/\varepsilon)=\alpha_K/\log(1/\lambda)\) exists. It is strictly positive for every minimal Cantor component and zero for a periodic component. More precisely, if \(K\) is a periodic orbit of length \(q\), then \(N_K(\varepsilon)=q\) for every sufficiently small \(\varepsilon>0\). By the recurrence characterization in [2], \(\alpha_K\) is also the number of discontinuities visited recurrently from both sides by the corresponding orbit: the first nonzero metric covering coefficient directly recovers a discrete dynamical recurrence count.

## Assumptions and scope

Write \(X=[a,b]\) with \(a<b\) and \(X\setminus\Delta=\bigcup_{i=1}^{r}X_i\), where the \(X_i\) are ordered disjoint intervals, with \(\Delta\) the finite boundary set. On each \(X_i\), assume \(f_i(x)=s_i\lambda x+b_i\), where \(s_i\in\{-1,1\}\), \(0<\lambda<1\), and the branch maps have their indicated continuous extensions to \(\overline{X_i}\). Assume every closed branch image \(f_i(\overline{X_i})\subset X\) and

\[
 g:=\min_{i\ne j}\operatorname{dist}\bigl(f_i(\overline{X_i}),f_j(\overline{X_j})\bigr)>0.
\]

Let \(\widetilde X\) consist of points whose complete forward orbits avoid \(\Delta\), and require the set \(D\) of all one-sided branch-limit values at discontinuities to satisfy \(D\subset\widetilde X\). The attractor \(\Lambda\) and its minimal basic components are those defined through the nested images and spectral decomposition in [1,3]. Thus each basic component is either a finite periodic orbit or a compact minimal Cantor set; an orbit in \(K\cap\widetilde X\) is dense in \(K\).

For each word \(w=i_1\cdots i_n\), define the generation-\(n\) atom \(A_w\) as the nonempty nested composition \(F_{i_n}\circ\cdots\circ F_{i_1}(X)\), where \(F_i(A)=\overline{f_i(A\cap X_i)}\). Use only *active* atoms \(\mathcal A_n(K):=\{A_w:A_w\cap K\ne\varnothing\}\); atoms that miss \(K\) are not counted in this theorem. The existence of a minimal Cantor component is not asserted for every parameter choice.

## Proof

**1. A quantitative atom-separation lemma.** Every generation-\(n\) atom is a compact interval of diameter at most \(L\lambda^n\), where \(L=b-a\). In addition, for every integer \(n\ge1\), any two distinct generation-\(n\) atoms \(A\) and \(B\) satisfy

\[
\operatorname{dist}(A,B)\ge g\lambda^{n-1}.
\]

For \(n=1\), their distinct closed branch images have distance at least \(g\). Suppose the bound holds at level \(n\), and write level-\(n+1\) atoms as \(F_i(A)\) and \(F_j(B)\), where \(A,B\) are level-\(n\) atoms. If \(i\ne j\), these atoms lie in the distinct closed branch images and are at distance at least \(g\ge g\lambda^n\). If \(i=j\) and \(A\ne B\), intersecting with the same branch interval cannot decrease their distance, and the common affine branch multiplies all distances by exactly \(\lambda\). Consequently their images are at least \(\lambda\,g\lambda^{n-1}=g\lambda^n\) apart. If \(A=B\) and \(i=j\), the resulting atoms coincide rather than being distinct. This proves the lemma by induction, and also gives uniqueness of a word for each atom.

**2. Exact count of active atoms.** Choose \(x\in K\cap\widetilde X\) with itinerary \(\theta\). Every length-\(n\) factor of \(\theta\) codes a generation-\(n\) atom containing a subsequent orbit point of \(x\), and therefore intersecting \(K\). Conversely, if a level-\(n\) atom \(A\) intersects \(K\), choose \(y\in A\cap K\). The orbit of \(x\) visits every neighborhood of \(y\) at arbitrarily large times by minimality. For every \(t\ge n\), the point \(f^t(x)\) belongs to a level-\(n\) atom; the positive separation proved in step 1 forces any sufficiently close such point to belong to \(A\) itself. Its preceding \(n\) itinerary symbols therefore label \(A\). Hence

\[
\#\mathcal A_n(K)=p_\theta(n)\qquad(n\ge1).
\]

The established complexity theorem [2, Theorems 1.2 and 2.10], also recalled in [1, Theorem 3.1], gives \(p_\theta(n)=\alpha_Kn+\beta_K\) for all large \(n\), with \(0\le\alpha_K\le r-1\). The periodic/Cantor dichotomy for \(\alpha_K\) is established in [3] and [1, §3]; the formula \(\alpha_K=\#\Delta_{lr}(x)\) is [2, Theorem 2.10].

**3. Matching physical-scale packing and covering.** Since the active atoms cover \(K\), at scale \(\varepsilon\ge L\lambda^n\) one interval of diameter at most \(\varepsilon\) per active atom suffices:

\[
N_K(\varepsilon)\le p_\theta(n).
\]

At the opposite scale, if \(0<\varepsilon<g\lambda^{n-1}\), no interval of diameter at most \(\varepsilon\) can meet two different active atoms, and each active atom meets \(K\). Hence

\[
N_K(\varepsilon)\ge p_\theta(n).
\]

Put \(a_0=\log(1/\lambda)>0\). For sufficiently small \(\varepsilon\), the integers

\[
n_-(\varepsilon)=\left\lfloor\frac{\log(g/\varepsilon)}{a_0}\right\rfloor,
\qquad
n_+(\varepsilon)=\left\lceil\frac{\log(L/\varepsilon)}{a_0}\right\rceil
\]

are positive and exceed the eventual-affinity threshold. By construction, \(g\lambda^{n_--1}>\varepsilon\) and \(L\lambda^{n_+}\le\varepsilon\), so

\[
\alpha_K n_-+\beta_K\ \le\ N_K(\varepsilon)\ \le\ \alpha_K n_++\beta_K.
\]

Both \(n_\pm(\varepsilon)=a_0^{-1}\log(1/\varepsilon)+O_f(1)\). Their difference is uniformly bounded, proving the claimed \(O_f(1)\) asymptotic and its coefficient. For a finite periodic \(K\), separate its finitely many distinct points by any sufficiently small \(\varepsilon\), giving exactly \(q\) required covering intervals.

## Verification

The proof relies on an *infinite-level induction*, not an extrapolation from finite experiments. Every bound needed for the result is explicit: the branch-image gap \(g>0\), common slope \(\lambda\), interval length \(L\), exact atom count \(p_\theta(n)\), and integer squeeze levels \(n_\pm\). A standalone exact-rational illustration in `verify.py` independently enumerates generation-one through generation-sixteen atoms of a two-branch affine map and checks the quantitative separation and diameter inequalities at each finite level. It is illustrative only; the induction and the prior complexity theorem establish the infinite claim.

## Relationship to prior work

Calderón and Villar-Sepúlveda [1] proved that the attractor of a separated piecewise contraction has zero Hausdorff and box dimension and related its finite-level atom cover to affine itinerary complexity. Their proof supplies a covering upper estimate. Catsigeras, Guiraud and Meyroneinc [2] proved eventual affine complexity and interpreted its slope as the number of two-sided recurrent discontinuities. Calderón, Catsigeras and Guiraud [3] supplied the basic-component decomposition. None of these inspected results states the matching metric lower bound or the exact **logarithmic covering coefficient** for minimal components. The new step is the scale-uniform lower separation of affine atoms, which converts symbolic word complexity into a two-sided Euclidean packing/covering asymptotic. As a concrete familiar case, every irrational two-branch contracted-rotation Cantor component satisfying these hypotheses has \(\alpha_K=1\), hence coefficient \(1/\log(1/\lambda)\).

## Limitations

The equality of the absolute slopes is essential to the matching logarithmic coefficient as proved: if contraction ratios vary by branch, the lower and upper geometric scales need not coincide. Strong separation of closed branch images is essential to the positive uniform gap \(g\). The result is *componentwise*; it does not identify an exact coefficient for the full attractor when several components coexist, and it does not identify the parameter values generating Cantor components. The calculation of \(\alpha_K\) uses the known itinerary complexity theorem rather than an algorithm for an arbitrary real input. The novelty assessment remains qualified by possible equivalent formulations in unindexed literature.

## References

[1] A. E. Calderón and E. Villar-Sepúlveda, *Piecewise contracting maps on the interval: Hausdorff dimension, entropy and attractors*, arXiv:2309.09154v1 (first posted 2023-09-17), especially §§2–4, Theorems 3.1 and 4.5 and Lemma 4.1. https://arxiv.org/abs/2309.09154

[2] E. Catsigeras, P. Guiraud and A. Meyroneinc, *Complexity of injective piecewise contracting interval maps*, arXiv:1702.03599v1 (2017-02-13), especially Theorems 1.2 and 2.10 and Lemma 2.3. https://arxiv.org/abs/1702.03599

[3] A. Calderón, E. Catsigeras and P. Guiraud, *A spectral decomposition of the attractor of piecewise contracting maps of the interval*, arXiv:1903.08591 (first posted 2019-03-20), especially Theorem 1.3. https://arxiv.org/abs/1903.08591
