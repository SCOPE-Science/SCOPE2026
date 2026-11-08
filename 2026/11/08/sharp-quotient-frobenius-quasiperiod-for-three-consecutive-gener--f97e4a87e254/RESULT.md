# Sharp quotient-Frobenius quasiperiod for three consecutive generators

## Finding

Fix an integer \(p\ge 2\). For every integer \(a\ge 2p+4\), let
\[
S_a=\langle a,a+1,a+2\rangle,\qquad Q_{a,p}=\{n\in\mathbb Z_{\ge0}:pn\in S_a\},
\]
and write \(F_p(a)=\max(\mathbb Z_{\ge0}\setminus Q_{a,p})\). Put \(\epsilon=\operatorname{rem}_2(a)\), \(t=(a-\epsilon)/2\), and for each integer \(j\ge0\) let
\[
R_j(a,p)=\operatorname{rem}_p((t-j)a-1),\quad 0\le R_j(a,p)<p.
\]
Define
\[
J_p(a)=\min\left\{0\le j\le \left\lceil\frac{p-1-\epsilon}{2}\right\rceil:R_j(a,p)\le\epsilon+2j\right\},
\]
which is always nonempty. With \(J=J_p(a)\), \(B_p(a)=\epsilon+2J\), and \(R_p(a)=R_J(a,p)\), the exact formula is
\[
\boxed{F_p(a)=\frac{a^2-B_p(a)a-2(1+R_p(a))}{2p}.}
\]
The functions \(B_p(a)\) and \(R_p(a)\) depend only on \(a\bmod 2p\). **The least eventual quasipolynomial period** of \(a\mapsto F_p(a)\), among all positive periods and all eventual polynomial branch presentations, is exactly \(\boxed{2p}\) for every \(p\ge2\). Each branch has leading coefficient \(1/(2p)\).

## Assumptions and scope

Integers \(p\ge2\) and \(a\ge2p+4\) are unrestricted by coprimality. The integer remainder \(\operatorname{rem}_m(x)\) is in \(\{0,\ldots,m-1\}\), including when \(x\) is negative. A positive integer \(T\) is an eventual quasipolynomial period when there are polynomials \(P_0,\ldots,P_{T-1}\in\mathbb Q[X]\) such that \(F_p(a)=P_{a\bmod T}(a)\) for all sufficiently large \(a\). Period means least positive such \(T\), not the period of a finite observed sequence.

## Proof

**Exact gap intervals.** Write every nonnegative integer uniquely as \(qa+r\) with \(0\le r<a\). A sum of exactly \(q\) generators of \(S_a\) has the form \(qa+s\), where every integer \(0\le s\le2q\) is attainable. For \(q< (a-1)/2\), a sum involving fewer than \(q\) generators is less than \(qa\), because \((q-1)(a+2)<qa\); more than \(q\) generators exceed \(qa+r\). Thus all gaps are precisely the disjoint intervals
\[
\mathbb Z_{\ge0}\setminus S_a=\bigsqcup_{q=0}^{\lfloor(a-2)/2\rfloor}
\{q(a+2)+1,\ldots,(q+1)a-1\}.
\]
For larger \(q\) every remainder \(r<a\) is obtained using \(q\) generators, so there are no further gaps.

**Largest quotient gap.** Writing \(a=2t+\epsilon\), the largest index above is \(q=t-1\). Write each candidate index as \(q=t-1-j\), \(j\ge0\). Its right endpoint is \(H_j=(t-j)a-1\), and its length difference (right minus left endpoint) is exactly \(\epsilon+2j\). Therefore the interval contains a multiple of \(p\) precisely when
\[
R_j(a,p)=\operatorname{rem}_p(H_j)\le \epsilon+2j;
\]
if so, the largest multiple is \(H_j-R_j\). At the upper endpoint \(j_{\max}=\lceil(p-1-\epsilon)/2\rceil\), one has \(\epsilon+2j_{\max}\ge p-1\), so this candidate always satisfies the remainder inequality and the minimum exists. The assumption \(a\ge2p+4\) ensures these indices all remain nonnegative. For successive intervals, the right endpoints differ by \(a>p\), so the largest admissible multiple occurs in the highest interval containing one, i.e., at the minimum \(J\). Dividing \(H_J-R_J\) by \(p\) gives the displayed formula. Since \(t\bmod p\) and \(\epsilon\) depend only on \(a\bmod2p\), so do \(B_p(a)\) and \(R_p(a)\). This proves an eventual quadratic quasipolynomial with period \(2p\).

**Minimality.** The branch polynomial is uniquely determined on every infinite residue class modulo \(2p\). Because all branches have the same quadratic coefficient, two classes share the same polynomial if and only if their ordered pairs \((B_p,R_p)\) agree. If any positive \(T\) is another eventual quasipolynomial period, the Chinese remainder theorem applied to compatible residue classes (equivalently, uniqueness of polynomials agreeing on infinite arithmetic progressions) shows the signature sequence \(a\mapsto(B_p(a),R_p(a))\) has cyclic period \(\gcd(T,2p)\). It suffices to show its least cyclic period is \(2p\).

For \(p=2k+1\) odd, at the class \(a\equiv0\pmod{2p}\) the signature is \((p-1,p-1)\). This signature occurs **exactly** at the two classes \(0\) and \(p-1\pmod{2p}\). Indeed, equality of the first coordinate forces \(a\) even and \(J=k\); equality of the second gives \(R_k=p-1\). Minimality of \(J\) forces \(R_{k-1}>p-3\), hence \(R_{k-1}\in\{p-2,p-1\}\). But \(R_{k-1}\equiv R_k+a\pmod p\), so \(a\equiv-1\) or \(0\pmod p\). The even classes corresponding to these residues are exactly \(p-1\) and \(0\pmod{2p}\). Conversely, \(a\equiv0\) gives \(R_j=p-1\) for all \(j\), and \(a\equiv p-1\) gives \(R_j=k+j\) for \(0\le j\le k\); in both cases \(J=k\) and the signature is \((p-1,p-1)\). A two-point subset \(\{0,p-1\}\) of the cyclic group of order \(2p\) has no nontrivial translational period: a nontrivial stabilizing translation would have to swap the points, requiring \(2(p-1)\equiv0\pmod{2p}\), which is false. Thus the least signature period is \(2p\) for odd \(p\).

For \(p=2k\) even, the signature \((p,p-1)\) attained at \(a\equiv0\pmod{2p}\) occurs exactly at classes \(0,p\). Indeed, it requires \(a\) even, \(J=k\), \(R_k=p-1\), and failure of the inequality at \(j=k-1\). The previous threshold is \(p-2\), so \(R_{k-1}=p-1\), whence \(a\equiv0\pmod p\); both even classes \(0,p\) attain the signature. Consequently any period must be \(p\) or \(2p\). At \(a\equiv1\pmod{2p}\), a direct remainder calculation gives \(J=\lceil(2k-2)/3\rceil\), whereas at \(a\equiv p+1\pmod{2p}\) it gives \(J=\max(0,\lceil(k-2)/3\rceil)\). For \(k\ge2\), the former is strictly larger, so the linear coefficients differ and \(p\) is not a period. At \(p=2\), both indices are zero, but the remainders at these two classes are respectively \(1\) and \(0\), so the constant terms differ. Again the least cyclic period is \(2p\), completing the proof.

## Verification

The included `verify.py` uses ordinary coin-closure dynamic programming to calculate the Frobenius number of each quotient independently of the gap interval construction. It compares \(5{,}000\) pairs with \(2\le p\le41\) and \(2p+4\le a<172\); all agree. A second check verifies \(43{,}554\) exact evaluations of quadratic residue branches and computes the least branch period and distinguished signature classes for all \(2\le p\le120\). Exact script output is in `checks.txt`. These finite tests are **not** an infinite-domain proof; the proof above supplies that step.

## Relationship to prior work

Adeniran et al., *On the genus of a quotient of a numerical semigroup* (arXiv:1809.09360), study three-term arithmetic progressions and explicitly compute quotient Frobenius numbers under divisibility \(p\mid a\) and additional hypotheses. Liu, *On quotients of numerical semigroups for almost arithmetic progressions* (arXiv:2312.06096), gives more general arithmetic-progression formulas, again requiring \(p\mid a\). Liu, *The Frobenius problem for a class of quotients of numerical semigroups* (arXiv:2604.26415), also uses divisor hypotheses. Liu, *On the Frobenius Number of Quotients of Numerical Semigroups* (arXiv:2607.23076, first posted July 25, 2026), proves quasipolynomial behavior for quotients of **two** consecutive generators, a different base semigroup. These papers motivate the natural fixed-modulus question but do not state the unrestricted three-consecutive-generator quotient formula with least period \(2p\). The earlier \(p\mid a\) cases are not claimed as new individually.

## Limitations

The formula is proved only for \(a\ge2p+4\), with \(p\) fixed or varying subject to this inequality. It says nothing about the smallest possible stabilization cutoff, higher factorization-count thresholds, or unequal generator spacings. The novelty assessment is relative to the explicitly inspected works and searches, not a guarantee of priority over all unindexed literature. Independent mathematical audit has not been performed.

## References

1. A. Adeniran et al., *On the genus of a quotient of a numerical semigroup*, arXiv:1809.09360v2 (2018), https://arxiv.org/abs/1809.09360.
2. F. Liu, *On quotients of numerical semigroups for almost arithmetic progressions*, arXiv:2312.06096v1 (2023), https://arxiv.org/abs/2312.06096.
3. F. Liu, *The Frobenius problem for a class of quotients of numerical semigroups*, arXiv:2604.26415v1 (2026), https://arxiv.org/abs/2604.26415.
4. F. Liu, *On the Frobenius Number of Quotients of Numerical Semigroups*, arXiv:2607.23076v1 (2026), https://arxiv.org/abs/2607.23076.
