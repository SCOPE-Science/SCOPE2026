# Sharp reflective-Kaczmarz ordering on a four-cycle Gram matrix

## Finding

**Theorem.** Let \(0<t<1/2\) and let four real unit row vectors \(u_0,\ldots,u_3\in\mathbb R^4\) have Gram matrix
\[
G_t=\begin{pmatrix}
1&t&0&t\\t&1&t&0\\0&t&1&t\\t&0&t&1
\end{pmatrix}.
\]
For any order \(\pi=(\pi_1,\pi_2,\pi_3,\pi_4)\) of the four rows, set \(H_i=I-2u_i u_i^{\mathsf T}\), \(Q_\pi=H_{\pi_4}H_{\pi_3}H_{\pi_2}H_{\pi_1}\), and define its **chordal eigengap** by
\[
d_\pi=\min_{\lambda\in\sigma(Q_\pi)}|1-\lambda|.
\]
Exactly the eight cyclic orders (each consecutive pair is joined by an edge of the four-cycle, including the last-to-first pair) maximize this gap. They have
\[
\begin{aligned}
 c_\pm(t)&=-1+4t^2+4t^4\pm4t^3\sqrt{2+t^2},\\
 d_{\mathrm{cyc}}(t)&=\sqrt{2\{1-c_+(t)\}}.
\end{aligned}
\]
The other sixteen orders have the same, strictly smaller gap
\[
d_{\mathrm{other}}(t)=2\sqrt{1-4t^2},\qquad
 d_{\mathrm{cyc}}(t)>d_{\mathrm{other}}(t)>0.
\]
The near-singular improvement is sharp:
\[
\lim_{t\uparrow 1/2}\frac{d_{\mathrm{cyc}}(t)}{d_{\mathrm{other}}(t)}=\frac2{\sqrt3}.
\]
For deterministic reflective Kaczmarz with repeated epochs, these eight orders uniquely minimize the inverse-gap constant \(\eta_\pi=2/d_\pi\), as defined via the sine of the reflection-product eigenphases.

## Assumptions and scope

The four rows are normalized and span \(\mathbb R^4\); the parameter domain is the entire open interval \(0<t<1/2\). The cycle edges are \(01,12,23,30\), with opposite-pair inner products zero. The linear system \(Ax=b\) may have any right-hand side; only its row Gram matrix affects the error reflections and their eigengap. One epoch consists of precisely one reflection at each of the four rows, in the prescribed order, with reflection relaxation parameter two. We optimize the eigengap, not the error after any fixed finite number of epochs.

## Proof

**Existence and normalization.** The Gram eigenvalues are \(1-2t,1,1,1+2t\). They are positive precisely in the stated range, so the required independent unit vectors exist. Write a vector in the row basis as \(v=\sum_j a_j u_j\). Reflection in row \(i\) acts on coefficients by
\[
B_i=I-2e_i G_{t,i:}.
\]
Thus \(Q_\pi\) is similar to \(B_{\pi_4}\cdots B_{\pi_1}\). Each \(B_i\) satisfies \(B_i^{\mathsf T}G_t B_i=G_t\), so its product has an orthogonal real realization; its eigenvalues have modulus one.

**Why four rows are minimal.** For at most three real Householder reflections, all permutations have the same characteristic polynomial: for three factors, the six orders are cyclic shifts of a product or of its reversed product. Cyclic shifts are similar, and reversing a product of symmetric involutions gives its inverse. A real orthogonal matrix and its inverse have the same eigenvalue multiset. Two factors are even simpler. The present four-row family therefore realizes the first possible ordering-dependent reflection spectrum.

**Complete order classification.** Direct multiplication of the four explicit \(B_i\), followed by the determinant, yields exactly two characteristic polynomials among the twenty-four orders. For the eight cyclic orders,
\[
p_{\rm cyc}(z)=(z+1)^4-16t^2z(z+1)^2-16t^4z(z-1)^2.
\]
For every other order,
\[
p_{\rm other}(z)=(z+1)^2\big[(z+1)^2-16t^2z\big].
\]
These identities can be checked by multiplying the four \(4\times4\) matrices in the coefficient basis for all twenty-four permutations. This is an exhaustive finite calculation, independently reproducible in the included standalone symbolic verifier; the two families have multiplicities eight and sixteen. No numeric sampling is used to establish exhaustiveness.

**Rotation angles and strict gap.** A real orthogonal matrix of determinant one with reciprocal degree-four characteristic polynomial has eigenvalues in two conjugate pairs. Writing those pairs as \(e^{\pm i\theta_+}\) and \(e^{\pm i\theta_-}\), comparison of coefficients gives their cosines \(c_+(t),c_-(t)\) above. The noncyclic polynomial has two eigenvalues \(-1\) and one conjugate pair with cosine
\[
c_{\rm other}(t)=-1+8t^2.
\]
Both cosine branches for the cyclic case lie strictly between \(-1\) and \(1\): \(c_-(t)>-1\) follows from \(1+t^2>t\sqrt{2+t^2}\); and \(c_+(t)<1\) follows because it is strictly increasing and equals one at the excluded endpoint \(t=1/2\). Therefore the smallest chordal gap is controlled by the largest cosine. For all \(0<t<1/2\),
\[
 c_{\rm other}(t)-c_+(t)
 =4t^2\bigl(1-t^2-t\sqrt{2+t^2}\bigr)>0.
\]
Indeed the term in parentheses is positive exactly when \(4t^2<1\), by squaring the two positive sides of \(t\sqrt{2+t^2}<1-t^2\). Hence cyclic orders strictly maximize the gap and all sixteen other orders tie.

**Boundary ratio and solver meaning.** Both largest cosines tend to one as \(t\uparrow1/2\), and their derivatives at that endpoint are \(c_+'(1/2)=32/3\) and \(c_{\rm other}'(1/2)=8\). Taking the ratio of the resulting first-order vanishing gaps proves the limit \(2/\sqrt3\). For the homogeneous error of the reflective row iteration, \(e_{4k}=Q_\pi^ke_0\). Since \(1\notin\sigma(Q_\pi)\), the average over \(N\ge1\) epochs obeys
\[
\left\|\frac1N\sum_{k=0}^{N-1}Q_\pi^k\right\|_2
 =\max_{\lambda\in\sigma(Q_\pi)}\frac{|1-\lambda^N|}{N|1-\lambda|}
 \le\frac{2}{N d_\pi}.
\]
The equality is the normal-matrix spectral theorem, and the bound follows from \(|1-\lambda^N|\le2\). The inverse eigengap convention based on the sine of eigenphases is exactly \(2/d_\pi\). The strictly largest \(d_\pi\) therefore gives the sharp order for this standard uniform averaging **bound**, not a claim of pointwise optimality at each finite \(N\).

## Verification

The included `verify_reflection.py` uses exact symbolic arithmetic to generate all twenty-four products, verify both characteristic polynomial identities, count the order classes, verify the Gram isometries and cosine identities, and establish the boundary derivatives. It additionally tests five rational parameters and compares spectra obtained from Euclidean Cholesky realizations at three positive parameter values across all permutations. The separately included `verification_output.txt` records the actual execution results. Symbolic finite exhaustion covers the order space exactly; the strict inequality and all-parameter assertions are proved algebraically above.

## Relationship to prior work

Shao's 2021 reflective Kaczmarz work defines an eigengap controlling deterministic epoch averaging; this motivates optimizing it rather than ordinary projection-convergence factors. The 2024 analysis gives a general characteristic equation (attributed there to Coxeter, 1939) and a general perturbation bound for how the eigengap changes under left orthogonal actions. These general statements determine the spectrum implicitly for a specified row matrix, but do not state the explicit two-class cycle ordering, the strict universal preference or its limiting \(2/\sqrt3\) ratio. Dax's 2022 discussion of projection-based Kaczmarz order selection has a distinct, non-reflective iteration and rate criterion. The current result isolates the exact permutation optimum for the natural four-cycle Gram geometry, not a general theory for all Gram matrices.

## Limitations

The result is limited to four rows with equal positive nearest-neighbor correlations and exactly zero opposite-row correlations. It does not compare all possible matrix geometries, random row orders, projection Kaczmarz, fixed-window actual errors or runtime. In particular, oscillatory numerator factors in the exact finite-epoch averaging norm can reverse the comparison for a given finite \(N\); the theorem only orders the eigengap and the uniform bound. The source-level priority assessment is not an independent exhaustive historical review, especially concerning older reflection-product spectral literature.

## References

1. Changpeng Shao, *A deterministic Kaczmarz algorithm for solving linear systems*, arXiv:2105.07736 (first public version, 17 May 2021), https://arxiv.org/abs/2105.07736 ; SIAM Journal on Matrix Analysis and Applications 44 (2023), 212–239, https://doi.org/10.1137/21M1463306 .
2. Changpeng Shao, *Reflective block Kaczmarz algorithms for least squares*, arXiv:2407.19226 (27 July 2024), https://arxiv.org/abs/2407.19226 .
3. Achiya Dax, *Kaczmarz Anomaly in Tomography Problems*, AppliedMath 2 (2022), 196–211, https://doi.org/10.3390/appliedmath2020012 .
