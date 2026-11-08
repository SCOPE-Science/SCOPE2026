# Sharp total-variation constant for simple chords in a uniform chord diagram

## Finding

Let \(S_n\) be the number of simple chords in a uniformly chosen perfect matching of \(2n\) cyclically ordered, distinctly labeled points. A simple chord pairs adjacent points, including the pair crossing the cyclic boundary. For every integer \(n\ge2\), the law admits the **uniform signed local expansion**

\[
\Pr(S_n=r)=\frac{e^{-1}}{r!}\left(1+\frac{-r^2+5r-3}{4n}\right)+\varepsilon_{n,r},
\qquad |\varepsilon_{n,r}|\le C n^{-2}2^{-r}
\]

for **all integers** \(r\ge0\), with a universal finite constant \(C\). Consequently,

\[
\boxed{d_{\mathrm{TV}}(\mathcal L(S_n),\operatorname{Pois}(1))
=\frac{73}{96e}\frac1n+O(n^{-2}).}
\]

In particular, the probability of having no simple chords is

\[
\Pr(S_n=0)=e^{-1}\left(1-\frac{3}{4n}\right)+O(n^{-2}).
\]

The leading local correction is positive for exactly \(r=1,2,3,4\), and negative for \(r=0\) and \(r\ge5\). Thus the total-variation constant is the total positive mass of an explicit signed perturbation. This statement includes both the sharp constant and the uniform local law; it is one coherent asymptotic distributional finding.

## Assumptions and scope

The sample space comprises all \((2n-1)!!\) perfect matchings of \(\{0,1,\ldots,2n-1\}\), equally likely. The cyclic adjacency pairs are \(\{i,i+1\bmod 2n\}\). For \(n\ge2\) these form a simple cycle with \(2n\) distinct edges. We write \((S_n)_k=S_n(S_n-1)\cdots(S_n-k+1)\), with \((S_n)_0=1\). Set \(N=2n\). Total variation is \(d_{\mathrm{TV}}(P,Q)=\frac12\sum_{r\ge0}|P\{r\}-Q\{r\}|\).

The result compares with the **fixed** law \(\operatorname{Pois}(1)\), not with a mean-matched Poisson law depending on \(n\). It is asserted for all large \(n\) with a uniform absolute error bound, and the exact factorial identities below hold for every \(n\ge2\). The special case \(n=1\) has two coincident cyclic adjacency arcs and is intentionally excluded.

## Proof

**1. Exact factorial moments.** A set of \(k\) required simple chords must be a matching of size \(k\) in the cyclic graph \(C_N\). The number of such sets is the classical cycle-matching count

\[
 m(C_N,k)=\frac{N}{N-k}\binom{N-k}{k},\qquad 0\le k\le n.
\]

For completeness, mark a selected cycle edge and cut the cycle immediately after it; counting linearly ordered gaps between the \(k\) selected edges yields \(N\binom{N-k-1}{k-1}/k\) when \(k\ge1\), which simplifies to the displayed formula; \(k=0\) gives one empty selection. The probability that every edge of a fixed set of \(k\) disjoint pairs occurs in the uniform perfect matching is \((N-2k-1)!!/(N-1)!!\). Counting **ordered** sets gives

\[
 a_{N,k}:=\mathbb E(S_n)_k
 = k!\frac{N}{N-k}\binom{N-k}{k}
 \frac{(N-2k-1)!!}{(N-1)!!}
 =\prod_{j=0}^{k-1}\frac{N-2j}{N-j-1},\qquad 0\le k\le n.
\]

Extend \(a_{N,k}=0\) when \(k>n\). Thus \(a_{N,0}=1\), and for \(0\le k<n\),

\[
 a_{N,k+1}=a_{N,k}\left(1+\frac{1-k}{N-k-1}\right).
\]

All factors are nonnegative; the first is greater than one, the second is one, and subsequent factors do not exceed one. In particular,

\[
0\le a_{N,k}\le\frac{N}{N-1}\le\frac43\qquad(N\ge4,\ k\ge0).
\]

**2. A factorial-moment expansion with uniform summable error.** Define \(b_k=k(3-k)/2\). Then \(b_0=0\) and \(b_{k+1}-b_k=1-k\). For \(k\le N/4\), the recurrence and the uniform bound above give

\[
 |a_{N,k}-1|\le C_1(k+1)^2/N.
\]

For \(0\le k<N/4\), subtracting the recurrence for \(1+b_k/N\) from the exact recurrence yields

\[
 \left(a_{N,k+1}-1-\frac{b_{k+1}}N\right)
 -\left(a_{N,k}-1-\frac{b_k}N\right)
 =(1-k)\left(\frac{a_{N,k}-1}{N-k-1}
 +\frac{k+1}{N(N-k-1)}\right).
\]

Its absolute value is at most \(C_2(k+1)^3/N^2\), since the denominators are bounded below by a fixed multiple of \(N\). Summing from \(0\) gives \(C_3(k+1)^4/N^2\) for \(k\le N/4\). For \(k>N/4\), including \(k>n\), the coarse bounds \(|a_{N,k}|\le4/3\) and \(|b_k|\le C_4(k+1)^2\), together with \(k>N/4\), imply the same bound after increasing the absolute constant. Therefore for **every integer** \(k\ge0\) and \(N\ge4\),

\[
\left|a_{N,k}-1-\frac{k(3-k)}{2N}\right|
\le C_5\frac{(k+1)^4}{N^2}.
\]

**3. Analytic probability-generating function.** The exact factorial-moment identity gives the finite polynomial

\[
G_n(z):=\mathbb E z^{S_n}
=\sum_{k\ge0}\frac{a_{N,k}}{k!}(z-1)^k.
\]

The last estimate and factorial summability imply, uniformly on any fixed complex disk \(|z|\le R\),

\[
G_n(z)=e^{z-1}\left[1+\frac{-(z-1)^2+2(z-1)}{2N}\right]
+O_R(N^{-2})
=e^{z-1}\left[1+\frac{-z^2+4z-3}{2N}\right]+O_R(N^{-2}).
\]

Indeed, \(\sum_{k\ge0}k(z-1)^k/k!=(z-1)e^{z-1}\) and the analogous second falling-factorial sum is \((z-1)^2e^{z-1}\). On \(|z|=2\), Cauchy's coefficient bound gives an error at coefficient \(z^r\) of at most \(C_6N^{-2}2^{-r}\), uniformly in \(r\ge0\). Extracting the polynomial's coefficients against \(e^{z-1}\) yields

\[
[z^r]G_n(z)=\frac{e^{-1}}{r!}
\left[1+\frac{-r(r-1)+4r-3}{2N}\right]
+O(N^{-2}2^{-r}),
\]

which is the stated local law because \(N=2n\).

**4. Sharp total variation.** The polynomial \(Q(r)=-r^2+5r-3\) is strictly positive exactly when \(r=1,2,3,4\) among nonnegative integers. The signed coefficient correction is normalized because \(\mathbb E Q(P)=0\) for \(P\sim\operatorname{Pois}(1)\) (use \(\mathbb EP=1\) and \(\mathbb EP^2=2\)). Its positive mass is

\[
\frac{e^{-1}}{4n}\sum_{r=1}^{4}\frac{Q(r)}{r!}
=\frac{e^{-1}}{4n}\left(1+\frac32+\frac36+\frac1{24}\right)
=\frac{73}{96en}.
\]

Because \(\sum_{r\ge0}2^{-r}<\infty\), the sum of absolute local errors is \(O(n^{-2})\). The total variation is therefore the positive signed mass plus \(O(n^{-2})\), giving the sharp constant. The displayed expansion at \(r=0\) follows by substitution. \(\square\)

## Verification

The standalone standard-library file `verify.py` independently enumerates all perfect matchings through \(n=6\); compares the resulting histograms to rational factorial moments and inversion; checks the exact cycle-matching counts; and repeats normalization, moment, variance, and recurrence identities through \(n=40\). It also includes noncertifying numerical convergence checks through \(n=120\). Run `python verify.py` in the same directory. Its recorded output is `VERIFY_OK 367 exact/reproducible assertions`.

These finite computations corroborate, but are not substitutes for, the uniform analytic remainder argument in the proof. The checker does not prove the infinitely quantified asymptotic result.

## Relationship to prior work

J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams* (first publicly released 2021), defines precisely this simple-chord count, proves \(d_{\mathrm{TV}}=O(n^{-1})\) against \(\operatorname{Pois}(1)\), and bounds the chance of zero simple chords (Section 3). The exact leading constant, complete signed local coefficient, and order-\(n^{-2}\) remainder obtained here sharpen those stated bounds. His mean-matched Poisson coupling is a distinct comparison and does not itself imply the constant for the fixed Poisson law.

H. Acan (2015; published 2017) treats simple chords and their Poisson convergence as part of random chord-diagram structure. Flajolet and Noy (2000) obtain the Poisson limit for the number of components and connected-diagram enumeration, a related but not identical statistic. None of the specific inspected arguments states the displayed first-order local law or total-variation constant. Established counting and Poisson-limit results are acknowledged; no claim of originating them is made.

## Limitations

The distributional correction concerns cyclic adjacency chords in **uniform** matchings, with the fixed \(\operatorname{Pois}(1)\) target. It makes no assertion about nonuniform matchings, crossings, or other chord lengths. An absolute constant is proved to exist in the order-\(n^{-2}\) remainder but is not optimized. Exact historical priority is not independently certified: additional older enumerative literature may encode an equivalent expansion implicitly. No independent external audit has been performed.

## References

1. J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134 (first version 2 April 2021), https://arxiv.org/html/2104.01134v2 (especially Sections 1 and 3).
2. H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489 (first version 7 January 2015), https://arxiv.org/abs/1501.01489 (especially the monolithic and simple-chord results).
3. P. Flajolet and M. Noy, *Analytic combinatorics of chord diagrams*, 2000, https://algo.inria.fr/flajolet/Publications/FlNo00.pdf (components and asymptotic chord-diagram counting).
