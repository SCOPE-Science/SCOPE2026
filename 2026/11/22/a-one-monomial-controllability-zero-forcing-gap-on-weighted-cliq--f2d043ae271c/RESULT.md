# A one-monomial controllability–zero-forcing gap on weighted clique barbells

## Finding

Let \(p,q\ge3\) be integers. Join a distinguished gateway of the complete graph \(K_p\) to a distinguished gateway of \(K_q\) by one edge. Give all edges inside the first clique conductance \(a>0\), all edges inside the second conductance \(b>0\), and the bridge conductance \(t>0\). Denote the weighted graph Laplacian by \(L\). For a vertex set \(S\), apply independent coordinate inputs to the system \(\dot x=-Lx+B_Su\), where \(B_S\) contains the standard basis vectors indexed by \(S\). Let \(\mathcal C(z)=\sum_{S:\,(-L,B_S)\text{ controllable}}z^{|S|}\).

**Theorem.** A set \(S\) is controllable if and only if it omits at most one *nongateway* vertex from each clique and, in the resonant case \(pa=qb\), does not simultaneously omit both gateways and exactly one nongateway vertex on each side. Equivalently,

\[
\boxed{\mathcal C(z)=z^{p+q-4}(p-1+z)(q-1+z)(1+z)^2-\mathbf 1_{\{pa=qb\}}(p-1)(q-1)z^{p+q-4}.}
\]

The minimum number of independently driven vertices is \(p+q-4\) when \(pa\ne qb\), attained at exactly \((p-1)(q-1)\) sets, and \(p+q-3\) when \(pa=qb\), attained at exactly \(2pq-p-q\) sets. Every statement is independent of the positive bridge conductance \(t\).

The graph's already-known ordinary zero-forcing polynomial is

\[
\mathcal Z(z)=z^{p+q-3}\big[z^3+(p+q)z^2+(pq+p+q-2)z+(2pq-p-q)\big].
\]

Thus the additional fixed-Laplacian result is the exact identity

\[
\boxed{\mathcal C(z)-\mathcal Z(z)=\mathbf 1_{\{pa\ne qb\}}(p-1)(q-1)z^{p+q-4}.}
\]

In particular, ordinary zero forcing and fixed-weight Laplacian controllability agree on **every vertex subset** exactly at the spectral resonance \(pa=qb\). Away from resonance, the only extra controllable sets are the \((p-1)(q-1)\) non-zero-forcing sets consisting of all but one nongateway vertex in each clique, with neither gateway controlled.

## Assumptions and scope

This is an exact algebraic controllability theorem for the symmetric, continuous-time, linear Laplacian dynamics with one independent unrestricted scalar input per chosen vertex. All \(p,q\ge3\) and all positive real \(a,b,t\) are covered, including unequal clique orders and coincident or differing internal conductance values. The result concerns exact rank, not control energy, numerical conditioning, arbitrary nonuniform weights inside the cliques, or time-varying controls restricted in amplitude.

The two cliques have labelled vertices. Write \(U\) and \(V\) for their bridge gateways, and \(A\) and \(B\) for their respective nongateway sets of sizes \(p-1\) and \(q-1\). For any initial actuator set \(S\subseteq A\cup B\cup\{U,V\}\), the input matrix \(B_S\) is the matrix of selected coordinate unit vectors. Positive edge weights are conductances, so each undirected edge \(ij\) of weight \(w\) contributes \(w(e_i-e_j)(e_i-e_j)^{\mathsf T}\) to \(L\).

## Proof

**1. Orthogonal invariant decomposition.** Let \(E_A\) be the vectors supported on \(A\), whose coordinates sum to zero, and similarly \(E_B\). Their dimensions are \(p-2\) and \(q-2\); they are Laplacian eigenspaces with eigenvalues \(pa\) and \(qb\), respectively. Their orthogonal complement \(W\) consists of vectors constant separately on \(A\) and \(B\), with arbitrary gateway coordinates.

In coordinates \((u,U,V,v)\), where \(u\) is the common left nongateway coordinate and \(v\) the common right nongateway coordinate, \(L|_W\) is represented by

\[
Q=\begin{pmatrix}
a&-a&0&0\\
-(p-1)a&(p-1)a+t&-t&0\\
0&-t&(q-1)b+t&-(q-1)b\\
0&0&-b&b
\end{pmatrix}.
\]

The basis is not orthonormal, but scaling coordinates by \((\sqrt{p-1},1,1,\sqrt{q-1})\) makes \(Q\) a real symmetric irreducible tridiagonal matrix. Therefore its four eigenvalues are simple. Its characteristic polynomial is

\[
F(\lambda)=\lambda\big[\lambda^3-(pa+qb+2t)\lambda^2
 +(abpq+t(a(p+1)+b(q+1)))\lambda-abt(p+q)\big].
\]

In particular,

\[
F(pa)=-a^2pt(p-1)(pa-qb),\qquad
F(qb)=b^2qt(q-1)(pa-qb).
\]

Since \(a,b,t>0\) and \(p,q\ge3\), the quotient spectrum intersects either nongateway difference eigenvalue precisely when \(pa=qb\). In that case both difference eigenvalues are the same and exactly one quotient eigenvector joins their eigenspace, making its dimension \(p+q-3\). Otherwise all eigenspaces are the two difference spaces \(E_A,E_B\) and four distinct simple quotient modes.

Every quotient eigenvector has nonzero nongateway value \(u\) **and** nonzero nongateway value \(v\). Indeed, if \(u=0\), the first quotient equation gives \(U=0\), the second then gives \(V=0\), and the last two equations force \(v=0\) (including the special case where the eigenvalue equals \(b\)); contradiction. The right-to-left argument is identical. Hence selecting at least one nongateway vertex on each side detects all quotient modes that have not collided with the difference spaces.

**2. The nonresonant case.** For a symmetric matrix, the Popov–Belevitch–Hautus criterion says that \((-L,B_S)\) is controllable precisely when restriction to \(S\) is injective on every eigenspace. If two nongateway vertices on the left are omitted, a nonzero difference vector supported on that pair belongs to \(E_A\) and vanishes on \(S\). The same argument holds on the right. Conversely, restriction of \(E_A\) to any \(p-2\) selected left nongateway coordinates is injective, because an additional zero-sum coordinate cannot be supported solely on one unselected nongateway vertex. The analogous statement holds for \(E_B\). With \(p,q\ge3\), at least one nongateway vertex per side is selected, so all simple quotient eigenvectors are detected. If \(pa\ne qb\), these checks exhaust the eigenspaces. This proves the nonresonant condition.

**3. The resonance and its compact eigenvector.** Suppose \(pa=qb=:r\). The quotient eigenvector at \(r\) has equal gateway values: the gateway equations, after using the nongateway equations, reduce to \(t(U-V)=0\). Moreover, if a quotient eigenvector at \(r\) has \(U=0\), then it is zero; the gateway value is a nonzero multiple of the quotient component. The full eigenspace at \(r\) is \(E_A\oplus E_B\oplus\operatorname{span}\{w\}\), where \(w\) is this quotient eigenvector.

If exactly one nongateway vertex is omitted from each clique and both gateways are omitted, define \(h\) to be \(-1\) at the two omitted nongateway vertices, \(+1\) at both gateways, and zero elsewhere. Directly summing weighted neighbor differences gives \(Lh=rh\): all selected nongateway coordinates cancel, both gateways receive \(pa=qb=r\), and the two omitted vertices receive \(-r\). Thus this actuator set is not controllable. If a gateway is instead controlled, any vector in the eigenspace at \(r\) vanishing on \(S\) must have zero quotient component; injectivity on \(E_A\) and \(E_B\) then forces it to vanish. If no gateway is controlled but every nongateway vertex in at least one clique is controlled, its average quotient coordinate is zero, forcing the common gateway value and quotient component to vanish; injectivity again applies. This proves that the displayed exceptional pattern is the **only** additional obstruction.

**4. Enumeration and zero forcing.** The allowed selections of nongateway vertices in the two cliques have generating factors \(z^{p-2}(p-1+z)\) and \(z^{q-2}(q-1+z)\). The gateways give \((1+z)^2\). At resonance, delete the \((p-1)(q-1)\) sets with exactly one omitted nongateway on each side and neither gateway selected; the polynomial for \(\mathcal C\) follows. Its first coefficient gives the stated minimum and number of minimizers in each regime.

Independently, ordinary graph zero forcing requires at most one omitted nongateway vertex in each clique: two omitted nongateway twins cannot be distinguished by a forcing step. If both gateways and one nongateway per clique are white, every initially blue nongateway has at least two white neighbors and forcing stalls. In every other case satisfying the local requirement, a blue gateway or a completely blue nongateway clique forces the remaining vertices successively across the bridge. Hence zero forcing has exactly the resonant selection criterion, yielding the stated \(\mathcal Z\) (also previously recorded in the literature). Subtraction proves the one-monomial identity.

## Verification

The accompanying `symbolic_certificate.py` verifies the four-by-four characteristic polynomial, both crucial resonance factorizations, and the exact generating-polynomial identity symbolically. `verify.py` independently enumerates vertex-control subsets for eleven small weighted networks, with \(3\le p,q\le5\), several positive integer edge weights, both sides of the resonance and the exact resonant surface. It computes Krylov ranks over the prime field \(\mathbb F_{1000003}\); all **3136** subset comparisons agree with the structural theorem. Nonzero modular rank certifies nonzero rational rank at those integer examples, while the all-real-parameter proof above, not the finite tests, proves the theorem. Run with `python symbolic_certificate.py` (SymPy required) and `python verify.py` (Python standard library only).

## Relationship to prior work

The exact-controllability framework of Yuan et al. (2013) supplies the multiplicity/PBH paradigm for fixed network matrices, but does not classify all dedicated actuator subsets for these weighted clique barbells. Monshizadeh, Zhang and Camlibel (2014) prove that zero forcing characterizes controllability across a whole qualitative matrix family, a stronger robustness requirement than the particular fixed Laplacian here. The published zero-forcing polynomial for bridge barbells is **prior work**, not claimed as a new formula; the contribution here is the parameter-dependent fixed-Laplacian polynomial and its exact one-monomial difference from that known polynomial. Related indexed work on two equally sized cliques joined by \(k\ge2\) matching edges has a different bridge topology and no asserted coverage of the present \(k=1\), separately weighted pair. Dai's 2022 full-text work gives leader-selection methods for general graphs and explicit treatments of other families, not this all-parameter census.

## Limitations

This is a mathematical rank statement, not a quantitative bound on the smallest controllability-Gramian eigenvalue. Although controllability changes discontinuously at \(pa=qb\), near-resonant control can be extremely ill-conditioned. The result does not treat multiple bridges, independently weighted intracluster edges, finite control-energy budgets, or disturbed observations. Priority relative to unindexed or inaccessible literature still requires human examination, especially full underlying text for the exact barbell zero-forcing record and the partially matched-clique result. No independent mathematical audit has been performed.

## References

1. Z. Yuan, C. Zhao, Z. Di, W.-X. Wang and Y.-C. Lai, “Exact controllability of complex networks,” *Nature Communications* **4**, 2447 (2013), first published 2013-09-12. https://doi.org/10.1038/ncomms3447 ; lawful full text https://pmc.ncbi.nlm.nih.gov/articles/PMC3945876/ .
2. N. Monshizadeh, S. Zhang and M. K. Camlibel, “Zero forcing sets and controllability of dynamical systems defined on graphs,” first public preprint 2014-03-19, https://arxiv.org/abs/1403.4868 ; *IEEE Transactions on Automatic Control* **59** (2014), 2562–2567.
3. L. Dai, “Minimum leader selection for controllability of undirected graphs with leader–follower framework,” first published 2022-10-29, https://doi.org/10.1049/cth2.12385 .
4. “Zero forcing polynomial of bridge barbells,” mathematical research record, 2026-10-04, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-zero-forcing-polynomial-of-bridge-barbells--5431b532d7f2 . Its recorded formula and zero-forcing minimum are acknowledged prior results.
5. “Exact minimum dedicated leader sets for cliques joined by a partial matching,” mathematical research record, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-minimum-dedicated-leader-sets-for-cliques-joined-by-a-part--7537ea98c09f . Its indexed scope requires \(k\ge2\) matching bridges.
