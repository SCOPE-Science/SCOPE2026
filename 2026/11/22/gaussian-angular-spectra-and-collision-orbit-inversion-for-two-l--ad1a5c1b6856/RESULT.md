# Gaussian angular spectra and collision-orbit inversion for two-lineup products of simplices

## Finding
Let \(p,q\ge 2\), and let \(L_{p,q}\) be the two-lineup polytope of the standard orthogonal product \(\Delta_{p-1}\times\Delta_{q-1}\), with any fixed weights \(1>w_1>w_2>0\) satisfying \(w_1+w_2=1\). Choose a Gaussian vector in the ambient Euclidean space, project to the affine tangent space if desired, and let \(V\) denote the almost-surely unique supporting vertex.

There are precisely \(p(p-1)q\) *row-change* vertices (the two ranked product vertices differ only in their first factor) and \(pq(q-1)\) *column-change* vertices. Let \(D_m\) denote the gap between the largest and second-largest of \(m\) independent standard normals, and let
\[
\alpha_{p,q}=\Pr(D_p<D_q).
\]
Every row-change vertex has Gaussian normal-cone probability \(\alpha_{p,q}/[p(p-1)q]\), and every column-change vertex has probability \((1-\alpha_{p,q})/[pq(q-1)]\). With \(\phi,\Phi\) the standard-normal density and distribution function, put
\[
 S_m(t)=m\int_{-\infty}^{\infty}\phi(x)\Phi(x-t)^{m-1}\,dx\qquad(t\ge0).
\]
Then the angle is exactly computable from the convergent integral
\[
 \alpha_{p,q}=\int_0^\infty[-S_p'(t)]S_q(t)\,dt,
\quad
 -S_p'(t)=p(p-1)\int_{-\infty}^\infty\phi(x)\phi(x-t)\Phi(x-t)^{p-2}\,dx.
\]
Two independent Gaussian directions expose the same vertex with exact probability
\[
\boxed{C_{p,q}=\frac{\alpha_{p,q}^2}{p(p-1)q}+\frac{(1-\alpha_{p,q})^2}{pq(q-1)}.}
\]
In particular, \(C_{p,p}=1/[2p^2(p-1)]\) exactly.

For fixed \(a,b>0\), let \(p_n=\lfloor n^a\rfloor\) and \(q_n=\lfloor n^b\rfloor\), with \(n\to\infty\). Then
\[
\boxed{\alpha_{p_n,q_n}\longrightarrow \frac{\sqrt a}{\sqrt a+\sqrt b}.}
\]
If \(a>b\), row-change vertices have limiting single-direction mass greater than one-half, yet **conditional on two directions exposing the same vertex, the exposed vertex is column-change with probability tending to one**. Quantitatively,
\[
\boxed{C_{p_n,q_n}\sim\frac{b}{(\sqrt a+\sqrt b)^2}\frac1{p_nq_n^2}\quad(a>b).}
\]
If \(a<b\), the reverse inversion holds: almost every collision is row-change, and
\[
\boxed{C_{p_n,q_n}\sim\frac{a}{(\sqrt a+\sqrt b)^2}\frac1{p_n^2q_n}\quad(a<b).}
\]

The limit extends coherently to every fixed lineup length. Write \(X_{[1]}>X_{[2]}>\cdots\) and \(Y_{[1]}>Y_{[2]}>\cdots\) for the decreasing Gaussian order statistics, \(b_m=\Phi^{-1}(1-1/m)\) for \(m>2\), and \(u_n=\sqrt{2\log n}\). For every fixed \(r\ge1\), the first \(r\) entries in decreasing order of the grid \(\{X_i+Y_j\}\), after subtracting \(b_{p_n}+b_{q_n}\) and multiplying by \(u_n\), jointly converge with their *row-column ranks* to the first \(r\) entries of
\[
\boxed{\left\{\frac{Z_i}{\sqrt a}+\frac{W_j}{\sqrt b}:i,j\ge1\right\},}
\]
where \(Z_1>Z_2>\cdots\) and \(W_1>W_2>\cdots\) are atoms of two independent Poisson point processes with intensity \(e^{-x}\,dx\). The first \(r\) grid ranks always belong to \([r]\times[r]\), so this is a finite-dimensional limit for every fixed \(r\). In particular, the top-to-second grid-score gap multiplied by \(u_n\) converges to an exponential random variable of rate \(\sqrt a+\sqrt b\).

## Assumptions and scope
The input point configuration is \(\{\mathbf e_i\oplus\mathbf f_j:1\le i\le p,1\le j\le q\}\subset\mathbb R^{p+q}\), with the standard orthonormal direct-sum metric. All random objectives have independent standard-normal coordinates; equivalently, directions are uniform on the intrinsic sphere, since orthogonal projection and radial scaling do not change maximizers. The weights are positive, strictly decreasing and normalized to sum one. The normal-cone and collision results are finite-dimensional exact statements for every \(p,q\ge2\); the limiting claims require the specified polynomial dimension growth with both exponents positive. The point-process assertion concerns ranks of *all* entries of the additive outer-sum grid and not independent Gaussian entries in an ordinary random matrix.

## Proof
**1. Lineup classification.** A generic objective has scores \(X_i+Y_j\). Let \(i_1,i_2\) denote its top and second row indices, and \(j_1,j_2\) the analogous column indices. The largest grid entry is \((i_1,j_1)\). Every other entry \((i,j)\) is no larger than either \((i_2,j_1)\) or \((i_1,j_2)\): when both indices differ it is smaller than both, and when exactly one differs it is bounded by the relevant one. Thus the runner-up is \((i_2,j_1)\) exactly when \(X_{[1]}-X_{[2]}<Y_{[1]}-Y_{[2]}\), and otherwise it is \((i_1,j_2)\). Every ordered candidate of either type is exposed by a strict objective (take chosen top/second scores and send other scores sufficiently low). Strictly ordered lineup weights ensure each is a distinct supporting vertex, by the lineup-vertex characterization in the reference. This yields the two orbit cardinalities.

**2. Exact cone angles.** Exchangeability of Gaussian rows and columns makes their rank permutations uniform and independent of the ordered values; hence the gap event is independent of all four top-index labels. Division of its probability by the corresponding orbit cardinality gives the asserted vertex probabilities. Since a Gaussian sample has a unique largest coordinate almost surely,
\[
 S_m(t)=m\int \phi(x)\Phi(x-t)^{m-1}\,dx
\]
by conditioning on which sample is the top coordinate and its value. Differentiation under the integral gives the displayed positive gap density. Independently sampled row and column gaps then give the integral for \(\alpha_{p,q}\). Squaring and summing the individual vertex probabilities gives \(C_{p,q}\). For \(p=q\), exchangeability and continuity give \(\alpha_{p,p}=1/2\), hence the balanced exact formula.

**3. Gaussian extreme spacings.** For \(m\to\infty\), the Gaussian Mills-ratio estimates give
\[
 m[1-\Phi(b_m+x/b_m)]\longrightarrow e^{-x}\qquad(x\in\mathbb R).
\]
The exceedance counts at finitely many thresholds are multinomial with rare cell probabilities, hence converge jointly to the increments of a Poisson process of intensity \(e^{-x}\,dx\). Consequently the upper ordered normalized sample values \(b_m(X_{[j]}-b_m)\), for every fixed number of indices \(j\), converge jointly to the descending points \(Z_j\) of that process. Independence gives a second such process \(W\) for columns. In particular the first spacing in this Poisson process is exponential of rate one: under the monotone map \(u=e^{-x}\), the two smallest points are the first two arrivals of a unit-rate Poisson process, and the ratio of the first two arrival times is uniform on \((0,1)\); therefore their logarithmic gap is \(\operatorname{Exp}(1)\).

Because \(b_{p_n}/u_n\to\sqrt a\) and \(b_{q_n}/u_n\to\sqrt b\), we have independent limits \(u_nD_{p_n}\Rightarrow\operatorname{Exp}(\sqrt a)\) and \(u_nD_{q_n}\Rightarrow\operatorname{Exp}(\sqrt b)\). Continuity of comparison yields the limiting orbit probability. The minimum of these two independent exponential variables has rate \(\sqrt a+\sqrt b\), which is also the limiting first grid-score gap.

**4. Rare-collision orbit inversion.** Writing the two exact collision contributions as \(C_R=\alpha^2/[p(p-1)q]\) and \(C_C=(1-\alpha)^2/[pq(q-1)]\), their ratio is
\[
\frac{C_R}{C_C}=\frac{\alpha^2}{(1-\alpha)^2}\frac{q-1}{p-1}.
\]
When \(a>b\), this ratio tends to zero, even though \(\alpha\to\sqrt a/(\sqrt a+\sqrt b)>1/2\). Thus \(C\sim C_C\) and the claimed conditional concentration and constant follow. The case \(a<b\) is symmetric. There is no inversion assertion for \(a=b\).

**5. Entire finite top-lineup field.** For any two strictly descending coordinate lists, a pair with row rank greater than \(r\) is exceeded by at least \(r\) entries in its own column; an analogous statement holds for a column rank greater than \(r\). Thus every one of the first \(r\) grid entries lies in the finite \(r\times r\) upper-left rank grid. Joint order-statistic convergence in Step 3 and \(u_n/b_{p_n}\to1/\sqrt a\), \(u_n/b_{q_n}\to1/\sqrt b\) give entrywise convergence of this grid to the stated Poisson outer-sum grid. Every finite set of distinct grid entries has unequal limiting values almost surely, by absolute continuity and independence of the two Poisson input processes, so sorting and retaining ranks are continuous almost surely. The continuous-mapping theorem yields the joint ranked-value/rank-location result. No truncation beyond \(r\) is needed because of the deterministic grid-rank lemma.

## Verification
The included `VERIFY.py` checks, for all \(2\le p,q\le5\), each ordered row- and column-change lineup by an explicit strict score witness, the two vertex counts, and the upper-left \(r\times r\) order-statistic truncation identity on deterministic and seeded random rank lists. It computes the finite exact angular integrals by independent one- and two-dimensional Gaussian quadrature and checks \(\alpha_{2,2}=1/2\), \(\alpha_{2,3}+\alpha_{3,2}=1\), the exact balanced collision identity, and a seeded Monte-Carlo comparison of the \((2,3)\) row-change probability against quadrature. These are finite corroborations only; the all-dimension and limiting proofs are Steps 1--5 above. Reproduce with `python VERIFY.py` using Python 3, NumPy and SciPy.

## Relationship to prior work
Castillo and Labbé (arXiv:2306.00082, §1.2 and §2.2.1) define lineup polytopes and their normal fans and give the additive-grid and realizability framework; their work does not evaluate Gaussian normal-cone masses or collision laws. A related exact minimum-sphere result for precisely these two-lineup polytopes gives their vertex orbits, center, radius and contacts, but those Euclidean distance data do not determine the Gaussian normal-cone masses. Standard extreme-value Poisson convergence supplies an analytic ingredient, not an existing angular-spectrum or rare-collision-inversion statement. More general realizable outer-sum tableaux work concerns allowable order types, not probability measures on their cones.

## Limitations
The exact cone formula is specific to the two-lineup polytope and the orthogonal simplex-product metric; arbitrary affine distortions alter Gaussian solid angles. The universal Poisson-grid limit treats fixed lineup length, not a length growing with dimension. No independent verification or exhaustive priority guarantee is asserted. An unindexed equivalent geometric probability theorem, or a general result for additive Gaussian arrays covering the same rank and collision assertions, remains a residual originality risk.

## References
1. Federico Castillo and Jean-Philippe Labbé, *Lineup polytopes of product of simplices*, arXiv:2306.00082, first public version 2023-05-31, https://arxiv.org/abs/2306.00082 (especially §1.2, Proposition 1.3, and §2.2.1); primary MSC 52B12.
2. Federico Castillo, Jean-Philippe Labbé, Julia Liebert, Arnau Padrol, Eva Philippe and Christian Schilling, *An effective solution to convex one-body N-representability*, arXiv:2105.06459, https://arxiv.org/abs/2105.06459.
3. *Two-lineup products of two simplices have an exact all-vertex minimum sphere*, published mathematical record (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-two-lineup-products-of-two-simplices-have-an-exact-all-vertex-mi--8c763d514594 (vertex-orbit and enclosing-sphere results only).
4. C. L. Mallows and R. J. Vanderbei, *Which Young tableaux can represent an outer sum?*, 2015 (realizable outer-sum rankings and combinatorics).
5. Classical Gaussian maximum-domain-of-attraction/Poisson-exceedance theorem; the needed tail and multinomial-to-Poisson argument is reconstructed in Proof Step 3.
