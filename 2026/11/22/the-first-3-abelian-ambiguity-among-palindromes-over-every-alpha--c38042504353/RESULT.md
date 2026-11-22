# The first 3-Abelian ambiguity among palindromes over every alphabet

## Finding

Fix a labeled alphabet \(\Sigma\) of size \(q\ge2\). Two linear words are \(3\)-Abelian equivalent when the number of overlapping occurrences of every factor of lengths one, two and three agrees. Among ordinary palindromes, this observation distinguishes every word of length at most nine. The first collision occurs at length ten, where every fiber has size at most two and exactly
\[
\frac{q^2(q-1)}2
\]
fibers have size two. There are precisely two forms, up to alphabet relabeling:

* **Repeated marker:** \((a,a,a,b,a,a,b,a,a,a)\) and \((a,a,b,a,a,a,a,b,a,a)\), for ordered distinct letters \(a,b\).
* **Interchanged markers:** \((a,a,b,c,a,a,c,b,a,a)\) and \((a,a,c,b,a,a,b,c,a,a)\), for three distinct letters \(a,b,c\). Each unordered pair \(\{b,c\}\) is counted once.

Thus the numbers of distinct profiles and singleton profiles among length-ten palindromes are, respectively,
\[
q^5-\frac{q^2(q-1)}2,\qquad q^5-q^2(q-1).
\]
The two collision-family counts are \(q(q-1)\) and \(q\binom{q-1}{2}\), respectively. For binary words the two collisions are `0001001000` versus `0010000100` and their bit complements.

## Assumptions and scope

Words are finite, indexed, noncyclic and exactly palindromic (equality to their reversal); the alphabet is labeled, and different letters are genuinely distinct. The spectrum counts **contiguous overlapping factors with multiplicities**, not scattered subsequences, distinct-factor sets or a spectrum with added sentinels. Equivalence is considered only among palindromes of the same length; a nonsymmetric word may share a spectrum without being an admissible competitor. The theorem covers all \(q\ge2\) and only lengths \(1\le n\le10\). For \(n<3\) the available length-one and length-two factors suffice.

## Proof

**A full-spectrum finite reduction.** Every palindrome of length \(n\) has a unique first half of length \(h=\lceil n/2\rceil\), with the second half determined by reversal. Consequently at lengths at most ten every palindrome uses at most five distinct letters. If two palindromes of length at most ten are equivalent over any alphabet, relabel their joint **used** alphabet injectively into \(\{0,1,2,3,4\}\). They necessarily use the same letter support, because they have equal length-one factor counts. Thus the two words are carried to a pair of palindromes on five labeled letters with exactly the same factor multiplicities; their distinctness and multiplicities are preserved. In particular, a complete check of all five-letter palindromes through length ten proves absence of shorter collisions for **all finite alphabets**, not just five-symbol alphabets.

**Exact finite certificate.** `verify_full.py` enumerates every one of the \(5^{\lceil n/2\rceil}\) five-letter palindromes of each length \(1\le n\le10\). It directly constructs all factor counters at lengths one, two and three and groups the actual words by their exact tuple of counters. The complete result is: every fiber is singleton at lengths \(1\) through \(9\); at length ten there are exactly \(3025\) singleton profiles and \(50\) two-word profiles, accounting for all \(5^5=3125\) words. The certificate independently constructs *all* instantiations of the two displayed candidate families on the five-letter alphabet and asserts equality of the entire set of unordered size-two fibers to that expected set. It checks that no larger fibers exist. It iterates a complete finite domain; it is not sampling or extrapolating an experimental count.

**Independent verification.** `verify_independent.py` separately constructs integer-coded length-three spectra by a sliding three-symbol window, with the first two symbols retained. The standard de Bruijn flow identity shows this determines all shorter factor counts: for each two-letter factor \(xy\), its count is the number of triples starting with \(xy\) plus the indicator that the last two letters are \(xy\); the same relation yields one-letter counts. On a palindrome the last two letters are the reversal of the first two. The program checks these identities word by word, verifies injectivity at lengths below ten, and recovers exactly the predicted 50 two-word fibers at length ten. This is independent of the first program's direct all-length factor counting.

**Uniform alphabet count.** Because all collisions on five letters are exactly the two listed symbolic families, the relabeling reduction proves the same exhaustive family classification for any \(q\). Family one has \(q(q-1)\) unordered word-pairs: the majority symbol and the one marker are each fixed by the words. Family two has \(q\binom{q-1}{2}\) unordered pairs, because swapping \(b,c\) interchanges the two words but does not change the pair. The families cannot overlap, since family one has two distinct letters and family two has three. Therefore the total number of two-word classes is
\[
q(q-1)+q\binom{q-1}{2}=\frac{q^2(q-1)}2.
\]
Each length-ten palindrome comes uniquely from a five-letter prefix, so there are \(q^5\) source words. Removing one duplicate per two-word fiber gives the profile count, and removing both words in each two-word fiber gives the singleton count. The two families have equal spectra as is also independently verified directly; no other pairs exist by the complete five-letter certificate.

## Verification

Run `python verify_full.py` and `python verify_independent.py` using Python 3.8 or later and only the standard library. The expected terminal lines are `VERIFY_FULL_OK alphabet=5 lengths=1..10 words= 7810 length10_pairs=50 two_isomorphism_families` and `VERIFY_INDEPENDENT_OK q=5 n=1..10 verified_second_order_projection`. The tested 7,810 words are all five-letter palindromes at lengths one through ten, not a random subset. The arbitrary-alphabet quantifier follows from the five-symbol support reduction, not from empirical extrapolation. The finite check is fully reproducible and short enough to inspect line by line.

## Relationship to prior work

Karhumäki, Saarela and Zamboni (2013) define \(k\)-Abelian equivalence and show the unrestricted first nontrivial equalities can occur already at length \(2k\), whereas the palindromic restriction changes the first threshold. Karhumäki, Puzynina, Rao and Whiteland (2016) establish the general \(k\)-switching characterization and de Bruijn-path class formulas, but these statements alone do not enumerate the palindrome-only fibers at length ten. Cassaigne, Karhumäki and Puzynina's work on \(k\)-Abelian palindromes concerns words equivalent to **their own reversals** and richness of palindromic factors, a different inverse question. A published three-mer fiber theorem for words with exactly two nonzero positions treats a narrower sparse shell: it contains portions of the repeated-marker behavior but does not classify the distinct-marker four-position family or prove the universal palindrome threshold. A published enumeration of binary \(4\)-Abelian palindromes also concerns equivalence to reversal, not coincidence of the fingerprints of two different ordinary palindromes.

## Limitations

This is a sharp first-collision classification, not a characterization of ambiguity for longer words, other observation orders, noisy or missing reads, or circularized spectra. The proof relies on two transparent, exhaustive finite enumerators together with an alphabet-independent reduction; it does not assert a general closed form for all lengths. Prior-literature comparison is qualified by the possibility of an unindexed or inaccessible earlier statement of the same restricted first-collision problem. No independent mathematical audit has been performed.

## References

1. J. Karhumäki, A. Saarela and L. Q. Zamboni, *On a generalization of Abelian equivalence and complexity of infinite words*, first public version 2013-01-22, https://arxiv.org/abs/1301.5104 (especially §2, Lemma 2.4 and Theorem 2.6).
2. J. Karhumäki, S. Puzynina, M. Rao and M. A. Whiteland, *On cardinalities of k-abelian equivalence classes*, first public version 2016-05-11, https://arxiv.org/abs/1605.03319 (especially §§2–5).
3. J. Cassaigne, J. Karhumäki and S. Puzynina, *On k-abelian palindromes*, *Information and Computation* 260 (2018), 89–98, https://doi.org/10.1016/j.ic.2018.04.001 .
