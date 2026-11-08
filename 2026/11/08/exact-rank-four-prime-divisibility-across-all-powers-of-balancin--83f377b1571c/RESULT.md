# Exact rank-four prime divisibility across all powers of balancing-number window sums

## Finding
Let \(B_0=0\), \(B_1=1\), and \(B_{n+2}=6B_{n+1}-B_n\) for all \(n\ge0\). For positive integers \(e,k\), define the positive integer
\[
H_e(k)=\gcd_{n\ge0}\left(\sum_{j=1}^{k}B_{n+j}^{e}\right).
\]
Then the following **exact classification**, simultaneously for every power and every window length, holds:
\[
\boxed{
17\mid H_e(k)\iff
\begin{cases}
8\mid k,& e\text{ odd},\\
4\mid k\ \text{and}\ (68\mid k\ \text{or}\ e\equiv10\pmod{16}),&e\text{ even}.
\end{cases}}
\]
In particular, for every even \(e\in\{2,4,6,8\}\), a length-four window has at least one starting point at which its sum is not divisible by \(17\). For \(e=10\), **every** length-four window sum is divisible by \(17\); the same happens for every even \(e\equiv10\pmod{16}\). For odd powers the least positive universal window length is \(8\).

## Assumptions and scope
The gcd is over all starting indices \(n\ge0\), not just one selected window. Divisibility by \(17\) is the only asserted local prime-factor property: neither the exponent of \(17\) in \(H_e(k)\) nor its other prime factors is determined. All exponents and lengths are positive integers, without upper bounds. The recurrence is the standard balancing sequence; the result is not asserted for an arbitrary Lucas recurrence.

The modulus is naturally tied to the recurrence: \(B_2=6\), \(B_3=35\), and \(B_4=204=2^2\cdot3\cdot17\), so \(17\) is the unique prime whose first positive occurrence among balancing terms is at index \(4\). Thus it is the rank-four prime in the first new prime layer of these terms, rather than a modulus chosen merely for numerical convenience.

## Proof
All congruences in the following argument are modulo \(17\). Directly from the recurrence,
\[
(B_0,B_1,\ldots,B_8)\equiv(0,1,6,1,0,-1,-6,-1,0).
\]
The recurrence has an invertible companion matrix because its determinant is \(1\). The consecutive state at index \(8\) is the original state, so the entire sequence repeats with period \(8\). Moreover,
\[
B_{n+4}\equiv-B_n\qquad(n\ge0),
\]
which follows by checking the two consecutive initial values of this identity and using the recurrence.

Fix \(e\ge1\), and put \(a_n=B_n^e\pmod{17}\). For any \(k\ge1\), write \(W_n=\sum_{j=1}^{k}a_{n+j}\). Then
\[
W_{n+1}-W_n=a_{n+k+1}-a_{n+1}.
\]
Consequently, **if all windows vanish**, the sequence \((a_n)\) has period \(k\). Conversely, if \((a_n)\) has period \(k\), its length-\(k\) sums are independent of the starting point, and all windows vanish if and only if any one such sum vanishes. The same statements follow for an arbitrary positive period of \((a_n)\).

**Odd exponents.** Since \(a_{n+4}\equiv-a_n\), the power sequence has period \(8\). It has *least* positive period \(8\): the only potential proper divisors of \(8\) are \(1,2,4\), but \(a_0=0\), \(a_1=1\), \(a_2=6^e\ne0\), and \(a_5=-1\ne a_1\). Every consecutive eight-term sum is zero, since the final four terms cancel the first four. By the window-difference identity, all length-\(k\) windows vanish exactly when \(8\mid k\).

**Even exponents.** Now \(a_{n+4}\equiv a_n\), and the repeated four-term block is
\[
(a_0,a_1,a_2,a_3)=(0,1,6^e,1).
\]
Its least positive period is exactly \(4\): periods \(1\) and \(2\) are excluded because \(a_0=0\), \(a_1=1\), and \(a_2=6^e\ne0\). Therefore all length-\(k\) windows can vanish only if \(k=4t\). In that case each window sum is
\[
W_n\equiv t(2+6^e),
\]
independent of \(n\). Because \(17\) is prime, this vanishes precisely when either \(17\mid t\) or \(6^e\equiv-2\pmod{17}\). Finally, \(6^2\equiv2\), \(6^4\equiv4\), \(6^8\equiv-1\), and \(6^{16}\equiv1\); hence \(6\) has multiplicative order \(16\), and \(6^e\equiv-2\) holds precisely when \(e\equiv10\pmod{16}\). Substituting \(t=k/4\) proves the stated even-exponent condition. The theorem follows.

## Verification
The standalone standard-library program `verify.py` reconstructs the recurrence residues, checks the order of \(6\), and tests the theorem against every sliding window for all \(1\le e\le96\) and \(1\le k\le400\). It verifies \(38{,}400\) exponent-length pairs with all eight starting residues for each pair. Run `python3 verify.py`; the expected output is recorded in `checks.txt`. This finite test is supplementary: the proof above is valid for unrestricted positive integers.

## Relationship to prior work
Mbirika and Spilker (2022) develop exact gcd formulas for sliding **squares** of generalized Fibonacci numbers and ask about higher powers. Mbirika, Schrader, and Spilker (2023), Section 6.1, turn to Pell and balancing families, providing partial square-power results and an explicit related question. The present theorem concerns all powers of the balancing sequence but isolates the first rank-four prime; it neither reproves nor claims as new the already-known square-power gcd formulas. It gives a local divisibility obstruction that any future formula for the complete higher-power window gcd must reproduce.

Patra, Panda, and Khemaratchatakumthorn (2020) address divisibility by powers of balancing **terms**, not the gcd of sliding sums of arbitrary powers. Fiebig, Mbirika, and Spilker (2024) study entry points, orders, and recurrence periods, not this two-parameter higher-power gcd divisibility law. Such recurrence theory supports the modular method but does not, in the inspected claims, state this exact phase diagram.

## Limitations
Only divisibility by the specific rank-four prime \(17\) is classified. The result does not give an exact value for \(H_e(k)\), describe higher \(17\)-adic valuations, or determine the corresponding local laws at other primes. All known prior recurrence congruences remain credited to the literature. An equivalent result under a different formulation or in unindexed sources may exist; no assertion of priority is made.

## References
1. aBa Mbirika and Jürgen Spilker, *GCD of sums of \(k\) consecutive squares of generalized Fibonacci numbers*, arXiv:2204.12626 (first public 2022-04-26), Section 6.1, Question 6.1. https://arxiv.org/abs/2204.12626
2. aBa Mbirika, Janee Schrader, and Jürgen Spilker, *Pell and Associated Pell Braid Sequences as GCDs of Sums of \(k\) Consecutive Pell, Balancing, and Related Numbers*, Journal of Integer Sequences **26** (2023), Article 23.6.4, especially Section 6.1. First arXiv release 2023-01-13, arXiv:2301.05758. https://cs.uwaterloo.ca/journals/JIS/VOL26/Mbirika/mbir5.pdf
3. Asim Patra, Gopal Krishna Panda, and Tammatada Khemaratchatakumthorn, *Exact Divisibility by Powers of the Balancing and Lucas-Balancing Numbers* (2020). https://www.researchgate.net/publication/344375677_Exact_Divisibility_by_Powers_of_the_Balancing_and_Lucas-Balancing_Numbers
4. Morgan Fiebig, aBa Mbirika, and Jürgen Spilker, *Period patterns, entry points, and orders in the Lucas sequences: theory and applications*, arXiv:2408.14632 (first released 2024-08-26). https://arxiv.org/abs/2408.14632
