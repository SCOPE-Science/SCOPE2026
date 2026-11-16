# A sharp angular Weyl law for coordinate Hankel operators on radial power Fock spaces

## Finding

For each integer \(d\ge2\) and real \(p>1\), the coordinate big Hankel operator on the radial power Fock space has a sharp, explicitly computable singular-value counting law. Put
\[
\delta=1-\frac1p,\qquad s_*=\frac{2d}{\delta}=\frac{2dp}{p-1}.
\]
For its singular values, arranged in nonincreasing order with multiplicity,
\[
\lim_{t\downarrow0}t^{s_*}\#\{n:s_n(H)>t\}=C_{d,p},\qquad
C_{d,p}=\frac{p^{-d/(p-1)}}{d(d-2)!}
\int_0^1(1-u)^{d-2}(1-\delta u)^{d/\delta}\,du.
\]
In particular, \(s_n(H)\sim (C_{d,p}/n)^{1/s_*}\). The critical power has the exact logarithmic spectral residue
\[
\lim_{M\to\infty}\frac1{\log M}\sum_{n=1}^{M}s_n(H)^{s_*}=C_{d,p}.
\]
The angular dependence is essential: the limiting squared singular-value profile across monomials of total degree \(k\) is \(p^{-1/p}(1-\delta u)\), with \(u\) the proportion of degree in the selected coordinate. For the first nontrivial quartic example \(d=p=2\),
\[
\boxed{\ C_{2,2}=\frac{31}{640}\ }.
\]
The exact compactness and Schatten-membership classification was previously established by Bommier-Hato and Youssfi [3]; the precise coefficient, its angular dependence, and the critical logarithmic residue are the distinct assertions here.

## Assumptions and scope

Let \(d\ge2\) and \(p>1\), and write \(|z|=(\sum_{i=1}^d|z_i|^2)^{1/2}\). The analytic Hilbert space \(\mathcal F_{d,p}\) comprises all entire functions with finite norm
\[
\|f\|_{d,p}^{2}=\int_{\mathbb C^d}|f(z)|^2e^{-|z|^{2p}}\,dV(z).
\]
Here \(dV\) is ordinary \(2d\)-dimensional Lebesgue measure and \(P\) is orthogonal projection of the weighted \(L^2\)-space onto \(\mathcal F_{d,p}\). Define the scalar big Hankel map on holomorphic polynomials by
\[
Hf=(I-P)(\overline z_1f).
\]
For \(\alpha\in\mathbb N_0^d\), put \(k=|\alpha|\), \(j=\alpha_1\), and use the normalized monomial \(e_\alpha=z^\alpha/\|z^\alpha\|_{d,p}\). The convention is that every nonzero singular value is counted with its Hilbert-space multiplicity. Define, for integers \(\ell\ge1\),
\[
r_\ell=\frac{\Gamma((\ell+d)/p)}{(\ell+d-1)\Gamma((\ell+d-1)/p)}.
\]
No assertion is made at \(p=1\): the Gaussian case has constant nonzero singular values and is not compact. Only the explicit radial weight above, one coordinate symbol, and \(p>1\) are covered.

## Proof

**1. Exact monomial norms and orthogonality.** The radial/angular decomposition and sphere Dirichlet integral give, for every \(\alpha\) with \(k=|\alpha|\),
\[
I_\alpha:=\|z^\alpha\|_{d,p}^{2}
=\frac{\pi^d}{p}\,\frac{\alpha!}{\Gamma(k+d)}\,
\Gamma\!\left(\frac{k+d}{p}\right).
\]
Multiplication by \(\overline z_1\) changes the torus weight of \(z^\alpha\) to \(\alpha-e_1\). Consequently its analytic projection vanishes when \(j=0\), and when \(j\ge1\) it is precisely
\[
P(\overline z_1 z^\alpha)=\frac{I_\alpha}{I_{\alpha-e_1}}z^{\alpha-e_1}.
\]
It follows, by the Pythagorean theorem, that the squared norm of \(He_\alpha\) is
\[
\|He_\alpha\|^{2}=
\frac{I_{\alpha+e_1}}{I_\alpha}
-\mathbf 1_{j>0}\frac{I_\alpha}{I_{\alpha-e_1}}
=(j+1)r_{k+1}-jr_k.
\]
The torus weights \(\alpha-e_1\) are pairwise different as \(\alpha\) varies, so **all distinct images \(He_\alpha\) are orthogonal in the target weighted \(L^2\)-space**, not merely images in different homogeneous degrees. This proves that the displayed nonnegative numbers are exactly the squared singular values, including multiplicity. For a given \(k,j\), the number of nonnegative integer choices for the other \(d-1\) coordinates is
\[
\binom{k-j+d-2}{d-2}.
\]
The \(k=0\) term has \(j=0\) and squared singular value \(r_1\).

**2. Uniform angular asymptotics.** Standard gamma-ratio asymptotics, with a first remainder estimate, yield for fixed \(d,p\)
\[
r_k=p^{-1/p}k^{-\delta}\bigl(1+B_{d,p}/k+O(k^{-2})\bigr),\qquad
r_{k+1}-r_k=-\delta p^{-1/p}k^{-\delta-1}\bigl(1+O(k^{-1})\bigr).
\]
There is no need to calculate the auxiliary constant \(B_{d,p}\). Substitute into the exact identity
\[
\sigma_{k,j}^{2}=r_{k+1}+j(r_{k+1}-r_k),
\]
and use \(0\le j\le k\). Both errors are uniform in that range, giving
\[
\sigma_{k,j}^{2}=p^{-1/p}k^{-\delta}
\left(1-\delta\frac{j}{k}+O(k^{-1})\right).
\]
Since \(1-\delta j/k\ge1-\delta=1/p>0\), the asymptotic is uniformly relative. Hence all squared singular values approach zero as \(k\to\infty\); the bounded extension of \(H\) is compact. If \(j/k\to u\), then
\[
k^{\delta/2}\sigma_{k,j}\longrightarrow
p^{-1/(2p)}\sqrt{1-\delta u},\qquad 0\le u\le1.
\]
The limiting ratio of largest to smallest singular values within a high homogeneous degree is \(\sqrt p\).

**3. Counting as a lattice-volume problem.** Let \(L=t^{-2/\delta}\). The uniform estimate from Step 2 turns the inequality \(\sigma_{k,j}>t\), outside a fixed number of low degrees, into
\[
\frac{k}{L}<\Bigl[p^{-1/p}(1-\delta u)\Bigr]^{1/\delta}+o(1),
\qquad u=j/k.
\]
The error in the cutoff is uniform over \(u\in[0,1]\), on compact subsets of positive rescaled degree. There is a uniform upper cutoff \(k\le K L\) for all counted large-degree terms, for some fixed \(K\). The finitely many low degrees and the region \(k/L\le\eta\) contribute at most \(O((\eta L)^d)=O(\eta^d L^d)\). Thus it suffices to take a Riemann-sum limit and then let \(\eta\downarrow0\). The multiplicity in Step 1 is a polynomial of degree \(d-2\); after summing over \(j\) its limiting density at \(j/k=u\) is
\[
\frac{k^{d-1}}{(d-2)!}(1-u)^{d-2}\,dk\,du.
\]
Integrating first in the total-degree variable, with upper limit
\(p^{-1/(p\delta)}(1-\delta u)^{1/\delta}L\), produces
\[
\lim_{t\downarrow0}t^{2d/\delta}N(t)
=\frac1{d(d-2)!}\int_0^1(1-u)^{d-2}
\left[p^{-1/p}(1-\delta u)\right]^{d/\delta}\,du.
\]
Since \(p\delta=p-1\), this is precisely \(C_{d,p}\) claimed above. The boundary of the limiting lattice domain has zero Lebesgue measure, and the strict versus non-strict threshold choice does not alter the leading volume.

**4. Ordered singular values and the critical logarithm.** The positive finite constant \(C_{d,p}\) and the monotone rearrangement theorem for counting functions yield
\[
s_n(H)\sim(C_{d,p}/n)^{\delta/(2d)}.
\]
At \(s_*=2d/\delta\) this implies \(s_n(H)^{s_*}\sim C_{d,p}/n\). Therefore
\[
\sum_{n=1}^M s_n(H)^{s_*}=C_{d,p}\log M+o(\log M).
\]
The same ordered asymptotic gives \(H\in\mathcal S_q\) precisely for \(q>s_*\). This last membership criterion is a known consequence of the earlier classification [3], and it is listed here solely to place the sharp spectral constants in context.

**5. Exact quartic example.** Set \(d=2\), \(p=2\). Then \(\delta=1/2\), \(s_*=8\), and
\[
C_{2,2}=\frac18\int_0^1(1-u/2)^4\,du
=\frac18\cdot\frac{31}{80}=\frac{31}{640}.
\]
This rational coefficient is not a numerical fit.

## Verification

The accompanying executable file `verification/verify_hankel.py` checks the gamma-ratio spectral identity and positivity for a range of degrees and parameters, the degreewise asymptotic at the two endpoints and intermediate angles, and the exact rational evaluation \(C_{2,2}=31/640\). It also evaluates finite counting functions at decreasing thresholds for that quartic example. The code uses Python, SciPy, and standard-library exact rational arithmetic. Its finite checks supplement the analytic derivation above; finite truncation alone cannot establish the infinite-dimensional theorem. No machine-assisted infinite proof is claimed.

## Relationship to prior work

Liu, Wang, and Zeng [1] give a September 2026 general Bergman-kernel and Hankel boundedness/compactness framework on weighted Fock spaces in several variables. Their stated results do not directly supply an exact coordinate-Hankel Weyl coefficient. Haslinger and Lamel [2] already gave a general moment-based diagonalization and Schatten criteria for the canonical \(\overline\partial\)-solution operator on analytic-coefficient forms. The monomial reduction in Step 1 is consistent with, and elementary in relation to, that earlier moment framework; **the exact monomial formula is not by itself claimed as an independent discovery**. Bommier-Hato and Youssfi [3] established the strong/compact/Schatten classification for anti-holomorphic symbols on precisely these power-weighted Fock spaces. Their criterion already implies the exponent \(s_*\), so this theorem's separate contribution is the exact coefficient and angular distribution, not the threshold. Bommier-Hato and Constantin [4] extend qualitative spectral-ideal criteria; Fan, Wang, and Zeng [5] discuss general singular-value asymptotics via function rearrangements. The older Stieltjes-moment work [6] is an additional potentially close source.

The novelty assessment rests on comparing the **exact coefficient, the uniform angular profile, and the logarithmic residue** against the inspected statements, rather than simply different titles or notation. It is provisional pending broader full-text comparison of older related articles.

## Limitations

The theorem applies to the isotropic radial weight \(e^{-|z|^{2p}}\), integer \(d\ge2\), \(p>1\), and a single coordinate anti-holomorphic symbol only. It does not classify arbitrary anti-holomorphic symbols or variable-Hessian weights, nor determine higher-order terms in the Weyl law. The previously established Schatten membership threshold is explicitly excluded from the novel claim. The closest 2007 and 2010 articles were not available for complete full-text inspection; the resulting residual bibliographic risk is material. No independent mathematical audit has been performed.

## References

[1] G. Liu, X. Wang, and Z. Zeng, *Bergman Kernels and Hankel Operators on Weighted Fock Spaces in Several Complex Variables*, arXiv:2609.26810v1, publicly posted 16 September 2026. https://arxiv.org/abs/2609.26810v1

[2] F. Haslinger and B. Lamel, *Spectral properties of the canonical solution operator to dbar*, arXiv:math/0612352, 2006. https://arxiv.org/abs/math/0612352

[3] H. Bommier-Hato and E.-H. Youssfi, *Hankel operators on weighted Fock spaces*, Integral Equations and Operator Theory 59 (2007), 1–17. https://doi.org/10.1007/s00020-007-1513-1

[4] H. Bommier-Hato and O. Constantin, *Big Hankel Operators on Vector-Valued Fock Spaces in C-d*, Integral Equations and Operator Theory 90 (2018), article 2. https://doi.org/10.1007/s00020-018-2433-y

[5] Z. Fan, X. Wang, and Z. Zeng, *IDA function and asymptotic behavior of singular values of Hankel operators on weighted Bergman spaces*, arXiv:2410.20082v1. https://arxiv.org/abs/2410.20082v1

[6] H. Bommier-Hato and E.-H. Youssfi, *Hankel operators and the Stieltjes moment problem*, Journal of Functional Analysis 258 (2010), 978–998. https://doi.org/10.1016/j.jfa.2009.08.004
