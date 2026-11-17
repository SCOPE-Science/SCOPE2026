# Exact boundary-dependent bounded-variation gain of one-level Haar sign reflection

## Finding

For any even block length \(L\ge2\) and number of blocks \(b\ge1\), let \(n=bL\). The signed Haar reflection \(R_L=I-2D_L\), defined below, has the exact path total-variation amplification

\[
C(L,b)=\begin{cases}
1+c_b,&L=2,\\
1+(2+c_b)(1-2/L),&L\ge4,
\end{cases}
\qquad c_b=\begin{cases}0,&b=1,\\1,&b=2,\\2,&b\ge3.\end{cases}
\]

The coefficient is attained by a one-jump input. The sharp universal bound over all even \(L\) and positive \(b\) is \(5\), with strict inequality for every finite length. For block lengths \(L=2^s\), this is exactly a sign reversal of one full Haar resolution level on a finite dyadic grid.

## Assumptions and scope

Index real coordinates by \(1,\ldots,n\). Divide them into ordered blocks \(B_t=\{(t-1)L+1,\ldots,tL\}\) for \(1\le t\le b\). In each block let \(h_t\) be \(+1\) on its first \(L/2\) coordinates, \(-1\) on its last \(L/2\), and zero elsewhere. Define

\[
D_Lx=\sum_{t=1}^{b}\frac{\langle x,h_t\rangle}{L}h_t,\qquad R_Lx=x-2D_Lx,
\qquad V(x)=\sum_{i=1}^{n-1}|x_{i+1}-x_i|.
\]

The contrasts are orthogonal and have squared Euclidean norm \(L\); hence \(D_L\) is an orthogonal projection and \(R_L\) is an orthogonal involution. Constants are fixed by \(R_L\). All signs, endpoints and variations are real; there is no periodic closing edge.

## Proof

Since \(R_L\mathbf1=\mathbf1\), every signal has the telescoping representation \(x=x_1\mathbf1+\sum_{j=1}^{n-1}(x_{j+1}-x_j)\mathbf1_{\{i>j\}}\). By linearity and the triangle inequality,

\[
V(R_Lx)\le \max_{1\le j<n}V(R_L\mathbf1_{\{i>j\}})\,V(x).
\]

Each nontrivial step has input variation exactly one, so the right-hand maximum is also a lower bound: the induced coefficient is exactly the largest transformed step variation.

Fix such a step. If its jump is at a block boundary, every block is constant and \(D_L\) vanishes, giving variation one. Otherwise the jump lies at local position \(q\in\{1,\ldots,L-1\}\) inside one block. Let \(a=2\min(q,L-q)/L\). On that block, \(R_L\) adds \(+a\) to the first half and \(-a\) to the second half; it leaves all other blocks unchanged. If \(q\ne L/2\), there is one original jump of size one within a half, a new midpoint jump of magnitude \(2a\), and one extra boundary jump of magnitude \(a\) at each end of the active block that is not an endpoint of the entire path. If \(c\in\{0,1,2\}\) is the number of such active-block ends, the resulting variation is

\[
V(R_L\mathbf1_{\{i>j\}})=1+(2+c)a \qquad(q\ne L/2).
\]

If \(q=L/2\), the original midpoint jump is simply reversed and each available outer block end contributes one, so the variation is \(1+c\). For \(L=2\) only this midpoint case exists. For \(L\ge4\), the maximal non-midpoint value of \(a\) is \(1-2/L\), attained at \(q=L/2\pm1\); the resulting coefficient \(1+(2+c)(1-2/L)\) is at least \(1+c\), since \(L\ge4\) and \(c\le2\). This proves the blockwise formula.

If \(b=1\), an active block has \(c=0\); if \(b=2\), it has \(c=1\); if \(b\ge3\), an interior active block with \(c=2\) exists. Choosing the corresponding step establishes the stated sharp constants and equality cases. For \(L\ge4\), the largest formula is \(5-8/L\), strictly below five at every finite length but converging to five as \(L\to\infty\), taking \(b\ge3\). For \(L=2\), the coefficient is at most three. This proves the universal envelope and its finite nonattainment.

## Verification

The standalone `verify.py` uses exact rational arithmetic. It exhausts every step input for all even \(L\in\{2,4,\ldots,24\}\) and \(1\le b\le6\), checks that the maximum equals the formula, and tests selected arbitrary rational signals, as well as the involution identity. Recorded output:

```text
EXACT_ALL_STEPS_AND_SHARP_WITNESSES_PASS 3204 72
EXACT_GENERAL_INPUT_AND_INVOLUTION_CHECKS_PASS 350
ALL_BLOCK_HAAR_VARIATION_CHECKS_PASS
```

These finite checks support the unrestricted elementary proof, not replace it. Reproduce using `python verify.py` with a Python standard-library interpreter.

## Relationship to prior work

Cohen, Dahmen, Daubechies and DeVore (2003) establish BV wavelet-coefficient estimates and discuss failure of uniform unconditional bases, but do not state the sharp finite-block reflected-contrast coefficient above. Osȩkowski (2013) derives sharp restricted weak-type bounds for Haar projections in \(L^p\), not path variation. Steidl, Weickert, Brox, Mrázek and Welk (2004, publicly circulating as a 2003 preprint) analyze nonnegative soft shrinkage and its connection to TV diffusion; their coefficient operation does not reverse the sign of a full Haar level. The present result isolates the exact path-boundary effect of such a reflection, rather than a general nonlinear shrinkage bound.

## Limitations

The exact formula assumes a uniform even block length, equal observation masses, full-block Haar contrast signs and unweighted open-path variation. It makes no claim for arbitrary wavelet sign patterns across multiple levels, nonuniform block weights, other wavelet families or cyclic variation. Historical priority is not independently certified.

## References

1. A. Cohen, W. Dahmen, I. Daubechies and R. DeVore, *Harmonic Analysis of the space BV*, Rev. Mat. Iberoam. 19 (2003), 235–263. https://doi.org/10.4171/RMI/345
2. A. Osȩkowski, *Sharp Inequalities for the Haar System and Fourier Multipliers*, J. Function Spaces (2013), article 646012. https://doi.org/10.1155/2013/646012
3. G. Steidl, J. Weickert, T. Brox, P. Mrázek and M. Welk, *On the Equivalence of Soft Wavelet Shrinkage, Total Variation Diffusion, Total Variation Regularization, and SIDEs*, SIAM J. Numer. Anal. 42 (2004), 686–713. https://doi.org/10.1137/S0036142903422429
