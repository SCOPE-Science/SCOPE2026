# Fredholm end-count dichotomy for parent composition on tree Lipschitz spaces

## Finding
Let \(T\) be a countably infinite, locally finite, leafless rooted tree with root \(o\), with \(\pi(o)=o\) and \(\pi(v)=v^-\) for nonroot vertices. The parent-composition operator is \(C_\pi f=f\circ\pi\). Denote the number of children of \(v\) by \(d(v)\), and let \(b(T)=\#\{v:d(v)\ge 2\}\), which may be infinite.

**Theorem.** On each complex space \(X=\mathcal L(T)\) and \(X=\mathcal L_0(T)\), defining essential spectrum by failure of Fredholmness, the following exhaustive alternative holds.

* If \(b(T)<\infty\), the integer \(k=1+\sum_{v\in T}(d(v)-1)\) is the number of infinite ends, and
\[
\sigma_{\mathrm{ess}}(C_\pi)=\{\lambda\in\mathbb C:|\lambda|=1\},\qquad
\operatorname{ind}(C_\pi-\lambda I)=\begin{cases}-k,&|\lambda|<1,\\0,&|\lambda|>1.\end{cases}
\]
* If \(b(T)=\infty\), then
\[
\sigma_{\mathrm{ess}}(C_\pi)=\{\lambda\in\mathbb C:|\lambda|\le1\}.
\]
For every \(|\lambda|<1\), the range of \(C_\pi-\lambda I\) is closed and its cokernel is infinite-dimensional.

In both cases \(\sigma(C_\pi)=\{\lambda:|\lambda|\le1\}\). For any nonzero polynomial \(p\), when \(b(T)<\infty\), \(p(C_\pi)\) is Fredholm precisely when \(p\) has no zeros on the unit circle, with index
\[
\operatorname{ind}p(C_\pi)=-k\,\#\{z:p(z)=0,\ |z|<1\},
\]
zeros counted with multiplicity. When \(b(T)=\infty\), \(p(C_\pi)\) is Fredholm precisely when \(p\) has no zeros in the closed unit disk, and then its index is zero. Thus infinitely many branching vertices cause the Fredholm essential spectrum to fill its interior, although they do not change the ordinary spectrum.

## Assumptions and scope
The tree is infinite, countable, locally finite, rooted, and **leafless**, meaning \(1\le d(v)<\infty\) for all vertices. The spaces consist of complex-valued functions \(f\) with norm
\[
\|f\|_{\mathcal L}=|f(o)|+\sup_{v\ne o}|f(v)-f(v^-)|,
\]
and \(\mathcal L_0\) is the closed subspace with \(|f(v)-f(v^-)|\to0\) as \(|v|\to\infty\). Fredholm means closed range and finite-dimensional kernel and cokernel; the index is kernel dimension minus cokernel dimension. Only this Fredholm essential spectrum, rather than the alternative index-zero or Browder essential spectra, is asserted. The polynomial \(p\) is nonzero; a nonzero constant is permitted.

## Proof
**1. Edge-coordinate conjugacy.** Set \(E=T\setminus\{o\}\) and \(g(v)=f(v)-f(v^-)\). Since a tree has a unique finite root-to-vertex path, the map \(f\mapsto(f(o),g)\) is an isometric linear isomorphism \(\mathcal L(T)\cong\mathbb C\oplus_1\ell^\infty(E)\). Local finiteness makes the condition of tending to zero with depth equivalent to membership in \(c_0(E)\), yielding \(\mathcal L_0(T)\cong\mathbb C\oplus_1 c_0(E)\). Under either map,
\[
C_\pi\cong I_{\mathbb C}\oplus D,\qquad
(Dg)(v)=\begin{cases}0,&|v|=1,\\g(v^-),&|v|\ge2.\end{cases}
\]
Local finiteness ensures \(D:c_0(E)\to c_0(E)\), and leaflessness makes \(D\) an isometry on both \(c_0(E)\) and \(\ell^\infty(E)\), because every edge coordinate occurs among its children's coordinates. Thus \(D-\lambda I\) is injective for all \(\lambda\in\mathbb C\): for \(\lambda\ne0\), induct on depth from level one; for \(\lambda=0\), use injectivity of \(D\). For \(|\lambda|<1\),
\[
\|(D-\lambda I)g\|\ge(1-|\lambda|)\|g\|,
\]
so the range is closed. For \(|\lambda|>1\), a norm-convergent Neumann series inverts \(C_\pi-\lambda I\).

**2. Finite branching.** If only finitely many vertices branch, choose a finite depth beyond all of them. There are exactly \(k\) vertices at that depth and therefore \(k\) infinite one-child tails, where \(k=1+\sum_v(d(v)-1)\) follows by summing \(\#T_{n+1}-\#T_n=\sum_{|v|=n}(d(v)-1)\). Divide edge coordinates into a finite initial set and the \(k\) infinite tails. Relative to this decomposition, \(D\) differs by a finite-rank operator from a finite-dimensional operator direct-summed with \(k\) copies of the standard unilateral right shift \(R\) on \(c_0(\mathbb N)\) or \(\ell^\infty(\mathbb N)\). For \(|\lambda|<1\), \(R-\lambda I\) is injective with closed range of codimension one: an annihilating functional is \(h\mapsto\sum_{n\ge0}\lambda^n h_n\), and the recurrence \(x_n=(Rx)_n-\lambda x_n\) gives a bounded solution when the functional vanishes (or use index homotopy from \(R\), whose range is exactly the sequences vanishing at the first coordinate). Since the Fredholm index is locally constant on the disk, \(\operatorname{ind}(R-\lambda I)=-1\). Finite-rank perturbation does not alter Fredholmness or index, while finite-dimensional blocks have index zero. Hence \(\operatorname{ind}(D-\lambda I)=-k\), which also equals the index for \(C_\pi-\lambda I\).

**3. Infinite branching.** For each branching vertex \(u\), choose two different children \(a_0,b_0\), and then choose two infinite downward rays \(a_0,a_1,\dots\) and \(b_0,b_1,\dots\), possible by leaflessness. For \(|\lambda|<1\), define the bounded functional on either edge-coordinate space
\[
L_{u,\lambda}(g)=\sum_{j=0}^\infty\lambda^j\big(g(a_j)-g(b_j)\big).
\]
The first difference vanishes on \(Dg\); every subsequent difference of \(Dg\) is the preceding difference of \(g\). Therefore \(L_{u,\lambda}(Dg)=\lambda L_{u,\lambda}(g)\), and \(L_{u,\lambda}\) annihilates \(\operatorname{ran}(D-\lambda I)\). These functionals, one for each distinct branching vertex, are linearly independent: in any purported finite linear relation choose a vertex \(u\) of smallest depth among the finitely many selected and evaluate on a coordinate unit vector supported on one of its two chosen children. All functionals from deeper branching vertices vanish at that coordinate; those of equal depth and different vertices have disjoint child sets. This isolates its coefficient, and iteration removes every coefficient. Thus the range has infinite codimension, though it remains closed by the estimate in Step 1.

**4. Unit circle.** Fix \(|\lambda|=1\). For each integer \(N\ge2\), define the scalar tent profile \(h_n=\min(n/N,\,(2N-n)/N)\) for \(0\le n\le2N\), and \(h_n=0\) outside that range. On edge coordinates set \(g_N(v)=\lambda^{-|v|}h_{|v|}\). Local finiteness makes \(g_N\) finitely supported, so it is in both spaces. It has norm one, and
\[
\|(D-\lambda I)g_N\|\le\frac1N.
\]
Because \(D-\lambda I\) is injective, it cannot be Fredholm: an injective Fredholm bounded operator has a bounded inverse on its closed range and hence is bounded below. Thus the entire unit circle belongs to the Fredholm essential spectrum.

**5. Ordinary and polynomial spectra.** The foregoing proves \(|\lambda|>1\) is resolvent and \(|\lambda|<1\) is not surjective (finite case: index negative; infinite case: infinite cokernel); the unit circle follows by closedness. For a nonzero polynomial, factorization over \(\mathbb C\), Atkinson's theorem in the Calkin algebra, and additivity of the Fredholm index show that \(p(C_\pi)\) is Fredholm exactly when every factor \(C_\pi-zI\) is Fredholm, and its index is the sum of the corresponding indices, with multiplicity. Nonzero constants have index zero. This proves all assertions. \(\square\)

## Verification
The proof needs only the edge-coordinate conjugacy, finite-rank decomposition for finitely many branches, and explicit independent annihilating functionals for infinitely many branches. The accompanying checker verifies finite-depth combinatorial rank counts for branched trees, the exact eigenfunctional cancellation on finitely supported probes, and normalized unit-circle tent defects. Such finite tests are consistency checks, not proofs of the infinite Fredholm assertions.

## Relationship to prior work
Rivera-Guasco and Martínez-Avendaño (2019) determined the spectrum and approximate point spectrum of the forward shift on both tree Lipschitz spaces. Its forward shift differs from the parent composition operator here by a finite-rank operator at the root, but that paper does not calculate a branching-dependent Fredholm essential spectrum or the end-count index. Kong and Liu (2026) characterize Fredholm weighted composition operators and give \(\operatorname{ind}C_\varphi\) at the unshifted parameter. That does not itself determine all translated Fredholm operators \(C_\pi-\lambda I\) or their polynomial index law. Colonna and Martínez-Avendaño (2024) study spectra of composition operators on the little space, but do not formulate this Fredholm dichotomy. The result uses standard finite-rank stability and index additivity, while the precise finite/infinite branching division is derived directly.

## Limitations
Leaflessness and local finiteness are essential hypotheses. The result does not classify arbitrary tree symbols, weighted parent operators, Browder spectra, or all Fredholm essential-spectrum conventions. The original source's unshifted Fredholm result is acknowledged; the new scope is the complete translated and polynomial index classification. An equivalent pre-existing formulation under direct-sum shift or tree-end terminology could potentially subsume this result and remains a bibliographic risk. There is no independent audit.

## References
1. Junkai Kong and Lei Liu, *Fredholm weighted composition operators on the Lipschitz space of a tree*, arXiv:2611.11737 (initially public 2026-11-09), https://arxiv.org/abs/2611.11737.
2. Emmanuel Rivera-Guasco and Rubén A. Martínez-Avendaño, *The forward and backward shift on the Lipschitz space of a tree*, arXiv:1906.02372, https://arxiv.org/abs/1906.02372.
3. Flavia Colonna and Rubén A. Martínez-Avendaño, *Composition Operators on the Little Lipschitz space of a rooted tree*, arXiv:2410.14714, https://arxiv.org/abs/2410.14714.
