# Two-type numerical rigidity and unbounded unary collisions in semigeneric directed graphs

## Finding

Let \(M\) be the countable homogeneous **semigeneric complete multipartite digraph**, described below. For a finite nonempty set \(A\) of individually named vertices, let \(n=|A|\), and let \(k\) be the number of nonadjacency classes meeting \(A\). For each integer \(r\ge0\), let \(t_r(A)\) be the number of complete types of an ordered \(r\)-tuple of pairwise distinct vertices, all different from \(A\), over these individually named parameters. Set \(t_0(A)=1\).

**Complete marked-base spectrum.** With \({j\brace\ell}\) denoting a Stirling number of the second kind, every count depends only on \((n,k)\), and is
\[
\boxed{t_r(n,k)=\sum_{\ell=0}^{r}\sum_{j=\ell}^{r}\binom{r}{j}k^{r-j}{j\brace\ell}\,2^{\ell n+(k+\ell-1)r-k\ell-\binom{\ell}{2}}.}
\]
In particular,
\[
\boxed{t_1(n,k)=2^n+k2^{k-1},\qquad t_2(n,k)=2^{2n+1}+(2k+1)2^{n+k}+k^22^{2k-2}.}
\]

**Sharp numerical recovery.** For any two nonempty named bases \(A,A'\), possibly of *different* sizes, equality of \(t_1\) and \(t_2\) forces equality of both their base sizes \(n\) and numbers of represented classes \(k\), and therefore equality of all their higher-arity counts. The cardinality of the base need not be supplied separately. One count is not sufficient, even with arbitrarily large differences in base size: for any \(g\ge0\), \(e\ge1\), put
\[
k=2^{g+2}(2^e-1)-1,\qquad n=k+g.
\]
Both \((n,k)\) and \((n+e,k-1)\) are feasible occupancy pairs, and they have equal \(t_1\) but strictly different \(t_2\). The smallest displayed example is \((3,3)\) versus \((4,2)\): both have \(t_1=20\), but their two-type counts are respectively \(720\) and \(848\).

The conclusion concerns the **numerical spectra**. It does not recover the orientations or sizes of the individual occupied classes within the named finite graph.

## Assumptions and scope

Nonadjacency, augmented by equality, is an equivalence relation \(E\) whose classes are infinite. Distinct \(E\)-classes are completely joined by oriented edges. The semigeneric axiom says that for any two distinct classes and any choice of two vertices in each class, the number of edges directed from the first chosen pair toward the second is even. Equivalently, binary cross-orientation matrices have even \(2\)-by-\(2\) rectangle sums. The countable homogeneous structure has exactly the finite digraphs satisfying these constraints as its age; therefore complete types of finite injective tuples over \(A\) correspond to admissible labelled extensions of the finite diagram \(A\). An element from an already represented class but different from every parameter is a new vertex, not an algebraic repetition.

No claim is made for arbitrary homogeneous digraphs, non-injective tuples or probabilistic sampling of actual vertices.

## Proof

**1. Counting parity orientations of a fixed class partition.** Fix a labelled finite vertex set with \(N\) elements and \(h\) equivalence classes of sizes \(s_1,\ldots,s_h\). For each unordered pair of classes of sizes \(u,v\), the binary orientation matrix \(X\) satisfies \(X_{ab}+X_{a'b}+X_{ab'}+X_{a'b'}=0\) modulo two. Precisely the solutions \(X_{ab}=\rho_a+\gamma_b\) are allowed, with one simultaneous-bit-flip redundancy. Thus there are \(2^{u+v-1}\) cross-orientations for that pair, including singleton classes. Different pairs of classes are unconstrained relative to each other. The total number is
\[
2^{\sum_{i<j}(s_i+s_j-1)}=2^{(h-1)N-\binom h2}.
\]
This class-partition formula is established in earlier work; the present proof uses it for **fixed named-base extension fibres** and then proves the numerical rigidity assertion.

**2. Exact extension fibres over a named base.** Fix the actual admissible orientations of a named base of size \(n\) meeting \(k\) classes. For \(r\) labelled new coordinates, choose \(j\) of them whose \(E\)-classes are not represented in the base, in \(\binom rj\) ways. The other \(r-j\) coordinates independently choose among the \(k\) existing classes, in \(k^{r-j}\) ways. Partition the \(j\) selected coordinates into \(\ell\) nonempty newly introduced classes, in \({j\brace\ell}\) ways. The entire extension then has \(n+r\) vertices and \(k+\ell\) classes. In every pair of old classes, the parity-compatible matrix solution space restricts surjectively to the given old matrix: a row/column decomposition of the old matrix extends by assigning new row or column bits. All class-pair blocks are independent. Hence the number of orientation assignments consistent with the *fixed actual old graph* is the quotient
\[
2^{(k+\ell-1)(n+r)-\binom{k+\ell}{2}-\left((k-1)n-\binom k2\right)}
=2^{\ell n+(k+\ell-1)r-k\ell-\binom\ell2}.
\]
Summing these contributions proves the all-arity formula. Every resulting finite diagram embeds over the old base in the homogeneous limit, giving precisely distinct complete types. For \(r=1\) the cases \(\ell=0,1\) give the first formula; for \(r=2\) the cases \(\ell=0,1,2\) give the second.

**3. A one-count equality forces strict two-count separation when class numbers differ.** Write \(U=t_1\), \(V=t_2\). Elimination of \(2^n\) using \(U\) gives the exact identity
\[
V(n,k)=2U^2+2U\,2^{k-1}-k(k+2)2^{2k-2}.
\]
Suppose \(U(n,k)=U(m,j)\) and \(k>j\ge1\). The term \(k2^{k-1}\) is strictly increasing, so \(n<m\). Put \(q=2^{k-j}\ge2\) and \(L=2^{j-1}\). The one-type equality becomes
\[
2^{n-j+1}(2^{m-n}-1)=kq-j.
\]
In particular \(U/L=2^{n-j+1}+kq<2kq\). Subtracting the two expressions for \(V\), and dividing by \(L^2\), yields
\[
\frac{V(n,k)-V(m,j)}{L^2}
=2\frac UL(q-1)-k(k+2)q^2+j(j+2)
< -k(k-2)q^2-4kq+j(j+2).
\]
If \(k=2\), necessarily \(j=1\) and \(q=2\), so the right-hand bound is \(-13\). If \(k\ge3\), using \(q\ge2\) and \(j\le k-1\), it is at most
\[
-4k(k-2)-8k+(k^2-1)=-3k^2-1<0.
\]
Therefore \(V(n,k)<V(m,j)\). This rules out simultaneous equal first and second counts with unequal class numbers. If class numbers are equal, equality of \(U=2^n+k2^{k-1}\) forces equal base sizes. Thus the ordered numerical pair \((t_1,t_2)\) universally recovers \((n,k)\) and every higher count.

**4. Arbitrarily separated unary collisions.** For \(g\ge0\) and \(e\ge1\), take \(k=2^{g+2}(2^e-1)-1\), \(n=k+g\). Then \(k\ge3\), \(k\le n\), \(k-1\le n+e\), and
\[
\begin{aligned}
t_1(n+e,k-1)-t_1(n,k)
&=2^{n+e}-2^n+(k-1)2^{k-2}-k2^{k-1}\\
&=2^{k-2}\left(2^{g+2}(2^e-1)-(k+1)\right)=0.
\end{aligned}
\]
The strict ordering from Step 3 shows \(t_2(n,k)<t_2(n+e,k-1)\). Every feasible \((n,k)\) is realized by a finite base, so every such unary collision occurs in the specified homogeneous digraph. Because \(e\) is arbitrary, the difference of base sizes is unbounded. This proves that arity two is the sharp universal numerical recovery threshold.

## Verification

The standalone standard-library script `code/verify_semigeneric.py` enumerates parity-compatible cross-class orientation diagrams over representative fixed old bases, **without** using the closed formula for direct diagram generation. It checks the displayed formula for all \(1\le n\le4\), \(1\le k\le n\), \(0\le r\le2\), selected triple types, and a changed old-base orientation. Separately, it checks both closed small-arity expressions, all numerical collisions within \(n\le89\), and twenty members of the explicit unary collision family. The recorded output is `verification/check_output.txt`. Re-run using `python code/verify_semigeneric.py`. Finite checks corroborate, rather than prove, the universal statements; their proof is in Steps 1–4.

## Relationship to prior work

Cherlin describes the semigeneric digraph and its even-parity constraint. Coskey and Ellis (2015 preprint, section 4) prove an equivalent two-class row/column decomposition for the automorphism/conjugacy study; Jasiński and collaborators also describe the semigeneric parity construction. The published result *Exact Stirling-layer orbit profile of the semigeneric complete multipartite digraph* provides the **unmarked** labelled-age count \(\sum_h {N\brace h}2^{(h-1)N-\binom h2}\), so the fixed-partition orientation formula is explicitly credited as prior work. This does **not** imply that the pair of numerical counts of pointwise named-base extensions recovers both \(n\) and \(k\) without knowing the number of parameters; the latter relies on the strict Diophantine comparison and the unbounded collision construction above.

The published result *Arity-two saturation and unbounded collisions in finite-base type spectra of the countable grid* instead treats two transverse equivalences and reconstruction conditional on known base cardinality. The result *Cycle-parity symmetry character for two-part semigeneric digraphs* counts unlabelled two-class symmetry orbits, not finite-base extension types. Targeted searches did not establish a covering earlier theorem under an equivalent formulation. Exact historical priority is not certified.

## Limitations

All new finite-base counting formulas ultimately derive from an earlier parity-matrix rank lemma; the new substantive claim is the global **numeric two-arity recovery theorem**, together with its sharp unary obstruction family, not the parity lemma or mere substitution into the unmarked age formula. The spectrum does not recover individual class sizes or edge orientations. The verification script tests finite cases; the proof is symbolic. An uncatalogued equivalent older result remains possible. No independent mathematical validation has been performed.

## References

1. Samuel Coskey and Paul Ellis, *The conjugacy problem for automorphism groups of homogeneous digraphs*, arXiv:1509.04222 (first posted 14 September 2015), section 4, https://arxiv.org/abs/1509.04222. MSC 03C15.
2. Gregory Cherlin, *Homogeneous directed graphs: the imprimitive case*, early classification preprint, section I, https://sites.math.rutgers.edu/~cherlin/Paper/43HDG-Imprimitive.pdf.
3. Jakub Jasiński et al., *Ramsey precompact expansions of homogeneous directed graphs*, arXiv:1310.6466 (first posted 24 October 2013), semigeneric section, https://arxiv.org/abs/1310.6466.
4. *Exact Stirling-layer orbit profile of the semigeneric complete multipartite digraph*, public published-finding corpus mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-stirling-layer-orbit-profile-of-the-semigeneric-complete-m--5135d85e91a6.
5. *Arity-two saturation and unbounded collisions in finite-base type spectra of the countable grid*, public published-finding corpus mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-arity-two-saturation-and-unbounded-collisions-in-finite-base-typ--801562567ff1.
