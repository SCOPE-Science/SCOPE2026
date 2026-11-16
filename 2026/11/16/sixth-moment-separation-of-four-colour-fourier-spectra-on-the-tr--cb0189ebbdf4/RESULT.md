# Sixth-moment separation of four-colour Fourier spectra on the triangular prism

## Finding

Let \(G=K_3\square K_2\) be the triangular prism and let the four named colours carry either of the two abelian group laws \(H_{\mathrm{cyc}}=\mathbb Z/4\mathbb Z\) or \(H_{\mathrm{Kl}}=(\mathbb Z/2\mathbb Z)^2\). For each group \(H\), write \(C_H\subset H^6\) for the proper vertex colourings, \(f_H=1_{C_H}\), and \(W_H\) for the unnormalised finite-group Fourier transform of \(f_H\). Both colouring sets contain 264 assignments. The **complete absolute multiplier distributions** (multiplicities at the indicated magnitude) are:

| \(|W_H|\) | Cyclic group | Klein group |
|:--:|--:|--:|
| 0 | 3072 | 3072 |
| 8 | 348 | 408 |
| 24 | 399 | 291 |
| 40 | 198 | 258 |
| 56 | 30 | 18 |
| 72 | 9 | 9 |
| 88 | 39 | 39 |
| 264 | 1 | 1 |

Consequently, counting convolution by \(f_H\) has rank \(1024\) on \(\mathbb C^{H^6}\) for both groups. Its smallest positive singular value is \(8\), its largest is \(264\), and its sharp condition number on the orthogonal complement of the kernel is \(33\).

For \(r=1,2,3\), define the normalised spectral moment
\[
M_{2r}(H)=4^{-6}\sum_{\xi\in\widehat{H^6}}|W_H(\xi)|^{2r}.
\]
The first two moments agree, but the third separates the two additive colour structures:

| Moment | Cyclic group | Klein group |
|:--:|--:|--:|
| \(M_2\) | 264 | 264 |
| \(M_4\) | 2044416 | 2044416 |
| \(M_6\) | 87824400384 | 87789010944 |

In particular \(M_6(H_{\mathrm{cyc}})-M_6(H_{\mathrm{Kl}})=35389440\). Thus the **sixth is the first distinguishing even Fourier moment** in the natural second/fourth/sixth moment hierarchy, even though rank, extreme singular values, and fourth moment coincide.

## Assumptions and scope

Vertices are labelled \(0,1,2,3,4,5\); the two triangular faces have edges \((0,1),(1,2),(2,0)\) and \((3,4),(4,5),(5,3)\); rungs are \((0,3),(1,4),(2,5)\). A proper colouring \(c\in H^6\) satisfies \(c_u\ne c_v\) at all nine edges. For the cyclic group, integers \(0,1,2,3\) label residues with characters \(\chi_k(x)=i^{kx}\). For the Klein group, integers \(0,1,2,3\) are two-bit vectors with characters \(\chi_k(x)=(-1)^{\langle k,x\rangle_{\mathbb F_2}}\). The transform convention is \(W_H(\xi)=\sum_{c\in C_H}\prod_{v=0}^5\chi_{\xi_v}(c_v)\), with no Fourier normalisation. Absolute values are the singular values of convolution for the counting-measure \(\ell^2\) norm.

The statement is a complete finite census for this one labelled graph and these two order-four abelian colour groups. It does not assert a family formula for longer prisms or for other palette sizes.

## Proof

**Colouring count.** Each colouring of the first triangle is an ordered triple of distinct colours, giving \(4\cdot3\cdot2=24\) possibilities. Conditional on this triple, the lower triangle must use three distinct colours, with each lower colour different from its vertically corresponding upper colour. Among the 24 possible lower triples exactly 11 satisfy the vertical restrictions, giving \(|C_H|=24\cdot11=264\) independently of the group law.

**Exact character-sum identity.** Expanding \(f_H(c)=\prod_{uv\in E(G)}(1-1_{\{c_u=c_v\}})\) over all edge subsets \(A\subseteq E(G)\), and summing characters component by component, gives
\[
W_H(\xi)=\sum_{A\subseteq E(G)}(-1)^{|A|}4^{k(A)}\prod_{B\in\pi(A)}1_{\{\sum_{v\in B}\xi_v=0\text{ in }\widehat H\}},
\]
where \(\pi(A)\) is the partition into connected components of the spanning graph \(([6],A)\) and \(k(A)=|\pi(A)|\). This follows from character orthogonality \(\sum_{h\in H}\chi(h)=4\) for the trivial character and zero otherwise. In particular the formula is an **exact integer** and applies to both group laws without numerical approximation. The nonbalanced frequencies vanish by the global-colour-translation invariance; there are \(4^6-4^5=3072\) such frequencies.

**Exhaustive certificate.** The standalone `partition_expansion.py` enumerates precisely the \(2^9=512\) edge subsets, constructs their connected components, and evaluates the displayed integer identity at each of the \(4^6=4096\) frequencies for both groups. It bins absolute values and checks the complete eight-row table, including the absence of additional balanced zeros. The independent `direct_characters.py` enumerates all \(4^6\) colour assignments, filters the 264 proper ones, and sums each cyclic character in exact Gaussian-integer coordinates or each Klein character in exact signed-integer arithmetic. These distinct methods agree on all tabulated multiplicities; no floating-point cutoffs are used. Since the domains in both computations are fully enumerated finite sets, the exact integer certificates prove the claimed counts, rather than extrapolating from samples.

**Moment and operator deductions.** The absolute multiplier table immediately yields the rank, positive singular-value endpoints, and all three tabulated moment values by substitution into \(M_{2r}\). Independently, orthogonality implies the additive-energy identity
\[
M_{2r}(H)=\#\big\{(a_1,\ldots,a_r,b_1,\ldots,b_r)\in C_H^{2r}:\sum_{j=1}^r a_j=\sum_{j=1}^r b_j\big\}.
\]
The standalone `additive_energy.py` constructs exact pair- and triple-sum histograms directly in the ambient group, without Fourier calculations. The squared sums of their bins equal the stated fourth and sixth moments in both palettes. Since the moment of order two is \(|C_H|\), the fourth agrees and the sixth differs, the first differing even moment is precisely the sixth.

## Verification

Run `python3 direct_characters.py`, `python3 partition_expansion.py`, and `python3 additive_energy.py` in the directory containing these standalone files, using Python 3.10 or later and only its standard library. All three programs were executed on the actual packaged sources, and each printed `PASS`. The direct and subgraph checks agree on the complete spectra; the third independent method verifies the two higher moments. The complete spectra sum to 4096 multiplicities for each palette, with 1024 nonzero multipliers in each case. All arithmetic relevant to the claim is integer arithmetic.

## Relationship to prior work

Sokal's multivariate Tutte/Potts formulation gives the classical spanning-subgraph expansion for counting proper colourings. The Ellis-Monaghan–Moffatt external-field framework contains a more general vertex-weighted partition representation, into which individual Fourier characters can formally be substituted. Shrock–Xu study weighted-set proper colourings, including cyclic graph families. Those frameworks are important antecedents to the component expansion above, and are **not** claimed to be new here. The contribution is the complete, exact, two-group Fourier multiplier census of the triangular prism and its non-obvious equality of fourth additive energies alongside unequal sixth additive energies. The inspected works do not tabulate or state this palette-group moment separation.

## Limitations

This is an exact finite result, not a classification for all six-vertex graphs, all cyclic prisms, or all four-palette group-labelled graph models. General Potts expansions imply an algorithm for evaluating Fourier coefficients on any finite graph; they do not by themselves identify the two reported complete multiplier distributions and their first separating moment without further evaluation. An indexed or unindexed earlier spectral table might cover these particular numerical statements; priority has been checked only against the explicitly listed literature and available mathematical records. No independent mathematical audit has been performed.

## References

1. A. D. Sokal, *The multivariate Tutte polynomial (alias Potts model) for graphs and matroids*, first public arXiv posting 2005-03-25, [arXiv:math/0503607](https://arxiv.org/abs/math/0503607). See §§1–2, especially the Fortuin–Kasteleyn component expansion.
2. R. Shrock and Y. Xu, *Weighted-Set Graph Colorings*, first public arXiv posting 2009-11-22, [arXiv:0911.4218](https://arxiv.org/abs/0911.4218). See §§I–II, IV–V on weighted proper-colouring functions.
3. J. A. Ellis-Monaghan and I. Moffatt, *The Tutte-Potts connection in the presence of an external magnetic field*, first public arXiv posting 2010-05-29, [arXiv:1005.5470](https://arxiv.org/abs/1005.5470). See Corollary 4.3 for a general component-weighted expansion.
