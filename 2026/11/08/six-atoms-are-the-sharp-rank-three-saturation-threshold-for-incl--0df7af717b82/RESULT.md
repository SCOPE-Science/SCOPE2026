# Six atoms are the sharp rank-three saturation threshold for inclusion-only Boolean lattices

## Finding

Write \(B_n=(\mathcal P([n]),\subseteq)\), where \([n]=\{1,\ldots,n\}\) and \(B_0\) is the singleton inclusion poset. The first-order signature consists of **only** the binary relation \(\subseteq\); there are no constants, Boolean operations, or named atoms. Let \(\equiv_3\) mean agreement on every first-order sentence of quantifier rank at most three, with unrestricted reuse of variables and Boolean connectives.

For all integers \(n,m\ge0\),
\[
B_n\equiv_3 B_m\quad\Longleftrightarrow\quad
(n=m<6)\ \lor\ (n\ge6\ \land\ m\ge6).
\]
Consequently the family has exactly seven rank-three theories: one for each of \(n=0,1,2,3,4,5\), and one containing every \(n\ge6\). For the explicitly verified sizes \(n=6,7,8\), the seven realized rank-two unary types correspond to seven cardinality regions: \(0\), \(1\), \(2\), \(3\le |A|\le n-3\), \(n-2\), \(n-1\), and \(n\). This finite observation is auxiliary to the all-size rank-three theorem. The smallest representative of the stable class is \(B_6\), with \(64\) elements; \(B_5\), with \(32\) elements, is not equivalent to it. In contrast to the pure-order signature, a known atom-count cutoff for the *full Boolean-algebra signature* is \(2^3=8\); that result does not imply the sharper pure-order threshold.

## Assumptions and scope

The underlying sets \([n]\) are finite; no finiteness or nonemptiness convention is imposed on the set of atoms beyond \(n\ge0\). First-order quantifiers range over **subsets** of \([n]\), not over ground atoms. Inclusion is reflexive. Formula rank is nesting depth of quantifiers, not the number of variable symbols. The answer concerns only this family and rank three. It is not a claim about elementary equivalence at every rank or about arbitrary distributive lattices.

## Proof

**Exact orbit recursion.** After choosing \(k\) subsets \(A_0,\ldots,A_{k-1}\), each ground atom has a membership word \(b\in\{0,1\}^k\). Let \(v_b\) be the number of atoms of pattern \(b\). The vector \(v\), whose entries are nonnegative and sum to \(n\), completely determines the tuple orbit under permutations of \([n]\), and every such vector is realized. The atomic diagram of the tuple records, for every \(i,j<k\), whether
\[
A_i\subseteq A_j\quad\Longleftrightarrow\quad
v_b=0\ \text{for all } b \text{ with } b_i=1,\ b_j=0.
\]
Mutual inclusion expresses equality, so the diagram includes every atomic formula.

Define a canonical rank-\(r\) signature \(T_r(n,k,v)\) recursively. At \(r=0\) it is the atomic diagram. At \(r>0\) it consists of this diagram and the **set** of signatures \(T_{r-1}(n,k+1,w)\) of every one-subset extension. Precisely, to choose the next subset, split each cell \(v_b\) into \(w_b\) outside and \(w_{b+2^k}\) inside, with
\[
w_b+w_{b+2^k}=v_b,\qquad 0\le w_b\le v_b.
\]
This is an exhaustive, duplication-free enumeration of extension *orbits*. The recursion is logically complete: by induction on \(r\), two tuples have the same \(T_r\) exactly when they satisfy the same formulas of rank at most \(r\) with the tuple as free parameters. Atomic formulas give the base; an existential quantifier depends on which rank-\((r-1)\) child types are realized, and a universal quantifier is its negation. Conversely, whenever two finite sets of child types differ, a characteristic formula for a missing type distinguishes them; such formulas exist by the induction hypothesis and finite branching. The root type is \(T_3(n,0,(n))\).

**Exact finite part.** Exhaustively evaluating this recurrence for every \(0\le n\le8\) gives the following number of *distinct rank-two types realized by single subsets*:

| Number of atoms \(n\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| Realized unary \(T_2\) types | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 7 | 7 |

The actual canonical root signatures are pairwise different for \(n=0,1,2,3,4,5\), and satisfy
\[
T_3(6,0,(6))=T_3(7,0,(7))=T_3(8,0,(8)).
\]
These are **exhaustive finite** statements, not extrapolations. The accompanying `checker.py` implements the recursion verbatim using Python integers, tuples, and exact sets; it checks the full canonical signatures, not just their counts. It also cross-checks all ten ordered size-pairs \(0\le n\le m\le3\) with a separate uncompressed three-round Ehrenfeucht–Fraïssé solver on individual subsets. The source is a self-contained finite certificate.

**Infinite tail.** For arbitrary \(n,m\ge8\), Duplicator wins the three-round game even in the richer Boolean-algebra language. After \(k\) moves, partition the ground atoms into the \(2^k\) Venn cells induced by the selected subsets. Maintain for each matched pair of cells that their sizes are exactly equal if below \(2^{3-k}\), and otherwise both at least \(2^{3-k}\). Initially there is just one cell and both cardinalities are at least \(8\). If a matched pair of parent cells has equal size below \(2t\), Duplicator copies Spoiler's split exactly. If both parent cells have size at least \(2t\), then a Spoiler split with one part smaller than \(t\) is answered by matching that small part exactly and putting the remaining atoms in the other part. If neither Spoiler part is smaller than \(t\), Duplicator splits the other parent into two parts each containing at least \(t\) atoms. These cases exhaust every split and maintain the invariant. Induction gives the invariant after all three moves. Then threshold \(1\) means corresponding Venn cells agree on emptiness, so all inclusion and equality statements among the chosen subsets agree. Duplicator wins.

Thus every \(B_n\) with \(n\ge8\) is rank-three equivalent to \(B_8\). The exact finite calculation connects \(B_6\) and \(B_7\) to this class. The computed unary-type refinement is asserted only for sizes six through eight; no all-size unary-type classification is needed for the theorem. All smaller sizes have different root signatures. This proves the displayed classification and its sharp cutoff.

## Verification

With Python 3 standard library only, run `python3 checker.py` in a directory containing the embedded file. Expected output:

```text
BOOLEAN_INCLUSION_RANK3_OK unary_type_counts=1,2,3,4,5,6,7,7,7 tail=6=7=8 direct_pairs=10
```

The finite checker evaluates all weak compositions of the ground-atom count into the relevant \(2^k\) Venn cells and all compatible splits. No randomized testing, floating-point tolerance, or arbitrary search timeout is involved. It does **not** enumerate infinite sizes: the written threshold strategy proves the infinite tail.

## Relationship to prior work

Kurilić's 2026 work on products of chains studies complete theories, model classes and model-theoretic invariants of fixed finite products of chains, and motivates asking quantitative, bounded-rank questions in these families. In particular, the present powerset posets are variable-length products of two-element chains. Inspection of the full preprint (Theorem 1.1, Section 4, Section 6, and Section 7) reveals no bounded-rank threshold statement: its first-order definability of a fixed number of chain factors uses formulas of unrestricted quantifier rank. These facts do not imply the exact three-round equivalence classes.

A previously published exact atom-visibility theorem for Boolean algebras in the **functional** signature states the rank-\(q\) cutoff \(2^q\). Its quantified language includes Boolean operations as basic symbols, unlike this theorem's strict inclusion-only language. It implies a convenient upper bound \(8\) at rank three (also proved independently above), but it neither proves nor contradicts the sharp cutoff \(6\). The full functional-language theorem also distinguishes \(B_6\) and \(B_7\) at rank three, whereas the pure-order language cannot.

The general Ehrenfeucht–Fraïssé theorem justifies the language-to-game translation and is not a result about the numeric cutoff. No claim of historical uniqueness is made.

## Limitations

This is a bounded-rank classification inside one natural family. The sharp finite cases rely on a deterministic, fully specified finite recursion and reproducible checker rather than a short hand-written list of separating formulas. The primary 2026 products-of-chains preprint and the closest published full-signature Boolean-algebra result were inspected in full. Earlier specialized sources on Boolean-lattice order reducts could still overlap, and the finite cases have a reproducible computational certificate instead of a short manually enumerated list of separating formulas. No independently performed mathematical or historical-priority review is asserted.

## References

1. Miloš S. Kurilić, *Model Theory of Products of Chains*, arXiv:2610.24683, first submitted 17 October 2026, https://arxiv.org/abs/2610.24683.
2. *Sharp atom-visibility threshold for finite Boolean algebras*, 2026 published research record, published scientific record 938cb5f89dc7 (the functional Boolean-algebra signature).
3. Ehrenfeucht–Fraïssé games, nLab, https://ncatlab.org/nlab/show/Ehrenfeucht-Fra%C3%AFss%C3%A9%2Bgames (general game characterization).
