# Exact Veronese Fourier-projection norms and a parity-sensitive second term

## Finding

For every odd prime power \(q\ge3\) and integer \(n\ge1\), let \(G=\operatorname{Sym}_n(\mathbb F_q)\) and let \(P_{n,q}\) be the Fourier projection onto the rank-one Veronese frequency set with the origin, \(\mathcal V_{n,q}=\{vv^{\mathsf T}:v\in\mathbb F_q^n\}\). The exact sharp endpoint norms \(\|P_{n,q}\|_{\ell^1\to\ell^1}=\|P_{n,q}\|_{\ell^\infty\to\ell^\infty}=L_{n,q}\) are the explicit rank sums below. Their large-dimension behavior, for each fixed \(q\), has the stronger two-term expansion
\[
 L_{n,q}=\frac{C_q}{2}q^{n/2}+B_{n\bmod2}(q)q^{-n/2}+o_q(q^{-n/2}).
\]
The leading constant is the convergent Euler product
\[
 C_q=\prod_{j\ge1}(1-q^{-(2j-1)})\prod_{j\ge0}(1+q^{-j-1/2}),
\]
and the two parity constants \(B_0(q),B_1(q)\) have absolutely convergent series given below. The exact finite sums separate the cases \(q\equiv1\pmod4\) and \(q\equiv3\pmod4\).

Put \(N=n(n+1)/2\), and write \(M_{n,r}\) for the number of symmetric \(n\times n\) matrices of rank \(r\) over \(\mathbb F_q\). With the Gaussian binomial coefficient, this number is
\[
 M_{n,r}={n\brack r}_q q^{r(r+1)/2}\prod_{j=1}^{\lceil r/2\rceil}(1-q^{-(2j-1)}),\qquad 0\le r\le n.
\]
For \(q\equiv1\pmod4\),
\[
 \boxed{L_{n,q}=\frac1{2q^N}\bigg[\sum_{r=0}^n M_{n,r}q^{n-r/2}+\sum_{s=0}^{\lfloor n/2\rfloor}M_{n,2s}q^{-s}\bigg].}
\]
For \(q\equiv3\pmod4\),
\[
 \boxed{L_{n,q}=\frac1{2q^N}\bigg[\sum_{s=0}^{\lfloor n/2\rfloor}M_{n,2s}(q^{n-s}+q^{-s})+\sum_{\substack{1\le r\le n\\r\ \mathrm{odd}}}M_{n,r}\sqrt{1+q^{2n-r}}\bigg].}
\]

For the explicit second term set \(Q=q^{-1}\), \(P_d=\prod_{i=1}^d(1-Q^i)\), with \(P_0=1\), and \(a=\prod_{j\ge1}(1-Q^{2j-1})\). Define
\[
 w_d=\frac{aQ^{d(d+1)/2}}{P_d},\qquad
 t_{\epsilon,d}=Q^{1-d}\left(\frac{Q^{(\epsilon-d)\bmod2}}{1-Q^2}-\frac{1-Q^d}{1-Q}\right),\quad \epsilon=0,1.
\]
Here \((\epsilon-d)\bmod2\) denotes its remainder in \(\{0,1\}\). Then
\[
 \boxed{\begin{aligned}
 B_\epsilon(q)={}&\frac12\sum_{d\ge0}w_dQ^{-d/2}t_{\epsilon,d}
 +\frac12\sum_{\substack{d\ge0\\d\equiv\epsilon\ (2)}}w_dQ^{-d/2}\\
 &+\frac{\mathbf1_{q\equiv3\ (4)}}4\sum_{\substack{d\ge0\\d\not\equiv\epsilon\ (2)}}w_dQ^{d/2}.
 \end{aligned}}
\]

## Assumptions and scope

The field has odd characteristic. A fixed nontrivial additive character \(\psi\colon\mathbb F_q\to\mathbb C\) determines the Fourier characters \(\chi_A(B)=\psi(\operatorname{tr}(AB))\) of \(G\). The trace pairing on symmetric matrices is nondegenerate because \(2\) is invertible. The Fourier convention is unnormalized synthesis and normalized Haar measure, so the convolution kernel of \(P_{n,q}\) at \(B\) is \(q^{-N}F(B)\) with \(F(B)=\sum_{A\in\mathcal V_{n,q}}\psi(\operatorname{tr}(AB))\). The endpoint norms equal the \(\ell^1\) norm of this kernel. The scope includes all odd prime powers and all positive dimensions, and no even-characteristic assertion is made.

## Proof

**1. Rank and type counts.** Exactly two nonzero vectors \(\pm v\) represent each nonzero \(vv^{\mathsf T}\). Therefore \(|\mathcal V_{n,q}|=(q^n+1)/2\) and
\[
 F(B)=\frac12\left(1+\sum_{v\in\mathbb F_q^n}\psi(v^{\mathsf T}Bv)\right).
\]
Diagonalizing \(B\) by congruence, a rank-\(r\) matrix of discriminant square class \(\tau\in\{-1,1\}\) has
\[
 F(B)=\frac12(1+q^{n-r}\tau\mathfrak g_q^{\,r}),
 \qquad \mathfrak g_q=\sum_{x\in\mathbb F_q}\psi(x^2),
 \qquad \mathfrak g_q^{\,2}=\eta(-1)q,
\]
where \(\eta\) is the quadratic multiplicative character. The rank count follows by choosing a radical, then a nonsingular symmetric form on the quotient: the number of the latter is \(q^{r(r+1)/2}\prod_{j=1}^{\lceil r/2\rceil}(1-q^{-(2j-1)})\). For odd rank, the two discriminant types occur equally often. For even rank \(r=2s\), their signed imbalance, with \(\tau=\eta(\det B_{\rm nd})\), is
\[
 M_{n,2s,+}-M_{n,2s,-}=\eta(-1)^s q^{-s}M_{n,2s}.
\]
The last identity follows either from the two orthogonal-group orders or by counting orthogonal bases in each nondegenerate quadratic space. It holds equally for radical-extended matrices because the radical choice contributes the same multiplicity in both types.

**2. Absolute coefficient average.** In even rank \(r=2s\), the Gauss sum is real and equals \(\tau\eta(-1)^s q^{n-s}\), with \(q^{n-s}\ge1\). Its mean absolute contribution across both discriminant types is
\[
 \frac12(q^{n-s}+q^{-s}).
\]
In odd rank, when \(q\equiv1\pmod4\), the two opposite real Gauss sums have equal frequency, giving mean modulus \(q^{n-r/2}/2\). For \(q\equiv3\pmod4\), those two Gauss sums are imaginary, giving modulus \(\sqrt{1+q^{2n-r}}/2\). Summing over all symmetric matrices and dividing by \(q^N\) proves both finite formulas, including the boundary \(r=0\). Translation invariance makes the row and column absolute sums of the convolution operator constant, so the \(\ell^1\) and \(\ell^\infty\) bounds are equalities (a delta input, or a phase-aligned input, attains them).

**3. Corank distribution and Euler product.** Write \(d=n-r\), \(P_j=\prod_{i=1}^j(1-Q^i)\), and \(a_h=\prod_{j=1}^{h}(1-Q^{2j-1})\). Then direct substitution into the rank count gives
\[
 p_{n,d}:=\frac{M_{n,n-d}}{q^N}
 =Q^{d(d+1)/2}\frac{P_n}{P_dP_{n-d}}a_{\lceil(n-d)/2\rceil},\quad 0\le d\le n.
\]
For every fixed \(d\), \(p_{n,d}\to w_d=aQ^{d(d+1)/2}/P_d\). Since \(P_d\ge\prod_{j\ge1}(1-Q^j)>0\), these probabilities have a uniform bound by a constant times \(Q^{d(d+1)/2}\). In particular the weighted sums in all following steps are dominated by rapidly decreasing summable sequences. The principal term in the finite norm is
\[
 \frac{q^{n/2}}2\sum_{d=0}^n p_{n,d}Q^{-d/2}.
\]
The limit of the weighted sum is
\[
 C_q=\sum_{d\ge0}w_dQ^{-d/2}=a\sum_{d\ge0}\frac{Q^{d^2/2}}{P_d}
 =a\prod_{j\ge0}(1+Q^{j+1/2}),
\]
where the final step is Euler's \(q\)-binomial identity applied to \(Q^{1/2}\).

**4. Sharp second term.** For fixed corank \(d\), write \(r=n-d\). The finite-product ratio and the missing odd factors have the uniform fixed-\(d\) expansions
\[
 \frac{P_n}{P_r}=1-\frac{Q^{r+1}(1-Q^d)}{1-Q}+O_q(Q^{2r}),
\qquad
 a_{\lceil r/2\rceil}=a\left(1+\frac{Q^{r+1+(r\bmod2)}}{1-Q^2}+O_q(Q^{2r})\right).
\]
Thus along \(n\equiv\epsilon\pmod2\),
\[
 Q^{-n}(p_{n,d}-w_d)\longrightarrow w_dt_{\epsilon,d}.
\]
The convergence passes through the weighted sum: split at \(d\le n/2\), use the product estimates uniformly on that range, and bound the tail by the Gaussian decay \(Q^{d(d+1)/2}\), which after any exponential rescaling remains negligible. Hence the principal term contributes the first series in \(B_\epsilon\).

For even ranks \(r=n-d\), the exact finite norm has the additional term \(\tfrac12 p_{n,d}q^{-r/2}\). After multiplying by \(q^{n/2}\), it contributes \(\tfrac12 w_dQ^{-d/2}\) when \(d\equiv\epsilon\pmod2\). If \(q\equiv3\pmod4\), each odd rank also contributes, relative to the principal term, \(\tfrac12p_{n,d}(\sqrt{1+q^{2n-r}}-q^{n-r/2})\). The expansion \(\sqrt{1+A^2}-A=1/(2A)+O(A^{-3})\), with \(A=q^{(n+d)/2}\), gives after multiplication by \(q^{n/2}\) exactly \(\tfrac14w_dQ^{d/2}\). For \(q\equiv1\pmod4\) this last correction is absent. Absolute summability and the same tail bounds justify termwise limits and give the stated \(o_q(q^{-n/2})\) remainder. This proves the theorem for both parities.

## Verification

The included independent finite-field checker constructs the complete quadratic frequency image and directly sums every Fourier coefficient using complex roots of unity for \((q,n)=(3,1),(3,2),(3,3),(5,1),(5,2)\). It verifies rank multiplicities, pointwise coefficient moduli, Parseval, and the sharp finite norm. The high-precision second checker checks the exact finite rank formulas against \(C_q\) and \(B_\epsilon(q)\) for \(q=3,5,7\) and \(4\le n\le16\), with explicit numerical error bounds. Both scripts use only the Python standard library; run `python check_veronese.py` and `python check_second.py` from the same directory. Numerical checks are corroboration of, not substitutes for, the general proof.

## Relationship to prior work

The rank-and-type eigenstructure and enumerators are within the translation association scheme of symmetric bilinear forms treated by K.-U. Schmidt (arXiv:1410.7184), particularly the eigenvalue formulas and appendix Gauss sums. Those eigenvalues and standard orthogonal-group rank counts are explicitly **not** claimed as new. The later treatment arXiv:1803.04274 gives a general association-scheme framework, including even-characteristic cases. The present evaluated claim is instead the sharp \(\ell^1/\ell^\infty\) norm of the Veronese frequency **projection**, its Euler-product leading constant, and the parity-sensitive second asymptotic coefficient. A search for equivalent endpoint-norm statements and corank-limit expansions did not identify a direct prior evaluation; this is bounded originality evidence, not proof of historical priority.

## Limitations

Only odd prime powers and the full quadratic rank-one frequency image including zero are considered. The two-term constants are rapidly convergent series, not elementary closed forms. No assertion about arbitrary rank-\(r\) frequency balls or even-characteristic Veronese sets is made. Earlier work may have deduced the same norm from the known association-scheme eigenvalues; that historical-priority risk remains. No independent mathematical audit has been performed.

## References

1. K.-U. Schmidt, *Symmetric bilinear forms over finite fields with applications to coding theory*, arXiv:1410.7184, first posted 2014-10-27. https://arxiv.org/abs/1410.7184 .
2. K.-U. Schmidt, *Quadratic and symmetric bilinear forms over finite fields and their association schemes*, arXiv:1803.04274, first posted 2018-03-12. https://arxiv.org/abs/1803.04274 .
3. Classical quadratic Gauss-sum identity, orthogonal-group order formulas, and Euler's \(q\)-binomial identity; invoked in the proof with their normalizations explicitly stated.
