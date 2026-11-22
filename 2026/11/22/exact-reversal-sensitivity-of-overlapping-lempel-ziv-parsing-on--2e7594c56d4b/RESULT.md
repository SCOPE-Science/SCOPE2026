# Exact reversal sensitivity of overlapping Lempel–Ziv parsing on binary four-run words

## Finding
For every four-tuple of positive integers \(a,b,c,d\), set \(W=0^a1^b0^c1^d\), let \(W^{\mathrm R}\) be its reversal, and let \(z(W)\) be the number of phrases in its greedy overlapping Lempel–Ziv factorization (defined precisely below). Write \([P]\) for the indicator of a proposition \(P\). Then
\[
z(W)=3+[a>1]+[b>1]+[c>a]+[c>2a]+[d>b],
\]
\[
z(W^{\mathrm R})=3+[d>1]+[c>1]+[b>d]+[b>2d]+[a>c].
\]
Consequently the oriented reversal defect \(\Delta(W)=z(W)-z(W^{\mathrm R})\) satisfies \(|\Delta(W)|\leq3\), sharply. Its two extreme cases are *exactly*
\[
\Delta(W)=3 \iff a\geq2,\ b\geq2,\ c>2a,\ d>b,
\]
\[
\Delta(W)=-3 \iff c\geq2,\ d\geq2,\ b>2d,\ a>c.
\]
The smallest length at which \(|\Delta|=3\) is 12, with only \((a,b,c,d)=(2,2,5,3)\) and \((3,5,2,2)\) among positive four-run compositions. In particular, \(z(0^21^20^51^3)=8\) whereas its reversal has five phrases.

Choose \((a,b,c,d)\) uniformly from all positive compositions of \(n\) into four ordered parts. As \(n\to\infty\), the probabilities for \(\Delta=-3,-2,-1,0,1,2,3\), respectively, converge to
\[
\bigl(1/6,\ 1/12,\ 1/18,\ 7/18,\ 1/18,\ 1/12,\ 1/6\bigr).
\]
In particular, \(\Pr(|\Delta|=3)\to1/3\), \(\Pr(\Delta=0)\to7/18\), and \(\mathbb E|\Delta|\to13/9\).

## Assumptions and scope
The alphabet is \(\{0,1\}\). All four run lengths are *positive integers*. There are exactly four maximal constant-letter runs, starting with zero; starting with one gives the same results by exchanging symbols. At each unread position \(i\), greedy overlapping Lempel–Ziv parsing selects the longest nonempty prefix of the remaining suffix having an occurrence starting at some position \(j<i\). The occurrence may overlap the current phrase, and the source is compared in the **original word** (equivalently, a self-referential copy is permitted). If no nonempty match exists, one new character is emitted as a literal phrase. This is the \(z\) factorization, not the triple-coded LZ77 or LZ78 variant. No sentinel is appended. The four phrase counts and all strict inequalities use this convention throughout.

## Proof
**Step 1: exact greedy phrase count.** The initial zero run emits \(0\), followed by one phrase for its remaining zeros if and only if \(a>1\): after the first literal, an overlapping copy can produce all remaining zeros. The following first one run similarly emits the new literal \(1\), and a second one-run phrase if and only if \(b>1\).

It remains to count phrases starting at the third run \(0^c\) and continuing through \(1^d\). When that run starts, every occurrence of a zero starting earlier lies in the first zero run \(0^a\). If \(c\le a\), align the source to the last \(c\) zeros of that first run: one phrase copies \(0^c\) and \(\min(b,d)\) following ones. It cannot copy more than \(b\) ones, because the only earlier zero-to-one boundary is followed by precisely \(b\) ones. If \(d>b\), the remaining ones form one further phrase (by overlapping copying); otherwise parsing ends.

If \(c>a\), no prior occurrence contains \(a+1\) initial zeros before the third run begins. Thus the first phrase there copies exactly \(a\) zeros. For the remaining \(r=c-a\) zeros, two possibilities are exhaustive. If \(r\le a\), align a source in the first zero run with its end: the next phrase copies the remaining \(r\) zeros and then \(\min(b,d)\) ones, again followed by one additional phrase precisely when \(d>b\). If \(r>a\), the next phrase is exactly \(0^r\), copied by self-overlap from the already parsed zeros of the third run; it cannot include any one because no previously available source has \(r>a\) zeros immediately followed by a one. The final run then needs one phrase for up to \(b\) ones and a second if and only if \(d>b\). These are exactly the regimes \(c\le a\), \(a<c\le2a\), and \(c>2a\), contributing \(1+[d>b]\), \(2+[d>b]\), and \(3+[d>b]\) phrases after the first two runs. Adding their initial \(2+[a>1]+[b>1]\) phrases yields the first formula, including all equality boundaries.

**Step 2: reversal and extrema.** Since exchanging the symbols does not affect greedy phrase count, \(z(W^{\mathrm R})=z(0^d1^c0^b1^a)\). Apply Step 1 to obtain its displayed formula. The difference separates into independent terms:
\[
\Delta=A(a,c)+B(b,d),
\]
\[
A(a,c)=[a>1]-[c>1]+[c>a]-[a>c]+[c>2a],
\]
\[
B(b,d)=[b>1]-[d>1]+[d>b]-[b>d]-[b>2d].
\]
Direct partition into \(a<c\), \(a=c\), \(a>c\), with the one-unit boundary cases, gives \(-1\le A\le2\), and \(A=2\) exactly for \(a\ge2\), \(c>2a\), whereas \(A=-1\) exactly for \(c\ge2\), \(a>c\). Similarly \(-2\le B\le1\), with \(B=1\) exactly for \(b\ge2\), \(d>b\) and \(B=-2\) exactly for \(d\ge2\), \(b>2d\). Thus \(|\Delta|\le3\) and the two displayed equality classifications follow without cancellation or exceptions. In the positive case minimal parameters are \(a=b=2\), \(c=5\), \(d=3\); in the negative case \(c=d=2\), \(b=5\), \(a=3\). Both have total length 12, and strict inequalities force uniqueness at this length.

**Step 3: limiting law.** Under uniform positive compositions of \(n\), the scaled run-length vector converges to a uniform point in the four-dimensional simplex, equivalently a \(\operatorname{Dirichlet}(1,1,1,1)\) vector. This follows by counting lattice points in simplex regions, with tie and unit-length boundaries having negligible proportion. Writing the limit as four independent unit exponential random variables divided by their sum shows that \(U=a/(a+c)\) and \(V=b/(b+d)\) converge jointly to independent uniform variables on \((0,1)\). Away from boundaries \(A=-1\) when \(a>c\) (probability \(1/2\)), \(A=1\) when \(a<c\le2a\) (probability \(1/6\)), and \(A=2\) when \(c>2a\) (probability \(1/3\)). Independently, \(B=1,-1,-2\) with probabilities \(1/2,1/6,1/3\), respectively. Their convolution gives the seven probabilities displayed above. Summing \(|k|\) against them yields \(13/9\). This proves all asserted limits.

## Verification
Two standalone Python 3 programs accompany this statement. `verify_lz.py` directly implements greedy longest-previous-factor parsing with overlapping sources on 28,561 independent positive parameter quadruples (each run from 1 through 13), testing both orientations against the closed formula; `verify_counts.py` enumerates *every* positive composition of each length 4 through 30, checks reversal symmetry, locates the first extremizers, and checks the exact rational convolution and expected absolute defect. Recorded outputs are `verify_lz.out` and `verify_counts.out`. These finite tests are not the proof of the universal statements; Steps 1–3 are.

## Relationship to prior work
Bannai, Fujie, Guo, Inenaga, Nakashima, Puglisi and Urbina (first public arXiv version, February 16, 2026) study reversal sensitivity of \(z\) and establish an unbounded additive gap and a ratio approaching three on more complicated strings. Their LZ definition matches ours, but their results do not determine exact parsing for all binary four-run strings or their distribution. Shibata and Fujie (first public August 4, 2026) subsequently establish a \(\Theta(\log n)\) worst-case multiplicative reversal sensitivity for arbitrary strings, using bit-reversal block constructions; the exact bounded-four-run classification is a different statement and does not follow from that asymptotic theorem. Related indexed research on LZ77 overlap versus non-overlap parsing of de Bruijn cycles studies a different operation and input family, and its spectrum does not imply the formulas here. This classification thus isolates a fixed-run regime within a broader reversal-sensitivity problem.

## Limitations
The theorem applies only to binary words with exactly four maximal runs, the *overlapping longest-previous-factor* LZ convention, and uniform distribution on positive run-length compositions for the limit law. No claim is made for five or more runs, nonoverlapping parsing, triple-coded phrases, LZ78, arbitrary word distributions, or optimal compressed bit length. The originality comparison is best-knowledge and cannot exclude unindexed or unpublished equivalent formulas; the published general theorems address different quantifiers or objects. Verification is same-model and reproducible but not independently audited.

## References
1. H. Bannai, Y. Fujie, P. Guo, S. Inenaga, Y. Nakashima, S. J. Puglisi and C. Urbina, *Sensitivity of Repetitiveness Measures to String Reversal*, arXiv:2602.14385v1 (first public 2026-02-16); CPM 2026, LIPIcs 369, paper 17. https://arxiv.org/html/2602.14385v1 ; https://doi.org/10.4230/LIPIcs.CPM.2026.17
2. H. Shibata and Y. Fujie, *Sensitivity and Size Relationships of the Lempel–Ziv Factorization*, arXiv:2608.03351 (first public 2026-08-04). https://arxiv.org/abs/2608.03351
3. N. Prezza and A. Policriti, *Computing LZ77 in Run-Compressed Space*, Data Compression Conference 2016. https://arxiv.org/abs/1510.06257
