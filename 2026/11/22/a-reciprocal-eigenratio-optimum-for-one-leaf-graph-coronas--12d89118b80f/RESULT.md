# A reciprocal eigenratio optimum for one-leaf graph coronas

## Finding

**Theorem.** Let \(H\) be a finite connected simple vertex- and edge-transitive graph with \(m\ge3\) vertices and degree \(d\ge2\). Write \(s=\lambda_2(L_H)>0\) and \(\ell=\lambda_m(L_H)\) for the extreme positive eigenvalues of its unit-conductance combinatorial Laplacian. Attach one private leaf to each vertex of \(H\). Each original edge costs \(P>0\) per unit conductance, and each pendant edge costs \(Q>0\). Every edge conductance may be chosen independently, nonnegatively, subject to *exactly* the total expenditure \(B>0\). The objective is the positive Laplacian eigenratio \(\mathcal R=\lambda_{2m}(L)/\lambda_2(L)\), interpreted as infinite for disconnected allocations.

The global optimum over **all** independent edge conductances is
\[
\boxed{\displaystyle
\mathcal R_*=\frac12\bigg(1+\sqrt{\frac\ell s}+\sqrt{1+\frac\ell s}\bigg)^2.}
\]
A global optimum has common original-edge conductance \(b_*\), common pendant conductance \(a_*\), where
\[
\boxed{\displaystyle
x_*:=\frac{b_*}{a_*}=\frac2{\sqrt{s\ell}},\qquad
a_* =\frac{B}{m[Q+(dP/2)x_*]},\qquad b_*=x_*a_*.}
\]
This is the **only** optimal allocation constant on each edge orbit. For the cyclic cores \(H=C_n\), \(n\ge3\), it is furthermore the **unique optimum even among all asymmetric allocations**. No uniqueness among non-orbit-constant allocations is claimed for arbitrary transitive cores.

For sunlets with \(n\) cycle vertices, \(s_n=4\sin^2(\pi/n)\), \(\ell_n=4\sin^2(\pi\lfloor n/2\rfloor/n)\). As \(n\to\infty\),
\[
\frac{b_*}{a_*}\sim\frac{n}{2\pi},\qquad
\mathcal R_* =\frac{2n^2}{\pi^2}+\frac{2n}{\pi}+O(1).
\]
For unit prices, the previously known allocation maximizing absolute spectral gap has a rim/pendant ratio asymptotic to \(n/\pi\), **twice** the new eigenratio-optimal ratio. In that same comparison the gap-optimal allocation incurs an eigenratio excess asymptotic to \(n/(2\pi)\), although its relative excess tends to zero.

## Assumptions and scope

The weighted Laplacian is \(L(w)=\sum_{\{i,j\}}w_{ij}(e_i-e_j)(e_i-e_j)^\mathsf T\). It has \(2m\) eigenvalues \(0=\lambda_1\le\lambda_2\le\cdots\le\lambda_{2m}\). The budget is an equality: \(P\sum_{e\in E(H)}w_e+Q\sum_{v\in V(H)}w_{v,v'}=B\), not an inequality (otherwise overall scaling destroys uniqueness). There are \(md/2\) original edges and \(m\) pendant edges. Positivity and connectivity are automatic at the displayed optimum. The optimization concerns the *ordinary* symmetric Laplacian and its ratio, not the largest-minus-smallest spectral width, discrete-time SLEM, or a normalized Laplacian.

## Proof

**1. Unrestricted-to-orbit reduction.** On the orthogonal complement of constants, \(\lambda_2(L(w))\) is concave in the edge weights; \(\lambda_{2m}(L(w))\) is convex. The automorphism group of \(H\), extended to the leaves, is transitive separately on original and pendant edges. Averaging a feasible connected allocation over this group preserves total expenditure, decreases (or preserves) \(\lambda_{2m}\), and increases (or preserves) \(\lambda_2\). Hence it does not increase \(\mathcal R\). Thus a globally optimal orbit-constant allocation exists. This argument does not assume that every optimum is symmetric.

**2. Exact spectrum.** Write \(a>0\) for a common pendant rate and \(b>0\) for a common original-edge rate, and put \(x=b/a\). In core/leaf order,
\[
L(a,b)=\begin{pmatrix}bL_H+aI&-aI\\-aI&aI\end{pmatrix}.
\]
For each base eigenvalue \(\eta\), the two corona eigenvalues are
\[
a f_\pm(x\eta),\qquad f_\pm(z)=\frac{z+2\pm\sqrt{z^2+4}}2.
\]
At \(\eta=0\) these are \(0,2a\). For \(z>0\), the lower branch satisfies \(0<f_-(z)<1\) and both branches increase strictly with \(z\). Thus \(\lambda_2=a f_-(sx)\) and \(\lambda_{2m}=a f_+(\ell x)\). Since \(f_-(z)f_+(z)=z\), writing \(F=f_+\) yields
\[
\mathcal R(x)=\frac{F(sx)F(\ell x)}{sx},\qquad F(z)=\frac{z+2+\sqrt{z^2+4}}2.
\]
The budget uniquely fixes the scale \(a=B/[m(Q+dPx/2)]\) for any chosen ratio \(x>0\).

**3. Strict one-variable optimality by reciprocal symmetry.** Define the logarithmic elasticity \(E(z)=zF'(z)/F(z)\). Explicitly,
\[
E(z)=\frac{z}{\sqrt{z^2+4}}\frac{z+\sqrt{z^2+4}}{z+\sqrt{z^2+4}+2}.
\]
It increases strictly from \(0\) to \(1\), since each displayed positive factor is strictly increasing. A direct radical identity gives \(F(4/z)=2F(z)/z\). Differentiate its logarithm to obtain \(E(z)+E(4/z)=1\). Consequently,
\[
\frac{d\log\mathcal R(x)}{d\log x}=E(sx)+E(\ell x)-1.
\]
The right-hand side is strictly increasing from \(-1\) to \(1\). It vanishes precisely when \((sx)(\ell x)=4\), i.e. at the unique minimizer \(x_*=2/\sqrt{s\ell}\). With \(r=\sqrt{s/\ell}\), substitution of \(sx_*=2r\) and \(\ell x_*=2/r\) into the spectral formula gives \(\mathcal R_*=(1+1/r+\sqrt{1+1/r^2})^2/2\). This is a global, not merely local, minimum for the unrestricted allocation by Step 1.

**4. No asymmetric minimizers on cycles.** For \(H=C_n\), fix an arbitrary global optimizer \(w\). Its rotational average is the unique orbit-constant minimizer from Step 3. By convexity/concavity and equality of the two eigenratios, *both* inequalities are equalities: \(\lambda_2(w)=\lambda_2(w_*)\) and \(\lambda_{2n}(w)=\lambda_{2n}(w_*)\). In particular the total original and pendant rates of \(w\) match the respective totals of \(w_*\).

Let \(\theta=2\pi/n\). The two real first-frequency eigenvectors of \(L(w_*)\) at \(\lambda_2(w_*)=t>0\) have core components \(U\cos(j\theta),U\sin(j\theta)\) and leaf components \(V\cos(j\theta),V\sin(j\theta)\), respectively, with \(U\ne0\), \(V-U\ne0\). For either edge orbit, the sum over these two vectors of squared coordinate differences across an edge is independent of that edge's cyclic index. Their total Rayleigh energy under the possibly asymmetric \(w\) therefore equals their total energy under \(w_*\), using the matching edge-class sums. Each Rayleigh quotient under \(w\) is at least \(t\); equality of their summed Rayleigh energies forces both vectors to be \(t\)-eigenvectors of \(L(w)\). At each leaf, their sine and cosine equations (which never vanish simultaneously) imply that its pendant rate is \(a_*\). The remaining core equations combined into a complex first Fourier mode then read
\[
(b_j-b_*)(1-e^{i\theta})+(b_{j-1}-b_*)(1-e^{-i\theta})=0.
\]
Its imaginary part is \(\sin\theta\,(b_{j-1}-b_j)=0\). Because \(n\ge3\), \(\sin\theta\ne0\), and hence all rim rates coincide; their fixed sum forces \(b_j=b_*\). This proves unrestricted uniqueness for every sunlet, including the three-cycle.

**5. Large-cycle law and the difference from spectral-gap design.** The base spectral edges satisfy \(s_n=4\pi^2n^{-2}+O(n^{-4})\) and \(\ell_n=4+O(n^{-2})\). Inserting these into Step 3 gives the two eigenratio asymptotics. The known unit-price spectral-gap allocation has original/pendant ratio \(x_{\mathrm{gap}}=(2+\sqrt{s_n})/[\sqrt{s_n}(1+\sqrt{s_n})]\), which equals \(2x_*(1+O(1/n))\). Taylor expansion in the exact expression \(F(s_nx)F(\ell_nx)/(s_nx)\) at the two distinct ratios yields \(\mathcal R(x_{\mathrm{gap}})-\mathcal R(x_*)=n/(2\pi)+O(1)\). This comparison is an implication of the prior gap allocation, not a novel derivation of that known allocation.

## Verification

The accompanying `verify.py` is standalone Python 3 standard-library code. It independently diagonalizes full finite weighted corona Laplacians with a Jacobi eigensolver for cycles, complete graphs, and hypercubes; checks the analytic two-orbit spectrum and budget; compares alternative symmetric ratios; and tests 60 separately perturbed *asymmetric* budget-feasible allocations per case. The executed output was `PASS 1522 exact-formula, Jacobi-spectrum and asymmetric-perturbation checks`. These finite tests are consistency checks. Strict global optimality and uniqueness for cycles follow from the analytic arguments above.

## Relationship to prior work

Kempton, Herrmann and di Bernardo (2015) study optimizing the Laplacian eigenratio using distributed eigenvalue estimators subject to degree constraints, a general framework, without a corona-specific reciprocal formula or unrestricted cyclic uniqueness theorem in the inspected full text. Earlier weighted-network synchronizability studies likewise optimize general graphs numerically. Corona-spectrum formulas are known, and are used here as a starting point rather than claimed as new. Du, Zhu, Gao and Li (2022) analyze weighted corona *coherence*, not eigenratio allocation. Previously published graph-corona designs give exact optimal **spectral gaps** and uniqueness for sunlets, but maximizing the gap is a different optimization from minimizing the ratio; their allocation differs asymptotically by a factor of two. Previously published sunlet first- and second-inverse-moment conductance optima optimize further distinct spectral objectives and do not imply the present ratio-optimal classification.

## Limitations

The base must be connected and both vertex- and edge-transitive; prices must be constant within original and pendant edge classes. Unrestricted uniqueness is established for cyclic cores only. A fixed expenditure **equality** is necessary for weight-level uniqueness; with an upper-budget inequality the scale is nonunique. The eigenratio is a spectral conditioning objective and a contraction proxy for appropriately tuned linear consensus, not a universal criterion for nonlinear synchronization. No complete classification of asymmetric optimizers for arbitrary transitive cores is provided. Publication priority remains uncertain for unindexed or inaccessible equivalent results. Independent external mathematical validation has not been performed.

## References

- L. Kempton, G. Herrmann, M. di Bernardo, *Self-organization of weighted networks for optimal synchronizability*, arXiv:1505.07279, first posted 2015-05-27. https://arxiv.org/abs/1505.07279
- M. Jalili, A. Ajdari Rad, M. Hasler, *Enhancing synchronizability of weighted dynamical networks using betweenness centrality*, arXiv:0812.4720, 2008. https://arxiv.org/abs/0812.4720
- D. Barik, S. Pati, B. K. Sarma, *The Spectrum of the Corona of Two Graphs*, SIAM Journal on Discrete Mathematics 21 (2007), 47–56. https://doi.org/10.1137/050624029
- W. Du, J. Zhu, H. Gao, X. Li, *Consensus analysis of the weighted corona networks*, Frontiers in Physics 10 (2022), 948247. https://doi.org/10.3389/fphy.2022.948247
- H. Liu, Y. Shao, *Two Kinds of Laplacian Spectra and Degree Kirchhoff Index of the Weighted Corona Networks*, Journal of Mathematics (2022), 6884839. https://doi.org/10.1155/2022/6884839
- Previously published *Exact price-optimal continuous-time mixing on transitive one-leaf coronas and rigid cyclic sunlets*. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-price-optimal-continuous-time-mixing-on-transitive-one-lea--eed5b428788a
- Previously published *Unique price-optimal fastest mixing on sunlet networks*. https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-unique-price-optimal-fastest-mixing-on-sunlet-networks--638ad6225b9e
- Z.-S. Duan and G.-R. Chen, *Does the eigenratio represent the synchronizability of a complex network?*, Chinese Physics B 21 (2012), 080506. https://doi.org/10.1088/1674-1056/21/8/080506
