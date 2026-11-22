# The exact dyadic value image of the Tetranacci sequence

## Finding

Let the four-step Fibonacci (Tetranacci) sequence be defined by \(u_0=u_1=u_2=0\), \(u_3=1\), and \(u_{n+4}=u_{n+3}+u_{n+2}+u_{n+1}+u_n\) for every \(n\ge0\). For \(k\ge1\), write \(V_k=\{u_n\bmod2^k:n\ge0\}\).

**Theorem.** For every \(k\ge4\),
\[
V_k=\{y\bmod2^k:y\bmod16\in\{0,1,2,4,5,8,9,12,13,15\}\},
\qquad |V_k|=10\cdot2^{k-4}.
\]
Equivalently, the closure of the sequence in the dyadic integers is exactly the disjoint union
\[
4\mathbb Z_2\ \cup\ (1+4\mathbb Z_2)\ \cup\ (2+16\mathbb Z_2)\ \cup\ (15+16\mathbb Z_2).
\]
Its normalized Haar measure is exactly \(5/8\). For completeness, \(V_1=\{0,1\}\), \(V_2=\{0,1,2,3\}\), and \(V_3=\{0,1,2,4,5,7\}\).

This determines the complete value-set obstruction, not just the recurrence period: six residue classes modulo sixteen never occur, while each of the other ten occurs at every higher precision.

## Assumptions and scope

The recurrence has the specified impulse initial conditions and is indexed by all nonnegative integers. The image is a **set of distinct values**, not a histogram of the number of times each value occurs. Moduli are powers of two. The earlier convention \(M_0=M_1=0\), \(M_2=M_3=1\) is the shifted sequence \(M_n=u_{n+1}\), which has the same set of values. We do not assert uniformity among the attained residue classes.

## Proof

**1. Exact matrix identity.** Let
\[
A=\begin{pmatrix}0&1&0&0\\0&0&1&0\\0&0&0&1\\1&1&1&1\end{pmatrix},\qquad v=(0,0,0,1)^\mathsf T.
\]
Then \(u_n=(A^nv)_0\), with zero-based matrix subscripts. Direct integer multiplication gives \(A^{10}=I+4B\), where
\[
B=\begin{pmatrix}7&11&13&14\\14&21&25&27\\27&41&48&52\\52&79&93&100\end{pmatrix}.
\]
For \(j\ge0\), put \(b_{j,m}=(B^mA^jv)_0\). For each \(t\in\mathbb Z_2\), the series
\[
f_j(t)=\sum_{m=0}^{\infty}4^m b_{j,m}\binom tm
\]
converges in \(\mathbb Z_2\), because its coefficients are integral and \(\binom tm\in\mathbb Z_2\). For every integer \(t\ge0\), the finite binomial theorem yields \(f_j(t)=u_{10t+j}\). Hence its values at nonnegative arguments already determine its full image modulo any fixed power of two, since these arguments are dense in \(\mathbb Z_2\).

**2. Two full dyadic balls.** The critical coefficients, calculated by integer matrix multiplication, are
\[
\begin{array}{c|rrr}
j&b_{j,0}&b_{j,1}&b_{j,2}\\\hline
1&0&27&4763\\4&1&193&34112\\5&2&372&65753\\8&15&2664&470913
\end{array}.
\]
For any \(s,t\in\mathbb Z_2\) and any positive integer \(m\),
\[
\nu_2\!\left(\binom sm-\binom tm\right)\ge\nu_2(s-t)-\nu_2(m!),
\]
interpreting the inequality trivially when \(s=t\). This follows by factoring \(s-t\) out of the difference between the two monic products of consecutive linear factors in the definition of the binomial polynomial. For every \(m\ge2\), \(2m-\nu_2(m!)\ge3\). Thus the contributions of the \(m\ge2\) terms to \(f_j(s)-f_j(t)\) are divisible by \(2^{\nu_2(s-t)+3}\). Since \(b_{1,1}\) and \(b_{4,1}\) are odd, for \(j=1,4\),
\[
\nu_2(f_j(s)-f_j(t))=\nu_2(s-t)+2.
\]
These two functions are scaled dyadic isometries. Reducing modulo \(2^r\), they induce injective, hence bijective, maps from \(\mathbb Z/2^r\mathbb Z\) onto their respective balls at scale \(4\). Their images are therefore exactly \(4\mathbb Z_2\) and \(1+4\mathbb Z_2\).

**3. Two smaller dyadic balls.** Restrict the remaining branches to even parameters, and define for \(j\in\{5,8\}\)
\[
g_j(s)=\frac{f_j(2s)-u_j}{16},\qquad s\in\mathbb Z_2.
\]
The numerator is divisible by sixteen: its linear term is \(8b_{j,1}s\) with \(4\mid b_{j,1}\), and \(4^m\binom{2s}{m}\) is divisible by sixteen for every \(m\ge2\). From the first two positive-degree terms,
\[
\frac{g_j(s)-g_j(t)}{s-t}
=\frac{b_{j,1}}2+b_{j,2}(2(s+t)-1)+R_j(s,t),
\]
where \(R_j(s,t)\in4\mathbb Z_2\): for \(m\ge3\), the corresponding divided difference is divisible by \(2^{2m-3-\nu_2(m!)}\), whose exponent is at least two. Since \(b_{j,1}/2\) is even and \(b_{j,2}\) odd, the displayed quotient is odd. Therefore
\[
\nu_2(g_j(s)-g_j(t))=\nu_2(s-t).
\]
Both \(g_5\) and \(g_8\) are bijective isometries of \(\mathbb Z_2\). Consequently, the actual subsequences \(u_{20s+5}\) and \(u_{20s+8}\) for \(s\ge0\) attain all residues of \(2+16\mathbb Z_2\) and \(15+16\mathbb Z_2\), respectively, at every finite precision.

**4. Exhaustion.** Since \(A^{10}=I+4B\), the binomial identity gives \(A^{40}\equiv I\pmod{16}\). Directly enumerating \(u_n\bmod16\) for \(0\le n<40\) gives precisely the ten residues \(\{0,1,2,4,5,8,9,12,13,15\}\). Therefore the global dyadic closure lies in the union of the four balls established above, which already supply every permissible residue. The union is disjoint, has Haar measure \(1/4+1/4+1/16+1/16=5/8\), and at modulus \(2^k\) contains \(10\cdot2^{k-4}\) classes for every \(k\ge4\). The three small-modulus cases follow by reducing the same 40-term orbit. This completes the proof.

## Verification

A standalone \(CHECK.py\) included with this statement reconstructs \(A^{10}\), the matrix \(B\), the decisive first two coefficients of each branch, and the complete images from recurrence enumeration for all moduli \(2^k\) with \(1\le k\le12\). It also checks that all four normalized branch maps permute complete finite dyadic residue rings through depth eight. The exact theorem for arbitrarily large \(k\) follows from the valuation argument above rather than finite enumeration.

Run: `python3 CHECK.py`. The expected output starts with `CHECK_OK`.

## Relationship to prior work

Waddill's *Some Properties of the Tetranacci Sequence Modulo m* (1992) was inspected in full. It studies periods, periodic-block scaling, recurrence sums, and polynomial factorization, but does not supply the complete distinct-value image at every dyadic depth. Waddill's companion paper *The Tetranacci Sequence and Generalizations* (1992), also inspected, establishes matrix identities and recurrence structure but no complete dyadic value image. Marques (2014) studies powers of two expressible as sums of generalized Fibonacci numbers and verifies the classical impulse initialization, but its theorem does not entail this image.

Related results on periods of all generalized Fibonacci sequences establish state-return times, not which scalar output residues occur, and the known three-step Tribonacci dyadic value image is for a genuinely different characteristic polynomial. Thus these sources do not imply the four-ball classification by an immediate specialization. Historical-priority uncertainty remains for unindexed earlier value-set studies.

## Limitations

This is a statement about the classical single impulse-initialized four-step recurrence, not arbitrary initial vectors or other primes. The theorem classifies **support**, not the relative frequencies of represented residues. A search for a prior equivalent cannot establish uniqueness across all literature; the result has not undergone independent mathematical validation.

## References

- M. E. Waddill, *The Tetranacci Sequence and Generalizations*, Fibonacci Quarterly 30(1) (1992), 9–20. https://www.fq.math.ca/Scanned/30-1/waddill.pdf
- M. E. Waddill, *Some Properties of the Tetranacci Sequence Modulo m*, Fibonacci Quarterly 30(3) (1992), 232–238. https://www.fq.math.ca/Scanned/30-3/waddill.pdf
- D. Marques, *Powers of two as sum of two generalized Fibonacci numbers*, arXiv:1409.2704v1, first posted 2014-09-09. https://arxiv.org/abs/1409.2704
- *Exact binary-power periods for every k-step Fibonacci sequence*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-binary-power-periods-for-every-k-step-fibonacci-sequence--4eeed3c3b3c2
- *The complete dyadic value image and seven-twelfths density of Tribonacci numbers*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-complete-dyadic-value-image-and-seven-twelfths-density-of-tr--a24da7d7968e
