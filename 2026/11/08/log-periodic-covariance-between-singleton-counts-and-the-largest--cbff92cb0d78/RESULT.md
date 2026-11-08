# Log-periodic covariance between singleton counts and the largest part of a uniform composition

## Finding

Choose a composition of the integer \(n\ge2\) uniformly from the \(2^{n-1}\) ordered positive-integer compositions. Let \(S_n\) be the number of parts of size one and \(M_n\) the largest part. Write \(L=\log_2 n\), \(x=\{L\}\), \(u_j(x)=2^{x-j-1}\), and define
\[
P(x)=\sum_{j\in\mathbb Z}u_j(x)e^{-u_j(x)},\qquad
Q(x)=\sum_{j\in\mathbb Z}(j-x)u_j(x)e^{-u_j(x)}.
\]
Both series converge absolutely and define continuous one-periodic functions. The dependence law is
\[
\boxed{\operatorname{Cov}(S_n,M_n)=-\frac{L}{4}P(x)-\frac14 Q(x)+o(1).}
\tag{1}
\]
In particular the covariance is strictly negative for each \(n\ge2\), and its leading magnitude is logarithmic, with an explicit nonconstant digital modulation. The exact mean is \(\mathbb E S_n=(n+2)/4\).

Equivalently, letting \(\lambda_{n,m}=n2^{-m-1}\),
\[
\boxed{\operatorname{Cov}(S_n,M_n)=-\frac14\sum_{m\ge1}m\lambda_{n,m}e^{-\lambda_{n,m}}+o(1).}
\tag{2}
\]
The Fourier coefficients of the leading profile are
\[
\widehat P(k)=\int_0^1P(x)e^{-2\pi ikx}\,dx
=\frac{\Gamma(1-2\pi ik/\ln2)}{\ln2},\qquad k\in\mathbb Z.
\tag{3}
\]
Consequently the mean coefficient is \(1/\ln2\), but the profile is not constant (the first harmonic alone has peak-to-peak amplitude approximately \(2.8520\times10^{-5}\)).

## Assumptions and scope

The composition is uniform, unrestricted and has positive integer parts summing to \(n\). A cut-bit representation has independent fair bits \(X_1,\dots,X_{n-1}\), with deterministic boundary cuts \(X_0=X_n=1\). Then \(S_n=\sum_{i=1}^n X_{i-1}X_i\), and \(M_n\) is one plus the longest zero-run. Results hold as \(n\to\infty\) over all positive integers, not merely subsequences. The \(o(1)\) error in (1) and (2) is additive, so the bounded second-order oscillatory term is resolved.

For \(m\ge1\), set \(A_m(z)=z+\cdots+z^m\), \(a_{n,m}=[z^n](1-A_m(z))^{-1}\) and \(b_{n,m}=[z^n]z(1-A_m(z))^{-2}\). Marking one singleton with an auxiliary variable proves
\[
\mathbb P(M_n\le m)=\frac{a_{n,m}}{2^{n-1}},\quad
\mathbb E[S_n\mathbf1_{\{M_n\le m\}}]=\frac{b_{n,m}}{2^{n-1}}.
\]
Thus the complete finite coefficient identity is
\[
\operatorname{Cov}(S_n,M_n)
=-2^{1-n}\sum_{m=1}^{n-1}\left(b_{n,m}-\frac{n+2}{4}a_{n,m}\right).
\tag{4}
\]
No independence of singleton counts and maximum parts is asserted.

## Proof

**Exact identity and sign.** The generating function with a singleton marker is
\[
F_m(z,u)=\frac1{1-A_m(z)-(u-1)z}.
\]
Its derivative at \(u=1\) gives \(b_{n,m}\). Since \(M_n=1+\sum_{m=1}^{n-1}\mathbf1_{\{M_n>m\}}\), taking covariance yields (4). Each singleton indicator \(X_{i-1}X_i\), and also \(\mathbf1_{\{M_n\le m\}}\), is increasing in the independent cut bits; Harris's inequality therefore gives \(\operatorname{Cov}(S_n,\mathbf1_{\{M_n\le m\}})\ge0\). The case \(m=1\) is strictly positive because \(M_n\le1\) forces all parts to be singletons while \(\mathbb ES_n<n\). Hence the covariance in (4) is strictly negative.

**Uniform coefficient estimates.** For \(m\ge5\) write
\[
F_m(z,u)=\frac{1-z}{1-2z+z^{m+1}-(u-1)z(1-z)}.
\]
For \(|z|=3/5\) and \(|u-1|\le1/20\),
\[
|z^{m+1}-(u-1)z(1-z)|
\le(3/5)^6+\frac1{20}\frac35\frac85<\frac15\le|1-2z|.
\]
Rouché's theorem gives precisely one, simple pole inside this circle, uniformly in \(m\) and \(u\). At \(u=1\) this pole \(\rho_m\) lies in \((1/2,11/20)\) and solves \(2\rho_m-1=\rho_m^{m+1}\). Define \(\varepsilon_m=2^{-m-1}\). When \(m\to\infty\),
\[
2\rho_m-1=\varepsilon_m+O(m\varepsilon_m^2),\quad
A_m'(\rho_m)=4\{1-m\varepsilon_m+O(m^2\varepsilon_m^2)\}.
\tag{5}
\]
Residue transfer, including differentiation with respect to the singleton marker, yields uniformly for growing \(m\ge5\)
\[
\begin{split}
a_{n,m}&=c_m\rho_m^{-n}+O((5/3)^n),\qquad c_m=\frac1{\rho_m A_m'(\rho_m)},\\
\frac{b_{n,m}}{a_{n,m}}&=\frac n{A_m'(\rho_m)}+\frac{\rho_m A_m''(\rho_m)}{A_m'(\rho_m)^2}+O(n(11/12)^n),
\end{split}
\tag{6}
\]
where \(2c_m=1+O(m\varepsilon_m)\) and \(\rho_m A_m''(\rho_m)/A_m'(\rho_m)^2=1/2+O(m^2\varepsilon_m)\). The estimates follow by isolating the unique pole on the fixed circle; the analytic remainder and its marker derivative are uniformly exponentially smaller than the residue. The derivative identity in (6) follows from implicit differentiation of \(A_m(\rho_m(u))+(u-1)\rho_m(u)=1\) and differentiation of its residue \(\{\rho_m(u)[A'_m(\rho_m(u))+u-1]\}^{-1}\).

Let \(h=7\log_2 L\), and consider integers \(m\) in the central window \(|m-L|\le h\). There \(m=O(L)\), \(\lambda_{n,m}=n\varepsilon_m\le L^7\), and \(\varepsilon_m\le L^7/n\). Equations (5)–(6) give, uniformly through this window,
\[
\begin{split}
\Pr(M_n\le m)&=e^{-\lambda_{n,m}}(1+O(\operatorname{poly}(L)/n)),\\
\mathbb E[S_n\mid M_n\le m]-\frac{n+2}{4}
&=\frac14m\lambda_{n,m}+O(\operatorname{poly}(L)/n),\\
\operatorname{Cov}(S_n,\mathbf1_{\{M_n\le m\}})
&=\frac14m\lambda_{n,m}e^{-\lambda_{n,m}}+O(\operatorname{poly}(L)/n).
\end{split}
\tag{7}
\]
Here each polynomial is fixed (independent of \(n\) and \(m\)); multiplication by a factor bounded by one is harmless. There are \(O(\log L)\) central indices, so their total error is \(o(1)\).

**Control of both tails.** For \(m<L-h\), partition the cut bits into disjoint blocks of length \(m\). If \(M_n\le m\), no such block can consist entirely of zeros. Independence gives
\[
\Pr(M_n\le m)\le(1-2^{-m})^{\lfloor(n-1)/m\rfloor}
\le\exp\{-c n2^{-m}/m\}.
\]
In this range \(n2^{-m}/m\ge c L^6\). Since \(0\le S_n\le n\), the total contribution of these \(m\)'s to (4) is \(o(1)\).

For the high tail, force the two cut coordinates defining any singleton indicator to one. This can change the event \(M_n\le m\) only if the original word has an all-zero string of length \(m\) containing a forced cut coordinate; at most \(2m\) such strings are possible. Consequently each singleton indicator contributes at most \(2m2^{-m}\) to the covariance with \(\mathbf1_{\{M_n\le m\}}\). Therefore
\[
0\le\operatorname{Cov}(S_n,\mathbf1_{\{M_n\le m\}})\le2nm2^{-m}
\]
for all \(n,m\), and summing over \(m>L+h\) gives \(O(L2^{-h})=o(1)\). The corresponding tails of \(\sum_{m\ge1}m\lambda_{n,m}e^{-\lambda_{n,m}}\) are controlled by exponential decay as \(\lambda\to\infty\) and the geometric bound \(O(L2^{-h})\) as \(\lambda\to0\). Summing (7) and (4) proves (2).

**Digital periodization.** Write \(m=\lfloor L\rfloor+j\). Then \(\lambda_{n,m}=u_j(x)\) and \(m=L+j-x\). Extend the lower index to all integers; the extra terms are exponentially small. Equation (1) follows. Integrate the periodized series against \(e^{-2\pi ikx}\) and substitute \(t=2^{x-j-1}\) to obtain (3) from the Gamma integral \(\int_0^\infty e^{-t}t^{s-1}\,dt=\Gamma(s)\). Since the Gamma function has no zeros, the first Fourier coefficient is nonzero and \(P\) is not constant.

## Verification

The accompanying standalone Python checker `verify_covariance.py` exhaustively enumerates the complete set of uniform compositions through \(n=14\), reconstructs all finite coefficients in (4) and verifies strict negativity. It then computes the exact finite mixed-moment recurrence numerically and compares it against the Poisson-sum asymptotic at \(n=256,512,1024,2048,4096\). It also checks the normalization of \(P(0)\). The checker produces 226 successful assertions on replay. Those experiments corroborate but do not establish the all-\(n\) theorem, which is proved above by singularity analysis and the two tail estimates.

## Relationship to prior work

Bender and Canfield's 2005 framework studies finite-size counts and maximum parts in locally restricted compositions but does not state this mixed singleton–maximum covariance asymptotic. Bender, Canfield and Gao (2012) obtain precise asymptotic maximum-part and large-part frequency information, including Poisson laws for large part sizes; this does not determine mixed covariance with a **fixed small part size** to additive \(o(1)\). Finch (2020) studies covariance of the **total part count** with the largest part, which is a different random variable. An accessible earlier result on uniform compositions likewise proves a negative total-part/maximum covariance bound, not the present sharp singleton/maximum law. The full text of the closest accessible predecessor was compared by hypotheses and mathematical implications, not only by title. Thus the novelty claim concerns (1)–(3), not the standard generating function or a generic negative-dependence observation.

## Limitations

No explicit optimal convergence rate for the additive \(o(1)\) is asserted. The result concerns unrestricted uniform compositions only; constrained compositions and biased cut processes require separate analysis. Existing general multivariate generating functions may encode this covariance implicitly, and unexamined older studies of longest runs and short-run counts remain a historical-priority risk. The result has not undergone an independent audit.

## References

1. E. A. Bender and E. R. Canfield, “Locally Restricted Compositions I. Restricted Adjacent Differences,” *Electronic Journal of Combinatorics* 12 (2005), #R57; first published 2005-11-07, DOI 10.37236/1954.
2. E. A. Bender, E. R. Canfield and Z. Gao, “Locally Restricted Compositions IV. Nearly Free Large Parts and Gap-Freeness,” arXiv:1208.0870 (first submitted 2012-08-03), *Electronic Journal of Combinatorics* 19 (2012), #P14.
3. S. Finch, “Covariance within Random Integer Compositions,” arXiv:2010.06643 (first submitted 2020-10-13).
4. S. Doğanaksoy et al., “New Statistical Randomness Tests Based on Length of Runs,” *The Scientific World Journal* (2015), DOI 10.1155/2015/626408.
5. “Rigorous decorrelation of part count and maximum in uniform compositions,” publicly available mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-rigorous-decorrelation-of-part-count-and-maximum-in-uniform-comp--0ee24a72cd31.
