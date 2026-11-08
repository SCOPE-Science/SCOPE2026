# Every smallest string attractor of a repeated permutation word

## Finding

Let \(q\ge3\) and \(k\ge2\) be integers, and let
\(P=c_0c_1\cdots c_{q-1}\) be any word of \(q\) pairwise distinct letters.
Consider \(W=P^k\), with its \(qk\) positions numbered from \(0\) to
\(qk-1\). A *string attractor* is a set of positions intersecting at least
one occurrence of every nonempty contiguous factor of \(W\).

**Theorem.** The minimum cardinality of a string attractor of \(W\) is
exactly \(q\). A set of that cardinality is an attractor if and only if
it contains exactly one occurrence of each of the \(q\) letters and does
**not** simultaneously contain the first and last positions of \(W\).
Equivalently, for integers \(0\le t_i<k\), every smallest attractor has
exactly the form
\[
\Gamma(t_0,\ldots,t_{q-1})
 =\{qt_i+i:0\le i<q\},
 \qquad \neg(t_0=0\ \text{and}\ t_{q-1}=k-1).
\]
Consequently, the exact number of smallest attractors is
\[
M(q,k)=k^q-k^{q-2}=k^{q-2}(k^2-1).
\]
Among all size-\(q\) sets with one position of each letter, the *single*
length-two factor \(c_{q-1}c_0\) is a complete test: attracting this
factor implies attracting every factor of \(W\).

## Assumptions and scope

The letters \(c_i\) are distinct, but their ordering and names are
arbitrary. The word is finite, with precisely \(k\) complete copies of
\(P\), no delimiter and no circular wrap between the final and first
positions. Factors are contiguous and nonempty, while occurrences and
attractor positions use the usual linear (not circular) convention.
The theorem claims *all* cardinality-minimal attractors for
\(q\ge3\), \(k\ge2\). It does not classify attractors with additional
positions or powers of words containing repeated letters within the
base period. The case \(k=1\) has only the full position set as a
smallest attractor; the case \(q=2\) admits the same formula but is not
claimed as new here.

## Proof

1. **Lower bound and form of a candidate.** Every letter \(c_i\) occurs
   in \(W\), so its singleton factor requires at least one position
   carrying that letter in any attractor. Therefore every attractor
   has at least \(q\) positions. A size-\(q\) attractor must choose
   exactly one position for each letter. This selection is uniquely
   represented by \(\Gamma(t_0,\ldots,t_{q-1})\) above.

2. **Necessary endpoint exclusion.** The factor \(c_{q-1}c_0\)
   appears exactly at the \(k-1\) junctions between consecutive
   copies of \(P\). A size-\(q\) selection can intersect one of its
   occurrences only through its chosen \(c_{q-1}\) position or its
   chosen \(c_0\) position. If both endpoint positions \(0\) and
   \(qk-1\) are selected, neither of these two chosen positions lies
   at an internal junction, and no other selected letter can help.
   Hence that selection is not an attractor.

3. **Occurrence-phase lemma.** Every nonempty factor \(v\) of length
   \(\ell\), whose first letter is \(c_s\), can start only at positions
   \(s+jq\) for nonnegative integers \(j\). Because \(P\) consists
   of distinct letters, no other starting residue is possible.
   Periodicity ensures that all admissible such positions give the
   same factor. In particular, the starts are exactly
   \[
     s,s+q,\ldots,s+Jq,\quad
     J=\left\lfloor\frac{qk-\ell-s}{q}\right\rfloor.
   \]
   At least one start exists because \(v\) is a factor.

4. **Short factors.** Suppose \(1\le\ell<q\). If
   \(s+\ell\le q\), the factor is wholly contained in each copy
   of \(P\). The chosen position with letter \(c_s\) is the start
   of one of these \(k\) occurrences, so the factor is attracted.
   If \(s+\ell>q\), the factor crosses the junction
   \(c_{q-1}c_0\), and it has an occurrence across *every* one of
   the \(k-1\) junctions. If the chosen positions do not contain
   both endpoints, then at least one chosen \(c_0\) or
   \(c_{q-1}\) position lies at an internal junction, and the
   corresponding occurrence of \(v\) intersects it.

5. **Long factors.** Suppose \(\ell\ge q\). The intervals of
   successive occurrences from step 3 overlap or touch, so their
   union is exactly
   \[
      I=[s,s+Jq+\ell).
   \]
   Its omitted left prefix \([0,s)\) has length less than \(q\),
   and the omitted right suffix \([s+Jq+\ell,qk)\) has length
   \(r=qk-s-Jq-\ell\) with \(0\le r<q\) by maximality of
   \(J\). If a size-\(q\) selection with one of each letter
   avoided \(I\), its chosen \(c_0\) position would have to be
   \(0\): the left prefix contains \(c_0\) only there and the
   right suffix, being shorter than a period, contains no \(c_0\).
   Similarly its chosen \(c_{q-1}\) position would have to be
   \(qk-1\): the left prefix contains no \(c_{q-1}\), while the
   right suffix can contain that letter only at the last position.
   This contradicts the endpoint exclusion. Thus \(I\) contains
   a chosen position, and because \(I\) is the union of actual
   occurrence intervals, \(v\) is attracted.

6. **Sharpness and enumeration.** Steps 4 and 5 show that every
   one-per-letter selection not containing both endpoints attracts
   every nonempty factor. Combined with steps 1 and 2, this proves
   the characterization and minimal size. There are \(k^q\)
   possible one-per-letter selections. Exactly \(k^{q-2}\) select
   both endpoints: the two outer letter positions are then fixed
   and all other \(q-2\) selections are free. Subtraction yields
   the stated formula. The length-two local test follows from the
   necessity in step 2 and the sufficiency in steps 4 and 5.

## Verification

The standalone Python 3 program `verify.py` constructs the complete
set of distinct factors of \(W\), unions position masks over *all*
occurrences of each factor, and checks each one-per-letter position
selection against these masks. It independently compares the outcome
with the theorem's endpoint predicate and compares the number of
successful selections with \(k^q-k^{q-2}\).

Running `python3 verify.py` gives a successful exhaustive finite check
for \(31\) parameter pairs with \(2\le q\le8\),
\(2\le k\le6\), subject to the explicitly stated finite runtime
bounds in the program. It tests \(204695\) candidate sets, on words
of length at most \(35\). The \(q=2\) tests are regression checks,
not part of the claimed new domain. The mathematical argument above
is a proof for all permitted integer parameters; finite tests are
only corroboration, not its substitute.

## Relationship to prior work

Mantaci, Restivo, Romana, Rosone and Sciortino (2019) introduce the
finite-word string-attractor framework and prove, in their
Proposition 4, the general power bound
\(\gamma^*(u)\le\gamma^*(u^k)\le\gamma^*(u)+1\).
They give a minimal attractor for an individual word consisting of
runs of pairwise distinct letters (Corollary 2), but these results
alone neither characterize all minimal position sets for a repeated
permutation nor count them. The present theorem settles both
questions exactly in this family.

Restivo, Romana and Sciortino (2022) treat attractor-profile questions
for infinite words, including boundedness for periodic words.
Cassaigne, Gheeraert, Restivo, Romana, Sciortino and Stipulanti (2024)
study attractor position dispersion and related complexity measures;
their general bounds do not imply this exact all-minimizer count.
More recently, Banbara and collaborators (2026) enumerate all
smallest attractors for particular Fibonacci and period-doubling
families, rather than permutation powers.

The binary alternating specialization is already accounted for by
prior work. Here the new domain has at least three distinct letters;
a binary position-pair classification does not imply the unrestricted
multi-letter theorem. The key new structural ingredient is the
short-factor/internal-junction versus long-factor/interval-union
dichotomy in steps 4 and 5.

## Limitations

This result concerns linear factors and exactly repeated
permutations only. General words with multiple occurrences of a
symbol within the base period can have different optimal attractor
families. The proof does not establish uniqueness against every
potentially unindexed prior formulation; mathematical priority is
subject to independent literature review. No independent audit or
formal mechanized proof is claimed.

## References

- S. Mantaci, A. Restivo, G. Romana, G. Rosone, and M. Sciortino,
  *String Attractors and Combinatorics on Words*, arXiv:1907.04660,
  first public version 2019-07-10, https://arxiv.org/pdf/1907.04660.
- A. Restivo, G. Romana, and M. Sciortino,
  *String Attractors and Infinite Words*, arXiv:2206.00376,
  first public version 2022-06-01, https://arxiv.org/pdf/2206.00376.
- J. Cassaigne, F. Gheeraert, A. Restivo, G. Romana, M. Sciortino,
  and M. Stipulanti, *New string attractor-based complexities for
  infinite words*, Journal of Combinatorial Theory A 208 (2024),
  article 105936, public author manuscript:
  https://orbi.uliege.be/handle/2268/309672.
- M. Banbara, H. Bannai, P. Guo, D. Köppl, T. Mieno, and Y. Okamoto,
  *The Smallest String Attractors of Fibonacci and Period-Doubling
  Words*, CPM 2026, https://doi.org/10.4230/LIPIcs.CPM.2026.33.
