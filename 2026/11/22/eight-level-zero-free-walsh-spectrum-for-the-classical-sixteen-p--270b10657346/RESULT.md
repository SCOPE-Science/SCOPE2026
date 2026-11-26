# Exact inverse endpoint norm for the affine sixteen-point Steiner quadruple system

## Finding
Let \(V=\mathbb F_2^4\), \(G=\mathbb F_2^V\), and let \(\mathcal B\) be the 140 incidence vectors of the affine two-flats of \(V\). For the unnormalized counting convolution
\[
(Tf)(z)=\sum_{P\in\mathcal B}f(z+P),
\]
the inverse is convolution by a kernel supported on the second-order Reed–Muller code \(C=RM(2,4)\). Its values are constant on the eight affine-coordinate orbits in \(C\):

| Type in \(C\) | Orbit size | \(3360k\) |
|---|---:|---:|
| Weight 0 | 1 | −255 |
| Weight 4 | 140 | 24 |
| Weight 6 | 448 | −9 |
| Weight 8, affine | 30 | 25 |
| Weight 8, nonaffine | 840 | −3 |
| Weight 10 | 448 | 7 |
| Weight 12 | 140 | 0 |
| Weight 16 | 1 | −415 |

In particular, the two sharp endpoint operator norms on the full group are
\[
\|T^{-1}\|_{\ell^1(G)\to\ell^1(G)}=\|T^{-1}\|_{\ell^\infty(G)\to\ell^\infty(G)}=3617/840.
\]
The eight spectral levels provide context; the result emphasized here is the inverse **in incidence coordinates** and its exact amplification norm.

## Assumptions and scope
An element of \(G\) is a 16-bit word indexed by the four-bit labels of \(V\); its weight is its number of ones. Affine equivalence of codewords in the table means permuting the point coordinates by an invertible affine map on \(V\), without adding any word to the result. The convolution uses counting, not probability, normalization. This is about the classical affine SQS(16), not arbitrary Steiner designs or higher dimensions.

## Proof
**Code and orbits.** A two-flat indicator is the product of two independent affine linear forms (using the level sets on which each form is one). Such products lie in \(C\). They span it: every quadratic monomial is such a product; for each variable \(x_i\) choose \(j\ne i\) and add the two products \(x_ix_j\) and \(x_i(1+x_j)\); and the four parallel two-flats of a fixed direction sum to the constant word. The span thus has dimension 11.

For \(Q\) of degree at most two, the alternating polar form of its quadratic part has rank 0, 2 or 4. Rank zero gives the affine cases. Rank two has normal form \(xy\) for the quadratic part: if the linear part vanishes on the radical, translation removes it and the two remaining constants distinguish weights 4 and 12. If it is nonzero on the radical, choose a radical coordinate \(z\) carrying it, and translate to absorb the constant, giving \(xy+z\), of weight 8. Rank four similarly has normal form \(xy+zt\) with linear term removable by translation and weights 6 and 10 distinguished by the constant. These normal forms show that the eight types are orbits. There are 35 rank-two polar forms, one for each two-dimensional annihilator of a radical (the nonzero alternating form on the two-dimensional quotient is unique), and the remaining 28 nonzero forms have rank four. For each rank-two form four linear terms vanish on its radical; for each, one constant yields weight 4 and the other weight 12. The other twelve linear terms and both constants give weight 8. For rank four all sixteen linear terms each admit one constant for each of the two weights. The nonconstant affine functions give 30 words. This yields all the displayed sizes.

**An eight-dimensional convolution equation.** Write the orbit representatives in table order as
\[
0,\ xy,\ xy+zt,\ x,\ xy+z,\ 1+xy+zt,\ 1+xy,\ 1.
\]
Point affine permutations preserve the block set, so convolution maps orbit-constant functions to orbit-constant functions on \(C\). For representative \(h_i\), let \(M_{ij}\) count the blocks \(P\) for which \(h_i+P\) has type \(j\). In the order above the transition matrix is
\[
M=\begin{pmatrix}
0&140&0&0&0&0&0&0\\
1&36&64&3&36&0&0&0\\
0&20&45&0&60&15&0&0\\
0&14&0&0&112&0&14&0\\
0&6&32&4&60&32&6&0\\
0&0&15&0&60&45&20&0\\
0&0&0&3&36&64&36&1\\
0&0&0&0&0&0&140&0
\end{pmatrix}.
\]
An exact recipe for each row is to take the set of distinct products \((a\cdot u+e)(b\cdot u+f)\) in the variables \(u\in V\), for unordered distinct nonzero \(a,b\in V\), \(e,f\in\{0,1\}\); this generates each of the 140 blocks, with repetitions removed. For each produced word add \(h_i\), tally its Hamming weight, and split weight eight according to membership in the 30 nonconstant affine words. This calculation is supplied in `orbit_inverse.py`. For example, from \(0\) all 140 planes give weight 4. From \(1\) they all give weight 12. Every row sums to 140, and \(|O_i|M_{ij}=|O_j|M_{ji}\) by reversal of each block addition.

Multiplying \(M\) by the integer column \((-255,24,-9,25,-3,7,0,-415)^{\mathsf T}\) gives \((3360,0,0,0,0,0,0,0)^{\mathsf T}\). Therefore the proposed \(k\) satisfies \(Tk=\delta_0\) on \(C\). Off \(C\), adding a block never brings a word into \(C\), so extension by zero satisfies the same identity on \(G\). Convolution by \(k\) is consequently the unique inverse, since composition of convolutions multiplies their kernels by convolution and \(\delta_0\) is its identity.

All row sums of absolute entries in the inverse matrix, and likewise all column sums, are \(\sum_g|k(g)|\). The \(\ell^1\) bound is attained on a single-coordinate unit vector; for \(\ell^\infty\) choose input signs agreeing with one row. The table gives \(\sum_g|k(g)|=14468/3360=3617/840\).

## Spectral context and relation to prior work
The affine design and its parallel classes are classical; see de Vries, *On orthogonal resolutions of the classical Steiner quadruple system SQS(16)*, DOI 10.1007/s10623-008-9207-5, and Kaski–Östergård–Pottonen, *The Steiner Quadruple Systems of Order 16*, J. Combin. Theory A 113 (2006), 1764–1770.

For a Boolean coloring \(s\), let \(W_s(\xi)=\sum_{x\in V}(-1)^{s(x)+\xi\cdot x}\). The multiplier of counting block convolution is
\[
\lambda_s=\frac{16^{-1}\sum_{\xi\in V}W_s(\xi)^4-736}{24}.
\]
Indeed the character-orthogonality sum runs over ordered zero-sum quadruples. The quadruples can be parametrized as \((x,x+a,x+b,x+a+b)\); the 46 pairs \((a,b)\) per base point with \(a=0\), \(b=0\) or \(a=b\) contribute \(+1\), while each genuine plane occurs 24 times. Thus the absolute Walsh distributions of the eight extended-affine classes of four-variable Boolean functions (for example the public [Affine Equivalence Classes, n=4 table](https://booleanfunction.github.io/equivalence-classes.html)) directly give the eight levels \(140,70,28,6,12,-4,-10,-20\); this reduction is not a new classification of Boolean functions or a claim of spectral priority. An unordered multiplier table does not specify the spatial inverse entries. The proof above obtains them by the affine-coordinate block-transition counts, without assuming spectral multiplicities or performing a full reciprocal transform.

## Verification and limits
Run `python3 orbit_inverse.py` with Python 3.10 or later. It generates the 140 planes as level-set products, evaluates the eight orbit rows and checks the convolution identity and exact norm. The original `verify.py` separately checks the full spectral and inverse tables with an integer Walsh transform. Neither calculation is an assertion about a different block system.
