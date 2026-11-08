# Entropy of maximum cube-product-free subsets

## Finding

Let \(\mathcal M(N)\) be the number of subsets \(A\subseteq\{1,\ldots,N\}\) of **maximum possible cardinality** among sets for which \(ab\) is not a perfect cube whenever \(a,b\in A\) are distinct. For \(N\ge1\), write \(L_N=\lfloor N^{1/3}\rfloor\). Let
\[
H(N)=\frac12\left(\sum_{\substack{u,v\ge1;\ uv\text{ squarefree}\\uv^2\le N,\ u^2v\le N}}
\mathbf1\left\{\left\lfloor\left(\frac N{uv^2}\right)^{1/3}\right\rfloor=
\left\lfloor\left(\frac N{u^2v}\right)^{1/3}\right\rfloor\right\}-1\right).
\]
All floors mean exact integer cube-root floors, so this defines an integer without floating-point conventions. The exact extremizer count is
\[
\boxed{\mathcal M(N)=L_N\,2^{H(N)}}.
\]
Put
\[
\delta=\prod_{p\text{ prime}}\left(1-\frac3{p^2}+\frac2{p^3}\right)>0.
\]
Then, as \(N\to\infty\),
\[
\boxed{H(N)\sim \frac{\delta}{2}(\pi^2-9)N^{2/3}},\qquad
\boxed{\log\mathcal M(N)=\left[\frac{\log2}{2}(\pi^2-9)\delta+o(1)\right]N^{2/3}}.
\]
The coefficient of \(N^{2/3}\) in the logarithm is approximately \(0.0864207\). In particular there are exponentially many maximum-size sets, with an explicit positive entropy constant. This result counts only *maximum-cardinality* subsets, not all maximal-by-inclusion or all admissible subsets.

## Assumptions and scope

The parameter \(N\) is any positive integer. A forbidden product involves two **distinct** members; this distinction allows one cube in each maximum set. All logarithms are natural. A positive integer is cube-free here when no prime cube divides it. The independent choices of paired cube-free kernels and the real-plane limiting region are as defined below. The theorem is unconditional and concerns cubes (third powers) only.

## Proof

**1. Complete component classification and exact multiplicity.** Every positive integer is uniquely \(rt^3\), where \(r\) is cube-free. It has a unique factorization \(r=uv^2\) with \(u,v\) squarefree and coprime (equivalently, \(uv\) squarefree). Its complementary kernel is \(r^*=u^2v\). The product of two integers is a cube exactly when their cube-free kernels are complementary. The available class at kernel \(r\) is
\[
\mathcal C_r(N)=\{rt^3:1\le t,\ rt^3\le N\},\qquad
c_r(N)=\left\lfloor(N/r)^{1/3}\right\rfloor.
\]
For \(r\ne r^*\), the forbidden-pair graph on the two classes \(\mathcal C_r(N)\), \(\mathcal C_{r^*}(N)\) is complete bipartite and has no edges within either class. Its maximum independent sets consist of the larger class, uniquely when sizes differ, or either whole class when the two positive sizes agree. If one side is absent, only the nonempty class is chosen, with no multiplicity. Complementarity of cube-free kernels fixes \(r\) precisely when \(r=1\); the cubes \(\mathcal C_1(N)\) form a clique, from which a maximum set chooses any one of \(L_N\) elements. All components are disjoint, hence independent. The ordered pairs \((u,v)\) and \((v,u)\) encode the same nontrivial complementary pair. Among positive pairs with squarefree product the only fixed pair is \((1,1)\). Therefore the number of tied nontrivial components is exactly \(H(N)\), proving the exact formula.

**2. Continuous tie region.** Put \(L=N^{1/3}\), \(x=u/L\), \(y=v/L\). The two class sizes equal \(\lfloor(xy^2)^{-1/3}\rfloor\) and \(\lfloor(x^2y)^{-1/3}\rfloor\). Both must be positive. Define
\[
\Omega=\bigcup_{j\ge1}\left\{(x,y)\in\mathbb R_{>0}^2:
(j+1)^{-3}<xy^2\le j^{-3},\quad
(j+1)^{-3}<x^2y\le j^{-3}\right\}.
\]
The ordered sum in the definition of \(H(N)\) is exactly the number of lattice points \((u,v)\in L\Omega\) with \(uv\) squarefree. In the change of coordinates \(s=xy^2\), \(t=x^2y\), the absolute Jacobian is \(\frac13(st)^{-2/3}\). Each \(j\)-square contributes
\[
\frac13\left[\int_{(j+1)^{-3}}^{j^{-3}}s^{-2/3}\,ds\right]^2
=3\left(\frac1j-\frac1{j+1}\right)^2.
\]
Consequently
\[
\operatorname{area}(\Omega)=3\sum_{j\ge1}\frac1{j^2(j+1)^2}
=3\left(2\zeta(2)-3\right)=\pi^2-9.
\]
The union is unbounded but has finite positive area.

**3. Arithmetic density in compact regions.** For any bounded Jordan-measurable region \(K\subset\mathbb R^2\),
\[
\#\{(u,v)\in LK\cap\mathbb Z_{>0}^2:uv\text{ squarefree}\}
=\delta\operatorname{area}(K)L^2+o_K(L^2).
\]
Indeed, for a prime \(p\), the permitted residue pairs modulo \(p^2\) are those where neither coordinate is divisible by \(p^2\) and the two are not both divisible by \(p\). Their proportion is exactly \((1-1/p)^2(1+2/p)=1-3/p^2+2/p^3\). For finitely many primes the Chinese remainder theorem and lattice-point equidistribution in Jordan sets give the product of these local factors. Pairs violating squarefreeness at some prime \(p>P\) have density \(O(1/P)\), uniformly after taking \(L\to\infty\): on a bounded box of side \(O(L)\), square divisibility in a coordinate contributes \(O(L^2\sum_{p>P}p^{-2}+L^{3/2})\), and simultaneous divisibility of both coordinates contributes \(O(L^2\sum_{p>P}p^{-2}+L\log L+L)\). Let \(P\to\infty\); absolute convergence of the Euler product gives the claimed constant \(\delta\). This also establishes \(\delta>0\).

**4. Removing the noncompact tails.** The two defining bounds for \(\Omega\) imply \(uv^2\le L^3\) and \(u^2v\le L^3\). For any \(0<\eta<1<M\), counting lattice pairs without the squarefree restriction gives
\[
\#\{(u,v)\in L\Omega:u<\eta L\}=O(\sqrt\eta L^2+L^{3/2}),
\]
using \(v\le\sqrt{L^3/u}\) and summing over \(u\). Similarly
\[
\#\{(u,v)\in L\Omega:u>ML\}=O(L^2/M+L^{3/2}),
\]
using \(v\le L^3/u^2\). The same inequalities hold with \(u,v\) interchanged. Thus the region outside \([\eta,M]^2\) has normalized point count \(O(\sqrt\eta+M^{-1})+o(1)\). On each such compact square, \(\Omega\) is Jordan measurable: only finitely many smooth boundary curves \(xy^2=j^{-3}\), \(x^2y=j^{-3}\) occur. Applying step 3, then sending \(\eta\downarrow0\), \(M\uparrow\infty\), proves
\[
\#\{(u,v)\in L\Omega:uv\text{ squarefree}\}
=\delta(\pi^2-9)L^2+o(L^2).
\]
Removing the unique diagonal pair and dividing by two gives the asymptotic for \(H(N)\). Finally \(\log L_N=O(\log N)=o(N^{2/3})\) and \(\log\mathcal M(N)=\log L_N+H(N)\log2\), completing the proof.

## Verification

Run the standalone standard-library-only script `python verify.py` and compare stdout with `verify_output.txt`. It exhaustively enumerates all cube-product-free subsets through \(N=16\), verifies both maximum sizes and numbers of maximum subsets, and calculates the exact tie exponents for six larger cutoffs through \(N=10^7\). Numerical normalization agrees with the stated positive constant. These are finite diagnostics, not the infinite proof; steps 1–4 establish the mathematical statements.

## Relationship to prior work

Yang and Zhao (2026), especially their Section 2, prove the complementary-kernel component decomposition and exact formulas for the **maximum size** \(F_{2,d}(N)\), and use a squarefree sieve to evaluate its asymptotic deficiency. They explicitly observe that either side may be chosen in a tie. The component decomposition and sieve machinery are prior results, not new claims here. The present distinct target is the **number of maximum-cardinality sets**, whose leading logarithm depends on counting exactly equal, positive paired class sizes; the square-slab volume \(\pi^2-9\) and the entropy constant are not the size constant \(\pi^2\delta/4\). Fleiner, Juhász, Kövér, Pach, and Sándor (2024 preprint) established earlier extremal-size bounds and also described the complementary cube-free classes. Their examined text does not report the asymptotic number of extremizers. An unindexed equivalent count cannot be ruled out.

## Limitations

No claim is made for higher perfect powers, for nonmaximum admissible sets, or for the number of maximal-by-inclusion sets. There is no effective error term beyond \(o(N^{2/3})\) in the entropy law. The Euler product's numerical approximation is illustrative and not a certified rigorous enclosure. Priority is based on inspected accessible sources and searches, not on a universal novelty guarantee. Independent mathematical auditing has not occurred.

## References

1. Quan-Hui Yang and Lilu Zhao, *Products of Two Integers Avoiding Perfect Powers*, arXiv:2608.11921v1 (first public posting 2026-08-12), especially Sections 1–4; https://arxiv.org/abs/2608.11921.
2. Zsigmond György Fleiner, Márk Hunor Juhász, Blanka Kövér, Péter Pál Pach, and Csaba Sándor, *Product representation of perfect cubes*, arXiv:2405.12088 (first preprint 2024-05-20), particularly the proof of Theorem 6; https://arxiv.org/abs/2405.12088.
