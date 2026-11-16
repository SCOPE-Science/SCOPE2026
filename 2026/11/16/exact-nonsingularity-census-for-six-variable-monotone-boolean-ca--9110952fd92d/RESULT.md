# Exact nonsingularity census for six-variable monotone Boolean Cayley operators

## Finding
Let \(f:\mathbb F_2^6\to\{0,1\}\) range over all coordinatewise monotone Boolean functions, and define \(S_f=\{x:f(x)=1\}\). Its **unnormalized** Walsh multiplier is
\[
\lambda_f(u)=\sum_{x\in S_f}(-1)^{u\cdot x},\qquad u\in\mathbb F_2^6.
\]
Of the **7,828,354** such functions, precisely **3,937,192** have \(\lambda_f(u)\ne0\) for every \(u\); the other **3,891,162** have at least one zero multiplier.

Every one of the **3,913,460** odd-cardinality supports has nonzero multipliers, with \(\min_u|\lambda_f(u)|=1\). Exactly **23,732** of the **3,914,894** even-cardinality supports have no zero multiplier, and every one of these has \(\min_u|\lambda_f(u)|=2\).

For the even-cardinality, nonsingular functions, the exact support-size distribution is:

| \(|S_f|\) | Count |
|:--:|--:|
| 10 | 15 |
| 14 | 195 |
| 18 | 225 |
| 22 | 886 |
| 26 | 4,275 |
| 30 | 6,270 |
| 34 | 6,270 |
| 38 | 4,275 |
| 42 | 886 |
| 46 | 225 |
| 50 | 195 |
| 54 | 15 |

For the convolution operator \((C_fg)(y)=\sum_{x\in S_f}g(y+x)\) on \(\ell^2(\mathbb F_2^6)\), these are exactly the nonsingular cases. The sharp inverse norm is \(1\) for an odd-support function and \(1/2\) for an even-support nonsingular function. Its condition number is exactly \(|S_f|\) or \(|S_f|/2\), respectively. Moreover, for every dimension \(1\le d\le5\), no even-cardinality monotone support yields a nonsingular convolution operator; dimension six is the first exception.

## Assumptions and scope
The domain consists of all 64 binary vectors \(x=(x_0,\ldots,x_5)\). Monotonicity means \(f(x)\le f(y)\) whenever each \(x_i\le y_i\). The two constant functions are included. Coordinates, functions, and Fourier characters are labelled, not identified under permutations. In this statement \(f\) is the **zero-one indicator**, not the character-valued sign function \((-1)^f\); the distinction matters at zero frequency. Empty supports give the zero convolution and are counted as singular. The Fourier transform and convolution are both unnormalized.

## Proof
The proof is a **finite exhaustive certificate with a complete enumeration argument**, not a claim of a symbolic infinite-dimensional theorem. Encode a monotone \(d\)-variable function as a bit mask whose bit indexed by \(x\in\{0,\ldots,2^d-1\}\) stores \(f(x)\). For any such function in dimension \(d+1\), its two cofactors \(a(x)=f(x,0)\) and \(b(x)=f(x,1)\) are monotone in dimension \(d\), and \(a(x)\le b(x)\) pointwise. Conversely, every such ordered cofactor pair uniquely defines a monotone \((d+1)\)-variable function. Therefore the complete lists obey
\[
\mathcal M_{d+1}=\big\{\,a+(b\ll 2^d):a,b\in\mathcal M_d,\ (a\mathbin{\&}\neg b)=0\,\big\},
\]
where the shift and bitwise relation refer to mask encodings. Starting with the two constant functions on the zero-cube gives \(|\mathcal M_5|=7,581\), and traversing every admissible pair of these five-dimensional functions gives \(|\mathcal M_6|=7,828,354\). No isomorphism reduction or probabilistic sampling enters this traversal.

Let \(A(v)\) and \(B(v)\) be the exact integer Walsh transforms of \(a\) and \(b\). Character orthogonality across the sixth coordinate gives
\[
\lambda_f(v,0)=A(v)+B(v),\qquad
\lambda_f(v,1)=A(v)-B(v),\quad v\in\mathbb F_2^5.
\]
Consequently, the zero-free condition is precisely that \(A(v)\ne B(v)\) and \(A(v)\ne-B(v)\) for every one of the 32 frequencies \(v\). This is the exact integer predicate tested by the attached complete verifier. The verifier **also** computes the 64-point integer Walsh transform independently by six direct butterfly passes and checks each of its coefficients against the two-cofactor character sum for **every admissible pair**, not just the nonsingular ones.

The complete exact traversal gives \(3,913,460\) odd-cardinality functions and \(3,914,894\) even-cardinality functions, with **23,732** nonsingular even functions and the support-size counts in the table. Since \((-1)^{u\cdot x}\equiv1\pmod2\), an odd support has every \(\lambda_f(u)\) odd and is automatically nonsingular. The verifier further finds \(\min_u|\lambda_f(u)|=1\) for each odd-support case and \(2\) for each of the **23,732** nonsingular even-support cases. The small-dimension exhaustive check gives zero nonsingular even supports for each \(1\le d\le5\).

Every Walsh character is an eigenvector of \(C_f\) with real eigenvalue \(\lambda_f(u)\), so \(C_f\) is invertible exactly when none vanish. The eigenvalue at \(u=0\) equals \(|S_f|\) and dominates all absolute multipliers by the triangle inequality. Therefore the sharp inverse norm and condition number follow from the certified minima.

## Verification
Compile the attached standalone verifier with a C++17 compiler and run it:

```sh
g++ -O3 -std=c++17 monotone6_spectral_census.cpp -o monotone6_spectral_census
./monotone6_spectral_census
```

The program exits nonzero if the independent spectral computations disagree, if an odd-support case lacks the unit gap, if a smaller dimension has an even-support nonsingular case, or if any stated census value, size-stratum count or even nonsingular gap disagrees. A successful run prints `MONOTONE_SIX_EXACT_WALSH_CENSUS_PASS` and all 12 size strata. Every branch and integer comparison is within fixed-width exact arithmetic; maximum absolute Fourier coefficient is at most 64. The algorithm fully enumerates all functions through the cofactor bijection. Independent human audit has not been conducted.

## Relationship to prior work
Celerier, Joyner, Melles and Phillips (2012) related monotone-function Cayley spectra to Walsh transforms, showed some classes are singular, and exhibited an **even-cardinality nonsingular example in dimension six**. That example and the Fourier diagonalization are prior work, not new findings here. Joyner's dated September 1, 2012 exposition describes this example. Carlet, Joyner, Stănică and Tang (2016), Theorem 7.2, provide a **general explicit Walsh formula** for monotone Boolean functions. Uyan (2013) tabulates Walsh spectral value occurrences among unrestricted Boolean functions of at most six variables, but does not restrict the population to all coordinatewise monotone functions.

The present finding is the **complete monotone-population singularity count, support-size profile and sharp nonzero gaps at the first exceptional dimension**, not a new transform formula or a new example of nonsingularity. The listed sources do not themselves supply the stated 7,828,354-case monotone census or its 12-stratum distribution. This is a bounded originality assessment rather than proof of absolute historical priority.

## Limitations
No conclusion about the corresponding exceptional fraction in dimension seven or beyond is made. The classification is finite and relies on a compiled exhaustive integer verifier, whose logic and full-run termination must be examined when reproducing it; the printed totals are not an independent symbolic proof. The main gap assertions are restricted to six variables. No distinctness modulo variable permutations is claimed. A previously overlooked computation or database could contain the same stratified counts; no independent mathematical validation is claimed.

## References
1. D. Joyner, "Some remarks on monotone Boolean functions," September 1, 2012, https://yetanothermathblog.com/2012/09/ .
2. C. Celerier, D. Joyner, C. Melles and D. Phillips, "On the Walsh-Hadamard transform of monotone Boolean functions," *Tbilisi Mathematical Journal* **5**(2) (2012), 19–35, https://tcms.org.ge/Journals/ASETMJ/Special%20issue/1/PDF/tmj5_2_2.pdf .
3. E. Uyan, *Analysis of Boolean Functions with Respect to Walsh Spectrum*, doctoral thesis, Middle East Technical University (2013), https://open.metu.edu.tr/bitstream/handle/11511/22847/index.pdf .
4. C. Carlet, D. Joyner, P. Stănică and D. Tang, "Cryptographic properties of monotone Boolean functions," *Journal of Mathematical Cryptology* (2016), https://faculty.nps.edu/pstanica/research/2016JMC_MonBent.pdf .
