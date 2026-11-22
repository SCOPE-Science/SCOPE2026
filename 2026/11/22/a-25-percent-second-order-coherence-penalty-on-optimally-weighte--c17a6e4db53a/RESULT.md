# A 25-percent second-order coherence penalty on optimally weighted double stars

## Finding

For each integer \(m\ge2\), form a *balanced double star* from two adjacent hubs, each joined to exactly \(m\) private leaves. Put arbitrary strictly positive conductances on the \(2m+1\) edges, subject only to their sum being one. Let \(L\) be the weighted graph Laplacian and \(L^+\) its Moore--Penrose pseudoinverse. Define
\[
F_1(L)=\operatorname{tr}(L^+),\qquad F_2(L)=\operatorname{tr}((L^+)^2).
\]
The second-order objective has a **unique global minimum across all independent edge allocations**. The minimizing weights on the \(2m\) spokes are all equal to \(a_2=(2m+r_2)^{-1}\), and the hub-to-hub bridge receives \(b_2=r_2/(2m+r_2)\), where \(r_2\) is the unique positive zero of
\[
2\left(2m-1+\frac1{(m+1)^2}\right)r^3+mr^2-2m^2r-m(m+1)^2=0.
\]
In contrast, the (previously accessible via the general tree formula for \(F_1\)) unique first-order minimizer has ratio
\[
r_1=\frac{b_1}{a_1}=\sqrt{\frac{m(m+1)}{2m-1+(m+1)^{-1}}}.
\]
The optimal bridge budget shares obey
\[
b_2\sim(32m)^{-1/3},\qquad b_1\sim(8m)^{-1/2}
\]
and the sharp asymptotic mismatch is
\[
\boxed{\lim_{m\to\infty}\frac{F_2(L_{\mathrm{first\text{-}order\ optimum}})}{\min F_2}=\frac54.}
\]
The first-order optimum is a comparison baseline, **not** claimed as a new result.

## Assumptions and scope

The graph has \(N=2m+2\) vertices, with two degree-\(m+1\) hubs joined by one bridge and \(m\) degree-one leaves at each hub. Every edge conductance is a free positive real variable; \(\sum_e w_e=1\). Requiring connectedness forces each weight to be positive because the graph is a tree. All zero-weight disconnected boundary points are excluded, and the objective diverges on approach to them. We use the combinatorial weighted Laplacian, not the normalized Laplacian. Both coherence functionals here omit the common noise/gain/vertex-count prefactors from the corresponding stochastic consensus model. Consequently their minimizers and the stated performance ratio are unaffected by those factors.

## Proof

**1. Symmetry is forced by global strict convexity.** Restrict \(L\) to \(\mathbf1^\perp\), producing a positive-definite affine matrix-valued function \(X(w)\). The map \(w\mapsto X(w)\) is injective: distinct weights give distinct off-diagonal Laplacian entries. On the positive-definite cone the spectral trace function \(\operatorname{tr}(X^{-2})\) is strictly convex. Indeed, in an eigenbasis of \(X\), its second directional derivative in a nonzero symmetric direction \(H\) is a sum of positive terms \(q_{ij}|H_{ij}|^2\), where \(q_{ij}=(f'(\lambda_i)-f'(\lambda_j))/(\lambda_i-\lambda_j)>0\) for distinct eigenvalues, \(q_{ii}=f''(\lambda_i)>0\), and \(f(t)=t^{-2}\). Thus \(F_2\) is strictly convex in the individual conductances. If any edge tends to zero, the graph disconnects in the limit, a positive Laplacian eigenvalue tends to zero, and \(F_2\to\infty\). The budget simplex therefore has exactly one interior minimizer. All graph automorphisms preserve objective and budget; uniqueness forces this minimizer to be constant on the full set of spokes and separately on the bridge. This proves global optimality of the forthcoming reduced solution without presupposing symmetric competitors.

**2. Exact spectral reduction.** Write every spoke weight as \(a>0\), bridge weight as \(b>0\), so \(2ma+b=1\). The leaf-difference modes have Laplacian eigenvalue \(a\) with multiplicity \(2m-2\). The hub-symmetric, leaf-uniform nonconstant mode has eigenvalue \((m+1)a\). The remaining two nonzero hub-antisymmetric eigenvalues \(\lambda_+,\lambda_-\) satisfy
\[
\lambda_++\lambda_-=(m+1)a+2b,\qquad \lambda_+\lambda_-=2ab.
\]
Along with a single zero eigenvalue, these account for all \(2m+2\) eigenvalues. Reciprocal-sum identities yield
\[
F_1=\frac{A_1}{a}+\frac{m+1}{2b},\quad A_1=2m-1+\frac1{m+1},
\]
\[
F_2=\frac{A_2}{a^2}+\frac{m}{ab}+\frac{(m+1)^2}{4b^2},\quad A_2=2m-1+\frac1{(m+1)^2}.
\]

**3. Exact constrained optimum.** Put \(r=b/a>0\). The budget yields \(a=(2m+r)^{-1}\), \(b=r/(2m+r)\), hence
\[
F_2(r)=(2m+r)^2\left(A_2+\frac mr+\frac{(m+1)^2}{4r^2}\right).
\]
Direct differentiation simplifies to
\[
F_2'(r)=\frac{2m+r}{r^3}\left[2A_2r^3+mr^2-2m^2r-m(m+1)^2\right].
\]
The bracketed polynomial has exactly one positive root by Descartes' rule of signs (coefficients \(+,+,-,-\)), since it is negative at zero and positive at infinity. Because \(F_2(r)\to\infty\) at both endpoints, the unique root gives the global reduced optimum, hence the unique unrestricted optimum by step 1. For the first-order objective,
\[
F_1(r)=(2m+r)\left(A_1+\frac{m+1}{2r}\right)
\]
so \(F_1'(r)=A_1-m(m+1)/r^2\), yielding the stated \(r_1\). This is also a special case of the published general optimal-weight law for trees.

**4. Asymptotic allocations and exact relative penalty.** Since \(A_2=2m+O(1)\), substitution \(r=m^{2/3}s\) into the optimality polynomial, divided by \(m^3\), gives the limiting equation \(4s^3-1=0\). The unique positive roots therefore obey \(r_2\sim4^{-1/3}m^{2/3}\). (Rigorous root convergence follows by evaluating the polynomial at \((4^{-1/3}\pm\varepsilon)m^{2/3}\) and using uniqueness, for any sufficiently small fixed \(\varepsilon>0\).) Also \(r_1\sim\sqrt{m/2}\). Transforming by \(b=r/(2m+r)\) gives the stated bridge shares. In the exact expression for \(F_2(r)\), substitution of \(r_2\) gives
\[
F_2(r_2)=8m^3+o(m^3).
\]
At the first-order ratio \(r_1\), the leading spoke term contributes \(8m^3\), the term proportional to \(m/r\) is lower order, and the bridge-square term contributes another \(2m^3\), hence
\[
F_2(r_1)=10m^3+o(m^3),\qquad F_2(r_1)/F_2(r_2)\longrightarrow 5/4.
\]
This proves the claimed asymptotic loss.

## Verification

The accompanying `verify_double_star.py` recomputes the full rational pseudoinverse from \((L+\mathbf1\mathbf1^{\mathsf T}/N)^{-1}-\mathbf1\mathbf1^{\mathsf T}/N\) and independently compares both trace identities on a family of rationally weighted graphs. It also numerically checks the cubic optimizer and asymptotic scales. It reports **60 assertions**; the universal theorem follows from the preceding proof, not from these finite tests. Run `python verify_double_star.py` with Python 3 and the standard library.

## Relationship to prior work

Patterson and Bamieh (2013), Section II, provide the spectral definitions of first- and second-order stochastic network coherence. Ghosh, Boyd, and Saberi (2008), Section 5.1, already solve the first-order total-effective-resistance budget problem on **all trees**, and therefore cover the first-order optimizer used here as a benchmark. Lin (2021), Theorem 5.1, treats the **unweighted** biharmonic index of double stars as the numbers of leaves on the two hubs vary. Neither result fixes the balanced double-star topology and optimizes \(F_2\) over all independently variable edge conductances, nor yields the cross-objective \(5/4\) limit. Summers and collaborators (2014) study first-order coherence by **adding edges** to a fixed graph, a distinct design variable. Searches of related indexed research revealed star second-order price effects and double-star spectral-gap optimization, which do not imply this second-order inverse-square-trace solution.

## Limitations

No assertion is made about unbalanced double stars, other graph families, costs other than a linear conductance budget, or nonlinear controller dynamics. The first-order baseline and generic strict-convexity techniques are established prior work. The novelty assessment is literature-based, not an exhaustive proof of publication priority; obscure or unindexed exact equivalents may exist. The asymptotic penalty is an all-size limiting statement, not a claim that the finite-size ratio equals \(5/4\). Independent external mathematical audit has not been performed.

## References

- S. Patterson and B. Bamieh, *Consensus and Coherence in Fractal Networks*, first posted 9 October 2013, https://arxiv.org/abs/1310.2592, especially Section II.
- A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37–66, https://stanford.edu/~boyd/papers/pdf/eff_res.pdf, especially Sections 2.7 and 5.1.
- Z. Lin, *The Biharmonic Index of Connected Graphs*, first posted 18 October 2021, https://arxiv.org/abs/2110.09931, especially Theorem 5.1.
- T. Summers, I. Shames, J. Lygeros, and F. Dörfler, *Topology Design for Optimal Network Coherence*, first posted 18 November 2014, https://arxiv.org/abs/1411.4884.
