# Exactly \(d-1\) sign reversals in the opposite-corner inverse of a blended tensor-product finite-element mass matrix

## Finding

**Theorem.** Let \(d\ge2\) be an arbitrary integer and let \(E=\prod_{j=1}^{d}(0,h_j)\) with all \(h_j>0\). Use the \(2^d\) tensor-product, multilinear nodal basis functions on this single unassembled cell. Let \(M_C\) be the exact scalar consistent mass matrix, and let \(M_L\) be its diagonal row-sum lumping. For \(0\le\alpha\le1\) define \(M_\alpha=(1-\alpha)M_L+\alpha M_C\). Fix any opposite pair of vertices \(u,v\), and set \(G_d(\alpha)=(M_\alpha^{-1})_{uv}\).

Then \(M_\alpha\) is symmetric positive definite at every \(\alpha\in[0,1]\); nevertheless, \(G_d\) has **exactly \(d-1\) distinct, simple zeros** in \(0<\alpha<1\). At each zero its sign changes. Thus the opposite-corner coupling of the inverse undergoes arbitrarily many sign reversals as the tensor dimension increases, while positive definiteness is never lost.

All zeros are paired by the exact involution
\[
\alpha\longmapsto \frac{3^d(1-\alpha)}{\alpha+3^d(1-\alpha)}.
\]
For even \(d\), one zero is exactly \(\alpha=3^{d/2}/(1+3^{d/2})\). For \(d=3\), the two zeros are \(9/(13+\sqrt{13})\) and \(9/(13-\sqrt{13})\): the opposite-corner inverse entry is negative, then positive, then negative over the three consecutive open intervals.

## Assumptions and scope

The statement concerns the **exact scalar element-level inverse** of an unassembled multilinear element on a nondegenerate axis-aligned orthotope, with constant positive density. All physical edge lengths and density scale the inverse by a strictly positive factor; they do not change its signs or zero locations. There are no mesh-assembly, finite-precision, time-discretization, or global-preconditioner claims. The dimension \(d\) can exceed three as a mathematical tensor-product model; the three-dimensional illustration is a physical hexahedral case.

Write \(V=|E|\). The one-dimensional mass factor normalized by its diagonal lump is
\[
B=\frac13\begin{pmatrix}2&1\\1&2\end{pmatrix}.
\]
Therefore
\[
M_L=\frac{V}{2^d}I,\qquad M_C=\frac{V}{2^d}B^{\otimes d},\qquad
M_\alpha=\frac{V}{2^d}\bigl((1-\alpha)I+\alpha B^{\otimes d}\bigr).
\]
The eigenvalues of \(B\) are \(1\) and \(1/3\). Hence the normalized blended matrix has eigenvalues \(1-\alpha+\alpha3^{-k}>0\), \(k=0,\ldots,d\), with multiplicity \(\binom dk\), proving positive definiteness, including both endpoints.

## Proof

**1. Exact opposite-corner entry.** The tensor Walsh eigenbasis gives opposite-corner parity \((-1)^k\) to Walsh degree \(k\). Therefore for \(0<\alpha\le1\), putting \(t=(1-\alpha)/\alpha\),
\[
G_d(\alpha)=\frac{2^d}{V}\,\frac{1}{2^d\alpha}F_d(t)=\frac{F_d(t)}{V\alpha},\qquad
F_d(t)=\sum_{k=0}^{d}\frac{(-1)^k\binom dk}{t+3^{-k}}.
\]
The denominators are strictly positive for \(t>0\). Multiplying \(F_d(t)\) by \(D_d(t)=\prod_{k=0}^{d}(1+3^kt)\) gives a polynomial \(N_d(t)\) of degree exactly \(d-1\): the apparent degree-\(d\) coefficient cancels by \(\sum_k(-1)^k\binom dk=0\), whereas
\[
F_d(t)=-\frac{(2/3)^d}{t^2}+O(t^{-3})\quad(t\to\infty)
\]
shows that the degree-\(d-1\) coefficient is nonzero. Thus \(F_d\) has at most \(d-1\) positive zeros, counting multiplicities.

**2. A zero-count lower bound from moment orthogonality.** Let \(h=\log3\), \(f(x)=(1+e^x)^{-1}\), and
\[
S_d(x)=\sum_{k=0}^d(-1)^k\binom dk f(x+kh).
\]
An elementary rearrangement using \(3^k/(1+3^kt)=(1-1/(1+3^kt))/t\) shows
\[
F_d(t)=-t^{-1}S_d(\log t),\qquad t>0.
\]
The finite-difference integral identity gives
\[
S_d(x)=(-1)^d\int_{[0,h]^d} f^{(d)}(x+u_1+\cdots+u_d)\,du_1\cdots du_d.
\]
All derivatives \(f^{(r)}\) with \(r\ge1\) decay exponentially at both ends. Integration by parts, performed under this finite integral, therefore yields the **exact vanishing moments**
\[
\int_{\mathbb R}x^jS_d(x)\,dx=0,
\qquad j=0,1,\ldots,d-2.
\]
The function \(S_d\) is nonzero (since \(F_d\) has nonzero leading behavior above) and decays exponentially. If it had at most \(d-2\) sign changes, one could choose the polynomial whose simple real zeros are precisely those sign-change points (or a constant when there are none). After choosing its overall sign, the product of that polynomial and \(S_d\) would be nonnegative everywhere and positive on some open interval, so its integral would be nonzero. Its degree is at most \(d-2\), contradicting the moment identities. Hence \(S_d\), and thus \(F_d\) on \(t>0\), has at least \(d-1\) distinct sign-changing zeros. Combined with the polynomial degree bound, there are exactly \(d-1\) zeros, all simple. The decreasing bijection \(t=(1-\alpha)/\alpha\) maps them to exactly \(d-1\) sign-changing values in \(0<\alpha<1\).

**3. Pairing.** The identity \(f(-x)=1-f(x)\), followed by reversing the binomial summation, yields
\[
S_d(-x-dh)=(-1)^{d+1}S_d(x).
\]
Thus a root at \(t=e^x\) has a partner at \(3^{-d}/t\). Translating through \(\alpha=1/(1+t)\) gives the asserted involution. When \(d\) is even, the antisymmetry forces its fixed point \(t=3^{-d/2}\) to be a root.

**4. Endpoint signs and the three-dimensional values.** As \(\alpha\downarrow0\), \(G_d(\alpha)\sim-(2^d/V)\alpha3^{-d}<0\). At \(\alpha=1\), \(G_d(1)=(2^d/V)(-1)^d\). For \(d=3\), direct common-denominator algebra yields
\[
F_3(t)=-\frac{8(27t^2-24t+1)}{(1+t)(1+3t)(1+9t)(1+27t)}.
\]
Its positive roots are \(t=(4\pm\sqrt{13})/9\), giving the stated two blend parameters and alternating signs.

## Verification

Run `python3 check.py` with Python 3 and no third-party dependencies. The script constructs the exact common-denominator polynomial and uses exact rational Sturm sequences to confirm the root count for \(2\le d\le9\); checks involution identities at rational parameters; and compares full exact-rational matrix inversion with the Walsh formula for \(d=2,3,4\). The completed execution returned `VERIFY_OK 261`. These are finite cross-checks; the proof of the assertion for **every** \(d\ge2\) is the moment-orthogonality argument above, not the finite checker.

## Relationship to prior work

Krzysik, Southworth and Wimmer (2026) motivate accurate element-local mass inversion through broken-space additive Schwarz preconditioning and provide general spectral bounds. They do not give an all-dimensional root-count theorem for inverse entries under consistent/lumped blending. Allen and Kirby (2019/2020) provide structured Bernstein mass inversion for a different univariate/simplicial setting, not this blend-parameter sign count. Hanukah (2026, available after the eligible anchor) gives an exact inverse for the mixed eight-node hexahedron: its opposite-corner numerator already implies the **three-dimensional numerical example** above. The contribution here is not that three-dimensional formula; it is the **arbitrary-dimensional exact \(d-1\) root theorem and pairing**. Earlier analyses of finite differences of logistic functions may provide alternative general proofs, but no directly covering mass-inverse result was identified in the sources inspected.

## Limitations

This is a statement about a single-element inverse entry, not a positive/negative-definiteness transition: the entire matrix stays positive definite. Inverse-entry signs do not by themselves establish instability, lack of physical positivity, global solver failure, or failure of the cited methods. For large \(d\), numerical evaluation of the alternating rational sum may suffer cancellation; the mathematics is in exact arithmetic. The possibility of an unindexed equivalent all-dimensional zero-count theorem remains an originality risk. No independent mathematical audit has been performed.

## References

1. O. A. Krzysik, B. S. Southworth, G. A. Wimmer, *Broken-space Additive Schwarz Mass Inverse Approximations and (Block) Preconditioning*, arXiv:2607.12138, submitted 2026-07-13, https://arxiv.org/abs/2607.12138.
2. E. Hanukah, *Direct Element-Level Mass Matrix Inversion*, arXiv:2611.21820v1, submitted 2026-11-16, https://arxiv.org/pdf/2611.21820. This later source is used only for the priority comparison, not to establish eligibility.
3. L. Allen, R. C. Kirby, *Structured Inversion of the Bernstein Mass Matrix*, arXiv:1907.05773, initially released 2019-07-12, https://arxiv.org/abs/1907.05773; SIAM J. Matrix Anal. Appl. 41 (2020), 413–431.
