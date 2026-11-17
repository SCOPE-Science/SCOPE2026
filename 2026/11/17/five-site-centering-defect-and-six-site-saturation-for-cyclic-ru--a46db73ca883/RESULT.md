# Five-site centering defect and six-site saturation for cyclic running medians

## Finding
For each integer \(n\ge 2\), define the cyclic three-point running median on real sequences by
\[
(T_nx)_i=\operatorname{med}(x_{i-1},x_i,x_{i+1}),\qquad i\in\mathbb Z/n\mathbb Z,
\]
where repeated indices at \(n=2\) are retained in the three-entry multiset. Let \(Q_n=I-\mathbf1\mathbf1^{\mathsf T}/n\) and let \(H_n(x)=\|Q_nx\|_2\), the root-sum-square deviation from the sample mean. The sharp two-input, translation-invariant Lipschitz constant is
\[
\boxed{\sup_{H_n(x-y)>0}\frac{H_n(T_nx-T_ny)}{H_n(x-y)}=
\begin{cases}1,&n=2,\\0,&n=3,\\\sqrt2,&n=4,5,\\\sqrt3,&n\ge6.\end{cases}}
\]
All positive sharp constants are attained by arbitrarily close pairs of distinct-valued input sequences. Thus the universal three-replication ceiling \(\sqrt3\) is first attained at six sites, whereas five sites have only \(\sqrt2\) centered amplification. This is a genuine centering effect: ordinary uncentered \(\ell_2\) input/output perturbations permit the replication ceiling already at five sites.

## Assumptions and scope
The underlying space is \(\mathbb R^n\), with uniform cyclic windows of length three, unit observation weights, and the centered Euclidean seminorm. Inputs may have arbitrary signs. The Lipschitz ratio is taken over all pairs whose difference is not constant; constant perturbations cause constant output perturbations because \(T_n(x+c\mathbf1)=T_n(x)+c\mathbf1\). No iteration, weighting, or noncyclic boundary condition is asserted.

## Proof
**1. Linear chambers and global Lipschitz bounds.** On every open strict-order chamber \(x_{\sigma(1)}<\cdots<x_{\sigma(n)}\), the median selects one input coordinate in each output row. Therefore \(T_nx=S_\sigma x\) on that chamber, where each row of \(S_\sigma\) contains one entry equal to one, the rest zero. Since the cyclic median is continuous and piecewise linear, the global constant equals the maximum of the quotient-operator norms \(\|Q_nS_\sigma Q_n\|_{2\to2}\) over the finitely many chambers. For the upper bound, integrate the local linearization along any segment (finitely many exceptional boundaries do not affect the result); for the lower bound, perturb a strictly ordered point along any maximizing direction while remaining in its chamber. Translation equivariance permits replacing every perturbation by its mean-zero representative.

**2. Universal ceiling.** For \(n\ge4\), an input coordinate \(j\) appears in only three candidate output windows, those centered at \(j-1,j,j+1\). If \(c_j\) is the number of rows of \(S_\sigma\) choosing column \(j\), then \(0\le c_j\le3\) and for any mean-zero \(h\),
\[
\|Q_nS_\sigma h\|_2^2\le\|S_\sigma h\|_2^2
=\sum_j c_j h_j^2\le3\|h\|_2^2.
\]
Hence the Lipschitz constant is at most \(\sqrt3\) in all dimensions \(n\ge4\).

**3. Exhaustive small-dimension certificate.** For \(n=4,5\) the stronger inequality \(\|Q_nS_\sigma Q_n\|_{2\to2}^2\le2\) holds in every strict-order chamber. This is an exact *exhaustive finite verification*, not a sample: ranks \(0,\ldots,n-1\) enumerate all \(n!\) strict orders and produce, respectively, 12 and 60 distinct selector matrices. Set \(C_n=nI-\mathbf1\mathbf1^{\mathsf T}=nQ_n\). For each enumerated selector \(S\), `CHECK.py` builds the integer symmetric matrix
\[
B_n(S)=2n^2C_n-C_nS^{\mathsf T}C_nSC_n
=n^3\bigl(2Q_n-Q_nS^{\mathsf T}Q_nSQ_n\bigr).
\]
It certifies that every \(B_n(S)\) is positive semidefinite using exact rational Schur-complement elimination (positive pivots and zero rows only; any negative pivot or nonzero zero-diagonal block fails). The complete enumeration covers 24 orders for \(n=4\) and 120 orders for \(n=5\), with no symmetry assumptions or discarded cases. Thus the squared quotient norm is at most two. At \(n=2\), the output swaps the two values and has constant one; at \(n=3\), all three cyclic windows coincide as multisets, giving a constant output and seminorm zero.

**4. Attainment below six sites.** For \(n=4\), take \(x=(1,0,2,3)\) and \(h=e_0-e_2\). The induced selector is \((0,0,2,2)\), and \(S h=(1,1,-1,-1)\), so \(H_4(Sh)^2/H_4(h)^2=4/2=2\). For \(n=5\), take \(x=(0,3,4,1,2)\) and \(h=e_1-e_4\). The selector is \((4,1,1,4,3)\), giving \(S h=(-1,1,1,-1,0)\), again squared ratio two. In both cases \(x\) has distinct values, so \(T_n(x+\varepsilon h)-T_n(x)=\varepsilon Sh\) for all sufficiently small nonzero \(\varepsilon\), proving attained sharpness. To compare the uncentered geometry directly, the five-site input \(x=(0,2,3,1,4)\) has selector \((1,1,1,2,3)\); the ordinary \(\ell_2\) perturbation \(h=e_1\) has squared input norm one and squared output norm three. Thus the raw \(\sqrt3\) gain at five sites does not survive mean centering.

**5. All \(n\ge6\).** For \(n=6\), set \(x=(0,2,4,1,3,5)\). For every \(n\ge7\), extend these first six values by \(x_6=5/2\) and \(x_j=2+1/(j+1)\) for \(7\le j<n\). These values are all pairwise distinct. Direct comparison of the three entries in each of the first six windows shows that the selector chooses column \(1\) at outputs \(0,1,2\) and column \(4\) at outputs \(3,4,5\); neither column can be selected elsewhere. With \(h=e_1-e_4\), the input has zero mean and squared norm two, while \(Sh=(1,1,1,-1,-1,-1,0,\ldots,0)\) also has zero mean and squared norm six. Thus \(H_n(Sh)/H_n(h)=\sqrt3\). Small same-chamber perturbations attain this ratio. The universal ceiling from step 2 completes the proof.

## Verification
Run `python3 CHECK.py` using only the Python 3 standard library. It exhausts all strict-order permutations at dimensions two through five, verifies the integer-matrix positive-semidefiniteness certificates with exact fractions, and reproduces the small-dimensional sharp witnesses. It also diagnoses the explicit family through dimension 100 with exact arithmetic; these latter diagnostics do **not** stand in for the uniform construction proved in step 5. There is no appeal to floating-point eigenvalue comparisons or incomplete enumeration for the finite cases.

## Relationship to prior work
Maragos and Schafer (1987) provide the order-statistic and max-min representations of median filters; these establish the relevant nonlinear-filter setting, not the centered two-input quotient norm. Little and Jones (2011) prove one-input total-variation diminution for three-point medians, a different question and seminorm. The published result *Arithmetic saturation of the Lipschitz amplification of cyclic running medians* calculates ordinary \(\ell_p\) amplification and hence gives an especially close comparison: ordinary \(\ell_2\) amplification can reach \(\sqrt3\) at five sites, whereas centering reduces the sharp five-site constant to \(\sqrt2\); its uncentered result therefore does not directly imply the centered classification. The published result *Sharp BV perturbation threshold for cyclic three-point medians* concerns cyclic adjacent-edge variation and is not an equivalent Hilbert quotient statement. The closest two public finding records were available as summaries, while their full documents were inaccessible, leaving a residual priority risk rather than a claim of exhaustive historical uniqueness.

## Limitations
The theorem covers only a single application of the uniform three-point median on finite real cycles and its mean-centered Euclidean seminorm. Other window sizes, repeated filtering, weighted observations, irregular neighborhoods, and arbitrary norm geometries are not covered. The small-dimension upper bound uses a complete finite exact certificate supplied with the result, not a simple closed-form chamber-free inequality. The originality comparison is qualified because the most relevant public finding texts could not be inspected in full. No independent mathematical validation has occurred.

## References
1. P. Maragos and R. W. Schafer, *Morphological filters—Part II: Their relations to median, order-statistic, and stack filters*, IEEE Transactions on Acoustics, Speech, and Signal Processing **35** (1987), 1170–1184, DOI 10.1109/TASSP.1987.1165254. Author bibliographic listing: https://robotics.ntua.gr/members/maragos/ ; original report: https://drum.lib.umd.edu/items/95ac7d84-40fc-46bd-9e9e-936ef1bbcb34 .
2. M. A. Little and N. S. Jones, *Generalized methods and solvers for noise removal from piecewise constant signals. I. Background theory*, Proc. R. Soc. A **467** (2011), 3088–3114, https://pmc.ncbi.nlm.nih.gov/articles/PMC3191861/ , Appendix A.
3. *Arithmetic saturation of the Lipschitz amplification of cyclic running medians*, published finding record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-arithmetic-saturation-of-the-lipschitz-amplification-of-cyclic-r--b3edfc2b2f2a . Only the indexed scientific summary was accessible.
4. *Sharp BV perturbation threshold for cyclic three-point medians*, published finding record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-bv-perturbation-threshold-for-cyclic-three-point-medians--59530ef626eb . Only the indexed scientific summary was accessible.
