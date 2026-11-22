# Six-level hexagon Walsh spectrum and sharp recovery projection for the Heawood graph

## Finding

Let \(H\) be the Heawood graph, the point–line incidence graph of the Fano plane. It has fourteen vertices and twenty-one edges. Let \(\mathcal H\) be its set of twenty-eight distinct six-edge cycles, and write \(b_\gamma\in\mathbb F_2^{E(H)}\) for the edge-incidence vector of \(\gamma\in\mathcal H\). On functions \(f:\mathbb F_2^{E(H)}\to\mathbb C\), consider the unnormalized counting convolution

\[
(Tf)(x)=\sum_{\gamma\in\mathcal H}f(x+b_\gamma).
\]

**Theorem.** The complete Walsh multiplier spectrum of \(T\), with character multiplicities, is:

| Multiplier | Multiplicity |
| ---: | ---: |
| \(-8\) | \(229376\) |
| \(-4\) | \(458752\) |
| \(0\) | \(884736\) |
| \(4\) | \(344064\) |
| \(12\) | \(172032\) |
| \(28\) | \(8192\) |

Consequently \(T\) has rank \(1212416\), nullity \(884736\), and sharp smallest nonzero multiplier magnitude \(4\). Its nonzero spectral condition number in \(\ell^2\) is \(7\), and its Moore–Penrose inverse has \(\ell^2\)-operator norm \(1/4\).

Let \(W=\operatorname{ran}T\), and let \(Q\) be the Walsh spectral projection onto \(W\). Among **all** real or complex linear projections onto \(W\), without a translation-invariance assumption,

\[
\min_{R^2=R,\ \operatorname{ran}R=W}\|R\|_{\ell^1\to\ell^1}
=\min_{R^2=R,\ \operatorname{ran}R=W}\|R\|_{\ell^\infty\to\ell^\infty}
=\frac{121}{16}.
\]

The twenty-eight cycle vectors span the eight-dimensional binary cycle space \(C(H)\). Thus every multiplier of the reduced eight-dimensional transform occurs exactly \(2^{13}=8192\) times in the full twenty-one-dimensional transform. The reduced signed spectrum, in order, is \(-8:28\), \(-4:56\), \(0:108\), \(4:42\), \(12:21\), \(28:1\).

## Assumptions and scope

All graphs are finite, undirected, simple, and labelled only to define coordinates; the invariants are independent of the labelling. The Fano plane's points are the seven nonzero vectors of \(\mathbb F_2^3\), and its lines are the triples \(\{a,b,a+b\}\), for distinct nonzero \(a,b\). A point–line incidence is one edge of \(H\). Fourier transforms are **unnormalized**: \(\widehat h(s)=\sum_xh(x)(-1)^{s\cdot x}\); inverse transforms include the factor \(2^{-d}\). Function-space norms use counting measure. A six-cycle is counted once, not once per root or direction. No statement is asserted for other graphs or other cycle lengths.

## Proof

**1. Complete hexagon list.** Every simple six-cycle in \(H\) alternates three distinct Fano points \(a,b,c\) with the three distinct lines through \(ab\), \(bc\), and \(ca\). Those lines are distinct precisely when the three points are noncollinear, or equivalently \(a+b+c\ne0\). Conversely each such triple produces one simple six-cycle. Exactly seven of the \(\binom73=35\) point triples are collinear, yielding precisely twenty-eight cycles. The attached verifier reconstructs the same twenty-eight edge masks independently by generic graph walk enumeration (with uniqueness enforced by edge-mask sets).

**2. Eight-dimensional reduction.** Since \(H\) is connected, its binary Eulerian cycle space has dimension \(|E(H)|-|V(H)|+1=21-14+1=8\). Fix any spanning tree. The eight non-tree edges provide independent coordinates on this cycle space: a cycle-space vector with no non-tree edges is supported in a tree and hence zero. Conversely every choice of the eight non-tree edges determines a unique Eulerian vector using fundamental cycles. Write \(A\subseteq\mathbb F_2^8\) for the twenty-eight distinct compressed six-cycle vectors. The verifier also checks directly that their binary span has dimension eight.

For each character indexed by \(s\in\mathbb F_2^{21}\), its restriction to \(C(H)\) determines \(\lambda_s=\sum_{\gamma\in\mathcal H}(-1)^{s\cdot b_\gamma}\). Every character of \(C(H)\) extends to \(\mathbb F_2^{21}\) in exactly \(2^{13}\) ways. Hence it suffices to compute the \(256\) integer values

\[
L(u)=\sum_{a\in A}(-1)^{u\cdot a},\qquad u\in\mathbb F_2^8.
\]

**3. Exhaustive integer identity.** The attached standard-library `verify.py` constructs the Fano lines; separately enumerates the simple graph six-cycles and the noncollinear point triples; constructs a spanning tree; reconstructs each six-cycle from its eight chord coordinates; and evaluates all \(256\) sums above by direct signs. It obtains the complete multiplicity table

\[
\begin{array}{c|rrrrrr}
L&-8&-4&0&4&12&28\\\hline
\#&28&56&108&42&21&1.
\end{array}
\]

A separately implemented integer butterfly Walsh–Hadamard transform of the \(256\)-entry characteristic function of \(A\) agrees term by term with the direct sums. Both calculations are exhaustive over their respective finite index sets, not statistical sampling. Multiplication of these six counts by \(8192\) proves the asserted full spectrum and ranks. The maximum absolute multiplier is \(28\) and the minimum positive magnitude is \(4\), giving the sharp Hilbert-space bounds.

**4. The range projection and optimality.** Set \(p(u)=1\) if \(L(u)\ne0\) and \(p(u)=0\) otherwise. The inverse Walsh kernel on the cycle space is \(K(c)=g(c)/256\), where

\[
g(c)=\sum_{u\in\mathbb F_2^8}p(u)(-1)^{u\cdot c}.
\]

An exhaustive integer transform, separately checked by Parseval, yields the *entire* histogram

\[
\begin{array}{c|rrrrrr}
g(c)&-12&-4&0&4&8&148\\\hline
\#&56&42&28&21&108&1.
\end{array}
\]

The full projection kernel vanishes outside \(C(H)\); it equals \(K\) on \(C(H)\), so its \(\ell^1\) kernel norm is

\[
\|K\|_1=\frac{56\cdot12+42\cdot4+21\cdot4+108\cdot8+148}{256}=\frac{1936}{256}=\frac{121}{16}.
\]

Convolution by \(K\) attains this norm on \(\ell^1\) (test a point mass) and on \(\ell^\infty\) (test the signs of the reversed real kernel). For an arbitrary bounded projection \(R\) onto the translation-invariant range \(W\), average its conjugates over all binary translations. This gives a translation-commuting projection onto \(W\) of no larger norm, since translations are isometries. A translation-commuting projection onto a fixed Fourier-character span is uniquely the Walsh projection \(Q\): it acts as one on characters in \(W\), and zero on characters outside \(W\). Therefore no projection, even one without translation symmetry, has smaller endpoint norm. This proves both optimality assertions.

## Verification

Run `python3 verify.py` with Python 3.9 or later. No third-party library or downloaded data is required. The executable lists all twenty-eight hexagons twice by independent constructions, verifies the cycle-space and fundamental-cycle reduction, computes both exact reduced transforms, checks their complete histograms and Parseval identities, and computes the sharp projection norm. Its last output line must be `PASS`. A separate full \(2^{21}\)-entry integer Walsh transform was also performed as a cross-check; the embedded eight-dimensional certificate suffices for the theorem because the character-extension factor is proved above.

## Relationship to prior work

The 2010 study by Dejter identifies the Coxeter graph as the disjointness graph of the twenty-eight Heawood hexagons, but investigates a different graph-geometric transformation. Lawrence and Wilson (2019) study the Heawood graph's cycles, including its hexagon count and disjoint pairs, without claiming the signed incidence-vector transform. Standard references record the Heawood graph's ordinary fourteen-vertex adjacency spectrum; that is not the present Fourier spectrum on the Boolean group of twenty-one edge coordinates.

A seemingly nearby Fano-triple incidence support also has twenty-eight objects, but its seven-coordinate triple vectors have affine span dimension six, whereas the present six-cycle edge vectors have affine span dimension eight. Thus these supports are not related by an affine coordinate change that would transfer the entire Walsh spectrum. A previously unindexed equivalent calculation remains possible; the result is not independently audited.

## Limitations

The claim is exact for this single canonical graph only, and the finite certificate is exhaustive rather than a symbolic general family classification. The primal scientific theorem relies on the stated standard Fourier and cycle-space identities plus the fully reproducible 256-case integer calculation. Although relevant primary sources and related indexed results were compared, exhaustive literature priority cannot be certified. No claim of independent validation or external certification is made.

## References

1. Italo J. Dejter, *From the Coxeter graph to the Klein graph*, arXiv:1002.1960, initially submitted 2010-02-09, https://arxiv.org/abs/1002.1960.
2. Emille Davie Lawrence and Robin T. Wilson, *The Structure of the Heawood Graph*, arXiv:1907.11978, initially submitted 2019-07-27, https://arxiv.org/abs/1907.11978.
3. Andries E. Brouwer, *Heawood graph*, graph reference, https://aeb.win.tue.nl/graphs/Heawood.html.
