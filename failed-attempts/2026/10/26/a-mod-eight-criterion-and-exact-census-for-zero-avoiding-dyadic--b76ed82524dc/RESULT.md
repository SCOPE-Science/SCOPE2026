# A mod-eight criterion and exact census for zero-avoiding dyadic Fibonacci orbits

## Finding

Let \(k\ge1\) and define the invertible Fibonacci update \(T(a,b)=(b,a+b)\) on \((\mathbb Z/2^k\mathbb Z)^2\). A pair is **zero-avoiding** when neither coordinate of any forward iterate is congruent to zero modulo \(2^k\). Let \(j\) be the common dyadic depth of the pair: the largest \(0\le j\le k\) for which both coordinates are divisible by \(2^j\). If \(j<k\), set \(h=k-j\) and let \(A=a/2^j\), \(B=b/2^j\) modulo \(2^h\).

**Exact criterion.** The pair is zero-avoiding if and only if \(h\ge3\) and
\[
 A^2+AB-B^2\equiv3\text{ or }5\pmod8.
\]
In particular, all pairs for \(k=1,2\) encounter zero. For \(k\ge3\), the total number of zero-avoiding ordered initial pairs is exactly
\[
 Z(k)=2^{2k-1}-8.
\]
More finely, for every \(h=3,\ldots,k\), there are exactly \(2^{h-2}\) zero-avoiding orbits of common depth \(j=k-h\); each has least period \(3\cdot2^{h-1}\). Consequently their total number of cycles is \(2^{k-1}-2\). The proportion of all initial pairs that avoid zero tends to \(1/2\) as \(k\) grows.

## Assumptions and scope

All pairs, including nonprimitive pairs, are counted **once as ordered residue pairs**. The zero pair is not zero-avoiding. The recurrence is computed in the indicated ring; no restriction to unit-valued sequences is imposed. If \(j<k\), division by \(2^j\) denotes choosing the unique primitive residual pair modulo \(2^h\); its parity profile is independent of integer representatives. The criterion uses its residues modulo eight only when \(h\ge3\).

## Proof

**1. Primitive periods.** Use the integral matrix
\[
 M=\begin{pmatrix}0&1\\1&1\end{pmatrix},\qquad
 M^3=I+2M,\qquad M^6=I+4M^3.
\]
For every \(r\ge0\), a direct induction by squaring yields
\[
 M^{3\cdot2^r}=I+2^{r+1}U_r,
\]
with \(U_r\) invertible modulo two. At \(r=0\), \(U_0=M\); at \(r=1\), \(U_1=M^3\). For \(r\ge1\), squaring gives \(U_{r+1}=U_r+2^rU_r^2\), so the reductions stay invertible. If \(u\) is odd, binomial expansion shows \(M^{u3\cdot2^r}-I\) divided by \(2^{r+1}\) is also invertible modulo two. Since \(M\) permutes the three nonzero pairs modulo two in a three-cycle, every primitive pair modulo \(2^h\) has **least period**
\[
 \pi_h=3\cdot2^{h-1} \qquad(h\ge1).
\]
Indeed, any period is divisible by three; writing its quotient by three as \(2^ru\) with \(u\) odd, the matrix displacement cannot annihilate a primitive vector unless \(r+1\ge h\). Conversely \(M^{\pi_h}=I\pmod{2^h}\).

**2. Exact zero spacing.** Let \(F_0=0\), \(F_1=1\), \(F_{n+2}=F_{n+1}+F_n\). The matrix identity \(M^n=F_{n-1}I+F_nM\) holds for positive \(n\). Direct recurrence calculation modulo eight, with period twelve, shows
\[
 8\mid F_n\quad\Longleftrightarrow\quad 6\mid n.
\]
Also \(M^6=5I+8M\). For \(n=6\cdot2^r\), express \(M^n=a_r I+b_r M\). Initially \(a_0=5\), \(b_0=8\); squaring and \(M^2=I+M\) gives
\[
 a_{r+1}=a_r^2+b_r^2,\qquad b_{r+1}=b_r(2a_r+b_r).
\]
Here all \(a_r\) are odd and \(8\mid b_r\), hence \(\nu_2(2a_r+b_r)=1\) and \(\nu_2(b_r)=r+3\). Raising \(a_rI+b_rM\) to an odd positive power \(u\), the coefficient of \(M\) is congruent to \(u a_r^{u-1}b_r\) modulo \(b_r^2\), and therefore still has exact valuation \(r+3\). Thus
\[
 \nu_2(F_{6t})=3+\nu_2(t)\qquad(t\ge1).
\]
For \(h\ge3\), the **least positive index** with \(F_n\equiv0\pmod{2^h}\) is consequently
\[
 \alpha_h=6\cdot2^{h-3}=3\cdot2^{h-2},
\]
and every index of a zero is a multiple of \(\alpha_h\). Direct checks give \(\alpha_1=3\), \(\alpha_2=6\).

**3. Primitive projective directions.** Primitive pairs modulo \(2^h\) are identified under multiplication by an odd unit. There are \(3\cdot2^{h-1}\) resulting directions: \(2^h\) represented uniquely as \((1,t)\), \(t\in\mathbb Z/2^h\mathbb Z\), and \(2^{h-1}\) as \((2s,1)\), \(s\in\mathbb Z/2^{h-1}\mathbb Z\). A primitive orbit encounters a zero precisely when its projective direction is in the orbit of \((0,1)\). Since \(M^{\alpha_h}\) is scalar (the coefficient \(F_{\alpha_h}\) vanishes), that projective orbit has \(\alpha_h\) distinct directions. The same argument applies to the second coordinate because the dynamics is invertible and coordinates shift under iteration.

For \(h=1,2\), all \(3\cdot2^{h-1}\) primitive directions belong to the zero-bearing orbit, and none are safe. For \(h\ge3\), precisely \(\alpha_h\) of the \(3\cdot2^{h-1}=2\alpha_h\) primitive directions are zero-bearing; the other half avoid zero.

**4. Quadratic mod-eight rigidity.** On primitive pairs define \(q(A,B)=A^2+AB-B^2\). An exact expansion gives \(q(T(A,B))=-q(A,B)\). All such values are odd, and multiplication of \((A,B)\) by an odd unit preserves \(q\pmod8\), since odd squares are one modulo eight.

For modulus eight, the twelve projective directions are represented by \((1,t)\) for \(0\le t<8\) and \((2s,1)\) for \(0\le s<4\). The corresponding values of \(q\pmod8\) are, respectively,
\[
(1,1,7,3,5,5,3,7)\quad\text{and}\quad(7,5,3,1).
\]
Exactly six directions have \(q\equiv\pm1\) and six have \(q\equiv\pm3\). The zero-bearing orbit modulo eight has length \(\alpha_3=6\), and starts at \((0,1)\) with \(q=-1\). Its six directions are therefore exactly the \(q\equiv\pm1\) directions. Every projective direction modulo eight has precisely \(2^{h-3}\) lifts to a projective direction modulo \(2^h\). As every zero-bearing direction reduces to a zero-bearing direction modulo eight, the zero-bearing orbit modulo \(2^h\) lies among the \(6\cdot2^{h-3}=\alpha_h\) lifts of those six directions. These sets have equal cardinalities, so they coincide. This proves the exact \(q\equiv\pm3\pmod8\) test, uniformly in \(h\ge3\).

**5. Count and nonprimitive reduction.** Each projective direction modulo \(2^h\) has \(\varphi(2^h)=2^{h-1}\) primitive representatives. Thus exactly \(\alpha_h2^{h-1}=3\cdot2^{2h-3}\) primitive states avoid zero when \(h\ge3\). By Step 1 they occupy \(2^{h-2}\) cycles of length \(3\cdot2^{h-1}\). Multiplying a primitive pair modulo \(2^h\) by \(2^{k-h}\) is an injective correspondence with pairs having common depth \(k-h\) modulo \(2^k\), preserving coordinate-zero events and periods. Therefore for \(k\ge3\),
\[
 Z(k)=\sum_{h=3}^k 3\cdot2^{2h-3}=2^{2k-1}-8,
\]
and the cycle count is \(\sum_{h=3}^k2^{h-2}=2^{k-1}-2\). This proves every assertion. \(\square\)

## Verification

The standalone file `verify.py` exhaustively enumerates every orbit modulo \(2^k\) for \(1\le k\le9\), independently flags encounters with a zero, checks the quadratic criterion and verifies the exact period and orbit counts at every common depth. It terminates with `VERIFY_OK: complete modular orbit enumeration through 512, dyadic norm test, periods, and exact counts`. For \(k=9\), the exact number is \(131064\) zero-avoiding pairs and \(254\) zero-avoiding cycles. No randomized sampling is used. Finite enumeration is corroboration; the universal assertions follow from the preceding proof.

## Relationship to prior work

Sedaghat (2014, *Fibonacci Quarterly*) counts solutions avoiding zero **over prime fields**, and explicitly raises the distinct extension to sequences of units over composite residue rings, observing that modulo a power of two no recurrence is entirely unit-valued. The present result instead permits even nonzero terms and counts avoidance of **literal zero** over every dyadic composite modulus; it neither contradicts nor follows from the unit-sequence obstruction. Renault (2013) gives periods and ranks of Fibonacci sequences modulo general integers, ingredients used here; his inspected article does not provide the dyadic projective zero-locus criterion or the count of arbitrary initial pairs. OEIS A015135 records orbit-length phenomena of generalized Fibonacci sequences modulo integers, with a directly dated May 2, 2005 comment describing the modulus-eight case, but does not give this zero-avoiding subset formula. Aoki and Sakai (2016) study generalized Fibonacci equivalence classes modulo primes. The current work determines an additional invariant and its full census at all powers of two.

## Limitations

The result is restricted to powers of two, the specific Fibonacci recurrence, and the exact condition of avoiding residue zero. It does not classify unit-only recurrences or arbitrary composite moduli. Equivalent results may exist in unpublished or unlocated literature. One potentially relevant paper on generalized modular Fibonacci sequences (Riddlesden, 2020) was available by abstract only; its full text could not be compared. No independent mathematical audit is claimed.

## References

1. H. Sedaghat, “Zero-Avoiding Solutions of the Fibonacci Recurrence Modulo a Prime,” *Fibonacci Quarterly* **52** (2014), 39–45. https://www.fq.math.ca/Papers1/52-1/Sedaghat.pdf .
2. M. Renault, “The Period, Rank, and Order of the \((a,b)\)-Fibonacci Sequence Mod \(m\),” *Mathematics Magazine* **86** (2013), 372–380. https://webspace.ship.edu/msrenault/fibonacci/RenaultPeriodRankOrderMathMag.pdf .
3. OEIS Foundation, A015135, “Number of distinct periods of Fibonacci-type sequences mod \(n\),” including the T. D. Noe comment dated 2005-05-02. https://oeis.org/A015135 .
4. M. Aoki and T. Sakai, “On Equivalence Classes of Generalized Fibonacci Sequences,” *Journal of Integer Sequences* **19** (2016), article 16.2.6. https://cs.uwaterloo.ca/journals/JIS/VOL19/Aoki/aoki4.pdf .
5. C. Riddlesden, “Generalised Fibonacci Sequences under Modular Arithmetic,” *Rose-Hulman Undergraduate Mathematics Journal* **21** (2020), abstract at https://scholar.rose-hulman.edu/rhumj/vol21/iss1/10/ .
