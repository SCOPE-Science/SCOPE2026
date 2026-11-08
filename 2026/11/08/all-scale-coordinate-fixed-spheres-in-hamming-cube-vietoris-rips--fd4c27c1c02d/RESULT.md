# All-scale coordinate-fixed spheres in Hamming-cube Vietoris–Rips complexes

## Finding

For every integer \(n\geq1\) and every integer \(0\leq r<n\), let \(Q_n=\{0,1\}^n\) have Hamming distance, let \(X_{n,r}=\operatorname{VR}_{\leq r}(Q_n)\) be its inclusive Vietoris–Rips complex, and let \(S_n\) act by permuting coordinates. Put
\[
a=\left\lfloor\frac r2\right\rfloor,\qquad t=n-r,\qquad s=\left\lfloor\frac a t\right\rfloor.\]
Then the geometric fixed-point space has an explicit finite simplicial model that collapses onto the boundary of the \((s+1)\)-dimensional cross-polytope. In particular,
\[
\left|X_{n,r}\right|^{S_n}\simeq S^s.
\]
The simultaneous bit-complement involution commutes with coordinate permutations, acts freely on this fixed space, and acts on \(\widetilde H_s(-;\mathbb Z)\cong\mathbb Z\) by multiplication by \((-1)^{s+1}\). For \(r\geq n\), the entire Rips complex and its fixed space are simplices and hence contractible.

## Assumptions and scope

An inclusive Rips simplex is a finite collection of binary words whose pairwise Hamming distances are at most the integer scale \(r\). The fixed points are those of the **geometric realization**, not only pointwise fixed vertices of the original complex. The action is the entire coordinate permutation group \(S_n\); complementation is a commuting additional involution, not part of the group whose fixed space is taken. The statement includes \(r=0\), \(n=1\), and every intermediate radius; no assertion is made about the inclusions between successive fixed-space stages.

## Proof

**Orbit simplices.** The orbits of \(S_n\) on \(Q_n\) are the Hamming-weight layers \(W_i\), indexed by \(0\leq i\leq n\). In any simplex fixed pointwise by the induced geometric action, the barycentric coefficients are constant along each orbit. Consequently, taking the normalized barycenter of each eligible orbit gives a PL simplicial model \(K_{n,r}\) of \(|X_{n,r}|^{S_n}\). A set of layer indices spans a simplex of \(K_{n,r}\) exactly when the union of the corresponding full layers spans an original Rips simplex. In particular, unlike the pointwise fixed **vertex** set, the orbit-barycenter model retains nontrivial fixed simplices.

**Exact compatibility.** The diameter of a weight layer is
\[
\operatorname{diam}(W_i)=2\min(i,n-i).
\]
For distinct weights \(i,j\), the maximum distance between a vector in \(W_i\) and one in \(W_j\) is
\[
\max\{d_H(x,y):x\in W_i,\ y\in W_j\}=\min(i+j,2n-i-j).
\]
These equalities follow respectively by choosing disjoint supports when possible and by choosing supports whose union fills all coordinates otherwise. Thus, for \(r<n\), an eligible orbit must lie among the low weights \(0,\ldots,a\) or high weights \(n-a,\ldots,n\), and these two sets are disjoint. Every pair of low weights is compatible, as is every pair of high weights. Label the low weight \(i\) by \(L_i\) and high weight \(n-j\) by \(R_j\), for \(0\leq i,j\leq a\). The two layers are incompatible precisely when
\[
\min(n+i-j,n-i+j)>r
\quad\Longleftrightarrow\quad |i-j|<n-r=t.
\]
Since a Rips complex is flag, this completely determines every face. Hence \(K_{n,r}=\operatorname{Ind}(B_{a,t})\), where \(B_{a,t}\) is the bipartite band graph with shores \(\{L_0,\ldots,L_a\}\) and \(\{R_0,\ldots,R_a\}\), having an edge \(L_iR_j\) if and only if \(|i-j|<t\).

**Folding lemma.** If distinct nonadjacent graph vertices \(u,v\) satisfy \(N(u)\subseteq N(v)\), then \(\operatorname{Ind}(G)\) simplicially collapses onto \(\operatorname{Ind}(G-v)\). Indeed, pair each independent set containing \(v\) but not \(u\) with the set formed by adding \(u\). This addition is legal because every neighbor of \(u\) is also a neighbor of \(v\). Process pairs in decreasing order of the smaller face's cardinality. At its turn, the smaller face has its paired upper face as its only remaining proper coface; therefore every pair is an elementary simplicial collapse. The procedure deletes precisely all faces containing \(v\), and proves the lemma without a homology approximation.

**Uniform band reduction.** For \(b=0,t,2t,\ldots\), up to \(b\leq a\), first delete \(L_{b+1},\ldots,L_{\min(a,b+t-1)}\) using \(L_b\) as the smaller-neighborhood vertex in the folding lemma. Then delete \(R_{b+1},\ldots,R_{\min(a,b+t-1)}\) using \(R_b\). These are valid neighborhood inclusions even after earlier blocks have been processed: before the left deletions, the surviving neighbors of \(L_b\) are \(R_b,\ldots,R_{\min(a,b+t-1)}\), all of which are neighbors of the left vertices being deleted. After the left deletions, \(R_b\) has only \(L_b\) as a surviving neighbor, and that vertex is adjacent to each right vertex being deleted. The graph remaining after all blocks consists exactly of the disjoint edges \(L_{kt}R_{kt}\), one for each \(0\leq k\leq\lfloor a/t\rfloor\). Thus \(K_{n,r}\) collapses onto the independence complex of \(s+1\) disjoint edges. That complex is the join of \(s+1\) copies of \(S^0\), the boundary of the \((s+1)\)-cross-polytope, and is homeomorphic to \(S^s\). This proves the homotopy statement over the integers, with no finite-range restriction.

**Complement action.** Bit complementation sends the barycenter of \(W_i\) to that of \(W_{n-i}\) and hence swaps \(L_i\) and \(R_i\). Their union cannot be a Rips simplex for \(r<n\), since it contains a pair of complementary words at distance \(n\). No geometric point can therefore have equal positive barycentric coefficients on both layers and be fixed by complementation. The induced involution on the fixed space has no fixed points. Its Lefschetz number is zero; the established sphere homotopy type gives \(0=1+(-1)^s\lambda\), where \(\lambda\in\{\pm1\}\) is its action on the rank-one reduced integral homology. Hence \(\lambda=(-1)^{s+1}\). This includes the disconnected case \(s=0\), using reduced zero-dimensional homology.

For \(r\geq n\), every pair of cube words is compatible. The original complex is the full simplex on \(Q_n\), whose coordinate-fixed locus is itself a nonempty simplex on orbit barycenters, so the fixed space is contractible.

## Verification

The self-contained Python program `verify_fixed_rips.py` makes 55 direct orbit-distance comparisons for all \(1\leq n\leq10\) and \(0\leq r<n\), reconstructing the orbit model from actual binary words rather than using the formula under test. It separately computes reduced mod-two homology for all 55 orbit complexes, verifies 1,220 explicitly ordered band-graph fold sequences with \(0\leq a\leq60\), \(1\leq t\leq20\), and checks 28 full elementary simplicial collapse sequences by enumerating their face sets. These checks completed successfully and are supplementary to the unrestricted proof.

Run `python3 verify_fixed_rips.py` using Python 3.10 or newer. The accompanying `verification_output.txt` contains the observed stdout. The reduced mod-two checks cannot by themselves certify the integral or infinite-family conclusions; those follow from the explicit simplicial collapses and Lefschetz argument.

## Relationship to prior work

Galetto, Montaño and Wellner (arXiv:2606.20784, first submitted 2026-06-18) determine representations of the **whole** hypercube Rips homology at scales at most three and at the submaximal scale. Those representations do not give geometric fixed-space homotopy types. Bendersky, Elia and Grbić (arXiv:2605.00705) develop all-scale cohomological bounds and cross-polytope generators of the whole Rips complexes, but not the orbit-barycenter fixed spaces. Adams and Virk (arXiv:2309.06222) prove whole-complex homological bounds and nullhomotopy of scale-inclusion maps, which do not imply a classification of the fixed-point spaces or their inclusion maps.

A prior coordinate-fixed classification covers the **single radius** \(r=n-2\), in which the forbidden band has width two; this theorem recovers that special radius but goes beyond it by classifying **every** scale below the diameter with the explicit variable-band recurrence and the complement character. This all-scale theorem does not follow from the earlier single-radius formula merely by substituting a parameter: the orbit compatibility and domination sequence must be established for arbitrary positive bandwidth \(t\).

## Limitations

The theorem concerns geometric fixed spaces of the full permutation group, not arbitrary coordinate subgroups, and does not determine equivariant attaching maps or persistent homology **between** successive fixed-space stages. It makes no statement about the topology of the much larger unrestricted Rips complexes at unknown radii. The result is subject to the possibility of unindexed or differently formulated equivalent previous work.

## References

- Federico Galetto, Jonathan Montaño and Zoe Wellner, *Homology of Vietoris-Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784 (first public submission 2026-06-18), https://arxiv.org/abs/2606.20784.
- Martin Bendersky, Salvatore Elia and Jelena Grbić, *Cohomological properties of the Vietoris--Rips Complex of a Hypercube Graph*, arXiv:2605.00705 (2026-05-01), https://arxiv.org/abs/2605.00705.
- Henry Adams and Žiga Virk, *Lower bounds on the homology of Vietoris-Rips complexes of hypercube graphs*, arXiv:2309.06222 (2023-09-12), https://arxiv.org/abs/2309.06222.
