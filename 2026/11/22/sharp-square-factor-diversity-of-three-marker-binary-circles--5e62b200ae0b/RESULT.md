# Sharp square-factor diversity of three-marker binary circles

## Finding

Let \(w\) be a binary circular word of length \(n\ge3\) containing exactly three ones. A *circular square* is a distinct literal nonempty word \(XX\) appearing in the doubled word \(ww\) with \(2|X|\le n\); different occurrences of the same square count only once. Let \(Q(w)\) be the number of these square words. Write \(w\), up to rotation, as \(1 0^p1 0^q1 0^r\), where \(p,q,r\ge0\) and \(p+q+r=n-3\).

**Sharp extremal theorem.** For every \(n\ge25\), write \(n=3m+s\) with \(s\in\{0,1,2\}\). Then
\[
\boxed{\max_{|w|=n,\ |w|_1=3} Q(w)=
\begin{cases}
n-4+\lfloor m/2\rfloor,&s=0,\\
n-6+\lfloor(m+1)/2\rfloor,&s=1,2.
\end{cases}}
\]
The *only* maximizers are those for which the unordered triple of zero-gap lengths is
\[
\boxed{\{p,q,r\}=
\begin{cases}
\{m-2,m-1,m\},&s=0,\\
\{m-2,m-1,m+1\},&s=1,\\
\{m-2,m,m+1\},&s=2.
\end{cases}}
\]
Consequently, exactly two circular words up to rotation maximize \(Q\) at each \(n\ge25\), interchanged by reversal, and the sharp density converges to \(7/6\):
\[\lim_{n\to\infty}\frac{\max Q(w)}n=\frac76.\]

For \(3\le n\le24\), the exact sharp maxima, in increasing order of \(n\), are
\[
(1,1,3,3,4,6,6,7,8,10,10,11,13,13,14,17,16,17,20,20,21,24).
\]
The smallest length at which a binary circle with three ones has **more distinct circular squares than positions** is precisely \(n=30\): the gaps \((8,9,10)\) give \(Q(w)=31\). No circle of Hamming weight at most two can have more square factors than positions. Thus three is the smallest marked-symbol count that permits this strict inequality.

## Assumptions and scope

The word is oriented and considered up to cyclic rotation, but not up to reversal; square factors are *literal* and can straddle the chosen boundary. Only squares of total length at most the circumference \(n\) are counted. Zero gaps may be zero. The maximum is taken over indexed binary words with exactly three ones; since it is rotation-invariant, the same value applies to necklaces. The two rotation classes of maximizers are distinct because their three positive, unequal gaps occur in opposite cyclic orders.

The pointwise formula for the square-factor count of any three-marker circle is known in prior work listed below. The new claim is its **sharp constrained optimization**, the complete extremizer rigidity, the two-necklace classification, and the first above-circumference threshold. No novelty claim is made for the pointwise count itself.

## Proof

**Step 1. An exact arithmetic description of each count.** This step reconstructs the known pointwise count to make all assumptions and the optimization self-contained. Write the gap triple \((p,q,r)\) cyclically and its sorted values as \(0\le a\le b\le c\). Any square has an even number of ones. Because the circle contains only three ones and its factor length is at most \(n\), a square has either zero or two ones. Its zero-only possibilities are \(0^{2j}\), \(1\le j\le\lfloor c/2\rfloor\).

A square containing exactly two ones has root \(0^x1 0^y\) with \(x,y\ge0\), and square word \(0^x1 0^{x+y}1 0^y\). It occurs around a specified cyclic gap \(g\) between consecutive ones, whose preceding and following gaps are respectively \(L\) and \(R\), exactly when
\[
\max(0,g-R)\le x\le\min(g,L),\qquad y=g-x.
\]
Indeed the central gap must be exhausted; the two outside zero sections must fit inside the adjacent gaps. Conversely the inequalities display a contiguous occurrence of total length \(2(g+1)\le n\). Different central gaps with unequal lengths create differently spelled squares. For equal central gaps, the intervals of admissible root offsets must be unioned.

Elementary interval union, with cases based on equality of the sorted gaps, yields the following complete count:
\[
Q(w)=\left\lfloor\frac c2\right\rfloor+T(a,b,c),\qquad
T(a,b,c)=\begin{cases}
a+1,&a=b=c,\\
a+1+(2a-c+1)_+,&a=b<c,\\
a+1+\min(c+1,2a+2),&a<b=c,\\
2a+2+(a+b-c+1)_+,&a<b<c,
\end{cases}\tag{1}
\]
where \(t_+=\max(t,0)\). This reconstructs rather than claims priority over the pointwise classification.

**Step 2. The balanced distinct-gap candidate.** Put \(S=n-3\). In the strictly ordered case \(a<b<c\), let \(x=b-a\ge1\) and \(y=c-b\ge1\), so
\[S=3a+2x+y,\quad c=\frac{S+x+2y}{3}.\]
When \(c\le a+b+1\), equation (1) becomes
\[Q=n-2(x+y)+\lfloor c/2\rfloor.\tag{2}\]
For \(S\equiv0,1,2\pmod3\), respectively choose the smallest admissible positive difference pairs \((x_0,y_0)=(1,1),(1,2),(2,1)\). Since \(S\ge22\), they define nonnegative, strictly increasing, positive gaps \((a_0,b_0,c_0)\) with \(c_0\le a_0+b_0+1\). Their counts given by (2) are exactly the three formulas in the theorem.

For any other admissible positive pair \((x,y)\) with the same \(S\bmod3\), set \(h=x+y-x_0-y_0\). A smaller or equal sum is impossible, except at the displayed pair: at sum two the only pair is \((1,1)\), and at sum three the possibilities \((1,2)\), \((2,1)\) have different residues. Therefore \(h\ge1\). Writing \(\delta x=x-x_0\ge-1\), we have
\[
c-c_0=\frac{2h-\delta x}{3}\le\frac{2h+1}{3}.
\]
The integer floor satisfies \(\lfloor c/2\rfloor-\lfloor c_0/2\rfloor\le\lceil(2h+1)/6\rceil\). Thus (2) gives
\[
Q-Q_0\le-2h+\left\lceil\frac{2h+1}{6}\right\rceil<0\qquad(h\ge1).\tag{3}
\]
This proves strict optimality among all ordered distinct gaps satisfying the stated containment inequality.

**Step 3. Excluding every other gap pattern.** If \(a<b<c\) but \(c>a+b+1\), equation (1) gives
\[
Q=\lfloor c/2\rfloor+2a+2\le S-c/2+2<3S/4+2.\tag{4}\]
Here \(2a\le a+b=S-c\) and \(c>S/2\) were used.

For repeated gaps, equation (1) gives the following uniform bounds. If \(a=b=c\), then \(Q\le S/2+1\). If \(a=b<c\), the range \(c\ge2a+1\) gives \(Q\le S/2+1\), while \(c\le2a\) gives \(Q\le5S/6+2\), using \(c>S/3\). If \(a<b=c\), the range \(c\le2a+1\) gives \(Q\le5S/6+2\), while \(c\ge2a+2\), equivalently \(5c\ge2S+2\), gives \(Q\le4S/5+4/5\). Thus all repeated-gap cases satisfy \(Q\le5S/6+3\).

Meanwhile the balanced candidate from Step 2 has \(x_0+y_0\le3\) and \(c_0\ge S/3\), so
\[Q_0=S+3-2(x_0+y_0)+\lfloor c_0/2\rfloor\ge7S/6-4.\]
For every integer \(S\ge22\), this exceeds both \(5S/6+3\) and \(3S/4+2\). Equations (3) and (4) prove that the balanced strictly distinct gap triple is the unique sorted maximizer. Its six permutations form two distinct cyclic rotation classes. Substitution yields all displayed exact \(n\ge25\) formulas.

**Step 4. Remaining lengths and first above-circumference case.** For each \(3\le n\le24\), enumerate all ordered nonnegative triples \((p,q,r)\) with \(p+q+r=n-3\), evaluate (1) and maximize; the exact vector shown in the finding results. This finite arithmetic verification is exhaustive: all triples have \(0\le p\le n-3\), \(0\le q\le n-3-p\), and forced \(r=n-3-p-q\). The standalone checker also independently reconstructs all literal square words for all triples through \(n=36\).

For \(n\ge25\), the formula shows that a value strictly exceeding \(n\) requires \(\lfloor m/2\rfloor>4\) if \(n\equiv0\pmod3\), or \(\lfloor(m+1)/2\rfloor>6\) otherwise. The first possible length is \(n=30\), with the stated gaps and 31 squares. The small-length table excludes every earlier length.

Finally, a binary circle with zero or one ones has only unary squares. For exactly two ones, write its two cyclic zero gaps \(p\le q\). A mixed square of total length at most \(n=p+q+2\) must use the shorter central gap \(p\), because a root embracing the longer gap would have total length \(2(q+1)>n\) when \(q>p\). The \(p+1\) roots \(0^x1 0^{p-x}\), \(0\le x\le p\), are exactly the mixed squares; when \(p=q\) both possible gap locations give the same literal set. Hence its number of distinct squares is \(\lfloor q/2\rfloor+p+1\le n\). This proves the smallest-weight assertion.

## Verification

Run `python3 verify_circular_three_squares.py` with Python 3 and no dependencies. The program uses a first-principles scan of the doubled binary word for literal square factors, an independently constructed structural square set, and the arithmetic expression (1). It checks equality on all 7,140 ordered gap triples with \(3\le n\le36\), then enumerates every 669,920 ordered gap triple with \(3\le n\le160\) to check the complete finite maxima and all maximum-attaining permutations. It performs 300 additional deterministic longer-parameter bound checks and verifies that the first length with more square factors than positions is 30. The exact program output is embedded as `verification_output.txt`.

All finite tests passed. They are checks of the implementation and the small-length finite enumeration; the unrestricted mathematical assertion for all \(n\ge25\) rests on Steps 1–3, not on finite data or sampled checks.

## Relationship to prior work

The existing exact three-marker *pointwise* circular-square classification provides (1), as well as a mean and a limiting distribution over random three-marker words [3]. It **does not state or establish** the globally sharp maxima over fixed circumference, the only optimizing gap triples, the two oriented necklace classes, or the first case with more squares than positions. The new contribution solves this discrete extremal optimization; the pointwise formula itself is acknowledged as known and used transparently. The parameterwise theorem is stronger as an oracle for computing each fixed word, but its published statement does not resolve the global constrained maximum without the optimization argument above.

A published four-run family with two cyclic blocks of each symbol [4] has a sharp maximum around \(3n/4\), and does not cover the three-one family with three separate zero runs. Hamai [1] proves the unrestricted universal upper bound \(\lfloor3(n-\sigma)/2\rfloor\), while Charalampopoulos and collaborators [2] developed earlier unrestricted bounds and constructions. Those bounds permit values up to roughly \(3n/2\) and do not identify the three-one extremizers or their \(7n/6\) growth. Separate Abelian-square results use equality of letter multisets rather than literal half-words.

## Limitations

This is a fixed-three-one, literal, circular, length-at-most-circumference result. The complete pointwise count formula (1) predates this theorem, and the result should be regarded as a sharp optimization of that formula rather than a new factor classification. It does not address general Hamming weights, square *occurrence* multiplicities, or longer periodic factors. Historical priority remains subject to the possibility of unindexed equivalent extremal results. Only self-review has occurred; independent audit has not been performed.

## References

[1] R. Hamai, *An Asymptotically Tight Bound on the Number of Distinct Squares in Circular Words*, first publicly posted September 25, 2026, arXiv:2609.32084v1; revised v3 November 11, 2026. https://arxiv.org/abs/2609.32084

[2] P. Charalampopoulos, M. Mohamed, J. Radoszewski, W. Rytter, T. Waleń and W. Zuba, *Improved Bounds on the Maximum Number of Distinct Squares in Circular Words*, CPM 2026, DOI:10.4230/LIPIcs.CPM.2026.6, https://doi.org/10.4230/LIPIcs.CPM.2026.6

[3] *Exact circular-square counts and limiting distribution for binary words with three marked positions*, earlier technical result, exact pointwise claim (no public bibliographic identifier).

[4] *Exact square spectra and sharp maxima for four-run binary circular words*, published technical result, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-square-spectra-and-sharp-maxima-for-four-run-binary-circul--f790bfb03bb7/RESULT.md

[5] *Exact distinct-square counts and aggregate law for binary words with three ones*, published technical result on **linear** rather than cyclic factors, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-distinct-square-counts-and-aggregate-law-for-binary-words--9614b0d1e103/RESULT.md
