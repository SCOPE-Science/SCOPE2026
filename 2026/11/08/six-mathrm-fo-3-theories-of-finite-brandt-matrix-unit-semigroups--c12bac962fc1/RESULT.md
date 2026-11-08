# Six \(\mathrm{FO}^{3}\) theories of finite Brandt matrix-unit semigroups

## Finding

For every integer \(n\ge1\), let \(B_n\) be the finite semigroup
\[
B_n=\{0\}\mathbin{\dot\cup}([n]\times[n]),\qquad
(i,j)(k,l)=\begin{cases}(i,l)&j=k,\\0&j\ne k,\end{cases}
\]
where multiplication by \(0\) is always \(0\). Regard \(B_n\) as a **relational** structure with equality, a named zero constant, and the ternary relation \(R(a,b,c)\) meaning \(ab=c\). In counting-free first-order logic using at most three reusable variables, at arbitrary quantifier depth,
\[
\boxed{B_m\equiv_{\mathrm{FO}^{3}}B_n\quad\Longleftrightarrow\quad
\min(m,6)=\min(n,6).}
\]
Thus there are exactly **six** theories represented by \(B_1,\ldots,B_6\); each theory has precisely the indicated minimum index size within this family. The minimum cardinalities of representatives in the family are \(2,5,10,17,26,37\). In particular \(B_5\not\equiv_{\mathrm{FO}^{3}}B_6\), but \(B_6\equiv_{\mathrm{FO}^{3}}B_n\) for every \(n\ge6\).

More sharply, at quantifier ranks \(0,1,2,3,4\), the numbers of different three-variable sentence theories in the family are respectively
\[
\boxed{1,\;2,\;3,\;5,\;6.}
\]
Rank four is the first rank that distinguishes \(B_5\) from \(B_6\), and ranks beyond four induce no further partition of this family. The least ranks distinguishing adjacent indices \(n\) and \(n+1\), for \(1\le n\le5\), are respectively \(1,2,3,3,4\).

## Assumptions and scope

The symbol \(0\) denotes the distinguished absorbing semigroup element, not a field zero. The notation \(\mathrm{FO}^{3}\) bounds the number of distinct variable names, **not** the depth of quantifier nesting; \(\equiv_r\) denotes agreement on every sentence with at most three variable names and quantifier rank at most \(r\). Counting quantifiers and functional multiplication are excluded. The classification compares members of the specified Brandt family; it does not assert that no smaller structure outside this family can realize the same theory.

## Proof

**1. Unrestricted equivalence for all indices at least six.** A nonzero pebbled matrix unit \((i,j)\) carries exactly two underlying index labels. Suppose that two three-pebble configurations over \(B_m,B_n\) have the same positions occupied by the zero element and the same equality partition of the row and column indices of all their nonzero pebbled elements. This condition preserves atomic equality, the named constant, and every atomic multiplication assertion, including repeated arguments and arguments equal to zero. Indeed, a product of two nonzero units is zero precisely when the second index of the first differs from the first index of the second; otherwise the product has the first index of the first and second index of the second.

When one pebble is moved, at most two nonzero matrix units remain stationary, so at most four distinct index labels are fixed. The moved pebble is either placed on zero or contributes at most two index labels, each old or new. If both base index sets have at least six elements, all prescribed equalities and inequalities can therefore be realized in either structure. The equality-partition invariant is maintained forever. The standard infinite three-pebble correspondence for finite-variable first-order logic then gives \(B_m\equiv_{\mathrm{FO}^{3}}B_n\) whenever \(m,n\ge6\).

**2. Exact finite orbit representation for the remaining comparisons.** Simultaneous permutations of the underlying index set act on \(B_n\) as automorphisms. Every assignment to the three variables is in exactly one orbit identified by the following data: which assigned elements are zero; and the equality partition of the at most six row/column endpoints of the other assigned elements. Canonicalize the labels by order of first occurrence. There are exactly
\[
1+3B_2+3B_4+B_6=1+6+45+203=255
\]
potential canonical patterns, where \(B_j\) in this single displayed counting identity denotes the **Bell number** (not the semigroup). A pattern is realized at index size \(n\) if and only if it uses no more than \(n\) different endpoint labels. There is no hidden realizability condition: each such equality partition may be represented by actual pairs of indices.

For a canonical state \(s\) and variable position \(i\), let \(E_{n,i}(s)\) be the set of canonical states obtainable by replacing the element assigned to variable \(i\). To compute this set exactly, first forget that element, retain the endpoint labels of the other two elements, and then insert either zero or an ordered pair of old and/or new labels. At most two new labels are needed. Discard precisely the patterns using more than \(n\) distinct labels. This accounts for **every possible replacement**, with no finite sampling.

Define a finite-rank invariant \(c_{n,r}(s)\). Its rank-zero value is the complete atomic diagram on the named zero and all three variable assignments. At each higher rank use
\[
c_{n,r+1}(s)=\left(c_{n,r}(s),\ \bigl(\{c_{n,r}(t):t\in E_{n,i}(s)\}\bigr)_{i=1}^{3}\right),
\]
renaming equal invariants by common integers across all compared structures. The use of **sets** instead of multisets corresponds to ordinary, counting-free existential quantification. Induction on formula formation proves that two assignments have the same rank-\(r\) invariant exactly when they agree on all formulas of quantifier rank at most \(r\) with the three given variable names, for the finite set of structures under consideration. In the reverse direction, each color is definable by a finite Boolean combination of atomic facts and quantified descriptions of predecessor colors. Thus unequal invariants are genuine logical separators, not merely game heuristics.

**3. Complete finite calculation.** The standalone program `verify_orbits.py` enumerates all 255 potential orbit patterns, computes their full atomic diagrams, constructs every replacement set, and iterates the displayed recurrence. Its exact ranks and cross-structure root colors are in `orbit_output.txt`. At the all-zero assignment, the ranks \(0\) through \(4\) induce successively \(1,2,3,5,6\) different classes for indices \(1\) through \(8\). All rank-four colors for indices \(6,7,8\) agree, and every color class has stabilized by rank four. The independent script `verify_direct.py` carries out the same refinement on every **concrete** triple of elements in \(B_1,\ldots,B_6\), without quotienting by automorphisms, and produces the identical root-color partition, as recorded in `direct_output.txt`.

The finite calculation is an exhaustive proof of separation for the **five adjacent finite comparisons** \(B_1/B_2,\ldots,B_5/B_6\), and of the first ranks of separation. Transitivity of logical equivalence and the unrestricted back-and-forth from Step 1 then give the entire claimed infinite classification. In particular, no finite computation is used to infer that untested, arbitrarily large indices behave similarly.

## Verification

Run `python3 verify_orbits.py` and `python3 verify_direct.py` using only the Python standard library. The programs assert the 255 canonical patterns, complete transition coverage, equality of orbit transition systems at sizes six through eight, stabilization of the common rank-color refinement, and the rank partition \(1,2,3,5,6\). The direct program separately enumerates all triples and all existential replacements for each size from one through six, giving independent agreement with the orbit computation. Both programs terminate with `ORBIT_CHECK_PASS` and `DIRECT_CHECK_PASS`, respectively; their full standard outputs are included.

There are two logically different verification steps: the **finite** lower bound uses exhaustive enumeration of the six specified finite semigroups, whereas the **uniform** upper bound follows from the mathematical coordinate-matching proof for all index sizes at least six.

## Relationship to prior work

Dawar and Holm [1, Section 2.3] give the general finite-variable pebble-game correspondence used here; they do not classify Brandt matrix units. Stronkowski and Trotta [2] investigate first-order axiomatizability for graphs of semigroup operations, with a different global/topological question. Gould and Quinn-Gregson [3, Section 4] describe Brandt semigroups and their simultaneous-index-permutation automorphisms, which justify the orbit labels, but they do not provide the sharp finite three-variable rank partition. The previously established **rank-three** comparison for these same finite Brandt semigroups has cutoff five; that weaker conclusion does **not** imply the present unrestricted three-variable result, because rank four newly distinguishes index sizes five and six. The present theorem determines the entire unbounded-depth tail and the exact stopping rank.

## Limitations

This result applies to the aperiodic Brandt semigroup of trivial maximal subgroup with named zero and a ternary multiplication **relation**. It does not classify general Brandt semigroups over nontrivial groups, languages with binary multiplication function symbols, two-variable or four-variable theories, counting logics, or arbitrary semigroups. The rank-four separation is certified by finite exhaustive state refinement and not by a short displayed separating sentence. The claim makes no assertion of independent validation or exhaustive historical priority beyond the stated comparisons.

## References

1. Anuj Dawar and Bjarki Holm, *Pebble Games with Algebraic Rules*, online preprint dated 2012-03-18 (https://bjarkiholm.com/publications/Dawar-Holm_2012_algebraicgames_pre-print.pdf); arXiv:1205.0913 first posted 2012-05-04, Section 2.3. https://arxiv.org/abs/1205.0913
2. Michał M. Stronkowski and Belinda Trotta, *Boolean topological graphs of semigroups: the lack of first-order axiomatization*, *Semigroup Forum* 89 (2014), 443–461, published online 2014-02-13. https://doi.org/10.1007/s00233-014-9582-3
3. Victoria Gould and Thomas Quinn-Gregson, *\(\aleph_0\)-categoricity of semigroups*, *Semigroup Forum* 99 (2019), 260–292, Section 4 (especially Proposition 4.1). https://doi.org/10.1007/s00233-019-10002-7
