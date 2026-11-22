# Exact Gaussian spectral dominance for every radial middle-third Cantor mask

## Finding

Let \(C_n(x)\) be the \(n\)-th closed middle-third Cantor approximation in \([0,x]\), where \(x>0\) and \(n\ge 0\) is an integer. Define the radial phase-space region
\[
\Omega_{n,x}=\{(q,p)\in\mathbb R^2:\ \pi(q^2+p^2)\in C_n(x)\}.
\]
For the normalized Gaussian \(\phi(t)=2^{1/4}e^{-\pi t^2}\), let \(V_\phi\) be the short-time Fourier transform with convention
\[
V_\phi f(q,p)=\int_{\mathbb R}f(t)\overline{\phi(t-q)}e^{-2\pi i pt}\,dt,
\qquad T_{n,x}=V_\phi^*\mathbf1_{\Omega_{n,x}}V_\phi.
\]
Then the Gaussian \(H_0=\phi\) is the **unique unit-norm maximizer up to complex phase** of \(\langle T_{n,x}f,f\rangle\), for every \(n\ge0\) and \(x>0\). In particular, the operator norm is **exactly**
\[
\boxed{\|T_{n,x}\|=\lambda_0(n,x)=
(1-e^{-x/3^n})\prod_{j=1}^{n}(1+e^{-2x/3^j}).}
\]
The product for \(n=0\) is empty. For the normalized Hermite functions \(H_k\), let
\[
\lambda_k(n,x)=\int_{C_n(x)}e^{-r}\frac{r^k}{k!}\,dr,
\qquad k=0,1,2,\ldots.
\]
For every integer \(k\ge1\), the following **quantitative strict gap** holds:
\[
\boxed{\lambda_0(n,x)-\lambda_k(n,x)\ge
\lambda_0(n,x)e^{-x}\sum_{j=0}^{k-1}\frac{x^j}{j!}>0.}
\]
A structural generalization is also proved: if a measurable set \(E\subset[0,X]\), with \(0<|E|<\infty\), has the *initial-window domination property*
\[
|E\cap[s,s+h]|\le |E\cap[0,h]|\quad(s,h\ge0),
\]
then the Gaussian is the unique top mode of the radial Gaussian localization operator for \(E\), with the same gap inequality after replacing \(x\) by \(X\).

## Assumptions and scope

All intervals are Lebesgue measurable; endpoints have no effect on operators. Define \(C_0(x)=[0,x]\), and recursively
\[
C_{n+1}(x)=\frac13 C_n(x)\;\cup\;
\left(\frac{2x}{3}+\frac13C_n(x)\right).
\]
The two components are disjoint, \(|C_n(x)|=x(2/3)^n\), and their reflection symmetry about \(x/2\) is exact. The operator acts on complex \(L^2(\mathbb R)\), not on a truncated Hermite span, and the result covers **all** integer iterations, all positive finite radii, and all Hermite degrees. It does not assert analogous optimality for a general disconnected radial symbol or for a non-Gaussian analysis window.

## Proof

**1. A self-contained sliding-window lemma.** Normalize to \(x=1\), write \(E_n=C_n(1)\) and \(m_n=|E_n|=(2/3)^n\), and define \(F_n(t)=m_n^{-1}|E_n\cap[0,t]|\). Set \(F_n(t)=0\) for \(t\le0\) and \(F_n(t)=1\) for \(t\ge1\). Reflection symmetry gives
\[
F_n(1-t)=1-F_n(t)\quad(0\le t\le1).
\]
We prove inductively that every interval of length \(h\ge0\) has at most as much \(E_n\)-mass as \([0,h]\). It is evident for \(n=0\). Assume it for \(n\); equivalently, \(F_n(u+v)\le F_n(u)+F_n(v)\) for all \(u,v\ge0\).

For \(E_{n+1}\), the occupied parent blocks are \([0,1/3]\) and \([2/3,1]\), each a \(1/3\)-scaled copy of \(E_n\). If \(0\le h\le1/3\), an interval of length \(h\) cannot meet both occupied blocks in positive measure. The inductive sliding property within whichever block it meets bounds its mass by that of \([0,h]\).

If \(1/3\le h\le2/3\), the initial interval captures exactly the whole left block, of mass \(m_n/3\). An arbitrary interval meeting at most one block captures no more. An interval meeting both blocks captures a suffix of the left block of length \(u\) and a prefix of the right block of length \(v\), where \(u+v\le h-1/3\le1/3\). Their combined mass equals
\[
\frac{m_n}{3}\big(F_n(3u)+F_n(3v)\big)
\le\frac{m_n}{3},
\]
because \(3v\le1-3u\), \(F_n\) is nondecreasing, and \(F_n(1-3u)=1-F_n(3u)\).

If \(2/3\le h\le1\), one may translate an arbitrary length-\(h\) observation interval into \([0,1]\) without decreasing its captured mass; write it as \([a,a+h]\), with \(0\le a\le1-h\). Its complement within \([0,1]\) comprises a left prefix of length \(a\) and a right suffix of length \(b=1-a-h\), both no longer than \(1/3\). By symmetry and the induction hypothesis, the mass it excludes is
\[
\frac{m_n}{3}\big(F_n(3a)+F_n(3b)\big)
\ge\frac{m_n}{3}F_n(3(a+b)).
\]
The right side is precisely the mass excluded by the initial window \([0,h]\), whose complement is the right suffix of length \(a+b=1-h\). Hence the initial window again captures at least as much. The case \(h\ge1\) is immediate. This completes the induction. Scaling establishes the sliding property for every \(C_n(x)\) and every \(x>0\).

**2. The exponential residual-window inequality.** Let \(E\subset[0,X]\) satisfy the sliding property, put \(L_0=\int_Ee^{-r}\,dr>0\), and for \(s\ge0\) define
\[
H(s)=\int_0^\infty\mathbf1_E(s+t)e^{-t}\,dt.
\]
The cumulative translated occupancy \(A_s(t)=|E\cap[s,s+t]|\) obeys \(0\le A_s(t)\le A_0(t)\) for all \(s,t\ge0\). Integration by parts (the bounded cumulative occupancies have vanishing exponentially weighted boundary terms) gives
\[
H(s)=\int_0^\infty e^{-t}A_s(t)\,dt
\le\int_0^\infty e^{-t}A_0(t)\,dt=L_0.
\]
Moreover, \(H(s)=0\) whenever \(s\ge X\).

**3. The full Hermite spectrum and strict top mode.** The standard Gaussian STFT–Hermite identity reads
\[
|V_\phi H_k(q,p)|^2
=e^{-\pi(q^2+p^2)}\frac{[\pi(q^2+p^2)]^k}{k!}.
\]
Its angular factors are mutually orthogonal on radial regions. Polar integration with \(r=\pi(q^2+p^2)\) yields exactly the diagonal eigenvalues \(\lambda_k(E)=\int_E e^{-r}r^k/k!\,dr\). They are nonnegative and their sum is \(|E|<\infty\), so the operator is positive trace class.

For \(k\ge1\), the Gamma-density convolution identity is
\[
\frac{e^{-r}r^k}{k!}
=\int_0^r\frac{e^{-s}s^{k-1}}{(k-1)!}e^{-(r-s)}\,ds.
\]
Tonelli's theorem and step 2 therefore imply
\[
\lambda_k(E)=\int_0^\infty\frac{e^{-s}s^{k-1}}{(k-1)!}H(s)\,ds
\le L_0\int_0^X\frac{e^{-s}s^{k-1}}{(k-1)!}\,ds.
\]
The last integral is the Erlang cumulative probability
\[
1-e^{-X}\sum_{j=0}^{k-1}\frac{X^j}{j!}<1.
\]
Hence \(\lambda_k(E)<L_0=\lambda_0(E)\) for **every** \(k\ge1\), with the claimed quantitative gap. The positive compact operator has a simple largest eigenvalue; the Gaussian is consequently the unique norming vector up to phase. No finite cutoff or numerical approximation enters this argument.

**4. Exact product for the Cantor regions.** At the finest ternary scale, \(C_n(x)\) consists of intervals \([x d/3^n,x(d+1)/3^n]\), where \(d\) has \(n\) ternary digits each in \(\{0,2\}\). Thus
\[
\begin{aligned}
\lambda_0(n,x)&=(1-e^{-x/3^n})
\sum_{d}\exp(-xd/3^n)\\
&=(1-e^{-x/3^n})
\prod_{j=1}^n(1+e^{-2x/3^j}).
\end{aligned}
\]
This product is present in the motivating literature for the **first** eigenvalue. Steps 1–3 establish the additional, sharp conclusion that it equals the **operator norm**, with simple ground state and a quantified gap.

## Verification

The included standalone `check_numerics.py` uses only Python's standard library. It evaluates normalized finite-Cantor occupancy exactly on all ternary-grid pairs for stages \(0\le n\le6\), then evaluates Gamma-integral eigenvalues with 75-decimal-digit arithmetic for stages \(0\le n\le6\), four positive radii, and the first 32 excited Hermite orders. Its actual replay returned:

```
PASS occupancy_exact=600064 product=28 strict_spectrum=896 quantitative_gap=896
```

These tests are finite, auxiliary checks only. The induction, residual-window inequality, Gamma convolution and product derivation constitute the infinite proofs. To rerun: `python check_numerics.py`.

## Relationship to prior work

Knutsen's *Daubechies' Time-Frequency Localization Operator on Cantor Type Sets I* (first public 1 July 2019) established the Hermite-Gamma diagonalization, Cantor cumulative subadditivity, the exact first-eigenvalue product, and a bound of **twice** the first eigenvalue for the operator norm (Theorem 4.1). The present theorem reuses these standard objects but proves a stronger, exact norm identity by comparing the entire translated exponential residual occupancy before Gamma convolution. It is not merely another estimate of the already explicit first eigenvalue.

Knutsen's *Part II* (first public 22 April 2021) proves that the Gaussian is optimal for a **different**, left-justified canonical digit alphabet, but states expressly in its introduction that this had not been established for the middle-third alphabet \(\{0,2\}\). The canonical-alphabet theorem does not cover the present noncanonical mask. A separately indexed Cantor–Bergman spectral-vacuum result uses a different analytic function space and restricted scaling; its statement does not imply the all-radius Gaussian STFT theorem. These are mathematical nonimplications, not evidence of global priority. Further specialized literature may contain an independent earlier argument.

## Limitations

The result requires the initial-window domination property. It is not asserted for arbitrary radial annuli, for all digit alphabets, for non-Gaussian windows, or for general weighted Bergman spaces. The bound on the positive Hermite gaps is explicit but need not be optimal. Numerical checks do not establish statements beyond their enumerated finite ranges. Novelty is a literature-comparison judgment, not independent certification; independent mathematical validation has not been performed.

## References

1. H. Knutsen, *Daubechies' Time-Frequency Localization Operator on Cantor Type Sets I*, arXiv:1907.00848 (first posted 1 July 2019); *Journal of Fourier Analysis and Applications* 26, article 47 (2020), DOI:10.1007/s00041-020-09751-9. In particular Theorem 2.1, Theorem 4.1, equations (2.10), (4.4), (4.7), and Proposition 4.1. https://arxiv.org/abs/1907.00848 ; https://link.springer.com/article/10.1007/s00041-020-09751-9
2. H. Knutsen, *Daubechies' Time-Frequency Localization Operator on Cantor Type Sets II*, arXiv:2104.10976 (first posted 22 April 2021); in particular introduction, Lemma 2.2, and Theorem 3.1. https://arxiv.org/abs/2104.10976
3. I. Daubechies, *Time-frequency localization operators: A geometric phase space approach*, IEEE Transactions on Information Theory 34 (1988), 605–612. The Gaussian STFT–Hermite identity is cited through [1, Theorem 2.1].
4. H. Knutsen, *A Fractal Uncertainty Principle for the Short-Time Fourier Transform and Gabor Multipliers*, arXiv:2204.03068 (first posted 6 April 2022); in particular §1 and Theorem 4.1 on general porous-region norm estimates and radial Cantor asymptotic bounds. https://arxiv.org/html/2204.03068v1
