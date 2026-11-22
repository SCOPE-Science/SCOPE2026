# The half-turn Fibonacci character and full symmetry quotient of three-row perfect-matching complexes

## Finding

For every integer \(n\ge2\), let \(G_n=P_3\square P_{2n}\), with three rows and \(2n\) columns, and let \(X_n\) be the simplicial complex on the **edges** of \(G_n\) whose faces are subsets of perfect matchings. Let \(R\) reverse the rows, \(C\) reverse the columns, and \(H=RC\) be the half-turn. These commute and generate \(V_4\).

Write \(F_0=0\), \(F_1=1\), \(F_{k+1}=F_k+F_{k-1}\), and use the backward extension \(F_{-1}=1\). The reduced rational homology of \(X_n\) is supported in degree \(n-1\), of rank \(F_{n-1}\). Combining the half-turn calculation below with previously obtained single-axis traces, the complete character of this degree is \(\big(F_{n-1},r_n,c_n,h_n\big)\), where

\[
r_n=\begin{cases}1,&n\equiv0,5\pmod6,\\0,&n\equiv1,4\pmod6,\\-1,&n\equiv2,3\pmod6,\end{cases}
\]

and, for \(k\ge1\),

\[
\begin{array}{c|cc}
 & n=2k & n=2k+1\\ \hline
c_n & (-1)^{k-1}F_{k-2} & (-1)^kF_k\\
h_n & (-1)^kF_{k+1} & (-1)^{k-1}F_k
\end{array}
\]

The four rational one-dimensional isotypic multiplicities, indexed by row and column signs \(a,b\in\{1,-1\}\), are exactly

\[
m_{a,b}(n)=\frac{F_{n-1}+a r_n+b c_n+ab h_n}{4}.
\]

For the **actual geometric quotient** by the full Klein-four group, not a quotient of chain-group generators,

\[
\widetilde H_j(|X_n|/V_4;\mathbb Q)\cong
\begin{cases}\mathbb Q^{m_{1,1}(n)},&j=n-1,\\0,&j\ne n-1.\end{cases}
\]

The first nonzero reduced rational quotient homology occurs at \(n=4\), when the quotient of the three-by-eight grid complex has exactly one rational third-homology class. The new half-turn trace has unbounded Fibonacci magnitude. The row and column characters are restated as previously known inputs, not as new findings.

## Assumptions and scope

All graphs are ordinary finite Cartesian rectangular grid graphs; no cylindrical or twisted boundary is imposed. Perfect matchings are vertex-covering collections of pairwise disjoint graph edges, and their subsets are faces. Involutions act on edge-vertices of the complex via graph automorphisms. The parameter \(n\) is the half-width, and the theorem covers all integers \(n\ge2\). The published nonequivariant homotopy equivalence \(X_n\simeq\bigvee^{F_{n-1}}S^{n-1}\) is an input [1]. The previous row and column reflection formulas are explicitly credited; the novel calculation is the half-turn trace, followed by the full-group character and quotient computation.

## Proof

**1. Reduced equivariant face formula.** For any involutive simplicial automorphism \(g\) of a finite complex whose vertices are graph edges, its reduced Lefschetz number is

\[
\widetilde L(g)=-\sum_{S\in X,\ gS=S}(-1)^{o_g(S)},
\]

where the sum includes the empty simplex and \(o_g(S)\) is the number of \(g\)-orbits of edge-vertices in \(S\). Indeed, the permutation of a setwise fixed face with \(f\) fixed vertices and \(p\) transposed pairs has sign \((-1)^p\), while its alternating chain coefficient is \((-1)^{f+2p-1}\), giving \((-1)^{f+p-1}\). As the only nonzero reduced homology is in degree \(n-1\), each homology trace equals \((-1)^{n-1}\widetilde L(g)\).

**2. A finite exact matching-extension automaton.** Represent a boundary column by a three-bit mask. At every column of a left-to-right strip, select a matching \(M\), represented by the incoming horizontal-edge mask \(i\), a vertical-edge mask \(v\in\{0,3,6\}\), and an outgoing horizontal-edge mask \(o\), all mutually disjoint. One selected vertical edge corresponds to mask 3 or 6, not two. Independently propagate the **set** \(Q\) of all feasible incoming horizontal-edge masks of a matching \(P\) that covers precisely the vertices not occupied by \(M\). For each \(p\in Q\), choose a disjoint vertical completion mask \(w\in\{0,3,6\}\); the only possible outgoing completion mask is

\[
p'=7\mathbin{\mathrm{xor}}(i\mathbin{\mathrm{or}}v\mathbin{\mathrm{or}}o\mathbin{\mathrm{or}}p\mathbin{\mathrm{or}}w).
\]

The bitwise expression is used only when all occupied masks are pairwise disjoint. The new state is \((o,Q')\) where \(Q'\) collects every feasible \(p'\). The initial state is \((0,\{0\})\). This deterministic subset construction is exact: by induction on columns, it records every possible completing matching and no impossible one. Each selected horizontal or vertical edge contributes sign \(-1\) per orbit of the applicable involution. The included `transfer_check.py` contains the precise elementary transition loops and integer weights.

**3. Column reflection and half-turn.** For either involution, a fixed face is uniquely determined by a matching \(M\) on the left \(n\)-column half and selected central horizontal edges. For column reversal, any subset \(B\subseteq\{0,1,2\}\) of central edges can occur. For the half-turn, \(B\) must be invariant under the row flip \(\rho(0)=2\), \(\rho(1)=1\), i.e. \(B\in\{\varnothing,\{1\},\{0,2\},\{0,1,2\}\). The number of edge orbits in the central subset is respectively \(0,1,1,2\) in the latter case.

Let \(Q\) be the completion masks at the end of the left half, with the selected matching's final outgoing mask zero. A fixed face extends to a perfect matching exactly when there is a completing boundary mask \(T\) containing \(B\), with \(T\in Q\) for column reversal or \(T\in Q\cap\rho(Q)\) for the half-turn. This follows by cutting a perfect matching along the central three edges and reflecting the right half; conversely, the two residual half-matchings glue over precisely the common boundary mask \(T\). In either case \(B\) must avoid already selected boundary vertices of \(M\). These conditions give exact terminal weights \(b_C\) and \(b_H\) for the same 24-state integer transition matrix \(T\).

If \(e\) selects the initial state, write \(z^g_n=eT^{n-1}b_g\). Direct exact evaluation of the displayed finite transition rules gives the four initial values \((z^C_1,z^C_2,z^C_3,z^C_4)=(0,1,1,0)\) and \((z^H_1,z^H_2,z^H_3,z^H_4)=(0,-1,-1,2)\). For each terminal vector, the exact integer scalar identity

\[
z^g_{n+4}+z^g_{n+2}-z^g_n=0
\]

is proved for every \(n\ge1\) as follows. The finite transfer has exactly 24 reachable states and 112 nonzero weighted transitions. The checker verifies \(eT^j(T^4+T^2-I)b_g=0\) for all \(j=0,\ldots,23\), using exact integer arithmetic. By the Cayley–Hamilton theorem applied to this 24-by-24 integer matrix, these 24 equalities imply the same equality for every nonnegative \(j\). Since the homology trace is \((-1)^n z^g_n\), the initial values and recurrence yield the displayed Fibonacci expressions for \(c_n,h_n\), including the boundary case \(k=1\).

**4. Row reversal.** A row-invariant matching cannot contain vertical edges because the two edges of each reflected pair meet at the middle-row vertex. Its horizontal selections are generated by independent middle-row edges and paired top/bottom edges. Accordingly the selected outgoing masks are exactly \(0,2,5,7\), weighted by the number of the two chosen edge-orbits. Propagating all completing matchings by the same three-bit rule yields an eight-state integer transfer \(U\). Its terminal coefficient \(w_n\) is determined by \(eU^{2n}b_R\). Exact verification shows \(w_{n+3}=w_n\) for the first eight half-width indices. Cayley–Hamilton for \(U^2\), an eight-by-eight matrix, proves this period-three identity for all \(n\ge0\). The initial values \(w_0=1,w_1=0,w_2=-1\), together with \(r_n=(-1)^nw_n\), give the stated six-periodic row character.

**5. Complete rational decomposition and quotient.** Since \(V_4\) is abelian of exponent two, its rational irreducibles are exactly the four one-dimensional sign characters. The character idempotent formula therefore gives the multiplicities \(m_{a,b}(n)\). A finite simplicial group action admits an equivariant barycentric subdivision, and rational homology of its geometric quotient equals the invariant rational homology of the original complex, without any freeness assumption. Taking the \((a,b)=(1,1)\) multiplicity proves the geometric-quotient assertion. Evaluation of the formulas for \(n=2,3,4\) gives quotient ranks \(0,0,1\), proving the first-occurrence statement.

## Verification

Run `python3 transfer_check.py` in the folder containing `direct_check.py`, using only Python's standard library. It reconstructs all reachable transfer states and signed transitions, verifies every finite Cayley–Hamilton base equality, checks the Fibonacci and periodic formulas through half-width 40, and checks nonnegative integer character multiplicities. An independently constructed exhaustive face enumeration of all perfect matchings and their subfaces verifies the three homology traces for \(n=2,3,4\) on 495, 12,375 and 309,480 distinct faces, respectively. The finite tests alone do not prove an all-width theorem; the all-width proof is the complete-state recurrence plus Cayley–Hamilton.

## Relationship to prior work

Chandrakar, Chau, Goyal, Karki and Subhash [1], first public 13 November 2026, establish the nonequivariant Fibonacci sphere-wedge homotopy formula, which is credited rather than claimed. Their manuscript defines the same Cartesian grid and perfect-matching complex, and its main theorem and proof contain no coordinate-symmetry character classification. A prior three-by-four reflection calculation [2] gives a boundary case. Earlier separate all-width row and column reflection calculations already establish the respective \(r_n\) and \(c_n\) formulas; neither is claimed as new. Their statements concern only individual involutions and contain no character of their product \(H=RC\). Those two traces and the total Betti number do not determine the \(V_4\)-character: for example at \(n=4\), the prior traces are \(r_4=c_4=0\) and rank is two, consistent with either \(h_4=2\) or \(h_4=-2\). The new independent half-turn trace resolves the missing character, thereby determining all joint isotypic multiplicities and the full-group quotient. The row and column transfers appear in the proof as independent checks, not originality claims. Results on the ordinary **matching complex** [3] concern a strictly larger simplicial complex with a different homology representation; they cannot be substituted for this perfect-matching subcomplex. No inspected primary result, indexed record or recoverable earlier claim determines the half-turn trace on these perfect-matching complexes or implies the full character; unindexed equivalent work remains a risk.

## Limitations

The new contribution is the half-turn character and its genuinely joint symmetry consequences; the result is a rational representation and rational quotient-homology theorem, not an integral representation-lattice or quotient-homotopy classification. The nonequivariant homotopy formula of [1] is an explicit theorem used as an input. The recurrence and comparisons are computationally transparent finite-state proofs but have not received an independent mathematical audit. Unindexed equivalent earlier research is a residual priority risk.

## References

1. H. Chandrakar, T. Chau, S. Goyal, R. Karki and B. Subhash, *Perfect Matching Complexes of \(3\times2n\) Grid Graph*, arXiv:2611.18058v1, 13 November 2026, https://arxiv.org/abs/2611.18058 . See Theorem 3.5 and the graph definition in Section 3.
2. *A five-cycle core and signed reflection homology for the three-by-four perfect-matching complex*, public research record dated 2 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-five-cycle-core-and-signed-reflection-homology-for-the-three-b--521893fb03dc .
3. *Orthogonal-reflection Lefschetz formulas for \(3\times n\) grid matching complexes*, public research record dated 11 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-orthogonal-reflection-lefschetz-formulas-for-3-times-n-grid-matc--c1da8c8f4653 ; and *Half-turn Lefschetz characters and full-symmetry quotients of \(3\times n\) grid matching complexes*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-half-turn-lefschetz-characters-and-full-symmetry-quotients-of-3--e4fab66f9a1a . Both concern ordinary matching complexes, not the perfect-matching subcomplex.
4. Prior single-axis computations for the same perfect-matching complex: *A six-periodic mirror character for three-row perfect-matching complexes* (row reversal) and *Integral column-reflection trace of the three-row grid perfect-matching complex* (column reversal). These previously recorded claims are credited; publicly accessible versions of these exact records were not verified.
