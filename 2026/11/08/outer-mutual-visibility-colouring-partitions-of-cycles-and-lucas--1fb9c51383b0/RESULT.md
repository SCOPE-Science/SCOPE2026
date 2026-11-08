# Outer mutual-visibility colouring partitions of cycles and Lucas enumeration

## Finding

Let \(n\ge4\) be an integer, and let \(C_n\) be the labelled simple cycle with vertices \(0,\ldots,n-1\). A colour class is *outer mutually visible* if for every selected vertex \(x\) and every vertex \(y\), at least one shortest \(x,y\)-path has no internal vertex of the class. Let \(\Pi_n(z)=\sum_k p_{n,k}z^k\), where \(p_{n,k}\) counts unordered partitions of \(V(C_n)\) into exactly \(k\) nonempty outer mutually visible classes.

Define the auxiliary graph \(\Gamma_n\) on these vertices by joining precisely the pairs \(\{x,y\}\) whose shortest cyclic distance is

\[
\begin{cases}
(n-1)/2,& n\text{ odd},\\
n/2-1\text{ or }n/2,&n\text{ even}.
\end{cases}
\]

Every outer mutually visible class in \(C_n\) is a singleton or an edge of \(\Gamma_n\). Thus outer mutually visible partitions are in canonical bijection with matchings of \(\Gamma_n\), and
\[
\Pi_n(z)=\sum_{j=0}^{\lfloor n/2\rfloor}m_j(\Gamma_n)z^{n-j},
\]
where \(m_j\) counts matchings with \(j\) edges. This determines the complete colour-class distribution as follows.

For odd \(n\ge5\), \(\Gamma_n\) is a simple cycle and
\[
\Pi_n(z)=\sum_{j=0}^{(n-1)/2}\frac{n}{n-j}\binom{n-j}{j}z^{n-j}.
\]

For even \(n=2m\ge4\), define the explicit three-by-three polynomial matrix
\[
B(t)=\begin{pmatrix}
1+t&2t&t^2\\
1&t&0\\
1&0&0
\end{pmatrix}.
\]
Then
\[
\Pi_{2m}(z)=\sum_{j=0}^{m}[t^j]\bigl(\operatorname{tr}(B(t)^m)-t^m\bigr)z^{2m-j}.
\]
In particular, the smallest number of outer mutually visible classes is \(\lceil n/2\rceil\). For odd \(n\ge5\) there are exactly \(n\) minimum partitions. For even \(n=2m\ge4\), the number is the Lucas number \(L_m\), specified by \(L_0=2\), \(L_1=1\), and \(L_m=L_{m-1}+L_{m-2}\).

The polynomial counting all assignments using up to \(q\) named colours, allowing unused names, is
\[
X_n(q)=\sum_{j=0}^{\lfloor n/2\rfloor}m_j(\Gamma_n)(q)_{n-j},
\]
where \((q)_h=q(q-1)\cdots(q-h+1)\). For the exceptional triangle \(C_3\), every class is outer mutually visible and \(\Pi_3(z)=z+3z^2+z^3\), \(X_3(q)=q^3\).

## Assumptions and scope

Graphs are finite, simple and labelled. A partition is unordered, classes are nonempty, and the visibility path must be geodesic in the original cycle. No properness restriction is imposed on adjacent vertices carrying the same colour. The definition of named colours counts each distinct map, including those with unused names. The result holds for all integers \(n\ge3\); the formulas based on matchings concern \(n\ge4\).

## Proof

**Pair lemma.** Write \(n=2m+1\), \(m\ge2\), and let two vertices have cyclic distance \(d\le m\). If \(d<m\), choose the target one step beyond the second vertex along the shorter arc. Its distance from the first is \(d+1\le m\), so its unique shortest path passes internally through the second selected vertex. This violates outer visibility. If \(d=m\), the selected vertices are maximally separated: from either selected endpoint, no shortest path to any other vertex needs to traverse the other selected vertex internally. Hence precisely distance \(m\) is allowed. For even \(n=2m\), \(m\ge2\), the same one-step argument excludes \(d\le m-2\). For \(d=m-1\) the only potential target reached through the other selected vertex is its next vertex, which is antipodal to the first and has an alternate geodesic avoiding the selected vertex; any further target has a shorter path in the opposite direction. Distance \(m\) is also allowed. This proves the pair criterion.

**No larger classes.** Outer visibility is hereditary under passing to subsets. Any three-element outer-visible class would induce a triangle in \(\Gamma_n\). For odd \(n\ge5\), \(\Gamma_n\) is a simple cycle: its permitted differences are \(\pm m\) modulo \(2m+1\), and \(\gcd(m,2m+1)=1\). Hence it is triangle-free. For even \(n=2m\ge8\), permitted differences are \(\pm(m-1)\) and \(m\) modulo \(2m\). The sum of three such differences cannot be zero modulo \(2m\): with at least one \(m\)-difference this follows by checking the possible sums \(m\), \(m\pm2(m-1)\), or \(\pm(m-1)\); with none it follows from \(\gcd(2m,m-1)\in\{1,2\}\) and \(m\ge4\). Therefore there are no triangles. At \(n=4\), every triple is equivalent under dihedral symmetry to \(\{0,1,2\}\), but both shortest paths from \(1\) to \(3\) have selected internal vertices. At \(n=6\), the only triangles of \(\Gamma_6\) are \(\{0,2,4\}\) and \(\{1,3,5\}\); in either case the two geodesics from a selected vertex to its antipode each contain another selected vertex. Thus no three-element class works for any \(n\ge4\), and hereditary exclusion rules out larger classes.

**Matching bijection.** Assign one matching edge to every two-vertex class, and leave the unmatched vertices as singleton classes. Distinct two-vertex classes are disjoint, so this is a matching; conversely every matching gives exactly one partition into permitted classes. A matching of \(j\) edges produces exactly \(n-j\) classes. Assigning distinct colour names to the \(n-j\) classes gives \((q)_{n-j}\) maps.

**Odd cycles.** If \(n=2m+1\), the edges of \(\Gamma_n\) join \(x\) with \(x\pm m\); coprimality implies \(\Gamma_n\cong C_n\). Choose \(j\) disjoint edges on a cyclic sequence of \(n\) edges. Mark one selected edge and write the cyclic gaps of unselected edges; each gap is at least one, yielding \(\frac{n}{j}\binom{n-j-1}{j-1}=\frac{n}{n-j}\binom{n-j}{j}\) matchings when \(j\ge1\), and one when \(j=0\).

**Even cycles and the transfer matrix.** Let \(n=2m\). If \(m\) is odd, differences \(\pm(m-1)\) form two length-\(m\) rail cycles joined by the difference-\(m\) rungs, so \(\Gamma_n\) is a circular ladder. If \(m\) is even, \(\pm(m-1)\) form a single length-\(2m\) cycle and the difference-\(m\) edges are its antipodal chords, giving a Möbius ladder. (The \(m=2\) case is the complete graph on four vertices.)

For either ladder, a column has two vertices, a possible rung, and two forward horizontal edges. The incoming/outgoing occupancy states are bitmasks \(a,b\in\{0,1,2,3\}\). Disjointness requires \(a\mathbin{\&}b=0\). Each outgoing edge contributes \(t\), and a rung may independently be chosen only when \(a=b=0\). Thus the exact matching transition matrix is
\[
T(t)=\begin{pmatrix}
1+t&t&t&t^2\\
1&0&t&0\\
1&t&0&0\\
1&0&0&0
\end{pmatrix}.
\]
For odd \(m\), close rails without swapping: the polynomial is \(\operatorname{tr}(T(t)^m)\). For even \(m\), close with a top/bottom swap \(S\), giving \(\operatorname{tr}(T(t)^mS)\). The swap commutes with \(T\). On the symmetric subspace with basis \(e_0,e_1+e_2,e_3\), \(T\) is \(B(t)\); on the antisymmetric line \(e_1-e_2\), \(T\) acts by \(-t\), while \(S\) acts by \(-1\). The antisymmetric contribution equals \(-t^m\) for both parities of \(m\). Hence the matching polynomial is exactly \(\operatorname{tr}(B(t)^m)-t^m\), establishing all coefficients.

**Optimal partitions and Lucas numbers.** The matching number is \(\lfloor n/2\rfloor\): in odd \(n\) the auxiliary cycle has near-perfect matchings; in even \(n\) the antipodal difference-\(m\) edges form a perfect matching. In an odd cycle of length \(n\), the number of maximum matchings is \(n\). To count perfect matchings for even \(n\), set \(U_m(t)=\operatorname{tr}(B(t)^m)\). The characteristic polynomial of \(B\) is \(\lambda^3-(1+2t)\lambda^2-t\lambda+t^3\). Thus \(U_m=(1+2t)U_{m-1}+tU_{m-2}-t^3U_{m-3}\) for \(m\ge3\). As \(\deg U_m\le m\), the leading coefficients \(u_m=[t^m]U_m\) obey \(u_m=2u_{m-1}-u_{m-3}\), with \((u_0,u_1,u_2)=(3,2,4)\). The sequence \(L_m+1\) has those initial values and satisfies the same recurrence. Hence \([t^m](U_m-t^m)=L_m\), as required.

## Verification

The attached standard-library script `verify.py` independently tests shortest paths against the original outer-visibility definition, enumerates all matchings of the auxiliary graphs, reconstructs the four-state matrix from occupancy constraints, and enumerates unrestricted set partitions of small cycles. The independent checks cover all pairs through order eighteen, all larger selected subsets through order twelve, all matching-polynomial coefficients through order eighteen, and all unordered set partitions for orders three through ten. The script does not replace the preceding unrestricted arguments; it checks their finite boundaries and algebraic encoding.

## Relationship to prior work

The 2026 introduction of outer mutual-visibility colouring asks for partitions into outer-visible classes and determines various chromatic numbers on other graph families. Earlier work defines and studies outer mutual-visibility sets and their counting polynomial, and observes that certain antipodal pairs on cycles are maximum outer-visible sets. The present result is a *partition* polynomial, counting matchings of a derived compatibility graph, not the polynomial counting individual outer-visible subsets. It gives the entire number-of-colour-classes distribution and the Lucas number of optimal partitions; it does not claim novelty for ordinary matching enumeration or the Lucas sequence in isolation. These published works and targeted record searches did not identify an equivalent general cycle-colouring partition formula. Historical priority remains provisional.

## Limitations

The graph family is restricted to cycles, with unordered partitions of labelled vertices. The result does not enumerate dihedral orbit classes and does not concern the dual or total colour-class variants. It uses the standard shortest-path (geodesic) definition. Searches cannot establish absolute novelty; independent assessment has not been performed.

## References

1. S. Babu, M. Jakovac, D. Kuziak, A. Lakshmanan S., I. G. Yero, *A variety of the mutual-visibility coloring problem for graphs*, arXiv:2609.31427v1 (first submitted 2026-09-25), https://arxiv.org/abs/2609.31427.
2. C. Bujtás, S. Klavžar, J. Tian, *Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets*, Aequationes Mathematicae 99 (2025), 1883–1901, https://doi.org/10.1007/s00010-025-01197-y.
3. S. Cicerone, G. Di Stefano, L. Droždek, J. Hedžet, S. Klavžar, I. G. Yero, *Variety of mutual-visibility problems in graphs*, arXiv:2304.00864 (2023), https://arxiv.org/abs/2304.00864.
