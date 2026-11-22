# A uniform five-adic window law for every even power of balancing numbers

## Finding
Let the balancing numbers be the integer sequence
\[
B_0=0,\qquad B_1=1,\qquad B_{n+2}=6B_{n+1}-B_n\quad(n\ge0).
\]
For every positive *even* integer \(d\), every positive integer \(k\), and each \(n\ge0\), put
\[
S_{d,k}(n)=\sum_{j=1}^{k}B_{n+j}^{d},\qquad
H_d(k)=\gcd\{S_{d,k}(n):n\ge0\}.
\]
If \(3\mid k\), then the **same sharp congruence holds at every starting index and every even exponent**:
\[
\boxed{S_{d,k}(n)\equiv\frac{2k}{3}\pmod{5^{\nu_5(k)+1}}.}
\]
Consequently the exact five-adic valuation of the global sliding-window gcd is
\[
\boxed{\nu_5(H_d(k))=
\begin{cases}
\nu_5(k),&3\mid k,\\
0,&3\nmid k.
\end{cases}}
\]
In fact, when \(3\mid k\), **each individual window sum** has valuation exactly \(\nu_5(k)\); no exceptional starting indices or even exponents occur. When \(3\nmid k\), at least one window has valuation zero.

## Assumptions and scope
All exponents are positive and even, all window lengths are positive, and starting indices are nonnegative. The gcd is the positive gcd of the entire infinite family, not of a chosen finite sample. The five-adic valuation \(\nu_5(m)\) is the nonnegative integer \(r\) with \(5^r\mid m\) and \(5^{r+1}\nmid m\) for a nonzero integer \(m\). The theorem only determines the five-primary part of \(H_d(k)\), not its other prime factors. The prime five is natural: the balancing companion matrix has cube \(-I\) modulo five, while five divides \(B_3=35\).

## Proof
**1. The basic three-term residue block.** Put
\[
M=\begin{pmatrix}6&-1\\1&0\end{pmatrix},\qquad
\begin{pmatrix}B_{n+1}\\B_n\end{pmatrix}=M^n\begin{pmatrix}1\\0\end{pmatrix}.
\]
Direct integer multiplication gives
\[
M^3=\begin{pmatrix}204&-35\\35&-6\end{pmatrix}
=-I+5\begin{pmatrix}41&-7\\7&-1\end{pmatrix}.
\]
Therefore \(B_{n+3}\equiv-B_n\pmod5\). Since \(d\) is even, \(B_n^d\bmod5\) has period three; the recurrence starts with residues \((B_0,B_1,B_2)\equiv(0,1,1)\pmod5\), and so
\[
(B_n^d)_{n\ge0}\equiv(0,1,1,0,1,1,\ldots)\pmod5.
\]
Every three consecutive powered terms thus sum to \(2\pmod5\).

**2. A matrix lifting lemma.** For every \(r\ge0\), set \(L_r=3\cdot5^r\). We claim that an integral \(2\times2\) matrix \(A_r\) exists with
\[
M^{L_r}=-I+5^{r+1}A_r.
\]
The base \(r=0\) was computed above. If it holds at \(r\), raising the matrix to the fifth power and using the binomial theorem (the identity matrix commutes with \(A_r\)) shows that its fifth power is \(-I\) modulo \(5^{r+2}\), proving the claim at \(r+1\).

Fix \(r\ge0\), \(t\ge0\), and \(0\le j\le4\). Expanding \((M^{L_r})^j\) modulo \(5^{r+2}\) gives
\[
M^{jL_r}\equiv(-1)^j(I-j5^{r+1}A_r)\pmod{5^{r+2}}.
\]
The terms quadratic in \(5^{r+1}\) vanish because \(2r+2\ge r+2\). On the relevant state vector this implies, for some integer \(e_{r,t}\) independent of \(j\),
\[
B_{t+jL_r}\equiv(-1)^j(B_t-j5^{r+1}e_{r,t})\pmod{5^{r+2}}.
\]
Since \(d\) is even, the outer sign disappears after taking the \(d\)-th power; a further binomial expansion yields
\[
B_{t+jL_r}^{d}\equiv B_t^d-dj5^{r+1}e_{r,t}B_t^{d-1}\pmod{5^{r+2}}.
\]
Summing over \(j=0,1,2,3,4\) eliminates the linear correction because \(\sum j=10\) is divisible by five:
\[
\boxed{\sum_{j=0}^{4}B_{t+jL_r}^{d}\equiv5B_t^d\pmod{5^{r+2}}.}
\]
This estimate is valid for **every** even \(d\), including multiples of five; no division by \(d\) is made.

**3. Lift complete three-power blocks.** For any \(n\ge0\) define
\[
T_r(n)=\sum_{i=1}^{L_r}B_{n+i}^{d}.
\]
Partitioning the length-\(L_{r+1}=5L_r\) sum into five blocks, applying the boxed five-block congruence to each of the \(L_r\) positions, and summing gives
\[
T_{r+1}(n)\equiv5T_r(n)\pmod{5^{r+2}}.
\]
Step 1 gives \(T_0(n)\equiv2\pmod5\). Induction therefore establishes the exact uniform residue
\[
\boxed{T_r(n)\equiv2\cdot5^r\pmod{5^{r+1}}}\qquad(r,n\ge0).
\]

**4. Arbitrary window lengths.** If \(3\mid k\), write \(k=3\cdot5^r u\) with \(r=\nu_5(k)\) and \(5\nmid u\). Partition every length-\(k\) sum into \(u\) consecutive length-\(L_r\) blocks. The uniform boxed formula gives
\[
S_{d,k}(n)\equiv2u5^r=2k/3\pmod{5^{r+1}}.
\]
Since \(5\nmid 2u\), this has valuation exactly \(r\), for each \(n\).

If \(3\nmid k\), write \(k=3q+s\), where \(s\in\{1,2\}\). The three-periodic binary residue word from Step 1 shows that the length-\(k\) window sum modulo five equals \(2q\) plus a prefix count. For \(s=1\), this prefix count can be either \(0\) or \(1\), depending on the starting index; for \(s=2\), it can be either \(1\) or \(2\). In either case the two possible window residues differ by one, so they cannot both vanish modulo five. Hence at least one window has valuation zero. This proves the formula for the gcd. \(\square\)

## Verification
The standalone integer-recurrence checker `verify.py` performs 870 exact full-window-gcd tests, 5,412 modular window-congruence tests (including exponents divisible by five), and 18 matrix-shift tests, for 6,300 assertions in total. The gcd test uses the first \(d+1\) windows: that is exhaustive for the fixed exponent \(d\) because \(B_n^d\) is a linear combination of the \(d+1\) distinct geometric sequences with roots \((3+2\sqrt2)^{d-2j}\), \(0\le j\le d\), so its window sums obey a monic integral recurrence of order \(d+1\). Each later window is therefore an integer combination of the first \(d+1\) windows. The checker rederives these values using plain integer arithmetic; recorded output is in `verification-output.txt`. These tests confirm examples and boundaries, while the all-exponent and all-index assertions follow from the preceding symbolic matrix proof.

## Relationship to prior work
Mbirika, Schrader, and Spilker (2023), Section 6.1, pose sliding-square gcd questions for balancing-related sequences and record partial results. The present five-adic statement is about **every even power** and identifies the precise prime-power divisibility and a uniform residue of **each** window; it neither supplies nor claims a complete integer formula for the global gcd. Mbirika and Spilker (2022) handle squares of generalized Fibonacci sequences, whose recurrence differs from the standard balancing sequence.

The published result *Exact even-window gcds of balancing and Lucas-balancing squares* already determines the entire gcd for \(d=2\) and even \(k\), and related published results handle the odd-\(k\) square case. Consequently, the \(d=2\) specialization here is **not** claimed as new. Another published result, *Exact rank-four prime divisibility across all powers of balancing-number window sums*, concerns prime \(17\), not the rank-three prime \(5\), and provides divisibility rather than full prime-power valuations. Its general-exponent scope does not imply the present five-adic congruence. The mathematical contribution here is the unrestricted **even-exponent** five-adic lifting law, which includes all higher even powers and every window length.

## Limitations
No assertion is made for odd exponents or for valuations at primes other than five. The theorem is restricted to the standard balancing recurrence; the matrix lifting method may apply elsewhere but no such generalized assertion is proved here. A literature search and relevant full-text comparisons do not constitute a guarantee of global novelty, particularly for unindexed results. The package has not undergone independent external mathematical validation.

## References
1. aBa Mbirika, Janee Schrader, and Jürgen Spilker, *Pell and Associated Pell Braid Sequences as GCDs of Sums of k Consecutive Pell, Balancing, and Related Numbers*, Journal of Integer Sequences **26** (2023), Article 23.6.4, especially Section 6.1. First public preprint 2023-01-13. https://arxiv.org/abs/2301.05758
2. aBa Mbirika and Jürgen Spilker, *GCD of Sums of k Consecutive Squares of Generalized Fibonacci Numbers*, Fibonacci Quarterly **60** (2022), 255–269. First public preprint 2022-04-26. https://arxiv.org/abs/2204.12626
3. *Exact even-window gcds of balancing and Lucas-balancing squares*, published mathematical result (2026-10-12). https://github.com/published-finding corpus/2026/blob/main/2026/10/12/SCOPE-exact-even-window-gcds-of-balancing-and-lucas-balancing-squares--dea4e87b5cd7/RESULT.md
4. *Exact rank-four prime divisibility across all powers of balancing-number window sums*, published mathematical result (2026-11-08). https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-rank-four-prime-divisibility-across-all-powers-of-balancin--83f377b1571c/RESULT.md
