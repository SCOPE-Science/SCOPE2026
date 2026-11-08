# Universal three-moment closure and exact energy of the modular cubic curve

## Finding
For \(N\ge1\), write \(R_N=\mathbb Z/N\mathbb Z\), and define \(J_{2,3}(N)\) as the number of ordered quadruples \((x,y,z,w)\in R_N^4\) satisfying
\[
x^j+y^j=z^j+w^j\quad\text{in }R_N\quad(j=1,2,3).
\]
Then, for every \(j\ge1\), all such quadruples also satisfy \(x^j+y^j=z^j+w^j\). Moreover, the exact number is the following multiplicative arithmetic function:
\[
J_{2,3}(p^k)=
\begin{cases}
p^{2k-1}\bigl(p+k(p-1)\bigr),&p\text{ odd},\\
k2^{2k},&p=2,\ k\ge2,\\
8,&p=2,\ k=1,
\end{cases}
\qquad J_{2,3}(1)=1.
\]
The least number of *initial* power sums required to guarantee equality of all positive power sums for every pair of pairs in \(R_N\) is \(1\) for \(N=2\), \(2\) for \(N>2\) with \(4\nmid N\), and \(3\) when \(4\mid N\) (with a trivial singleton case \(N=1\)).

## Assumptions and scope
All moduli are positive integers, all variables run over complete residue systems, and all quadruples are **ordered**. The count is the additive energy of the modular cubic moment curve \(\{(t,t^2,t^3):t\in R_N\}\), not a count of integer solutions restricted to a box. The term \(p^k\parallel N\) denotes an exact prime-power divisor; the formula for a general \(N\) is the product of its displayed prime-power factors.

## Proof
**1. Reduction to two parameters.** Equality of the first moments allows the unique parametrization
\[
 z=x-a,\qquad w=x-b,\qquad y=x-a-b,
\]
with \((x,a,b)\in R_N^3\). Set \(s=x+y=2x-a-b\) and \(\Delta=zw-xy=ab\). Direct expansion yields
\[
(x^2+y^2)-(z^2+w^2)=2ab,\qquad
(x^3+y^3)-(z^3+w^3)=3s ab.
\]
Thus the three-moment conditions are precisely \(2ab=3s ab=0\) in \(R_N\).

**2. Equality of every higher moment.** By the Chinese remainder theorem it suffices to work modulo prime powers. For an odd prime power, \(2ab=0\) implies \(ab=0\), so the two pairs have identical sum \(s\) and product. Their entire sequences of power sums are therefore identical, since the power sums \(P_j(s,t)\) satisfy \(P_0=2\), \(P_1=s\), and \(P_j=sP_{j-1}-tP_{j-2}\).

Modulo \(2\), \(u^j=u\) for every positive \(j\) and every residue \(u\); the first moment alone suffices. Modulo \(2^k\) with \(k\ge2\), the condition \(2ab=0\) says that either \(ab=0\) or \(ab=2^{k-1}\) as residues. In the latter case \(3s ab=0\) forces \(s\) even. For every \(t\in R_{2^k}\), the recurrence above shows that \(P_j(s,t)\) is even for all \(j\ge0\) whenever \(s\) is even. Two recurrences with the same sum \(s\) and product parameters differing by \(\Delta=2^{k-1}\) satisfy
\[
P_j(s,t+\Delta)-P_j(s,t)
=s\bigl(P_{j-1}(s,t+\Delta)-P_{j-1}(s,t)\bigr)
-(t+\Delta)\bigl(P_{j-2}(s,t+\Delta)-P_{j-2}(s,t)\bigr)
-\Delta P_{j-2}(s,t).
\]
The last term vanishes modulo \(2^k\), because \(P_{j-2}(s,t)\) is even. The difference is zero for \(j=0,1\), and induction proves it is zero for all \(j\ge0\). This proves universal three-moment closure.

**3. Counting odd prime-power collisions.** If \(N=p^k\) with \(p\) odd, the condition reduces to \(p^k\mid ab\). The number of eligible \((a,b)\) is
\[
\sum_{a\bmod p^k}\gcd(a,p^k)
=p^k+k(p-1)p^{k-1}.
\]
Indeed the \(p\)-adic valuation classes \(0\le i<k\) each contribute \((p-1)p^{k-1}\), while \(a=0\) contributes \(p^k\). There are independently \(p^k\) choices of \(x\), yielding \(J_{2,3}(p^k)=p^{2k-1}(p+k(p-1))\).

**4. Counting dyadic collisions.** For \(N=2^k\), \(k\ge2\), the \((a,b)\) with \(ab=0\pmod{2^k}\) number \(2^{k-1}(k+2)\) by the same valuation sum. In the additional case \(ab=2^{k-1}\pmod{2^k}\), the cubic condition holds iff \(s=2x-a-b\) is even, equivalently \(a+b\) is even. This forces both \(a\) and \(b\) even, with valuations \(i,j\ge1\) and \(i+j=k-1\). Each of the \(k-2\) possible ordered valuation splits has \(2^{k-1}\) pairs, giving \((k-2)2^{k-1}\) more. The total is therefore \(k2^k\) admissible \((a,b)\); multiplying by \(2^k\) choices of \(x\) gives \(k2^{2k}\). Modulo \(2\), any first-moment equality is sufficient: there are \(2^3=8\) quadruples.

**5. Chinese remainder theorem and sharp initial-moment threshold.** Independent local quadruple conditions prove multiplicativity. If \(4\nmid N\), every local prime-power component requires at most the first two moments. If \(4\mid N\), take modulo \(N\) the explicit quadruple
\[
(x,y,z,w)=\bigl(0,-1-N/2,-1,-N/2\bigr).
\]
Its first two power sums agree, while the difference of the third power sums is \(3s(N/2)\not\equiv0\pmod N\), because \(s=-1-N/2\) is odd. Finally, if \(N>2\), the pairs \((0,0)\) and \((1,-1)\) have equal first sums but unequal second sums, so one moment is insufficient. The special \(N=2\) case follows from \(u^j=u\); \(N=1\) is trivial.

## Verification
Run the embedded `verify_cubic_moment_energy.py` under Python 3 with the standard library only. It independently counts solutions by grouping ordered residue pairs according to their first three moments for every \(1\le N\le84\) and checks the multiplicative closed formula. It also checks, for \(1\le N\le54\), that congruent first-three-moment triples have matching power sums of degrees \(4\) through \(15\); all predicted two-moment counterexamples are checked. These finite checks do not establish the unbounded claims: those follow from the algebraic and valuation arguments above.

## Relationship to prior work
Wooley's cubic Vinogradov mean-value paper, first publicly available in January 2014, establishes estimates for *integer* equal-power-sum systems and discusses diagonal solutions when only two summands are present. It does not give the exact full-residue modular local factors here, nor the dyadic stabilization of **all** higher power sums from the first three.

Iosevich--Li--Yu later relate modular moment-curve Fourier norms to congruence counts; independently, a published calculation of the **sixth** moment for the cubic curve at squarefree moduli coprime to six studies *three-versus-three* collisions. Neither statement evaluates the present **fourth** energy over every prime power. Local weighted extension norms for parabolas and scalar polynomial graphs concern different objects and do not imply this formula.

## Limitations
This determines the **unweighted, constant-coefficient fourth moment** and the minimal initial-moment closure threshold, but not the optimal weighted \(\ell^2\to L^4\) Fourier extension norm or its extremizers. It does not count three-versus-three collisions modulo prime powers. Historical priority is not independently certified: equivalent modular symmetric-function identities could appear in older sources not located in the inspected literature. No independent mathematical audit has been conducted.

## References
T. D. Wooley, *The cubic case of the main conjecture in Vinogradov's mean value theorem*, arXiv:1401.3150v1 (first submitted 14 January 2014), especially its introductory discussion of the cubic moment system.

A. Iosevich, Z. Li, and K. Yu, *Spectral synthesis with the complexity parameter in \(\mathbb Z_N^d\)*, arXiv:2609.25404v1 (later related framework; not the archival originating source).
