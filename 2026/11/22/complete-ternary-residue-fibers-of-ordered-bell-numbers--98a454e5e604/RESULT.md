# Complete ternary residue fibers of ordered Bell numbers

## Finding

Write \(F_n=\sum_{j=0}^{n}j!S(n,j)\) for the ordered Bell (Fubini) numbers, with \(S(n,j)\) the Stirling numbers of the second kind and \(F_0=1\). For every integer \(k\ge2\), the least eventual period modulo \(3^k\) is \(P_k=2\cdot3^{k-1}\). For any starting index \(N\ge\max\{4,k+2\}\), the multiset
\[
\{F_n\bmod3^k:N\le n<N+P_k\}
\]
contains **exactly once** each residue \(y\equiv1\pmod3\), **exactly three times** each residue \(y\equiv3\pmod9\), and **no other residues**. There are precisely \(4\cdot3^{k-2}\) attained residue classes out of \(3^k\). Every attained residue occurs infinitely often. The full image of the nonnegative-index sequence modulo \(3^k\) is the same set, including early indices. For \(k=1\), the image is \(\{0,1\}\) with one occurrence of each per eventual period of length two.

The exact underlying difference law is, for every \(t\ge1\), with \(s=\nu_3(t)\), and every \(n\ge\max\{4,s+3\}\),
\[
\boxed{\nu_3(F_{n+2t}-F_n)=\begin{cases}s+2,&n\text{ even},\\s+1,&n\text{ odd}.\end{cases}}
\]
Thus the three-adic closure of the sequence is exactly \((1+3\mathbb Z_3)\cup(3+9\mathbb Z_3)\), of normalized Haar measure \(4/9\). For each \(k\ge2\), the natural index density of a residue is \(1/(2\cdot3^{k-1})\) in the first class, \(3/(2\cdot3^{k-1})\) in the second class, and zero otherwise.

## Assumptions and scope

All indices are nonnegative integers, all periods are eventually periodic index periods, and \(\nu_3\) denotes the three-adic valuation of a nonzero integer. The least eventual period is the smallest positive shift valid at all sufficiently late indices. Densities refer to uniformly sampled nonnegative indices. No assertion is made for other prime powers or for ordered-Bell polynomial coefficients.

## Proof

**1. Finite exponential truncation.** For any \(K\ge1\), choose \(J\) with \(3^K\mid(J+1)!\). Since \(F_n=\sum_{j=0}^n j!S(n,j)\), terms \(j>J\) vanish modulo \(3^K\). Inclusion-exclusion for Stirling numbers gives, for all \(n\ge1\),
\[
F_n\equiv\sum_{b=1}^{J}c_b b^n\pmod{3^K},\qquad
c_b=\sum_{j=b}^{J}(-1)^{j-b}\binom jb\in\mathbb Z.
\]
Let \(T\) be the step-two forward difference: \(TF_n=F_{n+2}-F_n\). Consequently, for every \(a\ge0\),
\[
T^aF_n\equiv\sum_{b=1}^{J}c_b b^n(b^2-1)^a\pmod{3^K}.
\]
If \(3\nmid b\), then \(3\mid(b^2-1)\); if \(3\mid b\), then \(3^n\mid b^n\). Therefore, for \(n\ge K\),
\[
3^a\mid T^aF_n\quad\text{whenever }0\le a\le K.
\]
In addition, for arbitrary \(a\), all nonunit-base contributions vanish modulo \(3^K\) once \(n\ge K\). These statements hold for every \(K\), since the finite exponential formula can be chosen at any precision.

**2. Sharp first differences.** At precision \(81\), choose \(J=8\), for which
\[
(c_1,\ldots,c_8)=(-4,16,-34,46,-40,22,-7,1).
\]
For \(n\ge4\), the bases divisible by three disappear modulo \(81\), and direct substitution gives
\[
TF_n\equiv48\,2^n+42\,4^n+12\,5^n+69\,7^n+63\,8^n\pmod{81},
\]
\[
T^2F_n\equiv9(7\,2^n+7\,4^n+5\,5^n+8\,7^n)\pmod{81}.
\]
At every even \(n\), the parenthesized sum vanishes modulo nine: it depends only on \(n\bmod6\), and the three values for residues \(0,2,4\) are \(27,144,153\), all divisible by nine. Thus \(T^2F_n\equiv0\pmod{81}\) for even \(n\ge4\). Since \(TF_4=F_6-F_4=4683-75=4608\equiv72\pmod{81}\), it follows by progression that
\[
TF_n\equiv72\pmod{81}\qquad(n\ge4\text{ even}).
\]
For odd \(n\ge5\), reduction of the first displayed expression modulo nine yields \(TF_n\equiv6\pmod9\), since unit bases are \(\pm1\pmod3\). Hence the first differences have valuation two at even indices and one at odd indices. Moreover \(T^aF_n\equiv0\pmod{81}\) at every even \(n\ge4\) and every \(a\ge2\), by repeated step-two differences.

**3. Arbitrary translations.** Let \(t\ge1\), \(s=\nu_3(t)\), and \(n\ge\max\{4,s+3\}\). The binomial identity
\[
F_{n+2t}-F_n=\sum_{a=1}^{t}\binom ta T^aF_n
\]
is exact. For \(1\le a\le t\),
\[
\nu_3\left(\binom ta\right)\ge s-\nu_3(a).
\]
At precision \(3^{s+3}\), the nonunit bases are absent by \(n\ge s+3\). For \(a\ge4\), unit contributions to the product have valuation at least \(s+a-\nu_3(a)\ge s+3\). For \(a=3\), the even-index \(T^3F_n\equiv0\pmod{81}\) raises the lower bound to \(s+3\); for \(a=2\), the even-index \(T^2F_n\equiv0\pmod{81}\) similarly gives valuation at least \(s+4\). Thus for even \(n\), modulo \(3^{s+3}\), only \(tTF_n\) survives; it has exact valuation \(s+2\). For odd \(n\), all terms with \(a\ge2\) have valuation at least \(s+2\), by the unit bound and the vanishing of nonunit bases. The \(a=1\) term has exact valuation \(s+1\). This proves the boxed translation law without numerical extrapolation.

**4. Complete fibers and least periods.** We have \(F_4=75\equiv3\pmod9\) and \(F_5=541\equiv1\pmod3\). The step-two valuations show that every later even term belongs to the first fixed class \(3\pmod9\), and every later odd term belongs to \(1\pmod3\). In an arbitrary block of \(P_k=2\cdot3^{k-1}\) indices starting at \(N\ge\max\{4,k+2\}\), there are \(3^{k-1}\) indices of each parity. Distinct odd-parity indices have differences with valuation \(1+\nu_3(t)\); hence all \(3^{k-1}\) odd terms are distinct modulo \(3^k\), filling the entire class \(1\pmod3\). Among the even-parity indices, equal values occur exactly when their half-index difference is divisible by \(3^{k-2}\), since the difference valuation is \(2+\nu_3(t)\). The \(3^{k-1}\) even terms therefore cover each of the \(3^{k-2}\) residues \(3\pmod9\) exactly three times. Both parity classes are disjoint modulo three.

Shifting by \(P_k\) preserves every sufficiently late term because \(\nu_3(P_k/2)=k-1\). Any eventual period must be even, since neighboring terms have different residues modulo three; its half must be divisible by \(3^{k-1}\) by the odd-index sharp difference law. Therefore \(P_k\) is the least eventual period. The initial values \(F_0=F_1=1,F_2=3,F_3=13\) already lie in the two permitted residue classes, so no additional exceptional residues occur. Taking compatible reductions modulo every \(3^k\) gives the two stated three-adic balls, while exact periodic fibers give the densities.

## Verification

The standalone standard-library script `verify.py` evaluates ordered Bell numbers independently by the first-block binomial recurrence and by the Stirling-number formula, checks the finite precision coefficient identities, the exact odd/even differences, complete residue histograms through modulus \(3^7\), period shifts, and thousands of exact translation valuations. Run `python3 verify.py`. These finite checks are independent corroboration; the all-index conclusions follow from the proof above.

## Relationship to prior work

Poonen (1988), especially Theorems 2–3 and 6, proves eventual modular periodicity and least eventual periods of the ordinary ordered Bell sequence, including the odd-prime-power period. This period is prior work. Asgari and Jahangiri (arXiv:1701.07276, first posted 2017-01-25), Sections 3–5, study the related residual \(r\)-Fubini sequence and characterize its period lengths; their ordinary-sequence discussion cites Poonen. Schreyer's 2024 modular-periodicity treatment and the related previously published prime-power shift-defect theorem address period and onset, not exact value fibers. The present contribution is the evaluated residue-by-residue multiplicity law, the two different sharp translation valuations, and the explicit three-adic image closure. Neither knowledge of a period alone nor of the exact preperiod determines the distribution of values in the period.

## Limitations

The theorem is specific to the prime three; the claimed onset \(N\) is sufficient and is not asserted to be the earliest possible for every modulus. It does not classify prime-power images at other primes. Earlier modular-congruence work contains ingredients for the proof, and absolute historical priority cannot be guaranteed by the sources inspected; an implicit exact distribution elsewhere remains a residual risk. No independent mathematical validation has been performed.

## References

1. A. A. Asgari and M. Jahangiri, *On the periodicity problem of residual r-Fubini sequences*, arXiv:1701.07276, first posted 2017-01-25, https://arxiv.org/abs/1701.07276; lawful full text https://ar5iv.labs.arxiv.org/html/1701.07276.
2. B. Poonen, *Periodicity of a Combinatorial Sequence*, Fibonacci Quarterly 26 (1988), 70–76, https://www.fq.math.ca/Scanned/26-1/poonen.pdf.
3. I. Mező, *Periodicity of the Last Digits of Some Combinatorial Sequences*, arXiv:1308.1637, first posted 2013-08-07, https://arxiv.org/abs/1308.1637.
4. B. Schreyer, *Rigged Horse Numbers and their Modular Periodicity*, arXiv:2409.03799, first posted 2024-09-04, https://arxiv.org/abs/2409.03799.
