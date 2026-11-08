# Exact \(q+1\)-to-\(q\) transition for three-survivor multiset deletion codes

## Finding
Let \(q\ge2\) and \(n\ge q+2\) be integers. Write \(S_q(n,n-3)\) for the largest cardinality of a length-\(n\) code of unordered \(q\)-symbol multisets correcting exactly \(n-3\) deletions, so that three symbols remain. Then
\[
S_q(n,n-3)=
\begin{cases}
q+1,&q+2\le n\le2q,\\
q,&n\ge2q+1.
\end{cases}
\]
The left endpoint of the stated range is sharp: for every \(q\ge2\), a valid code of \(q+2\) words exists at \(n=q+1\). Thus the two transitions at \(n=q+2\) and \(n=2q+1\) cannot be shifted downward.

## Assumptions and scope
A multiset is a vector \(x=(x_0,\ldots,x_{q-1})\) of nonnegative integer multiplicities, with \(\sum_i x_i=n\). Deleting exactly \(n-3\) symbols yields any multiplicity vector \(z\le x\) coordinatewise with \(\sum_i z_i=3\). Unique decoding means no two distinct codewords can produce the same such \(z\). The alphabet is fixed and labeled; codewords themselves are unordered multisets, not sequences. Only the three-survivor regime and integers \(q\ge2\), \(n\ge q+2\) are classified here.

## Proof
**1. The overlap criterion.** For two codewords \(x,y\), set \(I(x,y)=\sum_{i=0}^{q-1}\min(x_i,y_i)\). A common three-element deletion output exists exactly when \(I(x,y)\ge3\): a common submultiset of size three can be chosen from their coordinatewise minimum, and conversely every common output is bounded by that minimum. Therefore a code is valid if and only if \(I(x,y)\le2\) for every distinct pair.

**2. Heavy versus light words.** Call \(x\) heavy if some \(x_i\ge3\), and light otherwise (all \(x_i\le2\)). For each heavy word, choose one coordinate \(i\) with \(x_i\ge3\). No two heavy words can choose the same coordinate: if they did, their overlap would be at least three. Hence there are at most \(q\) heavy codewords.

If \(x,y\) are light, then for each coordinate \(i\), because \(0\le x_i,y_i\le2\),
\[
\min(x_i,y_i)\ge x_i+y_i-2.
\]
Summing and using \(\sum_i x_i=\sum_i y_i=n\) gives \(I(x,y)\ge2n-2q\). Since \(n\ge q+2\), this is at least four and contradicts the required bound of two. Thus there is at most one light codeword. Altogether every admissible code has at most \(q+1\) words.

**3. The longer-block threshold.** A light word has total multiplicity at most \(2q\). When \(n\ge2q+1\), no light word exists, so the above argument gives \(S_q(n,n-3)\le q\). The \(q\) distinct pure words \(n e_0,\ldots,n e_{q-1}\), where \(e_i\) is the \(i\)-th unit vector, have pairwise overlap zero and attain \(q\).

**4. Attainment in the intermediate range.** If \(q+2\le n\le2q\), choose any light word \(u\) of total multiplicity \(n\). Such a word exists: fill successive coordinates with at most two symbols until the total is \(n\). Adjoin \(u\) to the \(q\) pure words \(n e_i\). Distinct pure words overlap by zero, and \(I(n e_i,u)=u_i\le2\); therefore the resulting \(q+1\) codewords are valid and meet the upper bound.

**5. Sharpness of the first endpoint.** At length \(n=q+1\), begin with the \(q\) pure words. Construct two further light words \(u,v\) with overlap exactly two.

For \(q=2m+1\) odd, index coordinates from zero to \(2m\) and set \(u_i=2\) for \(0\le i\le m\), zero otherwise; set \(v_i=2\) for \(m\le i\le2m\), zero otherwise. Their lengths are \(2(m+1)=q+1\), and they overlap only at coordinate \(m\), by exactly two.

For \(q=2m\) even, set \(u_i=2\) for \(0\le i<m\), set \(u_m=1\), and zero otherwise. Set \(v_i=2\) for \(m\le i<2m\), set \(v_{m-1}=1\), and zero otherwise. Their lengths are \(2m+1=q+1\), and their overlap is one at each of coordinates \(m-1\) and \(m\), totaling two. In either case, \(u\ne v\), each has multiplicity at most two in every coordinate, and each overlaps every pure word in at most two symbols. We obtain \(q+2\) valid words at \(n=q+1\), as asserted. This completes the proof.

## Verification
The self-contained Python checker `checker.py` verifies the overlap criterion directly by enumerating all three-symbol outputs for selected small parameters; it independently checks the explicit constructions for \(2\le q\le8\), both phase ranges, and the sharp lower-endpoint witnesses. It also exhaustively compares possible light-word pairs for \(q\le5\). Run `python3 checker.py` using only the Python standard library. These finite checks are consistency tests; the universal assertions follow from the inequalities and constructions in the proof.

## Relationship to prior work
Kreindel, Barouch Essayag and Zabokritskiy [1, Section 3.5, Theorem 9] give the same overlap criterion and a general bound \(S_q(n,n-3)\le q^2(n-2)/(n-q-1)\) for \(n\ge q+2\). That bound is generally not sharp, and its statement does not imply either exact value above. Their companion work [2] studies deletion-ball geometry and volume-based bounds rather than this exact all-alphabet, three-survivor extremum. Exact small-alphabet cases are consistent with the theorem, but do not imply the simultaneous statement for all \(q\ge2\). The improvement comes from separating codewords by whether any multiplicity exceeds two and enforcing a coordinate injection for the heavy class.

## Limitations
The result concerns only the regime with exactly three surviving multiset elements, not ordered-word deletions or more survivors. It determines the maximum code cardinality but does not classify all optimal codes up to alphabet relabeling. The construction at \(n=q+1\) proves sharpness of the range boundary, not the exact optimum at that shorter length. Historical priority remains subject to additional literature review; independent mathematical validation has not been performed.

## References
1. A. Kreindel, I. Barouch Essayag, A. L. Zabokritskiy, *Multiset Deletion-Correcting Codes: Bounds and Constructions*, arXiv:2601.05636v1 (first publicly available 2026-01-09), Section 3.5, Theorem 9. https://arxiv.org/html/2601.05636v1
2. A. Kreindel, I. Barouch Essayag, A. L. Zabokritskiy, *Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes*, arXiv:2603.18322v1 (2026-03-18), Sections 4–5. https://arxiv.org/html/2603.18322v1
