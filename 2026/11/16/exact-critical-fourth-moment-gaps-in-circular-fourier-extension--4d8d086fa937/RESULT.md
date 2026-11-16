# Exact critical fourth-moment gaps in circular Fourier extension

## Finding

For each integer \(k\geq0\) and real \(q>4\), let \(J_k\) be the Bessel function of the first kind and set
\[
I_k(q)=\int_0^\infty |J_k(r)|^q\,r\,dr.
\]
For **every pair of fixed integers** \(0\leq m<n\), the separately divergent fourth moments have the exact, positive renormalized difference
\[
\boxed{\lim_{q\downarrow4}\bigl(I_m(q)-I_n(q)\bigr)
=\frac{2}{\pi^2}\sum_{j=m+1}^{n}\frac{1}{2j-1}.}\tag{1}
\]
Indeed, for each fixed \(k\),
\[
I_k(q)=\frac{3}{\pi^2(q-4)}+O_k(1),\qquad q\downarrow4,\tag{2}
\]
and hence the **squared-mode norm gaps** have the sharp endpoint law
\[
\boxed{\lim_{q\downarrow4}\frac{I_m(q)^{2/q}-I_n(q)^{2/q}}{\sqrt{q-4}}
=\frac{1}{\pi\sqrt3}\sum_{j=m+1}^{n}\frac{1}{2j-1}.}\tag{3}
\]
In particular the adjacent renormalized gaps are exactly \(2/[\pi^2(2j-1)]\) and are all strictly positive.

## Assumptions and scope

The inequalities are for ordinary Bessel functions with *integer* index, one radial variable, and the unweighted radial measure \(r\,dr\), corresponding to Fourier extension from \(\mathbb S^1\) with surface measure and Fourier phase \(e^{-ix\cdot\omega}\). The order indices \(m,n\) remain fixed as \(q\downarrow4\). Formula (3) uses the canonical mode coefficients \(I_k(q)^{2/q}\), not an independently optimized global stability constant. Both terms in (1) diverge if \(q=4\) is substituted before subtraction; the correct definition is the limit of their difference from \(q>4\).

## Proof

**1. Removing the common divergent tail.** For every fixed nonnegative integer \(k\), the classical Hankel expansion gives, uniformly for \(q\in[4,5]\) and \(r\geq1\),
\[
|J_k(r)|^q=\left(\frac2{\pi r}\right)^{q/2}
\left|\cos\left(r-\frac{k\pi}{2}-\frac\pi4\right)\right|^q+O_k(r^{-q/2-1}).\tag{4}
\]
The periodic cosine factor has mean \(M(q)=\Gamma((q+1)/2)/[\sqrt\pi\,\Gamma((q+2)/2)]\). Its mean-zero part has a uniformly bounded primitive for \(q\in[4,5]\). Integration by parts therefore gives an \(O_k(1)\) correction to the averaged tail, uniformly as \(q\downarrow4\); with \(M(4)=3/8\), the mean tail yields (2). For consecutive orders \(j-1,j\), the phases in (4) differ by \(\pi/2\), so the *leading difference* of periodic factors has mean zero for every \(q\in[4,5]\). Its integral against \(r^{1-q/2}\) converges uniformly on the full interval, with a tail bounded by \(O_j(R^{-1})\) for lower cutoff \(R\geq1\). The remainders are uniformly absolutely integrable. Consequently,
\[
\lim_{q\downarrow4}[I_{j-1}(q)-I_j(q)]
=\lim_{R\to\infty}\int_0^R r[J_{j-1}(r)^4-J_j(r)^4]dr.\tag{5}
\]
The right-hand integral is conditionally convergent in general; no absolute-convergence assertion is used.

**2. Exact Bessel recurrence reduction.** Put \(x(r)=J_{j-1}(r)\) and \(y(r)=J_j(r)\). The standard recurrences say \(x'=(j-1)x/r-y\) and \(y'=x-jy/r\), whence
\[
(rxy)'=r(x^2-y^2),\qquad (x^2+y^2)'=\frac2r[(j-1)x^2-jy^2].\tag{6}
\]
Integrate \(r(x^4-y^4)=(rxy)'(x^2+y^2)\) on \([0,R]\), then integrate by parts. Bessel small-argument series and fixed-order large-argument decay imply all boundary terms vanish at the relevant endpoints; when \(j=1\), the possible \(J_0(0)\) contribution is multiplied by \(j-1=0\). The identities \(y'=x-jy/r\) and \(x'=(j-1)x/r-y\) then give
\[
\lim_{q\downarrow4}[I_{j-1}(q)-I_j(q)]
=2\left[j^2 T_j-(j-1)^2T_{j-1}\right],\quad
T_j:=\int_0^\infty\frac{J_j(r)^4}{r}\,dr.\tag{7}
\]
Here \(T_j\) is absolutely convergent for every \(j\geq1\); the \(T_0\) term is assigned coefficient zero and is never evaluated.

**3. Exact fourth-power integral.** For every integer \(j\geq1\), the standard Neumann product identity reads
\[
J_j(r)^2=\frac2\pi\int_0^{\pi/2}J_0(2r\sin\theta)\cos(2j\theta)\,d\theta.\tag{8}
\]
The Frullani–Bessel identity and the angular-mean logarithmic potential identity imply that the *regularized* radial cross-kernel has the form
\[
\int_0^\infty\frac{J_0(ar)J_0(br)-\chi(r)}r\,dr
=C_\chi-\log\max\{a,b\},\tag{9}
\]
where \(a,b>0\), \(\chi\) is any fixed admissible near-zero subtraction, and \(C_\chi\) is independent of \(a,b\). This follows directly by averaging \(J_0(r|a-be^{it}|)\) over the angle and using \(\int_0^\infty[J_0(ur)-J_0(vr)]dr/r=\log(v/u)\). Endpoint values \(a=0\) or \(b=0\) follow by limits. Use (8) twice, insert an exponential radial cutoff if desired, and cancel the constant in (9) because \(\int_0^{\pi/2}\cos(2j\theta)d\theta=0\). Passing to the limit is justified by the integrable logarithmic angular kernel. With symmetry in \(\theta,\phi\), this gives
\[
T_j=-\frac2{j\pi^2}\int_0^{\pi/2}\sin(4j\theta)\log(\sin\theta)\,d\theta.\tag{10}
\]
Integration by parts, with the primitive \([1-\cos(4j\theta)]/(4j)\), gives
\[
-\int_0^{\pi/2}\sin(4j\theta)\log(\sin\theta)\,d\theta
=\frac{1}{2j}\sum_{\ell=1}^j\frac1{2\ell-1}.\tag{11}
\]
For (11), equivalently evaluate \(\int_0^{\pi/2}[1-\cos(4j\theta)]\cot\theta\,d\theta\) by the trigonometric telescoping identity, adding \(2/(2j-1)\) when \(j\) increases by one. Thus the exact absolutely convergent integral is
\[
\boxed{T_j=\frac{1}{j^2\pi^2}\sum_{\ell=1}^j\frac1{2\ell-1}.}\tag{12}
\]
Substituting (12) into (7) telescopes to \(2/[\pi^2(2j-1)]\). Summing adjacent gaps over \(m<j\leq n\) proves (1).

**4. Squared-mode asymptotic.** Since (2) holds with the same leading constant for both fixed indices and their difference tends to the finite value (1), the mean-value theorem applied to \(u\mapsto u^{2/q}\) yields
\[
I_m(q)^{2/q}-I_n(q)^{2/q}
=\left(\frac12+o(1)\right)\left(\frac{\pi^2(q-4)}3\right)^{1/2}
[I_m(q)-I_n(q)].
\]
This proves (3), with the stated exact coefficient.

## Verification

A standalone checker in `CHECK.py` evaluates the independent convergent integrals in (12), the finite-cutoff oscillatory differences in (5), and the trigonometric integral in (10), comparing with exact odd-harmonic rational sums. It uses SciPy quadrature and checks several orders and cutoffs. These finite comparisons check normalizations and boundary signs, but the infinite-parameter claims follow from the analytic steps above, not from numerical enumeration.

## Relationship to prior work

The original mixed-norm modal reduction and critical range are in Carneiro, Oliveira e Silva, and Sousa (2019), with an initial arXiv version publicly released in October 2017. Ciccone and Sousa (2025) prove qualitative modal inequalities in selected ranges. Xu (2026), first posted October 14, proves strict zeroth-mode dominance for every \(q>4\), partial adjacent ordering on the circle and sharp finite-exponent stability. Section 3.2 of that work explicitly treats the shared divergent \(q=4\) tail as an obstruction. The result here concerns a different quantitative endpoint question: *exact finite differences* after that common pole cancels, and their explicit odd-harmonic dependence on arbitrary fixed indices. Standard Bessel recurrences, Neumann products, and the Frullani identity are used as classical tools, not claimed to be new. No assertion is made that absence of a matching phrase in a search proves global publication priority.

## Limitations

The indices must be fixed before \(q\downarrow4\); no uniformity in increasing harmonic degree is proved. Each raw moment diverges at \(q=4\), and (1) is an ordered limiting difference, not an ordinary difference of two infinite numbers. Formula (3) compares two *pure-mode* squared coefficients and does not identify the globally second-largest mode or the optimal global stability constant on \(\mathbb S^1\). Publication-priority comparison with older integral tables under unrelated indexing remains a risk; the fourth-power integral identity itself may also have classical representations.

## References

1. Z. Xu, *Sharp radial--angular mixed norm Fourier extension and global stability on spheres*, arXiv:2610.19648 (first posted 2026-10-14), especially Sections 1, 3.2, 4 and 6.
2. E. Carneiro, D. Oliveira e Silva, M. Sousa, *Sharp mixed norm spherical restriction*, Advances in Mathematics 341 (2019), 583--608; arXiv:1710.10365 (first posted 2017-10-28).
3. V. Ciccone, M. Sousa, *Global and local maximizers for some Fourier extension estimates on the sphere*, Journal of Fourier Analysis and Applications 31 (2025), article 70; arXiv:2312.07309 (first posted 2023-12-12).
4. F. W. J. Olver et al. (eds.), NIST Digital Library of Mathematical Functions, Sections 10.6, 10.9, 10.17, 10.22 (standard Bessel recurrence, product, asymptotic and integral identities).
