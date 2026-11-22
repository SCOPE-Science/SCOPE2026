# Exact two-read deletion ambiguity and isolated-word spectrum in `010`-free binary words

## Finding

For each integer \(n\ge0\), let \(L_n\) consist of binary words of length \(n\) having no contiguous factor `010`. For \(n\ge1\), let \(D_1(w)\) be the **set of distinct** words obtained by deleting exactly one symbol from \(w\). Form the graph \(G_n\) on \(L_n\) by placing an edge between different words \(x,y\) precisely when \(|D_1(x)\cap D_1(y)|\ge2\). The empty graph \(G_0\) has the empty word as its sole vertex.

**Structural characterization.** For every \(n\), the edges of \(G_n\) are exactly the admissible adjacent swaps `01` \(\leftrightarrow\) `10`. More explicitly, each edge is represented *uniquely* by a word \(u01v\), with opposite endpoint \(u10v\), in which \(u\) and \(v\) avoid `010`, and each of \(u\) and \(v\) is either empty, is the single-letter word `1`, or respectively ends or begins in `11`.

The exact number \(e_n\) of edges has rational ordinary generating function
\[
\boxed{\sum_{n\ge0}e_nz^n=\frac{z^2(1-z)^2}{(1-2z+z^2-z^3)^2}.}
\]

**Isolated-word theorem.** A vertex \(w\in L_n\) has no ambiguity neighbors if and only if the padded word `11`\(w\)`11` avoids both `110111` and `111011`. Let \(s_n\) denote the number of isolated vertices, including \(s_0=1\). Then
\[
\boxed{\sum_{n\ge0}s_nz^n=
\frac{1+z+z^3+2z^4+2z^5+z^6}
{1-z-z^3-z^5-z^6-z^7}.}
\]
The first values for \(n=0,1,\ldots,12\) are
\[
(s_n)=(1,2,2,4,8,13,21,34,55,90,149,246,404),
\]
and for \(n=2,\ldots,12\),
\[
(e_n)=(1,2,3,6,13,26,50,96,184,350,661).
\]
The graph is bipartite, by the parity of the number of binary inversions in the word. Consequently its maximum independent set, when needed, is computable through bipartite matching, without claiming a closed formula for the optimal code size.

## Assumptions and scope

The alphabet is the labeled pair \(\{0,1\}\), and the forbidden factor `010` is contiguous and **linear**: there is no circular boundary condition. In particular the first or final one may be a singleton. The two reads are distinct **outputs**, not two deletion locations that happen to give the same output. At \(n=0\), the isolated-count convention concerns the empty word only and no deletion channel is applied. All formulas hold for all indicated nonnegative integral lengths; there is no probabilistic deletion model.

## Proof

**1. Two common single-deletion descendants.** Use the standard alternating-interval (Type-A) characterization of the one-deletion reconstruction relation, as proved by Cai, Kiah, Nguyen, and Yaakobi (2020): for two *different* length-\(n\) words, at least two distinct common single-deletion descendants occur precisely when their first-to-last differing interval has length at least two and consists of opposite phases of one alternating two-symbol pattern, with the words equal outside that interval. At most two distinct common descendants are possible. The statement can also be checked directly by aligning deletions: deletions at positions \(p<q\) force a one-position shift \(x_{p+1}\cdots x_q=y_p\cdots y_{q-1}\), while deletions at \(p>q\) force the reverse shift. Within either orientation repeated choices in the same constant run give the same output; obtaining both distinct outputs forces simultaneous opposite shifts and hence alternating phases over the minimal differing interval. Conversely deletion of opposite ends of such an interval gives two different common outputs.

For binary words, any opposite-phase alternating pair on an interval of length at least three contains `010` in one of its two words (already in the first three positions). Thus both endpoints can avoid `010` only when the interval length is two. Conversely swapping an adjacent unlike pair gives two distinct common deletion outputs, so the edge characterization is exact, including both ends of the word.

**2. Legal swap boundaries.** Orient an edge by writing its endpoints as \(u01v\) and \(u10v\), where the `01` is at the unique differing interval. The two words both avoid `010` if and only if \(u\) and \(v\) individually avoid `010` and the factors straddling the swap do not create `010`. For \(u\), this is equivalent to \(u\) being empty, `1`, or ending with `11`: an ending `0` creates `010` with the new `10`, whereas an ending `01` creates `010` with the old `01`; the other endings are safe. The right condition is the reversed counterpart: \(v\) is empty, `1`, or begins with `11`. The orientation `01` determines each edge exactly once, including its common outside words, so no edge is counted twice.

**3. Edge generating function.** Let \(a_m=|L_m|\). The standard prefix-state automaton for avoiding `010` has states ``, `0`, `01`, representing the longest proper-prefix suffix, with transitions respectively `(0,1)→(0,\epsilon)`, `(0,1)→(0,01)` and `(0,1)→(\mathrm{forbidden},\epsilon)`. Solving its three finite recurrences gives
\[
A(z)=\sum_{m\ge0}a_mz^m=\frac{1+z^2}{D(z)},\qquad D(z)=1-2z+z^2-z^3.
\]
The permitted left and right contexts have counts \(u_0=u_1=1\), and \(u_m=a_{m-2}\) for \(m\ge2\), since adjoining `11` on the appropriate side preserves avoidance. Their generating function is
\[
U(z)=1+z+z^2A(z)=\frac{1-z}{D(z)}.
\]
Each edge consists of two independent permitted contexts separated by the two swapped positions. Hence \(E(z)=z^2U(z)^2\), giving the displayed formula.

**4. Exact isolation language.** Append two `1` symbols on *each* side of a word, forming `11`\(w\)`11`. Such padding cannot create `010` across the ends. By step 2, a swappable pair is present precisely when the padded string contains a block `11 01 11` or `11 10 11`, i.e. `110111` or `111011`, with the pair inside the original word. Both six-letter patterns require two surrounding letters, so padding by exactly two is sufficient for the first and last swappable pairs. Thus a word is isolated exactly when its padded string avoids these two factors and `010`.

**5. Rational certificate for isolated words.** Apply the ordinary prefix automaton to forbidden factors `010`, `110111`, `111011`. Its eleven productive states, in this order, are
\[
\epsilon,0,1,01,11,110,111,1101,1110,11011,11101.
\]
For each state, appending `0` or `1` either hits a forbidden factor and is rejected, or moves to the longest suffix that is a state. Let \(T\) be the resulting eleven-state letter-count transition matrix, let \(b\) indicate which states permit a final suffix `11`, and start after reading initial padding `11`. Then the isolated-vertex series is the exact formal power series
\[
I(z)=\mathbf e_{11}^{\mathsf T}(\mathbf 1-zT)^{-1}b.
\]
Set \(Q(z)=1-z-z^3-z^5-z^6-z^7\), \(N(z)=1+z+z^3+2z^4+2z^5+z^6\). The standalone integer-polynomial verifier `verify_isolated.py` supplies all eleven polynomials \(X_i(z)\) and **proves algebraically** the finite polynomial identity
\[
(\mathbf 1-zT)X(z)=Q(z)b,\qquad X_{11}(z)=N(z),
\]
by checking each coefficient in every coordinate using integer arithmetic. Since \(Q(0)=1\) and \(\mathbf 1-zT\) is invertible as a matrix of formal power series, the identity proves \(I(z)=N(z)/Q(z)\) for every length, not merely for the tested finite range. The proof uses the explicit polynomial certificate, not a numerical matrix inversion or a finite extrapolation.

**6. Bipartiteness.** Swapping a `01` to `10` changes the inversion count by exactly one. Hence every edge joins an even- and an odd-inversion word, proving bipartiteness. The standard matching/vertex-cover theorem then gives the stated algorithmic consequence.

## Verification

Run `python3 verify_deletion.py`, `python3 verify_transfer.py`, and `python3 verify_isolated.py` from the directory containing these files. All scripts use only Python standard-library exact arithmetic; no external data or software packages are necessary. The first directly forms distinct deletion-descendant sets and checks every pair against legal swaps and the predicted edge count for every \(1\le n\le13\). The second checks the prefix automaton and exact rational edge-series coefficient identities through order 100 and independently counts all valid swaps through length 17. The third checks all coefficients of the eleven-vector polynomial identity, and independently compares isolation to the padded forbidden-factor test for all \(0\le n\le14\). Successful runs report `VERIFY_DIRECT_OK`, `VERIFY_TRANSFER_OK`, and `VERIFY_ISOLATED_OK`, respectively. Finite enumerations corroborate the universal theorem; the Type-A theorem, bijections and the displayed polynomial certificate establish the infinite claims.

## Relationship to prior work

The general alternating-interval characterization of two-read deletion ambiguity is an existing theorem; it is used here, not presented as new. The previously published unrestricted-alphabet edge census determines total edges in the full source space, while the present graph is the **induced** graph on `010`-free inputs. Its unique context factorization and the complete isolated-vertex rational spectrum are not supplied by that unrestricted census. Published binary pattern avoidance constructions consider related finite words without calculating this deletion-confusability graph. Published cyclic three-gram reconstruction for circular words without `010` has a different observation channel, boundary convention and equivalence relation; it cannot determine the number of vertices with two common deletion outputs here.

## Limitations

Neither the rational edge count nor the isolated count determines the exact maximum two-read reconstruction code size. The theorem says only that bipartite matching computes it for each finite length. The isolated series counts words with no neighbors, not every possible member of an optimal code. The alternating-interval lemma is used from published general literature, with a short alignment explanation included. A prior unindexed enumeration of exactly this constrained graph or its isolated vertices cannot be excluded; available source comparisons are not a proof of global historical priority. No results for other forbidden motifs, substitutions, insertions, circular words or multiple deletions are claimed.

## References

1. S. Bilotta, E. Grazzini, E. Pergola, R. Pinzani, “Generation of binary words avoiding alternating patterns,” arXiv:1210.7620, first publicly posted October 29, 2012. https://arxiv.org/abs/1210.7620
2. K. Cai, H. M. Kiah, T. T. Nguyen, E. Yaakobi, “Coding for Sequence Reconstruction for Single Edits,” arXiv:2001.01376, first posted January 6, 2020. https://arxiv.org/abs/2001.01376
3. L. Sala, R. Gabrys, C. Schoeny, L. Dolecek, “Exact Reconstruction from Insertions in Synchronization Codes,” arXiv:1604.03000, first posted April 11, 2016. https://arxiv.org/abs/1604.03000
4. “Exact edge count of the finite-alphabet two-read single-deletion reconstruction graph,” published mathematical record, October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-edge-count-of-the-finite-alphabet-two-read-single-deletion--737fed325e91
5. “Exact cyclic three-gram reconstruction for binary words with no isolated ones,” published mathematical record, November 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-cyclic-three-gram-reconstruction-for-binary-words-with-no--36dcf2861c14
