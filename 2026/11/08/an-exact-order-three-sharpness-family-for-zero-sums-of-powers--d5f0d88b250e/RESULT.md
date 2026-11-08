# An exact order-three sharpness family for zero sums of powers

## Finding
For every integer \(u\geq0\), choose \(t=7u+4\) or \(t=7u+5\), and set
\[
q=2t+1,\qquad e=\frac{q^3-1}{14}=\frac{t(4t^2+6t+3)}7.
\]
Let \(m(q,e)\) be the smallest positive integer \(\ell\) for which a sum of \(\ell\) nonnegative integral powers of \(q\), with repetitions permitted, is divisible by \(e\). Then
\[
\boxed{m(q,e)=2t=q-1=2\gcd(e,q-1).}
\]
The minimum-length representations, upon reducing all exponents modulo \(3\), have exactly three possible multiplicity triples \((x_0,x_1,x_2)\), related by cyclic rotation. For \(t=7u+4\) one triple is \((8u+5,4u+2,2u+1)\); for \(t=7u+5\) it is \((4u+3,8u+6,2u+1)\). Each of the three rotations occurs.

More precisely, writing \(s_q(v)\) for the sum of the base-\(q\) digits of \(v\), the *entire* spectrum for the fourteen multiples of \(e\) below \(q^3\) is
\[
\big(s_q(je)/t\big)_{j=1}^{14}=(3,2,3,2,3,4,3,2,3,4,3,4,3,6).
\]
The unique minimizers among \(1\leq j<14\) are \(j=2,4,8\).

## Assumptions and scope
The integer \(t\) lies in exactly the two stated residue classes, so \(t\geq4\), \(q\geq9\), \(e\geq52\), and all displayed quotients are integers. The base need not be prime. The first source motivating the sharpness question was publicly available on 20 April 2022 (arXiv:2204.09403v1); the present result is confined to the displayed two progressions and asserts nothing about arbitrary \((q,e)\).

The number \(q\) is coprime to \(e\), because every common divisor of \(q\) and \(q^3-1\) is \(1\). Since \(q\equiv9\) or \(11\pmod{14}\), the quotient \(e\) is integral. We have \(q^3\equiv1\pmod e\) and \(q\not\equiv1\pmod e\), so the order of \(q\) modulo \(e\) is exactly \(3\). The factor \((q^2+q+1)/7\) is odd, whence \(\gcd(e,q-1)=\gcd(t( q^2+q+1)/7,2t)=t\).

## Proof
**Step 1 (a fourteen-entry digit identity).** Write \([v]_{14}\) for the representative in \(\{0,\ldots,13\}\) of an integer modulo \(14\). Fix \(1\leq j\leq13\), and set \(r_0=j\), \(r_1=[qj]_{14}\), \(r_2=[q^2j]_{14}\), \(r_3=[q^3j]_{14}=j\). As \(\gcd(q,14)=1\), the four residues are nonzero. Define \(d_i=(qr_{i-1}-r_i)/14\), for \(i=1,2,3\). These are integers between \(0\) and \(q-1\). Telescoping gives
\[
j(q^3-1)=14(d_1q^2+d_2q+d_3),
\]
so \((d_1,d_2,d_3)\) is the base-\(q\) three-digit expansion of \(je\). Summing the digit identities gives
\[
14s_q(je)=(q-1)(r_0+r_1+r_2),\qquad
s_q(je)=\frac t7\big(j+[9j]_{14}+[11j]_{14}\big),
\]
because \(\{q,q^2\}\pmod{14}=\{9,11\}\). Evaluating the thirteen integers \(1\leq j\leq13\) yields the first thirteen entries of the displayed spectrum. For \(j=14\) one has \(14e=q^3-1\), whose three digits are all \(q-1\), yielding \(s_q(14e)=6t\).

**Step 2 (minimality).** For any zero sum of \(\ell\) powers modulo \(e\), reduction modulo \(t\) gives \(\ell\equiv0\pmod t\), as \(q\equiv1\pmod t\) and \(t\mid e\). If \(0<\ell<2t\), then \(\ell=t\). Reduce every exponent modulo \(3\) using \(q^3\equiv1\pmod e\), and write the resulting integer as \(U=x_0+x_1q+x_2q^2\), where \(x_i\geq0\) and \(x_0+x_1+x_2=t\). Each \(x_i<q\), so \(U\) is already in base \(q\); also \(0<U<q^3\). Since \(e\mid U\), necessarily \(U=je\) for some \(1\leq j\leq14\). Yet \(s_q(U)=t\), contradicting Step 1, where every positive multiple below \(q^3\) has digit sum at least \(2t\). Thus \(m(q,e)\geq2t\).

**Step 3 (attainment and rigidity).** In the first residue class the identity
\[
2e=(8u+5)+(4u+2)q+(2u+1)q^2
\]
holds; in the second, the corresponding identity is
\[
2e=(4u+3)+(8u+6)q+(2u+1)q^2.
\]
All coefficients are nonnegative and their sum is \(2t=q-1\); this proves the matching upper bound. Now let any zero sum have length \(2t\), and reduce its exponents modulo \(3\). Its counts \(x_0,x_1,x_2\) are each at most \(q-1\), so again the resulting integer is a genuine base-\(q\) expansion below \(q^3\), of digit sum \(2t\). Step 1 forces \(U=je\) for \(j\in\{2,4,8\}\). Multiplication by \(q\) cyclically rotates the count triple modulo \(e\); the three listed multiples of \(e\) supply exactly these three rotations. This proves uniqueness of the three reduced-exponent multiplicity triples.

**Step 4 (sharpness).** In Jacob--Külshammer's Conjecture 4, \(e_1=\gcd(e,q-1)=t\). We have
\[
e=\frac{t(4t^2+6t+3)}7<(t+1)^3-1,
\]
so this infinite family achieves equality \(m(q,e)=2e_1\) in the proposed \(k=2\) bound. Also \(e/t^3\to4/7\). As \(q=14u+11\) is prime for infinitely many \(u\) by Dirichlet's theorem, sharpness remains valid along an infinite subfamily of prime bases.

## Verification
The standalone standard-library program `artifacts/verify.py` checks the fourteen-entry spectrum, the three minimizers, and all witness rotations at \(228\) admissible parameters with \(4\leq t\leq800\). It independently solves the shortest nonempty zero-sum problem by breadth-first search on all residue states for the \(20\) admissible parameters with \(t\leq68\), visiting a combined \(1,061,940\) residue states. It reports:

`VERIFY_OK residue_parameters=228 exhaustive_bfs_cases=20 complete_residue_states=1061940 exact_full14_spectrum=yes 3_witness_orbit=yes`

The proof of the infinite statement is Steps 1–4 above; the finite computations are independent checks, not an extrapolation.

## Relationship to prior work
Jacob and Külshammer (2022), Conjecture 4, ask for \(m(q,e)\leq k e_1\) when \(e<(e_1+1)^{k+1}-1\). Their published results do not state the present order-three equality and rigidity family. Breuer, Héthelyi, Horváth, and Külshammer (2019/2021), Proposition 2.22, provide the broader general digit-sum minimization procedure
\[
m(q,e)=\min_{1\leq j\leq(q^n-1)/e}s_q(je),\quad n=\operatorname{ord}_e(q),
\]
and a residue-orbit expression for its terms. The computation of the fourteen-entry spectrum here is a **specialization** of that established framework, not a new general minimization principle. The result's additional assertions concern a uniform infinite family saturating the later proposed cubic-range bound and the complete classification of its minimum-length multiplicity triples. No claim of priority is made for the generic digit formula.

## Limitations
This theorem verifies sharpness in one explicit two-progression family; it does not prove Conjecture 4 in general. The fourteen-entry computation is elementary given the prior digit-sum formula. Unindexed equivalent orbit evaluations may exist, and independent bibliographic or mathematical validation has not been performed. The result classifies reduced exponent multiplicities, not ordered tuples of arbitrary exponents or all nonminimal zero sums.

## References
1. L. Jacob and B. Külshammer, *Congruences for sums of powers of an integer*, arXiv:2204.09403v1 (first public 2022-04-20), Conjecture 4 and Section 2. https://arxiv.org/abs/2204.09403
2. T. Breuer, L. Héthelyi, E. Horváth, and B. Külshammer, *The Loewy Structure of Certain Fixpoint Algebras, Part II*, arXiv:1912.03065v1 (first public 2019-12-06), Proposition 2.22 and Remark 2.23; *International Electronic Journal of Algebra* **30** (2021), 16–65. https://arxiv.org/abs/1912.03065
