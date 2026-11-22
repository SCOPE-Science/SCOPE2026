# Exact binary rank spectrum for all invertible Lucas recurrences

## Finding
Let \(a\ge1\), \(M=2^a\), and choose \(P\in\mathbb Z/M\mathbb Z\), \(Q\in(\mathbb Z/M\mathbb Z)^\times\). Define \(U_0=0\), \(U_1=1\), \(U_{n+2}=PU_{n+1}-QU_n\) modulo \(M\), and let \(\rho_a(P,Q)\) be its smallest positive zero index. All ranks exist. When \(a\ge3\), the **complete exact multiplicity spectrum** is
\[
\begin{aligned}
\#\{(P,Q):\rho_a=2\}&=2^{a-1},\\
\#\{(P,Q):\rho_a=2^j\}&=2^{a+j-3} &&(2\le j\le a),\\
\#\{(P,Q):\rho_a=3\}&=2^{a-1},\\
\#\{(P,Q):\rho_a=6\}&=3\cdot2^{a-1},\\
\#\{(P,Q):\rho_a=3\cdot2^j\}&=2^{a+j-1} &&(2\le j\le a-2).
\end{aligned}
\]
All omitted ranks have multiplicity zero. For \(a=1\), ranks \(2,3\) occur once each; for \(a=2\), ranks \(2,3,4,6\) occur twice each. Consequently the binary rank distribution has two disjoint power-of-two branches, with one rank-three branch ending at \(3\cdot2^{a-2}\), and the rank-six multiplicity is three times the rank-three multiplicity for every \(a\ge3\).

## Assumptions and scope
The pair \((P,Q)\) ranges over all \(2^{2a-1}\) residue pairs with \(Q\) odd, **without** a nondegeneracy assumption on integer lifts. Multiplicities count parameter pairs, not sequence orbits. The rank concerns zeros of the first-kind normalized recurrence, not the companion matrix's full period. Since \(Q\) is a unit, the companion matrix is invertible and the recurrence state \((U_n,U_{n+1})\) is periodic, so the first zero exists; the proof additionally determines it explicitly.

## Proof
**1. Even trace.** Let \(P\) be even. Modulo two the first zero is at index two. Write \(h=\nu_2(P)\), with \(h\ge a\) when \(P\equiv0\pmod{2^a}\). Use the companion sequence \(V_0=2,V_1=P,V_{n+2}=PV_{n+1}-QV_n\) and \(U_{2n}=U_nV_n\). For all \(j\ge1\), \(V_{2^j}\equiv2\pmod4\): initially \(V_2=P^2-2Q\equiv2\pmod4\), and the identity \(V_{2n}=V_n^2-2Q^n\) preserves the property. Thus \(\nu_2(U_{2^j})=h+j-1\) as long as the chosen integer lift has finite \(h\). An odd multiplier cannot introduce additional factors of two, by applying the odd-index polynomial \(U_m(V_{2^j},Q^{2^j})\equiv1\pmod2\). Hence \(\rho_a=2\) if \(h\ge a\), otherwise \(\rho_a=2^{a-h+1}\). The number of traces with \(\nu_2(P)=h<a\) is \(2^{a-h-1}\); the zero trace is unique. Multiplying by the \(2^{a-1}\) choices of odd \(Q\) yields the even-rank multiplicities.

**2. Odd trace valuation dichotomy.** Let \(P\) and \(Q\) both be odd. Modulo two the first zero is index three. Set \(A=P^2-Q=U_3\) and \(B=P^2-3Q=V_3/P\), both even. Write \(t=\nu_2(A)\), \(s=\nu_2(B)\), with valuations truncated at the required modulus when a residue vanishes. The identity \(B=3A-2P^2\) proves: if \(t\ge2\), then \(s=1\); if \(t=1\), then \(s\ge2\). Because \(U_6=U_3V_3\), \(\nu_2(U_6)=t+s\). For every \(j\ge1\), \(V_{3\cdot2^j}\equiv2\pmod4\), since \(V_6=V_3^2-2Q^3\equiv2\pmod4\) and the same doubling identity applies. Odd multipliers preserve valuations by the odd-index factor formula. Therefore the first zero is at index \(3\) if \(t\ge a\), at index \(6\) if \(t<a\le t+s\), and otherwise at \(3\cdot2^{a-t-s+1}\). In particular, all ranks have the asserted forms; no nonmultiple of three can be a zero by reduction modulo two.

**3. Exact odd-trace counts.** For each fixed odd \(P\), as \(Q\) runs through odd classes, \(A=P^2-Q\) is uniform among even residue classes modulo \(2^a\). Thus \(\Pr(t\ge a)=2^{-(a-1)}\); for \(1\le t<a\), \(\Pr(t)=2^{-t}\). If \(t\ge2\), then \(s=1\). Conditional on \(t=1\), write \(A=2u\) with \(u\) odd: \(B=2(3u-P^2)\). Because multiplication by three permutes odd classes, the value \(3u-P^2\) is uniformly distributed among even residues modulo \(2^{a-1}\). Consequently \(\Pr(s=j\mid t=1)=2^{-(j-1)}\) for \(2\le j<a\), with the remaining mass at \(s\ge a\). For \(a\ge3\), the rank-three, rank-six, and rank-\(3\cdot2^j\) probabilities conditional on odd \(P\) are respectively \(2^{-(a-1)}\), \(3\cdot2^{-(a-1)}\), and \(2^{-(a-j-1)}\) for \(2\le j\le a-2\). Multiply by the \(2^{2a-2}\) odd-\(P\), odd-\(Q\) pairs to obtain the displayed multiplicities. For \(a=1,2\) direct reduction of the same two-valuation dichotomy gives the exceptional formulas. The even and odd trace counts each sum to \(2^{2a-2}\), exhausting the parameter space. \(\square\)

## Verification
The standalone `verify.py` enumerates all pairs \((P,Q)\) with \(Q\) odd modulo \(2^a\) for \(1\le a\le8\), independently iterates each recurrence from \((0,1)\), and compares the exact first-zero rank counts with every displayed formula. All eight full modular enumerations pass. Exhaustive checks through \(a=8\) are finite corroboration, not the unrestricted proof; Steps 1–3 prove the formulas for every \(a\).

## Relationship to prior work
Riasat (2026) investigates primitive divisors and local multiplicities of individual Lucas sequences, including their binary valuation behavior. Classical \(2\)-adic Lucas valuation formulas, including Sanna (2016), provide the pointwise lifting ingredients; these are explicitly not claimed as new. A previously published parameter-rank census for generalized Fibonacci recurrences handles **odd** prime powers and fixes the second recurrence coefficient at one; its theorem explicitly excludes the prime two and variable \(Q\). The present result is the evaluated, uniform **two-parameter** binary distribution over all invertible companion matrices. No compared source states the two-branch rank multiplicities or the rank-six/three ratio. A broader unpublished or historically unindexed all-parameter distribution could still subsume the statement.

## Limitations
Only prime-power moduli \(2^a\) and unit \(Q\) are covered; nothing is asserted for odd prime powers or nonunit recurrence parameters. The theorem gives first-zero ranks, not complete orbit periods or distributions with additional coprimality restrictions on integer lifts. The mathematical proof was checked within the present manuscript; independent validation has not been performed.

## References
1. S. Riasat, *On Primitive Divisor Multiplicities of Lucas Sequences*, arXiv:2611.20650, initially posted November 16, 2026, https://arxiv.org/abs/2611.20650.
2. C. Sanna, *The p-Adic Valuation of Lucas Sequences*, Fibonacci Quarterly 54 (2016), 118–124, https://doi.org/10.1080/00150517.2016.12427821.
3. P. K. Ray, N. Irmak and B. K. Patel, *The rank of apparition of powers of Lucas sequence*, Turkish Journal of Mathematics 42 (2018), 1566–1570, https://doi.org/10.3906/mat-1705-116.
4. *Exact prime-power rank distributions for generalized Fibonacci sequences*, public record, October 18, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-prime-power-rank-distributions-for-generalized-fibonacci-s--9f2cc47756b9.
