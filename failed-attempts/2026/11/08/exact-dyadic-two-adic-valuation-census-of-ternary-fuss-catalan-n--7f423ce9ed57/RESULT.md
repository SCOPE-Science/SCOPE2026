# Exact dyadic two-adic valuation census of ternary Fuss–Catalan numbers

## Finding
For every integer \(n\ge0\), the second-order Catalan (ternary Fuss–Catalan) number is
\[
C_n=\frac{1}{2n+1}\binom{3n}{n}.
\]
For every integer \(r\ge0\) set
\[
P_r(t)=\sum_{0\le n<2^r}t^{\nu_2(C_n)}.
\]
Then, as an identity of formal power series over \(\mathbb Z[t]\),
\[
\boxed{\sum_{r\ge0}P_r(t)z^r=\frac{(1+z)(1-tz)}{1-(1+t)z-(t^2-t+1)z^2+(t^2+t)z^3}.}
\]
In particular, \(P_0(t)=1\), \(P_1(t)=2\), \(P_2(t)=3+t^2\), and for \(r\ge3\),
\[
P_r(t)=(1+t)P_{r-1}(t)+(t^2-t+1)P_{r-2}(t)-(t^2+t)P_{r-3}(t).
\]
For every \(r\ge2\), exactly the valuations \(0,2,3,\ldots,r\) occur. No second-order Catalan number has exact two-adic valuation one. Exactly \(F_{r+2}\) of the indices \(0\le n<2^r\) have \(C_n\) odd, where \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\).

## Assumptions and scope
The exponent \(r\) is any nonnegative integer; \(t\) and \(z\) are formal indeterminates. The valuation \(\nu_2\) applies to the positive integer \(C_n\). Every coefficient \([t^j]P_r(t)\) counts exactly the indices in \(\{0,\ldots,2^r-1\}\) at which the valuation equals \(j\). The finite initial cases \(r=0,1\) are included. The result is specific to the two-adic valuations and dyadic index intervals; it does not assert a parallel law for all primes or arbitrary interval endpoints.

## Proof
**1. Convert to binary carries.** Because \(2n+1\) is odd, \(\nu_2(C_n)=\nu_2\binom{3n}{n}\). By Legendre's formula (or Kummer's theorem),
\[
\nu_2(C_n)=2s_2(n)-s_2(3n),
\]
where \(s_2\) denotes the binary digit sum. This is also the total number of carries when adding \(n\) and \(2n\) in base two.

Write \(n=\sum_{i=0}^{r-1}a_i2^i\), padding on the left with zeros as necessary, and put \(a_{-1}=0\), \(c_0=0\). The outgoing carry after position \(i\) is
\[
c_{i+1}=\left\lfloor\frac{a_i+a_{i-1}+c_i}{2}\right\rfloor.
\]
For each digit position, the contribution to the valuation is \(c_{i+1}\in\{0,1\}\). Once the \(r\) input bits have been read, the next input digit is zero. A final carry is produced precisely when \((a_{r-1},c_r)=(1,1)\); after that there can be no further carries.

**2. An exact four-state transfer matrix.** Order the states \((a_{i-1},c_i)\) as \((0,0),(1,0),(0,1),(1,1)\). The two choices \(a_i=0,1\), with transition weight \(t^{c_{i+1}}\), give
\[
T(t)=\begin{pmatrix}
1&1&0&0\\
1&0&0&t\\
1&0&0&t\\
0&0&t&t
\end{pmatrix}.
\]
The terminal contribution at the first digit beyond the index range is \(v(t)=(1,1,1,t)^\mathsf T\); the initial row is \(e=(1,0,0,0)\). Thus the exact, finite-word identity is
\[
P_r(t)=eT(t)^r v(t)\qquad(r\ge0).
\]
There is no omitted carry: a second trailing zero makes the outgoing carry zero, regardless of the state after the first trailing zero.

**3. Evaluate the resolvent.** In the polynomial ring, direct determinant and adjugate calculations yield
\[
\det(I-zT(t))=1-(1+t)z-(t^2-t+1)z^2+(t^2+t)z^3,
\]
and
\[
e\,\operatorname{adj}(I-zT(t))\,v(t)=(1+z)(1-tz).
\]
Since the determinant has constant term one, \((I-zT(t))^{-1}\) exists as a matrix of formal series. Therefore
\[
\sum_{r\ge0}P_r(t)z^r=e(I-zT(t))^{-1}v(t),
\]
which is precisely the asserted rational function. Multiplication by its denominator gives the displayed recurrence and its initial values.

**4. Zero valuation and the missing valuation one.** No carry occurs if and only if the binary string \(a_0,\ldots,a_{r-1}\) contains no two consecutive ones. The number of such length-\(r\) strings is \(F_{r+2}\), so \([t^0]P_r(t)=F_{r+2}\). The same parity characterization is classically known.

Suppose a first carry appears at position \(i\). Its incoming carry was zero, hence \(a_i=a_{i-1}=1\). At position \(i+1\), the inputs \(a_i=1\) and \(c_{i+1}=1\) force another carry, even if \(a_{i+1}=0\). This argument includes the trailing position \(i+1=r\). Thus every positive valuation is at least two; in particular \([t^1]P_r(t)=0\) for all \(r\).

**5. Exact support and upper bound.** The carry at position zero is impossible because \(a_{-1}=c_0=0\). There can be at most one carry in each position \(1,\ldots,r\), so \(\nu_2(C_n)\le r\) whenever \(0\le n<2^r\). Conversely, for every \(2\le j\le r\), choose \(n=2^j-1\). Then \(s_2(n)=j\) and \(s_2(3n)=j\), so \(\nu_2(C_n)=j\). Finally \(n=0\) has valuation zero. All the claimed valuation levels therefore occur, and no other levels do.

## Verification
The standalone script `verify_ternary.py` computes the weighted carry automaton without symbolic libraries and independently enumerates all integer indices \(0\le n<2^r\) for each \(0\le r\le16\) using the binary digit-sum identity. The script also constructs the integer \(C_n=\binom{3n}{n}/(2n+1)\) for every \(0\le n<384\), checking integrality and the valuation directly. It checks the Fibonacci odd-count law, the missing first valuation, the exact support, and coefficient totals. This confirms \(131071\) digit-sum samples and \(384\) direct large-integer cases; these finite tests do not replace the unrestricted transfer-matrix proof.

## Relationship to prior work
Zhao, Pan, and Sun study congruences for this same second-order Catalan sequence, primarily sums modulo odd primes. Their main displayed congruences do not give the dyadic two-adic valuation histogram. OEIS A085357 already records the parity of this sequence as the characteristic function of binary strings without adjacent ones; neither that parity fact nor its Fibonacci enumeration is claimed new. Barat and Grabner developed general digital-block transfer-matrix methods for binomial valuations and asymptotic distributions; the transfer-matrix *method* here is not novel, but their examined results do not state this exact finite-index rational histogram. A previously documented three-adic valuation histogram for the same sequence concerns the different prime three and index ranges \(0\le n<3^r\); it neither states nor formally implies the binary two-adic result. Kauers, Krattenthaler, and Müller analyze congruences for several other Fuss–Catalan families, rather than the polynomial here.

## Limitations
Historical completeness and priority remain subject to independent investigation; a general digital-function framework might yield this formula with further specialization. The rational function classifies dyadic blocks, not arbitrary intervals, and no generalization to other Fuss–Catalan orders or prime powers is asserted. The parity count and the underlying carry and transfer-matrix principles are previously known. The claimed new contribution is the *specific complete exact two-adic histogram*, the exact exclusion of valuation one, and the full support classification. No independent audit has been performed.

## References
- G. Barat and P. J. Grabner, *Distribution of binomial coefficients and digital functions*, Journal of the London Mathematical Society, published online January 30, 2002, pp. 523–547. Lawful full-text author copy: https://www.math.tugraz.at/~grabner/Publications/Binomial.pdf .
- L.-L. Zhao, H. Pan, and Z.-W. Sun, *Some congruences for the second-order Catalan numbers*, arXiv:0909.3733v1 (September 21, 2009), https://arxiv.org/abs/0909.3733 .
- *OEIS A001764*, ternary Fuss–Catalan numbers, https://oeis.org/A001764 .
- *OEIS A085357*, their parity sequence and binary no-adjacent-ones characterization, https://oeis.org/A085357 .
- *OEIS A036556*, oddness of the two-adic valuation of the related binomial coefficient, https://oeis.org/A036556 .
- M. Kauers, C. Krattenthaler, and T. W. Müller, *A method for determining the mod-\(2^k\) behaviour of recursive sequences, with applications to subgroup counting*, Electronic Journal of Combinatorics 18 (2012), https://www.combinatorics.org/ojs/index.php/eljc/article/download/v18i2p37/pdf/ .
