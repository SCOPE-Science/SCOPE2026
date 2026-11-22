# Riordan spectral gaps and full Walsh recovery from Motzkin horizontal-step profiles

## Finding

For every integer \(n\ge 0\), let \(\mathcal M_n\) be the set of Motzkin excursions of length \(n\), with steps \(U=(1,1)\), \(D=(1,-1)\), \(H=(1,0)\), starting and ending at height zero and never going below zero. Encode a path by the binary indicator \(z\in\mathbb F_2^n\) of the *positions of all horizontal steps*, including those at positive height. Let \(\mu_n(z)\) count paths with this indicator, and define counting convolution \((T_ng)(x)=\sum_{z\in\mathbb F_2^n}\mu_n(z)g(x+z)\). All Fourier transforms below are **unnormalized**.

Let \(M_n=|\mathcal M_n|\), and let \(R_m\) count Riordan paths of length \(m\), namely Motzkin excursions with no horizontal steps at height zero. Put \(m=\lfloor n/2\rfloor\). Then:

1. A Walsh multiplier \(\widehat\mu_n(S)=\sum_z\mu_n(z)(-1)^{\langle S,z\rangle}\) depends only on \(r=|S|\); write it \(W_n(r)\). For \(0\le r\le m\), these are nonnegative integers satisfying \(W_n(0)\ge W_n(1)\ge\cdots\ge W_n(m)=R_m\), and \(W_n(n-r)=(-1)^nW_n(r)\).
2. For \(n\ge4\), every multiplier is nonzero, and \(\min_S|\widehat\mu_n(S)|=R_{\lfloor n/2\rfloor}>0\). The maximum absolute multiplier is \(M_n\). Hence \(T_n\) is invertible on every real or complex \(\ell^2(\mathbb F_2^n)\), with exact inverse operator norm \(1/R_{\lfloor n/2\rfloor}\) and sharp spectral condition number \(M_n/R_{\lfloor n/2\rfloor}\).
3. At lengths \(n=2,3\), the nullities are respectively \(2,6\), and the ranks are both \(2\). At lengths \(n=0,1\), convolution is invertible. Thus singularity occurs **only** at lengths two and three.
4. For every even \(n\), \(T_n\) is positive semidefinite (positive definite when \(n\ne2\)); for every odd \(n\ge5\), precisely the characters with \(|S|>n/2\) have negative eigenvalue. No statements about the two-bit up/down encoding's full spectrum are implied.

In particular, the \(n=10\) horizontal-step convolution is invertible with smallest multiplier \(R_5=6\), despite the classical Motzkin path count \(M_{10}=2188\) being even.

## Assumptions and scope

The graph/group is \(G_n=(\mathbb Z/2\mathbb Z)^n\), with the convention \(G_0\) is the trivial group. A coordinate of \(z\) is \(1\) exactly at a horizontal step and \(0\) at either an up or a down step. Repeated profiles are counted with multiplicity. The Fourier characters are \(\chi_S(z)=(-1)^{\sum_{i\in S}z_i}\). In particular, this is not the different embedding that records up and down positions separately in \(\mathbb F_2^{2n}\).

For a fixed indicator \(z\) with \(h=|z|\), deleting the \(h\) horizontal steps leaves a Dyck excursion of length \(n-h\). Conversely all placements of any such Dyck excursion reconstruct a unique Motzkin excursion with indicator \(z\). Thus
\[
\mu_n(z)=\begin{cases}C_{(n-h)/2},&n-h\text{ even},\\0,&n-h\text{ odd},\end{cases}\qquad C_k=\frac1{k+1}\binom{2k}{k}.
\]
This also gives an independent exact formula, with \([t^j]\) denoting coefficient extraction:
\[
W_n(r)=\sum_{k=0}^{\lfloor n/2\rfloor}C_k[t^{n-2k}](1-t)^r(1+t)^{n-r}.
\]

## Proof

Let \(A\) be the adjacency operator of the nonnegative integer half-line, on basis vectors \(e_0,e_1,\ldots\): \(Ae_0=e_1\), and \(Ae_h=e_{h-1}+e_{h+1}\) for \(h\ge1\). Its powers are well-defined on every finitely supported vector. Each up or down step contributes \(A\), while a horizontal step in a signed path contributes \(+I\) or \(-I\), depending on whether its position lies outside or inside \(S\). All factors commute because they are polynomials in \(A\). Therefore
\[
W_n(r)=\langle e_0,(A+I)^{n-r}(A-I)^re_0\rangle.
\]
This identity includes both the boundary at height zero and all path multiplicities.

Define \(B=A^2-I\). Its matrix entries in the basis \(e_h\) are all nonnegative: \(Be_0=e_2\), and for \(h\ge1\), \(Be_h=e_{h-2}+e_h+e_{h+2}\) when \(h\ge2\), while \(Be_1=e_1+e_3\). In particular, on even heights \(0,2,4,\ldots\), \(B\) is the transition operator for a Motzkin path with a forbidden horizontal step at height zero, after dividing heights by two. As \((A+I)(A-I)=B\), for \(0\le r\le\lfloor n/2\rfloor\),
\[
W_n(r)=\langle e_0,(A+I)^{n-2r}B^re_0\rangle\ge0.
\]
Each matrix element in this expression is an integer sum of nonnegative walk weights. Furthermore, if \(r+1\le n/2\), commuting the factors gives
\[
\begin{aligned}
W_n(r)-W_n(r+1)
&=\langle e_0,(A+I)^{n-2r-2}\big((A+I)^2-B\big)B^re_0\rangle\\
&=2\langle e_0,(A+I)^{n-2r-1}B^re_0\rangle\ge0,
\end{aligned}
\]
because \((A+I)^2-B=2(A+I)\) and both \(A+I\) and \(B\) are entrywise nonnegative.

For \(n=2m\), at the central frequency \(W_{2m}(m)=\langle e_0,B^me_0\rangle=R_m\). For \(n=2m+1\), \(W_{2m+1}(m)=\langle e_0,(A+I)B^me_0\rangle=R_m\), since \(B\) preserves height parity and \(\langle e_0,AB^me_0\rangle=0\). Here \(R_0=1\), \(R_1=0\), and \(R_m>0\) for all \(m\ge2\): a path goes up, stays at height one for \(m-2\) steps, and goes down. Thus nonnegativity and monotonicity yield strict positivity at every lower-half weight for \(n\ge4\).

Finally let \(Pe_h=(-1)^he_h\). Then \(PAP=-A\), \(PIP=I\) and \(Pe_0=e_0\), so replacing \(r\) by \(n-r\) in the transfer expression yields \(W_n(n-r)=(-1)^nW_n(r)\). This gives the full sign classification and absolute spectral minimum. At \(n=2\), the frequency list by weight is \((2,0,2)\), with weight-one multiplicity two; at \(n=3\), it is \((4,0,0,-4)\), with weights one and two contributing six zeros. The length-zero and length-one lists are \((1)\) and \((1,-1)\). The character basis diagonalizes convolution with eigenvalues \(W_n(|S|)\), and \(|W_n(r)|\le M_n=W_n(0)\) by the triangle inequality; hence all rank, positivity, inverse-norm and condition-number assertions follow.

## Verification

The standalone \(verify.py\) uses standard-library integer arithmetic only. It directly enumerates every Motzkin excursion through length twelve, groups them by their actual horizontal-position masks, checks each profile against the Catalan formula, performs an integer fast Walsh transform, and independently compares every frequency with transfer counts from \(B\) and \(A+I\). It checks the initial Riordan numbers and the symmetry, nonnegativity, weak monotonicity and sharp central gap of the transfer through length sixty. The supplied run passed 18,430 exact assertions. This finite calculation corroborates but is not substituted for the all-size proof above.

To reproduce:

```bash
python3 verify.py
```

## Relationship to prior work

The established Motzkin-path deletion/counting identity and classical Riordan-path sequence are used as inputs, not claimed as new. Chen, Deng and Yang (2006) give the Riordan-path interpretation and recurrence; Sun and Ma (2013) investigate weighted partial Motzkin paths using *height-dependent* weights and Riordan-array minors. The present statement instead concerns independent **position-dependent** character signs, all Fourier frequencies, zero-free deconvolution and the exact sharp spectral gap.

A previously recorded finite Fourier census for Motzkin paths of length ten uses **two bits at every position** to encode up and down steps, rather than the one-bit indicator for horizontal positions. The latter is an affine projection of the former: for admissible ternary steps, the horizontal bit is \(1+u_i+d_i\) in \(\mathbb F_2\). Consequently our Fourier multipliers form an affine-sign-adjusted **diagonal restriction** of the two-bit spectrum, not the complete two-bit spectrum. That finite census neither supplies an all-length zero-free result for this restriction nor the Riordan gap; conversely our result makes no claims about the non-diagonal modes of the two-bit encoding. A stronger unknown multivariate weighted enumeration could conceivably imply the theorem; the priority assessment remains bounded by the specified sources.

## Limitations

The result is restricted to ordinary (unrestricted-height) Motzkin excursions and the complete count of horizontal positions. It does not cover peak-restricted paths, weights dependent on local height, non-binary Fourier groups, or arbitrary signed up/down characters. The spectral gap is for the unnormalized counting convolution, not a probability-normalized operator. This report is a mathematical proof with finite reproducibility checks, not independent external certification.

## References

1. William Y. C. Chen, Eva Y. P. Deng and Laura L. M. Yang, *Riordan Paths and Derangements*, first public arXiv record 2006-02-14, https://arxiv.org/abs/math/0602298 .
2. Yidong Sun and Luping Ma, *Minors of a Class of Riordan Arrays Related to Weighted Partial Motzkin Paths*, first public arXiv record 2013-05-09, https://arxiv.org/abs/1305.2015 .
3. A previously recorded *First post-cubic Walsh resonance and exact Fourier range projection for length-ten Motzkin paths*, scientific identifier `5e973760-c6a6-439e-8833-96d9b2b74f9c` (distinct two-bit incidence encoding).
