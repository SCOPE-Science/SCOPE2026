# Bessel–Toeplitz singular-jet law for exponential Hardy composition iterates

## Finding

Let \(H^2(\mathbb D)\) have orthonormal monomials \(1,z,z^2,\ldots\). Fix real \(0<r<1\) and \(a>0\), and define the compact weighted composition operator
\[
(Tf)(z)=e^{az}f(rz),\qquad A=\frac{a}{1-r},\qquad q_n=r^n.
\]
Write \(s_j(S)\) for the \(j\)-th singular value in decreasing order, with \(j=1\) denoting the largest. Let \(I_m\) be the modified Bessel function of integer order \(m\), and put
\[
D_0(A)=1,\qquad D_j(A)=\det\bigl[I_{k-\ell}(2A)\bigr]_{k,\ell=0}^{j-1}\quad(j\ge1).
\]
Then \(D_j(A)>0\), and for **every fixed integer \(j\ge1\)**,
\[
\boxed{\lim_{n\to\infty}\frac{s_j(T^n)}{r^{n(j-1)}}
=c_j(A):=\sqrt{\frac{D_j(A)}{D_{j-1}(A)}}.}
\]
The constants satisfy \(1<c_j(A)\), \(c_{j+1}(A)\le c_j(A)\) for all \(j\ge1\), and \(\lim_{j\to\infty}c_j(A)=1\). Meanwhile the nonzero eigenvalues of \(T^n\) are exactly \(q_n^{k}\), \(k=0,1,\ldots\), each simple. Thus all fixed-rank approximation-number coefficients exceed the corresponding eigenvalue coefficients, but this finite-rank inflation vanishes as rank increases. For example,
\[
 c_1(A)=\sqrt{I_0(2A)},\qquad
 c_2(A)=\sqrt{I_0(2A)-\frac{I_1(2A)^2}{I_0(2A)}}.
\]

## Assumptions and scope

The domain and codomain are the usual complex Hardy Hilbert space \(H^2(\mathbb D)\) with normalized boundary measure, and \(0<r<1\), \(a>0\) are fixed before \(n\to\infty\). No uniform-in-\(j\) or simultaneous joint \(j,n\to\infty\) assertion is made. The Bessel normalization is
\[
I_m(2A)=\frac1{2\pi}\int_{0}^{2\pi}e^{2A\cos\theta}e^{-im\theta}\,d\theta.
\]
All formulae remain true at \(a=0\) after replacing the strict inequality by \(c_j(0)=1\); the theorem is stated for \(a>0\) to expose genuine nonnormality.

## Proof

**Step 1 (exact iterate and spectrum).** Multiplication by \(e^{Az}\) is bounded and invertible on \(H^2\). If \(D_rf(z)=f(rz)\), then
\[
T=M_{e^{Az}}D_rM_{e^{-Az}},\qquad
T^nf(z)=e^{A(1-q_n)z}f(q_nz).
\]
In particular, the spectrum of \(T^n\) is \(\{0\}\cup\{q_n^k:k\ge0\}\), with simple nonzero eigenvalues, because \(D_{q_n}\) is diagonal on the monomials. Compactness follows from the geometric diagonal decay.

**Step 2 (all exterior powers).** Put \(w_q(z)=e^{A(1-q)z}\), \(u_{k,q}(z)=z^kw_q(z)\), and \(e_k(z)=z^k\). For \(0<q<1\),
\[
T_q:=M_{w_q}D_q,\qquad T_qe_k=q^ku_{k,q}.
\]
For fixed \(j\), let \(J_0=(0,1,\ldots,j-1)\), with \(m_0=j(j-1)/2\). On the orthonormal exterior basis \(e_J=e_{k_1}\wedge\cdots\wedge e_{k_j}\),
\[
q^{-m_0}(\wedge^jT_q)e_J
=q^{k_1+\cdots+k_j-m_0}
 (u_{k_1,q}\wedge\cdots\wedge u_{k_j,q}).
\]
There is one index tuple with exponent zero, namely \(J_0\). Each \(\|u_{k,q}\|\le e^A\), uniformly in \(k\) and \(0<q<1\). The Hilbert–Schmidt norm squared of the contribution of all other tuples is bounded by
\[
e^{2Aj}\sum_{J\ne J_0}q^{2(\sum k_i-m_0)}=O_j(q^2),
\]
as follows by comparison with the convergent generating product \(\prod_{h=1}^{j}(1-q^{2h})^{-1}\). Also \(u_{k,q}\to u_k=z^ke^{Az}\) in \(H^2\). Thus
\[
q^{-m_0}\wedge^jT_q\longrightarrow
(u_0\wedge\cdots\wedge u_{j-1})\otimes e_{J_0}
\]
in Hilbert–Schmidt, hence operator, norm. For compact operators, \(\|\wedge^jS\|=\prod_{h=1}^j s_h(S)\). Therefore
\[
\lim_{q\downarrow0}q^{-j(j-1)/2}\prod_{h=1}^j s_h(T_q)
=\|u_0\wedge\cdots\wedge u_{j-1}\|=\sqrt{D_j(A)}.
\]
Here the last equality follows from the Gram determinant identity, since
\[
\langle u_k,u_\ell\rangle
=\frac1{2\pi}\int_0^{2\pi}e^{2A\cos\theta}
 e^{i(k-\ell)\theta}\,d\theta=I_{k-\ell}(2A).
\]
The vectors are linearly independent, proving \(D_j(A)>0\). Divide the consecutive exterior-power limits to obtain the claimed singular-value formula for \(q=q_n\to0\).

**Step 3 (strict inflation and rank rigidity).** Gram–Schmidt gives
\[
c_j(A)^2=
\min_{p(z)=z^{j-1}+\sum_{k=0}^{j-2}b_kz^k}
\frac1{2\pi}\int_0^{2\pi}e^{2A\cos\theta}|p(e^{i\theta})|^2\,d\theta.
\]
For every monic polynomial \(p\), Jensen's formula and the arithmetic–geometric-mean inequality imply
\[
\frac1{2\pi}\int e^{2A\cos\theta}|p(e^{i\theta})|^2d\theta
\ge \exp\biggl(\frac1{2\pi}\int\log|p(e^{i\theta})|^2d\theta\biggr)
=\prod_{p(\zeta)=0}\max\{1,|\zeta|^2\}\ge1.
\]
Equality is impossible when \(A>0\): equality in arithmetic–geometric mean would require \(e^{2A\cos\theta}|p(e^{i\theta})|^2\) to be constant almost everywhere, whereas the squared modulus of a polynomial is a finite Laurent polynomial and cannot equal a nonzero multiple of \(e^{-2A\cos\theta}\). Existence of the minimizing monic polynomial follows from positive definiteness of its finite Gram matrix. Hence \(c_j(A)>1\).

Multiplication of a monic polynomial by \(z\) preserves the integral on the circle, showing \(c_{j+1}(A)\le c_j(A)\). Finally consider the monic polynomial
\[
p_j(z)=\sum_{m=0}^{j-1}\frac{(-A)^m}{m!}z^{j-1-m}.
\]
Uniformly on \(|z|=1\), \(p_j(z)\) approaches \(z^{j-1}e^{-Az^{-1}}\) up to an error tending to zero as \(j\to\infty\). Since \(|e^{Az}z^{j-1}e^{-Az^{-1}}|=1\) on the unit circle, its candidate integral tends to \(1\). Consequently \(\limsup_{j\to\infty}c_j(A)^2\le1\). Combined with the lower bound, \(c_j(A)\downarrow1\), finishing the proof.

## Verification

The standalone \(checker.py\) builds finite monomial-matrix compressions of the **actual** iterate \(T^n\), independently evaluates the Bessel Gram determinants, compares their first four normalized singular values, and checks the Toeplitz-minor monotonicity and exact weighted-composition coefficient identity. It reports reproducible finite tests. These tests support the calculations but are not used to establish any infinite-dimensional limit. The preceding exterior-power and polynomial arguments prove the assertion for every fixed rank.

## Relationship to prior work

Chalendar–Partington (arXiv:1910.01475, Sections 1–2) provide general weak and norm convergence criteria for iterated weighted composition operators, including convergence to a fixed-point evaluation projection. Lechner–Li–Queffélec–Rodríguez-Piazza (arXiv:1612.01177, Section 2) study approximation numbers and bounds and a **fixed-operator large-singular-index** spectral-radius law. Putinar–Tener (arXiv:1612.03970, Sections 1–3) study singular values for a geometric derivative-weighted composition class and its exterior powers. None of those inspected statements gives the present **fixed-singular-index, increasing-iterate** limits with explicit Bessel–Toeplitz constants. Standard weighted Toeplitz prediction theory supplies background for the Gram-minor interpretation; the particular composition-iterate statement is the subject here, not a claim that Toeplitz determinants themselves are new.

## Limitations

The asymptotics are pointwise in fixed \(j\) and fixed \(a,r\), not uniform as rank, weight, or contraction strength varies. No complete finite-\(n\) closed formula for singular values is asserted. Similar results may be derivable from general prediction-theory or exterior-power principles in older literature; priority has not been independently certified. The numeric checker establishes no infinite-dimensional result.

## References

1. G. Lechner, D. Li, H. Queffélec, L. Rodríguez-Piazza, *Approximation numbers of weighted composition operators*, first public arXiv posting 4 December 2016, arXiv:1612.01177, https://arxiv.org/abs/1612.01177.
2. M. Putinar, J. E. Tener, *Singular values of weighted composition operators and second quantization*, first public arXiv posting 12 December 2016, arXiv:1612.03970, https://arxiv.org/abs/1612.03970.
3. I. Chalendar, J. R. Partington, *Weighted composition operators: isometries and asymptotic behaviour*, first public arXiv posting 3 October 2019, arXiv:1910.01475, https://arxiv.org/abs/1910.01475.
