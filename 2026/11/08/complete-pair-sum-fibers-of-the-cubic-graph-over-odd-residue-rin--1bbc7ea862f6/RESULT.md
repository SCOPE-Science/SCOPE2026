# Complete pair-sum fibers of the cubic graph over odd residue rings

## Finding
For every odd integer \(q\ge3\), write \(R_q=\mathbb Z/q\mathbb Z\) and define the cubic graph
\[
C_q=\{(x,x^3):x\in R_q\}\subset R_q^2.
\]
For \((s,t)\in R_q^2\), let \(r_q(s,t)\) count ordered representations of \((s,t)\) as a sum of two points of \(C_q\). The theorem below determines **every** \(r_q(s,t)\), the size of \(C_q+C_q\), and its additive energy \(\mathcal E_q=\sum_{s,t}r_q(s,t)^2\).

First let \(q=p^k\), with \(p\) an odd prime and \(k\ge1\). Set \(w=4t-s^3\in R_{p^k}\), and define \(\alpha\in\{0,\ldots,k\}\) by \(\alpha=\min\{k,\nu_p(3s)\}\) using any integer representative of \(s\). This truncated valuation is representative-independent. If \(\alpha=k\), then
\[
r_{p^k}(s,t)=\begin{cases}p^k,&w=0,\\0,&w\ne0.\end{cases}
\]
If \(\alpha<k\), a necessary condition is \(p^\alpha\mid w\); otherwise \(r_{p^k}(s,t)=0\). When it holds, write \(j=k-\alpha\), let \(v=3s/p^\alpha\), a unit modulo \(p^j\), and define
\[
c\equiv (w/p^\alpha)v^{-1}\pmod {p^j}.
\]
Then \(r_{p^k}(s,t)=p^\alpha R_p(j,c)\), where the **exact square-root count** is
\[
R_p(j,c)=\begin{cases}
p^{\lfloor j/2\rfloor},&c\equiv0\pmod {p^j},\\
2p^h,&\nu_p(c)=2h<j\text{ and }\left(\frac{c/p^{2h}}p\right)=1,\\
0,&\text{otherwise}.
\end{cases}
\]
Here \((\frac\cdot p)\) denotes the Legendre symbol of the reduced unit. In particular the above formulas cover every target, including nonattained targets and the singular prime \(p=3\).

Define, for \(j\ge1\), the number of quadratic residues including zero in \(\mathbb Z/p^j\mathbb Z\):
\[
Q_p(j)=1+\frac{p-1}{2}\sum_{h=0}^{\lfloor (j-1)/2\rfloor}p^{j-2h-1}.
\]
Then the exact twofold sumset cardinality is
\[
|C_{p^k}+C_{p^k}|=
\begin{cases}
1+(p-1)\displaystyle\sum_{j=1}^{k}p^{j-1}Q_p(j),&p\ne3,\\[2mm]
3+2\displaystyle\sum_{j=1}^{k-1}3^jQ_3(j),&p=3,
\end{cases}
\]
and the exact additive energy is
\[
\boxed{\mathcal E_{p^k}=
\begin{cases}
p^{2k}+(p-1)p^{2k-2}\left(kp+\frac{(p-1)k(k+1)}2\right),&p\ne3,\\[2mm]
3^{2k-1}(2k^2+4k+3),&p=3.
\end{cases}}
\]
For every odd \(q=\prod_{p^k\parallel q}p^k\), the Chinese remainder theorem yields the complete local-to-global formulas
\[
r_q(s,t)=\prod_{p^k\parallel q}r_{p^k}(s,t),\qquad
|C_q+C_q|=\prod_{p^k\parallel q}|C_{p^k}+C_{p^k}|,\qquad
\mathcal E_q=\prod_{p^k\parallel q}\mathcal E_{p^k}.
\]
The local factors evaluate \((s,t)\) modulo the corresponding prime power. In the Fourier normalization \(e_q(z)=\exp(2\pi iz/q)\), the same energy is the complete unweighted fourth moment
\[
\mathcal E_q=q^{-2}\sum_{a,b\bmod q}\left|\sum_{x\bmod q}e_q(ax+bx^3)\right|^4.
\]

## Assumptions and scope
All rings are \(\mathbb Z/q\mathbb Z\) with **odd** \(q\ge3\). Elements, sums and products are taken modulo the indicated modulus. The pair-sum representations count **ordered** pairs of graph points, hence \(\sum_{s,t}r_q(s,t)=q^2\). The \(p\)-adic valuation of a zero residue modulo \(p^k\) is truncated to \(k\). Quotienting \(w/p^\alpha\) when \(p^\alpha\mid w\) means reducing an integer divisible by \(p^\alpha\) modulo \(p^{k-\alpha}\); it does not depend on the chosen representative. Likewise \(3s/p^\alpha\) defines an invertible residue in that quotient. The Legendre-symbol branch applies only to the nonzero unit after removal of the exact even valuation.

## Proof
**1. Reduce each fiber to quadratic roots.** Since \(2\) and \(4\) are units for every odd modulus, the substitution \(u=x-y\) at fixed \(x+y=s\) is bijective between \(x\in R_q\) and \(u\in R_q\). Direct expansion gives
\[
4(x^3+y^3)=s^3+3su^2.
\]
Thus a pair contributes exactly when \(3su^2\equiv4t-s^3\pmod {p^k}\). If \(3s\equiv0\pmod {p^k}\), every one of the \(p^k\) values of \(u\) works for \(w=0\) and none otherwise. Otherwise factor \(3s=p^\alpha v\) with \(\alpha<k\), where \(v\) is a unit modulo \(p^{k-\alpha}\). If \(w\) is not divisible by \(p^\alpha\), there are no solutions. If it is, division gives \(u^2\equiv c\pmod{p^{k-\alpha}}\). Each solution in the quotient has exactly \(p^\alpha\) lifts modulo \(p^k\). This proves the displayed fiber reduction with no genericity assumption on \(s\) or \(t\).

**2. Count quadratic roots.** Let \(j\ge1\). For \(c\equiv0\pmod{p^j}\), the solutions of \(u^2\equiv0\pmod{p^j}\) are the multiples of \(p^{\lceil j/2\rceil}\), giving \(p^{\lfloor j/2\rfloor}\) roots. If \(\nu_p(c)=d<j\), any solution must have \(2\nu_p(u)=d\), hence \(d=2h\) even. Dividing by \(p^{2h}\) reduces to a unit-square congruence modulo \(p^{j-2h}\). Since \(p\) is odd, an invertible quadratic residue has precisely two roots modulo every \(p^m\) by the usual one-step Hensel lifting (the derivative \(2u\) is invertible), while a quadratic nonresidue has none. Each root has \(p^h\) lifts for \(u/p^h\) modulo \(p^{j-h}\). Therefore the exact count is \(R_p(j,c)\) above.

**3. Count attained targets.** Nonzero quadratic residues modulo \(p^j\) have valuations \(2h<j\). For a fixed \(h\), the unit part is a unit square modulo \(p^{j-2h}\), of which there are \(\varphi(p^{j-2h})/2=(p-1)p^{j-2h-1}/2\). Together with zero this proves \(Q_p(j)\).

When \(p\ne3\), the sum coordinate \(s=0\) gives one target \(t=0\). For each \(a=0,\ldots,k-1\), there are \((p-1)p^{k-a-1}\) coordinates \(s\) of exact valuation \(a\). For such \(s\) the fiber reduction has \(j=k-a\), and multiplication by a unit and translation preserve the number of possible targets \(t\). Exactly \(Q_p(j)\) choices occur. Reindexing \(j=k-a\) yields the first support formula.

For \(p=3\), the three coordinates \(s\equiv0\pmod {3^{k-1}}\) all satisfy \(3s\equiv0\pmod {3^k}\) and each has exactly one target. For each \(a=0,\ldots,k-2\), the \(2\cdot3^{k-a-1}\) coordinates of exact valuation \(a\) satisfy \(\nu_3(3s)=a+1\). Thus \(j=k-a-1\) and exactly \(Q_3(j)\) targets occur per \(s\). This proves the second support formula; for \(k=1\) the remaining sum is empty, as required.

**4. Second moment of quadratic-root fibers.** Put \(S_p(j)=\sum_{c\bmod p^j} R_p(j,c)^2\). It counts pairs \((u,v)\in (\mathbb Z/p^j\mathbb Z)^2\) satisfying \(u^2=v^2\). Since \(2\) is a unit, the invertible linear change to \((u-v,u+v)\) identifies this with the pairs \((a,b)\) for which \(ab\equiv0\pmod {p^j}\). For each \(a\) of valuation \(h<j\) there are \(p^h\) choices of \(b\), and there are \((p-1)p^{j-h-1}\) such \(a\); the unique \(a=0\) allows \(p^j\) choices. Therefore
\[
S_p(j)=p^j+j(p-1)p^{j-1}=p^{j-1}\bigl(p+j(p-1)\bigr).
\]
For \(p\ne3\), the singular coordinate \(s=0\) contributes \(p^{2k}\) to the energy. At a coordinate \(s\) of exact valuation \(a<k\), the support targets correspond bijectively to the \(c\in\mathbb Z/p^{k-a}\mathbb Z\), and the fiber weights are \(p^aR_p(k-a,c)\). Hence the squared-fiber sum for that \(s\) is \(p^{2a}S_p(k-a)\). Counting \((p-1)p^{k-a-1}\) such \(s\), the contribution per \(j=k-a\) is \((p-1)p^{2k-2}[p+j(p-1)]\). Summing \(j=1,\ldots,k\) gives the first closed energy formula.

For \(p=3\), the three singular sum coordinates contribute \(3\cdot3^{2k}\). At a nonsingular coordinate with exact valuation \(a<k-1\), the fiber factor is \(3^{a+1}\), and the quotient exponent is \(j=k-a-1\). Multiplying its squared-fiber sum by the \(2\cdot3^{k-a-1}\) possible coordinates gives \(2\cdot3^{2k-1}(3+2j)\). Thus
\[
\mathcal E_{3^k}=3\cdot3^{2k}+2\cdot3^{2k-1}\sum_{j=1}^{k-1}(3+2j)
=3^{2k-1}(2k^2+4k+3).
\]
This includes \(k=1\), when the sum is empty.

**5. Chinese remainder and Fourier identities.** The Chinese remainder isomorphism identifies \(R_q^2\) with the product of \(R_{p^k}^2\), and identifies the graph points, their twofold sums and every ordered fiber with the corresponding products. Hence all three invariants factor, and the support formula holds at every odd modulus. Finally, expanding the fourth power of the complete exponential sum and applying additive-character orthogonality in the two ambient coordinates gives \(q^2\) for each additive collision and zero for each noncollision. Dividing by \(q^2\) yields the displayed fourth-moment formula.

## Verification
The standalone finite direct enumeration in `verify.py` compares the formula with all ordered pairs and **every** target fiber modulo each of 13 prime powers (through modulus \(125\)); it also checks support sizes and additive energies for those moduli. It repeats CRT comparisons for five composite odd moduli, including non-squarefree cases. It performs exact integer calculations only and requires no nonstandard libraries. Run `python3 verify.py`; the expected final line is `VERIFY_OK local_cases=13 composite_cases=5 max_modulus=125`. These finite tests corroborate but do not establish the unbounded theorem; the steps above do.

## Relationship to prior work
The cubic collision factorization is classical and appears for bounded integer cubic Weyl sums in Wooley [1] and Hughes–Wooley [2]. Those papers address mean-value bounds for integer intervals, not the exact ordered two-sum representation function at every target modulo prime powers. Hickman–Wright [3] study polynomial graphs and Fourier restriction on general residue rings, but the inspected arguments supply general analytic estimates rather than the explicit target-by-target cubic-graph fiber and its arithmetic singular-prime census. The published finite-field cubic-graph fourth-moment study [4] uses the same identity at the nonsingular **field** level and determines a sharp operator norm, but not the prime-power fiber distribution or the \(p=3\) branch. The published cubic-graph prime-square spectra study [5] classifies orthogonal frequency bases, a different invariant. The present elementary prime-power square-root census unifies all targets, exact pair-sum sizes, and the complete unweighted fourth moments; it does not claim the factorization or quadratic-root lemma as new.

## Limitations
No assertion is made for even moduli, arbitrary weights, higher polynomial degrees or higher additive moments. The formula does not classify maximizing weighted fourth-moment functions. Historical equivalence with a general polynomial-congruence representation formula or an unindexed older cubic local-density computation cannot be definitively excluded. Independent validation has not been performed.

## References
1. T. D. Wooley, “Mean value estimates for odd cubic Weyl sums,” arXiv:1401.7152v1 (first public 2014-01-28), later *Bull. London Math. Soc.* 47 (2015), 946–957. In particular, the cubic collision factorization in Lemma 2.2.
2. K. Hughes and T. D. Wooley, “Discrete restriction for \((x,x^3)\) and related topics,” arXiv:1911.12262v1 (2019), §2; finite **interval** moment bounds.
3. J. Hickman and J. Wright, “The Fourier restriction and Kakeya problems over rings of integers modulo \(N\),” arXiv:1801.03176v2 (2018), especially §§6.5–7; general modular polynomial-curve theory.
4. “Exact sharp finite-field cubic-graph \(L^2\) to \(L^4\) extension norm and extremizers,” public mathematical research result, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-sharp-finite-field-cubic-graph-l-2-to-l-4-extension-norm-a--2db777d1e47b/RESULT.md (read complete scientific statement and proof).
5. “All exponential spectra of the cubic graph over prime-square cyclic rings,” public mathematical research result, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-all-exponential-spectra-of-the-cubic-graph-over-prime-square-cyc--a783058468ac/RESULT.md (read complete scientific statement and proof).
