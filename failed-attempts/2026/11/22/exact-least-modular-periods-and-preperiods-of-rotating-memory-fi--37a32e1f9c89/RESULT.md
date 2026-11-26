# Exact least modular periods and preperiods of rotating-memory Fibonacci numbers

## Finding
For each integer \(k\ge2\), the rotating-memory Fibonacci sequence \(R_n^{(k)}\) has an **explicit least eventual period and least preperiod modulo every integer \(M\ge2\)**. Write uniquely
\[
M=2^a3^b m,\qquad a,b\ge0,\quad \gcd(m,6)=1,
\]
and denote the multiplicative order of a unit \(u\) modulo \(h>1\) by \(\operatorname{ord}_h(u)\). Put \(c_k=3\cdot2^{k-2}\). The least eventual period \(T=T(k,M)\) is
\[
\boxed{
T(k,M)=\begin{cases}
2\operatorname{ord}_{M/3^b}(3),&k=2,\ M/3^b>1,\\
1,&k=2,\ M/3^b=1,\\
k\operatorname{ord}_{m}(c_k),&k\ge3,\ m>1,\\
1,&k\ge3,\ m=1.
\end{cases}}
\]
The least preperiod \(N=N(k,M)\) is the smallest integer \(N\ge0\) such that \(R_{n+T}^{(k)}\equiv R_n^{(k)}\pmod M\) for **every** \(n\ge N\). It too is explicit. Define \(Z_3(b,k)=0\) when \(b=0\); for \(b\ge1\), set
\[
Z_3(b,k)=\begin{cases}k(b+1),&k=2,3,\\kb,&k\ge4.\end{cases}
\]
For \(k=3\), define \(Z_2(0,3)=0\), \(Z_2(1,3)=3\), and \(Z_2(a,3)=3a-2\) for \(a\ge2\). For \(k\ge4\), define \(Z_2(0,k)=0\) and, for \(a\ge1\),
\[
Z_2(a,k)=a+2+2\max\!\left\{0,\left\lceil\frac{a-k+4}{k-2}\right\rceil\right\}.
\]
Then
\[
\boxed{
N(k,M)=\begin{cases}
\max\{2\,[M/3^b>1],\ Z_3(b,2)\},&k=2,\\
\max\{3\,[m>1],\ Z_2(a,3),\ Z_3(b,3)\},&k=3,\\
\max\{2\,[m>1],\ Z_2(a,k),\ Z_3(b,k)\},&k\ge4.
\end{cases}}
\]
Here \([P]\in\{0,1\}\) is the indicator of a statement \(P\). In particular, for \(k\ge3\), **the residue sequence eventually becomes zero if and only if all prime factors of \(M\) are 2 or 3**. For \(k=2\), eventual zero occurs exactly when \(M\) is a power of 3. These classifications cover arbitrary composite moduli, including all 2- and 3-power factors, without an unspecified transient.

## Assumptions and scope
Fix integers \(k\ge2\) and \(M\ge2\). Let \(R_0^{(k)}=0\), \(R_1^{(k)}=1\), \(R_t^{(k)}=0\) for negative \(t\), and
\[
R_n^{(k)}=\sum_{j=1}^{2+(n\bmod k)}R_{n-j}^{(k)}\quad(n\ge2).
\]
A positive integer \(t\) is an eventual period if some \(N\) satisfies \(R_{n+t}^{(k)}\equiv R_n^{(k)}\pmod M\) for all \(n\ge N\). Its least such \(t\) is \(T\); the *least preperiod* is the least \(N\) for this \(T\). No claim concerns \(k=1\), which is the classical Fibonacci sequence. By convention the order \(\operatorname{ord}_h(u)\) is used only for \(h>1\) and \(\gcd(u,h)=1\).

## Proof
**1. Exact block shape.** The established rotating-memory collapse gives, for every \(q\ge1\) and \(0\le r<k\),
\[
R_{qk+r}^{(k)}=A_k2^r c_k^{q-1},\qquad
A_2=1,\quad A_3=2,\quad A_k=3\cdot2^{k-4}\ (k\ge4).
\tag{1}
\]
The initial terms are \(R_0=0,R_1=1,R_2=1\); for \(k\ge4\), \(R_n=2^{n-2}\) for \(2\le n<k\). These identities may also be established directly by induction from the defining recurrence. At each nonreset transition within a block, the factor is 2; the transition from \(qk+k-1\) to \((q+1)k\) has factor \(3/2\).

**2. Sharp least period away from 2 and 3.** Work modulo \(m>1\) with \(\gcd(m,6)=1\). Every term in (1) is invertible. Its consecutive ratio \(R_{n+1}/R_n\) (for \(n\ge k\)) is 2 except at exactly one index per block of \(k\) consecutive indices, where it is \(3/2\). These two residues are *always distinct*: equality would imply \(4\equiv3\pmod m\), i.e. \(m\mid1\). Thus the ratio word has least period exactly \(k\), so every eventual period of the sequence must be divisible by \(k\). For a shift \(ks\), the block identity gives \(R_{n+ks}=c_k^sR_n\) for \(n\ge k\), and all terms are units; hence precisely those \(s\) for which \(c_k^s\equiv1\pmod m\) work. The least period is therefore \(k\operatorname{ord}_m(c_k)\).

**3. The exceptional \(k=2\) component.** Put \(h=M/3^b\); then \(\gcd(h,3)=1\). If \(h>1\), the exact expressions \(R_{2q}=3^{q-1}\), \(R_{2q+1}=2\cdot3^{q-1}\) for \(q\ge1\) show that a shift by \(2s\) works modulo \(h\) exactly when \(3^s\equiv1\pmod h\). Any eventual period must be even: if \(h\) is even, even and odd indices have opposite parities; if \(h\) is odd, the distinguished reset ratio in Step 2 applies modulo \(h\). Thus \(T=2\operatorname{ord}_h(3)\). If \(h=1\), all terms eventually vanish modulo \(3^b\), giving least period one. For \(k\ge3\), the 2- and 3-power parts similarly eventually vanish and cannot change the least period determined by \(m\). The Chinese remainder theorem proves all the asserted period formulas.

**4. Exact disappearance indices for nonunit prime factors.** Let \(Z_p\) mean the earliest index from which all terms are divisible by the specified \(p\)-power (zero for exponent zero). From (1), the 3-adic valuations are \(q-1\) for \(k=2,3\) and \(q\) for \(k\ge4\). The preceding initial terms are nonmultiples of 3. Thus \(Z_3\) is as stated, and the immediately preceding term is not divisible by \(3^b\).

For \(k=3\), the 2-adic valuation in block \(q\) at residue \(r\) equals \(q+r\). For \(a=1\), the last deficient term is at \(n=2\); for \(a\ge2\), the last deficient term is the start of block \(q=a-1\), at \(n=3(a-1)\). This proves \(Z_2(a,3)\).

For \(k\ge4\), the block valuation is \((k-2)q+r-2\), and the initial valuation is \(n-2\) for \(2\le n<k\). When \(1\le a\le k-4\), the last deficient term is \(n=a+1\). Otherwise set \(q=\left\lceil(a-k+4)/(k-2)\right\rceil\ge1\); the final deficient index is \(qk+r_*\), where \(r_*=a+1-(k-2)q\) satisfies \(0\le r_*\le k-3\). The following index is \(qk+r_*+1=a+2+2q\). This proves the formula for \(Z_2(a,k)\), including the assertion that one index earlier fails. The \(k=2\) sequence never vanishes eventually modulo a positive power of 2, because all positive even-indexed terms are odd.

**5. Sharp start of the periodic tail.** If a residue sequence modulo \(p^e\) becomes zero eventually and is eventually periodic from \(N\), it must actually be zero for *all* \(n\ge N\), since each initial tail value recurs infinitely often. Thus any eventual periodic tail must begin at least at its corresponding \(Z_p\); Step 4 proves these lower bounds sharply.

For the component coprime to 6, the period established in Step 2 is valid from index 2 when \(k\ge4\), from index 3 when \(k=3\), and from index 2 when \(k=2\). These are the *earliest possible* indices: if \(m>1\), the shift by its least period sends \(R_1=1\) to \(1/2\pmod m\) for \(k\ge4\); for \(k=3\) it sends \(R_2=1\) to \(4/3\pmod m\). Neither equals 1 modulo any \(m>1\) coprime to 6. For \(k=2\), the shift by \(2\operatorname{ord}_{h}(3)\) sends \(R_1=1\) to \(2/3\pmod h\) if \(h\) is odd, and to an even residue if \(h\) is even; in either case this is not 1 for \(h>1\). Combining the exact componentwise starts using the Chinese remainder theorem yields the displayed maxima for \(N(k,M)\).

## Verification
The standalone `verify_rm_periods.py` computes the defining recurrence with exact integers and separately computes \(N(k,M)\), \(T(k,M)\) from the claimed formulas. It tests all \(2\le k\le16\), \(2\le M\le150\), a total of 2235 parameter pairs. For each pair it checks the proposed congruence on at least five complete proposed periods, verifies failure at the immediately preceding index when \(N>0\), and rejects every proper divisor of the claimed least period using a later complete-period window. Executing `python3 verify_rm_periods.py` prints `ALL CHECKS PASSED 2235`. These finite tests are reproducibility diagnostics only; Steps 1–5 prove the infinite assertions.

## Relationship to prior work
Abdelaidoum, Mehiri and Belbachir (2026), arXiv:2609.12569v1, establish the scalar block collapse, closed forms, and exact valuations for the rotating-memory sequence. They explicitly identify divisibility, gcd, and modular periodicity as directions for further study. Their statements yield eventual periodicity but do not state the least period at every modulus or the least onset, including the \(k=2\) exception and exact 2/3-power transient. This theorem uses those established formulas rather than claiming them as new. Related general work on finite-field linear recurrence periods concerns more general recurrence classes and does not by itself give the modulus-by-modulus arithmetic formulas here. The indexed record on finite intersections of *different* rotating-memory periods concerns common integer values, not modular period/preperiod of a fixed sequence.

## Limitations
The novelty is the *complete exact modular period/preperiod classification*, not the block formula, which is prior work. The formulas are derived from the exceptionally simple scalar-collapse structure and do not extend automatically to arbitrary variable-memory cycles. Multiplicative orders remain written as \(\operatorname{ord}\); their computation for general composite moduli requires standard modular arithmetic. The finding has not received independent mathematical audit, and unindexed equivalent deductions from the published closed form remain a priority risk.

## References
1. W. Abdelaidoum, E.-M. Mehiri and H. Belbachir, *Rotating-Memory Fibonacci Numbers and Periodic Tilings*, arXiv:2609.12569v1, first posted 2026-09-11, https://arxiv.org/html/2609.12569.
2. R. P. Brent, *On the periods of generalized Fibonacci recurrences*, arXiv:1004.5439 (2010), https://arxiv.org/abs/1004.5439. This concerns a distinct general linear-recursion setting.
