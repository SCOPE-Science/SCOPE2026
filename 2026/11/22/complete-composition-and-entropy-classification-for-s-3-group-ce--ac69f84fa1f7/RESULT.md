# Complete composition and entropy classification for \(S_3\) group cellular automata

## Finding
Let \(G=S_3\) and \(X=G^{\mathbb Z}\) with pointwise multiplication and the bilateral shift \(\sigma(x)_i=x_{i+1}\). Let \(\mathscr M\) be the monoid of all continuous, shift-commuting group endomorphisms \(F:X\to X\). We determine this complete monoid, its composition, units, idempotents, center, semigroup-regular elements and exact topological-entropy spectrum.

For \(h\in\operatorname{Aut}(G)\), \(j\in\mathbb Z\), write
\[A_{h,j}(x)_i=h(x_{i+j}).\]
For a transposition \(\tau\in G\) and nonzero Laurent polynomial \(P=\sum_v p_vz^v\in\mathbb F_2[z,z^{-1}]\), write
\[B_{\tau,P}(x)_i=\tau^{\sum_v p_v\epsilon(x_{i+v})},\]
where \(\epsilon:G\to\mathbb F_2\) is permutation sign, and the exponent is interpreted in \(\{0,1\}\). Denote by \(0\) the constant map to the identity configuration.

**Classification.** Every element of \(\mathscr M\) has exactly one of these three normal forms. With multiplication interpreted as composition (left factor applied last):
\[
\begin{aligned}
A_{h,j}A_{k,l}&=A_{hk,j+l},\\
A_{h,j}B_{\tau,P}&=B_{h(\tau),z^jP},\\
B_{\tau,P}A_{h,j}&=B_{\tau,z^jP},\\
B_{\tau,P}B_{\upsilon,Q}&=B_{\tau,PQ}.
\end{aligned}
\]
Zero is absorbing; when a displayed product \(PQ\) vanishes, its value is zero. Since the Laurent polynomial ring is a domain, nonzero \(P,Q\) never have zero product.

The units form \(\operatorname{Aut}(S_3)\times\mathbb Z\cong S_3\times\mathbb Z\), and the nonunits form an ideal. There are exactly five idempotents: \(0\), \(A_{\mathrm{id},0}\), and the three sign projections \(B_{\tau,1}\). The center consists exactly of \(0\) and the pure shifts \(A_{\mathrm{id},j}\). An element \(B_{\tau,P}\) is semigroup-regular (some \(Y\in\mathscr M\) satisfies \(B_{\tau,P}YB_{\tau,P}=B_{\tau,P}\)) if and only if \(P=z^j\) for an integer \(j\).

For any specified neighborhood of \(r\ge1\) distinct sites, the exact number of possible local homomorphisms is \(1+6r+3(2^r-1)\). These are counted by allowed memory set, without requiring each site to be essential.

The topological entropies are
\[
\begin{aligned}
h_{\mathrm{top}}(A_{h,j})&=|j|\log6,\\
h_{\mathrm{top}}(B_{\tau,P})&=(\max(0,\max\operatorname{supp}P)-\min(0,\min\operatorname{supp}P))\log2,\\
h_{\mathrm{top}}(0)&=0.
\end{aligned}
\]
Consequently the complete realizable entropy set is \(\{k\log2:k\in\mathbb Z_{\ge0}\}\cup\{k\log6:k\in\mathbb Z_{\ge0}\}\). Apart from zero, the two branches are disjoint.

## Assumptions and scope
All maps are one-dimensional, bilateral, continuous group endomorphisms commuting with the shift; this is a strictly smaller class than arbitrary cellular automata on the six-symbol alphabet. The site neighborhood is finite by the Curtis–Hedlund–Lyndon theorem. No fixed-radius bound is imposed, except for the separate finite-neighborhood count. Topological entropy refers to temporal iteration of the cellular automaton, not the spatial entropy of its image.

## Proof
**(1) Exhaustive local homomorphism dichotomy.** A local rule on sites \(v_1,\dots,v_r\) is a homomorphism \(f:G^r\to G\). It factors uniquely as \(f(g_1,\ldots,g_r)=\prod_i u_i(g_i)\), with \(u_i:G\to G\) endomorphisms whose images commute pairwise, because the coordinate subgroups of \(G^r\) commute. The only normal subgroups of \(S_3\) are \(\{e\}\), \(A_3\), and \(S_3\). By the first isomorphism theorem, every endomorphism of \(S_3\) is trivial, an automorphism, or a map \(g\mapsto\tau^{\epsilon(g)}\) for one of its three transpositions. An automorphism image is all of \(S_3\), with trivial center; thus if one coordinate map is an automorphism, every other coordinate map must be trivial. Otherwise, any two nontrivial images are order-two subgroups. Two distinct transpositions do not commute, so all nontrivial coordinates use the same \(\tau\). This yields precisely the stated forms, including uniqueness. It also yields \(1+6r+3(2^r-1)\): one trivial rule, six automorphisms at each of \(r\) sites, and three choices of transposition for each nonempty subset.

**(2) Composition.** Sign is preserved by every automorphism of \(S_3\), and every transposition has odd sign. Evaluating compositions of the normal forms and collecting parity sums over \(\mathbb F_2\) gives the four laws, the last one by polynomial convolution \(PQ\). A zero sign-polynomial is exactly the constant map.

**(3) Algebraic structure.** A composition involving a sign-polynomial map cannot be a unit, so the sign maps and zero form an ideal; the other elements form \(\operatorname{Aut}(S_3)\times\mathbb Z\). Idempotency of \(A_{h,j}\) forces \(j=0,h=\mathrm{id}\), and idempotency of \(B_{\tau,P}\) forces \(P^2=P\), whence \(P=1\) since the Laurent ring is a domain. An element central in the monoid must commute with all \(A_{h,0}\); this rules out every nonzero \(B_{\tau,P}\), since automorphisms permute the transpositions transitively. A central automorphism-shift has \(h\) central in \(\operatorname{Aut}(S_3)\cong S_3\), so \(h=\mathrm{id}\); all pure shifts commute with cellular automata. Finally, for a nonzero sign element \(B_{\tau,P}\), regularity \(BYB=B\) demands \(P\cdot R=1\) for some Laurent polynomial \(R\) (whether \(Y\) is a unit or a sign element), and the only units of \(\mathbb F_2[z,z^{-1}]\) are monomials \(z^j\). Such monomials do have inner inverses \(B_{\upsilon,z^{-j}}\).

**(4) Temporal entropy.** Each \(A_{h,j}\) is a shift power composed with a finite-order alphabet automorphism, giving \(|j|\log6\). For nonzero \(P\), sign projects \(G^{\mathbb Z}\) onto the binary full shift, and the nonzero additive Laurent-polynomial automaton is surjective on that full shift. Thus \(B_{\tau,P}(X)=\langle\tau\rangle^{\mathbb Z}\); its restriction to that invariant image is the binary linear automaton with symbol \(P\). The entropy of a continuous map on a compact space equals the entropy on its eventual invariant image when its first image is invariant. The one-dimensional scalar polynomial entropy formula (Castronuovo–Dennunzio–Kari–Margara, Theorem 4, and its earlier scalar predecessors) gives the stated exponent span. Every \(k\log2\) occurs with \(P=z^k\) and every \(k\log6\) occurs with \(A_{\mathrm{id},k}\). Unique prime factorization shows the positive branches do not meet.

## Verification
The included standalone `verification/check_s3.py` enumerates all ten endomorphisms of \(S_3\), filters the commuting-image tuples for neighborhoods of one, two, and three sites, reproduces counts \(10,22,40\), and tests the composition and automorphism-interaction identities on cyclic configurations for a range of Laurent masks. It was executed successfully. These are finite consistency checks, not a substitute for the universal classification proof or the cited infinite-system entropy theorem.

## Relationship to prior work
The November 12, 2026 work of Castronuovo, Dennunzio, Kari and Margara proves effective computability and an exact characteristic-polynomial formula for entropy of abelian linear group cellular automata. Their 2025 predecessor develops general decomposition algorithms. This result instead gives the complete explicit composition monoid over the smallest nonabelian group, its intrinsic algebraic substructures, exact neighborhood census and full entropy spectrum. The scalar binary entropy formula and general factorization of a local group homomorphism are prior tools, not new claims.

## Limitations
No classification is asserted for cellular automata on \(S_3\) whose local rule is not a group homomorphism, for different finite nonabelian alphabets, or for higher-dimensional lattices. The monoid and entropy formulas are proved from finite-group structure and the cited entropy theorem; no independent audit has been performed. Earlier comprehensive treatments of monoids of algebraic cellular automata may imply part of this classification even if the inspected sources do not state it explicitly.

## References
1. N. Castronuovo, A. Dennunzio, J. Kari, L. Margara, *Topological Entropy of Group Cellular Automata is Effectively Computable* (first public November 12, 2026), https://arxiv.org/abs/2611.16746, especially Sections 2, 5 and 7.
2. N. Castronuovo, A. Dennunzio, L. Margara, *A Divide and Conquer Algorithm for Deciding Group Cellular Automata Dynamics* (2025), https://arxiv.org/abs/2507.09761.
3. A. Castillo-Ramírez, O. Mata-Gutiérrez, A. Zaldívar-Corichi, *Cellular automata over algebraic structures* (2019), https://arxiv.org/abs/1908.09675.
4. A. Castillo-Ramírez, *Generating infinite monoids of cellular automata* (2020), https://arxiv.org/abs/2004.07321 (related monoid context, not an inspected full-text noncoverage claim).
