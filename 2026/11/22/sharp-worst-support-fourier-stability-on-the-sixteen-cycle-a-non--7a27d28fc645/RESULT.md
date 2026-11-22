# Sharp worst-support Fourier stability on the sixteen-cycle: a nonconsecutive optimal sampling orbit

## Finding

Let \(\zeta=\exp(2\pi i/16)\), and write \(F=(\zeta^{rc})_{0\le r,c<16}\), with **no normalization**. For any four-point sampling set \(R\subset\mathbb Z/16\mathbb Z\), define its worst-frequency squared lower sampling bound by
\[
\gamma(R)=\min_{\substack{C\subset\mathbb Z/16\mathbb Z\\ |C|=4}}\lambda_{\min}\big(F[R,C]^*F[R,C]\big).
\]
Then the maximizing sets among **all** \(\binom{16}{4}=1820\) sampling sets are exactly
\[
\boxed{\{u\{0,1,3,14\}+b:u\in(\mathbb Z/16\mathbb Z)^\times,\ b\in\mathbb Z/16\mathbb Z\}},
\]
a single affine orbit of cardinality \(64\). This is strictly different from the orbit of four consecutive samples.

The extremizers satisfy the rigorous, frequency-uniform separation
\[
\gamma(R)>\frac1{1000}\quad\text{for all 64 maximizing sets},
\qquad
\gamma(R)<\frac1{1000}\quad\text{for all other 1756 sets}.
\]
For the \(192\) nonoptimal full-spark sets, the bound is also strictly positive; for the remaining \(1564\) sets, it equals zero. These strict rational inequalities, not a decimal approximation of the optimal value, are the certified statement.

## Assumptions and scope

The signal has exactly four unknown Fourier frequencies chosen arbitrarily among the sixteen cyclic frequencies. Samples are observed at four known positions \(R\), and additive noise is measured in the standard Euclidean norm. For a fixed support \(C\), the inverse reconstruction gain is the reciprocal of the least singular value of the \(4\times4\) matrix \(F[R,C]\). Thus maximizing \(\gamma(R)\) selects the sampling positions with the best guarantee over all four-frequency supports. A factor \(1/\sqrt{16}\) applied to every Fourier entry rescales all \(\gamma\) by the same \(1/16\) and does not change any optimizer.

## Proof

**1. Eliminate singular designs.** The prime-power full-spark criterion [1, Theorem 9], also given in the universal-sampling language in [2, Theorem 4], says that a four-row restriction of \(F\) is invertible on *every* four-frequency support if and only if its rows represent each residue class modulo four exactly once. Consequently, exactly \(4^4=256\) of the 1820 row sets have \(\gamma(R)>0\), while the other 1564 sets have \(\gamma(R)=0\).

**2. Reduce to three symmetry orbits.** For odd \(u\) and arbitrary \(b\), replacing \(R\) by \(uR+b\) multiplies Fourier columns by unimodular phases and permutes the set of all four-frequency supports through the bijection \(c\mapsto uc\). These operations preserve all singular values, and hence \(\gamma(R)\). Applying the \(128\) affine maps \(r\mapsto ur+b\) to the three sets
\[
R_0=\{0,1,2,3\},\qquad R_1=\{0,1,2,7\},\qquad R_2=\{0,1,3,14\}
\]
produces pairwise-disjoint orbits of respective sizes \(64,128,64\). Their union is precisely the 256 sets containing one representative of each residue modulo four (checked exhaustively as finite integer sets in the accompanying certificate). Therefore these three representatives exhaust the nonzero cases.

**3. Exclude the first two orbits with exact witnesses.** Let \(G(R,C)=F[R,C]^*F[R,C]\), and put \(H(R,C)=1000G(R,C)-I_4\). A negative determinant of a Hermitian \(H\) forces some negative eigenvalue; hence \(\lambda_{\min}(G)<1/1000\). Exact cyclotomic-ring calculation yields
\[
\det H(R_0,\{0,1,2,3\})<0,\qquad
\det H(R_1,\{0,1,4,5\})<0.
\]
The standalone `certificate.py` records the full integer coefficients of both determinants and rigorous negative-sign margins. Affine invariance excludes every row set in the first two orbits.

**4. Prove a uniform strict bound for the third orbit.** Fix \(R_2\). For each of the \(\binom{16}{4}=1820\) four-frequency supports \(C\), compute the first four leading principal minors of the Hermitian matrix \(H(R_2,C)\). All \(1820\) minors at each size \(k=1,2,3,4\) are **strictly positive** by a complete integer certificate. By Sylvester's criterion every such matrix is positive definite, so \(\lambda_{\min}(G(R_2,C))>1/1000\) for every frequency support. Affine invariance extends this to the entire third orbit.

**5. Exactness of the finite certificate.** Represent \(\zeta\) in the integral ring \(\mathbb Z[t]/(t^8+1)\). The Gram entries are sums of four sixteenth roots of unity, and the determinant of each principal minor is computed by its complete signed permutation expansion in that ring. Hermitian symmetry is verified algebraically by the conjugation map \(t\mapsto t^{-1}\). Every real cyclotomic integer \(a=\sum_{j=0}^7 a_j\zeta^j\) is signed by rational lower and upper bounds for \(\cos(j\pi/8)\), derived solely from integer square-root flooring and the radical identities for half-angle cosines. The program uses scale \(10^{25}\), checks that no sign interval meets zero, and requires strict positive signs for all \(7280\) relevant leading minors. No floating-point output, unproved numerical tolerance, or unexamined frequency set enters this proof.

The first two orbits each have a witnessed bad frequency support; the third satisfies the uniform positive-definiteness inequalities. Combining the exhaustive orbit partition with the full-spark theorem proves the claimed *exact optimizer class*.

## Verification

Run `python3 certificate.py` with Python 3 and no external packages. It checks the complete set of 256 universal row sets and its three affine orbits, both strict negative-determinant witnesses, and all 1820 frequency supports for the optimal orbit with four exact principal-minor sign checks each. The expected final line begins `PASS: all optimal 64 row sets`. The complete output and its positive sign margins are embedded in `certificate_output.txt`.

Run `python3 numeric_crosscheck.py` for an independently implemented, direct complex-matrix and real-symmetric Jacobi diagonalization of the three representative squared smallest singular values. This independent floating-point experiment is *diagnostic only*. It finds approximately \(0.000372349629\), \(0.000490835751\), and \(0.001201522338\) in the order \(R_0,R_1,R_2\), agreeing with the exact separating threshold without constituting its proof.

## Relationship to prior work

Alexeev, Cahill and Mixon [1, Theorem 9] classify the full-spark Fourier row sets for prime powers; this establishes which 256 candidates have a strictly positive lower bound, but does **not** compare their worst-case smallest singular values. Osgood, Siripuram and Wu [2, Appendix A] explicitly discuss potentially severe condition numbers for the **consecutive** universal sampling set and derive a lower bound for that design, without determining a minimax optimizer across all universal sets. A prior exact order-sixteen census [3] classifies the rank of every four-by-four submatrix, including its three universal affine row orbits, but its rank-only data are insensitive to the spectral separation and therefore do not imply the strict threshold or winning orbit. In particular, full-sparkness is a qualitative positivity property, while the present result compares uniform quantitative noise stability.

## Limitations

The statement is an exactly certified **finite** minimax classification for cyclic order 16 and precisely four unknown Fourier frequencies. It does not supply an algebraic closed form for the optimum \(\gamma(R_2)\), nor address other cycle sizes, other support sizes, or average-case reconstruction. No inference about those settings is made. A yet-unlocated publication or unpublished table containing the same minimax numerical comparison could affect historical priority. The exact proof has undergone a self-review but no independent mathematical audit.

## References

[1] B. Alexeev, J. Cahill, D. G. Mixon, *Full Spark Frames*, arXiv:1110.3548, first posted 2011-10-17. https://arxiv.org/abs/1110.3548

[2] B. Osgood, A. Siripuram, W. Wu, *Discrete Sampling and Interpolation: Universal Sampling Sets for Discrete Bandlimited Spaces*, arXiv:1204.0992, first posted 2012-04-04. https://arxiv.org/abs/1204.0992

[3] *Complete fourth-order rank incidence for the cyclic 16-point Fourier transform*, exact order-sixteen rank census. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-complete-fourth-order-rank-incidence-for-the-cyclic-16-point-fou--d844f172dad8
