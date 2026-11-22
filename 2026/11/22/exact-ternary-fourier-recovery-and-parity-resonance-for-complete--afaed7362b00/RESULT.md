# Exact ternary Fourier recovery and parity resonance for complete bipartite colourings

## Finding

For integers \(m,n\ge1\), let \(G=(\mathbb Z/3\mathbb Z)^{m+n}\), with coordinates indexed by the two shores of the labelled complete bipartite graph \(K_{m,n}\). Let \(f:G\to\{0,1\}\) indicate its proper three-colourings, and let \(T_f h=f*h\) be **unnormalized** group convolution. Write \(\omega=e^{2\pi i/3}\), and use the Fourier convention \(\widehat f(\alpha,\beta)=\sum_{x\in G}f(x)\omega^{\langle (\alpha,\beta),x\rangle}\).

For \(\alpha\in(\mathbb Z/3\mathbb Z)^m\), \(\beta\in(\mathbb Z/3\mathbb Z)^n\), let \(s_A=\sum_i\alpha_i\), \(s_B=\sum_j\beta_j\) modulo three, \(t_A=\#\{i:\alpha_i=0\}\), and \(t_B=\#\{j:\beta_j=0\}\). Put \(u_A=(-1)^{m-t_A}2^{t_A}\), \(u_B=(-1)^{n-t_B}2^{t_B}\). Every multiplier is the *integer*

\[
\widehat f(\alpha,\beta)
=3\mathbf1_{\{s_A+s_B=0\}}(u_A+u_B+1)
-9\mathbf1_{\{s_A=s_B=0\}}.
\tag{1}
\]

Thus frequencies with \(s_A+s_B\ne0\) vanish. Within the translation-balanced hyperplane, **no further coefficient vanishes when at least one of \(m,n\) is odd**. When both shores are even, all further zeros are exactly the following mutually disjoint types:

* \(s_A=-s_B\ne0\), with \((t_A,t_B)=(0,1)\) or \((1,0)\);
* \(s_A=s_B=0\), with \((t_A,t_B)=(0,0),(2,1)\), or \((1,2)\).

For even \(r\ge2\), set

\[
U_r=(2^r+2)/3,\quad V_r=(2^r-1)/3,\quad
B_r=r(2^{r-1}-2)/3,\quad D_r=r(2^{r-1}+1)/3,\quad
E_r=\binom r2(2^{r-2}+2)/3.
\]

The number of *additional* zero multipliers in the translation-balanced hyperplane is exactly

\[
Z_{m,n}=U_mU_n+E_mB_n+B_mE_n+2(V_mD_n+D_mV_n)
\tag{2}
\]

when \(m,n\) are even, and \(Z_{m,n}=0\) otherwise. In particular,

\[
\operatorname{rank}T_f=3^{m+n-1}-Z_{m,n},\qquad
\operatorname{nullity}T_f=2\cdot3^{m+n-1}+Z_{m,n}.
\tag{3}
\]

The largest singular value is \(3(2^m+2^n-2)\). The smallest strictly positive singular value is **\(9\) if both shores are even**, and **\(3\) otherwise**. Consequently the sharp condition number on the recoverable Fourier range is \((2^m+2^n-2)/3\) when both sides are even and \(2^m+2^n-2\) otherwise. Equation (1), together with the exact multiplicities in the proof, gives the **entire signed multiplier spectrum**, not just rank and extremal magnitudes.

## Assumptions and scope

The graph is the simple labelled \(K_{m,n}\), with \(m,n\ge1\); each vertex takes one of the three elements of the additive group \(\mathbb Z/3\mathbb Z\); proper means adjacent endpoints have different colours. The ambient dimension is \(3^{m+n}\), and all multiplicities count complex Fourier characters with labels, not graph orbits. No quotient by global colour translations is taken. The Fourier transform and convolution are unnormalized, but diagonalization uses the unitary character basis, so Fourier magnitudes are precisely the convolution singular values. The condition number excludes zero singular values.

## Proof

**Two-shore decomposition.** Every proper ternary colouring has at least one monochromatic shore. Otherwise each shore contains at least two distinct colours, and the two disjoint palettes would require at least four colours. Count once the colourings with shore \(A\) monochromatic, once those with shore \(B\) monochromatic, and subtract those with both monochromatic and differently coloured. If shore \(A\) is monochromatic with colour \(a\), the character sum at every \(B\)-vertex is \(2\) when its frequency is zero and \(-\omega^{\beta_j a}\) otherwise; here \(\sum_{b\ne a}\omega^{\beta_jb}=-\omega^{\beta_j a}\) for nontrivial \(\beta_j\). Summing over the three choices of \(a\) gives \(3\mathbf1_{s_A+s_B=0}u_B\). Interchanging shores gives the analogous term with \(u_A\). The doubly monochromatic contribution is

\[
\sum_{a\ne b}\omega^{s_Aa+s_Bb}
=9\mathbf1_{s_A=s_B=0}-3\mathbf1_{s_A+s_B=0}.
\]

Inclusion–exclusion proves (1), including its signs, without approximation.

**Zero classification.** Every \(u_A,u_B\) is a nonzero *signed power of two*. For a balanced frequency with \(s_A=-s_B\ne0\), (1) vanishes iff \(u_A+u_B=-1\). The only ordered signed-power solutions are \((u_A,u_B)=(1,-2),(-2,1)\): after ordering opposite signs, \(2^a-2^b=1\) forces \((a,b)=(1,0)\). For \(s_A=s_B=0\), (1) vanishes iff \(u_A+u_B=2\). Its only ordered signed-power solutions are \((1,1),(4,-2),(-2,4)\). The equal positive case follows from \(2^a+2^b=2\); the opposite-sign cases from \(2^a-2^b=2\). In the definition \(u=(-1)^{\ell-t}2^t\), the values \(1,-2,4\) mean respectively \(t=0,1,2\) and \(\ell\) even. Thus all extra zeros require both shores even, with exactly the five support patterns stated.

**Exact counts.** With \(r\) nonzero ternary frequency coordinates, the numbers of \(\{1,2\}\)-words having sum \(s\in\mathbb Z/3\mathbb Z\) are

\[
N_r(0)=\frac{2^r+2(-1)^r}{3},\quad
N_r(1)=N_r(2)=\frac{2^r-(-1)^r}{3}.
\tag{4}
\]

This follows from the three-element character orthogonality identity. For even \(r\), \(U_r,V_r\) count all-nonzero words with sum zero or a specified nonzero sum, respectively; \(B_r,D_r\) count words with exactly one zero and the corresponding sums; \(E_r\) counts words with exactly two zeros and sum zero. The first zero pattern at sum zero contributes \(U_mU_n\), the other two contribute \(E_mB_n+B_mE_n\), while the two nonzero-sum patterns have two possible opposite residue pairs and contribute \(2(V_mD_n+D_mV_n)\). This proves (2). There are exactly \(3^{m+n-1}\) balanced characters in the ambient group; their complement consists of \(2\cdot3^{m+n-1}\) forced zeros. Thus (3) follows.

**Complete multiplicities and sharp gaps.** For arbitrary \(m,n\), choose \(t_A,t_B\) zero coordinates and shore sums \(s_A,s_B\). The exact number of frequencies in this class is

\[
\binom{m}{t_A}\binom{n}{t_B}
N_{m-t_A}(s_A)N_{n-t_B}(s_B),
\]

and (1) gives their common signed multiplier. This describes the full multiset. The number of colourings, obtained from the same inclusion–exclusion, is \(3(2^m+2^n-2)\); the trivial character attains it and the triangle inequality bounds every other multiplier by it. Also, because \((-1)^{\ell-t}2^t\equiv(-1)^\ell\pmod3\), if both shores are even every nonzero multiplier in (1) is divisible by nine. Frequencies with all entries nonzero and with opposite *nonzero* shore sums exist for each \(m,n\ge1\). At these frequencies \(u_A=(-1)^m\), \(u_B=(-1)^n\), so (1) has magnitude \(9\) for two even shores and \(3\) if at least one shore is odd. This proves both sharp minimal magnitudes and both condition numbers.

## Verification

The accompanying standalone `verify.py` constructs the complete indicator array and applies an **independent exact radix-three Fourier transform over \(\mathbb Z[\omega]\)**. It checks every individual Fourier multiplier against (1), then checks (2)–(3), maximal magnitude and sharp positive spectral gap for each ordered \(1\le m,n\le6\) with \(m+n\le9\). The observed result is `VERIFY_OK cases=30 exact full DFT m+n<=9`. Reproduce with `python3 verify.py`. All-width assertions follow from the preceding proof, not finite testing.

Representative ranks are \(15\) for \(K_{2,2}\), \(179\) for \(K_{2,4}\), \(1719\) for \(K_{4,4}\), and \(3^{m+n-1}\) whenever at least one shore is odd.

## Relationship to prior work

The older literature on chromatic symmetric functions and zero-temperature Potts models provides the underlying proper-colouring and external-field frameworks, but does not give the listed exact additive Fourier multiplier zeros, parity-sensitive rank or sharp convolution gap. In particular, the full set of frequency-specific coefficients in (1) is different from a colour-permutation-invariant chromatic enumerator. Later weighted chromatic polynomials allow variable vertex weights and thus provide a general *expression* in which such character sums can be encoded; their general polynomiality results are not an explicit classification of the zeros or exact ranks for this graph family. The closest published complete-bipartite Fourier result concerns **only the constant-plus-degree-one restriction Gram matrix**, not the full all-degree diagonal convolution spectrum; its positivity is compatible with the present even/even kernel. The three-colour forcing polynomial of complete bipartite graphs counts a different vertex-forcing event, not character cancellation. Other previously indexed results on cycle-colouring convolutions concern different graphs and do not imply the two-shore sign classification.

## Limitations

Only the ternary additive colour group and complete bipartite graphs are covered. The result neither determines analogous all-degree convolution spectra at other alphabet sizes nor asserts an extension to arbitrary graphs. The proof identifies an integer spectrum, but does not claim an explicit inverse kernel or its \(\ell^p\)-norms. A separately indexed or unindexed equivalent specialization of weighted Potts or chromatic theory remains a historical-priority risk; no independent mathematical validation has been performed.

## References

1. M. Klazar, M. Loebl, I. Moffatt, *The Potts model and chromatic functions of graphs*, arXiv:1311.4348v1, first public 2013-11-18. https://arxiv.org/abs/1311.4348
2. R. P. Stanley, *A Symmetric Function Generalization of the Chromatic Polynomial of a Graph*, Advances in Mathematics 111 (1995), 166–194. https://sites.math.washington.edu/~billey/classes/Hopf.algebra/bulletins/stanley.1995.pdf
3. Y. Liu, *On Chromatic Functors and Stable Partitions of Graphs*, arXiv:1603.08310, first public 2016-03-28. https://arxiv.org/abs/1603.08310
4. E. Bajo, M. Beck, A. R. Vindas-Meléndez, *q-Chromatic Polynomials*, arXiv:2403.19573, first public 2024-03-28. https://arxiv.org/abs/2403.19573
5. *Exact Fourier sampling spectra and a thin-side conditioning transition for bipartite colourings*, publicly indexed mathematical result, 2026-11-01.
6. *Forced three-colouring polynomial of complete bipartite graphs*, publicly indexed mathematical result, 2026-10-04.
