# Geometric-square covariance spectrum of shifted Menon gcd statistics

## Finding

Let \(p\) be any prime, \(k\ge1\), \(N=p^k\), \(U=(\mathbb Z/N\mathbb Z)^\times\), and \(M=\varphi(N)=(p-1)p^{k-1}\). Sample \(u\) uniformly from \(U\), and, for each \(a\in U\), define
\[
X_a(u)=\gcd(a-u,N),\qquad C_{ab}=\operatorname{Cov}_{u\in U}(X_a(u),X_b(u)).
\]
The convention \(\gcd(0,N)=N\) is used. Write \(\operatorname{mult}_C(\lambda)\) for the multiplicity of eigenvalue \(\lambda\). Then the complete spectrum is
\[
\operatorname{mult}_C(0)=1,\qquad
\operatorname{mult}_C\bigl(M(k-\ell+1)^2\bigr)=
\begin{cases}
p-2,&\ell=1,\\
(p-1)^2p^{\ell-2},&2\le\ell\le k,
\end{cases}
\quad (1\le\ell\le k),
\]
with zero multiplicities omitted. There are no other eigenvalues. In particular, \(\operatorname{rank} C=M-1\); when \(M=1\), the sole eigenvalue is zero.

The empirical spectral measure of \(C/M\), including multiplicities,
\[
\mu_{p,k}=\frac1M\sum_{\lambda\in\operatorname{Spec}(C)}\delta_{\lambda/M},
\]
obeys the **exact total-variation identity**
\[
\left\|\mu_{p,k}-\sum_{j=1}^{\infty}\frac{p-1}{p^j}\delta_{j^2}\right\|_{\mathrm{TV}}
=\frac{1}{(p-1)p^{k-1}}.
\]
Thus the limiting normalized covariance spectrum is a geometric law supported on perfect squares. For odd \(p\), the condition number on the positive eigenspace is \(k^2\); for \(p=2\) and \(k\ge2\), it is \((k-1)^2\).

The covariance entries themselves have the exact form
\[
C_{ab}=-k^2+(p-1)\sum_{j=1}^{t}p^{j-1}\bigl(2(k-j)+1\bigr),
\quad t=\max\{0\le j\le k:a\equiv b\pmod{p^j}\}.
\]
In particular, for \(p>2\), two units distinct modulo \(p\) have covariance \(-k^2\).

## Assumptions and scope

The ambient probability distribution is **uniform on invertible residue classes**, not uniform on all residues. Both the row and column indices of \(C\) run over the same set \(U\). The prime \(p\) and exponent \(k\) are arbitrary subject to \(p\) prime and \(k\ge1\). The square-eigenvalue normalization uses \(C/M\), **not** \(C\) itself. Total variation of two discrete probabilities is one-half the sum of absolute mass differences on their combined support. Eigenvalues are counted with algebraic multiplicity, which here equals geometric multiplicity because \(C\) is real symmetric.

## Proof

**1. Gcd expansion and mean.** For every nonnegative \(h\le k\),
\[
p^h=1+\sum_{j=1}^{h}\varphi(p^j).
\]
Therefore for \(a,u\in U\),
\[
X_a(u)=1+\sum_{j=1}^k\varphi(p^j)\mathbf1_{a\equiv u\pmod{p^j}}.
\]
Among the \(M\) unit residues, exactly \(M/\varphi(p^j)\) reduce to a fixed unit modulo \(p^j\); hence each summand has mean one, and \(\mathbb E_u X_a(u)=k+1\), independently of \(a\).

**2. Nested projection decomposition.** For \(1\le j\le k\), let \(B_j\) be the \(M\)-by-\(M\) matrix with entries \((B_j)_{au}=\mathbf1_{a\equiv u\pmod{p^j}}\). Define \(P_j=(\varphi(p^j)/M)B_j\), and let \(P_0\) be the orthogonal projection onto the constant vectors, namely \(P_0=J/M\), where \(J\) is the all-ones matrix. Since each block of \(B_j\) has exactly \(M/\varphi(p^j)\) elements, \(P_j\) averages over the residue class and is an orthogonal projection. Its image \(V_j\) is the space of functions of the reduction modulo \(p^j\), with dimension \(\varphi(p^j)\). The images form a nested flag
\[
V_0\subseteq V_1\subseteq\cdots\subseteq V_k=\mathbb R^M.
\]
They are nested even in the degenerate case \(p=2,j=1\), where \(V_0=V_1\). Put \(H_{au}=X_a(u)-(k+1)\). The gcd expansion gives the **matrix identity**
\[
H=M\left(\sum_{j=1}^k P_j-kP_0\right).
\]
The matrix \(H\) is symmetric, and its rows and columns sum to zero.

**3. Eigenvalues and multiplicities.** Decompose \(\mathbb R^M\) orthogonally into \(V_0\) and \(W_\ell=V_\ell\cap V_{\ell-1}^{\perp}\), \(1\le\ell\le k\). For \(v\in W_\ell\), one has \(P_jv=0\) when \(j<\ell\) and \(P_jv=v\) when \(j\ge\ell\). Thus \(Hv=M(k-\ell+1)v\). On constants, \(Hv=0\). Since \(C=M^{-1}HH^{\mathsf T}=M^{-1}H^2\), the claimed eigenvalues follow. Their multiplicities are
\[
\dim W_1=\varphi(p)-1=p-2,\qquad
\dim W_\ell=\varphi(p^\ell)-\varphi(p^{\ell-1})=(p-1)^2p^{\ell-2}\quad(\ell\ge2).
\]
Summing these multiplicities plus one yields \(M\); therefore the spectrum is complete. As every nonempty \(W_\ell\) has a strictly positive eigenvalue, the nullspace is precisely the constants. The extreme positive eigenvalues give the condition-number statements.

**4. Exact covariance entries.** Because the projections are nested, \(P_iP_j=P_{\min(i,j)}\). There are \(2(k-j)+1\) ordered pairs \((i,i')\) with \(\min(i,i')=j\). Consequently
\[
C=M\left(\sum_{j=1}^k(2(k-j)+1)P_j-k^2P_0\right).
\]
Taking an entry and substituting the formulas for \(P_j\) gives the stated covariance formula; it also applies at \(a=b\), for which \(t=k\).

**5. Geometric-square limit and sharp error.** On dividing the eigenvalues by \(M\), the atom \(j^2\) for \(1\le j<k\) has mass exactly \((p-1)p^{-j}\). The atom \(k^2\) has mass \((p-2)/M\), while zero has mass \(1/M\). The proposed limit has mass \((p-1)p^{-k}\) at \(k^2\) and total mass \(p^{-k}\) on all larger squares. The deficit at \(k^2\) is \(1/(pM)\); the missing tail weighs \((p-1)/(pM)\). Hence the total variation is
\[
\frac12\left(\frac1M+\frac1{pM}+\frac{p-1}{pM}\right)=\frac1M.
\]
These identities remain valid for \(p=2,k=1\), when all mass of \(\mu_{p,k}\) is at zero. This completes the proof.

## Verification

Run `python3 check_spectrum.py` in the same directory. The standalone checker uses only the Python standard library, directly enumerates invertible classes, evaluates all gcd values and empirical covariance entries using integer arithmetic, and checks the explicit covariance formula. It then constructs a complete basis of residue-block difference vectors, verifies their predicted action under \(H\), checks dimension and trace, and verifies the spectral total-variation formula using exact rational arithmetic. Its successful output covers 15 prime-power parameter cases, 315 state coordinates, 315 basis vectors and 16,861 covariance entries, including both odd primes and the exceptional dyadic first level. These are finite regression tests **in addition to**, not a substitute for, the all-parameter proof above.

## Relationship to prior work

Menon's identity and its shifted versions give the common first moment \(\mathbb E X_a=k+1\); Tóth's 2021 survey explains these identities and their finite-Fourier formulations [1]. Tóth's 2019 paper [2] gives single-shift additive-character transforms for even functions, while van der Kamp's earlier work [3] treats the discrete Fourier transform of gcd functions on the full additive residue ring. Ushiroya's 2018 paper [4] determines eigenvalues of **Ramanujan-sum circulants on all residues**. The present claim is different: it concerns the complete **unit-indexed covariance Gram matrix** of simultaneous shifted gcd variables, including the multiplicity of every eigenvalue and the exact limiting spectral law. The nested averaging projections and the squaring from centered data to covariance are the essential additional steps. Nothing here claims novelty for Menon's first moment, the gcd divisor expansion, or the general theory of nested orthogonal projections.

## Limitations

The theorem concerns prime-power moduli and uniform random units. It does not assert the same spectrum for composite moduli with more than one prime factor, for unrestricted residues, or for arbitrary nonlinear functions of the gcd. The limit is an empirical spectral distribution of normalized *real* covariance eigenvalues; it is not a distribution of eigenvalues of a matrix over \(\mathbb Q_p\). The construction can potentially be obtained as a specialization of broader pre-existing ultrametric-kernel spectral theory; an equivalent earlier specialization remains a bibliographic priority risk despite the source comparisons. The numerical checker verifies finitely many instances only. Independent mathematical validation has not been performed.

## References

[1] László Tóth, *Proofs, generalizations and analogs of Menon's identity: a survey*, arXiv:2110.07271 (first posted 2021-10-14). https://arxiv.org/abs/2110.07271

[2] László Tóth, *Menon-type identities concerning additive characters*, Arabian Journal of Mathematics 9 (2020), 697–705 (online 2019-05-29). https://doi.org/10.1007/s40065-019-0259-3

[3] Peter H. van der Kamp, *On the Fourier transform of the greatest common divisor*, arXiv:1201.3139 (first posted 2012-01-16). https://arxiv.org/abs/1201.3139

[4] Noboru Ushiroya, *Eigenvalues of Matrices whose Elements are Ramanujan Sums or Kloosterman Sums*, arXiv:1803.02970 (first posted 2018-03-08). https://arxiv.org/abs/1803.02970
