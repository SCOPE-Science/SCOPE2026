# Exact Mayer path homology and symmetry of shortcut-free three-level networks

## Finding

Let \(A,B,C\) be disjoint sets with cardinalities \(a,b,c\geq2\). Form the directed graph \(D(A,B,C)\) whose entire arc set is \(A\times B\cup B\times C\): all arcs point to the next level, and **no** arcs join the first and last levels. Let \(G=\mathfrak S_A\times\mathfrak S_B\times\mathfrak S_C\) act by permutation within levels. For each level \(X\), set \(P_X=\mathbb C[X]\), let \(U_X=\ker(\varepsilon_X:P_X\to\mathbb C)\) be its standard augmentation module, and write \(\mathbf1\) for the trivial \(G\)-module. A tensor product below means an outer tensor product of the indicated level modules, inflated to \(G\).

For every \(N\geq2\), every primitive \(N\)-th root \(\zeta\in\mathbb C\), and every \(1\leq q<N\), the **unreduced, nonregular Mayer path homology** of \(D(A,B,C)\) is completely determined as a \(G\)-representation by the following formulas, with \(t=N-q\):

\[
H_0^{N,q}\cong
\begin{cases}
\mathbf1,&t=1,\\
\mathbf1^{\oplus3}\oplus U_A\oplus U_C,&t=2,\\
\mathbf1^{\oplus3}\oplus U_A\oplus U_B\oplus U_C,&t\geq3.
\end{cases}
\]

\[
H_1^{N,q}\cong
\begin{cases}
0,&(N,q)=(2,1),\\
U_B\otimes(\mathbf1\oplus U_A\oplus U_C),&N\geq3,\ q=1,\\
\mathbf1^{\oplus2}\oplus U_A\oplus U_B\oplus U_C,&q\geq2,\ t=1,\\
(P_A\otimes P_B)\oplus(P_B\otimes P_C),&q\geq2,\ t\geq2.
\end{cases}
\]

\[
H_2^{N,q}\cong
\begin{cases}
U_A\otimes U_B\otimes U_C,&q=1,\\
U_B\otimes(U_A\oplus U_C\oplus(U_A\otimes U_C)),&q=2,\\
P_A\otimes U_B\otimes P_C,&q\geq3.
\end{cases}
\]

All groups \(H_k^{N,q}\) with \(k\geq3\) vanish. The formulas remain meaningful without any choice of bases, and are independent of the particular primitive root of the given order. For example, the degree-two Betti numbers exhibit three genuinely different stages:
\[
\dim H_2^{N,1}=(a-1)(b-1)(c-1),\quad
\dim H_2^{N,2}=(ac-1)(b-1),\quad
\dim H_2^{N,q}=ac(b-1)\ (3\leq q<N).
\]
The second and third expressions apply only when their Mayer indices are admissible. In the ordinary case \((N,q)=(2,1)\), degree two is the sole positive-degree homology; it carries the genuine three-way tensor product \(U_A\otimes U_B\otimes U_C\). The root-order-three theory already separates this interaction module from two additional pairwise modules in its second-index degree-two group.

## Assumptions and scope

The three vertex levels are nonempty and have sizes at least two. The directed graph is **not** its transitive closure: in particular no arc from \(A\) to \(C\) is present. The coefficient field is \(\mathbb C\), with \(\zeta\) primitive of order \(N\). The boundary on an allowed \(k\)-path is \(d(v_0,\ldots,v_k)=\sum_{j=0}^{k}\zeta^j(v_0,\ldots,\widehat{v_j},\ldots,v_k)\) for \(k\geq1\), with \(d\) zero on vertices. The \(N\)-chain groups are the intersections of all prescribed boundary-invariant allowed path spaces, and \(H_k^{N,q}=\ker(d^q:\Omega_k\to\Omega_{k-q})/\operatorname{im}(d^{N-q}:\Omega_{k+N-q}\to\Omega_k)\). This is **unreduced** Mayer path homology; no augmented degree-minus-one chain is used.

## Proof

**1. Identify every invariant chain group.** The only allowed positive-length paths are the arcs from \(A\) to \(B\) or \(B\) to \(C\), and the two-step paths from \(A\) through \(B\) to \(C\). Every deleted middle vertex of such a two-step path would require a forbidden arc from \(A\) to \(C\). On a linear combination of two-step paths, these nonallowed faces cancel exactly when, for every fixed pair of endpoints, the coefficients of all middle vertices sum to zero. With \(\varepsilon_X:P_X\to\mathbb C\) the augmentation, this gives
\[
\Omega_0=P_A\oplus P_B\oplus P_C,\qquad
\Omega_1=(P_A\otimes P_B)\oplus(P_B\otimes P_C),\qquad
\Omega_2=P_A\otimes U_B\otimes P_C,\qquad
\Omega_k=0\ (k\geq3).
\]
These are the invariant groups for **every** root order; they are stable under \(G\), and the differential preserves them. In degree two the boundary-squared condition is automatic because its target consists of allowed vertices. In degree three there are no allowed paths at all.

**2. Compute the actual differentials.** For \(x\in P_A\), \(u\in U_B\), \(y\in P_C\), and arbitrary \(b\in P_B\), the differentials are
\[
\begin{aligned}
d_1(x\otimes b,0)&=(\zeta\varepsilon_B(b)x,\ \varepsilon_A(x)b,\ 0),\\
d_1(0,b\otimes y)&=(0,\ \zeta\varepsilon_C(y)b,\ \varepsilon_B(b)y),\\
d_2(x\otimes u\otimes y)&=(\zeta^2\varepsilon_C(y)x\otimes u,\ \varepsilon_A(x)u\otimes y),\\
d_1d_2(x\otimes u\otimes y)&=(0,\ (\zeta+\zeta^2)\varepsilon_A(x)\varepsilon_C(y)u,\ 0).
\end{aligned}
\]
The factor \(\zeta+\zeta^2\) is zero for \(N=2\) and nonzero for every \(N\geq3\): it would vanish only if \(\zeta=-1\). Thus \(d^N=0\) on this short complex, including the nontrivial \(N=2\) case.

**3. Split the chain representations.** Over \(\mathbb C\), each permutation module splits \(P_X=\mathbf1\oplus U_X\) by taking the normalized all-ones vector. The two summands are preserved by its symmetric group. The explicit maps in Step 2 are injective on the indicated nontrivial direct-sum blocks and zero precisely on the stated kernels, yielding
\[
\begin{aligned}
\ker d_2&\cong U_A\otimes U_B\otimes U_C,\\
\operatorname{im}d_2&\cong U_B\otimes(\mathbf1\oplus U_A\oplus U_C),\\
\ker d_1&\cong U_B\otimes(\mathbf1\oplus U_A\oplus U_C),\\
\operatorname{im}d_1&\cong\mathbf1^{\oplus2}\oplus U_A\oplus U_B\oplus U_C,\\
\operatorname{coker}d_1&\cong\mathbf1.
\end{aligned}
\]
For \(N\geq3\), the composite has image \(U_B\) and kernel \(U_B\otimes(U_A\oplus U_C\oplus U_A\otimes U_C)\). When \(N=2\), the composite vanishes and the two middle representations \(\ker d_1\) and \(\operatorname{im}d_2\) coincide as subspaces, since the differential is a chain complex and these spaces have the same dimension. Finally \(\operatorname{coker}(d_1d_2)\cong\mathbf1^{\oplus3}\oplus U_A\oplus U_C\) when \(N\geq3\).

**4. Evaluate all Mayer indices.** There are only three potentially nonzero degrees. In degree zero, the incoming boundary is \(d_1\), \(d_1d_2\), or zero according as \(N-q=1\), \(2\), or at least \(3\). In degree one, the outgoing \(d^q\) is \(d_1\) for \(q=1\) and zero for \(q\geq2\); the incoming map is \(d_2\) when \(N-q=1\) and zero otherwise. In degree two, the outgoing map is \(d_2\), \(d_1d_2\), or zero for \(q=1,2,\geq3\) respectively; there is no incoming map. Apply the kernels and image decompositions from Step 3. For the degree-one case with \(q\geq2\) and \(N-q=1\), the quotient \(\Omega_1/\operatorname{im}d_2\) decomposes as \(\mathbf1^{\oplus2}\oplus U_A\oplus U_B\oplus U_C\). Every displayed isomorphism is \(G\)-equivariant. This proves all assertions without relying on computations at finitely many parameters.

## Verification

The standalone `verify.py` enumerates vertices, arcs, and allowed two-step paths directly for eight tuples of level sizes, including nonconstant and degenerate width-one test cases. It builds the forbidden-chord matrix, constructs its full kernel using independent square-difference columns, and computes the three boundary ranks exactly in the finite field of \(2521\) elements. It tests every Mayer index for each primitive order \(2\) through \(10\) and also verifies representation characters against exact chain-level involutions for three further choices of level sizes and their eight coordinate-swap combinations. Execute `python3 verify.py`; the expected output is stored in `verify_output.txt`. The modular calculations corroborate the proposed identities, including the subtle distinction between a nonzero squared boundary at order \(N\geq3\) and the zero squared boundary at order two. They do not prove the infinite theorem; that is supplied by the preceding representation-theoretic argument.

## Relationship to prior work

Karaguler and Wei introduced the Mayer path differential and the invariant-path construction in 2026. Their full-text analysis classifies local low-dimensional path generators and gives individual four-vertex motif calculations, but it does not give the full three-level, all-order, equivariant homology formulas above. An existing calculation of complete **transitively** layered digraphs includes the additional arrows from the first to the third level. That changes both the allowed chain groups and the boundary: for example, its cubic-root degree-zero first-index rank is two, while here that rank is \(a+c+1\). Neither statement implies the other by a homotopy equivalence or a mere parameter specialization. A calculation for parallel two-edge paths is the special boundary case with one source and one sink; the present theorem requires all three layer widths at least two and includes a nonzero three-way integral-degree analogue in ordinary path homology. The new contribution is the full representation decomposition and all higher-root transitions for the nontransitively oriented complete feedforward family. An unindexed equivalent derivation in general \(N\)-complex literature remains possible.

## Limitations

The result concerns **complex** coefficients, nonregular unreduced Mayer path homology, complete consecutive interlevel adjacency, and three layers. It makes no assertion about integral Mayer models, transitive closures, missing arcs within consecutive levels, additional layers, or persistence as arcs are added. Even though finite-field experiments were used to test the formulas, no finite experiment is treated as an infinite-parameter proof. The scientific comparison does not establish absolute novelty against all unpublished work.

## References

1. D. Karaguler and G.-W. Wei, *Mayer Path Homology*, arXiv:2605.16525, originally public 2026-05-15, https://arxiv.org/abs/2605.16525 (definitions, low-dimensional invariant chains, motif calculations).
2. A. Grigor'yan, Y. Lin, Y. Muranov, and S.-T. Yau, *Homologies of path complexes and digraphs*, arXiv:1207.2834, https://arxiv.org/abs/1207.2834 (ordinary directed path homology background).
3. *Augmentation-block characters of Mayer path homology on layered digraphs*, public mathematical research record b242671c032d, 2026 (the transitively complete, distinct graph family).
