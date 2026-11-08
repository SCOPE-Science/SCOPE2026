# A sharp one-switch run-length covariance law for fixed-weight binary circles

## Finding

Let \(n\ge3\). Choose uniformly among the \(\binom nk\) labeled cyclic zero–one words with exactly \(k\) ones, where \(1\le k\le n-1\). Write \(R\) for the number of maximal cyclic one-runs and \(S_\ell\) for the number of those of length exactly \(\ell\). For \(1\le\ell\le k\), \(n-k\ge2\) and \(n\ge\ell+3\),

\[
\boxed{\operatorname{Cov}(R,S_\ell)
=n\frac{(k)_{\underline\ell}(n-k)_{\underline2}}{(n)_{\underline{\ell+2}}}
\frac{(n-k-1)[(\ell+1)k-(\ell-1)n-2]}{(n-1)(n-\ell-2)}.}
\]

Consequently its sign is precisely the sign of the integer \((\ell+1)k-(\ell-1)n-2\). Every nondegenerate fixed-weight cyclic word class with \(2\le k\le n-2\) exhibits **exactly one positive-to-negative transition** as \(\ell\) runs through \(1,\ldots,k\): strictly positive at \(\ell=1\), strictly negative at \(\ell=k\), with at most one zero in between.

If \(n=\ell+2\) and \(k=\ell\), the exceptional boundary value is \(2(1-\ell)/(\ell+1)^2\); if \(\ell>k\) or \(k=n-1\), the covariance is zero. For each fixed \(\ell\ge2\) and \(k/n\to p\in(0,1)\),

\[
\frac1n\operatorname{Cov}(R,S_\ell)\longrightarrow
p^\ell(1-p)^3[(\ell+1)p-(\ell-1)],
\]

whose interior sign transition is at \(p=(\ell-1)/(\ell+1)\).

## Assumptions and scope

Sites are labeled and arranged cyclically, with independent-of-rotation placement **not** assumed; every fixed-\(k\) word has equal probability. A run begins at an index \(i\) where \(X_{i-1}=0\) and \(X_i=1\), subscripts modulo \(n\). A run of length exactly \(\ell\) is the occurrence \(0,1,\ldots,1,0\) with exactly \(\ell\) consecutive ones between zeros. The falling factorial is \((x)_{\underline m}=x(x-1)\cdots(x-m+1)\), \((x)_{\underline0}=1\). No infinite-sequence or independent-site assumption is used for the finite theorem.

## Proof

**Mean identities.** By sampling without replacement, the probability of a prescribed \(0,1\) pair is \(k(n-k)/(n(n-1))\); hence \(\mathbb ER=k(n-k)/(n-1)\). Write \(J_i\) for the indicator of the prescribed exact run \(0,1^\ell,0\) starting at \(i\). For \(n\ge\ell+2\), the pattern fixes \(\ell\) ones and two distinct zeros, so

\[
\mathbb ES_\ell=n\mathbb EJ_i
=n\frac{(k)_{\underline\ell}(n-k)_{\underline2}}{(n)_{\underline{\ell+2}}}.
\]

**Marked-run conditional expectation.** Given \(J_i=1\), exactly one one-run is fixed. The \(m=n-\ell-2\) remaining sites form a contiguous linear interval between two forced zeros, with \(a=k-\ell\) ones and \(b=n-k-2\) zeros. If \(m\ge1\), the expected number of new runs starting in that interval is \(a/m+(m-1)ab/[m(m-1)]=a(b+1)/m\); the formula remains valid when \(m=1\) by directly considering the first site. Thus

\[
\mathbb E[R\mid J_i=1]=1+\frac{(k-\ell)(n-k-1)}{n-\ell-2}.
\]

Multiplying the difference with \(\mathbb ER\) by \(\mathbb ES_\ell\) yields

\[
\operatorname{Cov}(R,S_\ell)=\mathbb ES_\ell
\left(1+\frac{(k-\ell)(n-k-1)}{n-\ell-2}-\frac{k(n-k)}{n-1}\right).
\]

An exact common-denominator expansion factors the parenthesis as \((n-k-1)[(\ell+1)k-(\ell-1)n-2]/[(n-1)(n-\ell-2)]\), proving the displayed identity.

**Boundary.** If \(m=0\), nonzero \(J_i\) requires \(k=\ell=n-2\), and \(R=1\) conditioned on \(J_i=1\). Since \(\mathbb ES_\ell=n/\binom n2=2/(n-1)\) and \(\mathbb ER=2(n-2)/(n-1)\), the covariance equals \(2(1-\ell)/(\ell+1)^2\). If \(k=n-1\), every word has exactly one one-run and \(R\) is deterministic. If \(\ell>k\), \(S_\ell=0\).

**One switch.** In the interior range, the sign polynomial
\[
B_{n,k}(\ell)=(\ell+1)k-(\ell-1)n-2
\]
strictly decreases with \(\ell\), by \(n-k>0\), and \(B_{n,k}(1)=2(k-1)>0\) when \(k\ge2\). If \(n-k\ge3\), \(B_{n,k}(k)=(k-1)(2-(n-k))<0\). If \(n-k=2\), the last point \(\ell=k\) belongs to the exceptional boundary and has strictly negative covariance, while its immediate predecessor has positive sign. This proves exactly one transition, interpreted as a single zero when the integer affine expression vanishes at an interior run length.

**Asymptotic phase line.** With \(\ell\) fixed and \(k/n\to p\in(0,1)\), the marked-run mean divided by \(n\) tends to \(p^\ell(1-p)^2\), while the multiplicative covariance-to-mean ratio tends to \((1-p)[(\ell+1)p-(\ell-1)]\). Multiplication gives the limit and its unique interior zero for \(\ell\ge2\).

## Verification

The standalone standard-library program `verify.py` checks the exact covariance by independently enumerating every fixed-weight labeled circle of lengths \(3\) through \(14\), including all possible one-run lengths, and checks the sign classification for all sample sizes \(4\) through \(149\). It reports 22,288 passing exact rational assertions. The mathematical proof above, not this finite verification, establishes the infinite classifications.

Run from the same directory as `verify.py`:

```bash
python3 verify.py
```

## Relationship to prior work

Inoue and Aki (2005) derive joint generating functions and mixed-moment recursions for run counts at specified lengths on a circle. Their broader distributional machinery can in principle recover the present mixed covariance by further coefficient extraction and conditioning, so the existence of an exact moment computation is **not** asserted to be novel. The distinction is the closed, factored fixed-composition covariance and its global strict one-switch sign classification with exact arithmetic zero criterion and density phase transition, not stated in the inspected source. Makri, Philippou, and Psillakis (2007) establish marginal and same-threshold run statistics under urn sampling; Eryilmaz (2008) presents general joint run-pattern distributions; Makri, Psillakis, and Arapis (2013) count circular overlapping runs. These results supply relevant context but no inspected statement of the present sign theorem.

## Limitations

This theorem concerns uniformly sampled **labeled** circular fixed-weight words, not a uniformly sampled rotation-class necklace, nonuniform placements, or arbitrary dependent binary processes. The mixed moment is obtainable in principle from prior joint-distribution machinery; historical priority of the reduced sign classification is provisional until independent review of further run-statistics literature, including the closely related Inoue–Aki (2010) work. Finite enumeration is a test, not a general proof. Exact public day verified for the 2013 comparison paper is 9 July 2013; the 2005, 2007, and 2008 papers predate it but an original day of public release was not verified here.

## References

- K. Inoue and S. Aki, “Joint distributions of numbers of success runs of specified lengths in linear and circular sequences,” *Annals of the Institute of Statistical Mathematics* 57 (2005), 353–368, DOI 10.1007/BF02507029. https://www.ism.ac.jp/editsec/aism/pdf/057_2_0353.pdf
- F. S. Makri, A. N. Philippou, and Z. M. Psillakis, “Success run statistics defined on an urn model,” *Advances in Applied Probability* 39 (2007), 991–1019, DOI 10.1239/aap/1198177236.
- S. Eryilmaz, “Run statistics defined on the multicolor urn model,” *Journal of Applied Probability* 45 (2008), 1007–1023, DOI 10.1239/jap/1231340230.
- K. Inoue and S. Aki, “On the conditional and unconditional distributions of the number of success runs on a circle with applications,” *Statistics & Probability Letters* 80 (2010), 874–885.
- F. S. Makri, Z. M. Psillakis, and A. N. Arapis, “Counting runs of ones with overlapping parts in binary strings ordered linearly and circularly,” *International Journal of Statistics and Probability* 2 (2013), 50 ff., DOI 10.5539/ijsp.v2n3p50. https://ccsenet.org/journal/index.php/ijsp/article/view/28864
