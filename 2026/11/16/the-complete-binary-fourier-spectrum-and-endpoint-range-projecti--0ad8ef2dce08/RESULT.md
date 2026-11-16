# The complete binary Fourier spectrum and endpoint range-projection norm for order-three Latin squares

## Finding
Let \(G=\mathbb F_2^{27}\), with coordinates indexed by triples \((i,j,k)\in\{0,1,2\}^3\). For each Latin square \(L\) of order three, let \(v_L\in G\) be its incidence vector, where \((v_L)_{ijk}=1\) exactly when \(L(i,j)=k\). Write \(f=\mathbf1_{\{v_L:L\text{ is Latin}\}}\) and let \(C_fh=f*h\) use **unnormalized** convolution on the additive group \(G\). Then its unnormalized Walsh multipliers \(\widehat f(\xi)=\sum_{x\in G}f(x)(-1)^{\xi\cdot x}\) have exactly the following absolute-value distribution:

| \(|\widehat f(\xi)|\) | number of ambient frequencies |
| ---: | ---: |
| \(0\) | 56,623,104 |
| \(4\) | 70,778,880 |
| \(8\) | 6,291,456 |
| \(12\) | 524,288 |

For each nonzero magnitude, positive and negative signs occur equally often. Consequently,
\[
\operatorname{rank}C_f=77,594,624,\qquad
\operatorname{nullity}C_f=56,623,104,
\qquad \kappa_+(C_f)=3.
\]
Among **all** real or complex linear projections \(P\) from \(\ell^1(G)\), respectively \(\ell^\infty(G)\), onto the range of \(C_f\), the exact minimum operator norm is
\[
\boxed{\lambda_1(\operatorname{ran}C_f)=\lambda_\infty(\operatorname{ran}C_f)=\frac{31}{4}.}
\]
Both minima are attained by the canonical Fourier-support projection. In particular, the comparatively mild positive \(\ell^2\) spectral condition number \(3\) coexists with the larger unavoidable endpoint projection amplification \(31/4\).

## Assumptions and scope
All rows, columns, and symbols are separately labelled by \(0,1,2\); the symbols are not quotient by relabellings. An order-three Latin square has each symbol exactly once in each row and each column. The group has \(2^{27}=134,217,728\) points. Fourier transforms use no normalization in the forward direction and the factor \(2^{-27}\) in inversion. The operator range is considered over the real or complex scalars with counting-measure \(\ell^p\) norms. No assertion about orders four and larger is made.

## Proof
**Twelve Latin squares.** Each row is one of six permutations of three symbols. Enumerating the \(6^3=216\) possible row triples and retaining precisely the triples whose columns are also permutations produces twelve distinct squares. Equivalently, all twelve are
\[
 L_{a,b,c}(i,j)=ai+bj+c\pmod 3,
 \qquad a,b\in\{1,2\},\quad c\in\{0,1,2\}.
\]
The two descriptions are verified to coincide in the standalone exact checker. This agrees with the classical reduced count \(1\) and labelled count \(12\); this unsigned count is not claimed as new.

**Eight-dimensional affine compression.** Fix the first lexicographically enumerated incidence vector \(v_0\). Let \(D\) be the \(\mathbb F_2\)-span of all \(v_L-v_0\). Gaussian elimination on the twelve explicitly enumerated \(27\)-bit vectors gives \(\dim D=8\). With bit index \(9i+3j+k\), one reproducible ordered binary difference basis has integer bitmasks `62512128,14355888,102264240,219051,7299499,110808,13851,27702`. In the deterministically chosen difference basis (highest-bit pivot, first occurrence), the twelve affine coordinates are exactly
\[
 S=\{0,1,3,4,11,18,40,124,137,220,228,250\}
 \subseteq \mathbb F_2^8,
\]
where integers encode eight-bit masks. The checker constructs all \(256\) basis combinations, verifies that they are different, and maps all twelve input vectors into this list. Moreover \(v_0\notin D\), as checked by the same exact span computation. Every character on \(D\) has exactly \(2^{19}\) ambient extensions.

**Exact multiplier census.** For each \(u\in\mathbb F_2^8\), define \(w(u)=\sum_{s\in S}(-1)^{u\cdot s}\). The complete, finite \(256\)-character evaluation is

| \(w(u)\) | count |
| ---: | ---: |
| \(-8\) | 2 |
| \(-4\) | 45 |
| \(0\) | 108 |
| \(4\) | 90 |
| \(8\) | 10 |
| \(12\) | 1 |

This table is certified by exhaustive integer summation in the accompanying code, independently by a fast Walsh transform, and by direct sums on representatives of every ambient character restriction. It satisfies \(\sum_u w(u)^2=256\cdot12\). The ambient coefficient at a character \(\xi\) is \((-1)^{\xi\cdot v_0}w(\xi|_D)\). Since \(v_0\notin D\), changing an ambient character without changing its restriction can flip the sign: each nonzero magnitude's positive and negative values therefore occur equally often. Multiplying the absolute-value counts by \(2^{19}\) gives the displayed complete ambient distribution and rank. The smallest positive magnitude is \(4\), while \(|\widehat f(0)|=12\).

**Sharp endpoint projection.** Put \(E=\{u:w(u)\ne0\}\), with \(|E|=148\), and let
\[
 H(t)=\sum_{u\in E}(-1)^{t\cdot u},\qquad t\in\mathbb F_2^8.
\]
Its complete absolute-value distribution is

| \(|H(t)|\) | count |
| ---: | ---: |
| \(0\) | 12 |
| \(4\) | 81 |
| \(8\) | 108 |
| \(12\) | 54 |
| \(148\) | 1 |

The exhaustive checker evaluates all \(256\) values by two different integer methods, verifies \(\sum_t H(t)^2=256\cdot148\), and obtains \(\sum_t|H(t)|=1984\). The unique translation-invariant projection onto the range is the Fourier multiplier \(\mathbf1_{\{\widehat f\ne0\}}\). Its convolution kernel is supported on \(D\), and has values \(2^{-8}H(t)\) at the elements of \(D\) identified with \(t\). Hence its exact \(\ell^1\) and \(\ell^\infty\) norms are \(1984/256=31/4\).

For an arbitrary bounded projection \(P\) onto the same range, average \(\tau_gP\tau_g^{-1}\) over all translations \(g\in G\). Each conjugate remains a projection onto the translation-invariant range, and the average acts identically on that range. The average commutes with all translations and is therefore the unique Fourier-support projection. Convexity of the operator norm gives \(\|P\|\ge31/4\). This argument holds over both scalar fields and for both endpoint norms.

## Verification
Run `python3 artifacts/verify.py` with Python 3.10 or newer. It must print `LATIN3_WALSH_RANGE_PASS latin=12 dimension=8 quotient=256 rank=77594624 zero=56623104 norm=31/4`. It uses two independent descriptions of the twelve squares, exact binary Gaussian elimination, three character-sum routes, two projection-kernel routes, and the two Parseval identities. The relevant finite domains are exhausted, not sampled.

## Relationship to prior work
The classical number and triple-incidence interpretation of Latin squares are prior mathematics. Cameron's dated design-theory account describes the Latin-square incidence net. McKay and Wanless (2005; freely posted arXiv version 2009) derive enumeration formulas, an exact signed-permanent moment formula, and one-factorization counts; their displayed theorem concerns the total number of Latin squares, not this signed transform over all 27 incidence coordinates. Published work classifying twelve order-three Latin-square graphs as equality cases of ternary frameproof codes likewise determines the underlying set but not its Walsh multiplier distribution or its range-projection norm. Zippin discusses translation averaging for projection norms in general; that mechanism is acknowledged rather than claimed as new. The contribution here is the evaluated harmonic census and sharp norm for the Latin-square incidence family.

## Limitations
This is a complete result for the first nontrivial Latin-square order, not an all-order theorem. The finite spectral table depends on explicitly exhaustive, provided exact-integer calculations, not on a shorter symbolic closed formula. Previously unpublished or poorly indexed tabulations of the same small-parameter transform are a residual historical-priority risk. The review is same-model only and no independent mathematical audit has been performed.

## References
1. P. J. Cameron, *Encyclopaedia of Design Theory: Latin squares as incidence structures* (dated 16 April 2002), https://webspace.maths.qmul.ac.uk/l.h.soicher/designtheory.org/library/encyc/latinsq/i/ .
2. B. D. McKay and I. M. Wanless, *On the number of Latin squares*, *Annals of Combinatorics* 9 (2005), 335–344; accessible arXiv full text `arXiv:0909.2101v1` (11 September 2009), https://arxiv.org/pdf/0909.2101 .
3. M. Zippin, *A variant of Rudin's inequality for translation invariant projections on group algebras and its generalization to finite dimensional Banach spaces*, *Archiv der Mathematik* 82 (2004), 61–67, DOI `10.1007/s00013-003-0582-x`.
4. *Equality cases for ternary length-three 2-frameproof codes* (2026), published mathematical record `2026/10/12/...d9089a638b0a`, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-equality-cases-for-ternary-length-three-2-frameproof-codes--d9089a638b0a .
