# Matching erasures in simplex-edge spherical codes: an exact dimension-seven robustness transition

## Finding
For each integer \(n\ge5\), let \(M\) be a **nonempty matching** on \(\{1,\ldots,n\}\), of any cardinality \(1\le |M|\le\lfloor n/2\rfloor\). Define the centered edge-midpoint spherical code
\[
\mathcal C_{n,M}=\left\{u_{ij}:=\frac{e_i+e_j-(2/n){\bf1}}{\sqrt{2(n-2)/n}}:\ 1\le i<j\le n,\ \{i,j\}\notin M\right\}\subset S^{n-2},
\]
with sphere understood in the zero-sum hyperplane of \(\mathbb R^n\). Define its optimal spherical covering cosine by
\[
\rho_{n,M}=\min_{\substack{\|v\|_2=1\\\sum_i v_i=0}}\ \max_{u\in\mathcal C_{n,M}}\langle v,u\rangle.
\]
The covering radius is \(\Theta_{n,M}=\arccos\rho_{n,M}\). The following exact, *matching-size-independent* law holds:
\[
\boxed{\rho_{n,M}=\min\left\{\sqrt{\frac{2}{(n-1)(n-2)}},\frac{n-4}{2(n-2)}\right\}=\begin{cases}\frac{n-4}{2(n-2)},&n=5,6,\\\sqrt{\frac{2}{(n-1)(n-2)}},&n\ge7.\end{cases}}
\]
All unit vectors attaining the minimum (the deepest spherical holes) are **exactly**:
- for \(n=5,6\), the deleted code directions \(\{u_{ab}:\{a,b\}\in M\}\);
- for \(n\ge7\), the \(n\) directions \(-\bigl(e_i-(1/n){\bf1}\bigr)/\sqrt{(n-1)/n}\), one for every coordinate \(i\).

Thus removing an **arbitrary matching**, even of maximum size, leaves the worst-case spherical covering radius **unchanged** in every dimension \(n-1\ge6\), whereas every nonempty matching erasure worsens the radius for \(n=5,6\). The original unerased Johnson code has covering cosine \(\sqrt{2/((n-1)(n-2))}\) for all \(n\ge5\).

## Assumptions and scope
The Euclidean metric on \(S^{n-2}\) is the round metric's angular cosine convention; antipodal distance uses \(\arccos\). The matching is a family of pairwise-disjoint unordered pairs. No claim is made for adjacent deleted edges or for a general deletion graph. Every statement is exact for all integers \(n\ge5\) and for every such matching; its directions are expressed in the canonical regular-simplex realization.

## Proof
**1. Identifying the convex hull.** Put \(c=(2/n){\bf1}\), \(R=\sqrt{2(n-2)/n}\), and \(P_M=\operatorname{conv}\{e_i+e_j:\{i,j\}\notin M\}\). Partition the ground set into the paired blocks \(\{a,b\}\in M\) and its remaining singleton blocks. Each block is a parallel class of a connected rank-two partition matroid; there are \(n-|M|\ge3\) blocks. In the affine hyperplane \(H=\{z:\sum z_i=2\}\),
\[
P_M=\bigl\{z\in H:z_i\ge0\ (1\le i\le n),\ \sum_{i\in C}z_i\le1\ \text{for every block }C\bigr\}.
\]
For proof of the reverse inclusion, let \(q_C=\sum_{i\in C}z_i\); then \(q_C\in[0,1]\) and \(\sum_Cq_C=2\). The vector \((q_C)\) is a convex combination of vectors selecting two distinct blocks, since these are the vertices of \(\{q\in[0,1]^s:\sum q=2\}\). Conditional on each selected block, choose one coordinate with probabilities \(z_i/q_C\) (when \(q_C>0\)). The expected pair indicator is \(z\), completing the equality. The description also proves full affine dimension \(n-1\), since at \(c\) all constraints are strict for \(n\ge5\).

**2. Centered inball and spherical covering.** The normalized convex hull of code vectors is \(K_M=(P_M-c)/R\subset H_0\), where \(H_0=\{x:\sum x_i=0\}\). Its support function satisfies
\[
\min_{\|v\|=1,\ v\in H_0}h_{K_M}(v)=\max\{r\ge0:B_{H_0}(0,r)\subseteq K_M\}=\rho_{n,M}.
\]
The first equality follows since the ball has support \(r\) in every unit direction. Every defining inequality of \(P_M\) has a directly computable centered Euclidean clearance. A lower-coordinate inequality \(z_i\ge0\) has normalized clearance
\[
\alpha_n=\frac{(2/n)}{R\sqrt{(n-1)/n}}=\sqrt{\frac{2}{(n-1)(n-2)}}.
\]
A singleton-block upper inequality \(z_i\le1\) has clearance
\[
\beta_n=\frac{1-2/n}{R\sqrt{(n-1)/n}}=\sqrt{\frac{n-2}{2(n-1)}}.
\]
For each two-element matched block \(C=\{a,b\}\), the projected outward normal \(e_a+e_b-(2/n){\bf1}\) has norm \(R\), while its slack at \(c\) is \(1-4/n\). Its normalized clearance is
\[
\gamma_n=\frac{1-4/n}{R^2}=\frac{n-4}{2(n-2)}.
\]
Because \(\beta_n\ge\alpha_n\) whenever \(n\ge4\), the smallest clearance of all the defining halfspaces is \(\min\{\alpha_n,\gamma_n\}\). Their intersection is exactly \(K_M\); hence this is exactly the centered inradius and the covering cosine.

**3. Dimension threshold.** The term \(\alpha_n\) strictly decreases with \(n\), whereas \(\gamma_n\) strictly increases. At \(n=6\) they are \(1/\sqrt{10}\) and \(1/4\), respectively, with \(\gamma_6<\alpha_6\); at \(n=7\) they are \(1/\sqrt{15}\) and \(3/10\), with \(\alpha_7<\gamma_7\). This gives precisely the two regimes, including \(n=5\).

**4. Exhaustiveness of deepest directions.** If a centered maximal inscribed Euclidean ball touches a boundary point of a polytope, its contact with every active defining inequality is tangential: by the Cauchy--Schwarz equality condition, the radial contact direction must equal the corresponding unit outward halfspace normal. Therefore every support-minimizing direction arises among the halfspace normals attaining the least clearance. In dimensions \(n=5,6\), only the matched-block constraints attain it; their unit outward normals are exactly \(u_{ab}\). For \(n\ge7\), only the lower coordinate constraints attain it; their outward directions are the displayed negative centered coordinate vectors. These directions do attain the minimum: the matched-block constraints have available pair vectors in the supporting face (choose one of the two matched coordinates and one outside); the lower coordinate constraints have allowed pairs avoiding that index (there are at least three blocks among the remaining indices). Thus the deep-hole lists are complete.

**5. Comparison with the unerased code.** For \(M=\varnothing\) the same hull method has only \(z_i\ge0\) and \(z_i\le1\) bounds, whose minimum clearance is \(\alpha_n\). Hence \(\gamma_n<\alpha_n\) for \(n=5,6\) gives strict degradation, and \(\gamma_n>\alpha_n\) for every \(n\ge7\) gives complete worst-case-radius immunity.

## Verification
The accompanying standalone `verify.py` enumerates **all matching cardinalities** for \(5\le n\le11\), evaluates every predicted deep-hole direction against all surviving code points, verifies the predicted strict inequality for all other candidate facet normals, and samples 200 independent random directions for every parameter pair with a fixed random seed. The computations support the formulas but do not prove the universal statements: the symbolic halfspace proof above does.

## Relationship to prior work
Yi's 2026 isosceles-set result identifies the full centered edge-midpoint (Johnson) configuration as a distinguished extremal two-distance configuration, but does not analyze its spherical covering radius after matching erasures. A published exact harmonic-interpolation theorem studies the **same unerased** point orbit, but its Gegenbauer-eigenspace ranks do not imply this sharp metric erasure threshold. An exact inradius theorem for all connected rank-two matroid base polytopes computes the **optimally centered** Chebyshev inradius; it does not give the inradius about the fixed uniform centroid that is required for a spherical code, nor identify deepest covering-hole directions. The current formula is derived from the explicit fixed-center facet clearances and is valid for every matching size simultaneously. The classical rank-two matroid inequality description is prior mathematics and is not claimed as a new contribution.

## Limitations
The sharp law applies only to deleted edges forming a matching; deletion of adjacent edges may introduce larger parallel blocks or a nonmatroid edge set and can change the obstruction types. The limit is a spherical **covering radius** rather than a sphere-packing radius or an optimally recentered polytope inradius. The enumerator is finite corroboration, not an exhaustive certificate beyond its tested range. Despite full-text and targeted searches, unseen historical formulations of robust Johnson-code covering remain a priority risk; independent review has not been performed.

## References
1. H. Yi, *Isosceles sets and two-distance sets in Euclidean space*, arXiv:2611.05421, first public version 2026-11-02; v2 2026-11-05. https://arxiv.org/abs/2611.05421 (primary MSC 52C10).
2. *Exact-degree spherical-harmonic sampling of simplex-edge midpoints*, 2026-11-02, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-exact-degree-spherical-harmonic-sampling-of-simplex-edge-midpoin--a9addfb59135/RESULT.md .
3. *Exact Euclidean inradius of connected rank-two matroid base polytopes*, 2026-10-11, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-exact-euclidean-inradius-of-connected-rank-two-matroid-base-poly--04d0301093d4/RESULT.md .
