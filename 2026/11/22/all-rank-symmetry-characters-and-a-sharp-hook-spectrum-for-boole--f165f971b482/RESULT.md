# All-rank symmetry characters and a sharp hook spectrum for Boolean filtered order complexes

## Finding
Let \(n\ge3\), let \(P_n\) be the proper Boolean poset of all nonempty, proper subsets of \([n]\), and let \(K_{n,k}\) consist of strict inclusion chains whose largest and smallest subset cardinalities differ by at most \(k\), for \(1\le k\le n-2\). The coordinate-permutation action of \(\mathfrak S_n\) induces a rational representation \(V_{n,k}=\widetilde H_k(K_{n,k};\mathbb Q)\). For a permutation \(g\) having cycles of lengths \(\ell_1,\ldots,\ell_c\), its **complete character** is

\[
\chi_{n,k}(g)=(-1)^k\left(\sum_{d=0}^{k}[t^d]\left\{\prod_{i=1}^{c}(2-t^{\ell_i})-2\prod_{i=1}^{c}(1-t^{\ell_i})\right\}-1\right).
\]

The complete **hook multiplicity spectrum** is especially sparse. For \(1\le r\le n-1\), with \(S^{(n-r,1^r)}\) denoting the irreducible rational hook Specht module,

\[
\boxed{\dim\operatorname{Hom}_{\mathfrak S_n}(S^{(n-r,1^r)},V_{n,k})=
\begin{cases}
n-k-2,&r=k,\\
n-k-1,&r=k+1,\\
0,&\text{otherwise}.
\end{cases}}
\]

The trivial representation has multiplicity zero in every positive stage. In particular, for each interior level \(3\le k\le n-3\) the only hook constituents have leg lengths \(k\) and \(k+1\), with the displayed positive multiplicities; the alternating-sign module first appears at the final level \(k=n-2\), with multiplicity one. The formula for all \(k\) includes lower-level and terminal checks; the newly asserted general classification concerns the interior levels beyond previously studied rank span two.

## Assumptions and scope
The rank span is a *simplexwise* maximum minus minimum cardinality, not a selection of fixed global ranks. All inclusions in the chains are strict, and the empty and full subsets are excluded. We consider reduced simplicial homology with coefficients in \(\mathbb Q\), and the natural, untwisted action by relabeling the \(n\) ground-set elements. The coefficient notation \([t^d]F(t)\) means the coefficient of \(t^d\) in a polynomial \(F\). The formula determines the actual rational character of \(V_{n,k}\), hence its isomorphism class as a rational \(\mathfrak S_n\)-module. It does not produce a preferred integral module decomposition or a basis of homology cycles.

## Proof
**Concentrated homology.** The full Boolean lattice is geometric, so the established filtered-order-complex wedge theorem gives \(K_{n,k}\simeq\bigvee S^k\) for \(0\le k\le n-2\) (Kitajima, Corollary 4.19). Thus \(\widetilde H_i(K_{n,k};\mathbb Q)=0\) for \(i\ne k\). Its rational simplicial Lefschetz number therefore equals \((-1)^k\chi_{n,k}(g)\). We use the wedge theorem as a prior result, not as a new assertion.

**Fixed-simplex calculation.** A permutation fixing an inclusion chain setwise fixes every vertex of that chain individually: distinct elements of a strict chain have different cardinalities. In particular, a fixed simplex has orientation sign \(+1\). Fixed subsets are precisely unions of whole cycles of \(g\). There are \(2^c-2\) fixed vertices. For fixed higher-dimensional chains, let \(J\) be the nonempty subset of cycles added between the initial and final subsets. If their total ground-set length is at most \(k\), and \(|J|=s\), the remaining \(c-s\) cycles may be assigned to the initial or outside subset in \(2^{c-s}-2\) ways. The subtraction removes the empty initial subset and full terminal subset. To make a strict chain of dimension \(q\), the \(s\) added cycles must be distributed surjectively into \(q\) ordered nonempty increments, in \(q!\left\{\begin{smallmatrix}s\\q\end{smallmatrix}\right\}\) ways. The alternating sum over \(q\ge1\) is

\[
\sum_{q=1}^{s}(-1)^q q!\left\{\begin{matrix}s\\q\end{matrix}\right\}=(-1)^s,
\]

by the falling-factorial expansion evaluated at \(-1\). Therefore the reduced fixed-simplex Euler characteristic is

\[
2^c-3+\sum_{\substack{\emptyset\ne J\subseteq\{1,\ldots,c\}\\\sum_{j\in J}\ell_j\le k}}(-1)^{|J|}(2^{c-|J|}-2).
\]

Expanding the two products in the stated character formula gives exactly this sum. The simplicial Hopf trace identity now proves that formula over \(\mathbb Q\). Finite-group rational representations are determined by their characters.

**Hook multiplicities.** Write \(W=\mathbb Q^n/\mathbb Q(1,\ldots,1)\). The standard hook identity gives \(S^{(n-r,1^r)}\cong\bigwedge^r W\). A \(q\)-simplex is an ordered partition of \([n]\) into \(q+2\) nonempty blocks: the initial subset, the \(q\) successive differences, and the complement of the terminal subset. Its stabilizer is the associated Young subgroup \(H=\mathfrak S_{a_0}\times\cdots\times\mathfrak S_{a_{q+1}}\). On restricting \(W\) to \(H\), the fixed trivial summand has dimension \(q+1\), while each internal standard summand of a block has no positive exterior power fixed by that block's full symmetric group. Hence

\[
\dim(\bigwedge^r W)^H=\binom{q+1}{r}.
\]

This is the multiplicity of the hook representation in the permutation module of the orbit of that simplex, by Frobenius reciprocity. The number of \(q\)-simplex orbits is \(N_0=n-1\) for \(q=0\), and for \(q\ge1\),

\[
N_q=\sum_{m=q}^{k}(n-m-1)\binom{m-1}{q-1}.
\]

Indeed, \(m\) is the total size of the nonempty interior blocks, the two endpoint blocks admit \(n-m-1\) positive ordered size splits, and the internal blocks admit \(\binom{m-1}{q-1}\) positive compositions. The augmented degree-\(-1\) chain module is trivial and contains no nontrivial hook. Since homology occurs only in degree \(k\), taking the alternating sum of the multiplicities in the chain modules yields, for \(r\ge1\),

\[
\dim\operatorname{Hom}_{\mathfrak S_n}(S^{(n-r,1^r)},V_{n,k})
=(-1)^k\sum_{q=0}^{k}(-1)^q\binom{q+1}{r}N_q.
\]

To evaluate it, use the finite binomial identity

\[
\sum_{q=1}^{m}(-1)^q\binom{q+1}{r}\binom{m-1}{q-1}
=(-1)^m[u^r]\,u^{m-1}(1+u)^2.
\]

It follows by extracting \([u^r]\) from \(-(1+u)^2(1-(1+u))^{m-1}\). This vanishes unless \(m\in\{r-1,r,r+1\}\), with respective weights \(1,2,1\) before the factor \((-1)^m\). The endpoint contribution for \(q=0\) is \((n-1)\) when \(r=1\) and zero otherwise. Direct substitution gives \(n-k-1\) when \(r=k+1\), \(n-k-2\) when \(r=k\), and zero in all other cases, including the boundary cases \(r=1\) and \(k=n-2\). This proves the hook-spectrum formula.

**Trivial constituent.** A strict inclusion chain, up to coordinate permutations, is determined by its sequence of distinct cardinalities. Because these cardinalities are distinct, the action has no inversions of simplex vertices. Thus the orbit space is the simplicial complex on ranks \(1,\ldots,n-1\) whose faces have rank diameter at most \(k\). For \(k\ge1\), the leftmost rank vertex is dominated by its immediate successor; deleting it and repeating gives a simplicial collapse to one point. Consequently the quotient has zero reduced rational homology. Transfer for a finite simplicial group action without inversions identifies this with the invariant part of the original reduced rational homology. Therefore \(V_{n,k}^{\mathfrak S_n}=0\).

## Verification
The complete standalone script `verify.py` implements the cycle polynomial and hook-character formulas independently of chain enumeration, computes rational inner products over permutation cycle types exactly, and enumerates fixed chains directly in small cases. In one replay it checked \(240\) hook inner products for \(3\le n\le10\), and \(104\) independent cycle-type/level combinations for \(3\le n\le6\), involving a cumulative \(11{,}570\) fixed simplices. It verified all predicted hook multiplicities, vanishing trivial multiplicities, identity traces and the exact count of fixed chains. Run `python3 verify.py` from the same directory. Finite checks corroborate the combinatorial equalities; the preceding proof covers every permitted \(n,k\).

For instance, at \(n=8,k=3\), the top homology has dimension \(699\). Its third-hook leg representation has multiplicity \(3\), its fourth-hook leg representation has multiplicity \(4\), and every other hook constituent is absent. This does not mean the entire \(699\)-dimensional representation is a sum of hooks.

## Relationship to prior work
Kitajima (2026), especially Corollary 4.19, proves concentration of homology in one degree for these rank-span filtered complexes and computes sample Betti numbers. That theorem is an essential previously established input, but it does not specify the full coordinate-permutation characters or the hook spectrum. An earlier public rank-span-two calculation identifies the rational symmetric-group character at **only** \(k=2\); our general character specializes to it, while the new claimed range is the infinite collection of higher interior rank spans \(3\le k\le n-3\). A separate published computation determines nonequivariant integral ranks and barcodes for every \(k\) but explicitly does not determine the symmetric-group homology representation. Hersh and Sundaram (2026) study globally fixed rank-selected posets and their Specht-type bases. The moving rank-span union defining \(K_{n,k}\) is not a single global rank selection, and their stated theorems do not specify the character or the two-adjacent-hooks property here. These implications and distinctions were checked at the statement level; an unindexed equivalent equivariant treatment remains possible.

## Limitations
The theorem gives rational characters and hook multiplicities, not a canonical integral representation or full Specht-irreducible multiplicity table. Although the full character mathematically determines that table, no closed formula for each arbitrary nonhook partition is asserted. It uses the prior wedge theorem and the standard identification of hook Specht modules with exterior powers of the augmentation representation. Neither an equivariant sphere-wedge decomposition nor an integral equivariant persistence splitting is proved. The rank-span-zero stage and the known rank-span-two instance are not presented as independently novel. The supporting finite checker is not a proof of the infinite-family result, and no independent mathematical audit has been performed.

## References
1. Yoh Kitajima, *Filtered order complexes and magnitude homology of finite graded posets*, arXiv:2606.15241, first posted June 13, 2026, https://arxiv.org/abs/2606.15241, especially Corollary 4.19 and Example 4.21.
2. Patricia Hersh and Sheila Sundaram, *Stability and ribbon bases for the rank-selected homology of geometric lattices*, arXiv:2604.06479, first posted April 7, 2026, https://arxiv.org/abs/2604.06479, especially Section 4.
3. *Symmetric-group characters and contractible quotients of rank-span-two Boolean complexes*, published result of October 11, 2026; its complete degree-two character and quotient statement were compared.
4. *Complete integral persistence of rank-span filtered proper Boolean lattices*, published result of October 25, 2026; its complete nonequivariant barcode and scope were compared.
5. Bruce E. Sagan, *The Symmetric Group: Representations, Combinatorial Algorithms, and Symmetric Functions*, Springer, 2nd edition, 2001, for standard symmetric-group character and hook-module facts.
