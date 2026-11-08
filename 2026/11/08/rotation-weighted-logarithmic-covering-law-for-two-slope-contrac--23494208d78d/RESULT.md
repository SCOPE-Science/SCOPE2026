# Rotation-weighted logarithmic covering law for two-slope contracting circle maps

## Finding
For the two-branch affine interval map defined below, suppose its rotation number \(\rho\) is irrational and its attracting invariant set \(K\) is the associated minimal Cantor set. The minimal number \(N_K(\varepsilon)\) of closed Euclidean intervals of diameter at most \(\varepsilon\) needed to cover \(K\) obeys
\[
N_K(\varepsilon)=\frac{\log(1/\varepsilon)}{\chi}+O_f(1),\qquad
\chi=-(1-\rho)\log\lambda-\rho\log(\lambda\mu)>0.
\]
In particular, the logarithmic covering coefficient is the reciprocal of the *frequency-weighted geometric contraction exponent*, not the reciprocal of the larger one-step contraction rate. For \(\mu=1\), it reduces to \(1/|\log\lambda|\); for unequal slopes it varies with the irrational rotation number even when both slopes are held fixed.

## Assumptions and scope
Choose \(0<\lambda<1\), \(\mu>0\) with \(0<\lambda\mu<1\), and \(\delta\in(1-\lambda,1)\). Put \(\eta=(1-\delta)/\lambda\in(0,1)\) and suppose
\[
0<\lambda\mu(1-\eta)<\delta.
\]
Define the two-interval orientation-preserving map of \([0,1)\) by
\[
f(x)=\begin{cases}\lambda x+\delta,&0\le x<\eta,\\
\lambda\mu(x-\eta),&\eta\le x<1.\end{cases}
\]
The closures of the two branch images are disjoint, separated by the strictly positive gap \(g=\delta-\lambda\mu(1-\eta)\). The map induces a nondecreasing degree-one lift \(F\) through \(F(x)=f(x)+\mathbf1_{\{x\ge\eta\}}\) on \([0,1)\), extended by \(F(x+1)=F(x)+1\). Require an irrational rotation number \(\rho\in(0,1)\) and let \(K\) be its compact minimal Cantor omega-limit set. We use the standard two-interval Sturmian coding of its irrational-rotation semiconjugacy; equivalently, one may explicitly assume the branch language on \(K\) contains precisely \(n+1\) words of length \(n\), each with either \(\lfloor n\rho\rfloor\) or \(\lceil n\rho\rceil\) occurrences of branch 1, for every \(n\ge1\). The cited two-interval irrational-rotation construction supplies these conditions. The theorem makes no assertion for rational rotation numbers, overlapping branch images, or expanding branches.

An \(n\)-atom is the nonempty compact interval \(A_{w_1\cdots w_n}=F_{w_n}\circ\cdots\circ F_{w_1}([0,1])\), where set-valued branch operators mean \(F_i(E)=\overline{f(E\cap I_i)}\) with \(I_0=(0,\eta)\) and \(I_1=(\eta,1)\). Endpoint conventions do not change the compact closure. Only occupied atoms, namely those meeting \(K\), are counted.

## Proof
**1. Symbol counts and their contraction products.** The irrational-rotation coding is Sturmian, so its factor complexity is exactly \(p(n)=n+1\); in every admitted word \(w\) of length \(n\), the number \(k(w)\) of symbols 1 satisfies \(|k(w)-n\rho|<1\). This can also be read directly from the mechanical word \(\lfloor(j+1)\rho+t\rfloor-\lfloor j\rho+t\rfloor\). Since branch similarities have ratios \(\lambda\) and \(\lambda\mu\), their contraction product along \(w\) is
\[
L(w)=\lambda^n\mu^{k(w)}
=e^{-\chi n}\mu^{k(w)-n\rho}.
\]
With \(B=\exp(|\log\mu|)\), it follows for every factor word, independently of its position, that
\[
B^{-1}e^{-\chi n}\le L(w)\le Be^{-\chi n}.
\]
Note that \(\chi>0\) because it is the positive convex combination of \(-\log\lambda\) and \(-\log(\lambda\mu)\).

**2. Upper bounds for occupied atoms.** An atom of generation \(n\) whose code is \(w\) has diameter at most \(L(w)\) (the ambient interval has diameter one). Indeed, each branch restriction can only decrease the diameter of the input set before an affine similarity scales it. Thus each occupied generation-\(n\) atom has diameter at most \(Be^{-\chi n}\). The source's atom--itinerary correspondence for separated piecewise contracting interval maps, or directly the unique symbolic coding of the minimal Cantor orbit, gives precisely \(n+1\) occupied atoms. They cover \(K\). If \(\varepsilon\ge Be^{-\chi n}\), then \(N_K(\varepsilon)\le n+1\).

**3. Uniform lower separation for unequal slopes.** All distinct first-generation atoms lie inside different closed branch images, so their distance is at least \(g\). Let \(A_w,A_v\) be distinct occupied generation-\(n\) atoms. Read their words backward and let \(u\) be their maximal common final suffix, of length \(r\le n-1\). At the immediately preceding different symbols, their intermediate images are subsets of disjoint first-generation branch images, hence separated by at least \(g\). Applying the \(r\) final common affine branch operators contracts this distance by the common similarity product; intersection with branch domains cannot decrease the distance. Since \(u\) is an admitted Sturmian word, its product satisfies \(L(u)\ge B^{-1}e^{-\chi r}\). Consequently
\[
\operatorname{dist}(A_w,A_v)\ge gL(u)
\ge gB^{-1}e^{-\chi(n-1)}.
\]
Every occupied atom contains a point of \(K\), and an interval of diameter smaller than this bound can meet at most one occupied atom. Hence if \(\varepsilon<gB^{-1}e^{-\chi(n-1)}\), then \(N_K(\varepsilon)\ge n+1\).

**4. Two-sided logarithmic asymptotics.** In the upper bound choose \(n_+(\varepsilon)=\lceil \log(B/\varepsilon)/\chi\rceil\). For the lower bound choose \(n_-(\varepsilon)=\lfloor\log(gB^{-1}/\varepsilon)/\chi\rfloor\), reducing this integer by one only at a possible equality to ensure strictness. Then both integers equal \(\chi^{-1}\log(1/\varepsilon)+O_f(1)\). The preceding bounds therefore sandwich \(N_K(\varepsilon)\) between the same leading term with bounded additive errors, proving the displayed formula.

## Verification
The identity \(L(w)=e^{-\chi n}\mu^{k(w)-n\rho}\), strict positivity of \(\chi\), unique-word count and the two-sided atom estimates are proved analytically above. The included standalone \(verify.py\) checks two distinct contraction-ratio regimes and two irrational mechanical codings through finite word lengths, including the exact \(n+1\) factor count and the uniform product bounds. It additionally checks positivity of the disjoint-image gap for specific canonical map parameters generated by the published Hecke--Mahler formula. Those finite checks corroborate, but do not replace, the proof for all \(n\).

## Relationship to prior work
Calderón and Villar-Sepúlveda (2023) prove zero Hausdorff dimension and zero topological entropy for separated piecewise contracting interval attractors, and record the exact correspondence between occupied atoms and itinerary complexity. Laurent and Nogueira (2021) and Gaivão--Laurent--Nogueira (preprint 2022; journal 2024) establish explicit irrational-rotation semiconjugacies for two-branch maps with unequal affine slopes; those results are used for the Sturmian language and existence of this dynamical regime. None of those inspected statements evaluates the Euclidean small-scale covering number at its logarithmic order. Earlier equal-slope logarithmic covering identities are special cases: they lack the nonconstant frequency-weighted exponent. The new step is a **uniform metric separation bound using the entire balanced word, despite variable branch contraction rates**.

## Limitations
The theorem is conditional on strict branch-image separation and the irrational Sturmian minimal dynamics. It does not establish an optimal additive constant or the asymptotic for maps with overlapping images, irrational coding of higher complexity, or an expanding branch. The \(O_f(1)\) term depends on the particular map, including its branch gap; it is not uniform in parameters approaching contact of branch images. Published priority has been checked against the named primary sources and targeted mathematical searches, not every unindexed article. No independent mathematical audit has been performed.

## References
1. A. E. Calderón and E. Villar-Sepúlveda, *Piecewise contracting maps on the interval: Hausdorff dimension, entropy and attractors* (first public preprint 17 September 2023), arXiv:2309.09154; https://arxiv.org/abs/2309.09154. Primary MSC2020 37E05.
2. M. Laurent and A. Nogueira, *Dynamics of 2-interval piecewise affine maps and Hecke-Mahler series*, Journal of Modern Dynamics **17** (2021), 33–63; https://doi.org/10.3934/jmd.2021002.
3. J. P. Gaivão, M. Laurent and A. Nogueira, *Rotation number of 2-interval piecewise affine maps*, first public preprint 21 December 2022, arXiv:2212.10944; Aequationes mathematicae (2024 online), https://doi.org/10.1007/s00010-024-01064-2.
4. P. Guiraud, E. Catsigeras and A. Meyroneinc, *Complexity of injective piecewise contracting interval maps*, Ergodic Theory and Dynamical Systems **40** (2020), 64–88; https://doi.org/10.1017/etds.2018.34.
