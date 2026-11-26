# The sharp half-power cutoff for a Bergman coefficient coupling inequality

## Finding

Write a polynomial in the normalized analytic Bergman space \(A^2(\mathbb D,dA/\pi)\) as \(f(z)=\sum_{k=0}^{N}a_k\sqrt{k+1}\,z^k\). For \(s>0\), set
\[
\begin{aligned}
\mathcal E(f)&=\sum_{k=0}^{N}\frac{|a_k|^2}{(k+1)(k+2)},\\
\mathcal C_s(f)&=s\left|\sum_{k=0}^{N-1}\frac{\sqrt{(k+1)/(k+2)}\,\overline{a_k}a_{k+1}}{(k+1+s/2)(k+2+s/2)}\right|.
\end{aligned}
\]
These formulas include constant polynomials; the zero polynomial is excluded when considering ratios. The **sharp half-power theorem** is
\[
\mathcal C_s(f)\le s\mathcal E(f)\text{ for every polynomial }f
\quad\Longleftrightarrow\quad s\ge\tfrac12.
\]
Precisely, for every \(s>0\) the best constant \(K_s=\sup_{f\ne0}\mathcal C_s(f)/\mathcal E(f)\) equals the norm of a self-adjoint Jacobi matrix \(J_s\), with zero diagonal and positive off-diagonal entries
\[
j_{s,k}=\frac{s}{2}\frac{(k+1)\sqrt{(k+2)(k+3)}}{(k+1+s/2)(k+2+s/2)},\qquad k\ge0.
\]
Its essential spectrum is \([-s,s]\). If \(s\ge1/2\), \(K_s=s\) and there are no eigenvalues outside this interval. If \(0<s<1/2\), \(K_s>s\) and there are infinitely many simple eigenvalues in each of \((s,\infty)\) and \(( -\infty,-s)\), with no accumulation off the essential endpoints. In particular, the inequality fails for every subcritical exponent, witnessed by a finite polynomial.

For comparison with Toeplitz theory, the analytic Bergman Toeplitz operator with symbol \(z+c|z|^s\) is hyponormal exactly when \(|c|\le 1/K_s\). Consequently the exact permissible radius is \(1/s\) for \(s\ge1/2\), and is strictly smaller for every \(0<s<1/2\).

## Assumptions and scope

The disk is \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), the area measure is normalized to total mass one, \(s\) is any fixed positive real number, and polynomial degree is unbounded. The coefficient inequality is a statement about all *finite* polynomial coefficient strings of any length. The Jacobi matrix acts on \(\ell^2(\mathbb N_0)\). The matrix norm \(K_s\) below the cutoff is an exact spectral characterization, not a purported elementary closed formula. In the Toeplitz corollary, \(c\) is arbitrary complex and hyponormal means nonnegative self-commutator \(T^*T-TT^*\).

## Proof

**1. Exact Bergman reduction.** In the orthonormal basis \(e_k(z)=\sqrt{k+1}\,z^k\), multiplication by \(z\) is the unilateral weighted shift \(We_k=w_ke_{k+1}\), with \(w_k=\sqrt{(k+1)/(k+2)}\). For radial multiplication compressed to the Bergman space, \(D_s=T_{|z|^s}\) is diagonal, with \(D_se_k=d_{s,k}e_k\), \(d_{s,k}=(k+1)/(k+1+s/2)\). Direct calculation gives
\[
W^*W-WW^*=H=\operatorname{diag}\left(\frac1{(k+1)(k+2)}\right)_{k\ge0},\qquad
 d_{s,k+1}-d_{s,k}=\frac{s/2}{(k+1+s/2)(k+2+s/2)}.
\]
After the substitution \(y_k=a_k/\sqrt{(k+1)(k+2)}\), the two forms satisfy \(\mathcal E(f)=\|y\|_2^2\) and
\[
\mathcal C_s(f)=2\left|\sum_{k\ge0}j_{s,k}\overline{y_k}y_{k+1}\right|.
\]
Every finitely supported \(y\) arises from some polynomial. Phase alignment of consecutive coefficients makes the supremum equal to the norm of the bounded real symmetric Jacobi matrix \(J_s\) with entries \(j_{s,k}\); more formally \(\sup_y2|\sum j_{s,k}\overline y_k y_{k+1}|/\|y\|^2=\|J_s\|\), because nonnegative coefficients allow replacing a vector by its moduli and the unitary \(y_k\mapsto(-1)^k y_k\) negates \(J_s\).

**2. Essential spectrum.** Let \(a=s/2>0\). Expanding the explicit entries,
\[
\frac{j_{s,k}}{a}=1+\frac{1/2-2a}{k}+O_a(k^{-2})\qquad(k\to\infty).
\]
Thus \(J_s-a(S+S^*)\) is compact, where \(S\) is the unilateral shift. The latter operator has spectrum and essential spectrum \([-2a,2a]\). Weyl's theorem yields \(\sigma_{\rm ess}(J_s)=[-s,s]\), and \(K_s\ge s\).

**3. The entire supercritical and critical regime.** If \(s\ge1/2\), then \(a\ge1/4\). The arithmetic-geometric mean inequality yields, for all \(k\ge0\),
\[
\begin{aligned}
(k+1+a)(k+2+a)
&\ge(k+5/4)(k+9/4)\\
&=(k+1)(k+5/2)+5/16\\
&>(k+1)\sqrt{(k+2)(k+3)}.
\end{aligned}
\]
Hence \(0<j_{s,k}<a\) for every index. For any finite string,
\[
|\langle J_sy,y\rangle|\le2a\sum_{k\ge0}|y_k||y_{k+1}|\le 2a\|y\|_2^2.
\]
By density this proves \(K_s\le2a=s\). The essential spectral lower bound gives equality and excludes eigenvalues outside \([-s,s]\).

**4. Infinitely many outliers below the cutoff.** Let \(0<s<1/2\), so \(\delta=1/2-2a>0\). The expansion in step 2 shows \(j_{s,k}\ge a(1+\delta/(3N))\) throughout every sufficiently far block \(N\le k\le N+\lfloor N^{3/4}\rfloor\). In the coordinate block \(\{N,\ldots,N+L-1\}\), \(L=\lfloor N^{3/4}\rfloor\), use the discrete Dirichlet sine vector \(y_{N+i}=\sin(\pi(i+1)/(L+1))\), \(0\le i<L\), zero elsewhere. Since this is the top eigenvector of the constant-off-diagonal length-\(L\) path, its Rayleigh quotient satisfies
\[
\frac{\langle J_sy,y\rangle}{\|y\|^2}
\ge2a\left(1+\frac{\delta}{3N}\right)\cos\left(\frac\pi{L+1}\right)>2a=s
\]
for all sufficiently large \(N\), because \(L^{-2}=o(N^{-1})\). Choose arbitrarily many widely separated such blocks, with at least one unused index between them. The cross-terms vanish exactly, so the span of the block vectors has Rayleigh quotient strictly above \(s\) for every nonzero vector. The min-max principle and essential-spectrum description force infinitely many discrete eigenvalues above \(s\). The alternating-sign unitary conjugates \(J_s\) to \(-J_s\), giving equally many below \(-s\). Each eigenvalue of a half-line Jacobi matrix with nonzero subdiagonal is simple: its eigenvector is uniquely determined by the first coordinate through the three-term recurrence, and that first coordinate cannot vanish for a nonzero eigenvector. Compactness bounds the spectrum and confines accumulation to the essential-spectrum endpoints. As \(K_s>s\), density of finite strings supplies an actual finite-degree polynomial violating the proposed constant \(s\).

**5. Toeplitz interpretation.** With \(T=W+cD_s\), the direct diagonal/off-diagonal calculation gives
\[
T^*T-TT^*=H^{1/2}(I+Q_c)H^{1/2},
\]
where \(Q_c\) has off-diagonal entries of modulus \(|c|j_{s,k}\) and is diagonally unitarily equivalent to \(|c|J_s\). Positivity on the dense polynomial core, hence everywhere, holds exactly when \(I+|c|J_s\ge0\), equivalently \(|c|K_s\le1\) by spectral symmetry. This completes the claimed equivalence.

## Verification

The included `check.py` reconstructs the Jacobi weights directly, compares them with the normalized Bergman moment calculation, checks the entrywise supercritical bound at several exponents and large indices, and tests illustrative finite compressions on both sides of the cutoff. It requires Python 3 with NumPy and SciPy. The finite computations are diagnostic only; the exact inequality, infinite spectral multiplicity and quantifier over all degrees are established by the preceding proof. In particular, numerical eigenvalues near the spectral edge are not used to infer the critical threshold.

## Relationship to prior work

Simanek (2018), Section 2, proved the necessary bound \(|c|\le1/s\) and sufficiency for \(s\ge2\) in the one-step unweighted Bergman case; it explicitly left the smaller-exponent behavior open. Simanek (2020), Theorems 2.1–2.2, and Le–Simanek (2020), Theorem 2.1, give the abstract Jacobi-norm characterization and the essential interval for the more general weighted operator; they do not evaluate the one-step unweighted threshold \(1/2\), nor give the infinite-outlier dichotomy established here. The present work uses that well-established reduction only as context and independently derives the exact coefficient normalization and proves the missing norm/point-spectrum classification. A general prior norm formula is not itself a proof of the particular sharp half-power transition.

## Limitations

The sharp simple constant is established only for normalized unweighted analytic Bergman space and adjacent coefficient coupling, not for every weighted Bergman measure or higher-shift coupling. For \(s<1/2\), the optimal constant is specified exactly by the Jacobi spectral radius but not reduced to an elementary expression; this is a genuine limit, not a numerical approximation claim. Eigenvalue asymptotic counts and their edge spacing are not determined. Historical priority beyond the inspected sources has not been independently established.

## References

1. Brian Simanek, *Hyponormal Toeplitz Operators with Non-Harmonic Algebraic Symbol*, first posted 1 July 2018, https://arxiv.org/abs/1807.00356, especially Theorem 2.1 and the discussion following Corollary 2.3.
2. Brian Simanek, *Hyponormal Toeplitz Operators on Weighted Bergman Space*, first posted 22 January 2020, https://arxiv.org/abs/2001.07823, especially Theorems 2.1–2.2.
3. Trieu Le and Brian Simanek, *Hyponormal Toeplitz Operators on Weighted Bergman Spaces*, first posted 16 March 2020, https://arxiv.org/abs/2003.07330, especially Theorem 2.1 and the analytic Bergman example in Section 2.
4. Sumin Kim and Jongrak Lee, *Hyponormality of Toeplitz Operators with Non-Harmonic Symbols on the Bergman Spaces*, first published 7 April 2021, https://doi.org/10.1186/s13660-021-02602-1 (different monomial symbol families).
