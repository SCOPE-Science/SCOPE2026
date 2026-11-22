# Two-scale one-deletion diversity in \(321\)-avoiding permutations

## Finding

For a permutation \(\pi\in\mathrm{Av}_n(321)\), let \(a(\pi)\) count indices satisfying \(\pi_{i+1}=\pi_i+1\), and let \(d(\pi)\) count indices satisfying \(\pi_{i+1}=\pi_i-1\). These are respectively *ascending* and *descending bonds*. Let \(R(\pi)\) be the number of distinct order-standardized length-\(n-1\) patterns obtained by deleting one position. For \(n\ge1\),
\[
R(\pi)=n-a(\pi)-d(\pi).
\]

Define the Catalan series \(C(z)=(1-\sqrt{1-4z})/(2z)\), with \(C(0)=1\), and set
\[
T(z,u)=C\!\left(\frac{z}{1-(u-1)z}\right).
\]
The exact trivariate ordinary generating function is
\[
H(z,u,v)=\sum_{n\ge0}\sum_{\pi\in\mathrm{Av}_n(321)}z^nu^{a(\pi)}v^{d(\pi)}
=\frac{T(z,u)}{1-(v-1)z^2T(z,u)}.
\]

For uniformly random \(\Pi_n\in\mathrm{Av}_n(321)\), as \(n\to\infty\),
\[
\left(\frac{a(\Pi_n)-n/4}{\sqrt{3n/16}},\ d(\Pi_n)\right)
\xrightarrow{d}(Z,N),
\qquad \mathbb E[v^N]=\left(\frac8{9-v}\right)^2,
\]
where \(Z\) is standard normal and is independent of \(N\). Thus \(N\) has the negative-binomial law \(\mathbb P(N=j)=64(j+1)/(81\cdot9^j)\) for integers \(j\ge0\). The number of distinct deletion patterns has the centered Gaussian limit
\[
\frac{R(\Pi_n)-3n/4}{\sqrt{3n/16}}\xrightarrow{d}N(0,1).
\]
For integers \(n\ge2\), the exact mean is
\[
\mathbb E[R(\Pi_n)]=n-\frac{n(n+1)}{2(2n-1)}.
\]

## Assumptions and scope

Permutation-pattern avoidance is classical (not consecutive): \(\pi\) avoids \(321\) when no \(i<j<k\) satisfy \(\pi_i>\pi_j>\pi_k\). The empty permutation contributes the constant term. Only a single deletion followed by order-standardization is considered; duplicate outputs are counted once. Both bond types require adjacent positions and consecutive *values*. The limiting law is for uniform sources in the Catalan class, not for uniformly random deletion outputs or a channel with independent noise.

## Proof

**(1) Standardized deletion identity.** In any permutation, two one-position deletions agree if and only if the corresponding positions lie in the same maximal monotone run of consecutive-value adjacent bonds. A run of length \(r\) contributes \(r\) deletion positions but one distinct outcome, hence reduces the number by \(r-1\). Summing disjoint runs proves \(R=n-a-d\). This is Homberger's bond lemma, not a new lemma.

**(2) Marked ascending bonds.** Expand \(u^{a(\pi)}\) as \((1+(u-1))^{a(\pi)}\) and choose an arbitrary subset of ascending bonds to mark. Contract each maximally marked ascending string to one entry and standardize. Because the contracted entries form a consecutive interval of values in increasing order, contraction and expansion preserve classical \(321\)-avoidance in both directions: a forbidden triple with two positions from one marked string is impossible since those positions increase; a forbidden triple with at most one position from each string corresponds exactly to a forbidden triple in the contracted permutation. A contracted permutation of length \(m\) has \(m\) nonempty blocks; their expansion lengths can be any positive integers and carry a weight \((u-1)^{\text{length}-1}\). Its total weighted contribution is \([z/(1-(u-1)z)]^m\). Summing the Catalan count \(C_m\) over \(m\) gives \(T(z,u)\). This is the previously known ascending-succession specialization.

**(3) Marked descending bonds.** If the adjacent entries \(x+1,x\) occur in a \(321\)-avoider, every preceding entry is less than \(x\), since a preceding larger entry would make a \(321\) pattern, and every following entry is greater than \(x+1\), for the same reason. Hence the word has a unique direct-sum decomposition into an arbitrary left \(321\)-avoider, the component \(21\), and an arbitrary right \(321\)-avoider. Choose and mark any subset of descending bonds, with each mark weighted \(v-1\). Cutting at all marked descending components decomposes the permutation uniquely as
\[
\sigma_0\oplus21\oplus\sigma_1\oplus21\oplus\dots\oplus21\oplus\sigma_j.
\]
There are no ascending bonds crossing any direct-sum boundary adjacent to a marked \(21\) component. Therefore each free segment has weight \(T(z,u)\), each marked descending component contributes \((v-1)z^2\), and summing over \(j\ge0\) yields
\[
H=T\sum_{j\ge0}\big((v-1)z^2T\big)^j=\frac{T}{1-(v-1)z^2T}.
\]
The direct-sum observation for a descending small descent appears in later literature; the claimed result is its joint application and resulting two-scale asymptotics.

**(4) Joint limit.** The singularity of \(T(z,u)\) near \(u=1\) is the square-root singularity \(\rho(u)=1/(u+3)\); at \(z=\rho(u)\) one has \(T=2\). In a fixed neighborhood of \(u=v=1\), the denominator \(1-(v-1)z^2T\) is nonzero at the dominant singularity. Algebraic square-root transfer is uniform there and gives
\[
\frac{[z^n]H(z,u,v)}{[z^n]H(z,1,1)}
=K(u,v)\left(\frac{u+3}{4}\right)^n\big(1+O(n^{-1})\big),
\]
for an analytic \(K\), with \(K(1,v)=(8/(9-v))^2\) and \(K(1,1)=1\). Set \(u=\exp(t/\sqrt{3n/16})\), compensate the linear centering \(n/4\), and use \(\log[(e^s+3)/4]=s/4+3s^2/32+O(s^3)\) as \(s\to0\). The resulting joint moment generating function converges to \(e^{t^2/2}(8/(9-v))^2\) for \(v\) near one. This proves asymptotic independence, the Gaussian limit for ascending bonds, and the stated tight negative-binomial limit for descending bonds. Since \(R=n-a-d\), the deletion-spectrum limit follows by Slutsky's theorem.

**(5) Exact mean.** Differentiate the bivariate generating functions at \(u=v=1\): the total count of ascending bonds over length \(n\ge2\) is \((n-1)C_{n-1}\), and the total descending bond count is \(C_{n-1}\). Since there are \(C_n\) avoiders, \(\mathbb E R=n-nC_{n-1}/C_n=n-n(n+1)/(2(2n-1))\). The mean identity is asserted for \(n\ge2\), not for the degenerate length-one case.

## Verification

The attached `verify.py` computes both actual standardized one-deletion output sets and the two bond counts for each \(321\)-avoider of lengths one through nine, and independently computes coefficients of the proposed joint generating function by exact integer polynomial arithmetic. It verifies equality of all finite joint distributions and of the one-deletion identity. Reproduce with `python3 verify.py` from the directory containing this file. These exhaustive finite checks support the proof but do not replace the all-length marked-decomposition and singularity arguments.

## Relationship to prior work

Homberger's 2012 preprint proves the general identity between distinct one-deletion patterns and the number of bonds. Baril's 2016 work contains the ascending-succession Catalan substitution formula, and Elizalde–Rivera–Zhuang 2026 identify small descending bonds as direct-sum components in \(321\)-avoiders while studying ordinary descents and small descents jointly. These known results supply the two separate building blocks. The assessed contribution is the **simultaneous ascending/descending bond enumerator** and the split, asymptotically independent Gaussian and negative-binomial deletion profile; no individual component lemma or unrestricted deletion law is claimed as novel.

## Limitations

The exact generating function proves a distribution, not decoding-code optimality or a multi-deletion theorem. No claim of finite-sample independence is made: the two bond statistics can be dependent at fixed length. Previously unindexed equivalent bivariate refinements may exist; the structural decomposition makes the result a close synthesis of known ideas. No independent audit has been performed.

## References

1. C. Homberger, *Counting Fixed-Length Permutation Patterns*, arXiv:1211.7117, version 1 publicly posted 2012-11-29, https://arxiv.org/abs/1211.7117.
2. J.-L. Baril, *Avoiding patterns in irreducible permutations*, DMTCS (2016), https://doi.org/10.46298/dmtcs.2158.
3. S. Elizalde, I. Rivera, Y. Zhuang, *Counting Pattern-Avoiding Permutations by Big Descents*, 2026, https://doi.org/10.1007/s00026-026-00805-1.
