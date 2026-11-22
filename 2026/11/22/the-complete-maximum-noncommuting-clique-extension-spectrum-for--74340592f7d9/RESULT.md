# The complete maximum-noncommuting-clique extension spectrum for binary symplectic groups

## Finding

Let \(G\) be a finite group such that \(G'\cong C_2\) and \(G/Z(G)\cong\mathbb F_2^{2r}\), where \(r\ge1\), and write \(z=|Z(G)|\). For a pairwise noncommuting set \(T\subseteq G\) of size \(t\), let \(E_G(T)\) denote the number of *unordered* maximum-cardinality pairwise noncommuting sets containing \(T\). Define
\[
S_j=2^{j^2}\prod_{i=1}^{j}(2^{2i}-1)=|\operatorname{Sp}_{2j}(2)|,\qquad S_0=1.
\]
For \(0\le t\le2r\), the complete extension law is
\[
E_G(T)=z^{2r+1-t}\begin{cases}
\displaystyle\frac{S_{r-t/2}}{(2r+1-t)!},&t\text{ even},\\[6pt]
\displaystyle\frac{2^{2r-t}S_{(2r-t-1)/2}}{(2r+1-t)!},&t\text{ odd and }\sum_{g\in T}gZ(G)\ne0,\\[6pt]
0,&t\text{ odd and }\sum_{g\in T}gZ(G)=0.
\end{cases}
\]
All sums here are in the elementary abelian group \(G/Z(G)\). Every \((2r+1)\)-set of pairwise noncommuting elements is already maximum and has exactly one completion (itself). No larger pairwise noncommuting set exists.

In particular, the total number of unordered maximum sets is
\[
\boxed{N(G)=z^{2r+1}\frac{2^{r^2}\prod_{i=1}^{r}(2^{2i}-1)}{(2r+1)!}.}
\]
Every even-cardinality pairwise noncommuting set extends; every \((2r-2)\)-set of pairwise noncommuting *central cosets* has a **unique** completion to a \((2r+1)\)-set of such cosets, and each choice of the original group elements admits exactly \(z^3\) maximum-group-set completions. For odd \(t<2r+1\), the sole obstruction is zero quotient sum.

All projected maximum sets form one orbit of \(\operatorname{Sp}_{2r}(2)\), and the stabilizer of any unordered set in this symplectic group is isomorphic to \(S_{2r+1}\). This is an action on the central quotient, not a claim that every symplectic transformation lifts to an automorphism of the original group.

## Assumptions and scope

The group is finite; its derived subgroup is cyclic of order two; its quotient by its center is elementary abelian of dimension \(2r\ge2\). We count subsets, not ordered tuples, and a *maximum* set has the largest possible size, as distinct from merely inclusion-maximal sets. The convention for the symplectic nonorthogonality graph is: two nonzero vectors are adjacent when their alternating pairing equals one. This is the complement of the common polar-graph convention, which uses zero pairing as adjacency.

Because \(G'\) has order two, it is central (conjugation acts through the trivial automorphism group of \(C_2\)). The commutator induces a well-defined alternating bilinear form
\[
b:G/Z(G)\times G/Z(G)\to\mathbb F_2,\qquad [x,y]=c^{b(xZ(G),yZ(G))},
\]
where \(c\) is the nonidentity element of \(G'\). The radical is zero by the definition of \(Z(G)\); thus \(b\) is symplectic. Two group elements fail to commute precisely when their quotient vectors have pairing one. Consequently a pairwise noncommuting set uses at most one element from any given central coset.

## Proof

**1. Rank bound and maximal simplices.** A projected \(t\)-clique \(v_1,\ldots,v_t\) satisfies \(b(v_i,v_j)=1\) for \(i\ne j\). Its Gram matrix over \(\mathbb F_2\) is \(J_t+I_t\), with rank \(t\) when \(t\) is even and \(t-1\) when \(t\) is odd. Hence \(t\le2r+1\). For \(t=2r+1\), the vector sum is orthogonal to every \(v_i\), and the vectors span the whole space because their Gram matrix has rank \(2r\); therefore their sum is zero. Every \(2r\)-clique is a basis, and adjoining the sum of its vectors creates a \((2r+1)\)-clique, since \(2r-1\) is odd. Such a \(2r\)-clique exists: the matrix \(J_{2r}+I_{2r}\) is a nonsingular alternating matrix, isometric to the standard symplectic form. Thus the maximum is precisely \(2r+1\).

**2. Symplectic transitivity and the global count.** Each ordered maximum clique consists of a basis \(v_1,\ldots,v_{2r}\) and its sum, and every such basis has Gram matrix \(J_{2r}+I_{2r}\). Therefore there is a unique symplectic transformation carrying one ordered maximum clique to another. Ordered maximum cliques form a free transitive \(\operatorname{Sp}_{2r}(2)\)-set. Permuting all \(2r+1\) entries of a maximum clique preserves their Gram matrix and the unique sum relation, so each permutation extends uniquely to a symplectic map. The unordered stabilizer is \(S_{2r+1}\). Counting ordered symplectic bases gives \(S_j=(2^{2j}-1)2^{2j-1}S_{j-1}\), starting with \(S_0=1\); multiplying yields the stated product and \(S_r/(2r+1)!\) projected maximum cliques.

**3. Even-size extension formula.** Let \(t\) be even, \(0\le t\le2r\), and let \(W=\langle v_1,\ldots,v_t\rangle\). The Gram matrix is nonsingular, so \(W\) has dimension \(t\) and \(V=W\perp W^\perp\) with \(\dim W^\perp=2r-t\). Set \(s=\sum_{i=1}^t v_i\). For every \(i\), \(b(s,v_i)=t-1=1\) in \(\mathbb F_2\) (when \(t=0\), the statement is vacuous). The vectors pairing to one with *all* \(v_i\) are precisely \(s+w\) for \(w\in W^\perp\). Between these new vectors, the pairing is \(b(w,w')\). Thus if \(t<2r\), a completion to size \(2r+1\) corresponds bijectively to a maximum nonorthogonal clique of size \(2r-t+1\) in \(W^\perp\); the zero vector cannot occur among its members. For \(t=2r\), the sole extra vector is \(s\). Step 2, applied to the complement, gives \(S_{r-t/2}/(2r+1-t)!\) projected completions.

**4. Odd-size extension formula and the obstruction.** Let \(t\) be odd with \(1\le t\le2r-1\). Since the Gram matrix has a one-dimensional kernel generated by the all-ones vector, a linear dependence among \(v_1,\ldots,v_t\) occurs exactly when \(\sum_i v_i=0\). If that sum vanishes, no further common nonorthogonal vector exists: for any candidate \(w\), pairing with the sum would give simultaneously \(0\) and \(t=1\) in \(\mathbb F_2\). Hence no maximum-clique completion exists.

Otherwise the \(t\) vectors are linearly independent. Apply Step 3 to the first \(t-1\) vectors. Their orthogonal complement has dimension \(d=2r-t+1\ge2\). The last fixed vector is \(s+w\) with \(0\ne w\in W^\perp\). Completions correspond to maximum cliques in \(W^\perp\) containing \(w\). Since \(\operatorname{Sp}_{d}(2)\) is transitive on nonzero vectors, every such vector belongs to the same number of maximum cliques. Double-counting their incidences gives
\[
\frac{S_{d/2}}{(d+1)!}\frac{d+1}{2^d-1}
=\frac{2^{d-1}S_{(d-2)/2}}{d!}
=\frac{2^{2r-t}S_{(2r-t-1)/2}}{(2r+1-t)!}.
\]
The middle identity uses the symplectic-group order recurrence proved in Step 2.

**5. Lifts to the group.** Fix a projected maximum clique containing the projected set of \(T\). Its \(2r+1-t\) other central cosets are distinct, and choosing one of their \(z\) elements independently produces one maximum pairwise noncommuting superset of \(T\). Conversely each such superset gives a unique projected clique and unique lifts. Multiplication by \(z^{2r+1-t}\) proves all group formulas, with no extra assumption on the exponent of the group or on its central power structure. Setting \(t=0\) gives the total enumerator. At \(t=2r-2\), the complementary symplectic space is two-dimensional, whose unique projected maximum clique is the set of all three nonzero vectors. This proves the unique projected completion and exactly \(z^3\) group completions.

## Verification

The independent standard-library script `CHECK.py` constructs the binary symplectic adjacency relation directly by bit arithmetic, enumerates every nonorthogonal clique and every maximum clique, and compares the size, even/odd extension laws, zero-sum obstruction, and uniqueness at top even rank. It exhaustively checks symplectic dimensions \(2\), \(4\), \(6\), involving respectively \(8\), \(192\), and \(26896\) clique instances of all sizes, including the empty clique. The projected maximum-clique totals are \(1,6,288\); for extraspecial groups with \(z=2\) the corresponding group totals are \(8,192,36864\). These finite tests check the arithmetic and definitions, not all-dimensional correctness; Steps 1–5 are the proof for every \(r\ge1\).

## Relationship to prior work

Lecomte (2026), Lemma 3.1, proves the maximum size \(2r+1\), spanning property, and vanishing sum for a maximum binary symplectic clique, and the group theorem classifies central-index extremizers by isoclinism. These results provide the motivating objects, but do not enumerate maximum cliques or determine the extension spectrum for every prescribed clique. Liu and Wang (2015) also establish \(2r+1\) as a maximum size in a class of generalized extraspecial groups, without these incidence counts. Chin (2005) studies the *odd-prime* extraspecial setting. Godsil–Royle's symplectic graph construction gives the ambient binary graph, but the complete all-arity extension counts are a separate assertion. An article titled *The number of pairwise noncommuting sets in a finite group* studies families of pairwise noncommuting subsets of fixed size, a different invariant. These comparisons are by mathematical implication and domain, rather than title alone.

## Limitations

The theorem applies only to groups with order-two derived subgroup and elementary abelian central quotient of even rank. It does not classify arbitrary inclusion-maximal noncommuting sets, odd-prime commutator groups, or automorphism orbits of lifts in groups with distinct quadratic power maps. The symplectic orbit is on the *quotient* and need not be induced by automorphisms of \(G\). The displayed counts concern subsets (no ordering and no multiplicity). Finite enumeration through rank three is supportive, not a substitute for the all-rank proof. Historical priority in unindexed literature on binary symplectic graphs and group-theoretic clique designs remains possible.

## References

1. G. Lecomte, *The Exact Central-Index Profile of Groups with Bounded Noncommutativity*, arXiv:2611.00943v1 (public 2026-10-31), especially Theorems 1.1–1.2 and Lemma 3.1. https://arxiv.org/html/2611.00943v1
2. H. Liu and Y. Wang, *On Non-commuting Sets in Certain Finite p-Groups*, Algebra Colloq. 22 (2015), 555–560. https://doi.org/10.1142/S1005386715000474
3. A. Y. M. Chin, *On non-commuting sets in an extraspecial p-group*, J. Group Theory 8 (2005), 189–194. https://doi.org/10.1515/jgth.2005.8.2.189
4. C. Godsil and G. Royle, *Algebraic Graph Theory*, Springer (2001), §§8.11, 10.12.
5. *The number of pairwise noncommuting sets in a finite group*, Bull. Aust. Math. Soc. 112 (2025), 497–504. https://doi.org/10.1017/S0004972724001370
