# All maximizers of two length-two palindromic duplication spheres

## Finding
Let \(\Sigma\) be any alphabet of size \(q\ge2\), and let \(n\ge2\). For a word \(x\in\Sigma^n\), write \(D^2_{2,\mathrm{pal}}(x)\) for the set of **distinct** words obtainable by exactly two sequential palindromic duplications of a consecutive length-two block. The second duplication may use letters inserted by the first.

Then
\[
\max_{x\in\Sigma^n}|D^2_{2,\mathrm{pal}}(x)|
=\frac{n^2+5n-8}{2}.
\]
More precisely, equality holds **if and only if**
\[
x_i\ne x_{i+1}\qquad(0\le i<n-1).
\]
Thus the full set of maximizers consists of the proper \(q\)-colorings of a path on \(n\) vertices. Its cardinality is exactly
\[
q(q-1)^{n-1}.
\]
For an independent uniform \(q\)-ary source, the probability of attaining the maximal two-error sphere is therefore \(((q-1)/q)^{n-1}\).

## Assumptions and scope
Indices of words and operation starts are zero-based. Given any word \(y\) of length at least two, define
\[
T_i(y)=y_0\cdots y_{i+1}\,y_{i+1}y_i\,y_{i+2}\cdots y_{|y|-1},
\qquad 0\le i\le |y|-2.
\]
Thus \(T_i\) copies the ordered pair \((y_i,y_{i+1})\), reverses it, and inserts it directly after that pair. A two-step history is \((i,j)\) with \(0\le i\le n-2\) and \(0\le j\le n\), producing \(T_j(T_i(x))\). We count output **words**, not histories.

The alphabet is arbitrary (no field or complement is required). Length-two duplications are fixed, and both operations are legal on the current word. The result does not concern tandem duplication, arbitrary insertions, or other duplication lengths.

## Proof
**Step 1: a canonical exhaustive list of histories.** Fix a source word \(x\). For each \(0\le s\le n-2\), define the canonical history types
\[
A_s=(s,s),\qquad B_s=(s,s+1),\qquad C_s=(s,s+2).
\]
When \(s\le n-3\), also define
\[
D_s=(s,s+3),\qquad E_s=(s+1,s).
\]
Finally, for \(s+2\le r\le n-2\), define
\[
R_{s,r}=(s,r+2).
\]
A history label denotes its output under the two \(T\)-operations. Every legal history gives the same output as one of these canonical histories. Indeed, when the second start \(j\) lies from \(i-1\) through \(i+3\), the history is one of the five listed local types (the case \(j=i-1\) is \(E_{i-1}\)). If \(j\le i-2\), the operations act on disjoint original two-letter blocks and commute; moving the left operation first gives \(R_{j,i}\). If \(j\ge i+4\), its source is the original pair beginning at \(r=j-2\), disjoint from the original pair beginning at \(i\), and the history already is \(R_{i,r}\). The commutation follows directly by inserting the two disjoint reversed pairs at their original positions; it does not depend on the letters of \(x\).

The total number of canonical labels is
\[
3(n-1)+2(n-2)+\binom{n-2}{2}
=\frac{n^2+5n-8}{2},
\]
with the usual convention that the binomial term vanishes when \(n=2\). This proves the universal upper bound without assuming that canonical outputs are distinct.

**Step 2: injectivity for sources with unequal neighbors.** Suppose \(x_i\ne x_{i+1}\) at every adjacent pair. In the output of any canonical history whose first subscript is \(s\), the **first** pair of equal neighboring letters occurs at output positions \(s+1,s+2\). To see this, every listed output begins with the source prefix through \(x_{s+1}\), followed immediately by an extra copy of \(x_{s+1}\), while all earlier neighboring pairs are original and unequal. Consequently canonical histories belonging to different \(s\) cannot agree.

For a fixed \(s\), it remains to distinguish the five local types and the disjoint types. The following exhaustive comparison table gives, for each pair of **different** types, an output position \(p\) at which their respective letters are \(x_u\) and \(x_v\) with \(|u-v|=1\). Hence they disagree. The variable \(r\) satisfies \(s+2\le r\le n-2\), and for the last row \(r<t\). A row involving \(D_s\) or \(E_s\) is used only when that type exists.

| Types compared | Output position \(p\) | Original indices \((u,v)\) |
|---|---|---|
| \(A_s,B_s\) | \(s+3\) | \((s,s+1)\) |
| \(A_s,C_s\) | \(s+4\) | \((s+1,s)\) |
| \(A_s,D_s\) or \(A_s,E_s\) | \(s+4\) | \((s+1,s+2)\) |
| \(B_s,C_s\), \(B_s,D_s\), or \(B_s,E_s\) | \(s+3\) | \((s+1,s)\) |
| \(C_s,D_s\) or \(C_s,E_s\) | \(s+5\) | \((s+1,s+2)\) |
| \(D_s,E_s\) | \(s+6\) | \((s,s+1)\) |
| \(A_s,R_{s,r}\) | \(s+4\) | \((s+1,s+2)\) |
| \(B_s,R_{s,r}\) | \(s+3\) | \((s+1,s)\) |
| \(C_s,R_{s,r}\) | \(r+4\) | \((r,r+1)\) |
| \(D_s,R_{s,r}\) or \(E_s,R_{s,r}\) | \(s+5\) | \((s+2,s+3)\) |
| \(R_{s,r},R_{s,t}\) with \(r<t\) | \(r+4\) | \((r+1,r+2)\) |

Each entry follows by substituting the two operation starts into the definition of \(T\), retaining the indices of the original source letters rather than their values. For example, \(C_s\) inserts two further letters near \(s\), whereas \(R_{s,r}\) duplicates the original block starting at \(r\): at output position \(r+4\) their respective original indices are \(r\) and \(r+1\). Likewise, in the last row, the earlier second duplication gives original index \(r+1\) where the later one gives \(r+2\). The table exhausts every unordered pair within a fixed \(s\). Thus all canonical outputs are distinct, and the upper bound is attained.

**Step 3: necessity.** Suppose some neighboring source symbols agree, \(x_s=x_{s+1}\). Then the distinct canonical histories \(A_s=(s,s)\) and \(B_s=(s,s+1)\) have the same output: both perform two duplications solely within the constant pair \(x_sx_{s+1}\), replacing that pair by six identical copies of its symbol and leaving all other source letters unchanged. Hence the canonical list is not injective and the sphere size is strictly below the bound. This proves the stated equivalence.

**Step 4: counting.** The first source letter has \(q\) choices. Each subsequent letter must differ from its immediate predecessor and therefore has \(q-1\) choices, independently of earlier choices. This gives \(q(q-1)^{n-1}\) maximizers and the claimed probability for a uniform source. \(\square\)

## Verification
Run the standalone Python 3 script `checker.py` (no third-party dependencies). It forms every exact-two descendant directly, tests the theorem for all words over alphabets of sizes \(2,3,4\) through lengths \(10,8,6\), respectively, and tests the canonical index templates at every source length from \(2\) through \(27\). In particular, its second component verifies symbolically that every two-step history belongs to the canonical list and that every distinct canonical template pair contains a position comparing adjacent original indices. The executed checks covered 17,337 labeled source words, and all assertions passed. The infinitely many source lengths and alphabet sizes are established by Steps 1–4, **not** by those finite tests.

## Relationship to prior work
Zabokritskiy (2026), Theorem 5.1, establishes the same maximum numerical two-duplication sphere size for all even block lengths, proving attainment by binary alternating source words; it does not state the full set or count of maximizers at block length two in the inspected theorem and associated discussion. The new assertion is the **if-and-only-if classification for arbitrary alphabets**, yielding many nonalternating maximizers as soon as \(q\ge3\) (for example, the word \(012\)). The canonical-template argument provides its own proof of both attainability and necessity.

Lenz, Wachter-Zeh and Yaakobi (2017/2018), Lemma 3, determine the size of the **single** palindromic length-two duplication sphere through the run lengths of the source. That does not determine all two-step sphere maximizers. Related exact binary two-error **code-size** computations concern packing families of source words rather than equality cases for the sphere of an individual word.

## Limitations
The characterization is specific to **exactly two** length-two palindromic duplications, although its maximum sphere size matches the already published general-even-length bound. It does not classify the full distribution of nonmaximum sphere sizes or prove similar classifications for block lengths greater than two. The claim is mathematically proved here, but no independent mathematical audit or definitive global historical-priority certification has been performed.

## References
- A. L. Zabokritskiy, *Coding for Multiple Reverse-Complement and Palindromic Duplications*, arXiv:2609.00779, first submitted 2026-09-01, especially Sections 2 and 5 and Theorem 5.1. https://arxiv.org/abs/2609.00779 ; https://arxiv.org/html/2609.00779
- A. Lenz, A. Wachter-Zeh and E. Yaakobi, *Bounds on Codes Correcting Tandem and Palindromic Duplications*, arXiv:1707.00052, first submitted 2017-06-30, Section 3.3, Lemma 3. https://arxiv.org/abs/1707.00052
