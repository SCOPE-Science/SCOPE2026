# Exact two-sided halo saturation on finite cycles at the first bridging threshold

## Finding
For every integer \(N\geq3\), let \(G_N=\mathbb Z/N\mathbb Z\) with normalized counting measure and cyclic shift \(T(j)=j+1\). A *circular arc* is a set of \(\ell\) consecutive residues, with \(1\leq\ell\leq N\). For a nonempty \(E\subseteq G_N\), define the uncentered two-sided maximal average and its strict halo by
\[
M_E(v)=\max_{I\ni v}\frac{|I\cap E|}{|I|},\qquad H_\alpha(E)=\{v\in G_N:M_E(v)>\alpha\}.
\]
The exact minimum marked-set cardinality whose halo covers the whole orbit at the first three-site bridging threshold is
\[
\boxed{\min_{\varnothing\ne E\subseteq G_N\, :\,H_{2/3}(E)=G_N}|E|=\left\lfloor\frac N2\right\rfloor+1+\mathbf1_{\{N\equiv3\pmod4\}}.}
\]
A consecutive block of the displayed length always attains full saturation. In particular, for even \(N\geq4\), a half-density alternating set has full halo for every \(0<\alpha<2/3\), but **no** half-density set has full halo for \(\alpha\geq2/3\). The jump and the extra marked point when \(N\equiv3\pmod4\) are both sharp.

## Assumptions and scope
The space is the single uniform finite cycle of length \(N\geq3\); there is no randomness or limiting approximation. All inequalities defining a halo are *strict*. Witnesses are uncentered arcs, meaning that \(v\) may lie anywhere in the arc. These are also the sets of residues observed by uncentered interval averages along the full bilateral orbit: if a consecutive interval in \(\mathbb Z\) has length \(qN+r\), \(0\leq r<N\), its average is a convex combination of the full-cycle density \(|E|/N\) and an \(r\)-arc average. Consequently intervals with repeated cyclic visits cannot increase the strict halo beyond arcs of length at most \(N\).

## Proof
**A circular two-cover lemma.** Given any finite family of circular arcs that covers a specified set \(Z\subseteq G_N\), take a subfamily minimal under deletion while still covering \(Z\). No site lies in three members of this subfamily. Indeed, suppose three arcs \(I_1,I_2,I_3\) contain a common point \(p\). If an arc is the whole circle, it alone covers their union. Otherwise each complement \(G_N\setminus I_j\) is a (possibly empty) ordinary interval in the linear order obtained by cutting the circle at \(p\). Among their nonempty complements choose one with the rightmost left endpoint and one with the leftmost right endpoint. If both extrema occur in the same complement, its corresponding arc alone contains the other two arcs. Otherwise the intersection of the two chosen complements lies inside the remaining complement, so the two corresponding arcs cover all three. Hence one of any three co-occurring arcs is redundant, contradicting minimality. Thus the sum of their indicator functions is at most two at every site.

**The general lower bound.** Write \(k=|E|\), \(z=N-k\), and assume \(k\leq\lfloor N/2\rfloor\). The full circle has average at most \(1/2\), so for every unmarked site there is a proper witnessing arc \(I\) with
\[
3|I\cap E|>2|I|\quad\Longleftrightarrow\quad e(I)>2z(I),
\]
where \(e(I)=|I\cap E|\) and \(z(I)=|I\setminus E|\). Choose a deletion-minimal covering family \(I_1,\ldots,I_m\) of the \(z\) unmarked sites from these witnesses. Each arc has \(e(I_j)\geq2z(I_j)+1\). By the two-cover lemma and coverage,
\[
2k\geq\sum_{j=1}^m e(I_j)\geq2\sum_{j=1}^m z(I_j)+m\geq2z+m>2z.
\]
This contradicts \(k\leq z\). Hence every saturating set has at least \(\lfloor N/2\rfloor+1\) points.

**The congruence obstruction.** Now let \(N=4q+3\), \(q\geq0\), and suppose \(k=2q+2\), \(z=2q+1\). The full-cycle average \(k/N\leq2/3\) (equality only at \(N=3\)), so proper witnesses still exist. The previous chain becomes
\[
2z+2=2k\geq\sum_j e(I_j)\geq 2\sum_j z(I_j)+m\geq2z+m.
\]
Thus \(m\leq2\). A single witnessing arc cannot cover all unmarked sites, since it would need \(e(I_1)\geq2z+1>k\), so \(m=2\) and equality holds throughout. Consequently each marked point belongs to both witnessing arcs (because \(\sum e=2k\)); each unmarked point belongs to exactly one (because \(\sum z=z\)); and for each arc \(e(I_j)=2z(I_j)+1\). In particular \(e(I_j)=k=z+1\), forcing \(2z(I_j)=z\), impossible because \(z=2q+1\) is odd. The borderline cardinality is therefore excluded.

**Sharp consecutive-block construction.** Let
\[
k=\left\lfloor\frac N2\right\rfloor+1+\mathbf1_{\{N\equiv3\pmod4\}},\qquad z=N-k.
\]
Take \(E\) to be \(k\) consecutive sites. Any site in the complementary gap of \(z\) sites is covered by an arc containing the entire marked block and at most \(d=\lceil z/2\rceil\) unmarked sites: start at the nearer end of the gap and traverse the marked block. Its average is at least \(k/(k+d)>2/3\). The strict inequality follows by inspecting the four residue classes of \(N\pmod4\): respectively \((k,d)=(2q+1,q)\) for \(N=4q\); \((2q+1,q)\) for \(N=4q+1\); \((2q+2,q)\) for \(N=4q+2\); and \((2q+3,q)\) for \(N=4q+3\), with the degenerate empty gap at \(N=3\) immediate. Marked sites are in the halo via singleton arcs. This proves equality for all \(N\).

**Sharp threshold for half-density alternation.** When \(N\geq4\) is even, let \(E\) consist of alternating sites, so \(|E|=N/2\). Every unmarked site is centered within a three-site arc containing two marked sites, giving maximal average at least \(2/3\); hence its halo is full whenever \(\alpha<2/3\). Conversely, for \(\alpha\geq2/3\), a full halo would imply a full halo at \(2/3\), contradicting the proved lower bound \(k>N/2\).

## Verification
The self-contained standard-library script `VERIFY.py` computes every circular arc exactly by integer bit masks, uses the exact criterion \(3e>2\ell\), exhaustively tests every marked set for all \(3\leq N\leq14\), checks consecutive-block construction for \(3\leq N\leq200\), and checks alternating-set strict-threshold behavior for even \(4\leq N\leq100\). Run `python3 VERIFY.py`; the expected output starts with `VERIFY_OK`. Enumeration only corroborates the preceding all-size proof.

## Relationship to prior work
K. Huang (arXiv:2610.41156v1, 30 October 2026) studies uncentered discrete and ergodic maximal functions, sharp near-unit thresholds, and finite-period ergodic actions, including a finite-action eventual no-enlargement example in Section 5. That article does not give a sharp marked-set **full-halo saturation cardinality** at the fixed interior threshold \(2/3\), or the residue-class obstruction above. Hagelstein and Parissis (arXiv:1503.02900, 2015), particularly their uncentered ergodic Section 6, establish bounds near threshold one, not the finite-cycle optimization here. The classical interval overlap-two principle motivates the proof, but the circle-specific parity obstruction and sharp construction are additional steps. A forward one-sided orbit average is a different operator; its sharp finite-cycle halo cardinalities do not imply this two-sided full saturation threshold.

## Limitations
The result classifies only full saturation at the single threshold \(2/3\) and the half-density crossing for even cycles. It does not give the complete Tauberian function for all thresholds or all marked cardinalities, nor analogous results for centered arcs, nonuniform weights, or higher-dimensional actions. Mathematical correctness rests on the all-size combinatorial proof, while historical priority is assessed against the cited and searched literature, not guaranteed exhaustively.

## References
- K. Huang, *Sharp Solyanik Estimates for Discrete and Ergodic Hardy--Littlewood Maximal Operators*, arXiv:2610.41156v1 (first posted 2026-10-30), https://arxiv.org/html/2610.41156v1.
- P. A. Hagelstein and I. Parissis, *Solyanik estimates in ergodic theory*, arXiv:1503.02900 (first posted 2015-03-10); *Colloquium Mathematicum* 145 (2016), 193--207, https://arxiv.org/abs/1503.02900.
- K. Huang, *Solyanik Estimates for Ergodic Flows*, arXiv:2610.41151v1 (2026-10-30), https://arxiv.org/abs/2610.41151 (one-sided continuous-time comparison).
