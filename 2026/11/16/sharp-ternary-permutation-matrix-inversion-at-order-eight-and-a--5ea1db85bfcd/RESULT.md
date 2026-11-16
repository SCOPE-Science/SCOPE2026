# Sharp ternary permutation-matrix inversion at order eight and a fourfold circulant stability gap

## Finding
Let \(G=M_8(\mathbb F_3)\) be the additive group of ternary eight-by-eight matrices, \(\mathcal P_8\subset G\) the set of all 40,320 permutation matrices, and \(T f=1_{\mathcal P_8}*f\) the **unnormalized** counting convolution on \(\ell^2(G)\). Its least Fourier multiplier modulus is exactly nine:
\[
\min_{K\in G}\left|\sum_{P\in\mathcal P_8}\exp\left(\frac{2\pi i}{3}\sum_{i,j}K_{ij}P_{ij}\right)\right|=9.
\]
In particular \(T\) is invertible and \(\|T^{-1}\|_{2\to2}=1/9\).

For the 6,561 cyclically structured Fourier frequencies \(K_{ij}=a_{(j-i)\bmod 8}\), where \(a\in\mathbb F_3^8\), the sharp minimum modulus is **36**, achieved by exactly **48** words \(a\); the squared moduli attain exactly **59** values. On the Fourier span of these 6,561 frequencies, the inverse has exact norm \(1/36\). The minimum singular modulus is therefore four times as large on this natural cyclic symmetry class as on the full character space.

The sharp global minimum uses the explicit exponent matrix
```
00000000
01201100
00212210
01102002
01210201
02110222
01010212
00100120
```
whose complex third-root permanent is exactly nine. The cyclic witness \(a=(1,1,0,1,1,0,0,0)\) has permanent \(36\omega\), where \(\omega=\exp(2\pi i/3)\).

## Assumptions and scope
All statements concern the complete eight-by-eight permutation-incidence family over \(\mathbb F_3\), with each permutation counted once. The Fourier transform is unnormalized: \(\widehat f(K)=\sum_{X\in G}f(X)\omega^{\langle K,X\rangle}\). Thus the convolution multiplier of \(T\) is \(\widehat{1_{\mathcal P_8}}(K)=\operatorname{per}(\omega^{K_{ij}})\), with no division by \(8!\) or \(|G|\). The circulant restriction is on **frequency matrices**, not on the support of the permutation codebook; it is a translation-invariant Fourier subspace. Characters are indexed by all \(3^{64}\) matrices for the global statement, and by all \(3^8=6561\) exponent words for the cyclic statement.

## Proof
**Global lower bound.** Work in the Eisenstein integers \(\mathbb Z[\omega]\), and put \(\pi=1-\omega\). Then \(\pi^2=-3\omega\) and \(v_\pi(3)=2\). For an arbitrary cubic-root matrix \(A\), write \(A=J+\Delta\); every entry of \(\Delta\) is divisible by \(\pi\). Multilinearity of the permanent, grouping by partial matchings, gives the identity
\[
\operatorname{per}(A)=\sum_{k=0}^{8}(8-k)!
 \sum_{\substack{M\text{ a size-}k\\\text{partial row-column matching}}}
 \prod_{(i,j)\in M}\Delta_{ij}.
\]
The constant term is \(8!\), with \(v_\pi(8!)=2v_3(8!)=4\). For each \(k=1,\ldots,8\), every term in the \(k\)-th summand has valuation at least
\[
k+2v_3((8-k)!)=5,6,5,6,7,6,7,8
\]
respectively. Thus \(v_\pi(\operatorname{per}(A))=4\), with no cancellation at the leading valuation. It follows that \(\operatorname{per}(A)=9z\) for nonzero \(z\in\mathbb Z[\omega]\). Since \(|z|^2\) is a positive integer, \(|\operatorname{per}(A)|\ge9\). The exhibited exponent matrix has signed permutation residue counts \((13446,13437,13437)\) for exponents \(0,1,2\). Therefore its permanent is \(13446+13437\omega+13437\omega^2=9\), achieving the bound. Fourier diagonalization on the finite abelian group \(G\) yields invertibility and the stated full inverse norm.

**Cyclic exact minimum and multiplicity.** For every word \(a\in\{0,1,2\}^8\) build \(A_{ij}=\omega^{a_{(j-i)\bmod8}}\). Express each permanent exactly as \(u+v\omega\) with \(u,v\in\mathbb Z\), and compute its squared modulus \(u^2-uv+v^2\). The inclusion/subset recurrence
\[
D(\varnothing)=1,\quad D(S)=\sum_{j\in S}D(S\setminus\{j\})\omega^{a_{(j-|S|+1)\bmod8}}
\]
uses the row number \(|S|-1\) (zero based) and returns \(D(\{0,\ldots,7\})=\operatorname{per}(A)\). This is a finite exhaustive certificate over all 6,561 words, not a sample. Integer-only implementations supplied as `circulant_check.cpp` and `independent_check.py` agree that the minimum of \(u^2-uv+v^2\) is **1296**, with exactly **48** attaining words and **59** distinct squared values. The cyclic witness \(a=(1,1,0,1,1,0,0,0)\) produces \((u,v)=(0,36)\), so the minimum modulus is \(\sqrt{1296}=36\). Fourier diagonalization of the restricted invariant space yields norm \(1/36\).

## Verification
The independent Python routine uses arbitrary-precision Eisenstein-pair arithmetic and a subset dynamic program to evaluate every cyclic permanent. It also evaluates the explicit global witness both by that program and by a separate direct loop over all 40,320 permutations. The C++17 checker independently enumerates every cyclic phase word and verifies the minimum, count, number of levels and witness. To replay: `g++ -std=c++17 -O2 circulant_check.cpp -o circ_check && ./circ_check` and `python3 independent_check.py`. Integer equalities checked: squared minimum 1296, 48 minimizers, 59 distinct squared levels, witness permanent 9 and residue counts \((13446,13437,13437)\). There is no floating-point comparison. The global lower bound is a proof for all \(3^{64}\) Fourier frequencies and does not depend on enumeration.

## Relationship to prior work
The nonvanishing of permanents of third-root matrices in order eight is **known**: Akbari–Fanaï–Mahmoudian (2003) covers prime-root order \(p^\alpha-1\); Fanaï (2016), Theorem 1, broadens that family. The Eisenstein-valuation mechanism is directly related to the established argument, and the nonvanishing criterion and valuation technique are **not asserted novel**. The new bounded-comparison result is the *evaluated sharp minimum*, its attaining eight-by-eight character, and the exact cyclic-frequency minimum/count/spectrum-level separation. Akbari–Ariannejad–Tajfirouz (2015 online) concerns maximum permanent magnitude and other estimates; only its abstract was available, so deeper possible overlap is explicitly unresolved. Fanaï (2023) concerns further zero-free orders, but its accessible abstract gives no evaluated cyclic minimizer census. Related binary circulant power-of-two permanent congruences concern signs, not cubic roots, and do not evaluate sharp cyclic minima. The binary order-five permutation Fourier spectrum and ternary signed-permutation (monomial) examples also involve different phase alphabets or codebooks and do not imply the present exact numbers.

## Limitations
This is an exact order-eight result, not a uniform theorem for larger matrix orders. The 48 cyclic minimizers are counted as phase words and are not classified by cyclic/dihedral symmetry or by row/column phase equivalence. The complete distribution of the unrestricted \(3^{64}\) multipliers is not determined. Exhaustive numerical arithmetic establishes the finite cyclic census; it does not establish a general symbolic classification of all circulant permanent levels. A pertinent 2015 paper was only abstract-accessible and remains a historical-priority risk; no independent mathematical audit is claimed.

## References
1. S. Akbari, H.-R. Fanaï, and K. Mahmoudian, *On the matrices with constant determinant and permanent over roots of unity*, Linear Algebra and its Applications 375 (2003), 245–249, https://doi.org/10.1016/S0024-3795(03)00659-1 (publication metadata 2003-12-04).
2. H.-R. Fanaï, *On Matrices over Roots of Unity with Vanishing Permanent*, Ars Combinatoria 126 (2016), 117–119, https://combinatorialpress.com/article/ars/Volume%20126/volume-126-paper-10.pdf.
3. S. Akbari, M. Ariannejad, and Z. Tajfirouz, *Permanents of matrices over roots of unity*, Linear and Multilinear Algebra 64 (2016), 1769–1775, online 2015-12-28, https://doi.org/10.1080/03081087.2015.1120264 (abstract inspected; full text inaccessible).
4. H.-R. Fanaï, *Matrices over Roots of Unity and Permanent*, Journal of Mathematical Sciences: Advances and Applications 74 (2023), 37–41, https://doi.org/10.18642/jmsaa_7100122294 (abstract only).
