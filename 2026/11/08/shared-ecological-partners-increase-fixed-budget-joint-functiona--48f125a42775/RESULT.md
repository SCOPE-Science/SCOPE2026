# Shared ecological partners increase fixed-budget joint functional survival in supermodular order

## Finding

**Theorem (fixed-budget overlap order and exact transfer law).** Let \(n\ge2\), \(0\le k\le n\), and \(1\le a,b\le n\) be integers. Choose uniformly a subset \(S\) of exactly \(k\) surviving primary species from a set of \(n\) species. Let two secondary ecological functions have partner sets \(A,B\) with \(|A|=a\), \(|B|=b\), and \(|A\cap B|=c\). The feasible overlap is every integer
\[
\max(0,a+b-n)\le c\le\min(a,b).
\]
Write \(X_c=|S\cap A|\) and \(Y_c=|S\cap B|\). Their marginal laws do not depend on \(c\). Nevertheless the joint laws **increase in the full supermodular order** with \(c\). Specifically, if \(c<\min(a,b)\) is feasible and \(\phi\) is any real function on \(\{0,\ldots,a\}\times\{0,\ldots,b\}\) such that
\[
\Delta_{12}\phi(i,j):=\phi(i+1,j+1)-\phi(i+1,j)-\phi(i,j+1)+\phi(i,j)\ge0,
\]
then \(\mathbb E\phi(X_{c+1},Y_{c+1})\ge \mathbb E\phi(X_c,Y_c)\). More precisely, writing \(\binom{N}{j}=0\) when \(j\notin\{0,\ldots,N\}\), the exact increment is
\[
\frac{1}{\binom nk}\sum_{\substack{h,u,v,w\ge0\\h+u+v+w=k-1}}
\binom ch\binom{a-c-1}{u}\binom{b-c-1}{v}\binom{n-a-b+c}{w}
\Delta_{12}\phi(h+u,h+v).
\tag{1}
\]
For integer functional quorums \(1\le r\le a\) and \(1\le s\le b\), the joint survival probability \(Q_c(r,s)=\Pr(X_c\ge r,Y_c\ge s)\) therefore satisfies the *sharp, entirely explicit* law
\[
Q_{c+1}(r,s)-Q_c(r,s)=\frac{1}{\binom nk}\sum_{h\in\mathbb Z}
\binom ch\binom{a-c-1}{r-1-h}\binom{b-c-1}{s-1-h}
\binom{n-a-b+c}{k-r-s+1+h}\ge0.
\tag{2}
\]
The inequality is strict if and only if at least one summand has all four valid positive binomial factors. Hence, for any fixed species-loss budget and any two quorum requirements, increasing overlap cannot reduce the probability that **both** functions survive, although each function's marginal survival probability stays unchanged.

**Sharp association boundary for one-partner functions.** When a function survives if at least one of its partners survives, let \(F_c=\mathbf 1\{X_c\ge1\}\) and \(G_c=\mathbf 1\{Y_c\ge1\}\). Their covariance is
\[
\operatorname{Cov}(F_c,G_c)=
\frac{\binom{n-a-b+c}{k}}{\binom nk}
-\frac{\binom{n-a}{k}\binom{n-b}{k}}{\binom nk^2}.
\tag{3}
\]
It is nondecreasing in \(c\), with increment \(\binom{n-a-b+c}{k-1}/\binom nk\). The covariance changes sign at most once from negative to positive (allowing zero and flat segments), and its exact positivity criterion is
\[
\binom{n-a-b+c}{k}\binom nk>\binom{n-a}{k}\binom{n-b}{k}.
\tag{4}
\]
For \(n=7\), \(k=3\), and \(a=b=3\), the successive covariance values at \(c=0,1,2,3\) are
\[
-\frac{16}{1225},\quad-\frac{16}{1225},\quad
\frac{19}{1225},\quad\frac{124}{1225}.
\]
Thus sharing *one* partner can leave the two functions negatively associated under an exact species-survival budget, while sharing two makes them positively associated. This contrasts with independent species failures, where any positive partner overlap gives nonnegative association of the one-partner function-survival indicators.

## Assumptions and scope

The population of primary species is finite and labelled. Exactly \(k\) survive, and all survivor sets of that size are equally likely. The two distinct secondary functions are determined by deterministic partner sets with fixed sizes \(a,b\). Their viability is a monotone quorum condition on the number of surviving partners; species interactions beyond these partner sets, secondary feedbacks, heterogeneous survival risks, and temporal spread are **not** modelled. The conclusions quantify over every integer \(n,k,a,b,c,r,s\) in the displayed ranges, and over all functions with nonnegative adjacent mixed differences. Both \(k=0\) and \(k=n\) are included, with zero increments. No strictness is claimed without the explicit positivity criterion.

## Proof

Fix a feasible overlap \(c<\min(a,b)\). By relabelling species we may keep \(A\) fixed and choose one species \(x\) exclusive to \(A\) and one species \(y\) exclusive to \(B\), then form \(B'=(B\setminus\{y\})\cup\{x\}\). Thus \(|A\cap B'|=c+1\) and \(|B'|=b\). The other species split into four disjoint regions: \(c\) shared partners, \(a-c-1\) remaining \(A\)-exclusive partners, \(b-c-1\) remaining \(B\)-exclusive partners, and \(n-a-b+c\) species outside both partner sets. Let their survivor counts be \(h,u,v,w\), respectively.

If the survival status of \(x\) and \(y\) is the same, the pair \((|S\cap A|,|S\cap B'|)\) equals \((|S\cap A|,|S\cap B|)\), so the contribution to the expectation difference is zero. If exactly one of \(x,y\) survives, the two possible survivor configurations (one with \(x\) and not \(y\), the other with \(y\) and not \(x\)) together contribute
\[
\phi(h+u+1,h+v+1)+\phi(h+u,h+v)
-\phi(h+u+1,h+v)-\phi(h+u,h+v+1)
=\Delta_{12}\phi(h+u,h+v).
\]
Because exactly one special species survives, the four other counts sum to \(k-1\). The number of ways to realize each configuration with prescribed counts is the product of the four binomial coefficients in (1). Uniform division by \(\binom nk\) gives (1). Every weight is nonnegative, so supermodularity proves the asserted stochastic order, including all boundary cases. The marginal distributions are separately hypergeometric, depending only on \(n,k,a\) and \(n,k,b\).

For \(\phi(i,j)=\mathbf 1\{i\ge r\}\mathbf 1\{j\ge s\}\), the adjacent mixed difference is precisely \(\mathbf 1\{i=r-1,j=s-1\}\). Substituting \(u=r-1-h\), \(v=s-1-h\), and \(w=k-r-s+1+h\) in (1) proves (2), including its necessary-and-sufficient strictness criterion.

For (3), the two groups both fail precisely when \(S\) avoids the union \(A\cup B\) of size \(a+b-c\), an event of probability \(\binom{n-a-b+c}{k}/\binom nk\). Each group separately fails with respective probabilities \(\binom{n-a}{k}/\binom nk\) and \(\binom{n-b}{k}/\binom nk\). Inclusion–exclusion and subtraction of the fixed product of marginal survival probabilities yield (3). Pascal's rule gives its adjacent increment, hence monotonicity and the exact positivity test (4). Direct substitution gives the seven-species values. This completes the proof. \(\square\)

## Verification

Run `python3 verify.py` with Python 3 and the standard library. The independently enumerated survivor subsets validate (2) for all parameter choices with \(2\le n\le9\), every feasible \(k,a,b,c,r,s\). The checker additionally validates fixed marginal distributions, exact strictness values and the seven-species sign reversal. These finite checks **supplement** the preceding all-parameter combinatorial proof; they do not independently prove the infinite theorem.

## Relationship to prior work

Pocock, Evans and Memmott (2012) introduced empirical linked ecological networks and studied how their robustness covaries under species loss; their accessible accepted manuscript uses simulated removal sequences, not the exact arbitrary-quorum, finite-budget overlap ordering (1)–(2). Evans, Pocock and Memmott (2013) simulate random and selected habitat-removal permutations across linked networks; this is a distinct, applied network-robustness setting. Joag-Dev and Proschan (1983) describe negative association, which gives important background for disjoint sets under sampling without replacement but does not by itself provide the overlap increment and sharp transition in (2)–(4). Meyer and Strulovici (2015) characterize supermodular order abstractly using marginal-preserving four-point transfers; the present proof constructs the exact coefficients for this particular hypergeometric ecological model. No claim is made that the abstract ordering concept, hypergeometric marginals, or inclusion–exclusion themselves are new.

## Limitations

The model assumes uniformly sampled survivors of a **fixed total number**, identical partner effects, exact quorum viability, and no secondary feedback. In particular it does not imply an analogous conclusion for arbitrary correlated survival mechanisms or heterogeneous extinctions. The new content is the explicit all-parameter overlap comparison, strictness law and threshold association boundary for this model, rather than a claim about real ecosystem outcomes. Possible unindexed older results in sampling-without-replacement, multivariate hypergeometric dependence and reliability theory leave a genuine historical-priority risk. Independent scientific verification has not been performed.

## References

1. M. J. O. Pocock, D. M. Evans and J. Memmott, “The Robustness and Restoration of a Network of Ecological Networks,” *Science* **335** (2012), 973–977, https://doi.org/10.1126/science.1214915 ; accepted full text: https://nora.nerc.ac.uk/id/eprint/17964/1/N017964PP.pdf (first online 2012-02-23).
2. D. M. Evans, M. J. O. Pocock and J. Memmott, “The Robustness of a Network of Ecological Networks to Habitat Loss,” *Ecology Letters* **16** (2013), 844–852, https://doi.org/10.1111/ele.12117 ; accessible full text: https://nora.nerc.ac.uk/id/eprint/504615/1/N504615PP.pdf .
3. K. Joag-Dev and F. Proschan, “Negative Association of Random Variables, with Applications,” *Annals of Statistics* **11** (1983), 286–295, https://doi.org/10.1214/aos/1176346079 .
4. M. Meyer and B. Strulovici, “Beyond Correlation: Measuring Interdependence Through Complementarities,” public manuscript dated April 17, 2015, https://www.nuff.ox.ac.uk/Users/Meyer/ms17apr2015.pdf .
