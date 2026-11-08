# Unbounded separation of exact odd-window GCD periods

## Finding
Let \(F_0=0\), \(F_1=1\), \(F_{n+2}=F_{n+1}+F_n\), and \(L_n=F_{n-1}+F_{n+1}\) for \(n\ge1\). For **every prime \(h\ge5\)**, define the integer-seeded recurrence
\[
G_0=F_h,\qquad G_1=-F_{h-1}-1,\qquad G_{n+2}=G_{n+1}+G_n.
\]
For each **positive odd** window length \(k\), take nonnegative greatest common divisors over all \(n\ge0\):
\[
A_h(k)=\gcd_{n\ge0}\sum_{i=1}^{k}G_{n+i},\qquad
B_h(k)=\gcd_{n\ge0}\sum_{i=1}^{k}G_{n+i}^{2}.
\]
Then the exact identities are
\[
\boxed{A_h(k)=2^{\mathbf1_{3\mid k}},\qquad
B_h(k)=2^{\mathbf1_{3\mid k}}L_h^{\mathbf1_{h\mid k}}.}
\]
Consequently, when evaluated at successive odd lengths \(k=2j+1\), with \(j\ge0\), the **least positive periods in \(j\)** of \(A_h(2j+1)\) and \(B_h(2j+1)\) are respectively \(3\) and \(3h\). Their ratio is \(h\), and therefore the ratios of the two least periods are unbounded as the prime \(h\) varies. These are the same exact periods as \(6\) and \(6h\) when shifts are measured in the original window length \(k\), restricted to odd \(k\).

## Assumptions and scope
All sequences are integer-valued, including the possibly negative Gibonacci terms. A GCD is the greatest nonnegative common divisor of an integer set; its sign is immaterial. The parameter \(h\) is a prime at least \(5\); the formulas are not asserted for arbitrary composite \(h\) or even window lengths. The Lucas number \(L_h\) is odd, greater than \(1\), and not divisible by \(3\).

## Proof
**1. Primitive initial pair and Lucas norm.** Set \(a=F_h\), \(b=-F_{h-1}-1\). Since a Fibonacci number is even exactly when its index is a multiple of \(3\), \(a\) is odd. Any common divisor of \(a\) and \(b\) gives \(F_h\equiv0\), \(F_{h-1}\equiv-1\), and \(F_{h+1}\equiv-1\). Cassini's identity \(F_{h-1}F_{h+1}-F_h^2=(-1)^h=-1\) then implies the common divisor divides \(2\); hence \(\gcd(a,b)=1\). The same identity yields
\[
\mu:=b^2-ab-a^2=F_h+2F_{h-1}=L_h.
\]
The recurrence matrix \(T=\begin{pmatrix}0&1\\1&1\end{pmatrix}\) satisfies \(T^h(a,b)^\mathsf{T}=(-a,-b-L_h)^\mathsf{T}\). This follows directly from \(G_h=F_{h-1}a+F_hb=-a\) and \(G_{h+1}=F_ha+F_{h+1}b=-b-L_h\). Consequently the state is **antipodal after \(h\) steps modulo \(L_h\)** and returns after \(2h\) steps.

**2. Only primes dividing the norm can enter odd-window GCDs.** For a general sequence satisfying the same recurrence, put \(\mu_n=G_{n+1}^2-G_nG_{n+1}-G_n^2\). The recurrence gives \(\mu_{n+1}=-\mu_n\), so \(\mu_n=(-1)^n\mu\). Let \(d\) divide all linear window sums of an odd length \(k\). Successive differences of those sums give \(G_{n+k+1}\equiv G_{n+1}\pmod d\) for all \(n\ge0\); invertibility of \(T\) over \(\mathbb Z/d\mathbb Z\) extends this to an entire \(k\)-periodic state. Thus \(\mu_k\equiv\mu_0\pmod d\) and \(d\mid2\mu\).

Likewise, suppose \(d\) divides every squared window sum. Their successive differences give \(G_{n+k+1}^2\equiv G_{n+1}^2\pmod d\). Squares satisfy the reversible order-three recurrence
\[
G_{n+3}^2=2G_{n+2}^2+2G_{n+1}^2-G_n^2,
\]
so the square sequence is \(k\)-periodic modulo \(d\), including its term at index zero. The telescoping identity
\[
\sum_{i=1}^{k}G_{n+i}^2=G_{n+k}G_{n+k+1}-G_nG_{n+1}
\]
now gives \(G_kG_{k+1}\equiv G_0G_1\pmod d\). Together with periodic squares, it implies \(\mu_k\equiv\mu_0\pmod d\); hence again \(d\mid2\mu\). In the constructed family, **both GCDs therefore divide \(2L_h\)** for odd \(k\).

**3. Odd-prime local periods.** Fix any odd prime power \(q^e\mid L_h\). Since \(\gcd(a,b)=1\), the initial vector is nonzero modulo \(q\). The antipodal identity from step 1 shows that the least period of the original state modulo \(q^e\) divides \(2h\) but not \(h\): the latter would require \(2a\equiv2b\equiv0\pmod q\). Because \(h\) is prime, the only remaining possibilities are \(2\) and \(2h\). Period \(2\) is impossible: \(T^2-I=\begin{pmatrix}0&1\\1&1\end{pmatrix}\) has determinant \(-1\), so its kernel is zero modulo every prime power. Thus the **state period is exactly \(2h\)**, and no positive odd \(k\) makes the linear GCD divisible by \(q^e\).

The squared sequence, on the other hand, has period dividing \(h\) modulo \(q^e\) because the state changes sign after \(h\) steps. It cannot have period \(1\) modulo \(q\). Indeed, if \(a^2\equiv b^2\equiv(a+b)^2\pmod q\), then primitivity makes \(a\) nonzero modulo \(q\). With \(t=b/a\) one obtains \(t^2=1\) and \((1+t)^2=1\), which for an odd prime \(q\) forces \(q=3\). But \(3\nmid L_h\): the Lucas sequence modulo \(3\) has period \(8\), with residues \(2,1,0,1,1,2,0,2\), so its odd-indexed terms are nonzero. As \(h\) is prime, the **least square-sequence period is exactly \(h\)** modulo every \(q^e\mid L_h\).

For odd \(q\), a squared sequence has period \(k\) modulo \(q^e\) **if and only if** all \(k\)-window sums of squares vanish modulo \(q^e\). The forward direction follows from
\[
2G_nG_{n+1}=G_{n+2}^2-G_n^2-G_{n+1}^2
\]
(the factor \(2\) is invertible modulo \(q^e\)) and the telescoping identity in step 2. The reverse direction follows from differences of adjacent windows and the reversible square recurrence. Therefore \(q^e\mid B_h(k)\) exactly when \(h\mid k\), while \(q^e\nmid A_h(k)\) at every odd \(k\).

**4. The factor \(2\).** For prime \(h\ge5\), \(L_h\) is odd; thus step 2 bounds the two-adic valuations of both GCDs by \(1\). The nonzero binary recurrence state has period exactly \(3\), as the matrix \(T\) has order \(3\) modulo \(2\) and \((a,b)\) is nonzero modulo \(2\). Squaring preserves parity. Necessity of \(3\mid k\) for either GCD to be even follows from the window-difference argument and the period-three state. Conversely, if \(3\mid k\), each window consists of complete binary periods with the parity pattern containing precisely two ones, so both types of window sums vanish modulo \(2\). Hence \(2\) divides either GCD precisely for \(3\mid k\).

**5. Assemble prime powers and prove leastness.** Combining steps 2–4 gives the displayed identities because the entire admissible prime-power support is \(2L_h\). The function \(j\mapsto A_h(2j+1)\) equals \(2\) at exactly one residue of \(j\pmod3\), giving least period \(3\). The function \(j\mapsto B_h(2j+1)\) takes its unique maximum \(2L_h\) precisely when \(2j+1\) is divisible by both \(3\) and \(h\), i.e. in one residue class modulo \(3h\). Thus every period of that function is a multiple of \(3h\), while the formula gives period \(3h\). Since there are arbitrarily large primes, the ratio \(h\) is unbounded. \(\square\)

## Verification
Run `python3 verify.py` using the standalone, standard-library Python 3 checker. For all twelve primes from \(5\) through \(43\), it computes 852 odd window lengths and independently evaluates the exact GCD of eight consecutive windows for each of the linear and squared versions. The eight-window computation is sufficient because linear window sums satisfy a reversible order-two recurrence and squared window sums a reversible order-three recurrence; the proof of the infinite theorem does not depend on the tested parameter range. The checker separately verifies the Lucas norm and the antipodal modular identity. Sample rows are \(h=5\): \(L_h=11\), \(B_h(5)=11\), \(B_h(15)=22\); and \(h=7\): \(L_h=29\), \(B_h(7)=29\), \(B_h(21)=58\).

## Relationship to prior work
Guyer and Mbirika (2021) give the exact first-power window GCD and its Pisano-period characterization for arbitrary integer seeds. Mbirika and Spilker (2022) give the exact squared-window GCD and the odd-window divisor bound \(2|\mu|\). Their Example 6.3 already establishes a **single** ratio-five instance with initial pair \((-1,3)\), corresponding up to sign and recurrence shift to the case \(h=5\) above. Thus the isolated \(h=5\) phenomenon and the general starting formulas are **not claimed as new**. The result here is an explicit **infinite prime-indexed family**, complete odd-window GCD formulas for every family member, and exact period ratios increasing without bound. Existing general periodicity bounds for arbitrary seeds yield a possible period but do not by themselves imply that ratios of least periods are unbounded. This distinction is the mathematical contribution.

## Limitations
The argument covers only the specified primitive signed seeds, positive odd window lengths, and powers one and two. Nothing is asserted about other seed families, higher powers, even window lengths, or the rarity of such period separations. The proof supplies exact infinite identities; finite checks alone would not establish them. Bibliographic uniqueness beyond the inspected papers and searched literature remains subject to independent assessment.

## References
1. Dan Guyer and aBa Mbirika, *GCD of sums of \(k\) consecutive Fibonacci, Lucas, and generalized Fibonacci numbers*, Journal of Integer Sequences 24 (2021), Article 21.9.8, arXiv:2104.12262, first public version 2021-04-25, https://arxiv.org/abs/2104.12262.
2. aBa Mbirika and Jürgen Spilker, *GCD of sums of \(k\) consecutive squares of generalized Fibonacci numbers*, Fibonacci Quarterly 60 (2022), 255–269, arXiv:2204.12626, first public version 2022-04-26, https://arxiv.org/abs/2204.12626.
