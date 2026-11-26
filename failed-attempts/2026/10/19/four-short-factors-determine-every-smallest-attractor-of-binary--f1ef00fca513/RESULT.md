# Four short factors determine every smallest attractor of binary two-run powers

## Finding
For integers \(a,b,m\ge2\), let
\[
W=(0^a1^b)^m,\qquad p=a+b.
\]
Positions are indexed from \(0\) to \(mp-1\). Every smallest string attractor of \(W\) belongs to exactly one of two families:
\[
\mathcal L=\{\{ip+a-1,(j+1)p-1\}:0\le i<m,\ 0\le j<m-1\},
\]
\[
\mathcal F=\{\{ip+a,jp\}:0\le i<m,\ 1\le j<m\}.
\]
Both families have \(m(m-1)\) members and are disjoint. Thus the minimum attractor size is \(2\) and the total number of smallest attractors is
\[
\boxed{2m(m-1)}.
\]
Moreover, **a two-position subset of \(W\) is a string attractor if and only if it hits an occurrence of each of the four factors \(0\), \(1\), \(01\), and \(10\)**. The four-factor certificate works independently of the run lengths.

## Assumptions and scope
A *string attractor* of a finite word \(W\) is a set of positions \(\Gamma\) such that, for every nonempty contiguous factor \(f\) of \(W\), some occurrence interval of \(f\) in \(W\) intersects \(\Gamma\). Each occurrence is a closed integer interval of consecutive positions. Only ordinary contiguous factors are considered, not circular factors or scattered subsequences. The alphabet is binary, both constant-run lengths are at least two, and there are at least two complete periods. Every quantifier in the classification ranges over these parameters; the exceptional shorter-run and single-period regimes are not included.

For \(0\le i<m\), the first and last zero positions of block \(i\) are \(ip\) and \(ip+a-1\), and the first and last one positions are \(ip+a\) and \((i+1)p-1\). A two-position attractor must select one zero and one one because both unary factors \(0\) and \(1\) occur.

## Proof
**Necessary four-factor conditions.** The factor \(01\) occurs exactly at the within-block boundaries \(\{ip+a-1,ip+a\}\), for \(0\le i<m\). The factor \(10\) occurs exactly at inter-block boundaries \(\{(i+1)p-1,(i+1)p\}\), for \(0\le i<m-1\). Suppose a two-position set intersects an occurrence of each of \(0\), \(1\), \(01\), and \(10\). It consists of one zero position and one one position. To meet \(01\), either its zero is the last zero of a block or its one is the first one of a block. To meet \(10\), either its one is the last one of a nonterminal block or its zero is the first zero of a noninitial block. Because \(a,b\ge2\), first and last positions within either constant run are distinct. Hence the only viable combinations are precisely \(\mathcal L\) and \(\mathcal F\). It remains to show every such pair meets every factor.

**Sufficiency for \(\mathcal L\).** Fix \(\{ip+a-1,(j+1)p-1\}\in\mathcal L\). Every all-zero factor of \(W\) has an occurrence in block \(i\) ending at \(ip+a-1\); every all-one factor has an occurrence in block \(j\) ending at \((j+1)p-1\). Thus unary factors are covered.

Take a mixed factor \(f\) of length \(\ell\). Its first letter-change determines a *unique* possible starting residue \(r\) modulo \(p\). Indeed, if \(f\) begins with \(0^u1\), then \(r=a-u\in[0,a-1]\); if it begins with \(1^v0\), then \(r=p-v\in[a,p-1]\). All occurrence starts are therefore
\[
r+kp,\quad 0\le k\le K:=\left\lfloor\frac{mp-r-\ell}{p}\right\rfloor,
\]
where \(K\ge0\), and every integer \(k\) in this range gives an occurrence by periodicity.

First suppose \(\ell\ge p-r\). We show that one occurrence meets the designated last-one position \(t=(j+1)p-1\). If \(K\ge j\), the occurrence starting at \(r+jp\) contains \(t\), since its end is at least \((j+1)p-1\). If \(K<j\), use the final occurrence, starting at \(r+Kp\). Its end is at least \((m-1)p\) because the unused terminal slack \(mp-r-Kp-\ell\) is less than \(p\). But \(r+Kp\le r+(j-1)p<t<(m-1)p\), so its interval also contains \(t\).

Now suppose \(\ell<p-r\). This cannot occur if \(f\) starts with ones: the first \(1\)-to-\(0\) change would require \(\ell\ge p-r+1\). Hence \(f\) begins with zeros. The first \(0\)-to-\(1\) change means \(\ell\ge a-r+1\). Thus the occurrence starting at \(r+ip\) contains the last zero \(ip+a-1\) and ends strictly before \((i+1)p\). It is a valid occurrence even when \(i=m-1\). Therefore every mixed factor meets one of the two chosen positions.

**Sufficiency for \(\mathcal F\).** Reverse \(W\) and complement its bits. The resulting word is \((0^b1^a)^m\), so this bijection preserves the stipulated parameter domain and the property of being an attractor. Under the position reflection, an \(\mathcal F\) pair becomes an \(\mathcal L\) pair for this transformed word: its first-one position becomes a last-zero position, and its noninitial first-zero position becomes a nonterminal last-one position. Sufficiency therefore follows from the preceding argument.

**Optimality and count.** No singleton hits both one-letter factors \(0\) and \(1\). The two constructed classes contain only attractors, so the optimum is \(2\). The class \(\mathcal L\) contains \(m(m-1)\) distinct pairs; likewise \(\mathcal F\). They cannot overlap because \(a,b\ge2\): one class selects last positions in runs, the other first positions. The total is \(2m(m-1)\). Since the necessity argument used only the four short factors, and sufficiency proved every qualifying pair is a full attractor, the four-factor certificate is equivalent to the full definition in this restricted family.

## Verification
The standalone `verify.py` computes every factor of the finite word, collects the union of all positions covered by its occurrences, and tests every unordered position pair against every factor mask. It independently constructs the two asserted pair families from their displayed formulas. The two sets agree for all \(64\) parameter triples with \(2\le a,b,m\le5\), and for six additional asymmetric longer-run tests. It also checks the number \(2m(m-1)\) in every rectangular-grid case. Its recorded output is in `verification_output.txt`.

These exhaustive finite checks are corroboration; the preceding proof establishes the result for all integers in the scope.

## Relationship to prior work
Banbara, Bannai, Guo, Köppl, Mieno, and Okamoto examine **all smallest attractors** for Fibonacci, period-doubling, and Thue–Morse words, and motivate the count of optimal attractors as a finer measure than optimal size. Their family-specific results concern different words and do not imply the two-run power classification. Dvořáková and Hendrychová study string attractors of Rote and generalized pseudostandard words; the two antipalindromic boundary families analyzed in subsequent work include \((01)^n\) and \(0(1100)^{n-1}1\). Neither is the complete-period word \((0^a1^b)^m\) with \(a,b,m\ge2\). In particular, the alternating word \((01)^n\) is excluded by the run-length assumptions. The three-parameter complete-pair description and four-factor equivalence are not implied by either family statement.

A general algorithm for determining attractors of a finite word is not a closed classification of these optimal pair sets, although it could recompute any fixed case. The proof isolates the precise boundary-dependent structure needed for all parameters. No claim of novelty for the concept of string attractors or for the known minimum-cardinality bound of other periodic families is made.

## Limitations
The result counts position sets, not their orbit classes under rotations, and the finite word is not treated as cyclic. It does not cover \(a=1\), \(b=1\), or \(m=1\); there are different endpoint phenomena in those regimes. No independent scientific validation is claimed. The originality check cannot rule out an unindexed thesis or differently formulated older periodic-word classification. The finite verifier does not establish the theorem without the written all-parameter proof.

## References
1. M. Banbara, H. Bannai, Z. Guo, D. Köppl, T. Mieno, and Y. Okamoto, “The Smallest String Attractors of Fibonacci, Period-Doubling, and Thue–Morse Words,” arXiv:2602.16152v1 (first public 2026-02-18); full text arXiv:2602.16152v3, https://arxiv.org/html/2602.16152v3.
2. L. Dvořáková and V. Hendrychová, “String attractors of Rote sequences,” arXiv:2308.00850v1, https://arxiv.org/abs/2308.00850.
3. “All smallest attractors in two exceptional antipalindromic pseudostandard families,” published research record, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-all-smallest-attractors-in-two-exceptional-antipalindromic-pseud--fe2566e0098c/RESULT.md.
