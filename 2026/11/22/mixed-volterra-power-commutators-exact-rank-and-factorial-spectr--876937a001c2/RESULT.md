# Exact rank of mixed Volterra-power commutators at unequal orders

## Finding
For distinct positive integers \(m,n\), let \(Vf(x)=\int_0^x f(t)\,dt\) on complex \(L^2(0,1)\) with Lebesgue measure, and let \(V^*f(x)=\int_x^1 f(t)\,dt\). Then
\[
\operatorname{rank}\bigl(V^m(V^*)^n-(V^*)^nV^m\bigr)=2\min(m,n).
\]
Here rank means the dimension of the actual operator range. This is an exact result for the unweighted interval and positive integer orders, not a discretization or a result about fractional powers.

## Proof
Fubini gives the kernel \([y^n-(1-x)^n]/n!\) for \([V,(V^*)^n]\): the two terms of the commutator have kernels \([y^n-(y-x)_+^n]/n!\) and \([(1-x)^n-(y-x)_+^n]/n!\), respectively. The adjoint of the mixed commutator interchanges \(m\) and \(n\), so take \(m<n\). Telescoping gives
\[
[V^m,(V^*)^n]=\sum_{j=0}^{m-1}V^j[V,(V^*)^n]V^{m-1-j}.
\]
Each summand has kernel
\[
\frac1{n!}\left[(V^j1)(x)((V^*)^{m-1-j} p)(y)-(V^j q)(x)((V^*)^{m-1-j}1)(y)\right],
\quad p(y)=y^n,\quad q(x)=(1-x)^n.
\]
The \(2m\) left polynomials have distinct degrees: \(j\) and \(n+j\), for \(0\le j<m\). The \(2m\) right polynomials also have distinct degrees: \(n+m-1-j\) and \(m-1-j\). Each integration raises a nonzero polynomial's degree by one; reversing the integration endpoint changes the leading coefficient's sign but cannot annul it. Thus both lists are independent. In particular the right list's real polynomials give independent moment functionals on complex \(L^2\): their positive definite Gram matrix makes the map to \(\mathbb C^{2m}\) onto. Each coefficient in the separated sum is nonzero, so the range is precisely the span of the \(2m\) left polynomials. This proves the rank equality. \(\square\)

## Verification
The proof gives a checkable separated kernel and proves its rank uniformly. `verify_unequal.py` uses exact integer and rational arithmetic to form coefficient matrices directly from the Fubini kernels, check both polynomial pieces agree, and check the ranks for all 20 ordered unequal pairs with \(1\le m,n\le5\). Run `python3 verify_unequal.py`. The finite replay corroborates the formula but is not its all-orders proof.

## Relationship to prior work and limitations
*Integer-order collapse and infinite signed inertia of fractional Volterra self-commutators* gives the equal-order rank, signed inertia, and factorial spectral product, which are not contributions claimed here. *A note on self-commutators of Volterra operator and its square* treats particular equal-order norms. Ransford and Tsedenbayar and the opposing-power-pencil note concern linear combinations of forward and adjoint powers, not this mixed product. The rank-two building block and telescoping identity are standard techniques; the result identifies the exact rank rather than merely deriving a finite-rank bound. Older finite-interval convolution results may bear on priority. No conclusion on the unequal-order spectra is claimed.

## References
- *Integer-order collapse and infinite signed inertia of fractional Volterra self-commutators* (2026), [statement](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-integer-order-collapse-and-infinite-signed-inertia-of-fractional--393dc59f3565/RESULT.md).
- T. Ransford and D. Tsedenbayar, *On the real and imaginary parts of powers of the Volterra operator*, [arXiv:2402.09287](https://arxiv.org/abs/2402.09287).
- L. Khadkhuu and D. Tsedenbayar, *A note on self-commutators of Volterra operator and its square*, [DOI:10.5564/jasea.v3i1.2455](https://doi.org/10.5564/jasea.v3i1.2455).
- *Exact rank, inertia, and Schatten cancellation for opposing Volterra powers* (2026), [statement](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-exact-rank-inertia-and-schatten-cancellation-for-opposing-volter--498265e45420/RESULT.md).
