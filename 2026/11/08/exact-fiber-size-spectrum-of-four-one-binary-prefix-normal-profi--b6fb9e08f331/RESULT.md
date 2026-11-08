# Exact fiber-size spectrum of four-one binary prefix-normal profiles

## Finding

For every integer \(n\ge4\), let \(\mathcal W_{n,4}\) be the set of indexed binary words of length \(n\) with four occurrences of \(1\). For \(w\in\mathcal W_{n,4}\), define the maximum-one-factor profile
\[
F_w(k)=\max_{0\le j\le n-k}\bigl|w_{j+1}\cdots w_{j+k}\bigr|_1,\quad 0\le k\le n.
\]
Two words are **1-prefix equivalent** when these profiles agree at every length. Let \([w]_1\) be the equivalence class. Each class has a unique 1-prefix-normal representative.

All classes are uniquely indexed by four nonnegative integers \((m,p,q,r)\) satisfying \(3m+p+q+r=n-4\). The corresponding representative has its four ones at positions
\[
1,\quad 2+m,\quad 3+2m+p,\quad 4+3m+p+q,
\]
with zeros elsewhere. Its class has cardinality
\[
\boxed{|[w]_1|=(r+1)H(p,q)},\qquad
H(p,q)=\begin{cases}
1,&q=0,\\
2,&p=0<q\ \text{or}\ 0<q<p,\\
3,&0<p=q,\\
4,&0<p<q.
\end{cases}
\]
Thus the **entire class-size distribution** for every \(n\ge4\) is the finite polynomial
\[
\boxed{B_n(y)=\sum_{\substack{m,p,q,r\ge0\\3m+p+q+r=n-4}}y^{(r+1)H(p,q)}}.
\]
This polynomial records one monomial per class, including multiplicities of equal class sizes.

Let \(S_2(n)=\sum_{[w]_1}|[w]_1|^2\). Then
\[
\boxed{\sum_{n\ge4}S_2(n)z^n=\frac{z^4(1+4z+8z^2+7z^3)}{(1-z)^5(1-z^3)}}.
\]
For every \(n\ge10\), the largest class has size exactly \(4(n-6)\), and the unique maximizing prefix-normal representative is the word \(1101001\,0^{n-7}\). At smaller lengths the maximum is explicitly
\[
\max_{0\le j\le\min(3,n-4)}(j+1)(n-3-j).
\]
For independent uniform \(W,V\in\mathcal W_{n,4}\),
\[
\Pr(F_W=F_V)=\frac{S_2(n)}{\binom n4^2}=\frac{32}{n^3}+O(n^{-4}),
\qquad \mathbb E|[W]_1|=\frac{4}{3}n+O(1).
\]

## Assumptions and scope

Words are linear, with indexed positions and the binary alphabet \(\{0,1\}\). The exact composition is four ones, so \(n\ge4\). All factors are contiguous and nonempty except the harmless \(k=0\) profile entry. Equivalence uses **only the maximum number of ones** among factors at each length; it does **not** require the minimum number of ones to agree. Consequently, the class sizes here are generally larger than the classes defined by identical complete factor-Parikh sets. The parameterization includes all leading and trailing zero gaps and all boundary cases \(p=0\), \(q=0\) and \(p=q\).

## Proof

**1. Shortest-span characterization.** Write a word uniquely as
\[
w=0^a1\,0^b1\,0^c1\,0^d1\,0^e,
\qquad a,b,c,d,e\ge0,\quad a+b+c+d+e=n-4.
\]
The least possible length of a factor containing at least \(j\) ones equals the least span of \(j\) consecutive one positions: whenever a factor contains \(j\) ones, some consecutive \(j\) of them lie in that factor, and conversely such a span is itself a factor. For \(j=1,2,3,4\), these four threshold lengths are
\[
1,\quad 2+\min(b,c,d),\quad
3+\min(b+c,c+d),\quad 4+b+c+d.
\]
The complete nondecreasing integer function \(F_w\) is determined by these threshold crossings: \(F_w(k)\ge j\) if and only if \(k\) is at least the corresponding threshold. Put
\[
m=\min(b,c,d),\qquad v=c+\min(b,d),\qquad s=b+c+d.
\]
Hence \((m,v,s)\), with the common length \(n\), is a complete and injective identifier for a 1-prefix equivalence class, and its canonical prefix-normal word has ones at positions \(1,2+m,3+v,4+s\).

**2. Unrestricted nonnegative profile coordinates.** Set \(u=\min(b,d)\) and \(t=\max(b,d)\). Then
\[
v=c+u,\quad s=v+t,\quad m=\min(c,u),\quad t\ge u.
\]
It follows that \(v\ge2m\) and \(s\ge v+m\). Therefore there are unique nonnegative integers
\[
p=v-2m,\qquad q=s-v-m,\qquad r=n-4-s,
\]
and \(3m+p+q+r=n-4\). Conversely, for every such quadruple choose \((u,c,t)=(m,m+p,m+q)\) and any nonnegative exterior gaps totaling \(r\). This realizes the thresholds, so no other feasibility inequalities exist. Uniqueness of \((m,v,s)\) makes distinct quadruples yield distinct classes.

**3. Exact inverse-fiber size.** With \(m,p,q\) fixed, the condition \(m=\min(u,c)\) and \(u+c=2m+p\) permits \((u,c)=(m,m+p)\), always, and also \((u,c)=(m+p,m)\) when \(p>0\). The second option also requires \(u\le t=m+q\), or \(q\ge p\). For either choice, the ordered pair \((b,d)\) has two orientations unless \(u=t\), when it has one. The two choices coincide at \(p=0\), so they must not be double counted. This gives exactly the five cases in \(H(p,q)\). Independently, \(a+e=r\) has precisely \(r+1\) nonnegative ordered solutions. This proves \(|[w]_1|=(r+1)H(p,q)\) and the complete polynomial \(B_n(y)\).

**4. Squared-fiber generating function.** Directly summing the disjoint five regions for \(H\) gives
\[
\sum_{p,q\ge0}H(p,q)^2z^{p+q}
=\frac{1+4z+8z^2+7z^3}{(1-z)^2(1+z)}.
\]
Multiplying by the independent sums \(\sum_{m\ge0}z^{3m}=1/(1-z^3)\) and \(\sum_{r\ge0}(r+1)^2z^r=(1+z)/(1-z)^3\), and accounting for the four required one positions, gives the displayed rational function for \(S_2(n)\). As a consistency check, summing unsquared fibers gives \(\sum_{n\ge4}\binom n4 z^n=z^4/(1-z)^5\), the total population of weight-four words.

**5. Sharp maximum and limiting collision law.** For a class with \(H=j+1\), where \(j\in\{0,1,2,3\}\), the internal budget \(3m+p+q\) is at least \(j\). Equality is achieved at respectively \((m,p,q)=(0,0,0),(0,0,1),(0,1,1),(0,1,2)\). Thus its size is at most \((j+1)(n-3-j)\), and the bound is attained whenever this budget is available. This proves the maximum formula. For \(n\ge10\), the \(j=3\) candidate uniquely exceeds every other candidate, giving the stated unique maximizer.

Near \(z=1\), the second-moment generating function has principal part \(\frac{20}{3}(1-z)^{-6}\), while its other poles are simple roots of unity. Thus \(S_2(n)=n^5/18+O(n^4)\). Division by \(\binom n4\sim n^4/24\) proves the size-biased mean, and division by \(\binom n4^2\) proves the collision probability constant \(32\).

## Verification

Run the included standalone Python 3 standard-library program using `python3 verify.py`. It directly constructs all \(33{,}649\) weight-four words at lengths \(4\) through \(22\), computes every sliding-window maximum independently from the gap parameterization, and verifies full class membership, size and the exact squared-fiber coefficients. It also checks the integer-parameter formulas, population totals, second moments and sharp maximum through length \(200\). The recorded output is:

```text
DIRECT_SLIDING_WINDOW_OK 33649 N_4_TO_22
EXACT_FIBER_AND_SECOND_MOMENT_OK N_4_TO_200
ASYMPTOTIC_CONSTANT_FROM_POLE_OK 32
ALL_CHECKS_PASSED
```

These finite checks are consistency evidence; the arbitrary-length assertions follow from the preceding algebraic proof.

## Relationship to prior work

The definition and uniqueness of prefix-normal forms, their role in jumbled matching and finite tables of unrestricted fiber maxima are classical from Fici and Lipták (2011). Burcsi et al. (2014) generate prefix-normal words of fixed density; Burcsi et al. (2016) explicitly derive the **number** of weight-four 1-prefix-normal representatives, with generating function \(z^4/((1-z^3)(1-z)^3)\). That known class-count identity is not a novelty claim. The present finding instead determines every individual inverse-fiber cardinality, its complete size distribution, exact squared-fiber generating function, sharp fixed-weight maximizer and random collision asymptotic. Balister and Gerke (2019) address the unrestricted-alphabet-composition maximum through asymptotic bounds; this does not determine the fixed-four-one optimum. OEIS A238110 tabulates maxima without restricting Hamming weight.

## Limitations

The result applies only to four-one words and the one-sided maximum-one profile. It does not classify pairs agreeing on **both** prefix-normal forms or on their entire factor-Parikh sets. In particular the collision probability is for one-sided profiles, not full jumbled-index equality. Historical priority remains qualified because unindexed earlier equivalent calculations cannot be ruled out by database search. No independent mathematical audit has been performed.

## References

- G. Fici and Z. Lipták, *On Prefix Normal Words*, Developments in Language Theory (2011), DOI: https://doi.org/10.1007/978-3-642-22321-1_20 ; accessible preprint copy https://arxiv.org/abs/1805.12405 (later upload).
- P. Burcsi et al., *On Combinatorial Generation of Prefix Normal Words* (2014), https://arxiv.org/abs/1401.6346 .
- P. Burcsi et al., *Normal, Abby Normal, Prefix Normal* (2014), https://arxiv.org/abs/1404.2824 .
- P. Burcsi et al., *On Prefix Normal Words and Prefix Normal Forms* (2016 preprint), https://arxiv.org/abs/1611.09017 .
- P. Balister and S. Gerke, *The asymptotic number of prefix normal words* (2019), https://arxiv.org/abs/1903.07957 .
- OEIS A238110, maximum size of an unrestricted binary prefix-normal-form class, https://oeis.org/A238110 .
