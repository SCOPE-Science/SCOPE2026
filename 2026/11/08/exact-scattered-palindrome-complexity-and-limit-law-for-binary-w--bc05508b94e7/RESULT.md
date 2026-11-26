# Limit law for scattered palindrome counts in binary words with three ones

## Finding

For $n\ge3$, let $W_n$ be uniform among the length-$n$ binary words with exactly three ones, and let $P(w)$ count the distinct nonempty palindromic subsequences of $w$. Write $(A,B,C,D)$ for a uniform simplex vector ($\mathrm{Dirichlet}(1,1,1,1)$), $R=\min(A,D)$, and define
\[
\Phi(A,B,C,D)=R\big(B+C+\min(B,C)\big)+
\begin{cases}\min(B,D-A)C,& A\le D,\\\min(C,A-D)B,& A>D.\end{cases}
\]
Then $P(W_n)/n^2\xrightarrow{\mathrm d}\Phi(A,B,C,D)$, with convergence of its first and second raw moments. The limit has mean $7/80$, second raw moment $289/30240$, and variance $2299/1209600>0$.

## Assumptions and scope

Subsequences preserve order but need not be contiguous. Identical spelled words count only once. The empty subsequence is excluded. Every triple of one-positions has equal probability; this is not an iid bit model. No assumptions on the joint coupling of the words at different lengths are needed.

## Proof

**A known gap formula.** For $w=0^a1\,0^b1\,0^c1\,0^d$ set $z=a+b+c+d$, $r=\min(a,d)$, $s=\min(b,c)$ and
\[
T=\max\{\min(a,b+c+d),\min(a+b,c+d),\min(a+b+c,d)\},\quad
E=\begin{cases}\min(b,d-a)(c+1),&a\le d,\\\min(c,a-d)(b+1),&a>d.\end{cases}
\]
The earlier three-one gap theorem [1] gives, after subtracting the empty word,
\[
P(w)=z+T+1+(r+1)(b+c+1)+E+(r+1)(s+1).
\]
This counts respectively the four possible numbers of ones in the subsequence, with the middle two-one count obtained by taking the union of three rectangles. The finite identity, including zero-length gaps, is prior input, not a new enumeration.

**Passage to the limit.** The gaps of $W_n$ are uniformly distributed over the nonnegative integer compositions of $n-3$ into four parts. The vector of gaps divided by $n$ converges to uniform measure on the simplex by lattice Riemann sums in three independent coordinates. The homogeneous degree-two part of the known formula is exactly $\Phi$; every term of lower degree is uniformly $O(n)$. The function is continuous, including at equality of the two outside gaps, where its two case terms are both zero. Consequently $P(W_n)/n^2$ converges in distribution to the claimed functional, with uniform boundedness giving convergence of the two raw moments.

**Moments.** Let $U_1,\ldots,U_4$ be independent rate-one exponentials, and $S=\sum_i U_i$. The normalized vector is independent of $S$ and uniform on the simplex. Put $G=S^2\Phi(U_1/S,\ldots,U_4/S)$. Let $M=\min(U_1,U_4)$, $X=|U_1-U_4|$, $B=U_2$, $C=U_3$. The minimum and difference are independent, of rates two and one respectively and independent of $B,C$. By symmetry of the two orientations, $G$ has the distribution of $MH+J$, with $H=B+C+\min(B,C)$ and $J=C\min(B,X)$.

In particular $\mathbb EM=\mathbb EM^2=1/2$. Writing $H$ as three times a rate-two exponential plus an independent rate-one exponential gives $\mathbb EH=5/2$ and $\mathbb EH^2=19/2$. The minimum of $B,X$ is rate two and is independent of $C$, so $\mathbb EJ=1/2$ and $\mathbb EJ^2=1$. For the mixed term, $\mathbb E[\min(B,X)\mid B]=1-e^{-B}$. Thus
\[
\mathbb E[HJ]=\frac34+1+\frac34-\mathbb E[e^{-B}C\min(B,C)]=\frac{41}{18}.
\]
Here the two contributions to the subtracted expectation from $B\le C$ and $B>C$ are $5/27$ and $1/27$: the minimum is rate two, the independent difference is rate one, and either order has probability $1/2$. The displayed moments give $\mathbb EG=7/4$ and $\mathbb EG^2=289/36$. Since $S$ is Gamma$(4,1)$, division by $\mathbb ES^2=20$ and $\mathbb ES^4=840$ gives the mean and second moment. Subtracting the squared mean gives the stated positive variance.

## Verification

The bundled `verify.py` checks the known gap identity against distinct-subsequence enumeration for all 3,876 weight-three words with $3\le n\le18$ and evaluates the rational exponential-integral moment identities. Run `python3 verify.py`. The finite enumeration is a check of conventions and arithmetic, not a proof of the limit law.

## Relationship to prior work

The exact deterministic gap formula is already in [1] (counting also the empty palindrome). The finding here is the conditional limit law and its exact moments. Holub and Saari [2] reconstruct a word up to reversal from its full scattered-palindrome set. The alphabet-dependent Fibonacci-type bound and extremal results of Mahalingam and Pandoh [3] do not give the random fixed-weight law. Rubinchik and Shur [4] instead count contiguous factors under uniform iid letters.

## Limitations

This is the binary, exactly-three-ones model. The limit is specified as a pushforward, not by a density. The result gives neither an unconditioned iid law nor formulas for other weights.

## References

1. *A closed palindromic-subsequence count for three-one binary words*, Resultary, October 25, 2026 UTC, https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-a-closed-palindromic-subsequence-count-for-three-one-binary-word--3fb9dc585778/RESULT.md .
2. Š. Holub and K. Saari, *On highly palindromic words*, https://doi.org/10.1016/j.dam.2008.03.039 .
3. K. Mahalingam and P. Pandoh, *Counting Scattered Palindromes in a Finite Word*, https://arxiv.org/abs/2108.02729 .
4. M. Rubinchik and A. M. Shur, *The Number of Distinct Subpalindromes in Random Words*, https://arxiv.org/abs/1505.08043 .
