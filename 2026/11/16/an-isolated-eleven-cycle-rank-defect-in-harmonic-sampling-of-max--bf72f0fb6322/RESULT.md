# An isolated eleven-cycle rank defect in harmonic sampling of maximal independent sets on square cycles

## Finding
For every integer \(n\ge5\), sample uniformly from the inclusion-maximal independent sets of the squared labelled cycle \(C_n^2\). The covariance of its \(n\) binary occupation coordinates has an exact closed Fourier spectrum, and the dimension of the affine span of all incidence vectors is
\[
(\operatorname{rank}K_5,\ldots,\operatorname{rank}K_{11})=(4,2,6,7,9,10,10),\qquad
\operatorname{rank}K_n=n\quad(n\ge12).
\]
In particular, complete first-coordinate harmonic identifiability holds at lengths \(9\) and \(10\), fails again at length \(11\), then holds for every length at least \(12\). At length \(6\), the only nonconstant Fourier null modes are \(1,3,5\). The constant mode is null precisely at lengths \(5,6,7,8,11\). Here identifiability means the centered coordinate functions have no nontrivial linear dependence, or equivalently the covariance is positive definite.

## Assumptions and scope
The graph \(C_n\) has distinct labelled vertices \(0,\ldots,n-1\) cyclically, and \(C_n^2\) joins vertices at cycle distance one or two. All labelled **inclusion-maximal**, not merely maximum-cardinality, independent sets receive equal probability. Write \(X_i(S)=\mathbf1_{i\in S}\) and \(K_n=(\operatorname{Cov}(X_i,X_j))_{0\le i,j<n}\). Fourier eigenvectors are \((e^{2\pi i jr/n})_{r=0}^{n-1}\) for \(0\le j<n\); these are unitary after normalization by \(n^{-1/2}\). No rescaling of \(K_n\) is used.

Set \(a_m=0\) for negative integers, \(a_0=1\), and for positive integers put
\[a_m=a_{m-3}+a_{m-4}+a_{m-5}.\]
Define \(Z_n=3a_{n-3}+4a_{n-4}+5a_{n-5}\), \(p_n=a_n/Z_n\), and \(\omega_n=e^{2\pi i/n}\). For every \(n\ge5\), \(Z_n>0\) is the number of maximal independent sets and the **entire** spectrum is
\[
\boxed{\displaystyle
\Lambda_{n,j}=\frac{a_n+\sum_{d=1}^{n-1}a_da_{n-d}\omega_n^{-jd}}{Z_n}-n p_n^2\mathbf1_{j=0},\quad 0\le j<n.
}\]
The sum is real by the symmetry under \(d\mapsto n-d\).

## Proof
**Cyclic gap characterization.** List the occupied vertices of a nonempty independent set in cyclic order and measure successive forward gaps. Distance-two independence holds exactly when every gap is at least \(3\), and domination by the chosen vertices (equivalent to inclusion-maximality) holds exactly when every gap is at most \(5\). The latter equivalence follows because in a gap of \(6\) or more one may insert a vertex at distance at least three from both endpoints, whereas gaps \(3,4,5\) cover all omitted sites within distance two of a selected endpoint. Thus configurations correspond bijectively to cyclic gap lists with parts in \(\{3,4,5\}\) summing to \(n\).

**Exact counts and two-point function.** Let \(F(z)=z^3+z^4+z^5\). Then \(a_m=[z^m](1-F(z))^{-1}\) counts ordered compositions of length \(m\) into admissible gaps. Conditioning on site \(0\) being occupied identifies the configuration uniquely with such a composition of \(n\), so the number of sets containing \(0\) is \(a_n\). Conditioning on two distinct occupied sites \(0,d\) splits the circle into two independent ordered gap compositions; the number of such sets is \(a_da_{n-d}\). Finally,
\[
Z_n=n[z^n]\sum_{k\ge1}\frac{F(z)^k}{k}
=[z^n]\frac{zF'(z)}{1-F(z)}
=3a_{n-3}+4a_{n-4}+5a_{n-5}.
\]
The first equality counts each rooted cyclic composition with \(k\) selected vertices \(n/k\) times, so it counts each labelled set once. Consequently,
\[
\mathbb EX_0=p_n,\qquad
\mathbb EX_0X_d=\begin{cases}p_n,&d=0,\\a_da_{n-d}/Z_n,&1\le d<n.\end{cases}
\]
Rotational invariance makes \(K_n\) circulant. Fourier diagonalization of its first row proves the displayed eigenvalues, including the mean-subtraction term only for frequency zero.

**Criterion for a null frequency.** At a nonzero frequency \(j\), the expected unnormalized Fourier coefficient of \(X\) is zero. Therefore,
\[
\Lambda_{n,j}=\frac1n\mathbb E\left|\sum_{x\in S}\omega_n^{-jx}\right|^2\quad(j\ne0).
\]
This vanishes if and only if **every** maximal independent set has zero \(j\)-th Fourier coefficient. For \(n=8\), the cyclic gap lists \((3,5)\) and \((4,4)\) yield configurations differing only in the occupied site \(3\) versus \(4\). More generally, for \(n\ge11\), write \(n-8\) as a sum of parts in \(\{3,4,5\}\) (every integer at least three has such a decomposition), and replace the consecutive gaps \((3,5)\) by \((4,4)\), keeping the remaining gaps fixed. The two Fourier coefficients differ by \(\omega_n^{-3j}-\omega_n^{-4j}\), which is nonzero whenever \(j\ne0\). This establishes strict positivity of every nonconstant mode at \(n=8\) and all \(n\ge11\).

At \(n=5\), any one-site set has nonzero Fourier coefficient at every frequency. At odd lengths \(n=7\) and \(n=9\), respectively the configurations \(\{0,3\}\) and \(\{0,4\}\) have nonvanishing Fourier coefficients at all nonzero frequencies, since an odd-order root of unity cannot equal \(-1\). At \(n=10\), \(\{0,3,6\}\) has coefficient \(1+\omega_n^{-3j}+\omega_n^{-6j}\), which could vanish only if a tenth root of unity had order three; this is impossible. At \(n=6\), the complete configuration family is \(\{0,3\},\{1,4\},\{2,5\}\), and the Fourier coefficients vanish precisely for odd \(j\). Thus every nonconstant null mode is exactly as stated.

**The constant mode and the affine hull.** For \(j=0\), \(\Lambda_{n,0}=\operatorname{Var}(|S|)/n\). Because \(k\) admissible gaps can sum to every integer in the interval \([3k,5k]\), the attainable cardinalities are precisely the integers
\[\left\lceil\frac n5\right\rceil\le k\le\left\lfloor\frac n3\right\rfloor.\]
This interval contains only one integer exactly for \(n\in\{5,6,7,8,11\}\) among \(n\ge5\): check \(5\le n\le11\) directly; for \(n\ge12\), writing \(n=3h+r\) with \(h\ge4\) and \(0\le r\le2\) gives both \(h\) and \(h-1\) as feasible sizes since \(3(h-1)\le n\le5(h-1)\). Hence the constant mode is null at exactly those five lengths. Together with the preceding nonconstant-mode classification this gives all ranks. Since a finite distribution has full support on its configurations, the rank of its covariance equals their affine-hull dimension. This completes the proof.

## Verification
The standalone file `check.py` performs a separate bit-mask enumeration of every maximal independent set of \(C_n^2\) for each \(5\le n\le17\), checking the gap-count recurrence, all two-site counts, the Fourier covariance identity and the stated rank. It checks the gap-size interval and recurrence for larger lengths through \(120\). The checked script printed `PASS 639 families of exact-count, Fourier, rank, recurrence assertions`. Finite tests are corroboration only; the all-length statement follows from the gap-slide and cardinality proofs above. Run `python3 check.py` with Python 3. No external packages or data are required.

## Relationship to prior work
Galvin and Zhang's August 2024 paper studies domination polynomials and unimodality on powers of cycles. Its all-dominating-set distribution is not the uniform distribution on inclusion-maximal independent sets used here, and its polynomial recurrences do not provide covariance ranks. Cho, Kim, Kim and Oum's February 2022 paper establishes extremal independent-domination bounds on graphs of prescribed maximum degree, not the Fourier sampling geometry of maximal sets on these particular graph powers. Earlier harmonic calculations for maximal independent sets of ordinary cycles concern gap set \(\{2,3\}\), not the square-cycle gap set \(\{3,4,5\}\); their sharp rank threshold therefore does not imply the isolated length-eleven defect established here. General renewal transforms explain the shape of the finite covariance formula and are not asserted to be new.

## Limitations
This is an exact result for labelled square cycles at uniform maximal-set sampling, not for arbitrary graph powers, nonuniform fugacities, maximum-cardinality independent sets, or the broader class of all dominating sets. There is no claim about extremal positive eigenvalues or their asymptotic condition ratios. Historical priority is provisional: a specialized earlier affine-span theorem for distance-two independent dominating sets might imply the rank result even under different language.

## References
- D. Galvin and Y. Zhang, *The domination polynomial of powers of paths and cycles*, arXiv:2408.12731v1, first posted 2024-08-22, https://arxiv.org/abs/2408.12731.
- E.-K. Cho, J. Kim, M. Kim and S.-il Oum, *Independent domination of graphs with bounded maximum degree*, arXiv:2202.09594v1, first posted 2022-02-19, https://arxiv.org/abs/2202.09594.
