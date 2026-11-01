# An exact anisotropic power-saving region for constant-weight polynomial character sums
## Finding
Let \(f\in\mathbb Z[X]\) be fixed of degree \(k\ge2\), let \(p\) be a large prime, let \(\chi\) be a nontrivial Dirichlet character modulo \(p\), and take \(\boldsymbol{\beta}\equiv\mathbf1\) in Theorem 1.1 of Fouvry--Shparlinski--Xi. Assume
\[
A=p^{a+o(1)},\qquad B=p^{b+o(1)},\qquad C=p^{c+o(1)}.
\]
with fixed \(a,b,c>0\), \(ka<1\), and \(b+c<1\). Set
\[
M=\max\{ka+b+c,2b+2c\},\qquad S=b+\min\{a,b\}+2c.
\]
Then there exists a fixed positive integer \(r\) for which the bound of Theorem 1.1 gives
\[
|\mathcal C_{f,\chi}(\boldsymbol{\alpha},\mathbf1)|\le ABCp^{-\delta}
\]
for some \(\delta>0\), uniformly for \(\|\boldsymbol{\alpha}\|_\infty\le1\), if and only if
\[
S>\frac12+\max\{M-1,0\}.
\]
This is an exact description of the anisotropic power-law region supplied by that theorem, not a claim that cancellation is impossible outside the region.

## Assumptions and scope
The source theorem assumes \(A^k\le\gamma_f p\), \(A\ge1/\gamma_f\), \(BC\le p/73\), and \(C>4p^{1/(2r)}\), where \(\gamma_f>0\) depends only on the fixed polynomial. The strict exponent assumptions \(ka<1\), \(b+c<1\), and \(c>0\) ensure these conditions for all sufficiently large \(p\) after choosing a sufficiently large fixed \(r\). The statement concerns only the constant-\(\mathbf1\) weight branch of Theorem 1.1 and only power-law scales with fixed positive exponents.

## Proof
Theorem 1.1 gives
\[
|\mathcal C_{f,\chi}(\boldsymbol{\alpha},\mathbf1)|\le ABCp^{o(1)}\Delta_1,
\]
where
\[
\Delta_1=(AB)^{-1/(2r)}C^{-1/r}p^{(r+1)/(4r^2)}
\left(\frac AB+1\right)^{1/(2r)}
\left(\frac{(A^k+BC)BC}{p^{1+1/(2r)}}+1\right)^{1/(2r)}.
\]
For fixed \(r\), insertion of the power laws gives \(\Delta_1=p^{-\zeta_r+o(1)}\), with
\[
2r\zeta_r
=S-\left(\frac12+\frac1{2r}\right)
-\max\left\{M-1-\frac1{2r},0\right\}.
\]
Indeed, the factor \(A/B+1\) contributes \(\max\{a-b,0\}/(2r)\), while \((A^k+BC)BC\) has exponent \(M=\max\{ka+b+c,2b+2c\}\). Also
\[
(a+b)-\max\{a-b,0\}=b+\min\{a,b\},
\]
which yields the displayed formula for \(S\).

Define
\[
H_r=\frac12+\frac1{2r}+\max\left\{M-1-\frac1{2r},0\right\},\qquad
H_\infty=\frac12+\max\{M-1,0\}.
\]
A three-case check according as \(M-1\le0\), \(0<M-1<1/(2r)\), or \(M-1\ge1/(2r)\) gives \(H_r\ge H_\infty\) for every \(r\), and \(H_r\to H_\infty\). Hence \(\zeta_r>0\) for some fixed \(r\) if and only if \(S>H_\infty\). Because \(c>0\), the same \(r\) can be chosen large enough that \(c>1/(2r)\), which enforces \(C>4p^{1/(2r)}\) for large \(p\). This proves the criterion.

On the diagonal \(a=b=c=\eta\), one has \(S=4\eta\) and \(M=(k+2)\eta\). The criterion becomes
\[
4\eta>\frac12+\max\{(k+2)\eta-1,0\},
\]
which is equivalent to \(\eta>1/8\) together with \((k-2)\eta<1/2\) when \(k>2\). Thus it reproduces Corollary 1.2 exactly. A genuinely anisotropic point is \(k=2\), \(a=1/20\), \(b=c=1/5\): here \(M=4/5\), \(S=13/20\), so the criterion holds although \(A\) is far shorter than \(p^{1/8}\).

## Verification
The accompanying `verify.py` recomputes the exponent of every factor in \(\Delta_1\) and checks the reduced formula over \(10935\) exact rational parameter/moment cases. It also checks \(550\) rational diagonal points against Corollary 1.2 and verifies the anisotropic example, including \(\zeta_4=1/320\). The replay output is stored in `verify_output.txt`.

These finite checks verify the algebraic reduction on many exact instances; the all-parameter result itself is established by the symbolic calculation and the three-case argument above.

## Relationship to prior work
Fouvry--Shparlinski--Xi state the full unequal-range bound in Theorem 1.1, but their extracted power-saving corollary and the proof in Section 3.3 specialize to \(A=B=C=p^{\eta+o(1)}\). The criterion above converts the full theorem into a complete three-exponent phase region and shows explicitly how one short range can be compensated by the other two.

Their preceding trilinear paper treats the linear-polynomial case and gives its own unequal-parameter sufficient regions; it does not state the degree-\(k\ge2\) polynomial criterion proved here. Its Remark 2.3 explicitly notes the difficulty of fully describing the parameter range of its different bound.

## Limitations
The criterion is exact only for the power saving furnished by the stated Theorem 1.1 bound after optimization over fixed \(r\). It does not assert an optimal cancellation threshold for the underlying character sums, and other methods may work outside this region. Boundary equality \(S=1/2+\max\{M-1,0\}\) is excluded because the source bound retains a \(p^{o(1)}\) factor. The strict assumptions \(ka<1\) and \(b+c<1\) avoid the constant-sensitive boundary of the source size hypotheses.

## References
Fouvry, E.; Shparlinski, I. E.; Xi, P., *Tridimensional character sums with polynomial arguments and applications*, arXiv:2610.01524v1, 2026. Theorem 1.1, Corollary 1.2, Sections 3.2--3.3.

Fouvry, E.; Shparlinski, I. E.; Xi, P., *Estimates for trilinear and quadrilinear character sums*, Revista Matematica Iberoamericana 41 (2025), 1925--1956, DOI:10.4171/RMI/1530. Theorem 2.1 and Remark 2.3.
