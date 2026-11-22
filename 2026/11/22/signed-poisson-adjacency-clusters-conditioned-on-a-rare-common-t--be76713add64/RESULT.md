# Signed-Poisson adjacency clusters conditioned on a rare common triplet

## Finding
Let \(\pi_n\) be a uniformly random permutation of \(\{1,\ldots,n\}\), with \(n\ge3\). Let \(C_n\) count indices \(i\in\{1,\ldots,n-2\}\) for which the values \(i,i+1,i+2\) occupy three consecutive positions (in any order). Write \(E_n=\{C_n\ge1\}\). Let \(P_n\) and \(N_n\) count adjacent consecutive-value pairs occurring, respectively, in increasing and decreasing order in the permutation:

\[
P_n=\sum_{j=1}^{n-1}\mathbf{1}\{\pi_n^{-1}(j+1)=\pi_n^{-1}(j)+1\},\qquad
N_n=\sum_{j=1}^{n-1}\mathbf{1}\{\pi_n^{-1}(j+1)=\pi_n^{-1}(j)-1\}.
\]

Then, as \(n\to\infty\),

\[
\mathbb P(E_n)=\frac6n+O(n^{-2}),\qquad
(P_n,N_n)\mid E_n\ \xrightarrow{d}\ (Z_++U_+,Z_-+U_-),
\]

where \(Z_+,Z_-\) are independent \(\operatorname{Poisson}(1)\) random variables, independent of the discrete vector \(U=(U_+,U_-)\) whose law is

| \(U\) | Probability |
|---|---:|
| \((2,0)\) | \(1/6\) |
| \((0,2)\) | \(1/6\) |
| \((1,0)\) | \(1/3\) |
| \((0,1)\) | \(1/3\) |

Consequently the *total* number of common adjacencies, \(A_n=P_n+N_n\), obeys

\[
A_n\mid E_n\ \xrightarrow{d}\ Z+W,
\qquad Z\sim\operatorname{Poisson}(2),\quad
\mathbb P(W=1)=\tfrac23,\quad \mathbb P(W=2)=\tfrac13,
\]

with \(Z\) and \(W\) independent. Thus the classical unconditional \(\operatorname{Poisson}(2)\) null law cannot be reused unchanged after conditioning on the observed presence of a common three-marker block. For each fixed \(k\ge1\), the limiting conditional probability of exactly \(k\) adjacencies is

\[
e^{-2}\left[\frac23\frac{2^{k-1}}{(k-1)!}+\frac13\mathbf{1}_{\{k\ge2\}}\frac{2^{k-2}}{(k-2)!}\right],
\]

where the second summand is taken as zero for \(k=1\).

## Assumptions and scope
Only the uniform distribution on linear permutations of distinct, unsigned labels is assumed. The reference ordering is \(1,\ldots,n\); equivalently, this compares two independent uniformly permuted orders after relabelling one as the identity. Triplets are *unordered sets of three successive labels* but must form a consecutive positional block. Positive and negative adjacency counts distinguish the direction of the resulting neighbouring consecutive-value pair. The asymptotic limit is for \(n\to\infty\) with the triplet size fixed at three. No signed-gene, circular-genome, or multi-chromosome model is asserted.

## Proof
**1. Rarity and uniqueness of a triplet.** For \(1\le i\le n-2\), let \(T_i\) be the event that \(i,i+1,i+2\) form one consecutive block. Contracting that block gives \(6(n-2)!\) permutations, so

\[
\mathbb P(T_i)=\frac{6}{n(n-1)},\qquad
\mathbb E C_n=\frac{6(n-2)}{n(n-1)}.
\]

For \(n\ge6\) and \(i<j\), direct contraction of the union of two required blocks gives

\[
\mathbb P(T_i\cap T_j)=
\begin{cases}
4/(n)_3,&j-i=1,\\
8/(n)_4,&j-i=2,\\
36/(n)_4,&j-i\ge3,
\end{cases}
\]

where \((n)_r=n(n-1)\cdots(n-r+1)\). In the first case the overlapping triple windows share two labels and are realized by four linear orders of their union; the second case has eight admissible orders of five labels; the last case has two disjoint internally ordered blocks, with \(3!\cdot3!\) orders. There are \(O(n)\) pairs in each of the first two cases and \(O(n^2)\) in the third, so

\[
\sum_{i<j}\mathbb P(T_i\cap T_j)=O(n^{-2}).
\]

The union bound and its two-term Bonferroni reverse prove the displayed formula for \(\mathbb P(E_n)\); also \(\mathbb P(C_n\ge2)=O(n^{-2})\). Thus, conditional on \(E_n\), the marked triplet is unique with probability \(1-O(n^{-1})\).

**2. Conditioning on one specified triplet.** Given \(T_i\), the internal order of the three labelled elements is uniformly distributed over its six possibilities and is independent of the uniform order of the \(n-2\) contracted objects. The six internal orders contribute the four displayed values of \(U\): the increasing and decreasing three-runs contribute two adjacencies of one sign each; the other four orders contribute exactly one adjacency, two of each sign.

At most two adjacency events cross the boundary of the three-element block: those for \(i-1,i\) and \(i+2,i+3\), when the labels exist. Their total conditional probability is \(O(n^{-1})\), uniformly in \(i\), because the required outside singleton must neighbour the contracted object in a uniform permutation of \(n-2\) objects. Every other external adjacency concerns two singleton labels outside the contracted block.

**3. Independent Poisson external background.** After deleting the at most four value-pair indices touching the marked triple or its boundary, the remaining desired adjacency pairs are edges of two disjoint paths on \(n-3\) singleton labels. Their number is \(n-O(1)\). For any fixed nonnegative integers \(r,s\), expand the mixed factorial moment of the counts of positive and negative external adjacencies into ordered choices of \(r+s\) distinct requested pair-events. Choices using disjoint sets of labels number \(n^{r+s}+O(n^{r+s-1})\); each has probability exactly \(1/(n-2)_{r+s}\), since each directed pair may be contracted uniquely. The remaining choices number \(O(n^{r+s-1})\), and each is either impossible or has probability at most \(1/(n-2)_{r+s}\), by path contraction. Therefore every mixed factorial moment tends to \(1\), uniformly in \(i\). This identifies the joint limit as two independent \(\operatorname{Poisson}(1)\) variables. Independence of the internal six-way mark is exact under \(T_i\), and boundary contributions vanish in probability.

**4. Transfer from one marked block to existence.** For any bounded test function \(f\), the difference between \(\mathbb E[f(P_n,N_n)\mathbf{1}_{E_n}]\) and \(\sum_i\mathbb E[f(P_n,N_n)\mathbf{1}_{T_i}]\) has magnitude at most \(\|f\|_\infty\sum_{i<j}\mathbb P(T_i\cap T_j)=O(n^{-2})\). Divide by \(\mathbb P(E_n)=6/n+O(n^{-2})\). The uniform-in-\(i\) marked-block limit from Steps 2–3 then yields the claimed conditional joint distribution.

As a finite-size consistency check, if \(b_i=\mathbf{1}_{\{i>1\}}+\mathbf{1}_{\{i+2<n\}}\), the same contraction argument gives the **exact** identity for every \(n\ge3\):

\[
\mathbb E[P_n\mid T_i]=\mathbb E[N_n\mid T_i]
=\frac23+\frac{n-3-b_i}{n-2}+\frac{b_i}{3(n-2)}.
\]

The first term is the internal three-block contribution, the middle term comes from pairs of outside singletons, and the last term comes from admissible boundary adjacencies.

## Verification
Run the standalone file `verify.py` with Python 3 from the same directory as this document. It enumerates all permutations of sizes three through eight (46,230 permutations altogether), independently computes the signed adjacency statistics and all three-block events, checks exact first moments and all fixed-block internal order counts, checks every two-triplet probability for sizes at least six, and confirms the finite conditional signed-mean identity. Its expected final line is `PASS: 46230 exhaustively enumerated permutations; 230 exact assertions`. The finite checks support the combinatorial identities; the all-size asymptotic theorem is proved by the argument above, not by enumeration.

## Relationship to prior work
Corteel, Louchard and Pemantle studied common intervals in a uniform permutation and established the unconditional Poisson limit, the expectation of common three-blocks and higher-order information about their *number*. Xu, Alain and Sankoff studied marginal adjacency counts for random genomes, including unsigned Poisson-mean-two limits. Those statements do not specify the conditional signed adjacency-count law given a rare common three-block. Here the dependence is quantified by a nontrivial four-point orientation mark added to two independent Poisson backgrounds. The earlier marginal laws, expectation calculations and common-three-block enumeration are prior art, not new assertions of this work.

## Limitations
The result is an asymptotic distributional statement and does not give an explicit finite-size total-variation rate for the conditional joint law. The conditioning event has probability asymptotic to \(6/n\); conclusions require a large reference alphabet and are not a model of evolutionary genealogy. The exact formulas above do not imply a novel algorithm for finding common intervals. Historical priority for an equivalent *conditional* marked law, possibly under alternative genomic terminology, is not ruled out by the examined literature; no independent review has been performed.

## References
1. S. Corteel, G. Louchard and R. Pemantle, *Common Intervals in Permutations*, Discrete Mathematics & Theoretical Computer Science **8** (2006), 189–214. https://doi.org/10.46298/dmtcs.362 ; open text: https://dmtcs.episciences.org/en/articles/362/download
2. W. Xu, B. Alain and D. Sankoff, *Poisson adjacency distributions in genome comparison: multichromosomal, circular, signed and unsigned cases*, Bioinformatics **24** (2008), i146–i152. https://doi.org/10.1093/bioinformatics/btn295
3. F. de Montgolfier, M. Raffinot and I. Rusu, *Easy Identification of Generalized Common and Conserved Nested Intervals*, Journal of Computational Biology **21** (2014), 520–533. https://doi.org/10.1089/cmb.2013.0146
