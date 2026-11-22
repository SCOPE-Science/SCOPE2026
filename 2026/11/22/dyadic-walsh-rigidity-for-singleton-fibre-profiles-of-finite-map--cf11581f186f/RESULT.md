# Dyadic Walsh rigidity for singleton-fibre profiles of finite maps

## Finding

For each integer \(n\ge1\), associate to a map \(f:[n]\to[n]\) its *singleton-fibre set* \(S(f)=\{i\in[n]:|f^{-1}(i)|=1\}\). Let \(a_n(x)=\#\{f:S(f)=\operatorname{supp}(x)\}\) for \(x\in\mathbb F_2^n\), counting each map exactly once, and define unnormalized XOR convolution on \(\mathbb C^{\mathbb F_2^n}\) by
\[
(T_ng)(x)=\sum_{y\in\mathbb F_2^n}a_n(y)g(x\oplus y).
\]
For a Walsh frequency \(u\in\mathbb F_2^n\) of weight \(k\), its eigenvalue is
\[
\Lambda_{n,k}=\sum_{j=0}^{k}\binom{k}{j}(-2)^j\frac{n!}{(n-j)!}(n-j)^{n-j},\qquad 0\le k\le n,
\]
with \(0^0=1\). These eigenvalues have the following *complete nonvanishing and dyadic valuation classification*.

- At order one the eigenvalues are \(1,-1\). At order two they are \(4,0,4\) at weights \(0,1,2\), respectively. Thus \(T_2\) has rank two and nullity two.
- At every odd order, all eigenvalues are odd integers, hence nonzero.
- At every even order \(n\ge4\), writing \(\nu_2\) for the exponent of two in a nonzero integer,
\[
\nu_2(\Lambda_{n,0})=n\nu_2(n),\qquad
\nu_2(\Lambda_{n,k})=1+\nu_2(n)+\nu_2(k)\quad(1\le k\le n).
\]

Therefore, for every positive integer \(n\), **XOR convolution is singular if and only if \(n=2\)**. At even orders \(n\ge4\) the exact determinant valuation is
\[
\nu_2(\det T_n)=n\nu_2(n)+(2^n-1)(1+\nu_2(n))
+\sum_{k=1}^n\binom nk\nu_2(k).
\]
Moreover, the nonconstant Fourier modes with dyadic valuation \(1+\nu_2(n)+r\) have multiplicity \(\sum_{1\le k\le n,\,\nu_2(k)=r}\binom nk\) for each \(r\ge0\), with one separate constant mode of valuation \(n\nu_2(n)\).

## Assumptions and scope

All maps are labelled, unrestricted functions from \([n]\) to itself; no probabilistic independence is imposed on the fibre occupancies after conditioning on the total number of inputs. The group is the Boolean vector space \(\mathbb F_2^n\) with XOR addition; characters are \(\chi_u(x)=(-1)^{u\cdot x}\). Multipliers are *unnormalized map counts*, not probabilities. Multiplicity refers to algebraic eigenvalue multiplicity in the full \(2^n\)-dimensional complex group algebra. The determinant formula applies to even \(n\ge4\). No claim is made about the exact Euclidean condition number or the sign of every eigenvalue.

## Proof

Fix a character support \(U\subseteq[n]\) of cardinality \(k\). The multiplier is \(\sum_f(-1)^{|S(f)\cap U|}\). Expand each singleton indicator using \((-1)^{1_A}=1-2\,1_A\). For a prescribed set \(J\subseteq U\) with \(|J|=j\), exactly one preimage must map to each output in \(J\). There are \((n)_j=n!/(n-j)!\) injections choosing these labelled preimages, after which each remaining input has \(n-j\) admissible outputs. The resulting number of maps is \((n)_j(n-j)^{n-j}\). Summation over \(J\) yields the stated exact multiplier formula. Equivalently, the exponential generating function identity is
\[
\Lambda_{n,k}=n!\,[z^n]e^{(n-k)z}(e^z-2z)^k.
\]
Since every Walsh character is an eigenvector, its nonvanishing determines convolution invertibility.

If \(n\) is odd, the term with \(j=0\) is \(n^n\), which is odd, while every term with \(j\ge1\) contains a factor of two. Hence all multipliers are odd. Direct evaluation gives the stated order-one and order-two lists.

Now assume that \(n\ge4\) is even and \(k\ge1\). Write \(a=\nu_2(n)\) and \(b=\nu_2(k)\). The \(j=1\) term has exact valuation \(1+a+b\), because \(n-1\) is odd. The \(j=0\) term has valuation \(na\), which is strictly larger than \(1+a+b\): this is immediate for \(n=4\), while for even \(n\ge6\) the elementary bound \(b\le\lfloor\log_2n\rfloor\le n-3\) gives \((n-1)a>b+1\).

For each \(2\le j\le k\), factor the coefficient as
\[
\binom{k}{j}(n)_j=\frac{kn}{j}\binom{k-1}{j-1}(n-1)_{j-1}.
\]
The nonnegative valuations of the two factors on the right after the fraction give the lower bound
\[
\nu_2\!\left((-2)^j\binom kj(n)_j(n-j)^{n-j}\right)
\ge a+b+j-\nu_2(j)+(n-j)\nu_2(n-j),
\]
where the last summand is defined as zero when \(j=n\). If \(j\ge3\), then \(j-\nu_2(j)\ge2\). If \(j=2\), then \(n-j\) is positive and even, so \((n-j)\nu_2(n-j)\ge2\). In either case the valuation is strictly larger than \(1+a+b\). The \(j=1\) summand is thus uniquely of minimal dyadic valuation and cannot be cancelled; this proves the exact formula for nonconstant characters. At \(k=0\), the multiplier is \(n^n\) and has valuation \(na\).

Lastly, the Walsh basis diagonalizes \(T_n\). For each \(k\), there are \(\binom nk\) characters of weight \(k\). Summing the valuations of their nonzero eigenvalues gives the determinant and multiplicity formulas. The order-two nullity is \(\binom21=2\). This completes the proof for all positive orders.

## Verification

Execute `python3 check.py` with standard Python. The code independently enumerates all maps and computes each Walsh transform through \(n=6\), compares an exponential generating-function coefficient calculation through \(n=12\), tests all multiplier valuations through \(n=160\), and compares determinant valuations through \(n=40\). It passed 13,296 exact assertions. Exhaustive finite computations check the implementation and low-order boundaries; the all-order theorem follows from the proof above, not from extrapolation.

## Relationship to prior work

Milenkovic and Compton's classical 2004 study develops exact Poissonization and de-Poissonization for urn occupancies and the general counting framework. A published 2015 solution by Riedel gives the bivariate generating function for the *number* of singly occupied boxes, from which the character-generating-function identity can be recovered. These are credited counting inputs; neither inspected treatment states the all-order 2-adic valuation, binary Fourier rank, or determinant stratification. Barbour and Gnedin (2008) study *small occupancy counts* in an infinite-box asymptotic regime rather than this finite equal-box spectral question. The new statement requires the unique-minimal-valuation comparison across all character weights; the raw generating-function identity itself is not claimed as new.

## Limitations

This is an arithmetic and invertibility theorem, not a sign or real-condition-number classification. A 2-adic valuation of a Fourier eigenvalue is not its real magnitude. The theorem is based on exact self-contained algebraic proof with finite independent checks, but has not undergone independent mathematical audit. Broader unindexed occupancy literature could conceivably contain the same nonvanishing or valuation theorem, particularly as a consequence of general signed occupancy identities.

## References

1. O. Milenkovic and K. J. Compton, *Probabilistic Transforms for Combinatorial Urn Models*, Combinatorics, Probability and Computing 13 (2004), 645–675, DOI: https://doi.org/10.1017/S0963548304006285 (first publicly verified online 24 September 2004).
2. M. Riedel, answer to *Probability of \(k\) boxes containing exactly one ball*, Mathematics Stack Exchange (30 July 2015), https://math.stackexchange.com/questions/801454/probability-of-k-boxes-contain-exactly-1-ball/1379701 .
3. A. D. Barbour and A. V. Gnedin, *Small Counts in the Infinite Occupancy Scheme* (arXiv:0809.4387, 2008), https://arxiv.org/abs/0809.4387 .
