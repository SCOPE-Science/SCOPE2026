# Weighted matching census of square roots of arbitrary idempotent transformations

## Finding
For every nonempty finite set \(X\) and every idempotent \(f\in\mathcal T_X\), the number of solutions \(g^2=f\) depends only on the sizes of the fibers of \(f\) and is given by a weighted sum over matchings of those fibers. The same classification yields a rank-refined exponential generating function for every \(g\in\mathcal T_n\) whose square is idempotent.

Let \(S=f(X)=\{s_1,\ldots,s_r\}\), and write \(a_i=|f^{-1}(s_i)|\). Set
\[
F(a)=\sum_{u=0}^{a-1}\binom{a-1}{u}u^{a-1-u},\qquad
V(a,b)=\sum_{u=0}^{a-1}\sum_{v=0}^{b-1}\binom{a-1}{u}\binom{b-1}{v}v^{a-1-u}u^{b-1-v}.
\]
Then, writing \(\operatorname{Cyc}_2(\pi)\) for the unordered pairs in the two-cycles of the permutation \(\pi\),
\[
N(f):=\#\{g\in\mathcal T_X:g^2=f\}=
\sum_{\substack{\pi\in S_r\\\pi^2=1}}
\prod_{\pi(i)=i}F(a_i)
\prod_{\{i,j\}\in\operatorname{Cyc}_2(\pi)}V(a_i,a_j).
\]
The product over an empty index set equals one.

For \(P_n(u)=\sum_{g\in\mathcal T_n,\ g^4=g^2}u^{|\operatorname{im}g^2|}\), with \(P_0(u)=1\), the companion rank identity is
\[
\sum_{n\ge0}P_n(u)\frac{z^n}{n!}=
\exp\left(uR(z)+\frac{u^2}{2}R(z)^2\right),\quad R(z)=z\exp(ze^z).
\]

## Assumptions and scope
\(\mathcal T_X\) is the monoid of all total self-maps of a **finite labeled set**, with composition \((hg)(x)=h(g(x))\). We assume \(f^2=f\), so every \(s_i\in S\) is fixed by \(f\), and all \(a_i\ge1\). In every power sum, including at zero, \(0^0=1\) means the unique empty assignment. The weighted matching formula holds at every finite size and includes the rank-one constant and full-rank identity boundary cases. The generating series are formal exponential generating functions; no convergence hypothesis is required. For \(n=0\), only the generating-function convention is used.

## Proof
**1. The roots induce an involution of the fixed-point set.** If \(g^2=f\), then \(gf=g^3=fg\). For any \(s\in S\), \(f(s)=s\), hence \(f(g(s))=g(s)\); so \(g(S)\subseteq S\). The restriction \(\pi=g|_S\) satisfies \(\pi^2=\mathrm{id}_S\), and is therefore an involutive permutation. Moreover, for every \(x\in f^{-1}(s_i)\),
\[
f(g(x))=g(f(x))=g(s_i)=s_{\pi(i)},
\]
so \(g\) sends the \(i\)-th fiber into the fiber indexed by \(\pi(i)\). Distinct cycles of \(\pi\) cannot interact.

**2. Fixed fibers.** When \(\pi(i)=i\), the distinguished point \(s_i\) is fixed by \(g\). Let \(A_i\) be the subset of the \(a_i-1\) other points sent directly to \(s_i\), and let \(u=|A_i|\). Every remaining point must map to some member of \(A_i\), because its second iterate must be \(s_i\), and mapping directly to \(s_i\) would put it in \(A_i\). Conversely, every such assignment has second iterate constantly equal to \(s_i\) on this fiber. Hence there are exactly \(\binom{a_i-1}{u}u^{a_i-1-u}\) assignments at fixed \(u\); summation gives \(F(a_i)\).

**3. Exchanged fibers.** When \(\pi(i)=j\) and \(\pi(j)=i\), one has \(g(s_i)=s_j\) and \(g(s_j)=s_i\). Select \(A_i\subseteq f^{-1}(s_i)\setminus\{s_i\}\) of size \(u\) to map directly to \(s_j\), and \(A_j\subseteq f^{-1}(s_j)\setminus\{s_j\}\) of size \(v\) to map directly to \(s_i\). Each other point in the \(i\)-fiber must go to one of the \(v\) points of \(A_j\), while each other point in the \(j\)-fiber must go to one of the \(u\) points of \(A_i\). These conditions are both necessary and sufficient for \(g^2=f\) on the paired fibers. Their product count is \(\binom{a_i-1}{u}\binom{a_j-1}{v}v^{a_i-1-u}u^{a_j-1-v}\), giving \(V(a_i,a_j)\) on summation.

**4. No overcounting and completeness.** Each root \(g\) has the unique restriction \(\pi=g|_S\); the directly-to-root subsets \(A_i\) are uniquely recovered from \(g\); and the images of other points are exactly the assignments counted in steps 2 and 3. Conversely every combination described there defines a total map with square \(f\). Multiplying over independent fixed points and two-cycles and summing over involutions proves the exact fiber formula.

**5. Rank-refined identity.** The condition \(g^4=g^2\) is equivalent to \(g^2\) being idempotent. A finite functional digraph has this property precisely when every component has a directed cycle of length one or two, and each attached in-tree has height at most two, measured from its cycle vertex. A labeled rooted tree of height at most two is a root carrying an unordered set of children, each carrying an unordered set of leaves; its exponential generating function is \(R(z)=z\exp(ze^z)\). A one-cycle component has weight \(uR(z)\), while a two-cycle component has weight \(u^2R(z)^2/2\): each cycle vertex is fixed by \(g^2\), and the divisor two removes interchange of the two roots. Components form an unordered set, so the labeled exponential formula proves the stated identity. This also identifies \(|\operatorname{im}g^2|\) with the number of cycle vertices.

## Verification
The standalone program `verify_roots.py` requires only Python's standard library. It independently enumerates every self-map in \(\mathcal T_n\) for \(1\le n\le7\), computes its square and checks whether that square is idempotent, then groups all roots by that actual square and checks the weighted matching formula against every idempotent. The program separately computes the exact formal-series coefficients from \(R(z)\) by rational series arithmetic, and verifies each rank-weighted total at \(u=1,2,3\) against the exhaustive maps. This confirms totals \(1,4,25,194,1791,19312,237637\) for \(n=1,\ldots,7\) and generates the next formal coefficient \(3280524\) at \(n=8\). These finite tests support but do not replace the proof for all \(n\).

## Relationship to prior work
Kozyra (2018) studies finite functional square roots and explicitly counts the **constant-map** and **identity-map** special cases in Propositions 17 and 14, respectively; those cases are credited and are recovered at \(r=1\) and \(r=n\). The novel assessed statement is the single profile-sensitive formula for *every* idempotent, including all unequal fiber sizes and the \(V(a,b)\) interaction for swapped roots, together with the joint rank generating function for idempotent squares. Kozyra (2021) gives structural existence criteria for square roots on finite functional digraphs, and Bhat–Gopalakrishna (2022), Section 2, emphasizes existence and obstruction for general maps. Neither the accessed relevant text of the 2018 and 2022 works nor the available abstract of the 2021 work supplied this arbitrary-idempotent enumeration. Sarkar–Singh (2023) provides recent context for partition-structured full transformation semigroups, but no square-root formula is asserted there.

## Limitations
The result concerns **only idempotent target maps** \(f\) in a finite *full* transformation monoid. It does not enumerate square roots of arbitrary non-idempotent maps, nor does it resolve global extremal questions about which arbitrary map has most roots. The rank-generating function counts transformations \(g\) with idempotent squares, not the distinct idempotents \(g^2\). The 2021 structural paper was available only as an official abstract in the present comparison, so an unknown earlier specialization remains a priority risk. No independent mathematical validation is claimed.

## References
1. P. M. Kozyra, *On Half Iterates of Functions Defined on Finite Sets*, Computational Methods in Science and Technology 24(3) (2018), 187–209, DOI:10.12921/cmst.2018.0000027, published online 2018-09-30. Propositions 14 and 17.
2. P. M. Kozyra, *The Structure Of Functional Graphs For Functions From A Finite Domain To Itself For Which A Half Iterate Exists*, Theory and Applications of Graphs 8(1) (2021), DOI:10.20429/tag.2021.080108.
3. B. V. Rajarama Bhat and C. Gopalakrishna, *Iterative square roots of functions*, Ergodic Theory and Dynamical Systems 43 (2023), 2201–2227, DOI:10.1017/etds.2022.35, online 2022-05-24.
4. M. Sarkar and S. N. Singh, *Semigroups of transformations whose characters belong to a given semigroup*, arXiv:2310.19414, first submitted 2023-10-30.
