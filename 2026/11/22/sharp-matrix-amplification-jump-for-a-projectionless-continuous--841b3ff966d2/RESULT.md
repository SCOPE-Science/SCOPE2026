# Sharp matrix-amplification jump for a projectionless continuous-trace algebra

## Finding
Let \(S^5=\{x\in\mathbb C^3: \|x\|=1\}\) and let \(E\to S^5\) be the Hermitian rank-two bundle \(E_x=\{v\in\mathbb C^3:\langle v,x\rangle=0\}\). Put \(\mathcal A=\Gamma(S^5,\operatorname{End}E)\), with pointwise composition and the supremum operator norm. For any unital complex Banach algebra \(\mathcal B\), define its spectral depth by
\[
d_\sigma(\mathcal B)=\sup_{b\in\mathcal B}\#\pi_0(\sigma_\mathcal B(b)),
\]
where \(\#\pi_0\) is the number of connected components, interpreted as a cardinal if necessary.

**Theorem.** The exact matrix-amplification law is
\[
d_\sigma(\mathcal A)=1,\qquad d_\sigma(M_m(\mathcal A))=2m\quad(m\in\mathbb Z,\ m\ge2).
\]
In fact, \(M_m(\mathcal A)\cong C(S^5,M_{2m}(\mathbb C))\) as unital \(C^*\)-algebras for all \(m\ge2\). Hence a continuous-trace algebra with connected spectrum for every element becomes spectrally maximally split in every nontrivial matrix amplification, even though matrix amplification preserves strong Morita equivalence. The sphere dimension five is the first dimension permitting this construction using an indecomposable but stably trivial complex rank-two bundle.

## Assumptions and scope
The base is the **complex** unit sphere \(S^5\), not the quaternionic sphere, and all bundles are continuous complex vector bundles. Here \(M_m(\mathcal A)\) means full \(m\)-by-\(m\) matrices over the same unital algebra, and the spectrum is computed in the indicated **section algebra**, not merely in a fixed fiber. The finite-dimensional fiber is always \(M_2(\mathbb C)\); the section algebra itself is infinite-dimensional and not a trivial matrix-function algebra.

We use standard clutching classification of complex vector bundles over spheres and the classical homotopy facts \(\pi_4(U(2))\cong\mathbb Z/2\) and \(\pi_4(U(k))=0\) for \(k\ge3\). These facts are independently documented in the cited topology notes. The bundle \(E\) is the nonzero clutching class, as witnessed by the non-splitting of \(SU(2)\to SU(3)\to S^5\); its orthogonal complement identity also gives \(E\oplus\varepsilon^1\cong\varepsilon^3\).

## Proof
**1. Nontriviality and stabilization of the bundle.** The line subbundle \(L_x=\mathbb Cx\subset S^5\times\mathbb C^3\) has the explicit global unit section \(x\mapsto x\). Therefore \(L\cong\varepsilon^1\) and its orthogonal complement satisfies \(E\oplus\varepsilon^1\cong\varepsilon^3\). The associated principal \(U(2)\)-frame bundle is the homogeneous fibration \(U(2)\to U(3)\to S^5\). Its clutching class is the nonzero class of \(\pi_4(U(2))\cong\mathbb Z/2\): otherwise the fibration would admit a section, contradicting the classical nontriviality of \(SU(2)\to SU(3)\to S^5\). Thus \(E\not\cong\varepsilon^2\).

For each integer \(m\ge2\), the bundle \(E^{\oplus m}\) has complex rank \(2m\ge4\) and is classified over \(S^5\) by \(\pi_4(U(2m))=0\). It is therefore trivial. In particular the first amplification already trivializes all matrix coefficients.

**2. The original algebra has no nontrivial idempotents.** Suppose \(p\in\mathcal A\) satisfies \(p^2=p\). Each \(p(x)\) is an idempotent on a two-dimensional complex vector space. Its rank, equal to its trace, is an integer-valued continuous function on connected \(S^5\), hence constantly \(0\), \(1\), or \(2\). In ranks \(0\) and \(2\) the idempotent is respectively \(0\) or \(I\). In rank \(1\), the image and kernel are complex line subbundles giving a splitting \(E\cong L_1\oplus L_2\). Since \(H^2(S^5;\mathbb Z)=0\), every complex line bundle over \(S^5\) is trivial. The splitting would force \(E\cong\varepsilon^2\), a contradiction. So \(p\) is only \(0\) or \(I\).

If some \(a\in\mathcal A\) had disconnected spectrum, the holomorphic Riesz functional calculus on a nonempty proper clopen spectral subset would yield an idempotent distinct from \(0,I\). Therefore every spectrum is connected. Nonemptiness of spectra in unital Banach algebras yields \(d_\sigma(\mathcal A)=1\).

**3. Amplification and exact depth.** Fiberwise identification gives \(M_m(\operatorname{End}E)\cong\operatorname{End}(E^{\oplus m})\). Taking continuous sections, and using the trivialization from step 1, yields a *-isomorphism \(M_m(\mathcal A)\cong C(S^5,M_{2m}(\mathbb C))\) for every \(m\ge2\).

Set \(r=2m\). The constant matrix-valued function \(x\mapsto\operatorname{diag}(1,2,\ldots,r)\) has spectrum \(\{1,2,\ldots,r\}\), providing \(d_\sigma\ge r\). Conversely, suppose an arbitrary section \(T\) has at least \(r+1\) spectral components. The Riesz calculus supplies \(r+1\) pairwise orthogonal nonzero idempotent sections whose sum is the identity. Each nonzero section idempotent has positive **constant** fiber rank, because its pointwise rank is continuous and the base is connected. Their ranks sum to \(r\), which cannot accommodate \(r+1\) positive integers. Thus \(d_\sigma\le r\), proving equality.

**4. Sharp sphere-dimension threshold.** Complex rank-two bundles on \(S^d\) are classified by \(\pi_{d-1}(U(2))\). For \(1\le d\le4\), this group is either zero or is carried injectively into stable unitary homotopy: the groups are respectively \(0,\mathbb Z,0,\mathbb Z\), and stabilization is injective. Consequently no nontrivial rank-two bundle over such a sphere is stably trivial. The above nontrivial stably trivial \(E\to S^5\) realizes the first possible sphere dimension. This minimality refers to this bundle-based construction, not to all possible spaces or Banach algebras.

## Verification
All arguments are exact. Checkpoints: the explicit orthogonal splitting \(\mathbb C^3=L_x\oplus E_x\); the nonzero \(\mathbb Z/2\) clutching class and its trivialization under rank \(\ge3\) stabilization; constancy of idempotent ranks; vanishing of \(H^2(S^5;\mathbb Z)\); spectral Riesz projections; and the \(2m\)-rank counting contradiction. No numerical approximation, finite exhaustion or computational certificate is used to establish the theorem. The two essential topological homotopy groups are independently established in the referenced lecture solutions, rather than inferred from numerical examples.

## Relationship to prior work
Bračič and Kandić (2026) introduce the finite spectral-depth hierarchy and prove the general equivalence between disconnected spectra and nontrivial idempotents, and between several spectral components and orthogonal idempotents. The connected-spectrum implication in step 2 is an instance of their criterion, not a newly claimed general Banach-algebra theorem. The topology of the nontrivial, stably trivial rank-two bundle over \(S^5\) is classical and is not newly claimed. The contribution here is the explicit combination into an **exact matrix-amplification law** for a geometrically natural continuous-trace algebra, identifying a maximal spectral-depth jump under strong Morita equivalence and the least sphere dimension for this bundle construction. The cited texts inspected do not state this stabilized law, although a combination of the prior criterion with classical clutching facts makes it accessible.

## Limitations
The result concerns the specific section algebra and full matrix amplifications; it does not classify spectral depths of arbitrary homogeneous \(C^*\)-algebras or assert invariance properties beyond those stated. No assertion of independent peer review or external validation is made. The closest follow-up paper's accessible abstract and introduction were inspected, not every page of its full text; an unindexed explicit matrix-stabilization example remains a possible priority risk.

## References
1. J. Bračič and M. Kandić, *On operators with many spectral components* (2026), arXiv:2611.12208, https://arxiv.org/abs/2611.12208 (first submitted 2026-11-09); especially Proposition 3.1 and Corollary 3.2.
2. J. Bračič and M. Kandić, *On operators with infinitely many spectral components* (2026), arXiv:2611.14394, https://arxiv.org/abs/2611.14394 (first submitted 2026-11-10).
3. J. Rosenberg, *Homotopy Theory: Vector Bundles and Characteristic Classes*, Math 748R, Homework 8 solutions (2012), https://terpconnect.umd.edu/~jmr/748RS12/hw8-sol.pdf , Problem 2 on the nontrivial stably trivial rank-two bundle over \(S^5\).
