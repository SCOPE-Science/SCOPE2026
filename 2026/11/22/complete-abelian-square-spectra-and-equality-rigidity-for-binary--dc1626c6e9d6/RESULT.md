# Complete Abelian-square spectra and equality rigidity for binary two-cluster five-marker words

## Finding
Let \(a,c\geq0\), \(b\geq1\), and \(W=0^a11\,0^b111\,0^c\). Count distinct **literal contiguous factors** that are Abelian squares (the two equal-length halves have equal numbers of each letter), rather than occurrences or equivalence classes under Parikh vectors. Put \(M=\max(a,b,c)\), \(m=\min(a,b)\), and \(P_b(m)=|\{x\in\mathbb Z:0\leq x\leq m,\ x\equiv b\pmod2\}|\). Then

\[
\theta(W)=\left\lfloor\frac M2\right\rfloor+1+m+\mathbf1_{\{2\mid b\}}+P_b(m)+\mathbf1_{\{c\geq b\}}.
\]

For every length \(n\geq6\), among precisely this family of words of length \(n\), the sharp minimum is \(\lfloor(n+1)/4\rfloor\). Equality holds **if and only if** \(a=0\), \(b\) is odd, and either \(b-4\leq c<b\) or \(b=c\). There is one minimizing triple for each \(n\geq6\), except that there are two for \(n\equiv3\pmod4\), \(n\geq11\). The reversed family has the same classification by reversing words.

## Assumptions and scope
The alphabet is \(\{0,1\}\); the two runs of marked letters have lengths exactly two and three, separated by a positive zero-run. Outer zero-runs can be empty. No claim is made about all binary words with five ones or arbitrary run arrangements. All parameters and claims are exact, not asymptotic.

## Proof
Every Abelian square has an even number of ones, hence zero, two, or four. The squares with no ones are precisely \(0^{2j}\), for \(1\leq j\leq\lfloor M/2\rfloor\). The sole all-one square is `11`.

A two-one Abelian square lying in the first two-one cluster is necessarily \(0^x11\,0^x\) with \(1\leq x\leq m\), giving \(m\) additional distinct squares. The second cluster has three consecutive ones and cannot produce such a factor with positive flanking zero-runs. A two-one factor meeting both clusters necessarily consists of the last one of the first cluster, all \(b\) intervening zeros, and the first one of the second cluster. This is \(10^b1\) and is an Abelian square precisely when \(b\) is even (and \(b\geq1\), so it is distinct from `11`).

A four-one factor must take either two ones from each cluster or one from the first cluster and all three from the second. In the first case the possible factors are \(0^x11\,0^b11\), for \(0\leq x\leq a\). Their midpoint separates the two clusters exactly when \(x\leq b\), and integrality of that midpoint is exactly \(x\equiv b\pmod2\); this gives \(P_b(m)\) factors. In the second case the possible factors are \(10^b111\,0^z\). The midpoint must lie exactly between the first and second ones of the three-one cluster, forcing \(z=b\); the factor exists precisely when \(c\geq b\). The listed families are pairwise disjoint as literal words, except for `11`, which has already been counted once. This proves the formula.

For the minimum, write \(t=a+b+c=n-5\), \(K=\lfloor(t+6)/4\rfloor\). If \(m\geq1\), then \(t\leq2M+m\), \(P_b(m)\geq\lceil m/2\rceil\), and
\[
\theta(W)\geq\lfloor M/2\rfloor+1+m+\lceil m/2\rceil > (2M+m+6)/4\geq K.
\]
The strict middle inequality follows from \(\lfloor M/2\rfloor\geq M/2-1/2\), \(\lceil m/2\rceil\geq m/2\), and \(5m/4-1>0\). Since \(b\geq1\), the remaining case \(m=0\) forces \(a=0\). If \(b\) is even, the formula gives \(\theta=\lfloor M/2\rfloor+3+\mathbf1_{\{c\geq b\}}>K\). If \(b\) is odd and \(c>b\), then \(M=c\) and the strict inequality \(\theta=\lfloor c/2\rfloor+2>K\) follows by considering the parity of \(c\) and using that \(b<c\) is odd. If \(b=c\) is odd, direct substitution gives \(\theta=K\). Finally, if \(b\) is odd and \(c<b\), then \(M=b\), \(\theta=(b+1)/2\), and the integer equality \(\theta=\lfloor(b+c+6)/4\rfloor\) holds precisely when \(b-4\leq c<b\). At every \(n\geq6\) an admissible equality triple exists, by choosing the least odd \(b\) with \(b>(n-5)/2\), unless equality \(b=c\) provides the smaller choice. Solving \(b+c=n-5\) over these short intervals gives one minimizing triple, plus a second precisely when \(n\equiv3\pmod4\) and \(n\geq11\).

## Verification
The included independent literal-factor enumeration (`verify.py`) checks the formula for all 8,820 parameter triples with \(0\leq a,c\leq20\) and \(1\leq b\leq20\), and checks the predicted minimizing triples for each length \(6\leq n\leq300\). Results appear in `verify_output.txt`. The infinite quantifier follows from the proof, not these finite tests.

## Relationship to prior work
Fazekas, Mammoliti, Mercaş, and Simpson (2026) determine the unrestricted minimum for binary words with up to three occurrences of a given letter and give an effective four-run construction with specified composition (Theorem 12). For five ones their construction is an instance of the present family, but it does not provide this all-parameter literal square census or the complete equality classification within this two-cluster family. Related earlier results for four-one triple-plus-singleton words concern a different fixed-weight class and do not imply this five-one classification.

## Limitations
The minimization is over words with the exact run pattern \(0^a11\,0^b111\,0^c\), with \(b\geq1\), not over all five-one words. No unrestricted five-one conjecture is claimed. An unindexed equivalent enumeration or a more general theorem may exist; no independent mathematical validation has been performed.

## References
1. S. Z. Fazekas, A. Mammoliti, R. Mercaş, and J. Simpson, *Binary words containing few abelian squares*, first public 25 April 2026, arXiv:2604.23188v1, https://arxiv.org/html/2604.23188v1 (especially Theorems 7, 8, 12 and the discussion of unsolved fixed compositions).
2. G. Fici and S. Puzynina, *Abelian combinatorics on words: a survey*, Computer Science Review 47 (2023), 100532, as cited in reference 1.
3. *Abelian-square spectra and sharp minima for triple-plus-singleton binary words*, related fixed-four-one research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-abelian-square-spectra-and-sharp-minima-for-triple-plus-singleto--36a7f1823c0d (index summary; complete text not accessible during this comparison).
