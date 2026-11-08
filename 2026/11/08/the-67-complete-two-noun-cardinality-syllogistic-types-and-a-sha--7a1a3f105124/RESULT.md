# The 67 complete two-noun cardinality-syllogistic types and a sharp seven-element bound

## Finding

Consider the finite-model syllogistic language \(S^{\dagger}(\mathrm{card})\) with two named raw nouns \(p,q\), their complements, and its four atomic sentence forms: all, some, at least as many, and more than. A complete atomic theory records the truth value of every such sentence, with no additional sentence-level or noun-level connectives. Models have nonempty finite universes.

**Theorem.** Exactly **67** satisfiable complete atomic theories exist in this two-noun language. Every satisfiable (not necessarily complete) theory over these nouns has a model with at most **seven** elements, and seven is optimal. The complete theories have the following exact finite-spectrum distribution, where \(T_r=\{n\ge r\}\) and \(E_r=\{n\ge r:n\text{ is even}\}\):

| Complete-theory spectrum | Number of theories |
| --- | ---: |
| \(T_1\) | 4 |
| \(E_2\) | 6 |
| \(T_3\) | 16 |
| \(E_4\) | 9 |
| \(T_5\) | 20 |
| \(E_6\) | 4 |
| \(T_7\) | 8 |
| **Total** | **67** |

Consequently, the distribution of least model size \(1,2,\ldots,7\) is \(4,6,16,9,20,4,8\). The theorem also supplies an exact structural invariant for deciding whether two finite models have the same complete two-noun theory.

## Assumptions and scope

A model is \((W,P,Q)\), where \(W\) is nonempty and finite, and \(P,Q\subseteq W\) interpret \(p,q\). The nouns are \(p,\bar p,q,\bar q\), with complements interpreted relative to \(W\). For any nouns \(x,y\), the language contains \(\forall(x,y)\), \(\exists(x,y)\), \(\exists^{\ge}(x,y)\), and \(\exists^{>}(x,y)\), interpreted respectively as subset, nonempty intersection, cardinality at least, and cardinality greater than. There are \(4\cdot4\cdot4=64\) syntactically listed atomic sentences, with logical redundancies. Every false atomic sentence has a semantic negation that is itself an atomic sentence of this language; thus taking all true atomic sentences specifies one complete truth profile. Noun-level unions, intersections and sentence-level disjunctions are not allowed in the stated language.

Write the four Venn-cell sizes in the fixed order
\[
 a=|P\cap Q|,\quad b=|P\setminus Q|,\quad
 c=|Q\setminus P|,\quad d=|W\setminus(P\cup Q)|.
\]
These are arbitrary nonnegative integers with \(a+b+c+d>0\). Put \(u=a-d\) and \(v=b-c\). Define the *profile* of the model as the four-bit support of \((a,b,c,d)\), together with the four signs of \((u,v,u+v,u-v)\), where signs lie in \(\{-1,0,+1\}\).

## Proof

**1. Profiles characterize atomic truth.** Subset and nonempty-intersection sentences depend only on which of the four Venn cells are empty. For cardinality comparisons, the four noun sizes are \(a+b,c+d,a+c,b+d\). The differences between any two of these sizes belong, up to sign, to
\[
 b-c=v,\qquad a-d=u,\qquad (a+b)-(c+d)=u+v,\qquad
 (a+c)-(b+d)=u-v.
\]
Their signs determine all weak and strict comparisons. Conversely, all four cell-emptiness indicators are expressible by atomic nonempty-intersection sentences, and each of the four displayed sign comparisons is expressible by an appropriate comparison of two nouns (including equality as the conjunction of two opposite weak comparisons). Therefore two models satisfy exactly the same 64 atomic sentences **if and only if** their profiles agree.

**2. Possible profiles form a restricted \(B_2\) sign arrangement.** Consider the opposite Venn-cell pairs \((a,d)\) and \((b,c)\). Each pair has one of four support statuses: \(Z\), neither entry positive; \(F\), first only; \(S\), second only; or \(B\), both positive. For the first pair these respectively force \(u=0\), \(u>0\), \(u<0\), or allow any integer \(u\); analogously the second pair restricts \(v\). The sign vectors for \((u,v,u+v,u-v)\) are the 17 faces of the four-line central arrangement
\[
 u=0,\quad v=0,\quad u=v,\quad u=-v:
\]
there are eight open sectors, eight nonzero rays and one origin. Requiring the two prescribed support statuses restricts these faces as follows:

| Pair-status pattern | Number of status choices | Allowed sign faces per choice | Total |
| --- | ---: | ---: | ---: |
| \((B,B)\) | 1 | 17 | 17 |
| \((B,F),(B,S),(F,B),(S,B)\) | 4 | 7 | 28 |
| \((B,Z),(Z,B)\) | 2 | 3 | 6 |
| \((F,F),(F,S),(S,F),(S,S)\) | 4 | 3 | 12 |
| \((F,Z),(S,Z),(Z,F),(Z,S)\) | 4 | 1 | 4 |

The omitted \((Z,Z)\) case forces an empty universe. Every listed face is realizable by nonnegative integral cell counts: choose the prescribed signs of \(u,v\), with absolute sizes \((1,0)\) on an axis, \((1,1)\) on a diagonal, or \((1,2)\) or \((2,1)\) in an open sector. For each opposite pair, choose entries of minimal permitted size with the required difference. This proves the total \(17+28+6+12+4=67\). No identification of noun names is made: the four Venn regions and the two raw nouns are labelled.

**3. The exact minimum model sizes.** For a fixed status pair, realizing a difference \(u\) with minimum total \(a+d\) requires exactly \(|u|+2\) elements if the status is \(B\), and exactly \(|u|\) otherwise. The same holds for \(b+c\), with difference \(v\). Hence the smallest size of a model realizing a specified face and support is
\[
 N_{\min}=|u|+|v|+2\,\#\{\text{opposite pairs with status }B\},
\]
with \((u,v)\) selected as a lattice point of smallest \(\ell^1\)-norm on the prescribed sign face. The latter norm is \(0\) at the origin, \(1\) on an axis, \(2\) on a nonzero diagonal, and \(3\) in an open sector. All allowed support restrictions depend only on coordinate signs, so these minimum-norm representatives remain available in each allowed support case. Applying this rule to the five rows of the preceding table gives exactly the least-size distribution \(4,6,16,9,20,4,8\). In particular \(N_{\min}\le 4+3=7\).

An arbitrary satisfiable two-noun theory has a model. Replacing its four cell counts by the minimum representative of the **same complete profile** preserves every atomic sentence and yields a model of at most seven elements. This does not require the theory itself to contain every atomic sentence.

**4. Seven is sharp.** Consider the theory requiring all four Venn cells to be nonempty, together with \(\exists^{>}(p,q)\) and \(\exists^{>}(q,\bar q)\). The two comparison sentences mean \(v=b-c>0\) and \(u-v=a-d-b+c>0\). Hence \(b\ge2\) and \(a\ge3\), while \(c,d\ge1\); thus \(|W|\ge7\). The counts \((a,b,c,d)=(3,2,1,1)\) satisfy the theory, establishing optimality.

**5. Exact complete-theory spectra.** If \(u+v=0\) or \(u-v=0\), one of the two raw nouns has the same cardinality as its complement, so all models of that profile have even size. A minimum-size representative can be enlarged by two while preserving the profile: on a nonzero diagonal, increment the two positive cells corresponding to the two signed nonzero coordinates; at the origin, increment both entries of any present \(B\)-pair. This gives every larger even size, and no odd size. If neither diagonal equation holds, the sign face is either an axis or an open sector. Incrementing a positive cell belonging to the sole nonzero coordinate (axis), or the coordinate of strictly larger absolute value (open sector), enlarges the model by one without changing its profile; repeating obtains every larger size. Therefore each complete profile has spectrum exactly \(E_{N_{\min}}\) or \(T_{N_{\min}}\), respectively. The support-status counts yield the seven spectrum types and their multiplicities stated above.

## Verification

The standalone standard-library program `checker.py` constructs the profile catalogue using the 17-face sign arrangement and minimum Venn-cell representatives. Independently, it enumerates all integer quadruples of total size \(1\) through \(12\), computes all 64 atomic sentences directly from set membership and noun cardinalities, and checks that the direct truth vectors coincide exactly with profiles. The check covers \(1819\) quadruples, reconstructs all 67 profiles, verifies their seven minimum-size frequencies, checks each predicted spectrum against sizes through 12, and tests sharpness through six elements. Run with `python checker.py`; expected final marker: `TWO_NOUN_CARDINALITY_TYPES_OK`. The finite checks corroborate the full symbolic proof; they do not, by themselves, establish the infinite spectrum statements.

## Relationship to prior work

Jiang, *Finite Spectra of Syllogistic Logic with Cardinality Comparisons* (arXiv:2609.24902v1, first posted September 21, 2026), defines precisely this language and classifies spectra for an unrestricted supply of nouns as eventual ordinary or even tails (Theorem 3.16). That established global shape is used as context, **not claimed here**. The 67-profile count, the two-noun sharp small-model size seven, its extremal theory, and the complete spectrum multiplicities are a fixed-variable refinement not stated in the inspected manuscript. Moss, *Syllogistic Logic with Cardinality Comparisons* (2016), develops the finite-model proof theory; the available abstract advertises effective model construction, but does not resolve the particular two-noun exact classification. Moss and Topal, *Syllogistic Logic with Cardinality Comparisons, On Infinite Sets* (2017/2020), address infinite universes and do not directly supply the finite cardinality spectrum here.

## Limitations

The two raw nouns remain named, so the 67 count is **not** a count modulo swapping nouns or complementing either noun. The result concerns finite nonempty universes and the unextended base syllogistic. It does not classify the spectra of **all** incomplete two-noun theories, nor does it give a general bound for an unbounded number of nouns. The 2016 finite-model foundational chapter was not available as complete text for an exhaustive historical comparison; an equivalent fixed-fragment enumeration or small-model theorem could appear there or in unindexed literature. The result has received no independent audit.

## References

1. Ruiting Jiang, *Finite Spectra of Syllogistic Logic with Cardinality Comparisons*, arXiv:2609.24902v1, 2026-09-21, https://arxiv.org/abs/2609.24902 .
2. Lawrence S. Moss, *Syllogistic Logic with Cardinality Comparisons*, in *J. Michael Dunn on Information Based Logics*, 2016, doi:10.1007/978-3-319-29300-4_18.
3. Lawrence S. Moss and Selçuk Topal, *Syllogistic Logic with Cardinality Comparisons, On Infinite Sets*, arXiv:1705.03037, 2017; *Review of Symbolic Logic* 13 (2020), 1–22.
