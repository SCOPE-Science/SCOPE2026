# Rare perfect matchability changes the diameter of random permutation trees

## Finding

Let \(T_n\) be uniform among the \(2^{n-2}\) labelled inversion graphs of permutations of \(\{1,\ldots,n\}\) that are trees, for \(n\ge2\). Let \(P_n\) denote the event that \(T_n\) has a perfect matching, \(L_n\) its number of leaves, and \(\Delta_n\) its graph diameter (number of edges on a longest path). For every integer \(m\ge2\),

\[
\Pr(P_{2m})=2^{1-m},\qquad
L_{2m}\mid P_{2m}\ \overset{d}=\ 2+\operatorname{Bin}(m-2,1/2),
\qquad
\Delta_{2m}\mid P_{2m}\ \overset{d}=\ 2m-1-\operatorname{Bin}(m-2,1/2).
\]

In particular, writing \(\ell\) for any integer between \(2\) and \(2m-1\),

\[
\Pr(P_{2m}\mid L_{2m}=\ell)=
\begin{cases}
\displaystyle \binom{m-2}{\ell-2}/\binom{2m-3}{\ell-2}, &2\le\ell\le m,\\
0,&m<\ell\le2m-1.
\end{cases}
\]

The conditional probability strictly decreases as the leaf count rises from \(2\) to \(m+1\), taking value \(1\) for a path (two leaves) and becoming zero after \(m\) leaves. Exactly \(2\binom{m-2}{\ell-2}\) of the permutation trees on \(2m\) vertices are perfectly matchable and have \(\ell\) leaves. Perfect matchings do not occur at odd tree orders. The two-vertex tree has a perfect matching with probability one.

As \(m\to\infty\),

\[
\frac{\Delta_{2m}}{2m}\ \xrightarrow{\Pr}\ \frac34
\quad\text{under the conditional law given }P_{2m},
\qquad
\frac{\Delta_{2m}}{2m}\ \xrightarrow{\Pr}\ \frac12
\quad\text{unconditionally}.
\]

Moreover, under the conditional law, \((\Delta_{2m}-3m/2)/\sqrt{(m-2)/4}\) converges in law to a standard Gaussian. The perfect-matchability event is exponentially rare but changes the typical diameter at linear order.

## Assumptions and scope

For a permutation \(w=w_1\cdots w_n\), its inversion graph \(G_w\) has vertex set \(\{1,\ldots,n\}\), with an edge \(\{w_i,w_j\}\) precisely when \(i<j\) and \(w_i>w_j\). Each tree permutation has a unique binary insertion word \(b_1\cdots b_{n-2}\), with independent uniform binary letters under the stated uniform-tree law. Start with permutation \((2,1)\). The first insertion \(I_1\) places the new maximum immediately before the last symbol; the second \(I_2\) replaces the old maximum by the new maximum and appends the old maximum. We encode \(I_1\) by \(0\) and \(I_2\) by \(1\).

We use the established caterpillar identities for the number of leaves and diameter; we prove the new matching event characterization and its conditioned consequences below. A perfect matching means a set of vertex-disjoint edges covering every vertex. All probabilities concern this explicitly described uniform family, not a uniformly labelled Cayley tree or a random permutation conditioned only on the number of inversions.

## Proof

**1. A four-state matching recursion.** In a tree permutation of size \(k\ge2\), designate \(A=w_k\), the last symbol, and \(B=k\), the greatest symbol. They are distinct adjacent vertices. For \(a,b\in\{0,1\}\), let \(F_{ab}\) mean there exists a matching covering all vertices outside \(\{A,B\}\) and covering \(A\) exactly if \(a=1\), and \(B\) exactly if \(b=1\). These are existential flags, not counts. For the initial two-vertex edge, the complete set of possible flags is \(S=\{00,11\}\).

Under \(I_1\), a new leaf \(C\) is joined to \(A\), and the new designated pair is \((A,C)\); the old \(B\) must now be covered. Enumerating whether the new leaf edge is selected gives exactly

\[
01\mapsto \{00,11\},\qquad 11\mapsto\{10\},
\]

with flags \(00\) and \(10\) producing nothing. Under \(I_2\), a new leaf \(C\) is attached to \(B\), and the new designated pair is \((C,B)\); now the old \(A\) must be covered. Thus

\[
10\mapsto\{00,11\},\qquad 11\mapsto\{01\},
\]

with flags \(00\) and \(01\) producing nothing. The maps act by union over existing flags. Consequently a complete pair of operations \(I_1I_2\) or \(I_2I_1\) takes \(S\) back to \(S\), whereas either repeated pair takes \(S\) to the empty set. The empty set is absorbing. By induction, at an even order \(2m\), a perfect matching exists *if and only if* the insertion bits satisfy

\[
 b_{2j-1}\ne b_{2j}\qquad(1\le j\le m-1).
\]

Indeed, the graph has a perfect matching exactly when its final flag set contains \(11\), and this happens precisely when all consecutive disjoint bit pairs are complementary. Among the \(2^{2m-2}\) words, \(2^{m-1}\) obey those constraints, proving \(\Pr(P_{2m})=2^{1-m}\). Every tree has at most one perfect matching, since the symmetric difference of two distinct perfect matchings would contain an alternating cycle; uniqueness is not used for the count.

**2. Leaf and diameter distributions.** The binary insertion construction gives, for \(n\ge3\),

\[
L_n=2+\sum_{i=2}^{n-2}{\boldsymbol 1}\{b_i=b_{i-1}\},\qquad \Delta_n=n-L_n+1.
\]

The first identity follows by the leaf-status update at successive insertions; the second follows because every tree in this family is a caterpillar, with every longest path going between its terminal leaves. These identities and the unconditional binomial law are also established in the original construction paper.

Conditioned on \(P_{2m}\), the bits occur in \(m-1\) *independent, uniformly oriented complementary pairs*: each pair is equally likely to be \(01\) or \(10\). All within-pair equalities vanish. The \(m-2\) equalities between neighboring pairs are independent Bernoulli variables with success probability \(1/2\): the orientation of the first pair and the successive orientation-difference bits give a bijective linear transform of the independently fair pair orientations. This proves the conditional leaf binomial law; substitution into the diameter identity proves the conditional diameter law.

**3. Exact leaf-resolved probability.** The adjacent-equality indicators of an unrestricted uniformly fair bit word are independent fair bits, by the same invertible difference transform. Hence \(L_{2m}-2\) is unconditionally \(\operatorname{Bin}(2m-3,1/2)\). The number of eligible words with exactly \(\ell\) leaves equals \(2\binom{m-2}{\ell-2}\), and the number of all words with that leaf count equals \(2\binom{2m-3}{\ell-2}\). Dividing gives the displayed conditional probability. The ratio between successive positive probabilities is \((m-\ell)/(2m-\ell-1)<1\) for \(2\le\ell<m\); the next value at \(\ell=m+1\) is zero. This proves the strict ordering and the cutoff.

**4. Macroscopic geometry.** The conditioned and unconditioned diameter limits are immediate from their respective binomial laws and the weak law of large numbers. The centered, scaled conditional Gaussian limit is the usual binomial central limit theorem; the conditional mean and variance are respectively \(3m/2\) and \((m-2)/4\). No asymptotic assertion is needed to establish the exact finite formulas.

## Verification

Run `python verify.py` using only the Python standard library. The independent verifier constructs every insertion word through order fourteen, creates each permutation and its inversion graph, computes perfect matching existence using a vertex-subset recursion (not the four-state proof), and independently enumerates degrees and leaves. It checks the matching-word characterization, uniqueness of each permutation, tree edge counts, leaf identity and all exact leaf-resolved counts. The run completed successfully for all \(8191\) words, with \(41{,}003\) elementary assertions accounted for in its loop. Exhaustive checks stop at size fourteen: the proof, not the finite computation, establishes the all-order claims.

## Relationship to prior work

Acan and Hitczenko introduced the exact binary insertion correspondence for tree permutations and established their caterpillar shape, leaf count and diameter laws. The two insertion maps and those existing results are used explicitly above. Their main results do not state a perfect-matching event, its probability, or the associated conditional leaf and diameter distributions. Janson later studied pattern-occurrence limit laws in uniform tree and forest permutations using related random encodings; those pattern-count results do not supply this rare global perfect-matchability conditioning. General graph-theoretic results about matchings in trees apply to fixed trees but do not, without an additional specialization and probability calculation, produce these distributions.

Related published work was compared by objects, assumptions and implied statements, including the distinction between arbitrary bipartite permutation graphs and this very restricted random tree-permutation law. No inspected theorem covered the complete displayed matching-conditioned distribution and diameter shift. This is a best-knowledge originality assessment, not a claim of exhaustive historical uniqueness.

## Limitations

The independent bit-word distribution is essential; the formula does not apply to uniformly sampled Cayley trees, general random permutation graphs or differently weighted tree permutations. There is no claim about maximum matchings when a perfect matching fails, or about rare joint regimes outside the fixed even-order family. The finite verifier is not an infinite certificate. A very general earlier enumeration or renewal result could potentially imply the result after an unstated specialization; broader historical priority and external mathematical audit remain open.

## References

1. H. Acan and P. Hitczenko, *On random trees obtained from permutation graphs*, arXiv:1406.3958v1, first publicly posted 16 June 2014, especially §2 (insertion algorithm) and §3.1–3.2 (leaves and diameter). https://arxiv.org/abs/1406.3958
2. S. Janson, *The number of occurrences of patterns in a random tree or forest permutation*, arXiv:2203.04182, first posted 8 March 2022; §§3, 6, 10–12. https://arxiv.org/abs/2203.04182
3. A. Mészáros, *Matchings on trees and the adjacency matrix: A determinantal viewpoint*, Random Structures & Algorithms 63 (2023), 753–778. https://doi.org/10.1002/rsa.21167
