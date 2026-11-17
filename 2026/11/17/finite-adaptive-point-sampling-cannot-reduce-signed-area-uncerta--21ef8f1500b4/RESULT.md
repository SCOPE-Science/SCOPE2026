# Finite adaptive point sampling cannot reduce signed-area uncertainty under a total-variation budget

## Finding
Fix \(T,B>0\). Let \(\mathcal V_B\) be the planar absolutely continuous paths \(X:[0,T]\to\mathbb R^2\) with \(X(0)=0\) and total length \(\int_0^T\|\dot X(t)\|_2\,dt\le B\). For the canonical signed-area controlled differential equation
\[
 dZ^1=dX^1,\qquad dZ^2=dX^2,\qquad
 dZ^3=\tfrac12(Z^1\,dX^2-Z^2\,dX^1),\qquad Z(0)=0,
\]
let \(F(X)=Z^3(T)\). Every finite deterministic adaptive policy that observes both endpoints for free and requests at most \(N-1\) further exact planar point values leaves the same sharp worst-case output half-diameter:
\[
 \boxed{\mathfrak R_N(F;\mathcal V_B)=\frac{B^2}{2\pi}\quad\text{for every integer }N\ge1.}
\]
Thus no **finite** number of adaptively chosen point observations improves the minimax radius on a class with only a global total-variation budget. The answer is independent of \(N\) and \(T\). This is a statement about a particular area-sensitive controlled differential equation, not every controlled system.

## Assumptions and scope
All paths belong to \(W^{1,1}([0,T];\mathbb R^2)\) and have their continuous representatives. The variation is Euclidean arclength, not the sum of coordinatewise variations. Derivatives may be arbitrarily large on short intervals, provided their integrated norm is at most \(B\). A deterministic policy may query times in arbitrary order, may choose a next time from preceding time-value observations, may repeat values, and may terminate early; both \(X(0)\) and \(X(T)\) are known before internal queries. It makes at most \(N-1\) additional queries. No derivative, signature, path-length allocation, or continuous observation is supplied.

For a policy \(\pi\) and path \(X\), write \(\mathcal O_\pi(X)\) for the ordered transcript, including its deterministic termination. The compatible fiber is \(\mathcal F_\pi(X)=\{Y\in\mathcal V_B:\mathcal O_\pi(Y)=\mathcal O_\pi(X)\}\). We use
\[
 \mathfrak R_N(F;\mathcal V_B)
 =\inf_{\pi}\sup_{X\in\mathcal V_B}
 \frac12\operatorname{diam}\{F(Y):Y\in\mathcal F_\pi(X)\}.
\]
The convention agrees with the deterministic information radius of Gusev, Romanenkova, and Zaytsev [1]. The result is exact for each fixed finite \(N\), not an asymptotic approximation.

## Proof
**Step 1: exact area readout.** The first two controlled equations imply \(Z^1(t)=X^1(t)\) and \(Z^2(t)=X^2(t)\), so absolute continuity gives
\[
 F(X)=\frac12\int_0^T\left(X^1(t)\dot X^2(t)-X^2(t)\dot X^1(t)\right)dt.
\]
The integral is well defined: \(\|X(t)\|\le B\) and \(\dot X\in L^1\).

**Step 2: uniform sharp bound.** Every planar absolutely continuous curve starting at the origin with length at most \(B\) satisfies
\[
 |F(X)|\le\frac{B^2}{2\pi}. \tag{1}
\]
Here is a direct verification valid even for self-intersecting curves. Reflect the curve across any line through \(0\) and \(X(T)\) (choose any line through \(0\) if the endpoint is zero). Concatenate the original curve with the reflected curve traversed backwards. This is a closed rectifiable curve of length at most \(2B\), whose signed area is \(2F(X)\), because reflection reverses signed area and reversing traversal reverses it again. The signed planar isoperimetric inequality \(|A(\gamma)|\le \operatorname{length}(\gamma)^2/(4\pi)\) implies \(2|F(X)|\le (2B)^2/(4\pi)\), which is (1). For completeness, the signed inequality follows by arclength parameterizing a closed curve, subtracting the coordinate means, applying the periodic Wirtinger inequality to the position and then Cauchy--Schwarz to \(A(\gamma)=\tfrac12\int\gamma\wedge\gamma'\). It applies to non-simple rectifiable curves. Consequently all compatible output fibers lie in \([-B^2/(2\pi),B^2/(2\pi)]\), so their radius is at most \(B^2/(2\pi)\), whatever the policy.

**Step 3: adversarial open-gap construction.** Fix an arbitrary deterministic finite policy. Set \(R=B/\pi\) and \(q=(2R,0)\), and reveal endpoint data \(X(0)=0\), \(X(T)=q\). Maintain a gap \((a,b)\), initially \((0,T)\), with the invariant that all queried times \(t\le a\) have value \(0\), all queried times \(t\ge b\) have value \(q\), and no queried time lies inside \((a,b)\). For a query outside the gap answer the corresponding constant. For a query \(t\in(a,b)\), if \(t\le(a+b)/2\), answer \(0\) and set \(a=t\); otherwise answer \(q\) and set \(b=t\). (Repeated queries retain their assigned responses.) Each response preserves the invariant. After finitely many queries, \(a<b\), and the final transcript is compatible with the path constant at \(0\) up to \(a\), linear from \(0\) to \(q\) over \([a,b]\), and constant at \(q\) thereafter. This reference path has length \(2B/\pi<B\), showing that the adaptive answers describe a legitimate input. This strategy also works when query order is nonchronological and the policy's stopping decision is adaptive.

**Step 4: two indistinguishable extremizers.** With \(u=(t-a)/(b-a)\), keep the path constant outside \([a,b]\), but inside choose either
\[
 X_\sigma(t)=\left(R(1-\cos(\pi u)),\ \sigma R\sin(\pi u)\right),
 \qquad\sigma\in\{-1,+1\}.
\]
Both are absolutely continuous, join \(0\) to \(q\), and have total length exactly \(\pi R=B\), regardless of the positive gap width. They equal all previously reported point values, so determinism implies that both reproduce the complete query transcript, including termination. Direct integration gives
\[
 F(X_\sigma)=-\sigma\frac{\pi R^2}{2}=-\sigma\frac{B^2}{2\pi}.
\]
Hence that transcript's compatible fiber has diameter at least \(B^2/\pi\), or radius at least \(B^2/(2\pi)\). Since the policy was arbitrary, the minimax radius is at least that number. Together with Step 2, this proves the equality. \(\square\)

## Verification
All estimates and quantifiers are analytical. A symbolic differentiation-and-integration check independently confirms the semicircle identity: for \(X_+(u)=(R(1-\cos\pi u),R\sin\pi u)\), length is \(\pi R=B\), endpoint displacement is \(2R\), and signed area is \(-\pi R^2/2\). Neither the upper bound nor the adaptive indistinguishability uses finite numerical experimentation. Because \(N\) is finite, the final open gap is positive, although its width may depend on the policy. This proves exact optimality without uniform bounds on instantaneous speed.

## Relationship to prior work
Gusev, Romanenkova, and Zaytsev [1, Sections 3 and 5, Proposition 5.3, Appendices A and D] define this information-radius model, analyze the same canonical area CDE, and prove the sharp formula \(L^2T^2/(2\pi N)\) under the **pointwise speed** restriction \(\|\dot X\|_{L^\infty}\le L\). Their bounded-acceleration results use stronger regularity again. The present statement changes the actual admissible class to a **global length** restriction \(\|\dot X\|_{L^1}\le B\); these classes have different feasible path-speed concentrations, and the published bounded-speed result cannot imply the nondecaying finite-observation radius. The geometric semicircle bound and the area representation are already contained in [1]; the new point is the exact adaptive-information obstruction under the weaker global regularity and its sharp all-\(N\) consequence. General optimal-recovery/rough-path literature supplies context, and broader historical coverage is possible.

## Limitations
This theorem does not apply when a finite uniform speed or acceleration bound is imposed, when the sensor observes velocities or iterated integrals, or when it can make infinitely many queries. It concerns deterministic exact point-value policies only; randomized policies are not classified. It concerns the stated canonical area-sensitive CDE, not arbitrary learned vector fields or statistical input laws. The semicircle extremizers may have arbitrarily high but finite speed in a tiny gap. No claim of independence or certified historical priority is made.

## References
[1] R. Gusev, E. Romanenkova, A. Zaytsev, *The Information Limits of Neural Controlled Differential Equations Under Sparse Observations*, arXiv:2611.03887v1, first public 2026-11-02; https://arxiv.org/abs/2611.03887 (especially Proposition 5.3 and Appendices A, D).

[2] Classical planar isoperimetric inequality in signed-area form, with an elementary periodic-Wirtinger proof supplied above; the fixed-endpoint Dido bound also appears in [1, Lemmas A.2 and A.4].
