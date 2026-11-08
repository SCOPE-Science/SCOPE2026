# Four-modal observational profiles of finite intuitionistic chains

## Finding

Let \(C_n=\{0,1,\ldots,n-1\}\) have its usual order, where \(n\geq1\). For every binary relation \(R\subseteq C_n\times C_n\), interpret the four intuitionistic modal operators of Balbiani and Gencer (Přenosil possibility, Fischer–Servi necessity, Wijesekera possibility, and its dual necessity) on the lattice of upsets of \(C_n\). Two relations are **observationally equivalent** when the four unary operations are identical on all upsets; equivalently, every formula in the corresponding intuitionistic language has the same truth set for every upset valuation, with worlds held fixed.

For each row \(R[i]=\{j:iRj\}\), put \(a_i=\min R[i]\) and \(b_i=\max R[i]\) when the row is nonempty, with \(a_i=n\) and \(b_i=-1\) when the row is empty. Define four profiles at each world \(s\):

\[
F_s=\max_{i\leq s} b_i,\qquad H_s=\min_{i\geq s} b_i,\qquad I_s=\max_{i\leq s}a_i,\qquad G_s=\min_{i\geq s}a_i.
\]

**Profile theorem.** Two arbitrary relations on \(C_n\) are observationally equivalent if and only if all four profiles \((F,H,I,G)\) agree pointwise. Every relation is observationally equivalent to one with at most \(2n\) edges, and this uniform edge bound is attained for every \(n\geq2\). The map from relations to observable four-modal algebras is injective exactly when \(n\leq2\). For every \(n\geq4\), at least one algebra has \(9^{n-2}2^{n^2-4n+2}\) distinct inducing relations; this lower bound is exact for \(n=4,5\).

The following exact finite census counts the distinct four-modal algebra expansions of the **fixed, labelled** chain (not merely frame validities). The largest fibre is the greatest number of relations yielding one such expansion.

| Worlds \(n\) | Relations | Observable expansions | Largest fibre | Expansions with largest fibre |
|---:|---:|---:|---:|---:|
| \(1\) | \(2\) | \(2\) | \(1\) | \(2\) |
| \(2\) | \(16\) | \(16\) | \(1\) | \(16\) |
| \(3\) | \(512\) | \(279\) | \(8\) | \(5\) |
| \(4\) | \(65{,}536\) | \(7{,}171\) | \(324\) | \(1\) |
| \(5\) | \(33{,}554{,}432\) | \(235{,}152\) | \(93{,}312\) | \(1\) |

Thus three worlds are the sharp point at which the joint semantics of all four connectives ceases to reconstruct accessibility. For five worlds, a single observable algebra can be induced by \(93{,}312\) different relations.

## Assumptions and scope

A relation \(R\) is **arbitrary**: it is not required to be reflexive, serial, transitive, functional, or confluent. The chain order is fixed and every propositional variable is interpreted by an upset. Every upset has the form \(U_k=\{k,k+1,\ldots,n-1\}\), for \(0\leq k\leq n\), where \(U_n=\varnothing\).

For any upset \(U\), write \(\mathsf P U\) for Přenosil possibility, \(\mathsf B U\) for Fischer–Servi necessity, \(\mathsf W U\) for Wijesekera possibility, and \(\mathsf D U\) for dual necessity. Their world conditions are, respectively,

\[
\begin{aligned}
s\in\mathsf P U &\Longleftrightarrow \exists i\leq s\ \exists j\in R[i]:j\in U,\\
s\in\mathsf B U &\Longleftrightarrow \forall i\geq s\ \forall j\in R[i]:j\in U,\\
s\in\mathsf W U &\Longleftrightarrow \forall i\geq s\ \exists j\in R[i]:j\in U,\\
s\in\mathsf D U &\Longleftrightarrow \exists i\leq s\ \forall j\in R[i]:j\in U.
\end{aligned}
\]

Empty rows satisfy universal conditions and fail existential conditions. Formula equivalence is evaluated under the same upset valuation on the same labelled world set, **not** by comparing only sets of globally valid formulas or by arbitrary bisimulations.

## Proof

**Step 1: threshold evaluation.** For every \(0\leq k\leq n\), an inhabited row \(R[i]\) meets \(U_k\) exactly when \(b_i\geq k\), and the inclusion \(R[i]\subseteq U_k\) holds exactly when \(a_i\geq k\). The chosen empty-row conventions make both equivalences hold also for empty rows. Substitution into the four semantic clauses yields

\[
\begin{aligned}
s\in\mathsf P U_k&\Longleftrightarrow F_s\geq k,\\
s\in\mathsf B U_k&\Longleftrightarrow G_s\geq k,\\
s\in\mathsf W U_k&\Longleftrightarrow H_s\geq k,\\
s\in\mathsf D U_k&\Longleftrightarrow I_s\geq k.
\end{aligned}
\]

**Step 2: if and only if.** Identical profiles immediately give identical modal operations on every \(U_k\), hence on every upset. Conversely, the truth values of an operator on all \(U_k\) reconstruct the relevant integer profile by the preceding threshold equivalences: \(F_s,H_s\in\{-1,\ldots,n-1\}\) and \(I_s,G_s\in\{0,\ldots,n\}\) are all uniquely determined by which thresholds hold. Thus equality of all four modal operations forces equality of profiles. Since intuitionistic conjunction, disjunction, implication and coimplication depend only on the order and input upsets, induction on formulas proves the asserted equivalence with equality of all formula denotations. Applying each unary operator to a propositional variable proves the converse for formula denotations.

**Step 3: sparse representatives.** Replace every inhabited row by the set of its one or two endpoints, leaving empty rows empty. Its minima and maxima, hence its four profiles, are unchanged. Therefore no more than \(2n\) edges are needed. Sharpness for \(n\geq2\) is witnessed by the relation having \(R[i]=\{0,n-1\}\) for every \(i\). Its profile \(I_s=0\) for all \(s\) forces any observationally equivalent relation to have \(a_i=0\) for every row (because every term of each prefix maximum is nonnegative). Its profile \(H_s=n-1\) for all \(s\) forces \(b_i=n-1\) for every row. Thus every representative contains both endpoints in every row and has at least \(2n\) edges.

**Step 4: sharp reconstruction threshold.** For \(n=1\), the two possible relations have distinct profiles. For \(n=2\), the four profiles explicitly recover the row extrema: \(a_0=I_0\), \(a_1=G_1\), \(b_0=F_0\) and \(b_1=H_1\). Because a subset of a two-element chain is uniquely determined by emptiness and these extrema, every relation is recovered. For every \(n\geq3\), relations that differ only by the presence of the interior target \(1\) in the row \(R[0]\), whose other targets are \(0\) and \(n-1\), have identical row extrema and hence identical four profiles. They are distinct, so reconstruction fails.

**Step 5: a uniform large-fibre family.** For \(n\geq4\), fix the first row extrema at \(a_0=1\), \(b_0=n-1\) and the last row extrema at \(a_{n-1}=0\), \(b_{n-1}=n-2\). Allow each intermediate row to have any \(a_i\in\{0,1\}\) and any \(b_i\in\{n-2,n-1\}\), with arbitrary interior target choices. Every such relation has \(F_s=n-1\), \(I_s=1\), \(H_s=n-2\), and \(G_s=0\) for all \(s\). The first and last rows each have \(2^{n-3}\) choices, and an intermediate row has exactly \(2^{n-3}+2^{n-2}+2^{n-4}+2^{n-3}=9\cdot2^{n-4}\) possible actual target sets. The resulting single observational fibre therefore has cardinality \(2^{2n-6}(9\cdot2^{n-4})^{n-2}=9^{n-2}2^{n^2-4n+2}\). This provides the asserted lower bound independently of the finite computations.

**Step 6: exact census.** A row has either the empty type \((a,b)=(n,-1)\), of multiplicity one, or endpoints \(0\leq a\leq b<n\). For \(a=b\) there is exactly one row with those endpoints; for \(a<b\), its endpoints must occur and each of the \(b-a-1\) interior targets may occur independently, giving multiplicity \(2^{b-a-1}\). Therefore the Cartesian product of these row-type choices, weighted by the product of their multiplicities, partitions all \(2^{n^2}\) relations without omission or duplication. The profile theorem identifies precisely which choices belong to the same observational class. The included `checks/profile_census.cpp` enumerates these choices for each \(1\leq n\leq5\), groups them by all four profiles, and sums exact integer weights to obtain the table. This is a genuinely exhaustive finite calculation, **not** a sampling argument. The independently implemented `checks/direct_semantics.py` evaluates the four original semantic clauses on every relation and upset for \(1\leq n\leq4\), reproducing all overlapping counts, fibre maxima, and maximizing-class counts. The weighted checker also verifies that the sum of multiplicities is exactly \(2^{n^2}\) in every case.

## Verification

Compile and run `checks/profile_census.cpp` with a C++17 compiler, for example `g++ -std=c++17 -O2 -Wall -Wextra checks/profile_census.cpp -o profile_census && ./profile_census`. It prints, in order, the number of worlds, the number of distinct profiles, the total represented relations, the largest fibre, and the number of fibres attaining the maximum:

```text
1 2 2 1 2
2 16 16 1 16
3 279 512 8 5
4 7171 65536 324 1
5 235152 33554432 93312 1
```

Run `python3 checks/direct_semantics.py` to independently enumerate all \(2^{n^2}\) relations for \(1\leq n\leq4\). It gives the matching values in those four rows. The general profile, reconstruction, edge-bound and large-fibre assertions are proved algebraically in Steps 1–5 and are not inferred from finite experiments. The numerical statements for \(n\leq5\) depend on the complete finite enumeration in Step 6.

## Relationship to prior work

Balbiani and Gencer (2026) introduce the four semantics and study their eliminability, frame correspondence, axiomatization, and decidability. Their semantic clauses are used verbatim above. Přenosil (2023) gives a more general framework of compatible positive and negative modalities on distributive lattices and describes a canonical intersection of relation condensations; this is an important broader source for the **idea of quotienting relations by observable operators**, not evidence that that idea is new here. The present contribution is the explicit chainwise four-profile criterion, the sharp reconstruction/sparsification thresholds, and especially the full weighted enumeration and extremal fibre sizes through five worlds, as well as a uniform large-fibre construction. Related published chain-frame censuses count relations satisfying confluence constraints rather than equivalence classes of **all** relations under these four operators.

## Limitations

The counting table stops at five worlds. The profile theorem and sharp reconstruction and sparsification bounds hold for all finite chain lengths, but no general closed formula for the number of observational classes or the largest fibre is claimed. This classification uses all four modalities simultaneously and valuations into all upsets of a chain; it does not determine the number of formula meanings for a fixed finite set of variables, nor compare merely globally valid formulas. The full historical-priority landscape of related distributive modal algebras and digital relation convexity is not completely indexed; in particular, the general canonical-condensation literature is close and could contain implicit variants of the observational criterion. The primary 2026 paper's later sections were not all retrievable for a line-by-line check; no statement that those unread sections lack an equivalent census is made.

## References

1. P. Balbiani and Ç. Gencer, *Four intuitionistic modal connectives*, first public arXiv version 5 June 2026, arXiv:2606.07348v1, https://arxiv.org/abs/2606.07348 . Semantic clauses in Section 3.4, especially the four modal operators.
2. A. Přenosil, *Compatibility between modal operators in distributive modal logic*, 16 November 2023, arXiv:2311.10017, https://arxiv.org/abs/2311.10017 . Especially Section 2, Definition 2.2 and the general canonical relation/condensation framework.
3. The published research record *Maxima normal form and exact census for chain birelational relations*, publicly searchable at https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-maxima-normal-form-and-exact-census-for-chain-birelational-relat--f1e0f9b64170 . This enumerates constrained relations rather than four-operator observational classes.
4. The published research record *Endpoint normal form and exact census for finite-chain KI frames*, publicly searchable at https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-endpoint-normal-form-and-exact-census-for-finite-chain-ki-frames--df6301f11b97 . Its confluence hypotheses differ from the arbitrary-relational domain here.
