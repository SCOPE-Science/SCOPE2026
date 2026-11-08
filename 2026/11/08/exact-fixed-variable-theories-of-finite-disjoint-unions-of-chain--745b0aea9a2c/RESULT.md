# Exact fixed-variable theories of finite disjoint unions of chains

## Finding

Let \(\mathcal C\) be the class of nonempty finite partially ordered sets whose comparability components are nonempty finite strict linear orders; distinct components are everywhere incomparable. Write \(c_\ell(P)\) for the number of components of order \(\ell\). For every integer \(k\ge2\), in the pure strict-order language with equality and without counting quantifiers,

\[
P\equiv_{\mathrm{FO}^{k}}Q\quad\Longleftrightarrow\quad \forall\ell\ge1:\;\min(c_\ell(P),k)=\min(c_\ell(Q),k).
\]

Quantifier rank is unrestricted. Each class has the unique smallest representative containing exactly \(\min(c_\ell(P),k)\) chains of each length. Relative to \(\mathcal C\), the least number of variables distinguishing an individual poset \(P\) from every nonisomorphic member is \(1+\max_{\ell}c_\ell(P)\). Its finite-theory spectrum, indexed by the order of the smallest representative, has generating series

\[
1+\sum_{n\ge1}a_k(n)x^n=\prod_{\ell\ge1}\sum_{j=0}^{k}x^{j\ell}=\prod_{\substack{r\ge1\\(k+1)\nmid r}}(1-x^r)^{-1}.
\]

Thus \(a_k(n)\) is the number of ordinary integer partitions of \(n\) with no part divisible by \(k+1\). All nonempty members of \(\mathcal C\) are equivalent in the one-variable fragment; the variable-width hierarchy is strict at each transition within \(\mathcal C\).

## Assumptions and scope

A comparability component is a connected component of the undirected graph whose edges link distinct comparable elements. The signature contains one irreflexive, transitive binary relation \(<\) and equality, but no successor, predicates, endpoints, constants, component symbols, or counting quantifiers. The posets are nonempty; components may be singletons. Equivalence is agreement on *all* counting-free \(\mathrm{FO}^{k}\) sentences, not agreement only through a bounded quantifier rank. Statements about the least defining width are *relative to this family*, not among arbitrary finite posets.

## Proof

**One chain length is visible using two variable names.** For each nonnegative integer \(j\), define two formulas with one free variable \(z\) and at most two reusable variable names. Take \(D_0(z)=U_0(z)=\top\), and recursively set

\[
D_{j+1}(z)=\exists w\,(w<z\land D_j(w)),\qquad U_{j+1}(z)=\exists w\,(z<w\land U_j(w)).
\]

The bound name \(w\) and free name \(z\) alternate on expansion. In a chain of order \(\ell\), an element of zero-based rank \(i\) satisfies \(D_j\) exactly when \(j\le i\) and satisfies \(U_j\) exactly when \(j\le\ell-1-i\). The formulas cannot leave its comparability component, since any strict predecessor or successor belongs to the same chain. Consequently the following one-free-variable formula uses just two reusable names and is true exactly on elements belonging to chains of order \(\ell\):

\[
L_\ell(z)=\bigvee_{i=0}^{\ell-1}\left(D_i(z)\land\neg D_{i+1}(z)\land U_{\ell-1-i}(z)\land\neg U_{\ell-i}(z)\right).
\]

**Necessity.** For each \(1\le j\le k\), take \(j\) distinct variables \(z_1,\dots,z_j\), require \(L_\ell(z_i)\) for each, and require that all distinct selected elements be incomparable. The resulting sentence uses at most \(k\) distinct variable names: local auxiliary variable names in each \(L_\ell\) are bound only within their conjunct and may shadow another outer variable without changing its value outside the conjunct. This sentence holds precisely when \(c_\ell(P)\ge j\). Thus disagreement on any multiplicity after truncation at \(k\) is detected.

**Sufficiency.** Suppose all truncated multiplicities coincide. In the ordinary, non-counting, unlimited-round \(k\)-pebble game, Duplicator maintains an injection from currently occupied chains of one structure into occupied chains of the other, pairing chains of the same *exact* length, and maps each pebbled element to the element with the same rank in the paired chain. This maintains equality and strict comparison on all pebbled elements. If Spoiler moves a pebble to a chain still occupied by another pebble, its counterpart and the rank are forced and available. Otherwise, after the moving pebble is lifted, at most \(k-1\) distinct chains have pebbles. The matching chain length \(\ell\) is available: either both structures have fewer than \(k\) chains of that length and their counts are equal, or both have at least \(k\), so at least one unused counterpart exists. Match the moved element by rank. The invariant persists indefinitely, hence every finite-round pebble game is won by Duplicator and all \(\mathrm{FO}^{k}\) sentences agree.

**Minimum representatives and width.** Each chain count may be reduced to its truncation without changing the theory; reducing further loses an \(\mathrm{FO}^{k}\)-detectable threshold. The multiset of chain orders uniquely identifies a finite disjoint union of chains up to isomorphism. If \(m=\max_\ell c_\ell(P)\), the formula classifies \(P\) uniquely within \(\mathcal C\) at width \(m+1\); at width \(m\), increasing one count that equals \(m\) leaves the theory unchanged. For \(k\ge2\), a union of \(k\) singleton chains and one of \(k+1\) are \(\mathrm{FO}^{k}\)-equivalent but not \(\mathrm{FO}^{k+1}\)-equivalent. The one-variable case sees no nontrivial atomic order relation (irreflexivity ensures \(z<z\) is always false) and cannot distinguish any nonempty structures; it differs from width two on one versus two singleton chains.

**Exact spectrum.** An equivalence class is specified by independent multiplicities \(0,1,\dots,k\) for every length \(\ell\), all but finitely many zero, excluding the empty choice. The order of its minimum representative is their weighted sum. This gives the first Euler product. Use \(1+x^\ell+\cdots+x^{k\ell}=(1-x^{(k+1)\ell})/(1-x^\ell)\) and cancel factors to obtain the product over positive integers not divisible by \(k+1\). The coefficient interpretation follows.

## Verification

The included checker `verification/fo_k_poset_refinement.py` performs counting-free \(k\)-tuple color refinement on complete finite samples of isomorphism types (all integer partitions up to order \(8\) for width \(2\), order \(7\) for width \(3\), and order \(6\) for width \(4\)), and independently compares its theory partition to the claimed invariant. It makes \(2145+946+406=3497\) unordered structure-pair comparisons with zero discrepancies. The independent enumerator `verification/partition_spectrum.py` compares three partition characterizations for widths \(2,3,4,5\) and total orders through \(13\), with no discrepancies. Text files in the same directory contain exact deterministic outputs. These experiments are finite corroboration, not proofs of unrestricted quantifier-depth claims.

## Relationship to prior work

Grohe and Schweikardt prove foundational variable-fragment results for *single* finite linear orders, including length detection with two variable names. Their studied structures are totally ordered, so they do not compare unbounded multisets of disjoint chains. General pebble-game and transitive-relation methods are relevant; the present result gives a specialized complete invariant, exact multiplicity threshold, and restricted-partition theory spectrum for a natural family of posets. The partition product is a standard Euler/Glaisher identity, not claimed as a new partition theorem; its precise identification with this logical spectrum is the contribution. We do not claim that an exhaustive mathematical-priority search has been completed.

## Limitations

The classification does not apply automatically to arbitrary forests of posets, chains related by additional cross-comparabilities, richer signatures, or counting logic. The two-variable formulas may have arbitrarily large quantifier depth and size. The defining-width claim is relative to \(\mathcal C\). No independent mathematical validation has been performed. A stronger general disjoint-union/composition theorem could subsume this specialized invariant, and historical priority is provisional.

## References

1. M. Grohe and N. Schweikardt, *The Succinctness of First-Order Logic on Linear Orders*, Logical Methods in Computer Science 1 (2005), arXiv:cs/0502047, doi:10.2168/LMCS-1(1:6)2005 (public preprint 2005-02-09).
2. M. Szwast and L. Tendera, *FO² with One Transitive Relation Is Decidable*, STACS 2013, doi:10.4230/LIPIcs.STACS.2013.317 (used only for historical comparison of transitive-relation methods, not for its subsequently corrected decidability assertion).
3. Standard finite-variable pebble-game characterization of counting-free first-order equivalence and the classical Euler product/Glaisher partition identity.
