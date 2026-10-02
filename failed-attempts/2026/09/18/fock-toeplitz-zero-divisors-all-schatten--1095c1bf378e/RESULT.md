# Two-factor Fock Toeplitz zero divisors in every Schatten ideal

## Result

Let \(n\ge 2\), and let \(f,g\in \mathcal S(\mathbb C^n)\) be the explicit symbols in Jie Qin's Theorem 1.1 (arXiv:2609.20555), so that
\[
T_fT_g=0,\qquad T_f\ne0,\qquad T_g\ne0
\]
on the classical Fock space \(F^2(\mathbb C^n)\).

Then
\[
T_f,T_g\in\bigcap_{p>0}\mathcal S_p.
\]
In particular, both factors are trace class. More quantitatively,
\[
\|T_f\|_1\le \frac49,\qquad \|T_g\|_1\le\frac49.
\]

If \(s_k(A)\) denotes the singular values of a compact operator in decreasing order and
\[
N_m=\binom{n+m}{n}\qquad(m\ge0),
\]
then
\[
s_{N_m+1}(T_f)\le 2^{-n-m-1},\qquad
s_{N_m+1}(T_g)\le 2^{-n-m-1}.
\]
Consequently, for fixed \(n\),
\[
s_k(T_f)+s_k(T_g)=O_n\!\left(e^{-c_n k^{1/n}}\right)
\]
for some \(c_n>0\).

Thus, in complex dimension at least two, the two-factor zero-product implication for Fock-space Toeplitz operators is not restored by compactness, by trace-class regularity, or even by membership of both factors in every Schatten quasi-ideal.

## Proof

Qin's Gaussian building block is
\[
\sigma_U(z)
=\exp\!\bigl(((I_2-4U^*)\xi)\cdot\xi-|z'|^2\bigr),
\]
where \(U\) is a \(2\times2\) unitary matrix satisfying \(U+U^*=I_2\) and \(\det U=1\). His Lemma 2.1 gives
\[
T_{\sigma_U}K_a=\kappa_n K_{D_U^*a},
\qquad
\kappa_n=2^{-n-2},\qquad
D_U=\operatorname{diag}(U/4,I_{n-2}/2).
\]

For a linear map \(A\) on \(\mathbb C^n\), write
\[
(C_Ah)(z)=h(Az).
\]
Since \(C_A^*K_a=K_{Aa}\), the kernel identity yields
\[
T_{\sigma_U}=\kappa_n C_{D_U^*}^{\,*}.
\]

Write
\[
D_U^*=W S,\qquad
W=\operatorname{diag}(U^*,I_{n-2}),\qquad
S=\operatorname{diag}(1/4,1/4,1/2,\ldots,1/2).
\]
The composition operator induced by \(W\) is unitary on Fock space, so \(C_{D_U^*}\) has the same singular values as \(C_S\). On the normalized monomial basis
\[
e_\alpha(z)=\frac{z^\alpha}{\sqrt{\alpha!}},
\]
the latter is diagonal:
\[
C_Se_\alpha
=
4^{-(\alpha_1+\alpha_2)}
2^{-(\alpha_3+\cdots+\alpha_n)}e_\alpha.
\]
Therefore, for every \(p>0\),
\[
\|T_{\sigma_U}\|_p^p
=
\frac{2^{-p(n+2)}}
{(1-4^{-p})^2(1-2^{-p})^{\,n-2}}.
\]
In particular,
\[
\|T_{\sigma_U}\|_1=\frac19.
\]

Qin represents each of \(f\) and \(g\) as a sum of four such Gaussian symbols,
\[
f=\sum_{k=1}^4 d_k\sigma_{V_k},
\qquad
g=\sum_{j=1}^4 c_j\sigma_{U_j},
\qquad
|c_j|=|d_k|=1.
\]
Hence each summand belongs to every \(\mathcal S_p\), and finite sums remain in every Schatten class (or Schatten quasi-class when \(0<p<1\)). At \(p=1\), the triangle inequality gives
\[
\|T_f\|_1,\ \|T_g\|_1
\le 4\cdot\frac19=\frac49.
\]

It remains to quantify the singular-value decay. Let \(P_{\le m}\) be the orthogonal projection onto holomorphic polynomials of total degree at most \(m\). Then
\[
\operatorname{rank}P_{\le m}=N_m=\binom{n+m}{n}.
\]
Every \(C_{D_U^*}^{\,*}\) preserves homogeneous degree, and on the homogeneous subspace of degree \(q\) it has norm at most
\[
\|D_U\|^q\le 2^{-q}.
\]
Consequently, for a single Gaussian block,
\[
\|T_{\sigma_U}(I-P_{\le m})\|
\le \kappa_n2^{-(m+1)}.
\]
Using the four-term representations,
\[
\|T_f(I-P_{\le m})\|,
\ \|T_g(I-P_{\le m})\|
\le4\kappa_n2^{-(m+1)}
=2^{-n-m-1}.
\]
Since \(T_fP_{\le m}\) and \(T_gP_{\le m}\) have rank at most \(N_m\), the approximation-number characterization of singular values gives
\[
s_{N_m+1}(T_f),\ s_{N_m+1}(T_g)
\le2^{-n-m-1}.
\]
Because \(N_m\) grows polynomially like \(m^n/n!\), this is stretched-exponential decay in the singular-value index.

The nonvanishing of \(T_f,T_g\) and the identity \(T_fT_g=0\) are exactly Qin's Theorem 1.1; only the operator-ideal refinement above is asserted here.

## Literature context and originality boundary

Qin's 2026 construction resolves the two-bounded-symbol zero-product question on \(F^2(\mathbb C^n)\) for \(n\ge2\). The paper records that its symbols are nonradial Schwartz functions with Gaussian decay and proves that their Toeplitz operators are bounded, nonzero, and have zero product. It does not formulate the resulting pair as trace-class or Schatten-class zero divisors.

General Schatten criteria for Fock/anti-Wick/localization operators are classical. In particular, Cordero and Gröchenig developed Schatten criteria for localization (anti-Wick/Gabor-Toeplitz) operators, and Isralowitz and Zhu studied compactness and Schatten classes for Fock Toeplitz operators with positive measure symbols. Very recent work also develops broad Schatten--Lorentz criteria for complex symbols on weighted Fock spaces. Accordingly, no novelty is claimed for the general principle that sufficiently rapidly decaying symbols can produce highly regular compact operators.

The contribution here is the explicit operator-ideal consequence for Qin's first two-bounded-factor zero-divisor pair, together with the exact Schatten formula for each Gaussian building block, the dimension-independent nuclear bound \(4/9\), and the explicit stretched-exponential singular-value estimate. Searches for zero-product results combined with trace-class, Schatten, nuclear, compact, and Segal--Bargmann/Fock terminology did not locate this formulation or quantitative refinement. Originality is therefore claimed only to the best of our knowledge.

## Limitations

The result concerns Qin's explicit pair in dimensions \(n\ge2\). It does not settle the still-open two-bounded-symbol problem on \(F^2(\mathbb C)\). The constant \(4/9\) and the displayed singular-value estimate are upper bounds and are not claimed to be optimal. No assertion is made about exact singular values of the four-term sums, finer operator ideals beyond the stated consequences, or analogous zero divisors for other Toeplitz geometries.

## References

1. J. Qin, *Zero-product problem for Toeplitz operators on the Fock space*, arXiv:2609.20555 (2026). https://arxiv.org/abs/2609.20555
2. W. Bauer and T. Le, *Algebraic properties and the finite rank problem for Toeplitz operators on the Segal--Bargmann space*, J. Funct. Anal. 261 (2011), 2617--2640. https://doi.org/10.1016/j.jfa.2011.07.006
3. E. Cordero and K. Gröchenig, *Time-frequency analysis of localization operators*, J. Funct. Anal. 205 (2003), 107--131. https://doi.org/10.1016/S0022-1236(03)00166-6
4. J. Isralowitz and K. Zhu, *Toeplitz operators on the Fock space*, Integral Equations Operator Theory 66 (2010), 593--611. https://doi.org/10.1007/s00020-010-1768-9
5. C. Xu and J. Dong, *IDA symbols and Schatten--Lorentz theory for Toeplitz operators on weighted Fock spaces*, arXiv:2609.16970 (2026). https://arxiv.org/abs/2609.16970
