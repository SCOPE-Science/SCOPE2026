# Sharp stability of three-site Gabor tomography on the five-cycle

## Finding
Let \(G=\mathbb Z/5\mathbb Z\), let \(g\in\mathbb C^G\) have norm one, and require \(g\) to have **exactly three nonzero entries**. Define cyclic translations and modulations by
\[
(T_k g)(j)=g(j-k),\qquad (M_\ell g)(j)=e^{2\pi i\ell j/5}g(j),
\]
and define the intensity-lifting map on complex matrices, with Hilbert--Schmidt and Euclidean norms, by
\[
\mathcal L_g(H)=\bigl(\operatorname{tr}(H (M_\ell T_k g)(M_\ell T_k g)^*)\bigr)_{k,\ell\in G}.
\]
Write \(\kappa(\mathcal L_g)=\sigma_{\max}/\sigma_{\min}\), taking \(\kappa=+\infty\) if the map is singular. Then the **sharp global optimum over all three-site unit-norm windows** is
\[
\boxed{\min_{\lvert\operatorname{supp}g\rvert=3}\kappa(\mathcal L_g)
=\frac{5+\sqrt5}{2}.}
\]
The optimal least singular value is \(\sqrt5\,(5-\sqrt5)/10\), whereas the largest singular value is always \(\sqrt5\).

Here is the complete equality class. Every three-element support is a three-term arithmetic progression \(\{a,a+d,a+2d\}\) in \(G\), where \(d\ne0\). Put
\[
\alpha=\frac{5-\sqrt5}{10},\qquad \Delta=(1-\alpha)^2-4\alpha^2=\frac{5\sqrt5-9}{10}.
\]
The optimum holds if and only if, with \(u=|g(a)|\), \(v=|g(a+d)|\), \(w=|g(a+2d)|\),
\[
\boxed{
 v^2=uw=\alpha,\qquad
 \{u^2,w^2\}=\left\{\frac{1-\alpha+\sqrt\Delta}{2},
 \frac{1-\alpha-\sqrt\Delta}{2}\right\},\qquad
 \frac{g(a)g(a+2d)}{g(a+d)^2}\in\{e^{2\pi i m/5}:m=0,1,2,3,4\}.
}
\]
All such optimizers are informationally complete: their intensity measurements determine every Hermitian matrix and therefore the rank-one matrix \(ff^*\), hence any vector \(f\) up to one global phase.

Three sites are the **minimum support size** for informational completeness on the five-cycle. For comparison, any window supported on three *consecutive* sites on a cyclic group of order \(N\ge6\) has singular full Gabor intensity lifting because its support-difference set omits at least one nonzero delay. The last statement concerns consecutive sites only, not arbitrary three-site patterns.

## Assumptions and scope
All weights are complex, none of the three supported entries is zero, and \(\|g\|_2=1\). All \(25\) cyclic time-frequency shifts are used. The condition number is that of the **linear intensity lifting on all complex \(5\times5\) matrices**, not the nonlinear modulus measurement map restricted to rank-one matrices. The Hilbert--Schmidt norm on the domain and ordinary Euclidean norm on \(\mathbb C^{25}\) fix the singular-value normalization. The same nonzero singular values occur on the real Hilbert space of Hermitian matrices. Affine relabelings of \(G\) preserve the measurement singular spectrum.

## Proof
**1. Weyl diagonalization.** Define the ambiguity coefficients
\[
 A_g(k,\ell)=\sum_{j\in G}g(j)\overline{g(j-k)}e^{-2\pi i j\ell/5}.
\]
The \(25\) Weyl matrices \(M_\ell T_k/\sqrt5\) form an orthonormal Hilbert--Schmidt basis. Conjugation by a time-frequency shift multiplies every Weyl coefficient by a character. Taking the two-dimensional discrete Fourier transform of the \(25\) output coordinates consequently diagonalizes \(\mathcal L_g\). Its singular values, with multiplicities, are exactly
\[
\{\sqrt5\,|A_g(k,\ell)|:(k,\ell)\in G^2\}.
\]
Since \(A_g(0,0)=1\) and \(|A_g(k,\ell)|\le1\), the maximum singular value equals \(\sqrt5\). Thus minimizing the condition number is equivalent to maximizing \(\mu(g)=\min_{k,\ell}|A_g(k,\ell)|\).

**2. Reduce every support to a progression.** Complements of three-element sets in \(G\) are two-element sets, and every two-element set is affine-equivalent to every other. Hence any three-site support is affine-equivalent to \(\{0,1,2\}\). Such relabeling permutes the Weyl indices and preserves the multiset of ambiguity moduli. It suffices to write
\[
 g=(u e^{i\theta_0},v e^{i\theta_1},w e^{i\theta_2},0,0),\quad
 u,v,w>0,\quad u^2+v^2+w^2=1.
\]
The delay \(k=2\) has one overlap, so \(|A_g(2,\ell)|=uw\) for all \(\ell\). At delay \(k=1\) there are two overlaps, and, after removing an irrelevant unit phase,
\[
 |A_g(1,\ell)|=v\left|u+w e^{i\delta}e^{-2\pi i\ell/5}\right|,
 \qquad\delta=\theta_2-2\theta_1+\theta_0.
\]

**3. Exact five-point phase covering.** The nearest of five equally spaced angles to the opposite phase \(\pi\) is within angular distance \(\pi/5\). Therefore, for any \(u,w>0\),
\[
 \min_{\ell}\left|u+w e^{i\delta}e^{-2\pi i\ell/5}\right|^2
 \le u^2+w^2-2uw\cos(\pi/5),
\]
with equality precisely when \(e^{i\delta}\) is a fifth root of unity. Set \(s=uw\), \(t=v^2\), and \(\varphi=2\cos(\pi/5)=(1+\sqrt5)/2\). It follows that
\[
\begin{aligned}
 \mu(g)&\le\min\{s,\sqrt{t(1-t-\varphi s)}\}\\
 &\le \min\{s,(1-\varphi s)/2\}\\
 &\le \frac{1}{2+\varphi}=\alpha.
\end{aligned}
\]
The middle inequality is the elementary completed-square bound \(t(1-\varphi s-t)\le(1-\varphi s)^2/4\). Equality in the final min-bound forces \(s=\alpha\). Equality in the middle bound then forces \(t=(1-\varphi\alpha)/2=\alpha\). Equality in phase covering forces \(e^{i\delta}\) to be a fifth root of unity. The norm constraint now gives \(u^2+w^2=1-\alpha\); solving the quadratic with product \(u^2w^2=\alpha^2\) produces precisely the two endpoint magnitudes stated above. The discriminant \(\Delta>0\) ensures both solutions are positive.

**4. No neglected ambiguity is smaller.** For these candidates, \(k=\pm2\) has modulus \(\alpha\), while the optimal five-point covering at \(k=\pm1\) has minimum exactly \(\alpha\). The only remaining case is \(k=0\). For \(z=e^{-2\pi i\ell/5}\), its modulus equals \(|u^2+\alpha z+w^2 z^2|\). Multiplication by \(z^{-1}\) and the relations in step 3 give
\[
 |A_g(0,\ell)|^2=
 [\alpha+(1-\alpha)\cos(2\pi\ell/5)]^2
 +\Delta\sin^2(2\pi\ell/5).
\]
For \(\ell=0\), \(\ell=\pm1\), and \(\ell=\pm2\), these squared values are, respectively,
\[
 1,\qquad \frac{\sqrt5}{5},\qquad
 \frac{3\sqrt5-5}{10}.
\]
Each is strictly larger than \(\alpha^2=(3-\sqrt5)/10\); in the final case the difference is \(2(\sqrt5-2)/5>0\). Consequently \(\mu(g)=\alpha\), and all upper-bound equality conditions are necessary and sufficient. The sharp condition number is \(1/\alpha=(5+\sqrt5)/2\).

**5. Minimal support and boundary.** Any window supported on at most two sites has \(|\operatorname{supp}(g)-\operatorname{supp}(g)|\le3<5\). For each missing delay, its entire ambiguity row vanishes, and the Weyl diagonalization makes \(\mathcal L_g\) singular. An optimal three-site window has \(\mu(g)=\alpha>0\) and is therefore informationally complete. If \(N\ge6\) and the support is a consecutive triple, its difference set is contained in \(\{0,\pm1,\pm2\}\), which has fewer than \(N\) elements; the same argument proves singularity. No statement about arbitrary nonconsecutive triples at larger orders is used.

## Verification
Run `python CHECK.py` after installing the dependency listed in `REQUIREMENTS.txt`. The checker independently forms all \(25\) Gabor rank-one projectors and their \(25\times25\) complex-linear lifting matrix, compares singular values with the ambiguity spectrum for random complex three-site windows, tests all equality families, tests the five-cycle support equivalences, and checks off-grid phases. Its passing output is `THREE_SITE_GABOR_CHECKS_PASSED 5259`.

These are finite floating-point cross-checks. The global optimum, classification, and impossibility statements are proved by steps 1--5 and do not rely on parameter sampling or numerical optimization.

## Relationship to prior work
The full time-frequency magnitude/ambiguity relation and its role in phase retrieval are standard; Bojarovska and Flinth (2015/2016) establish qualitative injectivity criteria. Bartusel (2023), especially Section 4.1, gives qualitative examples of nonvanishing-ambiguity exceptions and short-window injectivity results. Bartusel's May 2026 preprint develops broader sufficient zero-tolerance conditions. Their inspected statements concern uniqueness or sufficient conditions, not the present **globally optimal lifting condition number and complete arbitrary-complex-amplitude equality class** for minimum-support five-cycle windows. This work does not claim novelty for the Weyl diagonalization itself or for the general nonzero-ambiguity sufficiency criterion.

## Limitations
The exact optimization is specific to \(\mathbb Z/5\mathbb Z\), full 25-shift measurements, and three supported sites. The larger-order obstruction applies only to **consecutive** supports. The optimum for linear matrix tomography is not asserted to minimize the nonlinear phase-retrieval Lipschitz constant. Some related preprint full texts could not be inspected; an equivalent specialized finite-dimensional design computation may exist under a different indexing or normalization. Independent scientific review and publication-priority certification have not been performed.

## References
1. David Bartusel, *Uncertainty Principles as a Tool for STFT Phase Retrieval*, arXiv:2605.31507, first made public May 29, 2026, https://arxiv.org/abs/2605.31507.
2. David Bartusel, *Injectivity Conditions for STFT Phase Retrieval on Z, Zd and Rd*, Journal of Fourier Analysis and Applications 29 (2023), article 53, https://doi.org/10.1007/s00041-023-10026-2.
3. Irena Bojarovska and Axel Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800, https://arxiv.org/abs/1503.05800; Journal of Fourier Analysis and Applications 22 (2016), 542--567.
