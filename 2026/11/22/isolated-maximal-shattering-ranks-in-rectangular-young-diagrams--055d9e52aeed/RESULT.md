# Isolated maximal shattering ranks in rectangular Young diagrams

## Finding

Fix an integer \(m\ge3\), set \(n=2m-2\), and let \(P=[m]\times[n]\) have the coordinatewise partial order. For every integer \(0\le k\le mn\), let \(\mathcal I_{m,k}\) be the set of its order ideals of cardinality exactly \(k\). Regard each ideal as a Boolean cell-membership concept on \(P\).

**Theorem (isolated maximal-rank shattering).** The maximum possible VC dimension across these ranks is \(m-1\). More precisely,

\[
\operatorname{VCdim}(\mathcal I_{m,k})=m-1
\quad\Longleftrightarrow\quad
k=\frac{m(m+1)}{2}-1+(h-1)(m-2)
\quad\text{for some }h\in\{1,\ldots,m\}.
\]

At each of these \(m\) distinct ranks there is **exactly one** shattered support of size \(m-1\); at every other rank there is none, and the VC dimension is at most \(m-2\). If the unique support corresponds to \(h\), it is

\[
S_h=\{(i,2m-i-1):1\le i<h\}\ \cup\
\{(i,m-i+1):h<i\le m\}.
\]

In particular, for \(m=6\) (the \(6\times10\) board), top-dimensional shattering occurs exactly at areas \(20,24,28,32,36,40\). For \(m\ge4\), the intervening ranks are genuine gaps of increasing length even though the number of Young diagrams by area is unimodal.

## Assumptions and scope

The two chains are labeled \([m]=\{1,\ldots,m\}\) and \([n]=\{1,\ldots,n\}\). A lower ideal \(I\subseteq P\) satisfies \(x\in I,\ y\le x\Rightarrow y\in I\). A query at \((i,j)\) returns \(1\) exactly if \((i,j)\in I\). A support \(S\subseteq P\) is *shattered* if every \(T\subseteq S\) is realized as \(I\cap S\) for some ideal \(I\in\mathcal I_{m,k}\). We count geometric cell supports, not orbits under a symmetry group. The proof is uniform for every integer \(m\ge3\) and every rank \(k\), including the empty and full ideals.

## Proof

**Step 1: the rank-restricted ideal trace test.** For any finite poset \(P\), write \(D(S)=\{x:\exists s\in S,\ x\le s\}\) and \(U(S)=\{x:\exists s\in S,\ x\ge s\}\). A query support for the family of size-\(k\) lower ideals is shattered precisely when it is an antichain and

\[
|D(S)|\le k\le |P|-|U(S)|.\tag{1}
\]

Indeed, comparability of two queried points prevents the pattern including the larger but excluding the smaller. The all-positive trace forces an ideal to contain \(D(S)\); the all-negative trace forces it to be inside \(P\setminus U(S)\). Conversely, if \(S\) is an antichain and (1) holds, each trace \(T\subseteq S\) can be obtained from a lower ideal between \(D(T)\) and \(P\setminus U(S\setminus T)\). The former lies in the latter; the former has size at most \(k\), while the latter has size at least \(k\). Any inclusion interval of finite ideals contains an ideal of every intermediate cardinality: repeatedly add a minimal element of the complement. Thus every trace is achieved. This general test is background; the novel conclusion below is its sharp aspect-ratio and rank rigidity.

**Step 2: an antichain of size \(m-1\) has at most \(m-1\) incomparable cells.** Every antichain in \([m]\times[n]\) uses distinct rows and distinct columns. Let \(S\) have \(m-1\) points and let \(h\) be its unique omitted row. Since all other rows contain a point of \(S\), every cell outside row \(h\) is comparable to some queried cell. In row \(h\), a cell whose column is already used by \(S\) is also comparable to its same-column queried cell. Consequently the number \(t\) of cells incomparable to *every* point of \(S\) satisfies

\[
0\le t\le n-(m-1)=m-1.\tag{2}
\]

Since \(S\) is an antichain, \(D(S)\cap U(S)=S\). The cells outside \(D(S)\cup U(S)\) are precisely those \(t\) incomparable cells. Hence

\[
|D(S)|+|U(S)|=mn+(m-1)-t.\tag{3}
\]

For (1) to hold, the left side of (3) must be at most \(mn\). By (2) this forces \(t=m-1\), so equality holds in (3) and the *only* feasible area is

\[
k=|D(S)|=mn-|U(S)|.\tag{4}
\]

**Step 3: equality uniquely determines the support.** List the queried points in increasing row order. Their columns are strictly decreasing. The cells of row \(h\) incomparable to every queried point form exactly the open column gap between the column used immediately before row \(h\) and the column used immediately after it; use the outer board boundaries if \(h=1\) or \(h=m\). Since \(t=m-1\), all \(m-1\) columns unused by the queried antichain must lie in this single gap. Therefore the \(h-1\) queried points above that row occupy the \(h-1\) largest columns, while the \(m-h\) points below occupy the \(m-h\) smallest columns. Strict decrease in the columns now forces precisely \(S_h\) displayed above, with no additional choices.

The down-closure of \(S_1\) has \((m-1)(m+2)/2=m(m+1)/2-1\) cells. Moving the missing row from \(h\) to \(h+1\) replaces one bottom-block point with one top-block point and increases the down-closure size by exactly \(m-2\). Thus direct summation of the occupied row widths gives

\[
|D(S_h)|=\frac{m(m+1)}2-1+(h-1)(m-2).\tag{5}
\]

Its incomparable row contains exactly the \(m-1\) unused columns, so (3) is an equality and \(|U(S_h)|=mn-|D(S_h)|\). By Step 1, \(S_h\) is shattered at exactly the rank in (5). Since \(m-2>0\) for \(m\ge3\), these are \(m\) distinct ranks and each has exactly one support of size \(m-1\).

**Step 4: no larger support.** An antichain has at most \(m\) members because all of its rows are distinct. If it has \(m\) members, every row contains a queried point and hence every cell is comparable to one, so the number of incomparable cells is zero. As before \(|D(S)|+|U(S)|=mn+m\), making (1) impossible. Larger antichains do not exist. This establishes the claimed exact VC-dimension equivalence and the top-support count for all areas.

## Verification

A standalone Python program, `verify.py`, separately enumerates all fixed-area Young diagrams and compares direct Boolean traces with cell-by-cell closure tests for all candidate top supports and all ranks at \(m=3,4,5\). It checks 19,307 support-rank instances. For \(m=6,7,8\), it uses independent grid-cell closure counts on 39,441 candidate supports (sizes \(m-1\) and \(m\)), verifying both the unique-support rank spectrum and absence of size-\(m\) shattered supports. Run `python3 verify.py` with the standard library only. These are finite diagnostic checks; the proof in Steps 1–4 establishes the all-integer theorem.

## Relationship to prior work

Melczer, Panova and Pemantle (2018) count Young diagrams of prescribed area inside rectangles and study the rank distribution and its asymptotics; their full-text statements do not determine VC traces or isolated top shattering ranks. Early (2019) studies rank-unimodality of order-ideal lattices of products of chains, again a different invariant. Kusch and Mészáros (2017) study shattering-extremal set families obtained from Sperner families, not fixed-area rectangular-ideal top-face supports. Iams, Johnston and Muth (2020) study adaptive membership searches for an unknown order ideal with a budget on positive answers, rather than the static VC traces of all ideals at a prescribed cardinality. An earlier square-board fixed-area bound addresses the central rank in square rectangles and does not yield this nonsquare isolated-rank classification. The general finite-poset ideal trace test is used as elementary background, not asserted to be new.

## Limitations

The theorem classifies exactly the top two candidate support sizes and the ranks at which the largest possible dimension occurs; it does **not** provide all lower-dimensional coefficients or exact VC dimensions at nonexceptional ranks. Finite verification is not an independent mathematical audit. Search cannot exclude unidentified equivalent results under other terminology.

## References

1. S. Melczer, G. Panova, R. Pemantle, *Counting partitions inside a rectangle*, arXiv:1805.08375, first public version 2018-05-22; https://arxiv.org/html/1805.08375v3.
2. E. Early, *Order ideals in a product of chains*, Australasian Journal of Combinatorics 73(3) (2019), 478–485; https://ajc.maths.uq.edu.au/pdf/73/ajc_v73_p478.pdf.
3. C. Kusch, T. Mészáros, *Shattering-extremal set systems from Sperner families*, arXiv:1710.03165, first public version 2017-10-09; https://arxiv.org/html/1710.03165v1.
4. A. Iams, H. Johnston, R. Muth, *Searching for quicksand ideals in partially ordered sets*, arXiv:2009.07348, first public version 2020-09-15; https://arxiv.org/html/2009.07348v1.
