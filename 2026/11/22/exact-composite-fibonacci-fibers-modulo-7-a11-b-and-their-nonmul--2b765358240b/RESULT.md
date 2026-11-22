# Exact composite Fibonacci fibers modulo \(7^a11^b\) and their nonmultiplicative density

## Finding

Let \(F_0=0\), \(F_1=1\), and \(F_{n+2}=F_{n+1}+F_n\). For integers \(a,b\ge1\) set \(m=7^a11^b\), \(T_{a,b}=80\cdot7^{a-1}11^{b-1}\), and
\[
V_{a,b}(x)=\#\{0\le n<T_{a,b}:F_n\equiv x\pmod m\}.
\]
**Theorem.** The least period of \(F_n\pmod m\) is \(T_{a,b}\). The exact frequency of every residue \(x\pmod m\) is
\[
\boxed{V_{a,b}(x)=E_{7,a}(x)E_{11,b}(x)+O_{7,a}(x)O_{11,b}(x),}
\]
where the factors below depend only on their indicated prime-power residue.

For \(y\pmod{7^a}\), if \(y\pmod7\in\{0,1,2,5,6\}\), the pair \((E_{7,a}(y),O_{7,a}(y))\) is given respectively by
\[
0:(2,0),\quad1:(2,2),\quad2:(0,2),\quad5:(0,2),\quad6:(2,2).
\]
For \(y\equiv3,4\pmod7\), put \((E_{7,a}(y),O_{7,a}(y))=(R_{7,a}(5y^2+4),0)\).

For \(z\pmod{11^b}\), if \(z\pmod{11}\in\{0,1,2,3,8,10\}\), the pair \((E_{11,b}(z),O_{11,b}(z))\) is respectively
\[
0:(1,0),\quad1:(1,2),\quad2:(0,2),\quad3:(1,0),\quad8:(1,0),\quad10:(1,0).
\]
For \(z\equiv5\pmod{11}\), put \((E_{11,b}(z),O_{11,b}(z))=(0,R_{11,b}(5z^2-4))\). Every unlisted residue has pair \((0,0)\).

For \(p\in\{7,11\}\), define the **divisible-root count**
\[
R_{p,k}(D)=\#\{u\pmod{p^k}:p\mid u,\ u^2\equiv D\pmod{p^k}\}.
\]
Let \(d=D\bmod p^k\), represented in \([0,p^k)\). Then \(R_{p,k}(D)=p^{\lfloor k/2\rfloor}\) if \(d=0\); if \(\nu_p(d)=2h\) with \(h\ge1\), \(2h<k\), and \(d/p^{2h}\) a quadratic residue modulo \(p\), then \(R_{p,k}(D)=2p^h\); in all other cases it is zero. This gives a closed integer formula for **every** residue frequency without enumerating an orbit.

Write \(Q_p(j)=1+\sum_{h=0}^{\lfloor(j-1)/2\rfloor}\frac{p-1}{2}p^{j-2h-1}\) for \(j\ge1\), and \(Q_p(j)=1\) for \(j\le0\). The number of residues attained modulo \(m\) is exactly
\[
\boxed{N_{a,b}=21\cdot7^{a-1}11^{b-1}+10\cdot11^{b-1}Q_7(a-2)+4\cdot7^{a-1}Q_{11}(b-2).}
\]
In particular \(N_{1,1}=35\) modulo \(77\), and the limiting two-prime image density is
\[
\boxed{\lim_{a,b\to\infty}\frac{N_{a,b}}{7^a11^b}=\frac{523}{1848}.}
\]
The limit holds along **any** path with both exponents tending to infinity. In contrast, the product of the separate prime-power limiting image densities is \((41/56)(145/264)=5945/14784\), strictly greater than \(523/1848\), by exactly \(587/4928\). The discrepancy is explained by incompatible index parity, not a failure of the ordinary Chinese remainder theorem.

## Assumptions and scope

The theorem concerns only the classical Fibonacci sequence, positive integer exponents \(a,b\), indices starting at zero, and the least *scalar* period. The two factors \(E_{p,k}\) and \(O_{p,k}\) count even and odd indices respectively **within one least Fibonacci period modulo \(p^k\)**; they are not probabilities. Quadratic-residue tests in the root count refer to the nonzero unit modulo the specified prime. The single-index case \(k=1\) uses the zero-root case and is included.

## Proof

**1. Exact local periods.** Put \(M=\begin{pmatrix}1&1\\1&0\end{pmatrix}\), so that its upper off-diagonal entry in \(M^n\) is \(F_n\). Direct multiplication gives
\[
M^{16}=\begin{pmatrix}1597&987\\987&610\end{pmatrix}=I+7\begin{pmatrix}228&141\\141&87\end{pmatrix},
\]
\[
M^{10}=\begin{pmatrix}89&55\\55&34\end{pmatrix}=I+11\begin{pmatrix}8&5\\5&3\end{pmatrix}.
\]
The orders modulo \(7\) and \(11\) are exactly \(16\) and \(10\), verified directly using the Fibonacci state. Both displayed matrices have a unit off-diagonal entry after division by their prime. For odd primes, binomial expansion of \((I+pB)^{p^jt}\) with \(p\nmid t\) implies the off-diagonal entry has valuation \(j+1\). Thus for all nonzero integers \(d\),
\[
\nu_7(F_{16d})=1+\nu_7(d),\qquad \nu_{11}(F_{10d})=1+\nu_{11}(d).
\]
The least Fibonacci periods are \(P_{7,a}=16\cdot7^{a-1}\) and \(P_{11,b}=10\cdot11^{b-1}\): returning the state \((F_n,F_{n+1})=(0,1)\) forces \(M^n=I\). Their greatest common divisor is exactly \(2\), so the least composite period is their least common multiple \(T_{a,b}\).

**2. Regular local branches.** Define the Lucas companion \(L_n=F_{n-1}+F_{n+1}\) for \(n\ge1\), with \(L_0=2\). For even \(h\), the addition identity
\[
2(F_{n+h}-F_n)=(L_h-2)F_n+F_hL_n
\tag{1}
\]
holds. Moreover \(L_h^2-5F_h^2=4\) for even \(h\). For \(h\) divisible by a local period \(P\), \(L_h+2\) is a prime-adic unit and hence
\[
\nu_p(L_h-2)=2+2\nu_p(h/P)
\]
for \(p=7\), \(P=16\), or \(p=11\), \(P=10\); the valuations of \(F_h\) are \(1+\nu_p(h/P)\). On each index branch \(n=r+Pt\) where \(p\nmid L_r\), (1) therefore gives the exact isometry
\[
\nu_p(F_{r+Pt'}-F_{r+Pt})=1+\nu_p(t'-t).
\tag{2}
\]
Thus this branch takes each target in its fixed residue class modulo \(p\) exactly once as \(t\) ranges over \(\mathbb Z/p^{k-1}\mathbb Z\). Its parity is the parity of \(r\), since the periods are even. Enumerating the 16 Fibonacci/Lucas pairs modulo 7 and ten pairs modulo 11 gives exactly the regular rows in the theorem's tables. The excluded indices are \(r=4,12\pmod{16}\) at 7 (both even) and \(r=5\pmod{10}\) at 11 (odd), exactly the positions with \(L_r\equiv0\) modulo the respective prime.

**3. Critical local branches.** The companion addition identity
\[
2(L_{n+h}-L_n)=(L_h-2)L_n+5F_hF_n
\tag{3}
\]
shows, by the same valuations and the fact that \(F_r\) is a unit at each excluded index, that
\[
\nu_p(L_{r+Pt'}-L_{r+Pt})=1+\nu_p(t'-t).
\tag{4}
\]
Consequently the critical Lucas values range bijectively over \(p\mathbb Z_p\), at each finite precision. The companion identity
\[
L_n^2-5F_n^2=4(-1)^n
\tag{5}
\]
becomes \(L_n^2=5F_n^2+4\) at the two even 7-adic branches, and \(L_n^2=5F_n^2-4\) at the odd 11-adic branch. In the respective critical target classes \(F_n\equiv3,4\pmod7\) and \(F_n\equiv5\pmod{11}\), the derivative \(10F_n\) is a unit. Hence Hensel's lemma makes the quadratic relation (5) bijective between target \(F_n\)-values and the indicated \(L_n^2\)-values, preserving counts of index parameters. By (4) the number of indices attaining a target is precisely the number of square roots of its corresponding \(D\) that are divisible by \(p\), proving the exceptional table entries. Ordinary quadratic-congruence lifting gives the displayed cases for \(R_{p,k}\): a square's valuation is even, a nonzero square unit has two roots, and a root with valuation \(h\) has \(p^h\) lifts at the given precision.

**4. Parity-synchronized CRT and support.** Fix a composite target \(x\). Each solution class modulo \(P_{7,a}\) has a definite parity, as does each solution class modulo \(P_{11,b}\). The generalized Chinese remainder theorem gives a unique simultaneous index modulo \(T_{a,b}\) exactly when these parities agree. This proves the product-sum formula for \(V_{a,b}\), including zero fibers. The seven-adic *even* support comprises three full residue disks plus two critical square images, the *odd* support four full disks, and their intersection two full disks. Their sizes are respectively \(3\cdot7^{a-1}+2Q_7(a-2)\), \(4\cdot7^{a-1}\), and \(2\cdot7^{a-1}\). The eleven-adic even and odd supports are respectively \(5\cdot11^{b-1}\) and \(2\cdot11^{b-1}+Q_{11}(b-2)\); their intersection is one full disk of size \(11^{b-1}\). Therefore inclusion-exclusion for the two parity-compatible Cartesian products yields exactly the claimed \(N_{a,b}\).

Finally the proportion of squares in \(\mathbb Z_p\) has measure \(\frac{p}{2(p+1)}\), so \(Q_p(j)/p^{j}\to p/(2(p+1))\). In particular \(Q_7(a-2)/7^a\to1/112\) and \(Q_{11}(b-2)/11^b\to1/264\). Substitution into the exact finite formula yields \(523/1848\), as claimed.

## Verification

The independent recurrence-based checker `artifacts/verify_fibonacci_composite.py` enumerates complete least periods, compares **all** predicted parity-resolved fibers locally for each prime at exponents one through five, and checks **all** predicted composite fibers for the exponent pairs \((1,1),(2,1),(1,2),(2,2),(3,2),(2,3),(3,3)\). It recomputes support sizes from the observed orbit and from the closed formula, verifying for example \(N_{1,1}=35\), \(N_{2,2}=1755\) and \(N_{3,3}=130525\). The script passed and printed `VERIFY_OK all local and composite parity fibers and exact support`. These are finite tests; the proof establishes the infinite family.

## Relationship to prior work

Bragman and Rowland (arXiv:2202.00704, first public 2022-02-01) analyze prime-power Fibonacci image density, including the known seven-adic density \(41/56\) and the seven-adic residue tree. They do **not** assert the mixed-modulus exact parity-coupled frequency law or its limiting \(523/1848\) density. The prime-power density \(41/56\) is credited, not new. Existing research also gives exact eleven-adic local Fibonacci fibers and exact seven-adic **Lucas** fibers; neither statement alone determines the composite Fibonacci frequencies because parity compatibility between distinct local periods must be resolved. The latter Lucas work supplies a closely analogous square-root lifting technique, explicitly credited here. The present theorem treats synchronized Fibonacci indices and gives an exact support law not present in the inspected statements. General recurrence frequency bounds, such as Carlip and Somer (2007), are broader in topic but do not state these concrete mixed fibers or exact density. An unindexed equivalent result or a hidden deduction from a more general p-adic interpolation statement remains possible; this result is not independently audited.

## Limitations

Only moduli of the form \(7^a11^b\) with both exponents positive are covered. The exact output support is not the same as equidistribution, and the values attained at other composite moduli are not classified. The numerical limit is a two-parameter limit as both exponents increase. Finite checker coverage is not an infinite certificate. Originality is assessed against inspected literature and indexed findings and remains subject to independent bibliographic review.

## References

1. Nicholas Bragman and Eric Rowland, *Limiting density of the Fibonacci sequence modulo powers of a prime*, arXiv:2202.00704 (first posted 2022-02-01), https://arxiv.org/abs/2202.00704. See especially Example 5 and the prime-power tree discussion.
2. William Carlip and Lawrence Somer, *Bounds for frequencies of residues of second-order recurrences modulo prime powers*, Mathematica Bohemica 132 (2007), 137–175, DOI:10.21136/MB.2007.134189, https://dml.cz/bitstream/handle/10338.dmlcz/134189/MathBohem_132-2007-2_3.pdf.
3. *Exact seven-adic Lucas residue fibers and the \(41/56\) range measure*, publicly indexed mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-seven-adic-lucas-residue-fibers-and-the-41-56-range-measur--be34cdadeedf.
4. C. L. Lang and M. L. Lang, *Fibonacci system and residue completeness*, arXiv:1304.2892 (2013), https://arxiv.org/abs/1304.2892.
