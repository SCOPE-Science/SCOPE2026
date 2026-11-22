# Exact sharp third-moment amplification and sixfold optimizer rigidity on the six-cycle

## Finding

Equip \(C_6=\mathbb Z/6\mathbb Z\) with uniform probability and define the word-length Fourier form \(\mathcal E_{\mathrm w}(f)=\sum_{k=0}^{5}\min(k,6-k)|\widehat f(k)|^2\). For every **real mean-zero** function \(f:C_6\to\mathbb R\), set \(s=\langle f^2\rangle\) and \(T=\mathcal E_{\mathrm w}(f)-s\). Then \(T\ge0\) and the following inequality has the **best possible constant**:

\[
|\langle f^3\rangle|\le K_6\,s\sqrt T,
\quad K_6=\frac{3z_*+8+\sqrt{81z_*^2+168z_*+16}}{2(z_*+2)\sqrt{2(z_*+1)}},
\]
where \(z_*\in(0,1)\) is the unique root in that interval of
\[
243z^4-225z^3-1800z^2-912z+704=0.
\]
Numerically, \(z_*=0.417702187780093\ldots\), \(K_6=2.366495837333408\ldots\), and \(K_6^2=5.600302548116345\ldots\). Thus the sharp squared coefficient improves the published bound \(59/10=5.9\) for the same six-cycle problem.

All nonzero equality cases with \(T>0\) form exactly the six translates, their nonzero real scalar multiples, and their sign reversals of the real profile
\[
F(x)=2t_*\cos(2\pi x/6)+2\cos(4\pi x/6)+r_* (-1)^x,
\]
where \(r_*=\sqrt{z_*}\),
\[
\lambda_* =\frac{3z_*+8+\sqrt{81z_*^2+168z_*+16}}{2(z_*+2)},
\qquad t_* =\frac{3r_*}{\lambda_*-3}.
\]
Here \(r_*=0.646298837829756\ldots\) and \(t_*=1.968699378731684\ldots\). Trivial equality also holds when \(T=0\), because then \(\langle f^3\rangle=0\).

## Assumptions and scope

For \(k\in C_6\) let \(\chi_k(x)=e^{2\pi ikx/6}\), and let \(\widehat f(k)=\langle f\overline{\chi_k}\rangle\). The normalization of \(\mathcal E_{\mathrm w}\) gives the first nonzero harmonic eigenvalue \(1\). Mean zero means \(\widehat f(0)=0\). Neither \(f\ge0\) nor a norm-one assumption is imposed. The claim concerns the whole five-dimensional real mean-zero space, not a band-limited subclass, and its sharp constant is not asserted for other cyclic orders or alternative Laplacians.

## Proof

**Step 1: exact resonances.** Every such function has the unique representation
\[
f=a\chi_1+\overline a\chi_{-1}+b\chi_2+\overline b\chi_{-2}+c\chi_3,
\quad a,b\in\mathbb C,\ c\in\mathbb R.
\]
Put \(A=|a|, B=|b|, C=|c|\). Orthogonality yields
\[
s=2A^2+2B^2+C^2,\qquad T=2B^2+2C^2.
\]
The complete list of zero-sum frequency triples modulo six is \((1,1,-2)\) and conjugate, \((2,2,2)\) and conjugate, and \((1,2,3)\) and conjugate, including permutations. Hence
\[
\langle f^3\rangle=6\operatorname{Re}(a^2\overline b)+2\operatorname{Re}(b^3)+12c\operatorname{Re}(ab),
\]
and consequently
\[
|\langle f^3\rangle|\le 6A^2B+2B^3+12ABC.
\tag{1}
\]
For \(A,B,C>0\), equality in (1) is attained by compatible phases (for example all three Fourier coefficients real positive), so no relaxation occurs.

**Step 2: the two-dimensional Rayleigh reduction.** If \(B=0\), then the cubic moment vanishes. If \(B>0\), scale so \(B=1\), put \(r=C/B\ge0\) and \(z=r^2\). For fixed \(r\), the ratio of the right side of (1) to \(s\sqrt T\) is
\[
\frac{6A^2+12rA+2}{(2A^2+2+r^2)\sqrt{2(1+r^2)}}.
\]
The fraction before the final square root is the generalized Rayleigh quotient of
\[
\begin{pmatrix}6&6r\\6r&2\end{pmatrix}
\quad\text{against}\quad
\begin{pmatrix}2&0\\0&2+r^2\end{pmatrix}.
\]
For \(r>0\) its maximum over \(A\ge0\) is the larger generalized eigenvalue, because the top eigenvector is strictly positive. It equals
\[
\lambda(z)=\frac{3z+8+\sqrt{81z^2+168z+16}}{2(z+2)}.
\]
Thus the exact remaining one-dimensional objective is
\[
H(z)=\frac{3z+8+\sqrt{81z^2+168z+16}}{2(z+2)\sqrt{2(z+1)}}.
\tag{2}
\]
At the maximizing \(z>0\), eigenvector equations give the unique amplitude ratio \(A/B=3\sqrt z/(\lambda(z)-3)\).

**Step 3: prove the global maximum of (2).** Let \(R(z)=81z^2+168z+16\) and
\[
D(z)=(-81z^3-174z^2+108z+272)-(3z^2+18z+20)\sqrt{R(z)}.
\]
Direct differentiation shows \(\operatorname{sgn} H'(z)=\operatorname{sgn}D(z)\). Squaring the equation \(D(z)=0\) yields the exact polynomial identity
\[
(-81z^3-174z^2+108z+272)^2-(3z^2+18z+20)^2R(z)
=24(z+2)^2Q(z),
\]
where \(Q(z)=243z^4-225z^3-1800z^2-912z+704\). By Descartes' rule of signs, \(Q\) has at most two positive zeros, counted with multiplicity. Its signs at \(0,1,3,4\) are respectively positive, negative, negative, positive; thus it has exactly two positive roots, one in \((0,1)\) and one in \((3,4)\). Now \(D(0)=192>0\) and \(D(1)<0\). Since a root of \(D\) must be a root of \(Q\), exactly the root \(z_*\in(0,1)\) is a critical point on \((0,2)\). For \(z\ge2\), the polynomial \(-81z^3-174z^2+108z+272\) is strictly negative and decreasing, so \(D(z)<0\). Thus \(H\) increases until \(z_*\) and decreases thereafter. Its global maximum is \(H(z_*)=K_6\). The boundaries \(z=0\) and \(z\to\infty\) give \(3/\sqrt2\) and \(0\), both strictly below \(K_6\).

**Step 4: classify equality.** The strict interior optimum forces \(A,B,C>0\) and unique ratios \(B:C:A=1:r_*:t_*\). If the cubic moment is positive, equality in the three triangle inequalities in (1) requires, writing \(a=Ae^{i\alpha},b=Be^{i\beta},c=\varepsilon C\) with \(\varepsilon=\pm1\),
\[
2\alpha-\beta\equiv0,\quad3\beta\equiv0,\quad\varepsilon e^{i(\alpha+\beta)}=1.
\]
These imply exactly \(\alpha=\pi j/3,\beta=2\pi j/3,\varepsilon=(-1)^j\) for \(j=0,\ldots,5\), i.e. precisely the six translates of \(F\). Negating \(f\) gives every negative-cubic equality case. Multiplying by a positive scalar preserves equality. Conversely these profiles meet all bounds with equality. If \(T=0\), then \(b=c=0\) and the cubic moment is zero.

## Verification

The standalone file `checker.py` verifies the exact derivative-elimination identity, rational sign brackets and the two-positive-root certificate, evaluates the positive optimizer, and independently compares the complete six-point Fourier cubic with the three-resonance expression for 4,000 deterministic random coefficient triples. It also verifies all twelve signed translates of the maximizing profile. A direct execution reported 16,020 passed assertions. Finite tests are supplementary to the symbolic identities and the global argument above; they do not establish the universal inequality by enumeration.

## Relationship to prior work

Xie and Zhang (2026) proved the uniform nonsharp cubic estimate with squared constant \(9\) for word-length energies on finite cycles. Chen, Lam and Lu (2026), Section 6.1, improve to \(383/64\) for orders at least six and derive \(59/10\) specifically for the six-cycle from their inequality (6.4). In their proof of the six-cycle case they list the same three resonance families and construct a nonoptimal sum-of-squares upper certificate; they do not optimize the resulting homogeneous quotient or classify its extremizers. The present theorem resolves the sharp six-cycle constant and all equality cases, without asserting an improvement to their log-Sobolev stability inequality. Work on sixth-power Fourier norms addresses \(\langle |f|^6\rangle\), not the real cubic functional weighted by excess word-length energy.

## Limitations

No result is asserted for longer cycles, the nearest-neighbor energy, or sharp log-Sobolev constants. The exact constant is algebraic but only its defining quartic/radical form is needed. This scientific review does not establish global bibliographic priority; an independently published equivalent optimization may exist. Independent mathematical audit has not been performed.

## References

- X. Xie and H. Zhang, *Sharp Log-Sobolev Inequalities for Finite Cyclic Groups with Word-Length*, arXiv:2606.02847v1 (first public June 1, 2026), https://arxiv.org/abs/2606.02847 .
- L. Chen, N. Lam and G. Lu, *Sharp uniform stability of the logarithmic Sobolev inequality on finite cycles and stability of the cubic Sobolev inequality*, arXiv:2610.05347v1 (first public October 4, 2026), Section 6.1, particularly the six-cycle calculation and inequality (6.4), https://arxiv.org/html/2610.05347v1 .
