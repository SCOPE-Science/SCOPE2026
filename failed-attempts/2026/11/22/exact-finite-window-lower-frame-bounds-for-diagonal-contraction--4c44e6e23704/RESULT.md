# Exact finite-window lower frame bounds for diagonal contraction semigroups

## Finding

Let \(n\geq1\), let \(0<\lambda_1<\cdots<\lambda_n\), and let \(S(t)=\operatorname{diag}(e^{-\lambda_1t},\ldots,e^{-\lambda_nt})\) on the real Hilbert space \(\mathbb R^n\). For \(T>0\), define the finite-window frame operator
\[
F_T(b)=\int_0^T S(t)bb^{\mathsf T}S(t)\,dt,
\qquad \|b\|_2=1,
\]
and its maximal optimal lower frame bound \(\Gamma(T)=\max_{\|b\|_2=1}\lambda_{\min}(F_T(b))\).

Write
\[
K_T=\left(\frac{1-e^{-(\lambda_i+\lambda_j)T}}{\lambda_i+\lambda_j}\right)_{i,j=1}^n,
\quad D=\operatorname{diag}((-1)^1,\ldots,(-1)^n),
\quad R_T=DK_T^{-1}D,
\quad s_T=\mathbf1^{\mathsf T}R_T\mathbf1.
\]
For **every** finite \(T>0\), all entries of \(R_T\) are strictly positive and
\[
\boxed{\Gamma(T)=s_T^{-1},\qquad
|b_i|^2=\frac{(R_T\mathbf1)_i}{s_T}\quad(1\le i\le n).}
\]
Exactly the \(2^n\) coordinatewise choices of signs of the displayed strictly positive magnitudes are optimal (including the two choices for \(n=1\)). Every normalized vector with a nonzero coordinate missing has lower frame bound zero.

Moreover, with \(\beta_i=\prod_{j\ne i}(\lambda_i-\lambda_j)^{-1}\), and
\(c_n=((n-1)!)^2(2n-1)\binom{2n-2}{n-1}^2\),
\[
\boxed{\lim_{T\downarrow0}\frac{\Gamma(T)}{T^{2n-1}}
=\frac{1}{c_n(\sum_i|\beta_i|)^2},\qquad
\lim_{T\downarrow0}|b_i(T)|^2=\frac{|\beta_i|}{\sum_j|\beta_j|}.}
\]
As \(T\to\infty\), the exact formula converges to the same inverse-row-sum prescription for the Cauchy matrix \(K_\infty=(1/(\lambda_i+\lambda_j))_{ij}\). The claimed new result is the **full finite-window optimizer and value for every horizon**, not the previously established infinite-horizon optimization or the known first small-time coefficients.

## Assumptions and scope

The Hilbert space is finite-dimensional and real; the generator is self-adjoint, strictly negative, and has simple spectrum. The time window is the full interval \([0,T]\) with Lebesgue measure. The vector is normalized in the Euclidean norm and the objective is the **minimum eigenvalue** of the continuous frame operator, not its determinant, condition number, or the optimal covariance relaxation. Spectral signs of the modes are immaterial, but mixing eigenspaces is excluded by the stated diagonal form (an orthogonal change of coordinates yields the same statement for any real symmetric negative-definite generator with simple spectrum).

## Proof

**1. Strict total positivity of the finite-window kernel.** For any ordered index subsets \(I,J\) of the same size \(m\), continuous Cauchy–Binet/Andréief integration gives
\[
\det K_T[I,J]
=\int_{0<t_1<\cdots<t_m<T}
\det(e^{-\lambda_i t_k})_{i\in I,k}
\det(e^{-\lambda_j t_k})_{j\in J,k}\,dt_1\cdots dt_m.
\]
For increasing real decay rates and increasing positive times, each determinant has the fixed sign \((-1)^{m(m-1)/2}\) and is never zero: a nontrivial sum of \(m\) exponentials with distinct real exponents cannot have \(m\) distinct zeros, proved inductively by dividing by the first exponential and using Rolle's theorem. The sign follows by letting all times coalesce and evaluating the resulting Vandermonde determinant. Thus the integrand is strictly positive on an open set, and **every** minor of \(K_T\) is positive. In particular \(K_T\) is positive definite (also directly a Gram matrix), its cofactors are nonzero, and Cramer's rule gives \((-1)^{i+j}(K_T^{-1})_{ij}>0\). Hence \(R_T>0\) entrywise.

**2. Universal lower bound on the inverse frame norm.** If all \(b_i\ne0\), then \(F_T(b)=B K_T B\), with \(B=\operatorname{diag}(b_i)\), so \(F_T(b)^{-1}=B^{-1}K_T^{-1}B^{-1}\). The unit vector \(Db\) has Rayleigh quotient
\[
(Db)^{\mathsf T}F_T(b)^{-1}(Db)=\mathbf1^{\mathsf T}R_T\mathbf1=s_T.
\]
Therefore \(\lambda_{\max}(F_T(b)^{-1})\ge s_T\), or equivalently \(\lambda_{\min}(F_T(b))\le s_T^{-1}\). A zero coordinate makes the Gram matrix singular and cannot maximize this positive bound.

**3. Attainment and uniqueness.** The numbers \(q_i=(R_T\mathbf1)_i/s_T\) are strictly positive and sum to one. Take \(b_i=\pm\sqrt{q_i}\). Direct multiplication shows \(F_T(b)^{-1}(Db)=s_T(Db)\). After diagonal sign similarity, \(F_T(b)^{-1}\) becomes the entrywise strictly positive symmetric matrix \(\operatorname{diag}(q_i^{-1/2})R_T\operatorname{diag}(q_i^{-1/2})\). Its eigenvector \((\sqrt{q_i})\) is strictly positive, so the Perron–Frobenius theorem implies that \(s_T\) is its **largest** eigenvalue. This proves equality. Conversely, any maximizing \(b\) makes \(Db\) attain its Rayleigh upper bound; it must be an eigenvector with eigenvalue \(s_T\). Its coordinate equations force \(b_i^2=(R_T\mathbf1)_i/s_T\), proving exact uniqueness of the squared magnitudes, and every independent sign choice works.

**4. The sharp short-window constant.** Let \(f_i(t)=e^{-\lambda_i t}\) and \(M_{ik}=(-\lambda_i)^k/k!\) for \(0\le k<n\). The Vandermonde-type matrix \(M\) is invertible. The transformed functions \(g_k(t)=\sum_i(M^{-1})_{ki}f_i(t)\) satisfy \(g_k(t)=t^k+O(t^n)\), uniformly for \(0\le t\le T\). Their scaled Gram matrix tends in operator norm to the positive Hilbert moment matrix \(H_{k\ell}=1/(k+\ell+1)\), after diagonal scaling by \(T^{k+1/2}\). Consequently,
\[
T^{2n-1}K_T^{-1}\longrightarrow (H^{-1})_{n-1,n-1}
(M^{-\mathsf T}e_{n-1})(M^{-\mathsf T}e_{n-1})^{\mathsf T}.
\]
Lagrange interpolation gives \((M^{-\mathsf T}e_{n-1})_i=(-1)^{n-1}(n-1)!\beta_i\). The shifted Legendre polynomial of degree \(n-1\) has leading coefficient \(\binom{2n-2}{n-1}\) and squared \(L^2[0,1]\) norm \(1/(2n-1)\). Its monic normalization shows
\((H^{-1})_{n-1,n-1}=(2n-1)\binom{2n-2}{n-1}^2\). Thus \(T^{2n-1}K_T^{-1}\to c_n\beta\beta^{\mathsf T}\). For ordered eigenvalues the signs of \(\beta_i\) alternate, so conjugating by \(D\) and taking positive row sums yields \(T^{2n-1}s_T\to c_n(\sum_i|\beta_i|)^2\) and the asserted limits of the optimal squared magnitudes.

**5. Long-window limit.** The entries of \(K_T\) converge to those of the positive definite Cauchy matrix \(K_\infty\). Inverse and normalized row sums are continuous on the positive-definite cone; hence the exact limit follows.

## Verification

The independently executable standard-library program `verify.py` checks the strictly positive checkerboard inverse, positive normalized optimal weights, the attained least eigenvalue, randomized competitor bounds for two- to four-mode examples, exact rational long-window examples, and high-precision short-window constants. It prints `FINITE_WINDOW_FRAME_CHECK_OK 1013`. These finite tests corroborate but do **not** replace the proof for arbitrary dimension, rates, and horizons.

For decay rates \((1,2)\), the short-window limit has \(|b_i|^2\to1/2\) and \(\Gamma(T)\sim T^3/48\); the long-window optimum has squared weights \((7/17,10/17)\) and lower bound \(1/102\). For rates \((1,2,3)\), the corresponding short-window weights are \((1/4,1/2,1/4)\), with \(\Gamma(T)\sim T^5/2880\), while the long-window weights are \((41/321,155/321,125/321)\), with lower bound \(1/3852\). This difference demonstrates genuinely horizon-dependent optimizers.

## Relationship to prior work

Bailey, Gallardo-Gutiérrez and Partington (2026) study which \(C_0\)-semigroup orbits form continuous frames, including a cogenerator criterion, but do not give optimized finite-window lower frame bounds. Chen and Belabbas (2016), Theorem 1, **already solve** the all-dimensional infinite-horizon scalar-actuator problem for real symmetric positive-definite dynamics, using a checkerboard inverse of a Cauchy matrix; that infinite-horizon conclusion is explicitly **not** claimed new. Trélat and Zuazua (2026), Theorem 2.4 and Proposition 2.6, establish the leading and next-order **small-horizon** scalar-actuator asymptotics and spectral weights, along with rank-constrained comparison and global statements about the relaxed covariance problem. In contrast, the present exact finite-window row-sum formula handles every finite horizon for the simple-spectrum self-adjoint semigroup with a single generating vector, with global uniqueness of its modal magnitudes. Its short-window leading constants agree with their results and are supplied for independent consistency checks, not as separate novelty claims.

## Limitations

The finite-window classification uses strict total positivity specific to strictly ordered **real** exponential decays; it does not classify nonnormal generators, complex frequencies, repeated spectral values, arbitrary sampling measures, multiple generator vectors, or the full semidefinite covariance relaxation. The novelty assessment remains subject to the possibility of an older equivalent result expressed through total positivity or optimal design; no claim of a unique historical priority or independent review is made. All statements are finite-dimensional and concern deterministic Lebesgue-time integration.

## References

1. V. Bailey, E. A. Gallardo-Gutiérrez and J. R. Partington, *Frames Associated with C0-Semigroups*, arXiv:2611.13867v1 (first posted 10 November 2026), https://arxiv.org/html/2611.13867v1 .
2. X. Chen and M.-A. Belabbas, *Optimal actuator design for minimizing the worst-case control energy*, arXiv:1610.08885 (first posted 27 October 2016), https://arxiv.org/abs/1610.08885 .
3. E. Trélat and E. Zuazua, *Optimal Actuator Design across Ranks and Control Horizons*, arXiv:2609.37081 (first posted 29 September 2026), lawful open-access full text https://dcn.nat.fau.eu/wp-content/uploads/actuator.pdf .
4. E. Trélat and E. Zuazua, *Two-term small-time spectral expansions for controllability Gramians*, arXiv:2609.37077 (first posted 29 September 2026), https://arxiv.org/abs/2609.37077 .
