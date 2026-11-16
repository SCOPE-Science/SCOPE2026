# The unique minimal modulo-three Walsh degree projector and its exponential norm gap

## Finding

Let \(n\ge3\) be an integer and let \(G_n=\mathbb F_2^n\), equipped with normalized counting measure. For \(r\in\{0,1,2\}\), write \(E_{n,r}=\{\xi\in G_n:|\xi|\equiv r\pmod3\}\), where \(|\xi|\) is Hamming weight. Let \(P_{n,r}\) be the Fourier projection on complex- or real-valued functions on \(G_n\) onto the span of the characters \(\chi_\xi(x)=(-1)^{\langle\xi,x\rangle}\) for \(\xi\in E_{n,r}\). Define its sharp endpoint norm \(L_{n,r}=\|P_{n,r}\|_{\ell^\infty(G_n)\to\ell^\infty(G_n)}\), which also equals its \(\ell^1\) norm and the least norm of **any** projection onto its range.

Put
\[
A_j=\sum_{s=0}^{\lfloor j/2\rfloor}\binom{j}{2s}3^s=\frac{(1+\sqrt3)^j+(1-\sqrt3)^j}{2},\qquad r_n\equiv2n\pmod3,\quad0\le r_n\le2,
\]
\[
\varepsilon_n=(-1)^{(n-2r_n)/3}\in\{-1,1\}.
\]
Then the three sharp endpoint norms satisfy the exact two-level law
\[
\boxed{L_{n,r_n}=\frac{2^n+2A_n+2\varepsilon_n-2}{3\cdot2^n}},
\]
\[
\boxed{L_{n,r}=L_{n,r_n}+\frac{2A_{n-1}+1-3\varepsilon_n}{3\cdot2^n}\quad(r\ne r_n).}
\]
In particular, the unique norm-minimizing residue is \(r_n\), the other two residue choices have exactly equal norms, and the separation is strictly positive for every \(n\ge3\). The corresponding three Fourier subspaces have dimensions differing by **at most one**:
\[
\dim\operatorname{ran}P_{n,r_n}=\frac{2^n+2\varepsilon_n}{3},\qquad
\dim\operatorname{ran}P_{n,r}=\frac{2^n-\varepsilon_n}{3}\quad(r\ne r_n).
\]

If \(\rho=(1+\sqrt3)/2>1\), then
\[
L_{n,r_n}\sim\frac{\rho^n}{3},\quad
L_{n,r}\sim\frac{1+\sqrt3}{6}\rho^n\ (r\ne r_n),\quad
\frac{L_{n,r}}{L_{n,r_n}}\longrightarrow\rho.
\]
Thus two equally ranked (up to one Fourier character) modular frequency classes have an exponentially growing sharp norm difference, with a nontrivial limiting relative penalty.

## Assumptions and scope

The underlying group is exactly \(\mathbb F_2^n\) for all integers \(n\ge3\); Fourier coefficients are \(\widehat f(\xi)=2^{-n}\sum_{x\in G_n}f(x)\chi_\xi(x)\). The kernel polynomial below uses the unnormalized character sum; the projection kernel is its \(2^{-n}\)-multiple. No normalization factor is suppressed. The exponent \((n-2r_n)/3\) is an integer by definition. Both real and complex endpoint norms are covered, because the extremizing kernel-sign function is real. All comparisons of the three residue classes are for the same fixed dimension \(n\).

## Proof

**1. Fourier kernel and sharp norm.** Write
\[
K_{n,r}(z)=\sum_{\xi\in E_{n,r}}(-1)^{\langle\xi,z\rangle}.
\]
Then \(P_{n,r}f(x)=2^{-n}\sum_{y\in G_n}K_{n,r}(x-y)f(y)\). Hence \(L_{n,r}=2^{-n}\sum_z|K_{n,r}(z)|\). The upper bound is the convolution triangle inequality, and equality at \(x=0\) is attained by \(f(y)=\operatorname{sgn}K_{n,r}(y)\), with any choice at zeros. The \(\ell^1\) norm agrees by column sums (or duality).

The same norm is minimal among *all* projections onto this Fourier subspace. Indeed, average any such projection under the \(G_n\)-translation action. The average has no larger norm, commutes with translations, and acts as the identity on the selected characters while annihilating every other character. Thus it is exactly \(P_{n,r}\). This is the elementary finite-group version of the translation-averaging principle.

**2. Root-of-unity evaluation.** If \(k=|z|\), the full Krawtchouk generating function gives
\[
\sum_{w=0}^n\left(\sum_{|\xi|=w}(-1)^{\langle\xi,z\rangle}\right)t^w=(1+t)^{n-k}(1-t)^k.
\]
Let \(\zeta=e^{2\pi i/3}\) and \(\theta_r=(n-2r)\pi/3\). The cubic roots-of-unity filter yields, for \(k\ge1\),
\[
K_{n,r}(z)=\frac23\,3^{k/2}\cos(\theta_r-k\pi/2),
\]
whereas \(K_{n,r}(0)=(2^n+2\cos\theta_r)/3>0\). These are exact identities (not approximations): \(1+\zeta=e^{i\pi/3}\) and \(1-\zeta=\sqrt3e^{-i\pi/6}\).

**3. Absolute-value sums.** Define \(B_n=\sum_{s\ge0}\binom n{2s+1}3^s\), so \(A_n\) and \(B_n\) are positive integers with \(A_0=1\), \(A_1=1\), \(A_2=4\), and
\[
A_{n+1}=A_n+3B_n,\qquad B_{n+1}=A_n+B_n.
\]
The unique residue \(r_n\) has \(\cos\theta_{r_n}=\varepsilon_n\in\{\pm1\}\). For its kernel, the terms at odd positive \(k\) vanish, while those at even positive \(k\) have magnitude \(2\,3^{k/2}/3\). Including \(k=0\) separately and multiplying by the \(\binom nk\) vectors of weight \(k\) gives
\[
3\cdot2^n L_{n,r_n}=2^n+2\varepsilon_n+2(A_n-1).
\]
For either of the two other residues, \(2\cos\theta_r=-\varepsilon_n\). Positive even \(k\) give absolute values \(3^{k/2}/3\), and positive odd \(k\) give \(3^{(k-1)/2}\). Thus
\[
3\cdot2^n L_{n,r}=2^n-\varepsilon_n+(A_n-1)+3B_n.
\]
Subtracting and using \(3B_n-A_n=2A_{n-1}\), an immediate consequence of the displayed recurrence, proves the two-level exact formula. Since \(A_{n-1}\ge A_2=4\) when \(n\ge3\), the difference numerator \(2A_{n-1}+1-3\varepsilon_n\ge6\) is strictly positive. The two other residues tie exactly because their cosine magnitudes agree at every Hamming weight, including \(k=0\).

**4. Dimensions and asymptotics.** Evaluate the kernel at \(z=0\): it equals the number of characters in the projection and gives the stated dimensions. Let \(u=1+\sqrt3\), \(v=1-\sqrt3\). The identity \(A_j=(u^j+v^j)/2\), together with \(|v|<2<u\), gives the asymptotic formulas. For the competitor, the leading term is \((u^n+u^{n-1})/(3\cdot2^n)=u^{n+1}/(6\cdot2^n)\), using \(u^2=2u+2\). Dividing by the distinguished leading term proves the limit \(u/2=\rho\).

## Verification

The attached `check.py` is a standalone Python 3 standard-library checker. It forms the complete indicator vector of each residue-frequency class and calculates its unnormalized Walsh transform via an integer fast Walsh-Hadamard transform, for every \(3\le n\le12\). It separately sums Krawtchouk values at all Hamming weights for \(3\le n\le18\), and compares those integer absolute sums with both closed expressions. The script confirms strict minimality and the exact tie. Further recurrence consistency and positivity tests cover \(3\le n\le100\). The proof above, rather than the finite tests, establishes the identities for all \(n\ge3\).

## Relationship to prior work

The Walsh expansion and finite-group character framework are standard; see Tan's 2012 lecture notes [1]. Defant, Galicer, Mansilla, Mastyło and Muro [2, Theorem 3.1] prove the general identity expressing the projection norm for an *arbitrary* Walsh frequency family as the mean absolute value of its character sum. That general formula, together with the classical Krawtchouk generating function, is the starting point here, not a newly claimed result. The assessed contribution is the closed all-dimension two-level evaluation for three weight residues, the unique dimension-dependent minimizing class, the exact strictly positive arithmetic gap, and its exponential asymptotics. The cited general results do not state those modular evaluations or optimizer classification. Other modular-three Walsh sampling work studies Gram matrices of low-degree restriction operators, not these full-spectrum translation-invariant projections.

## Limitations

The theorem is restricted to modulus three on binary cubes. It does not classify other moduli or optimize arbitrary unions of residue classes. The historical literature comparison is bounded, and an unlocated equivalent evaluation in older special-function literature cannot be ruled out. No independent mathematical audit has been performed. No inference about experimental or numerical precision is needed: all stated finite computations are exact integer computations.

## References

[1] Li-Yang Tan, *Analysis of Boolean Functions*, scribe notes for Ryan O'Donnell's 2012 lectures, arXiv:1205.0314v1 (first publicly submitted 2012-05-02), especially Section 1.1. https://arxiv.org/abs/1205.0314

[2] A. Defant, D. Galicer, M. Mansilla, M. Mastyło, S. Muro, *Asymptotic insights for projection, Gordon–Lewis and Sidon constants in Boolean cube function spaces*, arXiv:2302.00233v2, Theorem 3.1 and Section 4 (first submitted 2023-02-01). https://arxiv.org/abs/2302.00233
