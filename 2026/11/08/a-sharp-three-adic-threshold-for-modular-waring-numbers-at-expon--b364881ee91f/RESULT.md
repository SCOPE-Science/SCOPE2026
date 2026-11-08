# A sharp three-adic threshold for modular Waring numbers at exponents \(2\cdot3^s\)

## Finding
For integers \(k\ge1\) and \(N\ge2\), let \(\gamma(k,N)\) be the least positive integer \(r\) such that every residue modulo \(N\) is a sum of at most \(r\) integer \(k\)-th powers. Allowing zero summands makes “at most” equivalent to “exactly.”

**Theorem.** Let \(s\ge1\) be any integer and put \(k=2\cdot3^s\) and \(M=3^{s+1}\). Then for every integer \(N\ge2\),
\[
\gamma(k,N)\le M,\qquad
\gamma(k,N)=M\quad\Longleftrightarrow\quad3^{s+2}\mid N.
\]
The complete local values at the exceptional primes are
\[
\gamma(k,3^a)=
\begin{cases}
3^a-1,&1\le a\le s+1,\\
M,&a\ge s+2,
\end{cases}
\qquad
\gamma(k,2^a)=
\begin{cases}
2^a-1,&1\le a\le3,\\
8,&a\ge4.
\end{cases}
\]
For every prime \(p\ge5\) and exponent \(a\ge1\), the uniform estimate \(\gamma(k,p^a)\le k+1<M\) holds. Consequently the *global* modular Waring number \(\sup_{N\ge2}\gamma(k,N)\) is exactly \(3^{s+1}\), attained precisely on the moduli divisible by \(3^{s+2}\). For example, the global values at exponents \(6,18,54,162\) are respectively \(9,27,81,243\).

## Assumptions and scope
The variables in sums are unrestricted integers; their \(k\)-th powers are reduced modulo \(N\). The exponent parameter is restricted to positive integers \(s\), and the modulus is an arbitrary positive integer \(N\ge2\). This is the ordinary modular Waring number, not the variant requiring all summands to be units or allowing arbitrary nonunit coefficients. The exact value at a general modulus not divisible by \(3^{s+2}\) is **not** determined, except for the displayed prime-power cases.

## Proof
**1. Chinese remainder reduction.** If \(N=\prod_i p_i^{a_i}\), then
\[
\gamma(k,N)=\max_i\gamma(k,p_i^{a_i}).
\]
The lower inequality follows by reducing any representation modulo each prime power. For the upper inequality, choose the same number of summands in each prime-power ring (pad by zeros) and use the Chinese remainder theorem separately for each summand to obtain integers with all prescribed components.

**2. Powers modulo powers of three.** For \(a\le s+1\), Euler's theorem shows that every unit \(k\)-th power is \(1\pmod{3^a}\). Every nonunit \(k\)-th power is zero because \(k\ge s+2\ge a\). Thus the power residues are exactly \(\{0,1\}\), and representing the class \(3^a-1\) requires \(3^a-1\) summands, which also suffice.

For \(a\ge s+1\), the unit group modulo \(3^a\) is cyclic of order \(2\cdot3^{a-1}\). Since \(k=2\cdot3^s\), its \(k\)-th-power image is exactly the subgroup
\[
H_a=\{u\in(\mathbb Z/3^a\mathbb Z)^\times:u\equiv1\pmod M\}.
\]
For any target residue \(A\pmod{3^a}\), choose \(r\in\{1,\ldots,M\}\) satisfying \(r\equiv A\pmod M\). Then \(A-(r-1)\in H_a\), so it is one \(k\)-th power, and adding \(r-1\) copies of \(1\) realizes \(A\). Hence \(\gamma(k,3^a)\le M\).

For the reverse bound when \(a\ge s+2\), consider the target \(M\pmod{3^{s+2}}\). Every unit \(k\)-th power is \(1\pmod M\), while every nonunit \(k\)-th power is \(0\pmod{3^{s+2}}\) because \(k\ge s+2\). If fewer than \(M\) summands represented this target, the number \(r\) of unit summands would satisfy \(r\equiv0\pmod M\), hence \(r=0\). The resulting sum would be zero modulo \(3^{s+2}\), a contradiction. This establishes the asserted local values.

**3. Powers of two.** Since \(k\) is an even integer with \(v_2(k)=1\), the \(k\)-th-power image of the unit group modulo \(2^a\), for \(a\ge3\), is precisely the subgroup of units congruent to \(1\pmod8\). Indeed \((\mathbb Z/2^a\mathbb Z)^\times\cong C_2\times C_{2^{a-2}}\); exponentiation by \(k=2\cdot\text{odd}\) has the same image as squaring. For any target \(A\pmod{2^a}\), choose \(r\in\{1,\ldots,8\}\) with \(r\equiv A\pmod8\). Then \(A-(r-1)\) is a unit \(k\)-th power; adding \(r-1\) ones represents \(A\). Thus \(\gamma(k,2^a)\le8\) when \(a\ge3\). For \(a\ge4\), the target \(8\pmod{16}\) cannot be represented by fewer than eight summands: fewer than eight unit powers would have to number zero modulo eight, hence there are none, but all even \(k\)-th powers vanish modulo sixteen. At \(a\le3\), the only \(k\)-th-power residues are zero and one, giving \(2^a-1\).

**4. Every other prime.** Let \(p\ge5\) be prime. Then \(p\nmid k\). Write \(d=\gcd(k,p-1)\) and let \(H\subseteq\mathbb F_p^\times\) be the subgroup of nonzero \(k\)-th powers, of size \((p-1)/d\). The Cauchy–Davenport inequality applied repeatedly to \(T=H\cup\{0\}\) yields
\[
|kT|\ge\min\bigl(p,\,k(|T|-1)+1\bigr)=p
\]
because \(d\le k\). For any target \(A\in\mathbb F_p\), fix \(h\in H\) and express \(A-h\) as a sum of \(k\) elements of \(T\). Adding \(h\) produces a representation by \(k+1\) powers with at least one nonzero base modulo \(p\). Since \(p\nmid k\), the derivative of the sum-of-powers polynomial with respect to that variable is invertible modulo \(p\). Ordinary Hensel lifting therefore yields a representation by \(k+1\) powers of every target modulo \(p^a\), for every \(a\ge1\).

**5. Global sharp threshold.** Since \(M=3^{s+1}>\max\{8,k+1\}\) for every \(s\ge1\), only the prime \(3\) can force \(M\) summands. By Steps 1–4, it does so exactly when the modulus contains the factor \(3^{s+2}\). This proves the theorem. \(\square\)

## Verification
The self-contained `verify_local.py` enumerates every \(k\)-th-power residue and the growing sumsets at \(105\) prime powers, for four values of \(s\). `verify_composite.py` uses an independently written breadth-first residue search for \(458\) general moduli for exponents \(6\) and \(18\). Run `python3 verify_local.py` and `python3 verify_composite.py`; the exact output is in `checks/exact_enumeration.txt`. Both programs have been executed against the standalone files in this package; all assertions passed. Finite checks corroborate, but do not establish, the infinite theorem; the group, sumset, lifting, and Chinese-remainder arguments above are its proof.

## Relationship to prior work
Arias, Borja and Anaya (2023), Table 3, give the global value \(\gamma(6)=9\), but do not state the displayed infinite exponent family or the complete sharp divisibility threshold. Alnaser and Cochrane (2008), introduction, equation (2), print a value \(3^{s+1}-1\) for \(\gamma(2\cdot3^s,3^a)\) when \(a\ge s+1\). Taken literally at \(a=s+2\), that equation conflicts with the explicit obstruction proved here (already \(\gamma(6,27)=9\)). Their general estimates, cyclic-unit observations and lifting lemmas are useful context, not the asserted sharp global classification. Their wording should not be treated as a confirming novelty certificate: its discrepancy is a significant source-comparison issue.

Alnaser, Cochrane, Ostergaard and Spencer (2020) study stronger variants involving variable coefficients and primitive representations, with general bounds but no located identical sharp family. Small's two 1977 Monthly articles give general methods to determine modular Waring numbers; their full text could not be inspected, so a previously implicit specialization remains a residual originality risk. No claim of priority or independent external validation is made.

## Limitations
Only the stated exponent family is classified. For moduli without the factor \(3^{s+2}\), the theorem gives a uniform strict upper bound and some exact local cases but not a universal exact expression. The two 1977 primary articles were unavailable in full, and an unindexed equivalent corollary is possible; this limits the literature comparison. All computer checks are finite and must not be used as substitutes for the infinite argument.

## References
- F. Arias, J. Borja, and S. Anaya, *Counting Integers Representable as Sums of k-th Powers Modulo n*, Journal of Integer Sequences 26 (2023), Article 23.8.1, published 2023-08-28. https://cs.uwaterloo.ca/journals/JIS/VOL26/Borja/borja4.pdf
- A. Alnaser and T. Cochrane, *Waring's Number Mod m*, Journal of Number Theory 128 (2008), 2582–2590. https://www.math.k-state.edu/~cochrane/research/waringmodm.pdf
- A. Alnaser, T. Cochrane, M. Ostergaard, and C. Spencer, *Waring Numbers for Diagonal Congruences*, Rocky Mountain Journal of Mathematics 50 (2020), 825–838. https://www.math.ksu.edu/~cvs/alnaser_cochrane_ostergaard_spencer-diagonal_cong.pdf
- C. Small, *Waring's Problem Mod n*, American Mathematical Monthly 84 (1977), 12–25. https://doi.org/10.1080/00029890.1977.11994269
- C. Small, *Solution of Waring's Problem Mod n*, American Mathematical Monthly 84 (1977), 356–359. https://doi.org/10.1080/00029890.1977.11994355
