# Exact square spectra and sharp maxima for four-run binary circular words

## Finding

Let \(a,b,c,d\) be arbitrary positive integers, let \(n=a+b+c+d\), and let
\[
w=0^a1^b0^c1^d.
\]
A *circular square* is a **distinct literal word** \(XX\), with \(X\) nonempty and \(2|X|\le n\), that occurs as a contiguous factor of \(ww\). Denote the number of these squares by \(S_\circ(w)\). The number of circular squares containing both letters is exactly
\[
M(a,b,c,d)=
\begin{cases}
a+b,&a=c,\ b=d,\\
\min(b,d)+1,&a=c,\ b\ne d,\\
\min(a,c)+1,&a\ne c,\ b=d,\\
1,&a\ne c,\ b\ne d.
\end{cases}
\]
All these mixed-letter squares have a root conjugate to \(0^{\min(a,c)}1^{\min(b,d)}\). Thus the **exact count** is
\[
\boxed{S_\circ(w)=\left\lfloor\frac{\max(a,c)}2\right\rfloor+
\left\lfloor\frac{\max(b,d)}2\right\rfloor+M(a,b,c,d).}
\]
In particular, the sharp maximum over all circular binary words of length \(n\) with exactly four cyclic runs is
\[
\boxed{H_4(n)=
\begin{cases}
2,&n=4,\\
\lfloor3n/4\rfloor-1,&n\ge7\ \text{and}\ n\equiv3\pmod4,\\
\lfloor3n/4\rfloor,&n\ge5\ \text{otherwise}.
\end{cases}}
\]
Each maximum is attained by a specified four-run word in the proof.

## Assumptions and scope

The alphabet is precisely \(\{0,1\}\), and all four displayed run lengths are positive. Consequently, the circular word has exactly four cyclic changes of letter, and \(n\ge4\). The representative \(w\) is arbitrary up to cyclic rotation and letter complement. A square is counted once as a literal word, even if it appears at multiple positions; different conjugate squares are counted separately if their spellings differ. The square's *total* length is at most \(n\), including factors crossing the circular boundary. These conditions match the usual convention for distinct squares in circular words.

## Proof

**1. Transition limitation.** Any factor of the infinite periodic word \(w^\omega\) whose length is at most \(n\) has at most four changes of letter: the four cyclic transition boundaries recur every \(n\) positions. Let \(Y=XX\) be a mixed-letter square of total length at most \(n\). If \(X\) begins and ends with different letters, it has an odd number \(t\ge1\) of internal transitions and \(Y\) has \(2t+1\) transitions, so \(t=1\). If \(X\) begins and ends with the same letter, it has an even number \(t\ge2\), and \(Y\) has \(2t\) transitions, so \(t=2\). Hence \(Y\) has either three or four transitions, and the cyclic root \(X\) has exactly two changes. Such a root is a conjugate of \(0^p1^q\) for some positive \(p,q\).

**2. Three-transition mixed squares.** Here \(X\) has one internal transition. Up to the choice of the starting cyclic run, the complete list of possibilities and necessary/sufficient containment conditions is:

| Square | Containment condition |
|---|---|
| \((0^c1^b)^2\) | \(a\ge c\) and \(d\ge b\) |
| \((0^a1^d)^2\) | \(c\ge a\) and \(b\ge d\) |
| \((1^d0^c)^2\) | \(b\ge d\) and \(a\ge c\) |
| \((1^b0^a)^2\) | \(d\ge b\) and \(c\ge a\) |

For example, a factor \((0^p1^q)^2\) traversing the runs in the order \(0^a,1^b,0^c,1^d\) must exhaust the two interior runs, forcing \(q=b\), \(p=c\); the outer runs need only contain the corresponding initial and final portions, giving \(a\ge c\), \(d\ge b\). The other three rows follow by cyclic rotation and letter exchange. Conversely, each row's inequalities exhibit the factor directly. If neither pair of opposite runs is equal, exactly one row applies. If exactly one pair is equal, precisely two rows apply and spell distinct squares. If both pairs are equal, all four rows apply but reduce to precisely two distinct squares, \((0^a1^b)^2\) and \((1^b0^a)^2\).

**3. Four-transition mixed squares.** Here the first and last letters of \(X\) agree. One form of \(Y\) is
\[
0^u1^q0^{u+v}1^q0^v,\qquad u,v\ge1.
\]
Its two internal 1-runs exhaust the two circular 1-runs, forcing \(b=d=q\). Its middle 0-run is one of the two complete 0-runs, so \(u+v\) equals its length and the other 0-run must be at least that long. Thus \(u+v=\min(a,c)\), which has \(\min(a,c)-1\) positive ordered splits. All of these occur, and they are distinct because the leading zero-block length \(u\) differs. With 0 and 1 interchanged, the other form requires \(a=c\) and gives \(\min(b,d)-1\) distinct squares. The two forms have different endpoint symbols, so they are disjoint; they also cannot coincide with the three-transition squares. In summary, there are
\[
\mathbf1_{b=d}(\min(a,c)-1)+\mathbf1_{a=c}(\min(b,d)-1)
\]
four-transition mixed squares. Adding the cases in step 2 produces exactly \(M(a,b,c,d)\). All listed mixed squares are conjugates of the square of \(0^{\min(a,c)}1^{\min(b,d)}\); no other root or factor is possible.

**4. One-letter squares.** A factor consisting entirely of zeros is a square precisely when it is \(0^{2j}\) for \(1\le j\le\lfloor\max(a,c)/2\rfloor\); the same argument with ones gives \(\lfloor\max(b,d)/2\rfloor\) squares. There is no overlap with the mixed-letter squares. This proves the exact formula.

**5. Sharp maximum at each length.** Put \(p=\min(a,c)\), \(q=\min(b,d)\), \(A=\max(a,c)\) and \(B=\max(b,d)\), so \(n=p+q+A+B\). If both opposite pairs are unequal, \(M=1\), and
\[
S_\circ(w)=\lfloor A/2\rfloor+\lfloor B/2\rfloor+1\le\lfloor n/2\rfloor.
\]
If both are equal, write \(a=c=p\), \(b=d=q\) and \(m=p+q=n/2\). Then
\[
S_\circ(w)=m+\lfloor p/2\rfloor+\lfloor q/2\rfloor\le m+\lfloor m/2\rfloor=\lfloor3n/4\rfloor.
\]
Suppose exactly one pair is equal. By exchanging symbols if necessary, write \(a=c=p\), \(B=q+\delta\) and \(q=\min(b,d)\), where \(\delta\ge1\). Let \(\varepsilon_t\) equal 0 or 1 according to the parity of \(t\). Since \(n=2p+2q+\delta\), direct substitution gives
\[
3n-4S_\circ(w)=4p+\delta-4+2\varepsilon_p+2\varepsilon_{q+\delta}\ge3.
\]
Therefore \(S_\circ(w)<3n/4\). When \(n\equiv3\pmod4\), the left side is congruent to 1 modulo 4 and at least 3, so it is at least 5; hence \(S_\circ(w)\le\lfloor3n/4\rfloor-1\). For \(n\equiv3\pmod4\) and \(n\ge7\), the earlier two cases satisfy the same bound (the both-equal case is impossible for odd \(n\)). Thus all stated maxima are upper bounds, except that \(n=4\) has only \(0101\) up to rotation and gives two squares.

Sharpness is witnessed by the following positive quadruples, for integers \(k\) in the stated ranges:

| Length | \((a,b,c,d)\) | Attained count |
|---|---|---|
| \(n=4\) | \((1,1,1,1)\) | \(2\) |
| \(n=4k\), \(k\ge2\) | \((2,2k-2,2,2k-2)\) | \(3k\) |
| \(n=4k+2\), \(k\ge1\) | \((1,2k,1,2k)\) | \(3k+1\) |
| \(n=4k+1\), \(k\ge1\) | \((1,2k-1,1,2k)\) | \(3k\) |
| \(n=4k+3\), \(k\ge1\) | \((1,2k,1,2k+1)\) | \(3k+1\) |

This establishes the complete all-length extremal formula.

## Verification

Run `python3 check_circular_four_runs.py` using only the Python standard library. It enumerates all 5,985 positive run quadruples of total lengths \(4\) through \(21\), constructs every circular square by literal substring comparison in the doubled word, checks the full set of square words against the four-transition construction and the monochromatic and mixed counts separately against the formula, and independently compares the maxima at each length. A separate modulo-index, character-by-character square enumerator checks 300 seeded longer parameter tuples against the first implementation. All checks passed. These finite tests are corroboration, not a replacement for the infinite argument in the proof.

## Relationship to prior work

Amit and Gawrychowski (2017) initiated the extremal count for square factors of circular words and supplied general bounds and constructions. Charalampopoulos and collaborators (accepted 2025, CPM 2026) improved general bounds and studied Fibonacci constructions. Li and Song (first posted May 12, 2026) sharpened the universal upper bound, and Hamai (first posted September 25, 2026) proved the sharp universal \(\lfloor3n/2\rfloor\) upper bound. Their accessible main results concern arbitrary circular words, not the exact number or optimal count conditioned on precisely four cyclic binary runs. This classification is a stronger, explicitly parameterized restricted-family result; it is not a proof of any currently unresolved universal conjecture. Previous specialized enumerations of Abelian squares concern a weaker equality relation (equal letter multisets), and do not determine the number of ordinary squares proved here.

## Limitations

The formula requires exactly four cyclic runs over a binary alphabet and positive run lengths. It does not classify circular words with six or more cyclic runs, or count square occurrences with multiplicity, or include square factors longer than the circle's length. Its originality assessment is based on inspected accessible primary literature and indexed comparisons, not an exhaustive historical-priority guarantee. Independent validation has not been performed.

## References

1. M. Amit and P. Gawrychowski, *Distinct Squares in Circular Words* (2017), arXiv:1708.00639, https://arxiv.org/abs/1708.00639.
2. P. Charalampopoulos, M. Mohamed, J. Radoszewski, W. Rytter, T. Waleń and W. Zuba, *Improved Bounds on the Maximum Number of Distinct Squares in Circular Words*, CPM 2026, DOI:10.4230/LIPIcs.CPM.2026.6, https://drops.dagstuhl.de/storage/00lipics/lipics-vol369-cpm2026/html/LIPIcs.CPM.2026.6/LIPIcs.CPM.2026.6.html.
3. S. Li and Y. Song, *A Tighter Upper Bound for the Number of Distinct Squares in Circular Words* (2026), arXiv:2605.12215v1, https://arxiv.org/abs/2605.12215.
4. R. Hamai, *The Tight Upper Bound on the Number of Distinct Squares in Circular Words* (2026), arXiv:2609.32084v1, https://arxiv.org/abs/2609.32084.
