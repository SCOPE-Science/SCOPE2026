# Sharp sparse-return thresholds for the four-letter Rudin–Shapiro word

## Finding

Let \(\sigma\) be the constant-length substitution on \(\{a,b,c,d\}\) given by
\[
\sigma(a)=ab,\qquad \sigma(b)=ac,\qquad
\sigma(c)=db,\qquad \sigma(d)=dc,
\]
and let \(w=\sigma^\infty(a)\), indexed from \(0\). A *pseudoperiod* is a finite nonempty set \(S\subseteq\mathbb Z_{>0}\) with
\[
(\forall i\ge0)(\exists s\in S)\quad w_{i+s}=w_i.
\]
Three sharp optimization statements hold.

1. The least possible value of \(\max S\), without restricting \(|S|\), is \(10\). Every pseudoperiod contained in \(\{1,\ldots,10\}\) must contain all five even shifts \(\{2,4,6,8,10\}\), and this five-element set is itself a pseudoperiod. Hence the minimum cardinality at the shortest horizon is \(5\), uniquely attained.
2. The least cardinality of any pseudoperiod, with no bound on shifts, is \(4\).
3. Among four-element pseudoperiods, the least possible maximum shift is \(66\). The *complete list* with maximum shift at most \(66\) is
\[
\boxed{\{2,14,64,66\}\quad\text{and}\quad\{2,52,64,66\}}.
\]
In particular, the minimum-cardinality requirement increases the least maximum shift sharply from \(10\) to \(66\).

## Assumptions and scope

The alphabet consists of four *distinct literal symbols*. Equality of letters in the pseudoperiod condition is not equality under a binary coding. The fixed point is one-sided, begins in \(a\), and the quantifier over starting positions includes \(i=0\). Every shift is a strictly positive integer. “Unique” refers to literal sets of shifts, not to supersets obtained by adding redundant shifts.

## Proof

**1. Parity and binary projection.** The first letter of each substituted pair lies in \(\{a,d\}\), and the second lies in \(\{b,c\}\). Consequently,
\[
w_{2j}\in\{a,d\},\qquad w_{2j+1}\in\{b,c\}
\quad(j\ge0).
\]
Thus \(w_i\ne w_{i+s}\) whenever \(s\) is odd. Any odd shift is useless, and deleting odd shifts from a pseudoperiod preserves its defining property.

Define the binary coding \(\tau(a)=\tau(b)=0\), \(\tau(c)=\tau(d)=1\) and \(r_j=\tau(w_j)\). Directly from the substitution and the above parity classes,
\[
r_{2j}=r_j,\qquad r_{2j+1}=r_j\oplus(j\bmod2),\qquad r_0=0,
\]
where \(\oplus\) denotes addition modulo \(2\). These recurrences uniquely identify \(r_j\) as the parity of the number of overlapping \(11\) blocks in the base-two expansion of \(j\). Hence \(r\) is the ordinary binary Rudin–Shapiro sequence. Every pseudoperiod of \(w\) projects to one of \(r\). Meleshko–Ochem–Shallit–Shan, Theorem 28, prove that the latter has no pseudoperiod of cardinality \(3\); a smaller one could be enlarged to cardinality \(3\). Therefore \(w\) has no pseudoperiod of cardinality at most \(3\). (Their binary positive witness does *not* automatically lift to four distinct symbols.)

**2. Exact finite-language saturation.** For any finite word \(U\) and any positive integer \(L\), write \(\mathcal F_L(U)\) for its set of contiguous length-\(L\) factors. When \(|U|\ge L\) and \(L\ge3\), every factor of length \(L\) in \(\sigma(U)\) spans at most \(\lceil(L+1)/2\rceil\le L\) complete or partial preimage letters. This preimage interval extends to a length-\(L\) factor inside \(U\). Conversely, every length-\(L\) factor of \(\sigma(V)\) for \(V\in\mathcal F_L(U)\) occurs in \(\sigma(U)\). Thus the *exact equality*
\[
\mathcal F_L(\sigma(U))
=\bigcup_{V\in\mathcal F_L(U)}\mathcal F_L(\sigma(V))
\]
holds. It follows that equality of two consecutive substitution-stage length-\(L\) factor sets implies equality at every later stage, and hence gives the entire length-\(L\) language of the infinite fixed point.

Take \(L=67\) and \(W_j=\sigma^j(a)\). The independent, deterministic `verify.py` in this package constructs \(W_{11}\) of length \(2048\) and \(W_{12}\) of length \(4096\), and computes, by explicit substring sets,
\[
\mathcal F_{67}(W_{11})=\mathcal F_{67}(W_{12}),
\qquad|\mathcal F_{67}(W_{11})|=528.
\]
It additionally computes the substitution closure of these \(528\) words and checks equality, independently of comparing the two long prefixes. Thus its \(528\) listed-in-memory factors are *exhaustively* the factors of length \(67\) of \(w\). Their length-\(11\) prefixes are exactly the \(80\) factors of length \(11\) (also cross-checked against \(W_{12}\)). These are infinite-word statements, not an assumption that a large finite prefix is representative.

**3. Finite exact covering reduction.** Enumerate the \(528\) length-\(67\) factors in lexicographic order \(f_0,\ldots,f_{527}\). For each integer \(1\le s\le66\), let \(C_s\) be the \(528\)-bit integer with bit \(j\) set exactly when \((f_j)_0=(f_j)_s\). A nonempty \(S\subseteq\{1,\ldots,66\}\) is a pseudoperiod if and only if
\[
\bigvee_{s\in S}C_s=2^{528}-1,
\]
where \(\vee\) is bitwise inclusive OR. Both implications follow by taking the length-\(67\) factor beginning at each index of the infinite word, and by the fact that every listed factor occurs somewhere. Odd-shift columns are empty.

For \(s=2,4,6,8,10\), the following *actual length-\(11\) factors* have equality between positions \(0\) and \(s\), but no equality between position \(0\) and the other four even shifts up to \(10\):

| Only matching even shift | Witness factor |
|---|---|
| \(2\) | `babacdcacdc` |
| \(4\) | `acdcacdcdbd` |
| \(6\) | `acdcdbabdbd` |
| \(8\) | `abdbdcdbabd` |
| \(10\) | `abdbdcdbdca` |

These five witnesses force all five even shifts whenever the horizon is at most \(10\). In particular `abdbdcdbdca` witnesses the impossibility of any horizon at most \(9\). A full OR of the corresponding five columns is \(2^{528}-1\), proving the first assertion and its uniqueness statement. As a separate redundant exhaustive check, `verify.py` inspects all \(2^{10}=1024\) subsets of shifts at this horizon and finds precisely \(32\) pseudoperiods, obtained by optionally including the five useless odd shifts.

For cardinality \(4\), the binary-projection lower bound and parity rule force all four shifts to be even. The verifier examines **every** unordered four-subset of the \(33\) even integers from \(2\) through \(66\), i.e. all \(\binom{33}{4}=40920\) possibilities. It performs the exact \(528\)-bit OR comparison above for each; exactly the following two subsets cover the entire language:
\[
\{2,14,64,66\},\qquad\{2,52,64,66\}.
\]
All \(\binom{32}{4}=35960\) four-subsets with shifts at most \(64\) fail. An odd maximum shift of \(65\) cannot improve this bound, so no four-element pseudoperiod exists with maximum at most \(65\). The two successful sets establish cardinality \(4\), and the complete enumeration establishes their uniqueness at horizon \(66\), as claimed.

## Verification

Run `python3 verify.py` with the standard Python library. The code constructs substitution powers and factor sets from scratch; it does not import previously obtained tables, external data, or a specialized automata package. It checks the exact stage equality and substitution closure; all \(80\) relevant short factors; all ten-shift subsets; all \(40920\) even four-shift candidates; parity of positions; binary-coding agreement with direct adjacent-one digit counting; and independent direct-position testing in a substitution prefix of length \(8192\).

Observed output:

```
VERIFY_OK factors67=528 factors11=80 four_shift_sets_checked=40920 max64_checked=35960 optimum_sets=2 horizon10_minimum=5
```

The finite enumeration is exhaustive for the infinite problem *because* the length-\(67\) language is certified by the substitution-saturation argument, not because a long prefix is deemed sufficient.

## Relationship to prior work

The pseudoperiod definition and the **binary** Rudin–Shapiro cardinality lower bound are due to Meleshko, Ochem, Shallit, and Shan (2022/2023), particularly Definition 1 and Theorem 28 of their paper. Their binary-sequence result does not give the literal four-letter covering problem: coding two different states to one binary symbol can create equality that is absent before coding. We use their lower bound through a rigorously identified coding and independently solve the four-letter delay and sparse-support optimizations by an exact finite-language certificate.

Published studies of Rudin–Shapiro substitution structure and string attractors address different invariants. The statement above is about equality at a future index, and is not implied by factor-complexity counts, literal reflection complexity, or binary pseudoperiodicity alone.

## Limitations

The two listed optimal sets are all the *four-element* pseudoperiods only up to maximum shift \(66\); no claim classifies all four-element sets with larger maximum shift. The finite-language method is explicit for this substitution and is not asserted to generalize with these same numerical thresholds to arbitrary automatic words. The cardinality lower bound relies on a published binary result rather than re-running its extensive independent Walnut computation. Searches and comparisons cannot guarantee that no equivalent unindexed result predates this work. Independent review has not been performed.

## References

- Joseph Meleshko, Pascal Ochem, Jeffrey Shallit, Sonja Linghui Shan, *Pseudoperiodic Words and a Question of Shevelev*, arXiv:2207.10171 (first public version 2022-07-20), *Discrete Mathematics & Theoretical Computer Science* **25:2** (2023), DOI: 10.46298/dmtcs.9919. Definition 1 and Theorem 28, especially Section 4.4. https://arxiv.org/abs/2207.10171 ; https://dmtcs.episciences.org/en/articles/9919
- Jean-Paul Allouche and Jeffrey Shallit, *Automatic Sequences: Theory, Applications, Generalizations*, Cambridge University Press (2003), for background on uniform substitutions and the Rudin–Shapiro word.
