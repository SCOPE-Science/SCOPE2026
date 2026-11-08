# Three exact 2-adic residue balls for the Pell–Lucas sequence

## Finding
For the Pell–Lucas sequence \(Q_0=Q_1=2\), \(Q_{n+2}=2Q_{n+1}+Q_n\), the closure of its nonnegative-index values in \(\mathbb Z_2\) is precisely
\[
\overline{\{Q_n:n\ge0\}}^{\mathbb Z_2}=(2+16\mathbb Z_2)\ \dot\cup\ (14+16\mathbb Z_2)\ \dot\cup\ (6+64\mathbb Z_2).
\]
In particular, for every integer \(k\ge6\), the number of occupied classes modulo \(2^k\) equals \(9\cdot2^{k-6}\); the image fraction is exactly \(9/64\) at all such levels. For \(k=1,2,3,4,5\), the cardinalities are respectively \(1,1,2,3,5\). The closed image has normalized additive Haar measure \(9/64\). Every supported class occurs infinitely many times in the recurrence.

## Assumptions and scope
Let \(P_0=0\), \(P_1=1\), \(P_{n+2}=2P_{n+1}+P_n\) be the Pell sequence, and set \(x_n=Q_n/2\). Thus \(x_0=x_1=1\), with the same linear recurrence. For a nonzero integer \(m\), write \(\nu_2(m)\) for its 2-adic valuation, and let \(\mathbb Z_2\) denote the ring of 2-adic integers. The claim covers every exponent \(k\ge1\) and all integer indices \(n\ge0\). No assertion is made about equidistribution among the occupied classes or the index-frequency measure: \(9/64\) is the Haar measure of the *value-image support*.

## Proof
**1. Quadratic-unit identities.** In \(\mathbb Z[\sqrt2]\), the identity
\[
(1+\sqrt2)^n=x_n+P_n\sqrt2
\]
gives
\[
x_n^2-2P_n^2=(-1)^n,\quad P_{2m}=2x_mP_m,\quad x_{2m}=2x_m^2-(-1)^m,
\]
and the addition law \(x_{n+m}=x_nx_m+2P_nP_m\). Modulo 2, all \(x_n\) are odd, while \(P_n\) is odd precisely for odd \(n\). Repeated doubling yields \(\nu_2(P_m)=\nu_2(m)\) for every positive \(m\).

**2. The two odd-index balls.** For any odd positive integer \(n\) and any integer \(h\ge1\), the addition law gives
\[
x_{n+4h}-x_n=x_n(x_{4h}-1)+2P_nP_{4h}.
\]
The norm identity yields \(x_{4h}-1=4P_{2h}^2\). Therefore the valuations of the two displayed summands are \(4+2\nu_2(h)\) and \(3+\nu_2(h)\), respectively. They are distinct, so
\[
\boxed{\nu_2(x_{n+4h}-x_n)=3+\nu_2(h).}
\]
In particular, for different nonnegative integers \(s,t\), \(\nu_2(x_{4t+1}-x_{4s+1})=3+\nu_2(t-s)\), and the same holds with \(1\) replaced by \(3\). Because \(x_1=1\) and \(x_3=7\), the two subsequences occupy exactly the balls \(1+8\mathbb Z_2\) and \(7+8\mathbb Z_2\): for each \(k\ge3\), the \(2^{k-3}\) indices \(t\) in \(0\le t<2^{k-3}\) give different residues in the corresponding class modulo \(2^k\), exhausting that class. No limiting or approximation assumption is needed.

**3. The exceptional even-index ball.** For an even index \(2m\) with even \(m\), the doubling identity gives \(x_{2m}=2x_m^2-1\equiv1\pmod{16}\), inside the first ball. If \(m\) is odd, Step 2 shows \(x_m\equiv\pm1\pmod8\), whence \(x_m^2\equiv1\pmod{16}\), and thus \(x_{2m}=2x_m^2+1\equiv3\pmod{32}\). Conversely, restrict to \(m=4t+1\). By Step 2, these \(x_m\) attain every residue in \(1+8\mathbb Z_2\). Write \(x_m=1+8z\); then
\[
x_{2m}=2(1+8z)^2+1=3+32(z+4z^2).
\]
The polynomial \(f(z)=z+4z^2\) satisfies \(f(z)-f(w)=(z-w)(1+4(z+w))\). The second factor is odd, so \(f\) is an exact 2-adic isometry. On each finite ring \(\mathbb Z/2^j\mathbb Z\) it is an injection and therefore a bijection. Consequently \(x_{2(4t+1)}\) fills the entire ball \(3+32\mathbb Z_2\).

**4. Exhaustion, cardinalities and measure.** Every nonnegative index is odd, twice an even integer, or twice an odd integer; Steps 2–3 thus give exactly
\[
\overline{\{x_n:n\ge0\}}=(1+8\mathbb Z_2)\ \dot\cup\ (7+8\mathbb Z_2)\ \dot\cup\ (3+32\mathbb Z_2).
\]
Multiplication by 2 gives the claimed three disjoint balls for \(Q_n\). At depth \(k\ge6\) their cardinalities are \(2^{k-4}\), \(2^{k-4}\), and \(2^{k-6}\), respectively; their total is \(9\cdot2^{k-6}\). Direct reduction of the three balls gives cardinalities \(1,1,2,3,5\) at depths \(1\) through \(5\). Their normalized Haar measures are \(1/16,1/16,1/64\), summing to \(9/64\).

**5. Infinite occurrence.** The recurrence matrix \(\left(\begin{smallmatrix}2&1\\1&0\end{smallmatrix}\right)\) has determinant \(-1\), so it acts invertibly on the finite state space modulo every positive modulus. Consequently the sequence of consecutive-value pairs is periodic from its initial state. Every attained class recurs on infinitely many nonnegative indices.

## Verification
Run `python3 verify.py` (Python standard library only). It independently enumerates all modular consecutive-pair states and compares the observed image with the three predicted balls for exponents \(1\le k\le14\). It separately checks odd-index valuation isometries at finite depth, the exceptional quadratic bijection, the predicted image counts, and modular recurrences. These are finite checks, not an exhaustive proof of the all-exponent assertion.

## Relationship to prior work
Lang and Lang's 2013 paper, *Three term recurrence and residue completeness* (arXiv:1307.7463, Proposition 5.2), proves that the Pell–Lucas sequence is residue-complete precisely for powers of 3. That theorem implies non-surjectivity modulo powers of 2, but neither gives which 2-adic residues occur nor implies the exact support measure \(9/64\). Carroll, Jacobson, and Somer's 1994 theorem on distribution of two-term recurrences modulo prime powers explicitly assumes primes greater than 7 and concerns the first-kind recurrence, so it does not cover this ramified prime-2 second-kind image. A later result on the limiting density of *Fibonacci* residues modulo prime powers concerns a different sequence and is only methodological context. Related primary classifications of Lucas sequences use MSC 11B39.

## Limitations
This result classifies image support, **not** the natural-density distribution of indices among supported classes. It does not establish originality relative to all historical literature; an equivalent unlocated classification could exist. The proof assumes the stated Pell–Lucas normalization and does not immediately generalize to arbitrary companion Lucas sequences or odd moduli. The finite verifier cannot substitute for the all-depth isometry argument.

## References
- Cheng Lien Lang and Mong Lung Lang, *Three term recurrence and residue completeness*, arXiv:1307.7463, initial public version July 29, 2013, especially Proposition 5.2 and Appendix A. https://arxiv.org/abs/1307.7463
- D. Carroll, E. Jacobson, and L. Somer, *Distribution of two-term recurrence sequences mod prime powers*, Fibonacci Quarterly 32 (1994), 260–268. https://www.fq.math.ca/Scanned/32-3/carroll.pdf
- C. Smyth, *The terms in Lucas sequences divisible by their indices*, arXiv:0908.3832 (2009), primary subject MSC 11B39. https://arxiv.org/abs/0908.3832
- *Limiting density of the Fibonacci sequence modulo powers of a prime*, Research in Number Theory (2025), DOI:10.1007/s40993-025-00667-1; comparison only (not Pell–Lucas).
