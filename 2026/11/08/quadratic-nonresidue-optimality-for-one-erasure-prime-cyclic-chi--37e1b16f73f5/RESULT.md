# Quadratic-nonresidue optimality for one-erasure prime cyclic chirps

## Finding

For every odd prime \(p\), the usual prime-length quadratic chirps acquire explicit nonzero cyclic autocorrelation sidelobes when precisely one coefficient is erased. The **same root indices simultaneously minimize** the maximum sidelobe and the integrated squared sidelobe. When \(p\equiv3\pmod4\), all \(p-1\) roots tie. When \(p\equiv1\pmod4\), the exactly \((p-1)/2\) optimal roots are the quadratic nonresidues modulo \(p\). This is a complete all-prime classification for the one-erasure model, rather than a claim about arbitrary erasure patterns or arbitrary phase sequences.

Precisely, let \(\ell_p\) denote the least positive quadratic nonresidue modulo \(p\) when \(p\equiv1\pmod4\). Put \(P_{p,u}=\max_{1\le k<p}|R_{p,u,a}(k)|\) and \(I_{p,u}=\sum_{k=1}^{p-1}|R_{p,u,a}(k)|^2\) using unnormalized cyclic correlations. Both are independent of the erased index \(a\). Their exact values are

\[
(P_{p,u},I_{p,u})=
\begin{cases}
(2\cos(\pi/p),\ 2(p-2)),&p\equiv3\pmod4,\\
(2\cos(\pi/p),\ 2(p-2)+2\sqrt p),&p\equiv1\pmod4\text{ and }\chi_p(u)=1,\\
(2\cos(\pi\ell_p/p),\ 2(p-2)-2\sqrt p),&p\equiv1\pmod4\text{ and }\chi_p(u)=-1.
\end{cases}
\]

Here \(\chi_p\) is the quadratic character on the nonzero residues. In particular, when \(p\equiv1\pmod4\), both optima are strictly better for a nonresidue root; the integrated-sidelobe gap between the two root classes equals \(4\sqrt p\). The optimal squared-sidelobe sum is \(2(p-2)-2\sqrt p\) and the optimal peak is \(2\cos(\pi\ell_p/p)\). When \(p\equiv3\pmod4\), both objectives are constant across all roots.

## Assumptions and scope

Let \(p\ge3\) be an odd prime and let \(u\in\{1,\ldots,p-1\}\) be a root index. On \(\mathbb Z/p\mathbb Z\), choose the quadratic chirp

\[
c_u(n)=\exp\!\left(-\frac{\pi i u n(n+1)}p\right).
\]

The formula is \(p\)-periodic because \(p\) is odd. Fix any erasure location \(a\in\mathbb Z/p\mathbb Z\) and define \(y_{u,a}(n)=c_u(n)\) for \(n\ne a\), and \(y_{u,a}(a)=0\). For each \(k\in\mathbb Z/p\mathbb Z\), use the unnormalized periodic autocorrelation

\[
R_{p,u,a}(k)=\sum_{n\bmod p}y_{u,a}(n)\overline{y_{u,a}(n+k)}.
\]

The zero-lag correlation is \(p-1\); only \(k\ne0\) enters the two sidelobe objectives. No averaging by \(p\), \(p-1\), or by the number of sidelobes is used in the displayed constants. The theorem optimizes over the \(p-1\) standard prime chirp roots, not over general unimodular sequences.

## Proof

**1. Exact sidelobes.** For each nonzero lag \(k\), completing the difference of the quadratic phases gives

\[
c_u(n)\overline{c_u(n+k)}
=\exp\!\left(\frac{\pi i u k(2n+k+1)}p\right).
\]

Since \(uk\not\equiv0\pmod p\), the unpunctured cyclic sum is zero by the geometric sum of the nontrivial character \(n\mapsto\exp(2\pi iukn/p)\). Erasing \(n=a\) deletes the terms indexed by \(n=a\) and \(n=a-k\); these are distinct for nonzero \(k\). Consequently

\[
\begin{aligned}
R_{p,u,a}(k)
&=-\exp\!\left(\frac{\pi iuk(2a+k+1)}p\right)
  -\exp\!\left(\frac{\pi iuk(2a-k+1)}p\right)\\
&=-2\exp\!\left(\frac{\pi iuk(2a+1)}p\right)
  \cos\!\left(\frac{\pi uk^2}p\right).
\end{aligned}
\]

Thus the sidelobe modulus is exactly \(2|\cos(\pi uk^2/p)|\), independent of \(a\).

**2. Peak classification.** The set of nonzero squares \(Q_p=\{k^2\bmod p:k\ne0\}\) is a subgroup of index two of \(\mathbb F_p^\times\). The available residues \(uk^2\bmod p\) are exactly the coset \(uQ_p\). For an integer \(r\in\{1,\ldots,p-1\}\),

\[
|\cos(\pi r/p)|
=\cos\!\left(\frac{\pi\min(r,p-r)}p\right),
\]

which decreases strictly as the nearest-to-zero representative \(\min(r,p-r)\) increases through the integers \(1,\ldots,(p-1)/2\).

If \(p\equiv3\pmod4\), then \(-1\notin Q_p\), so each of the two cosets \(uQ_p\) contains one of \(1,-1\). All roots therefore have peak \(2\cos(\pi/p)\). If \(p\equiv1\pmod4\), then \(-1\in Q_p\): a residue root makes \(uQ_p=Q_p\) and attains nearest representative \(1\), whereas a nonresidue root makes \(uQ_p=\mathbb F_p^\times\setminus Q_p\). The latter is closed under negation, so the minimum nearest representative is the least positive nonresidue \(\ell_p\le(p-1)/2\). As \(1\) is a residue, \(\ell_p\ge2\) and the nonresidue peak is strictly smaller.

**3. Integrated sidelobes.** By the exact sidelobe formula and the identity \(4\cos^2(t)=2+2\cos(2t)\),

\[
I_{p,u}=2(p-1)+2\sum_{k=1}^{p-1}
\cos\!\left(\frac{2\pi uk^2}p\right)
=2(p-2)+2\operatorname{Re}G_p(u),
\]

where \(G_p(u)=\sum_{k\bmod p}\exp(2\pi iuk^2/p)\). The classical quadratic Gauss-sum evaluation gives

\[
G_p(u)=\chi_p(u)\begin{cases}
\sqrt p,&p\equiv1\pmod4,\\
i\sqrt p,&p\equiv3\pmod4.
\end{cases}
\]

This is the standard identity reproduced, with proof and references, in Gregoratti–Arteaga–Broquetas (2023), Appendix B, Propositions 2–3. Taking real parts yields the claimed integrated-sidelobe formula. Both objective classifications agree, with exactly \((p-1)/2\) minimizing roots when \(p\equiv1\pmod4\), and all roots minimizing when \(p\equiv3\pmod4\). This completes the proof.

## Verification

The standalone Python 3 script `verify_one_erasure.py`, requiring only the standard library, directly constructs each chirp, erases two separately selected positions, computes all nonzero periodic autocorrelations, and compares the results with the displayed complex-phase formula, peak, energy, and optimizing-root classification. It checks every root for every odd prime at most \(101\) (\(2268\) erased-root instances). Expected output is `ZC_ONE_ERASURE_CHECK_PASS cyclic_cases=2268 prime_range=3..101`.

These finite computations are checks only. The proof above applies without an upper bound on \(p\). For example, \(p=5\) has \(\ell_p=2\): the best peak is \(2\cos(2\pi/5)\) and the best sidelobe energy is \(6-2\sqrt5\), while the residue-root energy is \(6+2\sqrt5\). For \(p=7\), every root has peak \(2\cos(\pi/7)\) and energy \(10\).

## Relationship to prior work

Andrews, *A Primer on Zadoff Chu Sequences* (first public version November 10, 2022), introduces the root-indexed chirps, verifies perfect cyclic autocorrelation before erasure, and discusses communication uses and certain modified sequences. Gregoratti, Arteaga, and Broquetas, *Mathematical Properties of the Zadoff–Chu Sequences* (first public version November 2, 2023), give proofs of the perfect autocorrelation and quadratic Gauss-sum formulas. Neither inspected full-text treatment gives the present one-erasure root-dependent sidelobe formula or the simultaneous exact peak/energy extremizer classification. These baseline identities are explicitly acknowledged and not claimed as new.

Lee and Yang (2014) study partial-period correlations, obtain their moments, and could conceivably imply a related single-hole formula by recombination. Only an abstract and bibliographic record were available in the present comparison. This leaves genuine priority uncertainty; any complete earlier specialist derivation of the same root selection would supersede this claim of novelty. The present theorem concerns a *single isolated zero in a retained prime cycle*, not an arbitrary contiguous partial-period measurement, a shortened sequence with a different cyclic length, a multi-erasure mask, or phase retrieval.

## Limitations

This theorem is restricted to an odd prime period, one entirely erased coefficient, the standard unmodified quadratic chirp family, and **unnormalized periodic** autocorrelation. No claim is made about optimality among all complex sequences, composite lengths, nonbinary attenuation, aperiodic correlation, multiple erasures, synchronization error probabilities, or spectral-mask designs. The exact first-erasure formulas are derived here from standard CAZAC and Gauss-sum identities, so specialist prior-work coverage beyond the accessible primary text remains a residual novelty risk.

## References

1. Jeffrey G. Andrews, *A Primer on Zadoff Chu Sequences*, arXiv:2211.05702v1, first posted 2022-11-10. https://arxiv.org/abs/2211.05702
2. David Gregoratti, Xavier Arteaga, and Joaquim Broquetas, *Mathematical Properties of the Zadoff–Chu Sequences*, arXiv:2311.01035v1, first posted 2023-11-02. https://arxiv.org/abs/2311.01035
3. Tae-Kyo Lee and Kyeongcheol Yang, *Partial-Period Correlations of Zadoff–Chu Sequences and Their Relatives*, IEEE Transactions on Information Theory 60(9) (2014), 5791–5802, DOI:10.1109/TIT.2014.2334319 (bibliographic record and abstract examined, not complete text).
4. MSC2020, 42A05: Trigonometric polynomials, inequalities, extremal problems. https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=42A10
