# Exponent-one endpoint monotonicity for arithmetic-progression anti-Waring thresholds
## Finding
Let \(n,r,s\) be positive integers, let \(|t|<s\) with \(\gcd(s,t)=1\), and put
\[
a_i=si+t,\qquad A=(a_i)_{i\ge1}.
\]
Whenever \(N(k,n,r,A)\) exists,
\[
N(k,n,r,A)\ge1-s+\sum_{i=n}^{n+r+s-2}a_i^k. \tag{1}
\]
Fuller and Nichols proved
\[
N(1,n,r,A)=1-s+\sum_{i=n}^{n+r+s-2}a_i. \tag{2}
\]
Hence, for every such \(k\),
\[
N(1,n,r,A)\le N(k,n,r,A).
\]

## Assumptions and scope
A positive integer is \((k,n,r,A)\)-good when it is a sum of \(k\)-th powers of at least \(r\) distinct members of \(a_n,a_{n+1},\ldots\). When it exists, \(N(k,n,r,A)\) is the least integer from which onward every integer is good.

The theorem assumes existence for \(k>1\). It does not prove the stronger adjacent-exponent inequality
\[
N(k,n,r,A)\le N(k+1,n,r,A).
\]

## Proof
Set
\[
h_0=r+s-1,\qquad M_k=\sum_{i=n}^{n+h_0-1}a_i^k.
\]
Because \(a_i\equiv t\pmod s\), every sum of exactly \(h\) distinct \(k\)-th powers is congruent to
\[
h\,t^k\pmod s.
\]
Since \(\gcd(t^k,s)=1\), a representation in the residue class \(h_0t^k\pmod s\) must use
\[
h\equiv h_0\pmod s.
\]
But
\[
h_0-s=r-1<r,
\]
so the least allowed summand count in that residue class is \(h_0\).

The progression is positive and strictly increasing. Therefore every good integer in this residue class is at least
\[
M_k.
\]
The integer \(M_k-s\) has the same residue. If it is positive, it is bad, and therefore
\[
N(k,n,r,A)\ge M_k-s+1.
\]
If \(M_k-s=0\), the same bound reduces to the automatic inequality \(N(k,n,r,A)\ge1\). This proves (1).

For \(k=1\), (2) is Theorem 8 of Fuller and Nichols. Since \(a_i\ge1\),
\[
M_k\ge M_1.
\]
Thus
\[
N(k,n,r,A)\ge M_k-s+1\ge M_1-s+1=N(1,n,r,A).
\]

## Verification
The attached checker tests all admissible tuples
\[
1\le s\le20,\quad1\le n,r\le12,\quad1\le k\le6,
\]
and all \(|t|<s\) with \(\gcd(s,t)=1\). It checks the summand-count residue obstruction, the obstruction residue, and \(M_k\ge M_1\) by exact integer arithmetic.

The computation is corroborative only; the proof is symbolic.

## Relationship to prior work
Fuller and Nichols define \(N(k,n,r,A)\), prove (2) for coprime arithmetic progressions, and state in their Future Work section that their data support
\[
N(k,n,r,A)\le N(k+1,n,r,A)
\]
but that they were unable to prove it. The present result does not settle the full adjacent-exponent question. It proves the complete exponent-one endpoint comparison for every exponent and gives the quantitative lower bound (1).

Looper and Saritzky later prove existence for tails of the natural numbers. Their theorem is about existence, not threshold comparison, and does not imply (1).

Targeted statement, notation, and semantic searches located no equivalent theorem.

## Limitations
The result compares higher exponents only with exponent one and assumes the higher threshold exists. It does not prove adjacent monotonicity for \(k\ge2\), nor does it extend automatically beyond one invertible residue class modulo \(s\). An equivalent elementary observation in unindexed notes remains a residual originality risk.

## References
1. C. Fuller and R. H. Nichols, Jr., “Generalized Anti-Waring Numbers,” *Journal of Integer Sequences* 18 (2015), Article 15.10.5, published 24 September 2015.
2. N. Looper and N. Saritzky, “An Anti-Waring Theorem,” *Journal of Combinatorial Mathematics and Combinatorial Computing* 99 (2016), 237–240.
