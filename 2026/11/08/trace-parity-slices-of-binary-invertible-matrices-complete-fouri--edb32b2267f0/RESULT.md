# Trace-parity slices of binary invertible matrices: complete Fourier nullity and distinct limiting losses

## Finding

For any integer \(n\ge2\), put \(V=M_n(\mathbb F_2)\), and split its invertible matrices according to ordinary matrix-trace parity:
\[
H_\epsilon=\{X\in\operatorname{GL}_n(\mathbb F_2):\operatorname{tr}(X)=\epsilon\},\qquad \epsilon\in\{0,1\}.
\]
The unnormalized additive convolution \(C_\epsilon f(Y)=\sum_{X\in H_\epsilon}f(Y+X)\) has **a complete, explicit real Fourier spectrum**, the rank of each convolution, and two different limiting kernel proportions. The exact spectral and nullity statements below hold in every dimension, not merely asymptotically.

For frequency \(A\in V\), write \(u(A)=\dim\ker A\), \(v(A)=\dim\ker(A+I)\), and define for \(0\le r\le n\)
\[
 F_n(r)=(-1)^r 2^{n(n-1)/2}\prod_{j=1}^{n-r}(2^j-1).
\]
Then the Walsh multiplier of \(C_\epsilon\) is
\[
 \boxed{\lambda_\epsilon(A)=\tfrac12\big(F_n(n-u(A))+(-1)^\epsilon F_n(n-v(A))\big).}
\]
To give all multiplicities define \(\left[{a\atop b}\right]_2\) as the Gaussian binomial coefficient (zero when \(b\notin[0,a]\)), and for nonnegative integers \(k,\ell\) set
\[
 M_n(k,\ell)=\begin{cases}
 \left[{n\atop k}\right]_2\left[{n-k\atop\ell}\right]_2
 2^{k\ell+n(n-k-\ell)},& k+\ell\le n,\\0,&k+\ell>n.
 \end{cases}
\]
Let \(\mathcal N_n(u,v)\) denote the number of matrices \(A\) with \(u(A)=u\), \(v(A)=v\). Exactly, for \(0\le u+v\le n\),
\[
 \boxed{\mathcal N_n(u,v)=\sum_{k=u}^{n}\sum_{\ell=v}^{n-k}
 (-1)^{k-u+\ell-v}2^{\binom{k-u}{2}+\binom{\ell-v}{2}}
 \left[{k\atop u}\right]_2\left[{\ell\atop v}\right]_2M_n(k,\ell).}
\]
(The sum is empty if the lower bound exceeds the upper bound.) Thus each value of the multiplier occurs with the indicated multiplicity, with coincident values added.

**Null spaces.** In the Walsh basis,
\[
 \boxed{\lambda_0(A)=0\iff (u(A),v(A))\in\{(0,1),(1,0)\},\qquad
 \lambda_1(A)=0\iff u(A)=v(A).}
\]
Hence
\[
 \boxed{\dim\ker C_0=2\mathcal N_n(0,1),\qquad
 \dim\ker C_1=\sum_{j=0}^{\lfloor n/2\rfloor}\mathcal N_n(j,j).}
\]
Neither operator is injective when \(n\ge2\), but their kernels are disjoint. Indeed, the joint measurement \(f\mapsto(C_0f,C_1f)\) is injective because \(C_0+C_1\) is the invertible convolution with the indicator of \(\operatorname{GL}_n(\mathbb F_2)\).

**Limiting losses.** Put \(Q_0=1\), \(Q_j=\prod_{a=1}^j(1-2^{-a})\), \(Q_\infty=\prod_{a=1}^\infty(1-2^{-a})\), and \(p_j=Q_\infty 2^{-j^2}/Q_j^2\). Then
\[
 \boxed{\lim_{n\to\infty}\frac{\dim\ker C_0}{2^{n^2}}=2p_0p_1=4Q_\infty^2=0.33359425545499\ldots,}
\]
\[
 \boxed{\lim_{n\to\infty}\frac{\dim\ker C_1}{2^{n^2}}=
 \sum_{j\ge0}p_j^2=Q_\infty^2\sum_{j\ge0}\frac{2^{-2j^2}}{Q_j^4}=0.43349405676202\ldots.}
\]
The first limiting loss is about one-third of the Fourier directions, the second about forty-three percent. The positive singular values themselves are \(|\lambda_\epsilon(A)|\); no normalization is hidden.

## Assumptions and scope

All vector spaces and matrices are over \(\mathbb F_2\). The Walsh character indexed by \(A\) is \(\chi_A(X)=(-1)^{\langle A,X\rangle}\), where \(\langle A,X\rangle=\sum_{i,j}A_{ij}X_{ij}\in\mathbb F_2\). Ordinary matrix trace is \(\operatorname{tr}X=\sum_iX_{ii}\). The Fourier transform uses an **unnormalized** sum, while the convolution acts on \(\mathbb C^V\), of dimension \(2^{n^2}\). The formulas apply to all integer dimensions \(n\ge2\) and both trace parities. No assertion is made about other fields or other matrix constraints.

## Proof

**1. Rank-only Fourier transform.** For any \(A\), let \(S_n(A)=\sum_{X\in\operatorname{GL}_n(\mathbb F_2)}\chi_A(X)\). By subspace-lattice Möbius inversion,
\[
 \mathbf1_{\{\ker X=0\}}=\sum_{U\le\ker X}(-1)^{\dim U}2^{\binom{\dim U}{2}}.
\]
For fixed \(U\) of dimension \(k\), there are \(2^{n(n-k)}\) maps \(X\) killing \(U\). The signed Fourier sum over them vanishes unless the row space of \(A\) lies in the dual subspace associated with \(U\), in which case it equals that power of two. If \(\operatorname{rank}A=r\), the number of such \(k\)-subspaces is \(\left[{n-r\atop k-r}\right]_2\). Consequently
\[
 S_n(A)=\sum_{k=r}^n (-1)^k2^{\binom k2+n(n-k)}
 \left[{n-r\atop k-r}\right]_2.
\]
The finite \(2\)-Gaussian binomial identity evaluates this to \(F_n(r)\). (This rank-shell transform is classical, not asserted as a new result; see Delsarte.)

**2. Trace-parity splitting.** Over \(\mathbb F_2\), \(\chi_I(X)=(-1)^{\operatorname{tr}X}\). The identity
\[
 \mathbf1_{H_\epsilon}(X)=\tfrac12\mathbf1_{\operatorname{GL}_n}(X)
 \big(1+(-1)^\epsilon\chi_I(X)\big)
\]
shows the multiplier is \(\tfrac12(S_n(A)+(-1)^\epsilon S_n(A+I))\). This proves the spectral formula.

**3. Joint nullity multiplicities.** For a matrix \(A\), write \(U_A=\ker A\), \(W_A=\ker(A+I)\). The two subspaces meet trivially, since \(Av=0\) and \((A+I)v=0\) force \(v=0\). The number of ordered pairs of disjoint subspaces \(U,W\) with dimensions \(k,\ell\) is
\[
 \left[{n\atop k}\right]_2\left[{n-k\atop\ell}\right]_2 2^{k\ell}.
\]
After choosing them, the constraints \(A|_U=0\) and \(A|_W=I\) permit exactly \(2^{n(n-k-\ell)}\) linear-map extensions. Thus
\[
 M_n(k,\ell)=\sum_{u\ge k,v\ge\ell}
 \left[{u\atop k}\right]_2\left[{v\atop\ell}\right]_2\mathcal N_n(u,v).
\]
Two applications of the finite Gaussian-binomial inversion identity
\[
 b_k=\sum_{j\ge k}\left[{j\atop k}\right]_2 a_j
 \quad\Longrightarrow\quad
 a_u=\sum_{k\ge u}(-1)^{k-u}2^{\binom{k-u}{2}}
 \left[{k\atop u}\right]_2 b_k
\]
give precisely the displayed double sum. This also proves \(\sum_{u,v}\mathcal N_n(u,v)=2^{n^2}\).

**4. Exact zeros and joint reconstruction.** The nonzero magnitudes \(|F_n(r)|\) strictly decrease as \(r\) increases, with the unique exception \(|F_n(n-1)|=|F_n(n)|\); that exceptional pair has opposite signs. Therefore \(F_n(r)+F_n(s)=0\) holds only for \(\{r,s\}=\{n-1,n\}\), while \(F_n(r)-F_n(s)=0\) holds only for \(r=s\). These are the two stated nullity criteria. Since \(F_n(r)\ne0\) always, \(C_0+C_1\) is invertible and the kernels cannot intersect.

**5. Limiting independent fixed spaces.** Divide \(M_n(k,\ell)\) by \(2^{n^2}\). Writing \(|\operatorname{GL}_j(\mathbb F_2)|=2^{j^2}Q_j\), a direct simplification gives
\[
 \frac{M_n(k,\ell)}{2^{n^2}}=
 \frac{\prod_{a=0}^{k+\ell-1}(1-2^{a-n})}
 {|\operatorname{GL}_k(\mathbb F_2)|\,|\operatorname{GL}_\ell(\mathbb F_2)|},
 \qquad k+\ell\le n.
\]
For each fixed \(k,\ell\), this tends to the product of the one-variable Gaussian moments \(1/|\operatorname{GL}_k|\) and \(1/|\operatorname{GL}_\ell|\). The latter moments determine the classical limiting nullity law \(p_j\) (see Fulman–Goldstein). The double Gaussian-inversion series is absolutely dominated by a summable bound of the form \(C_{u,v}2^{-(k^2+\ell^2)/4}\): indeed the inversion multipliers grow at most quadratically in \(k,\ell\) with leading exponent one-half, whereas \(|\operatorname{GL}_k|^{-1}|\operatorname{GL}_\ell|^{-1}\) decays with leading exponent minus one. Taking the limit termwise yields \(\Pr(u=j,v=k)\to p_jp_k\) for each pair. Tightness follows directly from \(\Pr(u\ge K)\le M_n(K,0)/2^{n^2}\le |\operatorname{GL}_K|^{-1}\), and similarly for \(v\). Thus the full joint laws converge to independent copies, and the stated zero-mode limits follow by bounded convergence and the exact zero criteria. In particular \(p_0=Q_\infty\) and \(p_1=2Q_\infty\).

## Verification

The accompanying standalone `verify_trace_GL.py` uses Python 3 standard-library exact integers. It enumerates every one of the \(2^{n^2}\) frequency matrices in dimensions \(n=1,2,3,4\), forms both trace-restricted invertible sets, computes their entire Walsh transforms by exact butterfly operations, and independently compares every transform coefficient with the closed multiplier formulas. It verifies every joint multiplicity by direct enumeration versus double Gaussian inversion. The exact nullities for \(n=2,3,4\) are \((6,8)\), \((196,216)\), and \((23280,28224)\), respectively, ordered as even/odd trace. The script ends with `TRACE_SLICE_BINARY_GL_EXACT_CHECKS_OK`. The infinite-family and limiting statements depend on the proof, not on finite checks.

## Relationship to prior work

Delsarte's rank-metric association scheme gives the full character transform of a rank shell; the rank-only transform in Step 1 is a classical specialization. Fulman's cycle-index treatment of all finite matrices contains substantially stronger information about individual rational-canonical-form components, and can in principle generate the joint eigenspace multiplicities here. Fulman–Goldstein give the one-variable finite-field nullity distribution and its limit. The distinct mathematical statement established here is the trace-parity-sliced **convolution** spectrum, the exact two different kernel criteria, the explicit resulting finite nullities, and the two contrasting information-loss constants. None of the materially inspected sources states this paired parity-restricted spectral classification. This is a bounded comparison, not a universal novelty or priority guarantee.

## Limitations

The result concerns additive convolution on the whole binary matrix space, not convolution in the multiplicative group of invertible matrices. All eigenvalue multiplicities count additive Walsh modes, not matrix similarity classes. The asymptotic density calculations take \(n\to\infty\) with field order fixed at two. Existing rank-shell transforms and classical random-matrix distributions are antecedents, not rediscovered theorems. Broader cycle-index and trace-hyperplane literature may contain an equivalent consequence. No independent mathematical audit has been performed.

## References

1. Ph. Delsarte, *Bilinear forms over a finite field, with applications to coding theory*, Journal of Combinatorial Theory A 25 (1978), 226–241, DOI `10.1016/0097-3165(78)90015-8` (particularly Sections 2–3 and Appendix Theorem A2).
2. J. Fulman, *Random matrix theory over finite fields: a survey*, arXiv `math/0003195`, first public version 28 March 2000 (particularly Sections 2.1–2.2, the full-matrix cycle index).
3. J. Fulman and L. Goldstein, *Stein's method and the rank distribution of random matrices over finite fields*, arXiv `1211.0504`, first version 2 November 2012 (particularly Section 1, nullity laws).
4. J. Fulman and D. Stanton, *On the distribution of the number of fixed vectors for the finite classical groups*, arXiv `1505.06383`, first version 23 May 2015 (particularly Section 1, known eigenspace distribution antecedents).
