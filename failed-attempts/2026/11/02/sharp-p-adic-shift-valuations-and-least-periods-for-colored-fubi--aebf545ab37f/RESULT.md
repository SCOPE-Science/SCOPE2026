# Sharp \(p\)-adic shift valuations and least periods for colored Fubini polynomials

## Finding

For every odd prime \(p\) for which \(2\) is a primitive root modulo \(p^2\), and every integer \(t\ge1\) with \(s=\nu_p(t+1)\ge1\), define the colored ordered-partition polynomial
\[
F_n(t)=\sum_{k=0}^{n} k!\,\left\{\begin{matrix}n\\ k\end{matrix}\right\}t^k \qquad(n\ge0).
\]
For every positive even integer \(q\), put \(\ell=\nu_p(2^q-1)\). **The exact shift valuation** is
\[
\nu_p(F_{n+q}(t)-F_n(t))=s+\ell
\qquad\text{for every integer }n\ge s+\ell+1.
\]
For every positive odd \(q\), the same difference has valuation zero for all \(n\ge0\). Consequently, for every \(a\ge1\), the least *eventual* period of \(n\mapsto F_n(t)\bmod p^a\) is exactly
\[
T_a(t)=\begin{cases}
2,&1\le a\le s,\\
(p-1)p^{a-s-1},&a>s.
\end{cases}
\]
In the second case the claimed shift of size \(T_a(t)\) holds for all \(n\ge a+1\); in the first case the shift of size two holds for all \(n\ge0\). The least-eventual-period assertion refers to all sufficiently large indices, not necessarily to an initial periodic sequence.

## Assumptions and scope

The symbol \(\nu_p(m)\) means the largest exponent of \(p\) dividing the nonzero integer \(m\), with \(\nu_p(0)=+\infty\). The Stirling number in braces counts set partitions of \(n\) labeled elements into \(k\) nonempty blocks. The factor \(k!\) orders those blocks and \(t^k\) independently assigns one of \(t\) colors to each block. The convention \(F_0(t)=1\) is used. Requiring \(2\) to generate the multiplicative group modulo \(p^2\) is a checkable hypothesis (for example \(p=3,5,11,13\)); no claim is made for primes failing it. The valuation theorem concerns all even \(q>0\), all the indicated \(n\), and all positive integer weights in the specified residue class.

## Proof

**1. A convergent moment expansion.** Put \(h=t+1\). The exponential generating function from colored ordered partitions is
\[
\sum_{n\ge0}F_n(t)\frac{z^n}{n!}
=\frac1{1-t(e^z-1)}
=\frac{e^{-z}}{1+h(e^{-z}-1)}.
\]
Expanding the denominator formally in \(h\), the coefficient of \(z^n/n!\) receives contributions only from powers \(h^j\) with \(j\le n\), since \((e^{-z}-1)^j\) has order \(j\). The binomial expansion therefore gives the exact polynomial identity
\[
F_n(h-1)=(-1)^n\sum_{j=0}^{n}h^j
\sum_{i=0}^j(-1)^i\binom ji(i+1)^n.
\]
Equivalently, reorganizing as a formal power series in \(h\), and then specializing to the \(p\)-adically small integer \(h\), gives the convergent identity in \(\mathbb Z_p\):
\[
F_n(t)=(-1)^n\sum_{b=1}^{\infty}
\frac{(-1)^{b-1}h^{b-1}}{(1-h)^b}\,b^n.
\tag{1}
\]
Indeed, the coefficient of \(h^j\) in \(h^{b-1}(1-h)^{-b}\) is \(\binom{j}{b-1}\) for \(j\ge b-1\), which recovers the displayed finite-difference formula; the original finite differences vanish for \(j>n\). Every denominator \((1-h)^b\) is a \(p\)-adic unit. In particular the coefficient at \(b\) in (1) has valuation exactly \((b-1)s\). Reduction of (1) modulo \(p\) leaves only its \(b=1\) term, so
\[
F_n(t)\equiv(-1)^n\pmod p.
\tag{2}
\]

**2. The first nonzero term of an even shift.** For even \(q>0\), subtracting (1) at the two indices gives
\[
F_{n+q}(t)-F_n(t)
=(-1)^n\sum_{b=2}^{\infty}
\frac{(-1)^{b-1}h^{b-1}}{(1-h)^b}\,b^n(b^q-1).
\tag{3}
\]
The term \(b=2\) has valuation **exactly** \(s+\ell\), where \(\ell=\nu_p(2^q-1)\). If \(p-1\nmid q\), then \(\ell=0\), since \(2\) has multiplicative order \(p-1\) modulo \(p\). Every term from \(b\ge3\) with \(p\nmid b\) has valuation at least \(2s\), strictly greater than \(s+\ell=s\).

If \(p-1\mid q\), write \(q=(p-1)m\). For any integer \(b\) prime to \(p\), Fermat's congruence together with the standard lifting-the-exponent lemma yields
\[
\nu_p(b^q-1)\ge1+\nu_p(m).
\]
Because \(2\) generates modulo \(p^2\), one has \(\nu_p(2^{p-1}-1)=1\), so the same lifting lemma gives \(\ell=1+\nu_p(m)\). Therefore every unit term with \(b\ge3\) in (3) has valuation at least \(2s+\ell>s+\ell\). Finally, every term with \(p\mid b\) has valuation at least \(n\), hence strictly greater than \(s+\ell\) when \(n\ge s+\ell+1\). All terms other than \(b=2\) are thus strictly more divisible by \(p\). As (3) converges, no cancellation can change the valuation of its unique lowest-valuation term. This proves the exact even-shift law.

**3. Odd shifts and exact eventual periods.** By (2), when \(q\) is odd the difference \(F_{n+q}(t)-F_n(t)\) is congruent to \(-2(-1)^n\) modulo \(p\), hence is a \(p\)-adic unit. When \(a\le s\), (1) gives \(F_n(t)\equiv(-1)^n\pmod{p^a}\) for every \(n\ge0\), so its least period is two.

For \(a>s\), the even-shift result shows that a positive even \(q\) is an eventual period modulo \(p^a\) if and only if \(\nu_p(2^q-1)\ge a-s\); the statement follows in both directions by choosing sufficiently large \(n\) for the applicable exact-valuation law. Since \(2\) generates modulo \(p^2\), its order modulo every \(p^r\) is \((p-1)p^{r-1}\) for \(r\ge1\) (use the order modulo \(p\) and \(\nu_p(2^{p-1}-1)=1\)). Hence the least such \(q\) is \((p-1)p^{a-s-1}\), which is even. For this shift \(\ell=a-s\), and its congruence is valid at all \(n\ge a+1\). All smaller positive shifts are excluded by the odd-shift obstruction or the sharp even-shift valuation.

## Verification

The standalone file `verify.py` implements independent evaluations through the Stirling triangle, the first-block recurrence, and a finite truncation of the convergent \(p\)-adic moment representation. It then checks the sharp valuation formula at many shifts and compares period predictions with direct modular recurrences while excluding every proper divisor of the predicted period. In the recorded replay: 228 independent Stirling/first-block comparisons, 108 moment-expansion comparisons, 1596 exact shift-valuation comparisons, and 45 prime-power period/minimality tests passed. These finite computations are checks, not the basis of the universal theorem.

For illustration, \(t=2\), \(p=3\) and \(s=1\) give least eventual periods \(2,2,6,18,54,\ldots\) modulo \(3,9,27,81,243,\ldots\). For \(t=4\), \(p=5\) and \(s=1\), the periods modulo \(5,25,125,625,\ldots\) are \(2,4,20,100,\ldots\).

## Relationship to prior work

The usual Fubini numbers \(F_n(1)\) and their last-digit periodicity were studied by Poonen (1988) and Mező (2013 preprint; 2014 journal article). Poonen proves exact prime-power periods for the unweighted sequence. Mező treats restricted, associated, and \(r\)-Fubini numbers. Neither theorem supplies the parameter-sensitive result here: the hypothesis \(p\mid t+1\) excludes the unweighted specialization \(t=1\) at odd primes.

Mihoubi and Taharbouchet (2019, initially circulated in 2017) study exactly the geometric/Fubini polynomials \(F_n(t)\), including polynomial congruences modulo \(p\), but the inspected congruence section does not provide exact valuations of all even index shifts modulo arbitrary powers of \(p\) or the least eventual periods for this colored-block specialization. Schreyer (2025) studies a different \(r\)-horse variant built from shifted ordinary Fubini numbers, not the independent block-color parameter. The complete sharp valuation is not a formal consequence of a modulo-\(p\) congruence or a period for \(F_n(1)\).

## Limitations

The criterion requiring \(2\) to be a primitive root modulo \(p^2\) is essential to the stated proof; no assertion is made for other odd primes, for \(p=2\), or for weights with \(p\nmid t+1\). The theorem proves eventual periods; it does not assert that the same period holds from \(n=0\) in the second case. An equivalent theorem may exist in broader unpublished or unlocated \(p\)-adic polynomial-congruence literature. The 2017 Diagana--Maïga paper on generalized Fubini congruences was identified, but its full text was not available for a decisive whole-document comparison; this remains an originality risk.

## References

- B. Poonen, “Periodicity of a Combinatorial Sequence,” *Fibonacci Quarterly* **26** (1988), 70–76, https://www.fq.math.ca/Scanned/26-1/poonen.pdf.
- I. Mező, “Periodicity of the Last Digits of Some Combinatorial Sequences,” arXiv:1308.1637v1, first public posting 2013-08-07; *Journal of Integer Sequences* **17** (2014), Article 14.1.1, https://arxiv.org/abs/1308.1637.
- M. Mihoubi and S. Taharbouchet, “Identities and Congruences Involving the Geometric Polynomials,” *Miskolc Mathematical Notes* **20** (2019), 395–408, https://real.mtak.hu/94956/1/2498.pdf; arXiv:1706.08950.
- T. Diagana and H. Maïga, “Some New Identities and Congruences for Fubini Numbers,” *Journal of Number Theory* **173** (2017), 547–569, DOI:10.1016/j.jnt.2016.09.032 (abstract inspected; full text not obtained).
- B. Schreyer, “Rigged Horse Numbers and their Modular Periodicity,” *Journal of Integer Sequences* **28** (2025), Article 25.4.1, https://cs.uwaterloo.ca/journals/JIS/VOL28/Schreyer/schreyer7.html.
- OEIS A000670, “Fubini numbers,” https://oeis.org/A000670; database covers \(t=1\), not the modular colored-weight claim.
