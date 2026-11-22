# Critical multichannel sampling across irregular and nearly colliding spectral clusters

## Finding
An infinite diagonal positive contraction can possess clusters of up to \(r\) eigenmodes with arbitrarily small internal spectral gaps, yet admit a **Riesz basis of weighted observations at exactly one time per cluster using \(r\) sensors**. This conclusion persists under independently varying, uniformly invertible complex sensor-mixing matrices. The cluster times may have arbitrarily large gaps. An explicit quantitative separation test simultaneously guarantees that the *original, unthinned integer-time multichannel observation family* is a frame and that the critical-count real-time observation family is a Riesz basis.

The theorem is constructive, provides stated frame bounds, and achieves the factor \(1/r\) of the eigenmode counting function up to an additive constant. No general assertion for arbitrary positive operators, arbitrary cluster separation, or prescribed integer sample times is made.

## Assumptions and scope
Fix \(r\in\mathbb N\) with \(r\ge 2\), numbers \(0<m\le M\), \(d\ge 0\), and \(L>2d\). Let \((x_k)_{k\ge0}\) be real numbers with \(x_0\ge d\) and \(x_{k+1}-x_k\ge L\), with no upper bound on these gaps. For every \(k\), choose \(\delta_{k,\sigma}\in[-d,d]\), \(1\le\sigma\le r\), and \(U_k\in\mathbb C^{r\times r}\) satisfying
\[
\sigma_{\min}(U_k)\ge m,\qquad\|U_k\|\le M.
\]
No commutativity or convergence is imposed on the matrices \(U_k\). Put \(s_{k,\sigma}=\exp(-x_k-\delta_{k,\sigma})\) and \(\lambda_{k,\sigma}=\exp(-s_{k,\sigma})\). On \(H=\ell^2(\mathbb N_0;\mathbb C^r)\), define \(Ae_{k,\sigma}=\lambda_{k,\sigma}e_{k,\sigma}\) and the bounded sensor \(C:H\to\mathbb C^r\) by
\[
Ce_{k,\sigma}=\sqrt{s_{k,\sigma}}\,U_ke_\sigma.
\]
For \(A^t\), use the positive-operator continuous functional calculus. Define
\[
\phi(u)=\exp\bigl(u/2-e^u\bigr),\quad a_d=\min_{|u|\le d}\phi(u),\quad q=e^{-L/2},\quad c_0=\frac{2}{1-e^{-2}},
\]
\[
\varepsilon=\frac{2M e^{d/2}q}{1-q},\qquad
\eta=\frac{2rM^2c_0e^dq}{1-q}.
\]
Assume \(\varepsilon<ma_d\) and \(\eta<m^2/2\). Both conditions hold for all sufficiently large \(L\), with \(r,m,M,d\) fixed. Set \(t_k=e^{x_k}\) and choose the positive weights \(w_k=t_k\).

**Theorem.** For every \(v\in H\), the integer-time multichannel frame satisfies
\[
\left(\frac{m^2}{2}-\eta\right)\|v\|^2
\le\sum_{n=0}^\infty\|CA^nv\|_{\mathbb C^r}^2
\le\left(\frac{M^2}{1-e^{-2}}+\eta\right)\|v\|^2.
\]
The weighted real-time analysis map
\[
Bv=\left(\sqrt{t_j}\,CA^{t_j}v\right)_{j\ge0}
\]
is a bounded isomorphism from \(H\) onto \(\ell^2(\mathbb N_0;\mathbb C^r)\), with
\[
(ma_d-\varepsilon)\|v\|\le\|Bv\|\le
\left(\frac{M}{\sqrt{2e}}+\varepsilon\right)\|v\|.
\]
Consequently the scalar coordinate observations comprising \(B\) constitute a Riesz basis of analysis vectors. Define \(n_A(R)=\#\{(k,\sigma):s_{k,\sigma}\ge 1/R\}\) and \(N_T(R)=\#\{k:t_k\le R\}\). For every \(R>0\),
\[
|n_A(R)-rN_T(R)|\le r;
\qquad N_T(R)=\frac{n_A(R)}r+O(1).
\]
In particular, as \(R\to\infty\) the counting ratio tends to \(1/r\).

## Proof
**1. Bounded sensor and positive evolution.** Since \(x_k\ge d+kL\) and \(|\delta_{k,\sigma}|\le d\), one has \(0<s_{k,\sigma}\le e^{-kL}\). The sum of their values converges; \(\sum_{k,\sigma}\|Ce_{k,\sigma}\|^2\le M^2r/(1-e^{-L})\), so \(C\) is Hilbert--Schmidt. The contraction \(A\) is positive self-adjoint, and \(A^te_{k,\sigma}=e^{-ts_{k,\sigma}}e_{k,\sigma}\) for every \(t\ge0\).

**2. Weighted sampling and surjectivity.** View \(B\) as a matrix of \(r\)-by-\(r\) blocks. The entry in its \((j,k)\)-block, acting on coordinate \(\sigma\), is
\[
\sqrt{t_j}\sqrt{s_{k,\sigma}}e^{-t_js_{k,\sigma}}
=\phi(x_j-x_k-\delta_{k,\sigma}).
\]
Thus \(B_{jk}=U_k\operatorname{diag}_\sigma\phi(x_j-x_k-\delta_{k,\sigma})\). On the diagonal, \(\sigma_{\min}(B_{kk})\ge ma_d\); also \(\|B_{kk}\|\le M/\sqrt{2e}\) because \(\max_u\phi(u)=1/\sqrt{2e}\). For all real \(u\), \(0<\phi(u)\le e^{-|u|/2}\). Therefore, if \(j\ne k\),
\[
\|B_{jk}\|\le Me^{d/2}e^{-L|j-k|/2}.
\]
The block Schur test bounds the strictly off-diagonal operator by \(\varepsilon=2Me^{d/2}q/(1-q)\). The diagonal block operator is boundedly invertible with inverse norm at most \(1/(ma_d)\). Since \(\varepsilon<ma_d\), a Neumann-series argument makes the full \(B\) invertible and gives the two stated singular-value bounds. This uses no uniform upper bound on \(x_{k+1}-x_k\).

**3. Stability of the original integer orbit.** Let \(G\) be the Gram matrix of the integer-time observation operator. Its entries are absolutely convergent and given exactly by
\[
G_{k\sigma,\ell\tau}=
\frac{\sqrt{s_{k,\sigma}s_{\ell,\tau}}\,
\langle U_ke_\sigma,U_\ell e_\tau\rangle}
{1-e^{-(s_{k,\sigma}+s_{\ell,\tau})}}.
\]
For a fixed cluster \(k\), the associated diagonal Gram block is the sum of positive matrices \(D_{k,n}U_k^*U_kD_{k,n}\), with \(D_{k,n}=\operatorname{diag}_\sigma(\sqrt{s_{k,\sigma}}e^{-ns_{k,\sigma}})\). Its quadratic form lies between \(m^2\sum_\sigma|v_\sigma|^2s_{k,\sigma}/(1-e^{-2s_{k,\sigma}})\) and the analogous upper bound with \(M^2\). Since \(0<s\le1\),
\[
\frac12\le\frac{s}{1-e^{-2s}}\le\frac1{1-e^{-2}}.
\]
Hence the block-diagonal part of \(G\) is bounded below by \(m^2/2\) and above by \(M^2/(1-e^{-2})\).

For distinct clusters, use the elementary inequalities, valid for \(0<a,b\le1\),
\[
\frac{1}{1-e^{-(a+b)}}\le\frac{c_0}{a+b},\qquad
\frac{\sqrt{ab}}{a+b}\le\sqrt{\frac{\min(a,b)}{\max(a,b)}}.
\]
By separation of the logarithmic centers, the latter square root is at most \(e^dq^{|k-\ell|}\). Every off-cluster Gram entry is therefore at most \(M^2c_0e^dq^{|k-\ell|}\) in absolute value, and the norm of each off-cluster \(r\)-by-\(r\) block is at most \(r\) times this. A second block Schur test bounds their total operator norm by \(\eta\). The stated integer-orbit inequalities follow, as does convergence of the analysis series for every \(v\).

**4. Exact counting.** Write \(y=\log R\). Then \(n_A(R)\) counts coordinates with \(x_k+\delta_{k,\sigma}\le y\), whereas \(N_T(R)\) counts centers with \(x_k\le y\). Outside the disjoint intervals \([x_k-d,x_k+d]\), these counts agree after multiplying the latter by \(r\). Inside at most one such interval, the discrepancy is bounded by \(r\). This proves the uniform additive error and hence the limiting factor \(1/r\).

## Verification
The proof is infinite-dimensional and analytic. For a reproducible finite-section check, run `python check_clustered_sampling.py` with NumPy installed. The script constructs independently varying orthogonal sensor matrices, distinct randomly perturbed decay scales, and compares (i) the singular values of the sampled block matrix, (ii) the exact *infinite-time* integer-orbit Gram summed in closed form, and (iii) the counting discrepancy. It performs 27 combinations with \(r\in\{2,3,4\}\), cluster counts \(3,6,9\), and three reproducible random seeds, and prints `CLUSTERED_CRITICAL_MULTICHANNEL_OK 27` on success. This is a diagnostic, not a computer proof of the theorem.

For example, with \(m=M=1\), \(d=1/4\), and \(L=12\), the separation conditions hold for each \(r\in\{2,3,4\}\): \(a_d\approx0.31379185\), \(\varepsilon\approx0.00563155\), and \(\eta\le0.05904143<1/2\). Arbitrary deterministic or random choices of the bounded offsets and invertible mixing matrices are included in the theorem, not just those tested.

## Relationship to prior work
J. Wu, *Optimal weighted sampling of positive and normal operator orbits* (arXiv:2610.31278v1, 22 October 2026), proves general lower counting constraints and sparse frame preservation. Its Proposition 4.6 supplies the spectral counting obstruction for finitely many sensors; the single-orbit and separated-spectral settings do not provide this theorem's explicit one-time-per-cluster **multichannel Riesz basis** with varying matrix-valued sensors and nearly colliding eigenvalues. The factor \(1/r\) as a general lower-bound target is accordingly **not** claimed to be newly discovered.

Cabrelli, Molter, Paternostro and Philipp, *Dynamical sampling on finite index sets* (2017 preprint, later journal publication), Theorem 2.3, gives an abstract characterization for finite collections of *all* nonnegative integer-time orbits; it does not classify the nonuniform weighted real-time critical-count design here.

Krishtal and Wu, *Totally Positive Interpolation and Critical Sampling of Positive Operator Orbits* (arXiv:2611.20122v1, first public 15 November 2026), Theorem 3.4, constructs critical-count sampled Riesz bases for a **single observation direction**. It is a related comparison rather than a source of this result; no multichannel clustered theorem is asserted from it. Its release is later than the motivating October preprint.

## Limitations
The sufficient condition forces **large enough intercluster gaps**. No necessity, optimal separation constant, arbitrary positive-operator generalization, or robustness against time-sampling jitter is established. Critical counting is established for this explicit family, not for all finite-sensor frames. Individual eigenvalues may merge within clusters; if one wishes them distinct, choose pairwise distinct offsets. The result does not imply that integer sample times admit the same exact-count Riesz basis. Older literature on vector-valued interpolation or clustered Carleson frames might contain a more general theorem implying this result; that remains a bibliographic risk. No independent external mathematical audit has been performed.

## References
1. J. Wu, *Optimal weighted sampling of positive and normal operator orbits*, arXiv:2610.31278v1 (first posted 2026-10-22). https://arxiv.org/abs/2610.31278 . Full preprint available at https://borowiecki.dev/pdf/2610.31278 .
2. C. Cabrelli, U. Molter, V. Paternostro, F. M. Philipp, *Dynamical sampling on finite index sets*, arXiv:1702.03384 (2017), especially Theorem 2.3. https://arxiv.org/abs/1702.03384 .
3. I. A. Krishtal and J. Wu, *Totally Positive Interpolation and Critical Sampling of Positive Operator Orbits*, arXiv:2611.20122v1 (first posted 2026-11-15), especially Theorem 3.4. https://arxiv.org/abs/2611.20122 .
