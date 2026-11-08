# Exact counting law and thin-annulus scaling for monomial self-commutators

## Finding

The positive self-commutator of a monomial multiplier on a Hardy annulus has an exact hyperbolic-cosine eigenvalue profile. Its spectral counting function differs from a closed-form continuous profile by **at most one eigenvalue**, uniformly in the power and annulus width. Consequently all Schatten moments obey an explicit, uniform, finite-size estimate, even when the power grows inversely to the annulus thickness.

Specifically, fix \(0<r<1\) and an integer \(k\ge1\). Put \(b=-\log r>0\), \(a=kb\), and
\[
q=e^{-2a},\qquad c_a=(1-e^{-a})^2,\qquad L_a=\frac{(1-e^{-2a})^2}{2e^{-a}}.
\]
For the positive operator \(D_{r,k}=[M_{z^k}^{*},M_{z^k}]\) defined below, the complete nonzero point spectrum, with multiplicities indexed by \(n\in\mathbb Z\), is
\[
\lambda_{n,k}=\frac{(1-r^{2k})^2}{(1+r^{2n})(1+r^{2(k-n)})}
=\frac{L_a}{\cosh a+\cosh(b(2n-k))}.
\]
All these eigenvalues are strictly positive, tend to zero at both ends of the index set, and comprise the full positive spectrum. The operator belongs to \(\mathcal S_p\) for every \(p>0\), including quasi-Schatten classes.

For \(0<t<c_a\), define
\[
A_a(t)=\operatorname{arcosh}\!\left(\frac{L_a}{t}-\cosh a\right),
\quad N_{r,k}(t)=\#\{n\in\mathbb Z:\lambda_{n,k}>t\}.
\]
Then the following **uniform spectral-counting estimate** is exact up to lattice rounding:
\[
N_{r,k}(t)=\#\big\{n\in\mathbb Z:|2n-k|<A_a(t)/b\big\},
\qquad \left|N_{r,k}(t)-\frac{k}{a}A_a(t)\right|\le1.
\]
For \(t\ge c_a\), \(N_{r,k}(t)=0\). The estimate applies for every \(r,k\), not just in an asymptotic regime.

For any \(p>0\), put
\[
W_p(a)=\frac{p}{a}\int_0^{c_a} t^{p-1}A_a(t)\,dt.
\]
This is finite and positive, and satisfies
\[
\boxed{\left|\operatorname{Tr}(D_{r,k}^{p})-kW_p(a)\right|\le c_a^{p}.}
\]
The first two continuous moments are
\[
W_1(a)=1-e^{-2a},\qquad
W_2(a)=1-e^{-4a}-\frac{(1-e^{-2a})^2}{a}.
\]
In fact \(\operatorname{Tr}D_{r,k}=k(1-r^{2k})\) holds without error. Thus, when \(r_k=e^{-a/k}\) with fixed \(a>0\),
\[
\frac1k N_{r_k,k}(t)\longrightarrow\frac{A_a(t)}{a}\quad(0<t<c_a),
\qquad
k^{-1/p}\|D_{r_k,k}\|_{\mathcal S_p}\longrightarrow W_p(a)^{1/p},
\]
with counting discrepancy at most \(1/k\) and moment discrepancy at most \(c_a^p/k\).

The **finite-power top eigenvalue** has a parity effect:
\[
\|D_{r,k}\|=
\begin{cases}
(1-r^{k})^{2},& k\text{ even},\\[3pt]
\dfrac{(1-r^{2k})^{2}}{(1+r^{k-1})(1+r^{k+1})},& k\text{ odd}.
\end{cases}
\]
For even \(k\) the top eigenvalue is simple; for odd \(k\) it has multiplicity two.

## Assumptions and scope

The complex Hardy space on the annulus \(\mathbb A_r=\{z:r<|z|<1\}\) is the completion of Laurent polynomials in the norm
\[
\left\|\sum_{n\in\mathbb Z}a_nz^n\right\|_{H_r}^{2}
=\sum_{n\in\mathbb Z}(1+r^{2n})|a_n|^2.
\]
This is the equal-normalized-boundary-weight convention. Write \(M_{z^k}f(z)=z^kf(z)\). The commutator notation is \([T^*,T]=T^*T-TT^*\); no claim concerns the opposite sign. The integer power \(k\ge1\), width \(0<r<1\), parameter \(a=k(-\log r)>0\), Schatten exponent \(p>0\), and spectral threshold \(t>0\) are arbitrary in the indicated ranges. The normalized counting limit is only asserted for thresholds strictly inside \((0,c_a)\).

## Proof

**Step 1: exact diagonalization.** The Laurent monomials \(e_n(z)=z^n/(1+r^{2n})^{1/2}\), for \(n\in\mathbb Z\), form an orthonormal basis. Multiplication acts by the \(k\)-step bilateral shift
\[
M_{z^k}e_n=w_ne_{n+k},\qquad
w_n^2=\frac{1+r^{2(n+k)}}{1+r^{2n}}.
\]
Consequently \(D_{r,k}e_n=(w_n^2-w_{n-k}^2)e_n\). Setting \(x=r^{2n}\), \(q=r^{2k}\), direct factorization yields
\[
\begin{aligned}
w_n^2-w_{n-k}^2
&=\frac{1+qx}{1+x}-\frac{q(1+x)}{q+x}\\
&=\frac{(1-q)^2x}{(1+x)(q+x)}
=\frac{(1-r^{2k})^2}{(1+r^{2n})(1+r^{2(k-n)})}.
\end{aligned}
\]
This proves positivity. As \(n\to\pm\infty\), the diagonal entries decay geometrically, proving membership in every \(\mathcal S_p\). Multiplying numerator and denominator by the suitable exponential factor gives the stated hyperbolic-cosine expression. The only other spectral point is the accumulation point \(0\), which is not an eigenvalue.

**Step 2: top eigenvalue and multiplicity.** The denominator \(\cosh a+\cosh(b(2n-k))\) is minimized at the integers closest to \(k/2\). If \(k\) is even, this is \(n=k/2\); otherwise it is the two indices \(n=(k\pm1)/2\). Substitution proves both parity formulas and multiplicities.

**Step 3: lattice counting.** For \(0<t<c_a\), solving \(\lambda_{n,k}>t\) gives \(|2n-k|<A_a(t)/b\). The admissible integers lie in an open interval of length \(A_a(t)/b=(k/a)A_a(t)\). An open interval of real length \(\ell\) contains a number of integers differing from \(\ell\) by at most one. This proves the uniform counting estimate, including possible threshold equality. Because \(\lambda_{n,k}\le c_a\) for every index, larger thresholds have no eigenvalues.

**Step 4: uniform Schatten moments.** For any positive summable diagonal sequence in \(\ell^p\), layer cake gives
\[
\operatorname{Tr}(D_{r,k}^p)
=p\int_0^{c_a} t^{p-1}N_{r,k}(t)\,dt.
\]
The continuous comparison is \(kW_p(a)\). Taking the absolute difference under the integral and using the unit counting bound yields \(p\int_0^{c_a}t^{p-1}dt=c_a^p\). Finiteness at \(t=0\) follows because \(A_a(t)=O(1+|\log t|)\).

**Step 5: exact and limiting moments.** The telescoping sum \(\sum_{n\in\mathbb Z}(w_n^2-w_{n-k}^2)=k(1-q)\) follows by finite symmetric truncation, using \(w_n^2\to q\) at \(-\infty\) and \(w_n^2\to1\) at \(+\infty\). For any fixed \(a>0\), taking \(k\to\infty\) with \(r=e^{-a/k}\) in the uniform moment inequality yields \(W_1(a)=1-q\). Alternatively the comparison density is
\[
F_a(s)=\frac{(1-q)^2}{(1+e^{-2as})(1+e^{-2a(1-s)})},
\qquad W_p(a)=\int_{\mathbb R}F_a(s)^p\,ds.
\]
Substituting \(y=e^{-2as}\) gives
\[
W_2(a)=\frac{(1-q)^4}{2a}
\int_0^\infty\frac{y}{(1+y)^2(q+y)^2}\,dy
=1-q^2-\frac{(1-q)^2}{a},
\]
using \(\log q=-2a\). For \(r_k=e^{-a/k}\), the counting and Schatten limits follow immediately from the uniform finite-size estimates. No assumption of uniformity in the degree is imported from a fixed-symbol theorem.

## Verification

The included `checker.py` uses exact rational arithmetic to verify the diagonalization, reflection symmetry, positivity, top-eigenvalue parity, and finite telescoping identities over several rational annuli and powers. It separately checks level-counting at explicitly specified real parameters and numerically integrates the two closed continuous moments. The script reports `ANNULUS_MONOMIAL_SPECTRAL_CHECKS_OK 2508` in the executed check. These finite checks are not substitutes for Steps 1–5, which prove all quantified assertions.

## Relationship to prior work

Jain and Sarkar (2026) establish Brown–Halmos-type algebraic characterizations of Toeplitz operators and compact Toeplitz perturbations on the equal-boundary-weight Hardy annulus. Their paper supplies the same orthonormal Laurent basis but does not state this all-power commutator counting law or the simultaneous thin-annulus/large-power scaling.

Douglas and Kim (2009) analyze reducing subspaces of monomial multipliers on Hardy and Bergman annuli, including decomposition into residue classes modulo the power; their classification does not give the spectral counting function or the uniform Schatten estimates stated here. Classical trace identities for cyclic subnormal operators inform the trace calculation; only the explicit counting-and-scaling package is advanced here as a best-knowledge addition.

## Limitations

The theorem is restricted to scalar monomial multipliers and equal-normalized-boundary Hardy norms. It does not classify general Laurent-polynomial symbols or arbitrary multiply connected domains. Known weight formulas, positive self-commutators, and qualitative trace-class facts are not claimed as new. The uniform eigenvalue-counting estimate is elementary once this model is diagonalized; the substantive claim is its global all-power sharp formula together with the width-power crossover, all-Schatten moment control, and exact finite-size discrepancy. Older equivalent spectral formulations may exist. No independent audit or exhaustive publication-priority certification is claimed.

## References

1. S. Jain and J. Sarkar, *Characterizations of Toeplitz operators on the annulus*, arXiv:2610.40118v1 (first posted 2026-10-29), https://arxiv.org/html/2610.40118v1.
2. R. G. Douglas and Y.-S. Kim, *Reducing Subspaces on the Annulus*, arXiv:0902.1794 (first posted 2009-02-11), https://arxiv.org/abs/0902.1794.
3. N. S. Feldman, *The Self-Commutator of a Subnormal Operator*, public summary of trace and compactness results, https://feldman.academic.wlu.edu/papers/the-self-commutator-of-a-subnormal-operator/.
