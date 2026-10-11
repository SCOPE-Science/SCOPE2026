# Exact quantifier-rank profiles for finite equivalence relations
## Finding
Let \(A\) and \(B\) be nonempty finite structures in the language with one binary relation \(E\), interpreted as an equivalence relation, and let \(q\ge 1\). For \(k\ge 1\), let \(N_k(A)\) be the number of \(E\)-classes of cardinality at least \(k\). For \(1\le k<q\), let \(C_k(A)\) be the number of \(E\)-classes of cardinality exactly \(k\). Define the analogous quantities for \(B\).

Then \(A\) and \(B\) satisfy exactly the same first-order sentences of quantifier rank at most \(q\) if and only if both families of truncated equalities hold:
\[
\min\bigl(N_k(A),q-k+1\bigr)=\min\bigl(N_k(B),q-k+1\bigr)\qquad(1\le k\le q),
\]
and
\[
\min\bigl(C_k(A),q-k\bigr)=\min\bigl(C_k(B),q-k\bigr)\qquad(1\le k<q).
\]
Thus bounded-rank first-order equivalence of finite partitions is determined by a triangular amount of class-size data: cumulative counts use threshold \(q-k+1\), while exact small-class counts use threshold \(q-k\).

## Assumptions and scope
The structures are finite and nonempty, equality is available as a logical symbol, and \(E\) is the only nonlogical relation. Quantifier rank is the usual nesting depth. The statement is for ordinary first-order logic, not monadic second-order logic and not richer vocabularies containing unary labels or additional relations.

## Proof
By the Ehrenfeucht--Fraisse theorem it is enough to characterize when Duplicator wins the \(q\)-round game.

Necessity is witnessed by formulas. Fix \(k\). With one free variable \(x\), the assertion that the \(E\)-class of \(x\) has at least \(k\) elements has quantifier rank \(k-1\): choose \(k-1\) further distinct elements equivalent to \(x\). The assertion that the class of \(x\) has exactly \(k\) elements has quantifier rank \(k\): conjoin the preceding lower bound with the assertion that every element equivalent to \(x\) is one of those \(k\) displayed elements.

For \(m\ge1\), the assertion that there are at least \(m\) pairwise distinct \(E\)-classes of size at least \(k\) is obtained by choosing representatives \(x_1,\ldots,x_m\), requiring \(\neg E(x_i,x_j)\) for \(i\ne j\), and requiring the size-at-least-\(k\) formula at each representative. Its quantifier rank is \(m+k-1\). Hence rank \(q\) determines \(N_k\) up to threshold \(q-k+1\). Similarly, the assertion that there are at least \(m\) classes of size exactly \(k\) has quantifier rank \(m+k\), so rank \(q\) determines \(C_k\) up to threshold \(q-k\). This proves both truncated equalities are necessary.

For sufficiency, assume all truncated equalities. After \(j\) rounds, Duplicator maintains a partial isomorphism and the following stronger invariant for every pair of already touched classes. If \(r\) distinct selected points lie in the paired classes, then either the two full class sizes are equal, or each class has at least \(q-j\) unselected points. This invariant is vacuous before the first move and guarantees a legal response whenever Spoiler returns to a previously touched class. If Spoiler repeats a previously selected point, Duplicator repeats its mate.

Suppose the next move is round \(j+1\), and Spoiler chooses the first point from a previously untouched class of size \(s\). Put \(h=q-j\). After this move there will be \(q-j-1\) rounds left, so it is enough to pair the new class with a fresh class of exactly size \(s\), or, when \(s\ge h\), with any fresh class of size at least \(h\).

First suppose \(s<h\). If the other structure had no fresh class of size exactly \(s\), every previously used class of size \(s\) there must have been matched earlier to a class of size exactly \(s\): at each earlier first-touch move the threshold was strictly larger than \(s\), so flexible matching was impossible. Let \(u\) be the number already used. Then \(u\le j\le q-s-1<q-s\). Exhaustion would give \(C_s\) equal to \(u\) on the responding side, while the side just played in has at least \(u+1\) such classes, contradicting equality after truncation at \(q-s\).

Now suppose \(s\ge h\). If the other structure had no fresh class of size at least \(h\), let \(u\) be the number of already used classes there having size at least \(h\). Every such class was matched to a class of size at least \(h\): at an earlier first-touch move the threshold was at least \(h\), so a smaller class could only have been matched exactly. Thus the side just played in already has \(u\) used classes of size at least \(h\), plus the new one. But \(u\le j=q-h<q-h+1\), contradicting equality of \(N_h\) after truncation at \(q-h+1\). Therefore a suitable fresh class always exists.

With the new classes paired as above, either their sizes agree or both have at least \(h-1=q-(j+1)\) unselected points after the selected representatives are removed, so the invariant is preserved. Duplicator therefore survives all \(q\) rounds.

## Verification
The proof is self-contained. As a finite consistency check, `verify.py` exhaustively compares the criterion with a direct recursive Ehrenfeucht--Fraisse game solver for every pair of integer partitions of nonempty sets of size at most \(8\) and for \(1\le q\le4\). The verifier prints `VERIFY_OK` only if there is no discrepancy. This finite computation is corroboration only; it is not used to justify the general theorem.

## Relationship to prior work
Tenney's 1975 analysis of one equivalence relation defines a sufficient relation \(S_n\) by truncating, uniformly at \(n\), the number of classes of every exact size below \(n\) and the number of classes of size at least \(n\); his Corollary 1 states that \(S_n\) implies \(n\)-round first-order equivalence. The criterion above is both necessary and sufficient and replaces that uniform truncation by two sharp triangular thresholds, one cumulative and one exact.

Kieronski and Kuusisto study richer first-order fragments with a freely usable built-in equivalence relation and prove finite-model and small-class properties. Their setting motivates explicit compression of equivalence-class information, but the exact pure-language quantifier-rank profile above is not stated in the inspected paper.

## Limitations
The literature search found no statement matching these two simultaneous threshold families, but absence from the searched sources is not a proof of priority. The result may be folklore or appear in an unindexed exercise, thesis, or older treatment of the first-order theory of one equivalence relation. The theorem does not directly extend to two equivalence relations, unary colors, or monadic second-order quantification.

## References
1. R. L. Tenney, “Second-order Ehrenfeucht games and the decidability of the second-order theory of an equivalence relation,” Journal of the Australian Mathematical Society 20 (1975), 323–331, DOI 10.1017/S1446788700020681.
2. E. Kieronski and A. Kuusisto, “Uniform One-Dimensional Fragments with One Equivalence Relation,” CSL 2015, DOI 10.4230/LIPIcs.CSL.2015.597.
3. A. Ehrenfeucht, “An application of games to the completeness problem for formalized theories,” Fundamenta Mathematicae 49 (1961), 129–141.
