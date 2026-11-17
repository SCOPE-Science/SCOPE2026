# Complete three-transposition resonance in a quadratic population flow

## Finding

For the four-species non-Volterra quadratic stochastic family of Jamilov [1], run a three-season deterministic calendar that uses each of the peripheral swaps \((12)\), \((23)\), and \((13)\) exactly once, with the same mixing strength \(0<\alpha<1\) in all seasons. **Every one of the six calendars has the same nonstationary spectrum.** In normalized peripheral composition its three-season return has trace and determinant on the two-dimensional sum-zero plane
\[
 t(\alpha)=-\alpha(\alpha^2-6\alpha+3),\qquad d(\alpha)=(2\alpha-1)^3,
\]
and spectral discriminant
\[
 \Delta(\alpha)=(1-\alpha)^4(\alpha^2-8\alpha+4).
\]
Consequently there is one, and only one, spectral coalescence for \(0<\alpha<1\), at
\[
 \boxed{\alpha_\triangle=4-2\sqrt3}.
\]
Below this threshold the two nonstationary eigenvalues are real and distinct; above it they form a nonreal conjugate pair. At the threshold they form a **genuine nonsemisimple Jordan block**, with repeated eigenvalue
\[
 \boxed{\lambda_\triangle=15\sqrt3-26<0}.
\]
For every probability composition \(p_0\in\mathbb R^3_{\ge0}\) with unit coordinate sum and every integer \(n\ge1\), the stroboscopic orbit at the threshold satisfies the *exact*, not merely asymptotic, identity
\[
 \boxed{p_{3n}-u=\lambda_\triangle^n(p_0-u)+n\lambda_\triangle^{n-1}N(p_0-u)},
 \qquad u=(1/3,1/3,1/3)^{\mathsf T},
\]
where \(N=(M_{\alpha_\triangle}-\lambda_\triangle I)|_E\) is a nonzero nilpotent endomorphism of the sum-zero plane \(E\), with \(N^2=0\). For all initial compositions outside one proper affine line, the second term is nonzero. It produces an alternating, polynomially enhanced exponential transient.

The phase ordering is reversed from that of a two-season calendar using two distinct swaps. The two-season threshold \(2\sqrt3-3\), established in earlier analysis, and the complete three-season threshold obey the exact complement relation
\[
 (2\sqrt3-3)+(4-2\sqrt3)=1.
\]
The two-season result is a comparison, not part of the new assertion.

## Assumptions and scope

Let \(\mathcal S^3=\{(x_1,x_2,x_3,w):x_i,w\ge0,\ x_1+x_2+x_3+w=1\}\). For a transposition \(\pi\) on \(\{1,2,3\}\) and \(0<\alpha<1\), define
\[
 (V_{\alpha,\pi}x)_i=2w\bigl(\alpha x_i+(1-\alpha)x_{\pi(i)}\bigr)\quad (i=1,2,3),
 \qquad (V_{\alpha,\pi}x)_4=w^2+(1-w)^2.
\]
Take any deterministic periodic three-season schedule containing each of \((12),(23),(13)\) once and repeat it indefinitely. Assume \(0<w_0<1\) so that normalized composition \(p_t=(x_{1,t},x_{2,t},x_{3,t})^{\mathsf T}/(1-w_t)\) is defined for every finite time. Define the swap permutation matrix \(P_{ij}\), \(B_{ij}=\alpha I+(1-\alpha)P_{ij}\), the all-ones rank-one projector \(J=\frac13\mathbf1\mathbf1^{\mathsf T}\), and \(E=\ker\mathbf1^{\mathsf T}\). All comparisons concern the same calendar phase, sampled after whole three-season blocks. No claim is made about arbitrary unequal mixing strengths or nonperiodic calendars.

For the representative chronological order \((12)\), \((23)\), \((13)\), the return matrix is \(M_\alpha=B_{13}B_{23}B_{12}\). Its explicitly factored form is
\[
 M_\alpha=\begin{pmatrix}
 -\alpha^3+4\alpha^2-3\alpha+1 & \alpha(\alpha-1)(\alpha-2) & \alpha(1-\alpha)\\
 \alpha(1-\alpha)&\alpha^2&1-\alpha\\
 \alpha(\alpha-1)(\alpha-2)&(1-\alpha)(\alpha^2-\alpha+1)&\alpha^2
 \end{pmatrix}.
\]
Every entry is strictly positive for \(0<\alpha<1\); each row and column sums to one. Thus \(u\) is the unique stationary peripheral composition, and all peripheral compositions tend to \(u\).

## Proof

**1. Exact nonlinear reduction.** Write \(y=(x_1,x_2,x_3)^{\mathsf T}\). Summing the peripheral equations gives \(1-w'=2w(1-w)\). Therefore
\[
 p'=\frac{2w B_{\pi}y}{2w(1-w)}=B_{\pi}p.
\]
Writing \(z=2w-1\) in the distinguished coordinate equation yields \(z'=z^2\). Hence \(z_t=z_0^{2^t}\), so \(w_t=(1+z_0^{2^t})/2\) for every \(t\ge0\). With \(0<w_0<1\) the normalization never vanishes. Repeating the season calendar gives exactly \(p_{3n}=M_\alpha^np_0\), without any linear approximation.

**2. Calendar completeness.** There are exactly three unordered edges among peripheral species and six orders that each use every edge once. Any permutation of these three edges is induced by some permutation of the three vertex labels (the natural \(S_3\) action on the edges is faithful and has order six). Simultaneously relabeling all three species conjugates the three kernels by the corresponding permutation matrix. Thus any complete three-edge calendar has a return matrix permutation-similar to \(M_\alpha\) and the same eigenvalues, nilpotent structure and relaxation classification.

**3. Characteristic polynomial and sharp phase boundary.** Direct multiplication yields the displayed matrix and
\[
 \operatorname{tr}M_\alpha-1=-\alpha(\alpha^2-6\alpha+3).
\]
A swap kernel has eigenvalues \(1,1,2\alpha-1\), so the product has determinant \((2\alpha-1)^3\). Since the uniform vector is an eigenvector of eigenvalue one and \(E\) is invariant, the other eigenvalues are the roots of \(\xi^2-t(\alpha)\xi+d(\alpha)\). Expanding its discriminant gives
\[
 t(\alpha)^2-4d(\alpha)=(1-\alpha)^4(\alpha^2-8\alpha+4).
\]
The quadratic's zeros are \(4\pm2\sqrt3\). Exactly \(4-2\sqrt3\) belongs to \((0,1)\). Thus the eigenvalues are distinct real for \(0<\alpha<\alpha_\triangle\), equal real at the threshold and nonreal conjugates for \(\alpha_\triangle<\alpha<1\). More specifically, for \(0<\alpha<1/2\) they have opposite signs, for \(\alpha=1/2\) they are \(0\) and \(-1/8\), and for \(1/2<\alpha<\alpha_\triangle\) both are negative. Above the threshold their common modulus is \((2\alpha-1)^{3/2}\), by their product.

**4. Defectiveness and exact powers.** Substituting \(\alpha_\triangle\) into half the trace yields \(\lambda_\triangle=15\sqrt3-26\), nonzero and strictly negative. At an eigenvalue collision, a diagonalizable operator on a two-dimensional space must equal the scalar \(\lambda_\triangle I\) there. If that occurred for \(M\), then \(M=J+\lambda_\triangle(I-J)\), a symmetric matrix. But direct multiplication gives \((M_\alpha)_{12}-(M_\alpha)_{21}=\alpha(1-\alpha)^2>0\) for every interior parameter. Therefore the collision is defective. Cayley–Hamilton on \(E\) gives \(N^2=0\) and \(N\ne0\). The binomial identity \((\lambda_\triangle I+N)^n=\lambda_\triangle^n I+n\lambda_\triangle^{n-1}N\) proves the exact expression for every integer \(n\ge1\). The kernel of the rank-one nonzero nilpotent \(N\) in \(E\) is one-dimensional, so generic deviations have the polynomial correction.

**5. Comparison with a two-edge calendar.** For any two distinct peripheral swaps, one two-season return has discriminant \((1-\alpha)^2(\alpha^2+6\alpha-3)\), with critical value \(\alpha_2=2\sqrt3-3\). It is complex below \(\alpha_2\) and real above. Algebra gives \(\alpha_2+\alpha_\triangle=1\). The result for two seasons is explicitly excluded from the new contribution; the three-season all-edge classification and reversed phase are the asserted contribution.

## Verification

`CHECKER.py` is a standalone SymPy script. It symbolically multiplies the three stochastic kernels, verifies their restricted trace, determinant and factorized discriminant, checks that all six all-edge calendars have the same characteristic polynomial, and verifies nonzero square-zero nilpotence at the exact radical threshold. It then checks the Jordan power identity at several finite exponents, the exact original nonlinear normalization on 21 rational examples across three parameters, and the two-season comparison discriminant. The successful output is `TRIANGULAR_SWITCHING_SYMBOLIC_OK all_calendars=6 Jordan_powers=4 nonlinear_trajectories=21`. The proof above, not the finite checks, establishes the identities for all values quantified in the theorem.

## Relationship to prior work

Jamilov [1, Section 3] supplies the nonlinear quadratic family and proves its autonomous fixed-permutation trajectory behavior, including regularity for interior mixing. This theorem retains exactly that family but changes the subject to a periodic calendar using **all three distinct peripheral transpositions**. Its complete-order spectral discriminant and nonsemisimple collision are not part of the autonomous claims. An earlier two-transposition analysis already identifies a different exceptional-point threshold; it is not rediscovered here. The complete triangle has a different spectral polynomial, a complementary threshold and the opposite complex/real phase ordering. General statements that products of reversible stochastic kernels can be nonreversible do not alone calculate this exact all-calendar classification.

Additional relevant literature [2,3] discusses non-Volterra operators and superpositions, but the accessible abstracts do not establish this three-season formula. Their full texts could not be inspected; the possible existence of an equivalent result there remains a priority caveat, rather than a claim of exhaustive noncoverage.

## Limitations

The theorem fixes four species, three transposition seasons using every peripheral pair exactly once, a common interior mixing parameter, and a repeated deterministic season order. The eigenvalue collision pertains to the normalized peripheral three-season return; it is not a separate bifurcation of the scalar central mass. No assertion is made about arbitrary calendar lengths, unequal seasonal parameters, or parameter-uniform mixing as \(\alpha\to1\). A same-source or general Markov-product equivalent outside accessible full texts could affect publication priority. The result has not received an independent mathematical audit.

## References

[1] U. U. Jamilov, *A family of non-Volterra quadratic operators corresponding to permutations*, Communications in Mathematics 31 (2023), 31–41. First public arXiv version dated 2022-10-11. https://arxiv.org/abs/2210.05107 ; https://doi.org/10.46298/cm.10135.

[2] U. U. Jamilov and A. Khudoyberdiev, *On the dynamics of non-Volterra quadratic operators corresponding to permutations*, DOI https://doi.org/10.1080/10236198.2023.2284827 (full text not inspected).

[3] N. Aralova and U. Jamilov, *The dynamics of superposition of non-Volterra quadratic stochastic operators*, DOI https://doi.org/10.1080/10236198.2022.2126316 (full text not inspected).
