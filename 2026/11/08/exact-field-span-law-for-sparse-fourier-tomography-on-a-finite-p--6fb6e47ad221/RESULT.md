# Exact field-span law for sparse Fourier tomography on a finite parabola

## Finding
Let \(F=\mathbb F_{p^m}\), where \(p\) is an odd prime and \(m\ge1\). Fix a nontrivial additive character \(\psi:F\to\mathbb C\). For a nonempty set of offsets \(C\subset F\), define the complete nonhorizontal line-view measurement map
\[
(\mathcal M_C f)(c,s)=\sum_{t\in F}f(t)\psi\big(s(t^2-ct)\big),\qquad (c,s)\in C\times F.
\]
Equivalently, these are the ambient Fourier samples of a function supported on the parabola \(P=\{(t,t^2):t\in F\}\), at the frequency lines \(L_c=\{(-cs,s):s\in F\}\). Put
\[
H_C=\operatorname{span}_{\mathbb F_p}\{c-c_0:c\in C\},\qquad h=|H_C|,
\]
where \(c_0\) is any point of \(C\). Then the **exact complex-linear nullity** and rank are
\[
\boxed{\dim\ker\mathcal M_C=\frac{q/h-1}{2},\qquad
\operatorname{rank}\mathcal M_C=q-\frac{q/h-1}{2},\quad q=p^m.}
\]
When \(h<q\), the **minimum support size of a nonzero null vector** is exactly \(2h\). Thus \(\mathcal M_C\) uniquely identifies every signal with at most \(k\) nonzero values if and only if \(k<h\); for \(k\ge h\) there are distinct \(h\)-sparse signals with identical data. When \(h=q\), the map is injective on all signals.

Consequently, the smallest number of distinct complete nonhorizontal frequency-line views giving injectivity on all complex signals is \(m+1\); equality holds exactly when the offsets form an affine \(\mathbb F_p\)-basis of \(F\). Such a design has \(1+(q-1)(m+1)\) distinct scalar Fourier samples (the origin is shared by all lines).

## Assumptions and scope
The field has odd characteristic. Every view contains all \(q\) frequencies on its designated line through the origin. Reconstruction is complex-linear with exact data, not phase retrieval. The horizontal frequency line \(\{(u,0):u\in F\}\), which already forms a Fourier basis on the parabola, is intentionally excluded. The stated minimum counts complete nonhorizontal line views, not arbitrary individual Fourier samples.

The support claim uses the usual number of nonzero coordinates of \(f:F\to\mathbb C\). The offsets are distinct and \(C\ne\varnothing\); repeated measurements do not change the conclusions.

## Proof
**Fourier-line inversion.** For a fixed offset \(c\), invert the full Fourier transform in the variable \(s\in F\). It recovers, for every \(y\in F\), the fiber sum
\[
F_c(y)=\sum_{t:t^2-ct=y}f(t).
\]
The fibers of \(t\mapsto t^2-ct\) are singletons at \(t=c/2\), unordered pairs \(\{t,c-t\}\) elsewhere, or empty. It follows, including at the fixed point, that
\[
\mathcal M_{\{c\}}f=0\quad\Longleftrightarrow\quad f(c-t)=-f(t)\quad\text{for every }t\in F.
\]

**Translation invariance.** Write \(r_c(t)=c-t\). If \(f\) is odd under all \(r_c\) with \(c\in C\), it is invariant under each product \(r_c r_{c_0}\), which is translation by \(c-c_0\). Since the additive group of \(F\) has exponent \(p\), it is invariant under translations by the whole subspace \(H_C\). Conversely, translation invariance under \(H_C\) and oddness under \(r_{c_0}\) imply oddness under every \(r_c\). Thus the kernel consists precisely of functions constant on \(H_C\)-cosets and odd under the induced reflection
\[
\bar t\longmapsto\overline{c_0}-\bar t
\quad\text{on }F/H_C.
\]

**Orbit count and a concrete basis.** The quotient has the odd cardinality \(Q=q/h\). Since doubling is bijective, the reflection has exactly one fixed coset, \(\overline{c_0/2}\), and \((Q-1)/2\) transposed pairs. A kernel function is zero at the fixed coset and is determined freely on one coset of each other pair, with the negative value on its partner. These orbit-pair indicator differences form a basis. This proves the nullity and rank formulas.

**Sharp support and uniform sparse recovery.** Each nonzero kernel function occupies at least one pair of different \(H_C\)-cosets, each of size \(h\); hence support is at least \(2h\). A single orbit-pair basis vector has exactly this support. If two signals are each supported on at most \(k\) points, their difference is supported on at most \(2k\). For \(k<h\), it cannot be a nonzero kernel vector. For \(k\ge h\) and \(h<q\), the two indicator functions of a transposed pair of cosets are distinct \(h\)-sparse signals with identical measurements. The case \(h=q\) has zero kernel, so all signals are identifiable.

**Optimal number of views.** The rank is full if and only if \(H_C=F\). A set of \(|C|\) offsets has affine span dimension at most \(|C|-1\) over \(\mathbb F_p\), and \(\dim_{\mathbb F_p}F=m\). Therefore \(|C|\ge m+1\) is necessary. For any basis \(u_1,\ldots,u_m\), the offsets \(\{c_0,c_0+u_1,\ldots,c_0+u_m\}\) attain it; at the minimum, affine independence is necessary. Different lines \(L_c\) share only the zero frequency, proving the distinct-sample count.

## Verification
`CHECK.py` is a standalone Python 3 program requiring only the standard library. It constructs exact integer fiber-sum matrices, independently constructs their complex Fourier counterparts, and compares both ranks with the formula for every nonempty offset set of size at most four in \(\mathbb F_3\), \(\mathbb F_5\), \(\mathbb F_7\), and \(\mathbb F_9\) (390 tested configurations). It additionally checks the sharp six-coordinate invisible support at a two-view configuration over \(\mathbb F_9\) by exact matrix ranks and an explicit colliding pair. Its floating-point Fourier checks supplement, but do not replace, the exact algebraic proof and exact rational incidence checks.

## Relationship to prior work
Fourier restriction and extension for finite-field paraboloids are studied by Lewko (2026), who proves bounds between function spaces rather than the exact rank of finite collections of complete frequency lines. The relation to finite Radon and X-ray transforms is standard: a complete Fourier line gives a family of projection sums. Feldman and Grinberg (2017) study projective X-ray transforms and minimal admissible complexes, on a different domain and measurement family. Closely related indexed work treats two-view Fourier tomography on finite-field *unit conics*, and coordinate-character Gram spectra on higher-dimensional paraboloids; neither inspected summary determines the parabolic reflection-translation nullspace law stated here. These comparisons do not establish that no unindexed equivalent result exists.

## Limitations
The theorem does not optimize arbitrary selections of scalar Fourier coefficients, permit the horizontal full Fourier line, or give noise-robust frame bounds. It does not cover fields of characteristic two. Exact Fourier line data are assumed. Published related work accessible only at record-summary level could contain relevant additional comparisons; independent mathematical validation has not been performed.

## References
1. M. Lewko, *A bilinear approach to the finite field restriction problem, II*, arXiv:2606.22882, first submitted 2026-06-22, https://arxiv.org/abs/2606.22882.
2. D. V. Feldman and E. L. Grinberg, *Admissible Complexes for the Projective X-Ray Transform over a Finite Field*, arXiv:1707.06695, https://arxiv.org/abs/1707.06695.
3. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, Duke Math. J. 121 (2004), 35–74. (General background on finite-field Fourier restriction.)
