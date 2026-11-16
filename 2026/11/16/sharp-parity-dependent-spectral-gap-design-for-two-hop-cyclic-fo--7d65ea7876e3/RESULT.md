# Sharp parity-dependent spectral-gap design for two-hop cyclic Fourier differences

## Finding

A nonnegative fixed-budget combination of one-hop and two-hop shifts on a finite cycle admits an exact optimal design for the least singular gain on the mean-zero subspace of its difference operator. Its optimal weighting and its extremizing Fourier modes are different in odd and even cycle orders, and in large cycles the optimal lower gain approaches **twice** that of the one-hop difference.

Let \(n\ge3\), let \(S\) be the unitary cyclic shift on \(\mathbb C^n\), and, for \(0\le b\le1\), put
\[
L_b=I-(1-b)S-bS^2=(I-S)(I+bS),\qquad
\gamma_n(b)=\min_{u\perp\mathbf1,\ \|u\|_2=1}\|L_bu\|_2.
\]
The first component is constant, so its zero singular value is omitted. The following are exact global maxima over the **entire** allowed weighting interval, including the boundary.

**(i) The triangle.** For \(n=3\),
\[
\gamma_3(b)=\sqrt{3(1-b+b^2)},\quad
\max_{0\le b\le1}\gamma_3(b)=\sqrt3,
\]
with equality precisely at \(b=0\) and \(b=1\).

**(ii) Even cycles.** Let \(n\ge4\) be even and \(s=\sin(\pi/n)\). There is a unique optimal weighting,
\[
\boxed{b_n=(\sqrt{1+s^2}-s)^2},\qquad
\boxed{\max_b\gamma_n(b)=2(1-b_n)=4s(\sqrt{1+s^2}-s)}.
\]
The Fourier modes attaining the minimum at this parameter are exactly \(k=1\), \(k=n-1\), and \(k=n/2\).

**(iii) Odd cycles.** Let \(n\ge5\) be odd, let \(d=\cos(\pi/n)\), \(c=\cos(2\pi/n)\), and \(h=1+d-c\). There is a unique optimal weighting,
\[
\boxed{b_n=h-\sqrt{h^2-1}=\frac1{h+\sqrt{h^2-1}}},
\]
\[
\boxed{\max_b\gamma_n(b)=2\sqrt{b_n(1-c)(1+d)}}.
\]
The minimizing modes at this parameter are exactly \(k=1\), \(k=n-1\), \(k=(n-1)/2\), and \(k=(n+1)/2\).

For every \(n\ge4\), the optimal weight is strictly between zero and one. The one-hop design has \(\gamma_n(0)=2\sin(\pi/n)\), whereas, as \(n\to\infty\) along the corresponding parity classes,
\[
 b_n=\begin{cases}1-2\pi/n+O(n^{-2}),&n\text{ even},\\1-\sqrt3\pi/n+O(n^{-2}),&n\text{ odd},\end{cases}
 \qquad \max_b\gamma_n(b)=\frac{4\pi}{n}+O(n^{-2}).
\]
Thus the optimal improvement factor relative to a one-hop difference tends to \(2\) for both parities.

## Assumptions and scope

The graph signal space is \(\mathbb C^n\) with the ordinary Euclidean inner product, the cyclic shift is \((Su)_j=u_{j-1\;\mathrm{mod}\;n}\), and \(b\in[0,1]\) allocates the fixed unit total outgoing conductance between clockwise one-hop and two-hop edges. The difference operator is \(I-P_b\), where \(P_b=(1-b)S+bS^2\) is row/column stochastic. No negative weights or additional hops are allowed. The optimization concerns **least singular gain** on the mean-zero subspace, not the absolute second eigenvalue of \(P_b\), the largest singular value, or a condition number.

## Proof

Let \(\omega=e^{2\pi i/n}\). The normalized Fourier characters \(u^{(k)}_j=n^{-1/2}\omega^{jk}\) diagonalize the cyclic shift, hence the complete (possibly complex) eigenvalue and singular-value lists are
\[
\lambda_k(L_b)=(1-\omega^{-k})(1+b\omega^{-k}),\qquad
\sigma_k(L_b)=|1-\omega^k|\,|1+b\omega^k|,
\quad 0\le k<n.
\]
The only zero singular value is \(k=0\): for \(k\ne0\), the factor \(1-\omega^k\) does not vanish, and \(|1+b\omega^k|>0\) unless \(b=1\) and \(\omega^k=-1\). At this exceptional endpoint on an even cycle, \(b=1\) makes \(L_b=I-S^2\) and introduces a second zero singular value at \(k=n/2\). Accordingly the quantity \(\gamma_n(b)\) is defined over **all mean-zero modes**, and it vanishes at \(b=1\) for even cycles. It is the least gain, which may include zero singular values, rather than the smallest strictly positive singular value.

For \(x=\cos(2\pi k/n)\),
\[
\sigma_k(L_b)^2=2(1-x)(1+b^2+2bx)=:F_b(x).
\]
This is a concave quadratic in \(x\), with second derivative \(F_b''(x)=-8b\le0\). Among nonconstant modes the largest cosine is \(c=\cos(2\pi/n)\); the smallest is \(-1\) for even \(n\), and \(-d=-\cos(\pi/n)\) for odd \(n\). A concave function on this interval is at least the lesser of its two endpoint values. Consequently, the entire Fourier optimization reduces exactly to two competing endpoint-frequency gains:
\[
 A_n(b)=2\sin(\pi/n)\sqrt{1+b^2+2bc},\qquad
\gamma_n(b)=\min\{A_n(b),B_n(b)\},
\]
where
\[
 B_n(b)=\begin{cases}
2(1-b),&n\text{ even},\\
\sqrt{2(1+d)(1+b^2-2bd)},&n\text{ odd}.
\end{cases}
\]
For \(b>0\), strict concavity forces every other cosine strictly above the smaller endpoint value; this yields the exact minimizing-mode lists when the endpoints tie. At \(n=3\) the two extrema of the cosine set coincide, namely \(-1/2\), yielding the stated triangle formula and its two endpoint maximizers directly.

For even \(n\ge4\), \(c\ge0\) makes \(A_n\) strictly increasing on \([0,1]\), while \(B_n(b)=2(1-b)\) is strictly decreasing. We have \(A_n(0)<B_n(0)\) and \(B_n(1)<A_n(1)\); there is a unique crossing and the minimum increases before, then decreases after it. Setting \(s=\sin(\pi/n)\) and \(t=\sqrt b\), the condition \(A_n(b)=2(1-b)\) is equivalent to
\[
s^2\big((1+b)^2-4bs^2\big)=(1-b)^2.
\]
The crossing is exactly the unique solution \(t^2+2st=1\) in \((0,1)\), namely \(t=\sqrt{1+s^2}-s\). To verify this equivalence for that root, the latter identity gives \(1-b=2st\) and \(1+b=2t\sqrt{1+s^2}\), hence the displayed crossing equation; uniqueness follows from monotonicity. This proves the claimed optimal value and equality modes.

For odd \(n\ge5\), \(c>0\), \(d>\tfrac14\), and \(c+d>0\). The first endpoint gain \(A_n(b)\) increases strictly, whereas \(B_n(b)\) decreases on \([0,d]\) and increases on \([d,1]\). Their squared difference factors as
\[
A_n(b)^2-B_n(b)^2
=2(c+d)\big(2hb-(1+b^2)\big),\qquad h=1+d-c>1.
\]
At \(b=0\) it is negative, while at \(b=d\) it is positive, because
\[
2hd-(1+d^2)=(1-d)(4d-1)(1+d)>0.
\]
The unique crossing in \([0,d]\) is the smaller positive root of \(b^2-2hb+1=0\), which is \(b_n=h-\sqrt{h^2-1}\). On \([0,b_n]\) the minimum equals strictly increasing \(A_n\); on \([b_n,d]\) it equals strictly decreasing \(B_n\). Finally for \(d\le b\le1\),
\[
B_n(b)\le B_n(1)=2\sin(\pi/n)=A_n(0)<A_n(b_n),
\]
so no later point can match the maximum. At the crossing, equating the two endpoints and using \(1+b_n^2=2hb_n\) gives
\[
A_n(b_n)^2=4b_n(1-c)(1+d),
\]
as asserted. Strict concavity excludes all other minimizing modes.

The asymptotics use \(\sin(\pi/n)=\pi/n+O(n^{-3})\), \(d=1-\pi^2/(2n^2)+O(n^{-4})\), and \(c=1-2\pi^2/n^2+O(n^{-4})\). In the odd case \(h=1+3\pi^2/(2n^2)+O(n^{-4})\), yielding the stated \(b_n\) expansion. In both cases the optimal low-frequency gain is \(4\pi/n+O(n^{-2})\), whereas the one-hop gap is \(2\pi/n+O(n^{-3})\). All quantifiers, endpoints, and parity restrictions have thus been proved.

## Verification

An independent finite-matrix calculation is provided in `check.py`. It constructs cyclic shift matrices and obtains singular values from dense SVD for every integer \(3\le n\le100\), compares the analytic optimum and all two-endpoint Fourier values across a 201-point weight grid, and makes additional off-optimum comparisons. It reports 392 passed assertions. These finite numerical checks are diagnostic only; the theorem, uniqueness, and limits rest on the exact proof above.

To run: `python check.py` with Python 3 and NumPy installed. The sign convention of the shift changes Fourier eigenvalue conjugations but never its singular values.

## Relationship to prior work

Emirov, Cheng, Jiang, and Sun introduce polynomial graph filters of multiple shifts and distributed inversion (first preprint March 24, 2020). Chen, Cheng, and Sun explicitly diagonalize Laplacians of directed circulant graphs and identify their singular-value Fourier multipliers (first preprint May 12, 2022); their general symbol calculus supports the first step of our proof. Neither inspected article provides the fixed-budget two-hop maximin design, its sharp odd/even weighting formulas, or its full minimizing-mode equality classification. Segarra, Marques, and Ribeiro study optimal graph-filter coefficients for approximating prescribed linear operators; that is a different objective and leaves a risk of a related specialization. The finite-cycle optimality statement is not presented as a general theorem about arbitrary graph filters or arbitrary directed graph spectral gaps.

## Limitations

The result is confined to two nonnegative consecutive shifts, total weight exactly one, and cyclic Euclidean Fourier analysis. It does not optimize a graph Markov mixing rate or Laplacian's positive eigenvalue real parts. The fact that general circulant matrices are Fourier-diagonalizable is prior art, not part of the asserted originality. The presented closed-form global optimization and equality modes may have appeared as a specialization of earlier generic trigonometric minimax results; historical priority is not independently certified. The finite checker does not certify the infinitely many cycle sizes.

## References

1. N. Emirov, C. Cheng, J. Jiang and Q. Sun, *Polynomial graph filter of multiple shifts and distributed implementation of inverse filtering*, arXiv:2003.11152, version 1 submitted 2020-03-24. https://arxiv.org/abs/2003.11152
2. Y. Chen, C. Cheng and Q. Sun, *Graph Fourier transform based on singular value decomposition of directed Laplacian*, arXiv:2205.06242, version 1 submitted 2022-05-12, especially Section II and Appendix A. https://arxiv.org/html/2205.06242v1
3. S. Segarra, A. G. Marques and A. Ribeiro, *Optimal Graph-Filter Design and Applications to Distributed Linear Network Operators*, IEEE Transactions on Signal Processing (2017), author manuscript: https://tsc.urjc.es/~amarques/papers/ssamar_tsp17.pdf
