# Almost-injective curling-number transforms of binary words with two marked positions

## Finding

For a nonempty finite binary word \(w=w_1\cdots w_n\), let \(\kappa(w)\) be the largest integer \(k\ge1\) for which \(w=xy^k\) for some possibly empty \(x\) and nonempty \(y\). Its **prefix curling-number transform** is
\[
C(w)=(\kappa(w_1),\kappa(w_1w_2),\ldots,\kappa(w_1\cdots w_n)).
\]
For \(n\ge2\), restrict \(C\) to the \(\binom n2\) binary words containing exactly two ones. Encode a source uniquely as \(w(a,b,c)=0^a1\,0^b1\,0^c\) with \(a,b,c\ge0\) and \(a+b+c=n-2\).

**Theorem (complete fibers).** Every fiber of this restricted transform has size at most two. The nontrivial fibers are exactly the unordered pairs of triples below; every other source is uniquely identified by its transform.

* \(n=2,3\): no nontrivial fibers.
* \(n=4\): \(\{(0,0,2),(2,0,0)\}\), \(\{(0,1,1),(1,1,0)\}\), and \(\{(0,2,0),(1,0,1)\}\).
* \(n=5\): \(\{(0,1,2),(1,1,1)\}\).
* \(n=6\): \(\{(2,1,1),(2,2,0)\}\).
* \(n\ge7\): precisely \(\{(n-4,1,1),(n-4,2,0)\}\) and \(\{(n-5,1,2),(n-5,2,1)\}\).

Thus the number \(I(n)\) of distinct output sequences is
\[
I(2)=1,\quad I(3)=3,\quad I(4)=3,\quad I(5)=9,\quad I(6)=14,\qquad
I(n)=\binom n2-2\ \ (n\ge7).
\]
For a uniformly sampled source of weight two and \(n\ge7\), the chance of ambiguous recovery from the entire transform is exactly \(8/[n(n-1)]\), the conditional Shannon entropy is exactly \(8/[n(n-1)]\) bits, and the optimal success probability of one-guess reconstruction is \(1-4/[n(n-1)]\).

## Assumptions and scope

The input alphabet is the labeled binary alphabet \(\{0,1\}\); the source length is fixed and known; exactly two symbols are ones; the complete ordered vector of curling numbers for **all nonempty prefixes** is observed. Equal outputs mean identical integer vectors, not just equal final curling numbers, histograms, or sets of factor values. Occurrences of repeated suffix blocks are contiguous. The empty source is excluded. All assertions cover every integer \(n\ge2\); no asymptotic inference is used to assert the finite classification.

## Proof

Define \(R_j=(1,2,\ldots,j)\) for \(j\ge1\) and let \(R_0\) be empty. For all \(a,b,c\ge0\), the full transform has the following explicit factorization:
\[
C(w(a,b,c))=R_a\,(1)\,R_b\,(s)\,T_c,
\qquad s=\begin{cases}2,&a\ge b,\\1,&a<b,\end{cases}
\]
where \(T_0\) is empty and for \(c\ge1\),
\[
T_c=(e,2,3,\ldots,c),\qquad
 e=\begin{cases}2,&b\ge1\text{ and }a\ge b-1,\\1,&\text{otherwise.}\end{cases}
\]
Here the notation \((e,2,3,\ldots,c)\) has just its first entry when \(c=1\).

**Suffix-power lemma.** Before the second one, a prefix ending in a run of \(k\ge1\) zeros has curling number exactly \(k\); a prefix ending in its sole one has curling number one. The prefix ending in the second one has curling number two exactly when \(a\ge b\). After that one, if its trailing zero run has length \(k\ge2\), the curling number equals \(k\); at its very first following zero the curling number is two instead of one exactly when \(b\ge1\) and \(a\ge b-1\).

To prove the lemma, any repeated suffix block containing a one must have one one in each of two consecutive copies. More than two copies would require at least three ones, which do not exist. The two ones are separated by \(d=b+1\), forcing the repeated block length to equal \(d\). Their positions are \(p=a\) and \(q=a+b+1\) in zero-based indexing. A square of period \(d\) ending at index \(t\) contains both ones in aligned positions if and only if
\[
t-2d+1\le p\le t-d,\qquad p+d=q\le t.
\]
The intervening positions in the two copies are zeros, so these inequalities are also sufficient. At \(t=q\) they reduce to \(a\ge b\). At \(t=q+1\), they reduce to \(b\ge1\) and \(a\ge b-1\). Every other suffix power consists entirely of zeros, with exponent equal to its terminal zero-run length, which establishes the formula including the cases \(a=0\), \(b=0\), and \(c=0\).

**Inverting the formula.** Consider two triples of the same total length with equal output.

First, the initial digits determine the following disjoint classes: \(a\ge3\) begins with \((1,2,3)\); \(a=2\) or \((a,b)=(0,0)\) begins with \((1,2,1)\) whenever three entries exist; and \(a=1\) or \((a=0,b\ge1)\) begins with \((1,1)\). When \(a\ge3\), the initial increasing staircase ending at the first subsequent \(1\) recovers \(a\) exactly. The case \(a=2\) is distinguished from \((a,b)=(0,0)\) by their fourth or fifth entries: if \(b\ge1\), the fourth entries are \(1\) and \(2\); if \(b=0\), they share \((1,2,1,2)\) but differ at the fifth entry whenever it exists. Hence the sole cross-class collision here is \(\{(2,0,0),(0,0,2)\}\) at \(n=4\).

For \(a=1\) versus \(a=0,b\ge1\), comparison of the third entry leaves only two possibilities. If the second source has \(b\ge2\), the first must have \(b=0\); comparing the fourth and fifth entries forces \(\{(1,0,1),(0,2,0)\}\) at \(n=4\). Otherwise the second source has \(b=1\) and the first has \(b\ge1\). The fourth entry is \(2\), but the fifth, when present, forces the first source to have \(b=1\); the sixth then separates the two sources if it exists. The only remaining pairs are \(\{(0,1,1),(1,1,0)\}\) at \(n=4\) and \(\{(0,1,2),(1,1,1)\}\) at \(n=5\). This also covers short vectors lacking the quoted entries because their fixed total lengths are then exactly the listed small cases.

It remains to compare two sources with the same \(a\). After the prefix \(R_a(1)\), the case \(b=0\) starts with \(2\), while every \(b\ge1\) starts with \(1\); thus it cannot collide with another \(b\). The case \(b\ge3\) is recovered exactly from the initial increasing staircase \(R_b\) up to its first subsequent value below three, so it cannot collide with a different \(b\). For \(b=1\) versus \(b=2\), the third entry after \(R_a(1)\) is \(2\) for both only when \(a\ge1\). If \(a=1\), their next entries are respectively \(2\) and \(1\), so they differ. For \(a\ge2\), length equality requires comparing \((a,1,c)\) with \((a,2,c-1)\), with \(c\ge1\). Their suffixes after \(R_a(1)\) agree exactly when \(c\in\{1,2\}\): for \(c=1\) both equal \((1,2,2)\), for \(c=2\) both equal \((1,2,2,2)\), whereas for \(c\ge3\) the first has a \(3\) where the second still has \(2\). These are exactly the two stated same-\(a\) families, with the first existing when \(a\ge2\) and the second when \(a\ge2\). (For \(n=6\), only the first family is possible.)

The case split is exhaustive. Every named pair agrees by the factorization and every other pair is separated, proving the fiber theorem. Since every nontrivial fiber merges precisely two sources, \(I(n)\) equals \(\binom n2\) minus the number of named pairs. In the uniform case, two doubleton fibers give four ambiguous inputs; each such output has posterior probability \(1/2\) on its two inputs. This proves the three information-theoretic formulas.

## Verification

The included `verify_direct.py` independently computes the curling number of each nonempty prefix by searching all possible terminal repeated-block periods and multiplicities. For all \(2\le n\le40\), it compares those values against the explicit formula and groups all \(10{,}660\) two-one words into actual transform fibers. It confirms the complete stated collision list, the image-count formula, and the bound of two on every fiber.

The included `verify_inverse.py` independently groups formula outputs for every \(2\le n\le100\), checking all collisions and all image counts against the theorem. Files `direct_output.txt` and `inverse_output.txt` record the executions. Both programs use only Python 3 standard-library modules. Run them from a directory containing their files using `python verify_direct.py` and `python verify_inverse.py`.

The all-length claims are proved by the preceding suffix-power and inversion arguments. Finite computations are checks, not a substitute for those arguments.

## Relationship to prior work

Caveney, Dong, and Shallit (arXiv:2608.15670v1, August 16, 2026) introduce and use this direct-prefix curling-number transform to study simultaneous avoidance of repetitions in source and output, reporting sharp finite thresholds and infinite constructions. Their analyzed conditions are repetition constraints, rather than conditional injectivity or exact inverse fibers on the fixed-weight-two source class. Chaffin, Linderman, Sloane, and Wilks (arXiv:1212.6102, December 25, 2012; Journal of Integer Sequences 16 (2013), Article 13.4.3) develop curling numbers and enumerate binary sources by **one final curling number**, a strictly coarser observation than the complete prefix transform. The present claim is a fixed-weight inverse-reconstruction classification, not a theorem about power avoidance, general binary final-curling statistics, or the curling-number conjecture. The recent paper motivates the precise observation object; the two-marker subclass is the first fixed-weight family allowing repeated suffix blocks involving both binary symbols.

## Limitations

The classification requires both the exact input weight and the complete ordered vector of prefix curling numbers; it does not assert injectivity, a fiber bound, or a recovery algorithm for unrestricted binary words or for other Hamming weights. It treats two symbols as distinguished and uses the standard contiguous suffix-power notion, not scattered powers. The scientific priority assessment is bounded by the indexed and inspected sources; equivalent unindexed or unpublished results cannot be categorically excluded. No independent mathematical audit is claimed.

## References

1. G. Caveney, H. Dong, J. Shallit, *Repetition Avoidance in Curling-Number Transforms*, arXiv:2608.15670v1, initially public 2026-08-16, https://arxiv.org/html/2608.15670v1.
2. B. Chaffin, J. P. Linderman, N. J. A. Sloane, A. R. Wilks, *On Curling Numbers of Integer Sequences*, arXiv:1212.6102, first public 2012-12-25; Journal of Integer Sequences 16 (2013), Article 13.4.3, https://arxiv.org/abs/1212.6102.
3. OEIS A216955, *Number of binary sequences of length \(n\) and curling number \(k\)*, https://oeis.org/A216955.
