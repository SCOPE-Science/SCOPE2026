# Geometric fixed-point phase change for transitive coordinate groups on binary-cube Rips complexes

## Finding

For every integer \(n\geq1\), let \(Q_n=\{0,1\}^n\) with Hamming metric and let \(X_n=\operatorname{VR}(Q_n;2)\), where a simplex is a set of binary words of pairwise Hamming distance at most two. Let \(G\leq S_n\) be **any subgroup acting transitively on the \(n\) coordinate positions**, acting on \(Q_n\) by coordinate permutations and on \(|X_n|\) simplicially. Its actual geometric fixed-point space has the following complete PL-homeomorphism classification:

\[
|X_n|^G\cong_{\mathrm{PL}}
\begin{cases}
\Delta^1,&n=1,\\
\Delta^2,&n=2,\\
|C_4|,&n=3,\\
\Delta^1\sqcup\Delta^1,&n\geq4.
\end{cases}
\]

Here \(\Delta^j\) is a closed geometric \(j\)-simplex and \(|C_4|\) is the geometric realization of a four-edge cycle. Thus the reduced integral homology is \(\mathbb Z\) in degree one for \(n=3\), \(\mathbb Z\) in degree zero for \(n\geq4\), and zero otherwise; no torsion occurs. The classification is **independent of which transitive coordinate subgroup is chosen** and concerns geometric fixed points, not merely vertices fixed by all permutations.

## Assumptions and scope

A binary word \(x\) is identified with its support \(\operatorname{supp}(x)\subseteq[n]\). Its Hamming weight is the support size, and the distance between two words is the size of their symmetric difference. The action preserves Hamming weight and scale-two simplices. The group may be cyclic, dihedral, symmetric, alternating, imprimitive, regular, or any other transitive subgroup. No assumption of primitivity, freeness, or double transitivity is used.

Let \(z=0^n\) and \(u=1^n\). For \(n\geq2\), put \(E=\{e_1,\ldots,e_n\}\), the words of weight one, and \(\overline E=\{u-e_1,\ldots,u-e_n\}\), the words of weight \(n-1\). Each of these is one \(G\)-orbit because \(G\) is coordinate-transitive.

## Proof

**1. Geometric orbit-face model.** For any simplicial complex \(K\) whose vertices are permuted by a finite group, a point of \(|K|\) is fixed precisely when its barycentric coefficient function is constant on each vertex orbit. Its positive-coefficient support is then a union of complete orbits, and must span a simplex of \(K\). Define the *orbit-face complex* to have a vertex for each vertex orbit which itself spans a simplex, and a simplex on any collection of orbit vertices when the union of their underlying vertex orbits spans a simplex of \(K\). Sending the orbit vertex to the barycenter of its orbit simplex and extending affinely yields a PL homeomorphism from the orbit-face complex onto \(|K|^G\). This is a homeomorphism on each face, and face intersections are preserved by uniqueness of barycentric coordinates. In particular, including only globally fixed original vertices would generally be incorrect.

**2. A Johnson-clique lemma.** Suppose \(2\leq k\leq n-2\). A family \(\mathcal F\) of distinct \(k\)-subsets with any two members intersecting in \(k-1\) elements is contained either in a star (all members contain one fixed \((k-1)\)-subset) or a top (all members are contained in one fixed \((k+1)\)-subset). To see this, choose distinct \(A=S\cup\{a\}\) and \(B=S\cup\{b\}\) in the family. Every other member adjacent to both either contains \(S\), or has the form \((S\setminus\{s\})\cup\{a,b\}\) for some \(s\in S\). In the latter case, a member \(S\cup\{d\}\) with \(d\notin\{a,b\}\) is not adjacent to that member, so all members lie inside \(S\cup\{a,b\}\). This proves the dichotomy, including the case of only two members.

**3. Only four eligible vertex orbits.** Fix \(2\leq k\leq n-2\). A \(G\)-orbit \(\mathcal O\) of weight-\(k\) words has at least two elements, since a singleton would give a nonempty proper coordinate subset invariant under transitive \(G\). Were \(\mathcal O\) of diameter at most two, its supports would be pairwise adjacent in the Johnson graph and Step 2 would apply. In the star case their common intersection contains a nonempty \((k-1)\)-subset; in the top case their union is a nonempty subset of at most \(k+1<n\) coordinates. But both the intersection and the union of an orbit are \(G\)-invariant, while transitivity permits only the empty set and \([n]\) as invariant subsets. Both cases are impossible. Therefore no middle-weight orbit is admissible.

The constant words \(z,u\) are singleton orbits, and \(E,\overline E\) are the unique weight-one and weight-\((n-1)\) orbits, each of diameter two. For \(n\geq3\), **these are exactly the four admissible orbits**. For \(n=2\), the weight-one and weight-\((n-1)\) orbits coincide, giving three; for \(n=1\), just \(z,u\) remain.

**4. Compute orbit-face incidences.** When \(n\geq4\), the only compatible pairs among \(z,u,E,\overline E\) are \((z,E)\) and \((u,\overline E)\). Their unions have diameter at most two. All other pairs contain words at distance greater than two: \(d(z,u)=n\), \(d(z,\overline e_i)=d(u,e_i)=n-1\), and \(d(e_i,\overline e_i)=n\), where \(\overline e_i=u-e_i\). Thus the orbit-face complex consists of two disjoint edges. In dimension \(n=3\), each constant word is compatible with each of \(E\) and \(\overline E\); the two constants are incompatible with each other and \(E\) is incompatible with \(\overline E\), giving exactly the four-cycle \(K_{2,2}\). For \(n=2\), the diameter of all of \(Q_2\) is two and the three vertex orbits form a filled triangle. For \(n=1\), \(X_1\) itself is one edge. Step 1 identifies the orbit-face complexes PL-homeomorphically with the geometric fixed spaces, completing the proof.

**5. Homology and sharpness.** The explicit complexes are a simplex, a simplex, a circle, and two contractible components, respectively. Their reduced integral homology follows immediately, with no reliance on finite computations or any unproved homotopy assertion. The change from a circle at \(n=3\) to two components at \(n=4\) is sharp.

## Verification

The standalone `verify.py` directly constructs orbits of binary words under generating permutations, filters orbit supports by exact Hamming diameter, constructs their full compatible-face complexes, computes ordinary mod-two Betti numbers by bitwise Gaussian elimination, and compares both face counts and admissible-orbit sizes with the theorem. It tested 32 transitive permutation actions in dimensions one through eight, including cyclic, dihedral, symmetric, alternating, and several imprimitive or regular actions. The recorded output ends with `ALL_VERIFY_OK cases=32`. These are *finite checks only*. The unrestricted integral and PL statements are proved in Steps 1--5.

To reproduce, run `python3 verify.py` from the directory containing the standalone verifier; no third-party modules or external data are needed.

## Relationship to prior work

Adamaszek and Adams established that scale-two hypercube Rips complexes have ordinary homotopy types given by wedges of three-spheres. Bendersky, Elia, and Grbić (first posted 2026-05-01) study their cohomology and connectivity. Galetto, Montaño, and Wellner (first posted 2026-06-18), particularly Theorem 5.4, determine the ambient rational hyperoctahedral homology representations. Those results concern the ambient complex and its homology action, not the **PL-homeomorphism type of the geometric fixed set for every transitive coordinate subgroup**. Character data alone do not determine PL fixed-point topology.

Earlier calculations of geometric fixed spaces for translation subgroups or a single coordinate transposition involve actions that differ essentially from arbitrary *coordinate-transitive* permutation subgroups. The classical Johnson-graph star/top clique lemma is used explicitly as a combinatorial input, not claimed as new. The novelty claimed here is only the uniform four-case geometric classification and its sharp phase change.

## Limitations

The theorem applies to inclusive Hamming scale two and coordinate-transitive permutation subgroups, not arbitrary subgroups of the full signed-permutation/translation automorphism group. It does not classify general scales, orbit-space quotients, equivariant homotopy types, or equivariant attaching maps. The finite verifier is not an exhaustive list of all transitive subgroups in the tested degrees. An independently reviewed proof and exhaustive identification of every unindexed prior formulation remain outside the present result.

## References

- M. Bendersky, S. Elia, J. Grbić, *Cohomological properties of the Vietoris--Rips Complex of a Hypercube Graph*, arXiv:2605.00705 (initial public posting 2026-05-01), https://arxiv.org/abs/2605.00705.
- F. Galetto, J. Montaño, Z. Wellner, *Homology of Vietoris-Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784 (initial public posting 2026-06-18), https://arxiv.org/abs/2606.20784.
- M. Adamaszek, H. Adams, *On Vietoris--Rips complexes of hypercube graphs*, arXiv:2103.01040 (initial public posting 2021-03-01), https://arxiv.org/abs/2103.01040.
- M. Varisco, M. C. B. Zaremsky, *Equivariant Morse theory on Vietoris--Rips complexes and universal spaces for proper actions*, arXiv:1909.04487 (2019), https://arxiv.org/abs/1909.04487. The general equivariant Morse setting is distinct from the explicit finite orbit-face classification here.
