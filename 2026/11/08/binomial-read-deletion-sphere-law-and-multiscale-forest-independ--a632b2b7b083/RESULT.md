# Binomial read-deletion sphere law and multiscale forest independence

## Finding

For a uniformly sampled length-\(n\) word over \(q\ge 2\) letters, the number \(B_\ell\) of distinct single-coordinate deletions of its **interior, unordered-composition** length-\(\ell\) read sequence has the exact finite law
\[
 B_\ell\ \overset{d}{=}\ 1+\operatorname{Bin}\left(n-\ell,\frac{q-1}{q}\right),\qquad 1\le\ell\le n.
\]
The laws at different window sizes have zero pairwise covariances:
\[
\operatorname{Cov}(B_\ell,B_k)=0\qquad(\ell\ne k).
\]
This **does not** imply independence: with binary words of length three, \(B_1=2\) forces \(B_2=2\), although each event has probability \(1/2\). The underlying equality comparisons on an arbitrary set of distinct position-pairs are mutually independent if and only if that pair graph is a forest.

## Assumptions and scope

Let \(q,n\) be integers with \(q\ge2\) and \(n\ge1\). Let \(\Sigma_q=\{0,\ldots,q-1\}\) and let \(X=(X_1,\dots,X_n)\) have independent uniform coordinates. For integer \(1\le\ell\le n\), put \(m=n-\ell+1\), and define \(R_\ell(X)=(W_1,\dots,W_m)\), where \(W_i\in\mathbb Z_{\ge0}^q\) counts all symbols in \(X_i,\dots,X_{i+\ell-1}\). Thus the entries are unordered composition vectors, **not** ordered \(\ell\)-mers. Only the \(m\) fully contained windows are used: no zero padding or partial boundary windows. Let \(D_1(y)\) be the set of sequences obtained from a nonempty sequence \(y\) by removing one of its entries, and \(B_\ell(X)=|D_1(R_\ell(X))|\); for \(m=1\), this is one (the empty sequence). The same original \(X\) determines the entire family indexed by \(\ell\).

## Proof

**Deletion classes.** For any nonempty finite sequence \(y=(y_1,\dots,y_m)\), deleting positions \(i<j\) produces equal sequences if and only if \(y_i=y_{i+1}=\cdots=y_j\). The forward implication follows by comparing coordinates \(i,\dots,j-1\) of the two outputs; the reverse is immediate. Consequently, there is exactly one distinct deletion descendant per maximal constant run and
\[
 |D_1(y)|=1+\sum_{i=1}^{m-1}\boldsymbol1_{\{y_i\ne y_{i+1}\}}.
\]

**Window transitions.** Moving from \(W_i\) to \(W_{i+1}\) removes one instance of \(X_i\) and adds one of \(X_{i+\ell}\). Equality of vectors holds precisely when \(X_i=X_{i+\ell}\), so
\[
 B_\ell(X)=1+\sum_{i=1}^{n-\ell}\boldsymbol1_{\{X_i\ne X_{i+\ell}\}}.\tag{1}
\]
This identity includes \(n=\ell\), with empty sum.

**Forest lemma.** Let \(F\) be a set of distinct unordered pairs of vertices in \([n]\). If graph \(([n],F)\) is a forest, root each tree and expose the root's symbol and then each child symbol in parent-before-child order. For every edge, conditional on everything previously exposed, the child is independent uniform, so its equality indicator has conditional probability \(1/q\) and its inequality indicator probability \((q-1)/q\). Hence all such edge indicators are mutually independent Bernoulli\((1/q)\). Conversely, if the graph contains a simple cycle of length \(r\ge3\), all \(r\) edge equalities on that cycle hold exactly when its \(r\) vertices have the same symbol. That event has probability \(q^{1-r}\), rather than \(q^{-r}\) as mutual independence would require. Hence independence is impossible. This proves the exact forest criterion.

For each fixed \(\ell\), the edges \(\{i,i+\ell\}\), \(1\le i\le n-\ell\), form \(\ell\) disjoint paths (some may be singletons). By the forest lemma, all summands in (1) are independent Bernoulli\(((q-1)/q)\). The binomial law follows. In particular,
\[
\Pr(B_\ell=1+j)=\binom{n-\ell}{j}\left(\frac{q-1}{q}\right)^j\left(\frac1q\right)^{n-\ell-j},\quad 0\le j\le n-\ell,
\]
and \(\mathbb E B_\ell=1+(n-\ell)(q-1)/q\), \(\operatorname{Var} B_\ell=(n-\ell)(q-1)/q^2\).

If \(\ell\ne k\), an edge of length \(\ell\) and an edge of length \(k\) are distinct. Any two distinct edges either share no vertices or exactly one. In either case they form a forest; their equality (or inequality) indicators are independent. Expanding the covariance of the two sums in (1) shows that every pairwise term is zero. Therefore \(\operatorname{Cov}(B_\ell,B_k)=0\).

For failure of mutual independence, take \(q=2,n=3\). Then \(B_1=2\) is the event that precisely one of \(X_1\ne X_2\) and \(X_2\ne X_3\) holds; it occurs with probability \(1/2\) and implies \(X_1\ne X_3\), namely \(B_2=2\). Since \(\Pr(B_2=2)=1/2\), these two events are dependent.

## Verification

Run `python3 checker.py` with the standard Python library. This exhaustively counts deletion descendants and checks their complete distributions and all pairwise covariances for small alphabets and lengths, independently enumerates forest/cyclic equality events, and tests the explicit dependence witness. These finite tests serve as regression checks; the proof above is valid for all stated parameters without finite-enumeration assumptions.

## Relationship to prior work

The 2026 ordered \(\ell\)-symbol read-deletion study of Ye and Ge motivates deletion of window observations but uses **ordered** \(\ell\)-mers; equality of consecutive ordered windows is not the exiting/entering equality in (1). Yu, Ye and Schwartz (2024) analyze an **unordered-composition** window-read model under tandem-duplication errors, with asymptotic code rates rather than the random single-deletion output multiplicity and joint-window statistics computed here. Banerjee, Yehezkeally, Wachter-Zeh and Yaakobi (2024) analyze binary padded read vectors and a single deletion, using run methods for code bounds; their model includes additional boundary observations and the inspected results do not give the all-\(q\) unpadded binomial law, cross-window covariance identity, or forest criterion. These differences matter: no equivalence of padded and interior models is asserted. Forest label independence is a general combinatorial fact used in the proof; the stated read-channel laws arise by identifying its specific graph.

## Limitations

The input symbols must be independent and uniform. For biased independent symbols, neighboring edge equalities sharing a vertex need not be independent and the binomial law can fail. The full read sequence is unpadded and its observations are unordered composition vectors, not ordered \(\ell\)-mers. The pairwise uncorrelated property is not joint independence and does not itself produce a packing bound or correcting code. No claim is made about two or more deletions, noisy windows, or optimized code sizes. Priority relative to unindexed work and independent validation remain open.

## References

1. Z. Ye and G. Ge, *Deletion-Correcting Codes for the \(\ell\)-Symbol Read Channel*, arXiv:2606.26434, first public 2026-06-24. https://arxiv.org/abs/2606.26434
2. W. Yu, Z. Ye and M. Schwartz, *On the Asymptotic Rate of Optimal Codes that Correct Tandem Duplications for Nanopore Sequencing*, arXiv:2408.08223, first public 2024-08-15. https://arxiv.org/abs/2408.08223
3. A. Banerjee, Y. Yehezkeally, A. Wachter-Zeh and E. Yaakobi, *Correcting a Single Deletion in Reads from a Nanopore Sequencer*, arXiv:2401.15939, first public 2024-01-29. https://arxiv.org/abs/2401.15939
