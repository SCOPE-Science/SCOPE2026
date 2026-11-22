# Unit-conjugacy orbit sizes of idempotent cycle-graph endomorphisms

## Finding
Let \(C_n\) be the simple undirected loopless cycle on vertices \(\mathbb Z/n\mathbb Z\), \(n\ge4\), and \(M_n=\operatorname{End}(C_n)\) its monoid of full edge-preserving maps. Its unit group is the dihedral automorphism group \(D_n\) of order \(2n\), acting on \(M_n\) by composition conjugation. For each \(n\) the following gives the complete image-rank and *unit-conjugacy orbit-size* distribution of the idempotents \(f^2=f\).

For odd \(n\), there is exactly one idempotent, the identity, forming one singleton orbit. Suppose \(n\) is even. Write \(A_k\) for the adjacency matrix of the simple \(k\)-vertex path, indexed by \(0,\ldots,k-1\), and let \(2\le k\le n/2+1\). Put \(L=n-k+1\) and
\[
T_{n,k}=\bigl(A_k^{L}\bigr)_{k-1,0},\qquad
S_{n,k}=\begin{cases}
\bigl(A_k^{L/2}\bigr)_{k-1,(k-1)/2},&k\text{ odd},\\[3pt]
\bigl(A_k^{(L-1)/2}\bigr)_{k-1,k/2-1}+\bigl(A_k^{(L-1)/2}\bigr)_{k-1,k/2},&k\text{ even}.
\end{cases}
\]
Then precisely \(S_{n,k}\) unit-conjugacy orbits of rank \(k\) have size \(n\), and precisely \((T_{n,k}-S_{n,k})/2\) orbits have size \(2n\). No other rank-\(k\) orbit sizes occur. The only orbit of size \(1\) is the identity. Consequently the complete rank-refined class polynomial is
\[
\boxed{K_n(z)=z^n+\frac12\sum_{k=2}^{n/2+1}(T_{n,k}+S_{n,k})z^k.}
\]
The number of labeled idempotents at rank \(k<n\) is \(nT_{n,k}\), agreeing with the preexisting labeled-retraction census. The number having nontrivial unit stabilizer is exactly \(1+n\sum_k S_{n,k}\). For uniformly random idempotents the probability of nontrivial unit stabilizer is \(O(n(\sqrt2/\varphi)^n)\) along even \(n\), where \(\varphi=(1+\sqrt5)/2\). In particular, asymptotically almost every nonidentity idempotent has the maximal dihedral conjugacy orbit of size \(2n\), and
\[
\#(\text{unit-conjugacy classes})\sim\frac{\#(\text{idempotents})}{2n}.
\]
Exact pairs of labeled idempotent counts and conjugacy class counts for \(n=4,6,8,10,12,14,16\) are respectively \((9,3),(25,4),(73,8),(221,14),(685,36),(2157,83),(6881,234)\).

## Assumptions and scope
An endomorphism is a *strict* graph homomorphism: if vertices are adjacent, their images remain adjacent, not equal. It is a total vertex map. Multiplication means composition, and unit-conjugacy is \(f\mapsto gfg^{-1}\) for \(g\in D_n\); it is not two-sided multiplication by unrelated units, isomorphism of kernels, Green equivalence, or graph-reflection equivalence on an arbitrary auxiliary path. Image rank is the cardinality of the image. The formulas assume all \(n\ge4\), with the displayed nontrivial formulas only for even \(n\). The asymptotic probability and class-number asymptotic are along even \(n\to\infty\).

## Proof
**1. Images of retractions.** If \(f^2=f\), every vertex in \(\operatorname{Im}(f)\) is fixed. Because \(C_n\) is connected, its image vertex set is connected in the cycle. For a proper image it is a unique consecutive path of \(k\ge2\) vertices. Choosing its vertices as \(0,1,\ldots,k-1\) in cycle order, the complementary domain arc is an edge path of length \(L=n-k+1\) from \(k-1\) back to \(0\). The only freedom in \(f\) is a nearest-neighbor length-\(L\) walk \(w_0,\ldots,w_L\) in \(\{0,\ldots,k-1\}\) with \(w_0=k-1\) and \(w_L=0\). Thus there are exactly \(T_{n,k}\) retracts per image path, and \(nT_{n,k}\) total rank-\(k\) maps. Necessarily \(L\ge k-1\), giving \(k\le n/2+1\), and for even \(n\) the required walk parity is automatic. Conversely every such walk defines a retraction. The only surjective idempotent is the identity. If \(n\) is odd, the increment of a closed length-\(n\) nearest-neighbor walk, considered as an integer, is an odd multiple of \(n\) in \([-n,n]\); hence all increments have the same sign, every endomorphism is a rotation or reflection, and only the identity is idempotent.

**2. Stabilizer of an image.** The group \(D_n\) acts transitively on the \(n\) proper consecutive \(k\)-vertex image paths, with stabilizer of each path of order two: identity and reflection \(\rho\) reversing the path. Any unit centralizing a retraction must preserve its image, because \(\operatorname{Im}(gfg^{-1})=g(\operatorname{Im}f)\). Therefore a proper retraction's stabilizer has order one or two. The orbit-stabilizer theorem makes its conjugacy-orbit size respectively \(2n\) or \(n\).

**3. Reflection-fixed walk count.** For the representative image \(\{0,\ldots,k-1\}\), the unique nontrivial image stabilizer is \(\rho(i)=k-1-i\pmod n\). On the complementary arc, conjugation by \(\rho\) maps a walk \(w\) to \(w'_j=k-1-w_{L-j}\). Thus \(f\) is fixed exactly when \(w_j+w_{L-j}=k-1\) for every \(j\). If \(L\) is even (equivalently \(k\) is odd, since \(n\) is even), the midpoint image must be \((k-1)/2\); the first \(L/2\) steps can be chosen in \((A_k^{L/2})_{k-1,(k-1)/2}\) ways, and reflection uniquely forces the remainder. If \(L\) is odd (equivalently \(k\) even), the two middle images must be the adjacent central pair \(k/2-1,k/2\), in either order. The first \((L-1)/2\) steps end at one of these two vertices, giving the stated sum for \(S_{n,k}\). Again reflection uniquely completes the walk, and all its edges are valid. In particular \(T_{n,k}-S_{n,k}\) is even because reflection is an involution on the finite set of the \(T_{n,k}\) walks.

**4. Complete orbits.** The \(n\) labeled image paths comprise one transitive \(D_n\)-set. A reflection-fixed representative contributes one full \(D_n\)-orbit of size \(n\); a pair of mutually reflected, nonfixed walks contributes one orbit of size \(2n\). These account for all rank-\(k\) retractions and prove the polynomial. Replacing orbit counts with their sizes gives \(nS_{n,k}+2n(T_{n,k}-S_{n,k})/2=nT_{n,k}\), an independent consistency relation. The identity, fixed by every unit, supplies the lone rank-\(n\) singleton.

**5. Asymptotic disappearance of symmetric maps.** Each symmetric walk is determined by its first at most \(\lceil L/2\rceil\) signs, with at most one binary middle-edge choice. Hence \(S_{n,k}\le2^{(n+1)/2}\), so \(\sum_k S_{n,k}\le n2^{(n+1)/2}\). On the other hand, for all even \(n\ge6\), the rank-four walks obey \(T_{n,4}=F_{n-4}\), where \(F_j\) is the Fibonacci sequence defined by \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\); Indeed, for \(h_j=(A_4^{2j+3})_{3,0}\), the identity \(A_4^4=3A_4^2-I\) gives \(h_0=1\), \(h_1=3\), and \(h_{j+2}=3h_{j+1}-h_j\). Thus \(h_j=F_{2j+2}\), proving the claimed formula for all even \(n\). In particular \(\sum_kT_{n,k}\ge F_{n-4}\ge c\varphi^n\) for an absolute \(c>0\) and even \(n\ge6\). Since the number of symmetric idempotents is \(1+n\sum S\) and the number of all idempotents is \(1+n\sum T\), their ratio is \(O(n(\sqrt2/\varphi)^n)\). Finally \(K_n(1)=1+(\sum T+\sum S)/2\) and \(1+n\sum T\sim n\sum T\), yielding the class-number asymptotic. This asymptotic is elementary and does not rely on any numerical extrapolation.

## Verification
The standalone standard-library Python program `verify.py` enumerates all edge-preserving maps from closed nearest-neighbor walks for each \(4\le n\le16\), filters by \(f^2=f\), explicitly enumerates the full dihedral conjugation orbits, and checks every class rank and size against the transfer-matrix counts \(T_{n,k},S_{n,k}\). The reported complete totals for even \(n=4,6,8,10,12,14,16\) are \((9,3),(25,4),(73,8),(221,14),(685,36),(2157,83),(6881,234)\); odd dimensions each have one idempotent. Run `python3 verify.py` in this directory. The program prints `CYCLE_ORBIT_CLASSIFICATION_VERIFIED` upon complete success; an actual execution transcript is included as `verify_output.txt`. Finite checks corroborate, but the universal assertion and exponential estimate follow from the proof above.

## Relationship to prior work
Dimitrova–Fernandes–Koppitz–Quinteiro [1] give the semigroup theory of strict and weak cycle-endomorphism monoids, including total cardinalities, generators, Green relations and regularity. Their full arXiv preprint was inspected: they do not state this unit-conjugacy idempotent-orbit distribution. Published cycle-graph idempotent rank calculations [2] already give the stronger *labeled* counts \(nT_{n,k}\), so neither the walk formula \(T_{n,k}\) nor the known rank total is asserted to be new. The present result refines this total by the intrinsic dihedral-unit conjugation and its exact reflection-fixed strata, class sizes and asymptotic rarity. Previously established path-graph reflection-orbit formulas [3] use two independent exterior tails, rather than a single complementary cycle arc; they do not imply the present midpoint-walk formula without an additional cycle-specific argument. The older Michels–Knauer work [4] studies endomorphism counts and induced congruence classes; only its abstract was available to inspect, so an implicit stronger statement in the inaccessible full paper is a residual priority risk. None of these comparisons is a proof of historical uniqueness.

## Limitations
These formulas concern strict full graph endomorphisms, not weak maps, partial maps, or endomorphism kernels. The asymptotic probability estimate is a deliberately non-sharp upper bound; a sharper exponential rate is not claimed. The proof does not classify pairs of commuting idempotents or their multiplication table. Historical originality remains provisional pending broader expert literature review, especially the inaccessible full text of Michels–Knauer. No independent mathematical audit or external certification has been performed.

## References
[1] I. Dimitrova, V. H. Fernandes, J. Koppitz, T. M. Quinteiro, *On monoids of endomorphisms of a cycle graph*, arXiv:2310.04149v1 (first public 6 October 2023), https://arxiv.org/abs/2310.04149 ; subsequently *Mathematica Slovaca* 74 (2024), 1071–1088, DOI: 10.1515/ms-2024-0078.

[2] *Exact idempotent rank spectrum and sharp stretched-exponential law for even-cycle endomorphisms*, 8 November 2026, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-idempotent-rank-spectrum-and-sharp-stretched-exponential-l--503622b19b3b/RESULT.md .

[3] *Reflection-conjugacy orbit spectra of idempotent path endomorphisms*, 26 October 2026, https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-reflection-conjugacy-orbit-spectra-of-idempotent-path-endomorphi--4c53adec9545/RESULT.md .

[4] M. A. Michels and U. Knauer, *The congruence classes of paths and cycles*, *Discrete Mathematics* 309 (2009), 5352–5359, DOI: 10.1016/j.disc.2008.11.022, https://doi.org/10.1016/j.disc.2008.11.022 (abstract available; full article not inspected).
