# Fourth-moment separation of the two abelian four-colour structures on complete bipartite graphs

## Finding

Let \(H\) be either the cyclic group \(C_4=\mathbb Z/4\mathbb Z\) or the Klein group \(V_4=(\mathbb Z/2\mathbb Z)^2\). For each integer \(n\ge1\), let \(P_{H,n}\subset H^{n+2}\) be the labelled proper colourings of the complete bipartite graph \(K_{2,n}\): if the two vertices in the smaller part receive \(u,v\) and the other vertices receive \(w_1,\ldots,w_n\), then \(w_j\notin\{u,v\}\) for every \(j\). The two pole vertices are not required to have different colours.

Define their **ordered additive energy** by
\[
E_H(n)=\#\{(x_1,x_2,x_3,x_4)\in P_{H,n}^{4}: x_1+x_2=x_3+x_4\},
\]
where addition is coordinatewise in \(H^{n+2}\). Then for every \(n\ge1\),
\[
\boxed{E_{C_4}(n)=64\bigl(2\cdot2^n+12\cdot4^n+30\cdot6^n+8^n+18\cdot10^n+21^n\bigr)},
\]
\[
\boxed{E_{V_4}(n)=64\bigl(18\cdot4^n+24\cdot6^n+3\cdot8^n+18\cdot10^n+21^n\bigr)}.
\]
Thus
\[
\boxed{E_{V_4}(n)-E_{C_4}(n)=128\cdot2^n\bigl(4^n-3\cdot3^n+3\cdot2^n-1\bigr)}.
\]
The difference vanishes exactly for \(n=1,2\) and is strictly positive for every \(n\ge3\). At \(n=3\), the respective energies are \(2,242,368\) and \(2,248,512\), differing by \(6,144\). For large \(n\), their difference is asymptotic to \(128\cdot8^n\), although each energy is asymptotic to \(64\cdot21^n\): the relative group-law separation is asymptotic to \(2(8/21)^n\).

For the unnormalized character transform \(W_{H,n}(\chi)=\sum_{x\in P_{H,n}}\overline{\chi(x)}\), the equivalent fourth-moment identity is
\[
\sum_{\chi\in\widehat{H^{n+2}}}|W_{H,n}(\chi)|^4=4^{n+2}E_H(n).
\]
Hence the fourth Fourier moments agree at \(n=1,2\) and first distinguish the two group structures at \(n=3\).

## Assumptions and scope

Both groups have exactly four distinct elements, represented for calculations by integers \(0,1,2,3\). For \(C_4\), addition and subtraction are modulo four; for \(V_4\), both are bitwise exclusive-or on two-bit labels. All colourings and the four copies in the energy are ordered and labelled. The graph is the ordinary \(K_{2,n}\), with no extra edge between the two pole vertices. The transform is unnormalized, and the energy counts ordered quadruples, including repetitions. The result holds for every positive integer \(n\); it does not assert complete Fourier-multiplier histograms or extend to other graph families.

## Proof

**Reduction to a fixed 64-state calculation.** Write the four pole-colour pairs as \((u_i,v_i)\) for \(i=1,2,3,4\). The coordinatewise additive-energy equation requires
\[
u_1+u_2=u_3+u_4,\qquad v_1+v_2=v_3+v_4.
\]
Set \(d_i=v_i-u_i\). Subtracting the two equations gives \(d_1+d_2=d_3+d_4\), so \(d_4=d_1+d_2-d_3\). Conversely, for every such difference quadruple, there are exactly \(4^3=64\) choices of the pole colours \(u_1,u_2,u_3\), with \(u_4=u_1+u_2-u_3\) and \(v_i=u_i+d_i\). Translate the colours in copy \(i\) by \(-u_i\), at both its poles and all its right-hand vertices. The additive constraint is preserved, as \(u_1+u_2-u_3-u_4=0\). The pole colours become \((0,d_i)\), and each right-hand vertex in copy \(i\) may take exactly the colours in \(A_{d_i}=H\setminus\{0,d_i\}\).

For an admissible quadruple \(d=(d_1,d_2,d_3,d_4)\), write
\[
T_H(d)=\#\{(a,b,c,e)\in A_{d_1}\times A_{d_2}\times A_{d_3}\times A_{d_4}:a+b=c+e\}.
\]
The \(n\) right-hand positions are independent; therefore
\[
E_H(n)=64\sum_{(d_1,d_2,d_3)\in H^3}T_H(d_1,d_2,d_3,d_1+d_2-d_3)^n.
\]
In particular, this is an identity valid for every \(n\), rather than an extrapolation from experiments.

**Exact 64-state lemma.** For each \(d_i\), let \(1_{A_{d_i}}\) be its indicator and use the ordinary unnormalized group convolution. Then
\[
T_H(d)=\sum_{t\in H}(1_{A_{d_1}}*1_{A_{d_2}})(t)\,(1_{A_{d_3}}*1_{A_{d_4}})(t).
\]
This expression involves only four-point sets. Evaluating it for the 64 ordered triples \((d_1,d_2,d_3)\in H^3\), with the fourth difference forced as above, gives the following **complete** frequency table. A blank entry means zero occurrences.

| Value of \(T_H\) | \(C_4\): triples | \(V_4\): triples |
|---:|---:|---:|
| 2 | 2 | 0 |
| 4 | 12 | 18 |
| 6 | 30 | 24 |
| 8 | 1 | 3 |
| 10 | 18 | 18 |
| 21 | 1 | 1 |
| **Total** | **64** | **64** |

The separately supplied `T_TABLE.csv` contains all 64 ordered triples and both values of \(T_H\), rather than only totals. The script `verify_energy.py` independently recomputes every entry by a direct enumeration of the three free right-hand colours, derives the corresponding energy polynomial, and checks the difference. The independent `verify_fourier.py` builds the proper-colouring indicators and applies the full tensor character transforms without using the 64-state calculation, for \(1\le n\le4\).

Substituting the table into the displayed 64-state identity proves the two energy expressions. Their subtraction gives
\[
128\left(8^n-3\cdot6^n+3\cdot4^n-2^n\right)=128\cdot2^n\left(4^n-3\cdot3^n+3\cdot2^n-1\right).
\]
The parenthesized factor on the right counts length-\(n\) words on four letters containing each of three specified letters at least once, by inclusion-exclusion. It is zero for \(n=1,2\) and positive for \(n\ge3\), proving the strict threshold. The asymptotics follow from the unique largest base \(21\) in both energies and largest base \(8\) in the difference.

**Fourier conversion.** By character orthogonality on the finite abelian group \(H^{n+2}\),
\[
\sum_\chi|W_{H,n}(\chi)|^4
=|H|^{n+2}\sum_{x_1+x_2=x_3+x_4}\prod_{i=1}^4 1_{P_{H,n}}(x_i),
\]
which is precisely \(4^{n+2}E_H(n)\). No normalization factor is omitted.

## Verification

Run `python verify_energy.py` and `python verify_fourier.py` using Python 3 with only the standard library. The first checks the complete 64-state histogram for both groups and the difference identity on additional positive input values, while the all-length proof is the 64-state reduction and exhaustive state lemma. The second independently computes integer fourth moments by the full tensor Fourier transform for \(n=1,2,3,4\). Both were run successfully on the exact embedded scripts. The first check is a complete finite certificate for the 64-state lemma; the second is a finite cross-check, not a proof for arbitrary \(n\).

## Relationship to prior work

Goodall's finite-abelian graphical Fourier analysis establishes group-character and Potts/Tutte duality, including an Ashkin–Teller discussion of the Klein-four group; it does not state this two-group ordered-additive-energy comparison for \(K_{2,n}\). Sokal's multivariate Tutte treatment supplies older chromatic/Potts motivation but no analogous fourfold group-law formula. Celaya, Choo, MacGillivray and Seyffarth address cyclic Gray codes of proper colourings of complete bipartite graphs, rather than additive-energy comparisons. A published first-Fourier-band sampling analysis of complete bipartite colourings concerns a different observation operator; an earlier Klein-four parity result covers Fourier **support**, not these fourth moments. The present formulas compute both fourth moments and identify their first strict divergence with all-length positivity. Unindexed equivalent computations remain a priority risk; a search failure alone is not taken as an independence certificate.

## Limitations

No claim of a complete pointwise Fourier spectrum, optimal Fourier inverse norm, or generalization to larger palettes or arbitrary bipartite graphs is made. The exact state lemma was verified by two finite-algorithm descriptions and one complete supplied 64-entry table; an independent external mathematical audit has not been performed. Historical novelty is based on accessible comparative evidence and remains subject to additional literature discovery.

## References

1. A. Goodall, *Fourier Analysis on Finite Abelian Groups: Some Graphical Applications*, author-hosted full manuscript, https://iuuk.mff.cuni.cz/~andrew/dwajgApr06.pdf ; book chapter DOI https://doi.org/10.1093/acprof:oso/9780198571278.003.0007 (published 2007-01-18).
2. A. D. Sokal, *The multivariate Tutte polynomial (alias Potts model) for graphs and matroids*, original arXiv submission 2005-03-25, https://arxiv.org/abs/math/0503607 .
3. M. Celaya, K. Choo, G. MacGillivray and K. Seyffarth, *Reconfiguring k-colourings of Complete Bipartite Graphs*, Kyungpook Mathematical Journal 56 (2016), 647–655, https://doi.org/10.5666/KMJ.2016.56.3.647 .
4. *Exact Fourier sampling spectra and a thin-side conditioning transition for bipartite colourings*, published research note, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-fourier-sampling-spectra-and-a-thin-side-conditioning-tran--2b34d08d2568 .
