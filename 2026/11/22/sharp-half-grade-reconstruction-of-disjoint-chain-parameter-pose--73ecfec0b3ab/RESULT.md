# Sharp half-grade reconstruction of disjoint-chain parameter posets from singleton type counts

## Finding
Let \(\mathcal R\) be the countable universal homogeneous strict partial order. Let \(P\) be an individually named induced subposet of \(\mathcal R\), isomorphic to a disjoint union of \(k\ge1\) nonempty chains of lengths \(\ell_1,\ldots,\ell_k\), and put \(n=\sum_i\ell_i\). For each complete nonalgebraic singleton type \(p(x)\) over the named parameters, define its **comparability grade** as the number of parameters comparable with \(x\), and let \(c_j(P)\) count types of grade \(j\). Write \(F_P(z)=\sum_{j=0}^{n}c_j(P)z^j\).

**Exact enumerator.** For \(S_\ell(z)=1+z+\cdots+z^\ell\) and \(M_\ell(z)=\sum_{j=2}^{\ell}(j-1)z^j\), with empty sums zero,
\[
\boxed{F_P(z)=2\prod_{i=1}^{k}S_{\ell_i}(z)-1+\sum_{i=1}^{k}M_{\ell_i}(z).}
\]

**Sharp inverse theorem.** Suppose the total number \(n\ge1\) of individually named parameters is known. The coefficient list
\[
\boxed{c_0(P),c_1(P),\ldots,c_{\lfloor n/2\rfloor}(P)}
\]
uniquely reconstructs the unordered multiset \(\{\ell_1,\ldots,\ell_k\}\), hence \(P\) up to isomorphism. This cutoff cannot be reduced: for every \(n\ge2\) there exist nonisomorphic disjoint unions of nonempty chains on \(n\) vertices whose coefficients agree in all grades strictly below \(\lfloor n/2\rfloor\).

More precisely, for \(n=2r\ge4\), the two profiles \((r-1,r+1)\) and \((r,r)\) agree through grade \(r-1\), while their grade-\(r\) counts differ by \(-(r+1)\), first profile minus second. For \(n=2r+1\ge5\), the same assertion holds for \((1,r-1,r+1)\) and \((1,r,r)\). At \(n=2,3\), constant coefficients alone never reconstruct the chain partition. For \(n=1\), grade zero is sufficient because there is only one profile.

In contrast to reconstruction from the graded counts, even the *total* type count together with \(n\) and \(k\) need not identify a profile: \((1,4,12)\) and \((2,2,13)\) each have \(n=17\), \(k=3\), and \(F_P(1)=331\), but have different graded polynomials.

## Assumptions and scope
The language consists of one strict partial-order relation and equality. All old points are **individually named** and the new variable is required to be distinct from every parameter. Components are pairwise incomparable chains; chains of size zero are excluded. The input size \(n\) is provided to the reconstruction procedure. A type is counted once per distinct labelled one-point extension, not once per automorphism class of the unlabeled parameter poset. Grade \(j\) counts old points strictly below **or** strictly above the new point; incomparable points contribute zero. The count is a first-order complete type count because every finite poset embeds into \(\mathcal R\), every finite one-point extension is realized, and finite partial isomorphisms extend to automorphisms.

## Proof
**1. Types as ideal/filter pairs.** For a new point \(x\notin P\), define \(L=\{a\in P:a<x\}\) and \(U=\{a\in P:x<a\}\). The strict-order axioms are equivalent to three conditions: \(L\) is a down-set, \(U\) is an up-set, and \(a<b\) for every \(a\in L\) and \(b\in U\). These conditions suffice: declaring precisely these old-to-new comparisons makes a strict poset, and the extension property of \(\mathcal R\) realizes it. Its grade is \(|L|+|U|\).

**2. Enumerate pure types.** For \(U=\varnothing\), a down-set of \(P\) independently chooses a prefix of each chain of length between zero and \(\ell_i\). Its grade enumerator is \(\prod_iS_{\ell_i}(z)\). By duality, the same holds for \(L=\varnothing\). The wholly incomparable type \((\varnothing,\varnothing)\) was counted twice and must be subtracted once.

**3. Enumerate mixed types.** If both \(L,U\) are nonempty, the requirement \(L<U\) forces **all** their elements into the same chain: otherwise a member of one shore and a member of the other would be incomparable. On a chain of length \(\ell\), \(L\) is a nonempty initial prefix of length \(a\) and \(U\) is a nonempty final suffix of length \(b\), with \(a+b\le\ell\). At grade \(j=a+b\ge2\), the positive solutions number exactly \(j-1\), provided \(j\le\ell\). Thus the mixed contribution is \(\sum_iM_{\ell_i}(z)\). Combining pure and mixed types proves the exact enumerator. In particular \(c_0=1\) and \(c_1=2k\).

**4. Triangular reconstruction.** Put \(q_j=\#\{i:\ell_i\ge j\}\), so \(q_1=k=c_1/2\), and \(m_s=q_s-q_{s+1}\), the number of chains of length exactly \(s\). Suppose \(j\ge2\) and all \(m_s\) for \(1\le s\le j-2\) are known. Form the explicitly known auxiliary polynomial
\[
B_j(z)=\left(\prod_{s=1}^{j-2}S_s(z)^{m_s}\right)
S_{j-1}(z)^{\,k-\sum_{s=1}^{j-2}m_s}.
\]
For each chain of length at least \(j\), replacing its exact factor by \(S_{j-1}\) deletes exactly one degree-\(j\) monomial, up to terms of degree at least \(j+1\). All other factors have constant term one, so
\[
[z^j]\prod_i S_{\ell_i}(z)=[z^j]B_j(z)+q_j.
\]
The mixed-term coefficient at degree \(j\) is \((j-1)q_j\). Therefore
\[
\boxed{q_j=\frac{c_j-2[z^j]B_j(z)}{j+1}.}
\]
This inductively recovers \(q_2,\ldots,q_r\) from the coefficients through degree \(r=\lfloor n/2\rfloor\), hence every \(m_s\) for \(s<r\). The quotient is an integer since it counts actual chain components.

**5. Recover the remaining long chains.** Let \(t=q_r\) be the number of unrecovered chains, each of length at least \(r\), and let \(N=n-\sum_{s<r}s m_s\) be their total length. For \(r\ge2\), \(n\le2r+1\) implies \(t\le2\). When \(t=0\), the remaining multiset is empty; when \(t=1\), it consists of the single length \(N\). When \(t=2\), necessarily \(2r\le N\le2r+1\), hence the only possible sorted lengths are \((r,r)\) or \((r,r+1)\), determined by \(N\). Thus the entire multiset is recovered. For \(n=2,3\), the coefficient \(c_1=2k\) alone determines the integer partition of \(n\) (and \(c_0=1\)); for \(n=1\) there is exactly one possibility. This proves reconstruction at every positive \(n\).

**6. Sharpness.** For \(n=2r\ge4\), compare \((r-1,r+1)\) and \((r,r)\). They have the same total length and two components, and their counts \(q_j\) coincide for every \(j<r\). The formula in Step 4 (applied degree-by-degree) therefore gives identical coefficients below grade \(r\). At grade \(r\) the first profile has one long chain and the second has two, while multiplicities below length \(r-1\) are identical; their coefficient difference is \((r+1)(1-2)=-(r+1)\). For odd \(n=2r+1\ge5\), adjoining an isolated one-point chain to both profiles preserves that difference and all earlier agreements: its factor \(1+z\) contributes identically to both, and its mixed term vanishes. For \(n=2,3\), the constant grade is always one although there are at least two chain partitions. Hence no lower uniform cutoff works.

**7. Scalar-count contrast.** Evaluating the polynomial at one yields
\[
F_P(1)=2\prod_i(\ell_i+1)-1+\sum_i\binom{\ell_i}{2}.
\]
For \((1,4,12)\) this is \(2(2\cdot5\cdot13)-1+6+66=331\); for \((2,2,13)\) it is \(2(3\cdot3\cdot14)-1+1+1+78=331\). Their grade-two coefficients are respectively \(12\) and \(15\), so the scalar equality is a genuine loss of information.

## Verification
The standalone standard-library program `verify.py` provides two independent exact counting implementations. First it computes the closed polynomial using algebraic convolution. Second it constructs every ternary old-to-new comparison assignment and tests transitivity of the complete enlarged strict relation directly, without using the ideal/filter decomposition. The outputs agree for all 66 nonempty-chain partitions on one through eight named parameters. The program also enumerates all 28,628 integer partitions on one through 30 elements, checks uniqueness and the actual triangular reconstruction for each truncated coefficient list, and verifies a sharp smaller-truncation collision at every size two through 30. It confirms the explicit four-point pair and the 17-point scalar collision. Its captured output `verify_output.txt` ends `VERIFY_OK`. These are reproducibility checks, not substitutes for the all-size combinatorial proof.

## Relationship to prior work
Fraïssé's theory and the standard homogeneous generic-poset construction are background; Hubička's 2010 thesis constructs the generic partial order explicitly. Dolinka and Mašulović (2010, §3.1) use the lower-set/upper-set description of a finite-poset one-point extension, but study extension of homomorphisms and endomorphism monoids, not this weighted counting invariant. Pach, Pinsker, Pluhár, Pongrácz and Szabó (2011) classify reducts of the random poset rather than inverse reconstruction of named-base type counts.

A published finite-parameter type-counting result establishes the same general ideal/filter correspondence and its counting complexity. Another establishes an incomparability-sensitive **ungraded** lower bound, including disjoint unions of at most two chains as equality cases. Related published results enumerate ordered pair types over two chains, exact tuple types over a single chain, and collisions of the **bivariate** profile on arbitrary finite posets. None of their inspected statements supplies either the all-grade disjoint-chain formula together with the triangular inversion or the sharp half-grade recovery cutoff. The contribution claimed here is the **sharp universal truncation threshold for reconstructing every disjoint-chain base**, not the general one-point-extension correspondence, an ungraded type count, or the Fraïssé background.

## Limitations
The reconstruction assumes known base cardinality and parameter posets consisting of disjoint chains. It does not imply that the truncated grade profile determines an arbitrary finite poset or that its cutoff remains sharp when additional statistics are given. The uniqueness proof recovers the **unlabelled chain-size multiset**, not the original names attached to individual vertices. The algorithm is a deterministic exact reconstruction, not a claim about optimal computational bit complexity. Priority remains provisional: unindexed results on weighted ideal/filter enumerators or symmetric-function inversion could contain an equivalent statement. No independent mathematical audit has been conducted.

## References
1. Jan Hubička, *Combinatorial Properties of Finite Models*, arXiv:1009.0566v1, first public version 2010-09-03, Chapter 3, §3.1. https://arxiv.org/abs/1009.0566
2. Igor Dolinka and Dragan Mašulović, *A universality result for endomorphism monoids of some ultrahomogeneous structures*, arXiv:1009.2892v1, first public version 2010-09-15, §3.1. https://arxiv.org/abs/1009.2892
3. Péter Pál Pach, Michael Pinsker, Gabriella Pluhár, András Pongrácz and Csaba Szabó, *Reducts of the random partial order*, arXiv:1111.7109v1, first public version 2011-11-30. https://arxiv.org/abs/1111.7109
4. *Finite-parameter 1-type counting in the random poset is #P-complete*, public research record (2026), underlying ideal/filter description and ungraded counting-complexity comparison.
5. *An incomparability-sensitive lower bound for one-point types of the generic poset*, public research record (2026), ungraded sharp inequality and equality cases.
6. *Order-polynomial spectra of tuple types over chains in the generic partial order*, public research record (2026), all-arity tuple types over one chain.
7. *Exactly 102 rank-three theories of finite direct sums of at most three chains*, public research record (2026), a distinct bounded-quantifier-rank logical classification.
