# Exact smallest singular values for rank-two convolution on finite matrix spaces

## Finding
Let \(q\ge2\) be a prime power, and let \(2\le m\le n\) be integers. On the additive group \(X=M_{m,n}(\mathbb F_q)\), equip complex functions with counting-measure \(\ell^2\), and define
\[
(T_2f)(A)=\sum_{\substack{B\in X\\\operatorname{rank}B=2}}f(A+B).
\]
The operator is invertible for all these parameters. Its largest singular value equals its degree
\[
V=\binom{m}{2}_q(q^n-1)(q^n-q),
\]
where the bracket is the Gaussian binomial coefficient. Define \(C=q\binom{m}{2}_q\). Except for the binary square matrix space with \(m=n\ge3\), the least singular value and condition number are exactly
\[
\sigma_{\min}(T_2)=C,\qquad
\kappa_2(T_2)=\frac{(q^n-1)(q^n-q)}q.
\]
The least-stable Fourier sector has frequency rank \(m\) and is unique, except that for \((q,m,n)=(2,2,2)\), ranks \(m\) and \(m-1\) tie. For \(q=2\) and \(n=m\ge3\), put \(u=2^{m-1}\). Then
\[
\sigma_{\min}(T_2)=\frac23|u^2-6u-1|,\qquad
\kappa_2(T_2)=\frac{(2u-1)^2(u-1)^2}{|u^2-6u-1|}.
\]
In this exceptional family the unique least-stable Fourier sector has rank \(m-2\), not full rank. Thus the exact optimizer switches harmonic sectors at the binary square boundary. No zero eigenvalues occur.

## Assumptions and scope
The prime-power field can have any characteristic; no primality of \(q\) is assumed in the theorem. The convolution uses the indicator of **all** rank-two matrices and is unnormalized. For any \(0\le t\le m\), additive Fourier characters of matrix frequency rank \(t\) have multiplicity
\[
N_t=\binom mt_q\prod_{i=0}^{t-1}(q^n-q^i).
\]
The empty product equals one. The original rank-metric association-scheme eigenvalue formula is an established result of Delsarte; the new assertion here is the globally optimized *least absolute* eigenvalue, the sharp condition number and exceptional optimizing sector.

## Proof
Write \([a]_q=(q^a-1)/(q-1)\) and use \(\binom ab_q\) for Gaussian coefficients, defined as zero outside \(0\le b\le a\). Fix any nontrivial additive character \(\psi\) of \(\mathbb F_q\). For each \(Y\in X\), the function \(\chi_Y(A)=\psi(\operatorname{tr}(YA^{\mathsf T}))\) is a Fourier character. These characters form an orthogonal basis of \(\ell^2(X)\); inversion of \(B\mapsto-B\) preserves matrix rank, so \(T_2\) is self-adjoint. By the bilinear-forms association-scheme character table (Delsarte, Theorem A2), the eigenvalue on rank-\(t\) characters depends only on \(k=m-t\) and is
\[
\lambda(k)=C-B[k]_q+q^{2n}\binom{k}{2}_q,
\qquad C=q\binom m2_q,\quad B=q^n[m-1]_q,
\qquad 0\le k\le m.
\]
The frequency rank multiplicity follows by choosing the \(t\)-dimensional image and counting surjections onto it. The largest absolute eigenvalue is the degree \(V=\lambda(m)\), because each Fourier multiplier is a sum of \(V\) unimodular terms and the constant character attains \(V\).

It remains to minimize \(|\lambda(k)|\). The Gaussian-binomial difference identities give, for \(1\le k<m\),
\[
\lambda(k+1)-\lambda(k)
=q^{n+k-1}\big(q^n[k]_q-q[m-1]_q\big)>0.
\]
Indeed \(q^n\ge q^m>q[m-1]_q\) for all \(q\ge2\), \(m\ge2\). For \(m\ge3\),
\[
\lambda(3)-C=q^n[3]_q\big(q^n-[m-1]_q\big)>0,
\]
so every \(k\ge3\) has \(\lambda(k)>C>0\). For \(m=2\), only the cases \(k=0,1,2\) occur and \(\lambda(2)=V>C\). We have \(\lambda(0)=C\) and \(\lambda(1)=C-B<0\), with
\[
\frac BC=\frac{q^{n-1}(q+1)}{[m]_q}.
\]
This ratio exceeds two whenever \(q\ge3\) or \(n>m\). It equals two when \((q,m,n)=(2,2,2)\) and lies strictly between one and two when \(q=2\), \(n=m\ge3\). Finally,
\[
\lambda(2)-C=q^n\big(q^n-(q+1)[m-1]_q\big).
\]
This is strictly positive for \(q\ge3\) or \(n>m\). Therefore those cases have \(|\lambda(1)|>C\) and \(\lambda(k)>C\) for all \(k\ge2\), proving the unique full-rank minimum. In the isolated \((2,2,2)\) case, \(|\lambda(1)|=C\) and \(\lambda(2)>C\).

For \(q=2\), \(n=m\ge3\), write \(u=2^{m-1}\ge4\). Direct substitution yields
\[
C=\frac{4u^2-6u+2}{3},\quad
\lambda(1)=-\frac{2(u^2-1)}{3},\quad
\lambda(2)=\frac{2(-u^2+6u+1)}3.
\]
Here \(-C<\lambda(2)<C\). The first inequality is equivalent to \(2u^2+6u+4>0\); the second follows from \(2^m<3(2^{m-1}-1)\) at \(m\ge3\). Also \(\lambda(1)<\lambda(2)<-\lambda(1)\): the first relation is the positive adjacent difference above, and the second follows from \(2u^2-6u-2>0\) for \(u\ge4\). Thus \(|\lambda(2)|\) is strictly smaller than both \(C\) and \(|\lambda(1)|\); all \(k\ge3\) exceed \(C\). The exceptional least singular value is therefore \(|\lambda(2)|\), and it is nonzero: the integer \(u=2^{m-1}\) cannot solve \(u^2-6u-1=0\) (the roots are \(3\pm\sqrt{10}\)). Dividing \(V\) by the two respective least singular values gives the stated sharp condition numbers. This proves the theorem for every prime power and dimension in its scope.

## Verification
A standalone Python checker, `check_rank2_bilinear.py`, uses integer Gaussian coefficients and tests the exact minimizer for \(760\) parameter configurations, with \(q\in\{2,3,4,5,7,8,9,11\}\), \(2\le m\le20\), and \(m\le n\le m+4\). It also independently computes the complete rank-two matrix indicator Fourier transform in \(673\) small-character cases for the prime fields \(q=2,3\) and compares every multiplier with the analytic formula. The recorded successful output is `RANK_TWO_BILINEAR_FOURIER_PASS parameter_cases=760 complete_fourier_characters=673`. Integer tests cannot establish the all-dimensional theorem; the preceding inequalities do so. Run with `python check_rank2_bilinear.py` using Python 3 and NumPy.

## Relationship to prior work
Delsarte's 1978 work establishes the bilinear-forms association scheme, its rank-distance Fourier multipliers and q-Krawtchouk character table. The Fourier eigenvalue formula is a **prerequisite**, not claimed as a discovery here. Brouwer, Cioabă, Ihringer and McGinnis (2018, particularly their Section 7) study the algebraically smallest and second-largest-in-absolute-value eigenvalues of related distance graphs, not the eigenvalue *nearest zero* across all ranks; their Theorem 7.5 does not identify the minimum singular value of the rank-two convolution. Schmidt's 2020 work concerns symmetric and quadratic forms rather than the unrestricted rectangular matrix spaces considered here. Under the bounded comparison performed, none of those inspected statements gives the all-parameter absolute minimum or the binary-square switch. It remains possible that a more general theorem not identified in that comparison implies this result.

## Limitations
The optimization concerns only the distance-two convolution, not higher rank distances, weighted rank shells, other operator norms, or perturbations of its support. Exact small singular values measure linear \(\ell^2\) deconvolution stability; no claims of numerical floating-point stability under extreme dimensions are made. Historical priority is not independently certified; in particular, the theorem may be derivable from an uninspected broader result on generalized q-Krawtchouk zeros. Independent validation has not been performed.

## References
1. Philippe Delsarte, *Bilinear Forms over a Finite Field, with Applications to Coding Theory*, Journal of Combinatorial Theory, Series A 25 (1978), 226–241, especially Theorem A2. DOI: 10.1016/0097-3165(78)90015-8.
2. Andries E. Brouwer, Sebastian M. Cioabă, Ferdinand Ihringer, Matt McGinnis, *The smallest eigenvalues of Hamming graphs, Johnson graphs and other distance-regular graphs with classical parameters*, Journal of Combinatorial Theory, Series B 133 (2018), 88–121, especially Section 7. DOI: 10.1016/j.jctb.2018.04.005; preprint arXiv:1709.09011.
3. Kai-Uwe Schmidt, *Quadratic and symmetric bilinear forms over finite fields and their association schemes*, Algebraic Combinatorics 3 (2020), 161–189. DOI: 10.5802/alco.88.
