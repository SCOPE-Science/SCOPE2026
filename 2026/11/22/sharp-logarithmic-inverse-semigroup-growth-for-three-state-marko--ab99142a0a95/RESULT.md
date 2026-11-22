# Sharp logarithmic inverse-semigroup growth for three-state Markov generators

## Finding
Let \(Q\) be any real \(3\times3\) matrix whose off-diagonal entries are nonnegative and whose columns sum to zero. Equip matrices with the induced counting \(\ell^1\)-norm. Then
\[
\boxed{\|Q\|_1\le \frac83\log\|e^{-Q}\|_1.}
\]
The coefficient \(8/3\) is the smallest constant valid uniformly over all such \(Q\), including irreducible generators. In fact the stronger sharp spectral inequality holds:
\[
\|Q\|_1\le\frac83\max\{\operatorname{Re}\lambda:\lambda\in\sigma(-Q)\}.
\]
For two-state column-conservative Markov generators the optimal inverse-semigroup coefficient is \(2\). Hence dimension three is the first finite Markov dimension requiring a coefficient strictly above \(2\).

## Assumptions and scope
A column-conservative continuous-time Markov generator \(Q\) has \(Q_{ij}\ge0\) whenever \(i\ne j\) and \(\sum_iQ_{ij}=0\) for each column \(j\). The induced matrix \(\ell^1\)-norm is the maximum absolute column sum, and \(\log\|e^{-Q}\|_1\) is the real natural logarithm; it is nonnegative because \(e^{-Q}\) has eigenvalue \(1\). No irreducibility, stochastic reversibility, primitivity, or diagonalizability is assumed in the upper bound. The sharpness family is irreducible. The time of the inverse exponential is fixed to one, while the generator itself is unrestricted in scale.

## Proof
Write \(q_j=-Q_{jj}=\sum_{i\ne j}Q_{ij}\ge0\). Every absolute column sum of \(Q\) is \(2q_j\), so \(\|Q\|_1=2q\), where \(q=\max_jq_j\). The conclusion is immediate for \(q=0\). Otherwise rescale the generator by \(q^{-1}\) and relabel states so that \(q_1=1\), \(q_2=b\), \(q_3=c\) for \(b,c\ge0\). Put \(t=b+c\).

The eigenvalues of \(-Q\) are \(0\) and the roots of \(\lambda^2-s\lambda+p=0\), where \(s=1+t\) and
\[
p=b+c+bc-(Q_{12}Q_{21}+Q_{13}Q_{31}+Q_{23}Q_{32})\le t+bc\le t+\frac{t^2}{4}.
\]
Here the first displayed \(Q\) is the already normalized generator. Let \(\mu\) be the largest real part of these roots. If \(t\ge 1/2\), the roots have average real part \(s/2\), hence \(\mu\ge(1+t)/2\ge3/4\). If \(0\le t\le1/2\), their discriminant obeys
\[
s^2-4p\ge(1+t)^2-4\left(t+\frac{t^2}{4}\right)=1-2t\ge0,
\]
and therefore
\[
\mu\ge\frac{1+t+\sqrt{1-2t}}2\ge\frac34.
\]
The last inequality follows because the expression decreases from \(1\) to \(3/4\) as \(t\) increases from \(0\) to \(1/2\); its derivative is \((1-1/\sqrt{1-2t})/2\le0\) in the interior. Rescaling proves \(\mu\ge 3q/4\), or \(\|Q\|_1\le (8/3)\mu\). Finally, since \(e^{-Q}\) has spectral radius \(e^{\mu}\), the spectral-radius inequality \(\|e^{-Q}\|_1\ge e^{\mu}\) yields the logarithmic estimate.

Sharpness is witnessed by the irreducible one-way cycle
\[
Q_0=\begin{pmatrix}-1&0&1/4\\1&-1/4&0\\0&1/4&-1/4\end{pmatrix},\quad
P=\frac19\begin{pmatrix}1&1&1\\4&4&4\\4&4&4\end{pmatrix},
\]
\[
N=-Q_0-\frac34(I-P)=\begin{pmatrix}1/3&1/12&-1/6\\-2/3&-1/6&1/3\\1/3&1/12&-1/6\end{pmatrix}.
\]
Direct multiplication gives \(P^2=P\), \(PN=NP=N^2=0\), \(Q_0P=0\), and \(\|N\|_1=4/3\). Thus for every \(h\ge0\),
\[
e^{-hQ_0}=P+e^{3h/4}\bigl((I-P)+hN\bigr),
\]
whence \(\|e^{-hQ_0}\|_1=e^{3h/4}h(4/3+o(1))\) as \(h\to\infty\). Since \(\|hQ_0\|_1=2h\),
\[
\lim_{h\to\infty}\frac{\|hQ_0\|_1}{\log\|e^{-hQ_0}\|_1}=\frac83.
\]
The same example has nonzero eigenvalues \(3/4,3/4\) for \(-Q_0\), making the spectral estimate itself sharp.

In dimension two, writing exits \(r,s\ge0\), \(-Q\) has eigenvalues \(0,r+s\), and \(\|Q\|_1=2\max(r,s)\le2(r+s)\le2\log\|e^{-Q}\|_1\). For a pure-death generator of exit rate \(h\), the inverse matrix has norm \(2e^h-1\), so \(2h/\log(2e^h-1)\to2\). This proves the stated two-state sharpness.

## Verification
The standalone `check.py` uses rational arithmetic to check the proposed projection and nilpotent decomposition, exact characteristic-polynomial coefficients, and norm values. Its supplementary tests cover a 41-by-41 rational parameter grid, 12,000 randomly generated positive Markov generators, and several values of the sharpness scaling parameter. Executing the included file prints `PASS 13685 supplementary tests; exact projection/nilpotent certificate holds`. The infinite-dimensional parameter ranges and all-time asymptotic statement are justified by the preceding analytic proof, not inferred from finite computations.

## Relationship to prior work
Glück (2020), *On the decoupled Markov group conjecture*, proves dimension-free boundedness of the inverse of positive-semigroup exponentials under a fixed bound \(M\) and mentions the elementary finite-dimensional estimate \(\|Q\|_1\le2d\log\|e^{-Q}\|_1\); the present sharp three-dimensional coefficient improves its \(d=3\) coefficient \(6\) to \(8/3\). The published three-state cycle result *Exact priced spectral-abscissa design on a one-way three-state cycle* (2026) maximizes the **slowest** decay exponent subject to rate prices; it does not estimate the **largest** real-part eigenvalue or induced logarithmic inverse norm over all Markov generators. Cuthbert's 1975 paper titled *An Inequality with Relevance to the Markov Group Problem* is a historically plausible predecessor whose full text could not be inspected, so absolute priority is not claimed.

## Limitations
This statement is for the counting \(\ell^1\) norm, real three-state column-conservative Markov generators, and the inverse exponential. It is not a claim for general positive (non-Markov) semigroups, other dimensions, weighted \(\ell^1\) norms, or pointwise asymptotic equality for every generator. The sharp constant is approached only in a large-rate limit of the displayed family, not asserted to be attained at finite nonzero generator norm. The inaccessible 1975 specialist source leaves a historical-priority risk. Independent mathematical audit has not been conducted.

## References
- J. Glück, “On the decoupled Markov group conjecture,” arXiv:2004.05995v1 (first posted 2020-04-13), https://arxiv.org/abs/2004.05995 ; published in *Bulletin of the London Mathematical Society*, DOI: 10.1112/blms.12416.
- “Exact priced spectral-abscissa design on a one-way three-state cycle,” published mathematical research record (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-exact-priced-spectral-abscissa-design-on-a-one-way-three-state-c--e5d1f1e388c4/RESULT.md .
- J. R. Cuthbert, “An Inequality with Relevance to the Markov Group Problem,” *Journal of the London Mathematical Society* (1975), DOI: 10.1112/jlms/s2-11.1.104. Full text not inspected.
