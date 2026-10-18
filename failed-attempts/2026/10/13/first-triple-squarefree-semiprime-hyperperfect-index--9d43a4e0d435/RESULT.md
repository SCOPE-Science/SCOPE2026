# First triple squarefree-semiprime hyperperfect index
## Finding
For an integer
\[
k\ge1,
\]
let \(M(k)\) be the number of squarefree semiprimes
\[
pq,\qquad p<q,
\]
that are \(k\)-hyperperfect. Equivalently,
\[
pq=1+k(p+q).
\]

Then
\[
M(k)\le2
\]
for every
\[
1\le k<132,
\]
and equality occurs exactly for
\[
k=12
\quad\text{and}\quad
k=18.
\]

The first index with at least three squarefree-semiprime realizations is
\[
k=132,
\]
where
\[
M(132)=3.
\]
The three realizations are
\[
137\cdot3617=495529,
\]
\[
157\cdot829=130153,
\]
and
\[
173\cdot557=96361.
\]

Thus \(132\) is the first multiplicity-three layer in the squarefree-semiprime branch of the hyperperfect equation.

## Assumptions and scope
A positive integer \(n\) is \(k\)-hyperperfect when
\[
n=1+k\bigl(\sigma(n)-n-1\bigr),
\]
where \(\sigma(n)\) is the sum of the positive divisors of \(n\).

For a squarefree semiprime
\[
n=pq
\]
with distinct primes \(p<q\),
\[
\sigma(pq)-pq-1=p+q,
\]
so the condition becomes
\[
pq=1+k(p+q).
\tag{1}
\]

The theorem concerns only this squarefree-semiprime branch. Hyperperfect numbers with repeated prime factors or at least three distinct prime factors are outside its scope.

## Proof
Starting from (1),
\[
pq-kp-kq=1.
\]
Adding \(k^2\) gives the classical factorization
\[
(p-k)(q-k)=k^2+1.
\tag{2}
\]

The two factors on the left of (2) must be positive. Indeed, they have positive product. If both were negative, then
\[
(k-p)(k-q)<k^2,
\]
because \(p,q\ge2\), contradicting (2). Hence
\[
p>k,\qquad q>k.
\]

Put
\[
d=p-k,\qquad e=q-k.
\]
Then
\[
de=k^2+1,
\qquad
d<e.
\]
Since
\[
d^2<de=k^2+1,
\]
we have
\[
d<\sqrt{k^2+1}<k+1.
\]
As \(d\) is an integer,
\[
1\le d\le k.
\tag{3}
\]

Conversely, let \(d\) be a positive divisor of \(k^2+1\) satisfying (3), and put
\[
e=\frac{k^2+1}{d},
\]
\[
p=k+d,\qquad q=k+e.
\]
If \(p\) and \(q\) are prime and \(p<q\), then (2) holds, hence so does (1). Therefore
\[
M(k)
=
\#\left\{
d:
d\mid k^2+1,\ 
1\le d\le k,\ 
k+d\text{ prime},\
k+\frac{k^2+1}{d}\text{ prime},\
d<\frac{k^2+1}{d}
\right\}.
\tag{4}
\]

Formula (4) is a complete finite criterion for each \(k\).

The accompanying exact enumeration applies (4) for every
\[
1\le k\le132.
\]
The nonzero values are:
\[
\begin{array}{c|l}
k & (p,q)\\
\hline
1&(2,3)\\
2&(3,7)\\
6&(7,43)\\
12&(13,157),(17,41)\\
18&(23,83),(31,43)\\
30&(47,83)\\
48&(53,509)\\
60&(73,337)\\
66&(67,4423)\\
78&(79,6163)\\
108&(113,2441)\\
132&(137,3617),(157,829),(173,557)
\end{array}
\]
and all other \(k\) in this interval have \(M(k)=0\).

For the terminal layer, one can also see the three solutions directly. Since
\[
132^2+1=17425=5^2\cdot17\cdot41,
\]
the divisors at most \(132\) are
\[
1,5,17,25,41,85.
\]
They give the candidate smaller primes
\[
133,\ 137,\ 149,\ 157,\ 173,\ 217.
\]
Only \(137,157,173\) pair with prime complementary values:
\[
3617,\ 829,\ 557.
\]
The \(d=17\) candidate has complementary value
\[
1157=13\cdot89,
\]
while \(133\) and \(217\) are composite. Hence exactly three solutions occur at \(132\).

The exhaustive scan of (4) for the preceding \(131\) indices shows that only \(12\) and \(18\) attain multiplicity \(2\), and none attains multiplicity \(3\).

## Verification
The attached `verify.py` uses integer trial division only. For each
\[
1\le k\le132
\]
it examines every integer
\[
1\le d\le k
\]
dividing \(k^2+1\), constructs the two candidate primes from (4), tests primality exactly, and verifies the original hyperperfect identity
\[
pq=1+k(p+q).
\]

It asserts the complete nonzero spectrum displayed in the proof, verifies that the maximum below \(132\) is \(2\), that multiplicity \(2\) occurs there only at \(12\) and \(18\), and that the three \(132\)-solutions are exactly those stated.

The computation is finite and exhaustive because the factorization proof shows that every squarefree-semiprime solution corresponds to exactly one tested divisor \(d\). It is not a heuristic prime search.

## Relationship to prior work
The divisor factorization itself is not new. Te Riele's 1984 construction specializes, for the two-prime branch, to factoring
\[
1+k^2
\]
and obtaining primes by adding \(k\) to the two factors. McCranie's 2000 Theorem 2 gives the equivalent condition
\[
q=\frac{kp+1}{p-k}
\]
and a table of examples. That table already contains the three pairs at \(k=132\), as well as the two pairs at \(k=12\) and \(k=18\).

The new statement is the multiplicity cutoff: the cited tables are presented as examples and do not establish that no third squarefree-semiprime realization occurs for any smaller index. The finite criterion inherited from the classical factorization makes that comparison exhaustive.

OEIS A034913 and A034914 encode the prime-pair construction and computational divisor tests, but they are sequences of participating primes rather than the multiplicity function \(M(k)\). They therefore do not by themselves state or certify that \(132\) is the first index with three squarefree-semiprime realizations.

## Limitations
The theorem is intentionally restricted to squarefree semiprimes. It does not claim that \(132\) is the first index having three hyperperfect numbers of all possible factorization types; McCranie's tables explicitly discuss multiplicities among the broader hyperperfect population.

The factorization criterion is classical and is used here as prior structure, not claimed as a new lemma. The new finite claim is only the exact multiplicity spectrum through the first triple layer.

Te Riele's 1984 paper is older than the exact-date source stored in the metadata. Its inspected repository record verifies the year and the full paper was read, but no exact public calendar day was available there. To avoid inventing a day, the structured date uses the earliest exact public day verified among the inspected archival sources, McCranie's 21 January 2000 publication date.

## References
1. H. J. J. te Riele, “Rules for constructing hyperperfect numbers,” *Fibonacci Quarterly* 22(1) (1984), 50–60.
2. J. S. McCranie, “A Study of Hyperperfect Numbers,” *Journal of Integer Sequences* 3 (2000), Article 00.1.3.
3. OEIS Foundation, A034913, primes occurring as the smaller member in the squarefree-semiprime hyperperfect construction.
4. OEIS Foundation, A034914, primes occurring in the squarefree-semiprime hyperperfect construction.
