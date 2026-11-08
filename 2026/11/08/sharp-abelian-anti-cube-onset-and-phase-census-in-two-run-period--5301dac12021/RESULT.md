# Sharp Abelian anti-cube onset and phase census in two-run periodic words

## Finding
Fix integers \(a,b\ge1\) and the infinite binary word
\[
X_{a,b}=(0^a1^b)^\omega,\qquad p=a+b.
\]
An **Abelian \(q\)-antipower with block length \(k\)** is a factor consisting of \(q\ge2\) consecutive length-\(k\) blocks whose Parikh vectors are pairwise different. Let \(N_q(a,b;k)\) be the number of starting positions modulo the primitive period \(p\) that produce such a factor.

**Theorem (sharp onset and exact census).** Put \(s=\min(a,b)\) and \(t=\max(a,b)\). If \(K(a,b)\) is the least positive block length for an Abelian \(3\)-antipower, with \(K=\infty\) if none exists, then
\[
K(a,b)=\begin{cases}
\infty,&s=1\text{ or }(s,t)\in\{(2,2),(2,4)\},\\
2,&s\ge3,\\
\lfloor(a+b)/3\rfloor+1,&s=2,\ t=3\text{ or }t\ge5.
\end{cases}
\]
At the first permitted block length, the exact number of starting phases is
\[
N_3(a,b;K(a,b))=\begin{cases}
2+2[\,a=3\,]+2[\,b=3\,],&s\ge3,\\
2,&s=2,\ t=3\text{ or }t\ge5.
\end{cases}
\]
Here brackets denote indicator functions. The cases with infinite \(K\) have no Abelian \(3\)-antipower at any block length.

Furthermore, for **every** \(q\ge2\), \(k\ge1\), and positive \(a,b\), the exact integer \(N_q(a,b;k)\) is computable using at most \(2(q+1)+2\) circular breakpoints and \(O(q^3\log q)\) integer-arithmetic operations, independently of the numerical size of \(p\) or \(k\). The algorithm and its complete proof appear below and in `verify.py`.

## Assumptions and scope
All starting phases are residues \(0,\dots,p-1\), indexed from the beginning of the displayed period; the count is a count of **occurrences per period**, not a count of distinct factors. Distinct blocks in an Abelian antipower are required to have pairwise distinct *Parikh vectors*, not merely different literal strings. The word is genuinely primitive of period \(p\) since both run lengths are positive. Complexity is measured in integer-arithmetic operations; integers have bit length polynomial in \(\log(p+qk)\). No aperiodic or multiple-run generalization is asserted.

## Proof
**1. Periodic reduction and Parikh range.** Let
\[
F(x)=a\lfloor x/p\rfloor+\min\{a,x\bmod p\},\quad x\ge0.
\]
This counts zeros in the first \(x\) letters. Write \(k=mp+r\) with \(0\le r<p\). The zero count of the \(j\)-th length-\(k\) block starting at phase \(u\) is
\[
ma+g_j(u),\qquad g_j(u)=F(u+(j+1)r)-F(u+jr).
\]
Thus common full periods do not affect pairwise equality. If \(r=0\), all block Parikh vectors agree. Otherwise the zero counts in length-\(r\) windows attain every integer between \(\max(0,r-b)\) and \(\min(a,r)\); this interval has width \(\min\{a,b,r,p-r\}\). Hence \(N_q=0\) if \(q>1+\min\{a,b,r,p-r\}\).

**2. Exact phase-census algorithm.** Regard \(F\) as the continuous piecewise-affine interpolation of its integer values. Its slope changes only at positions congruent to \(0\) or \(a\) modulo \(p\). Therefore, for \(j=0,\dots,q-1\), all \(g_j\) are simultaneously affine on each half-open integer interval between consecutive members of
\[
\mathcal B=\{0,p\}\cup\{(-jr)\bmod p,(a-jr)\bmod p:0\le j\le q\}.
\]
There are at most \(2(q+1)+2\) members. For an interval \([L,R)\) with \(L<R\), compute \(v_j=g_j(L)\). When \(R-L\ge2\), compute \(d_j=g_j(L+1)-g_j(L)\); when \(R-L=1\), put \(d_j=0\), since there is only one integer point. Then throughout its integer points,
\[
g_j(u)=v_j+d_j(u-L).
\]
For each pair \(i<j\), the equality \(g_i(u)=g_j(u)\) is \((d_i-d_j)(u-L)=v_j-v_i\). If both sides are identically zero, reject the whole interval. Otherwise the equality is impossible or has exactly one integer solution in the interval. Collect the distinct integer solutions over all pairs. Subtract their number from \(R-L\) and sum the remainders. This counts precisely the starting phases whose \(q\) vectors are all distinct, without inspecting all \(p\) phases. Sorting at most \(O(q^2)\) forbidden points for each of \(O(q)\) intervals costs \(O(q^3\log q)\) arithmetic comparisons, with \(O(q^2)\) auxiliary storage; direct evaluation of \(F\) is constant-time arithmetic. This establishes exactness and the stated bound.

**3. Sharp onset for the short-run cases.** If \(s=1\), the possible rare-letter counts in any fixed-length window differ by at most one; three pairwise distinct Parikh vectors are impossible. If \(s=2\), interchange letters if needed and write the period as \(00\,1^t\). At any block length with \(3k\le p=t+2\), the union of three consecutive blocks has at most two zeros, whereas three distinct individual zero counts would have to include \(0,1,2\) and total at least three. Thus \(k>p/3\). The exceptional periods \(0011\) and \(001111\) yield no Abelian three-antipower: for \(k\bmod p\) equal to \(0,\dots,p-1\), the largest possible number of pairwise distinct consecutive length-\(k\) block Parikh vectors is respectively \((1,2,2,2)\) for \(p=4\) and \((1,2,2,2,2,2)\) for \(p=6\), by direct enumeration of their four or six starting phases. These finite checks are exhaustive because the block Parikh differences depend only on \(k\bmod p\).

For \(t=3\) or \(t\ge5\), set \(k=\lfloor p/3\rfloor+1\) and \(h=3k-p\in\{1,2,3\}\). The starting phase \(u=1\), the second zero of \(00\,1^t\), gives three length-\(k\) blocks having respectively \(1,0,2\) zeros: the first contains that second zero; the second lies in the long one-run; the third crosses the next occurrence of both zeros. The inequalities \(1+k\ge3\), \(1+2k\le p\) and \(1+3k\ge p+2\) hold for \(p=5\) and all \(p\ge7\). Therefore \(K=k\), attaining the lower bound. At this \(k\), every successful triple has zero counts \(0,1,2\). Its total of three zeros equals the two zeros of a whole period plus exactly one zero in its remaining length-\(h\) segment. For the specified values of \(p,h,t\), precisely two cyclic starts have exactly one zero in a length-\(h\) segment. Both work by reversal symmetry and the explicit witness. Thus there are exactly two successful phases.

**4. Sharp onset when both runs have length at least three.** A block length of one cannot yield three distinct binary Parikh vectors, but block length two does: the two transitions give the six-letter factors \(000111\) and \(111000\), whose three consecutive two-letter blocks have zero counts \(2,1,0\) and \(0,1,2\). Every possible successful length-six factor must have exactly one of its three two-letter blocks equal to \(00\), one to \(11\), and the remaining block mixed. Within a two-run periodic host with both runs at least three, only the following six literal words among these arrangements can occur:
\[
000111,\quad111000,\quad100011,\quad110001,\quad011100,\quad001110.
\]
The first two always occur, the next two occur exactly when \(a=3\), and the final two occur exactly when \(b=3\). Since each contains a run transition and both run lengths are at least three, each occurs at exactly one starting phase per period. This proves both the threshold and the asserted exact multiplicity.

## Verification
Run `python3 verify.py` using Python 3 standard library. The checker independently computes the count from the fully expanded periodic source and compares it with the breakpoint census. The included run completed 16,642 all-parameter moderate-size count comparisons, 2,500 onset-and-multiplicity cases, and 1,000 seeded large-parameter tests (cases with period at most 5,000). Finite tests are corroboration; the all-parameter statements follow from the preceding proof. The code has no external dependencies. The exhaustive finite exceptions in step 3 are also directly inspectable by hand.

## Relationship to prior work
Fici, Postic and Silva (2018) introduced Abelian antipowers and studied global existence in infinite words, notably paperfolding words; their paper does not determine this two-run periodic phase census or its sharp three-antipower onset. Kociumaka et al. (2018) give general algorithms for **ordinary** antipowers, whose blocks need only be unequal strings; those counts are not Abelian-antipower counts. Peltomäki and Whiteland (2020) investigate cyclic avoidance of **Abelian powers**, requiring equality rather than pairwise inequality of block Parikh vectors. The present result concerns a different property: exact phase counts of pairwise distinct Parikh vectors. It also differs from formulas for Abelian powers in this same host family, since none of their all-equal conditions imply pairwise distinctness.

## Limitations
The bound counts phases, not distinct factor words, and does not claim asymptotic optimality for the counting algorithm. The exact shortest-block theorem treats three blocks only; the census algorithm treats arbitrary orders without a closed-form shortest-block threshold for higher orders. The scientific novelty comparison is limited to the listed accessible sources and semantic research-record searches; unknown equivalent earlier results remain possible. No independent audit or formal proof-assistant certification is claimed.

## References
1. G. Fici, M. Postic and M. Silva, *Abelian Anti-Powers in Infinite Words*, arXiv:1810.12275, first public 2018-10-29. https://arxiv.org/pdf/1810.12275
2. T. Kociumaka, J. Radoszewski, W. Rytter, J. Straszyński, T. Waleń and W. Zuba, *Efficient Representation and Counting of Antipower Factors in Words*, arXiv:1812.08101, first public 2018-12-19. https://arxiv.org/abs/1812.08101
3. J. Peltomäki and M. A. Whiteland, *Avoiding Abelian Powers Cyclically*, arXiv:2006.06307, first public 2020-06-11. https://arxiv.org/pdf/2006.06307
