# Prime-relative Fuss–Catalan nondivisibility: exact spectra and p-adic dimension

## Finding

For every prime \(p\) and integer \(n\geq 0\), define the \((p+1)\)-ary Fuss–Catalan number
\[
F_p(n)=\frac{1}{pn+1}\binom{(p+1)n}{n}\in\mathbb Z.
\]
Write the base-\(p\) expansion of \(n\) as \(n=\sum_{j\geq0}d_jp^j\), with \(0\leq d_j<p\) and all sufficiently high digits zero. Then
\[
p\nmid F_p(n)\quad\Longleftrightarrow\quad d_j+d_{j+1}\leq p-1\quad\text{for every }j\geq0.
\]
For every integer \(r\geq1\), put
\[
N_p(r)=\#\{0\leq n<p^r:p\nmid F_p(n)\}.
\]
With \(\theta_j=(2j+1)\pi/(2p+1)\), for \(0\leq j<p\), the exact formula is
\[
\boxed{N_p(r)=\frac{1}{2p+1}\sum_{j=0}^{p-1}
\cot^2\!\left(\frac{\theta_j}{2}\right)
\left(\frac{(-1)^j}{2\sin(\theta_j/2)}\right)^{r-1}.}
\]
In particular, with
\[
\rho_p=\frac{1}{2\sin\!\left(\frac{\pi}{4p+2}\right)},\qquad
c_p=\frac{1}{2p+1}\cot^2\!\left(\frac{\pi}{4p+2}\right),
\]
we have \(1<\rho_p<p\) and
\[
N_p(r)\sim c_p\rho_p^{r-1}\qquad (r\to\infty).
\]
The indices \(n\geq0\) with \(p\nmid F_p(n)\) have natural density zero. Their closure \(K_p\) in the \(p\)-adic integers is exactly the set of infinite base-\(p\) digit sequences satisfying the adjacent-digit inequality. Its Hausdorff dimension in the normalized \(p\)-adic metric is
\[
\boxed{\dim_H(K_p)=\frac{\log\rho_p}{\log p}.}
\]
As \(p\) runs through the primes, this dimension tends to one, more precisely
\[
\dim_H(K_p)=1+\frac{\log(2/\pi)}{\log p}+O\!\left(\frac{1}{p\log p}\right).
\]

## Assumptions and scope

The symbol \(p\) always denotes a rational prime, including \(p=2\). The integer \(r\) is arbitrary and positive. The number \(F_p(n)\) is a Fuss–Catalan integer; the subscript records the prime relative to which the arity is \(p+1\), not arity \(p\). Leading zero digits are allowed. All density and dimension claims concern the same fixed prime \(p\), except for the final explicitly stated limit as \(p\to\infty\).

Set \(A_p=(a_{ij})_{0\leq i,j<p}\) with \(a_{ij}=1\) if \(i+j\leq p-1\) and \(a_{ij}=0\) otherwise. Thus, for each \(r\geq1\), \(N_p(r)=\mathbf{1}^{\mathsf T}A_p^{r-1}\mathbf 1\), where \(\mathbf1\) is the length-\(p\) all-ones vector.

## Proof

**1. Divisibility and digits.** The denominator \(pn+1\) is prime to \(p\). Kummer's theorem therefore identifies \(v_p(F_p(n))\) with the number of base-\(p\) carries in the addition \(n+pn\). The digit in position \(j\) of \(pn\) is \(d_{j-1}\), with \(d_{-1}=0\). No carry occurs precisely when \(d_j+d_{j-1}<p\) at every position. With leading zeros, this is equivalent to the displayed adjacent-digit inequalities. As a consequence, the admissible \(r\)-digit words are exactly paths of length \(r-1\) in the adjacency matrix \(A_p\), proving the matrix count. The empty integer \(n=0\) is admissible.

**2. Complete spectral decomposition.** Put \(\theta_j=(2j+1)\pi/(2p+1)\) and
\[
v^{(j)}_i=\cos\!\left((i+\tfrac12)\theta_j\right),\qquad 0\leq i<p.
\]
The finite cosine-sum identity yields
\[
(A_pv^{(j)})_i
=\sum_{h=0}^{p-1-i}\cos\!\left((h+\tfrac12)\theta_j\right)
=\frac{\sin((p-i)\theta_j)}{2\sin(\theta_j/2)}
=\frac{(-1)^j}{2\sin(\theta_j/2)}v^{(j)}_i.
\]
Thus \(v^{(j)}\) is an eigenvector with eigenvalue \(\lambda_j=(-1)^j/(2\sin(\theta_j/2))\). The \(\lambda_j\) are pairwise distinct, since their absolute values decrease strictly as \(j\) increases. Symmetry of \(A_p\) makes these eigenvectors orthogonal. Direct trigonometric summation gives
\[
\sum_{i=0}^{p-1}(v^{(j)}_i)^2=\frac{2p+1}{4},\qquad
\sum_{i=0}^{p-1}v^{(j)}_i=\frac{(-1)^j}{2}\cot\!\left(\frac{\theta_j}{2}\right).
\]
Resolving \(\mathbf1\) in this orthogonal eigenbasis and computing \(\mathbf1^{\mathsf T}A_p^{r-1}\mathbf1\) proves the exact finite trigonometric formula. The largest eigenvalue in absolute value is \(\lambda_0=\rho_p\), and its coefficient is \(c_p>0\), proving the asymptotic. The nonnegative matrix is primitive: each state reaches state zero, and state zero reaches every state, with a loop at zero. Its unequal row sums are \(p,p-1,\ldots,1\), so Perron–Frobenius theory gives \(1<\rho_p<p\).

**3. Natural density and closure.** Every admissible finite base-\(p\) word extends to an admissible infinite sequence by appending only zeros. Hence the closure of admissible ordinary nonnegative integers in \(\mathbb Z_p\) consists of exactly the infinite admissible words. The ratio \(N_p(r)/p^r\) tends to zero. For any \(p^r\leq X<p^{r+1}\), the number of admissible indices below \(X\) is at most \(N_p(r+1)=O(\rho_p^{r+1})\). Since \(\rho_p<p\), the ratio to \(X\) tends to zero, giving natural density zero for arbitrary cutoffs, not merely along prime powers.

**4. Dimension.** The \(p\)-adic cylinder given by \(r\) initial digits has diameter \(p^{-r}\). Exactly \(N_p(r)\) such cylinders meet \(K_p\), giving the upper bound \(\dim_H K_p\leq\log_p\rho_p\). For the lower bound, let \(v\) be the strictly positive eigenvector \(v^{(0)}\) of \(A_p\). Start a digit path with probability \(v_i/\sum_hv_h\) at digit \(i\), and use transition probabilities \(a_{ij}v_j/(\rho_pv_i)\). An admissible length-\(r\) cylinder ending at digit \(j\) has probability \(v_j/((\sum_hv_h)\rho_p^{r-1})\), uniformly bounded by a constant times \(\rho_p^{-r}\). The mass distribution principle in the ultrametric gives \(\dim_H K_p\geq\log_p\rho_p\), establishing equality.

Finally, as \(p\to\infty\), the Taylor expansion of sine gives \(\rho_p=(2p+1)/\pi+O(p^{-1})\). Taking logarithms proves the stated prime-asymptotic dimension formula.

## Verification

Run `python3 verify.py` from the same extracted directory. The script uses Python's standard library only, computes exact Fuss–Catalan numbers and adjacency-path counts for primes \(2,3,5,7,11\) across the ranges specified in the source, checks each index's digit criterion, and numerically checks the trigonometric spectral formulas and eigenvector identities. Expected output starts `VERIFY_OK` with 4449 index checks. These finite computations do not establish the unrestricted formulas; the proof above does.

Examples of exact block counts: \(N_2(10)=144\), \(N_3(6)=157\), \(N_5(4)=190\). The well-known binary special case is the count of binary words avoiding adjacent ones; here it is included as a consistency check, not claimed as new.

## Relationship to prior work

Stănică's 2000 study established divisibility descriptions for Fuss–Catalan numbers of arity equal to a prime power and stated the difficulty of other composite arities. His Theorem 4 concerns arity \(p\) and divisibility by \(p\); his prime-square analysis concerns arity \(p^2\). Our arity is instead \(p+1\) with the same prime as modulus. Sury (2009) reproved the prime-arity criterion, not the present prime-relative arity shift. Krattenthaler and Müller (2025), Section 7, likewise explicitly restrict the arity parameter to a power of the modulus prime. The classical Kummer theorem supplies the starting carry criterion but does not itself give the exact all-prime spectral enumeration or explicit \(p\)-adic dimension computed here. The \(p=2\) (fibbinary) specialization is classical and is not claimed as new.

## Limitations

The theorem concerns only divisibility by the specified prime \(p\), not complete prime-power residue distributions, primality, or factorization of Fuss–Catalan numbers. The asymptotic equivalent for \(N_p(r)\) is along prime-power cutoffs \(p^r\); no constant-coefficient asymptotic for arbitrary real cutoffs is asserted. Novelty is claimed only for the combined exact spectral count and dimension across all primes, not for Kummer's theorem, the adjacency test in isolation, or the binary specialization. Other equivalent counting formulas may exist under different digit-language terminology; independent historical-priority review is not performed.

## References

1. P. Stănică, *\(p^q\)-Catalan Numbers and Squarefree Binomial Coefficients*, arXiv:math/0010148, first posted 2000-10-15. https://arxiv.org/abs/math/0010148
2. B. Sury, *Generalized Catalan Numbers: Linear Recursion and Divisibility*, Journal of Integer Sequences 12 (2009), Article 09.7.5. https://cs.uwaterloo.ca/journals/JIS/VOL12/Sury/sury31.html
3. C. Krattenthaler and T. W. Müller, *A method for determining the mod-\(p^k\) behaviour of recursive sequences*, Aequationes Mathematicae 99 (2025), Section 7, DOI:10.1007/s00010-025-01195-0. https://link.springer.com/article/10.1007/s00010-025-01195-0
4. E. E. Kummer, classical base-\(p\) carry criterion for binomial valuations (1852), quoted as Theorem 3 in Reference 1.
