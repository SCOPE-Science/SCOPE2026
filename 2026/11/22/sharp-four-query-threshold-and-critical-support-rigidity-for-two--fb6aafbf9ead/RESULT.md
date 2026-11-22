# Sharp four-query threshold and critical-support rigidity for two equal-width windows

## Finding
Fix integers \(r\ge2\) and \(n\ge2r+1\). On the zero-based chain \([0,n-1]\), let \(\mathcal W_{n,r}^{(2)}\) be all sets
\[
W_{p,q}=[p,p+r-1]\cup[q,q+r-1],\qquad
0\le p,\quad p+r\le q,\quad q+r\le n,
\]
where intervals contain integer positions. The two length-\(r\) intervals are disjoint as sets; **adjacent** intervals are permitted. The Boolean query at a position asks if the position belongs to the unknown union. Then
\[
\boxed{\operatorname{VCdim}(\mathcal W_{n,r}^{(2)})=4\ \Longleftrightarrow\ n\ge3r+3.}
\]
Moreover, at the sharp onset \(n=3r+3\), there are **exactly two** four-element shattered supports, namely
\[
S=\{1,r,2r+1,2r+2\}\quad\text{and}\quad
\rho(S)=\{r,r+1,2r+2,3r+1\},
\]
where \(\rho(i)=3r+2-i\) is reflection of the chain. There are no five-element shattered supports at any length.

## Assumptions and scope
All coordinates and interval endpoints are integers and zero-based. Each concept consists of *exactly two nonoverlapping length-\(r\) intervals*, not at most two intervals and not arbitrary-length intervals. If the intervals are adjacent, their union is a single length-\(2r\) run; this is allowed. Nonempty concepts only. Shattering means all \(2^{|S|}\) coordinate labelings occur as intersections \(W\cap S\). The theorem concerns four-query onset and the unique critical extremal supports; it does **not** give the complete VC dimension below onset, a whole shattering polynomial, or an adaptive Littlestone dimension.

## Proof
**Universal upper bound four.** On any five increasing coordinates \(x_1<\cdots<x_5\), the trace \((1,0,1,0,1)\) requires at least three nonempty consecutive runs of selected coordinates. A union of two intervals, regardless of length, cannot realize it. Thus \(\operatorname{VCdim}\le4\).

**Necessary length for a shattered four-support.** Let \(x_1<x_2<x_3<x_4\) be shattered. Write
\[
L=x_1,\quad a=x_2-x_1,\quad b=x_3-x_2,\quad c=x_4-x_3,\quad R=n-1-x_4.
\]
The alternating trace \((0,1,0,1)\) needs a length-\(r\) window containing \(x_2\) but neither \(x_1\) nor \(x_3\), hence \(a+b\ge r+1\); the other window contains \(x_4\) and excludes \(x_3\), forcing \(R+c\ge r\). Likewise, \((1,0,1,0)\) gives \(b+c\ge r+1\) and \(L+a\ge r\). The all-positive trace requires two windows whose ordered distribution of the four query points cannot be \(1+3\) or \(3+1\), because those distributions contradict respectively \(b+c\ge r+1\) and \(a+b\ge r+1\). It must be \(2+2\); consequently \(1\le a,c\le r-1\). We have established
\[
1\le a,c\le r-1,\quad a+b\ge r+1,\quad b+c\ge r+1,
\quad L+a\ge r,\quad R+c\ge r.\tag{1}
\]
For the all-negative trace, two disjoint length-\(r\) windows must avoid the four queried points. Since the gaps between \(x_1,x_2\) and between \(x_3,x_4\) have lengths \(a-1,c-1<r\), these windows must fit in the three remaining zero gaps of lengths \(L\), \(M=b-1\), and \(R\). Thus either two distinct gaps among \(L,M,R\) each have length at least \(r\), or one gap has length at least \(2r\).

If \(L,R\ge r\), then (1) gives \(a+b+c\ge r+1+\max(a,c)\ge r+2\); hence \(n=L+a+b+c+R+1\ge3r+3\). If \(L,M\ge r\), then \(b\ge r+1\) and \(R\ge r-c\), giving \(n\ge r+a+(r+1)+c+(r-c)+1=3r+a+2\ge3r+3\). The case \(M,R\ge r\) is the reflection. If \(L\ge2r\) or \(R\ge2r\), (1) implies \(n\ge3r+4\) (use \(b\ge2\)); if \(M\ge2r\), it implies \(n\ge4r+2>3r+3\). This proves the necessary threshold.

**Rigidity at equality.** Suppose \(n=3r+3\). The equality cases just derived are exactly:

1. \(L=R=r\), \(a=c=1\), \(b=r\), giving \(S_0=\{r,r+1,2r+1,2r+2\}\).
2. \(L=r\), \(a=1\), \(b=r+1\), \(R=r-c\), \(1\le c\le r-1\), giving \(S_c=\{r,r+1,2r+2,2r+2+c\}\).
3. Reflections of case 2.

The trace \((0,1,1,0)\) eliminates \(S_0\): its first window, containing \(r+1\) but excluding \(r\), must start at least at \(r+1\); its second, containing \(2r+1\) but excluding \(2r+2\), must end no later than \(2r+1\). These inequalities contradict disjointness. For \(S_c\), the same trace requires a first start at least \(r+1\), a second start at least \(2r+1\), and a second end no later than \(2r+1+c\); hence \(c\ge r-1\). Thus only \(c=r-1\) survives and its reflection is the other candidate.

**Constructive sufficiency.** It remains to shatter \(S=\{1,r,2r+1,2r+2\}\) at \(n=3r+3\). For each four-bit label in the order of these coordinates, the table gives two window starts \(p,q\) achieving exactly that trace. Every row obeys \(0\le p\), \(p+r\le q\), \(q+r\le3r+3\) for all \(r\ge2\), and direct substitution gives the displayed trace.

| Trace | First start \(p\) | Second start \(q\) |
|---|---:|---:|
| `0000` | \(r+1\) | \(2r+3\) |
| `1000` | \(0\) | \(r+1\) |
| `0100` | \(r\) | \(2r+3\) |
| `1100` | \(0\) | \(r\) |
| `0010` | \(r+2\) | \(2r+3\) |
| `1010` | \(0\) | \(r+2\) |
| `0110` | \(2\) | \(r+2\) |
| `1110` | \(1\) | \(r+2\) |
| `0001` | \(r+1\) | \(2r+2\) |
| `1001` | \(0\) | \(2r+2\) |
| `0101` | \(r\) | \(2r+2\) |
| `1101` | \(1\) | \(2r+2\) |
| `0011` | \(r+1\) | \(2r+1\) |
| `1011` | \(0\) | \(2r+1\) |
| `0111` | \(r\) | \(2r+1\) |
| `1111` | \(1\) | \(2r+1\) |

Reflection maps this shattered support to the second candidate. For every \(n>3r+3\), the same 16 windows remain admissible within the enlarged chain, preserving all traces. This proves sufficiency, equality-case rigidity, and the theorem.

## Verification
The dependency-free `verify_two_windows.py` independently constructs all admissible start pairs and their integer membership masks. A run with Python 3 produced three successful markers: `WITNESS_AFFINE_PASS 15984 r_range_2_1000`, `EXHAUSTIVE_FOUR_SUPPORT_PASS 92099 r_range_2_7 critical_counts [(2, 9, 2), (3, 12, 2), (4, 15, 2), (5, 18, 2), (6, 21, 2), (7, 24, 2)]`, and `INDEPENDENT_RUN_SHAPE_PASS`. This exhausts all four-query supports over \(2\le r\le7\) and \(2r+1\le n\le3r+3\), while the affine-witness check tests \(2\le r\le1000\). The universal conclusion depends on the preceding inequalities and explicit affine table, not the finite sweep.

## Relationship to prior work
H. R. Johnson's 2021 study *Binary strings of finite VC dimension* treats substring families of an individual binary word and bounds their VC dimensions through one-run alternations (Theorem 5). It does not classify the fixed-size family of exactly two equal-width windows with separate start parameters.

Two accessible related results address respectively (a) single fixed-width windows on chains, with exact static coefficients and online dimension, and (b) *at most* two arbitrary-length intervals, with standard VC dimension four and a finite online-dimension table. Neither implies the new length threshold \(3r+3\), which depends on *both* exactly-two and equal-width restrictions, nor the two-support rigidity at the onset. The general four-point upper bound is standard and is not claimed as original.

## Limitations
The result is not a classification of three-query or lower supports, not an all-coefficient polynomial, and not an online-dimension theorem. It does not cover a model requiring at least one **zero between** the two length-\(r\) intervals; in this theorem two adjacent intervals are allowed. Historical priority under equal-duration bursts, rigid segmentation, and finite consecutive-ones system terminology is not guaranteed without further independent searching. Only the universal proof above establishes all values of \(r\); finite code checks alone would not suffice.

## References
1. H. R. Johnson, *Binary strings of finite VC dimension*, arXiv:2101.06490v1, first public 2021-01-16. https://arxiv.org/abs/2101.06490
2. *Exact online ranks and shattering polynomials of fixed-width intervals on finite chains*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-online-ranks-and-shattering-polynomials-of-fixed-width-int--8f87b8e9beef
3. *Finite online-shattering thresholds for unions of two intervals*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-finite-online-shattering-thresholds-for-unions-of-two-intervals--3374b1fb8ebf
