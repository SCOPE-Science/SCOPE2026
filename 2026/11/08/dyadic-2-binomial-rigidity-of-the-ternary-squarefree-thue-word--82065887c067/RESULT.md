# Dyadic 2-binomial rigidity of the ternary squarefree Thue word

## Finding

Let \(x=012021012102\cdots\) be the ternary Thue word, the infinite fixed point beginning with \(0\) of the morphism \(\theta(0)=012\), \(\theta(1)=02\), and \(\theta(2)=1\). Two finite words are *2-binomially equivalent* if the counts of all scattered subsequences of lengths one and two agree. Write \(b_{x,2}(n)\) for the number of such equivalence classes among length-\(n\) factors, and \(p_x(n)\) for their ordinary factor complexity.

**Theorem.** For every integer \(j\ge2\), putting \(n=2^j\),
\[
b_{x,2}(n)=p_x(n)=3n.
\]
More precisely, the \(3n\) factors \(x[i:i+n]\), \(0\le i<3n\), are distinguished by the four elementary statistics
\[
\bigl(N_1(w),M_1(w),N_0(w),M_0(w)\bigr),\quad
N_a(w)=\#\{r:w_r=a\},\quad
M_a(w)=\sum_{r=0}^{n-1}r\,\mathbf 1_{w_r=a}.
\]
Thus all distinct factors at these dyadic lengths have distinct 2-binomial signatures. This is a theorem about the *ternary squarefree* Thue word, not the binary Thue–Morse word or the uniform three-letter generalized Thue–Morse word.

## Assumptions and scope

The alphabet is \(\{0,1,2\}\); indices start at \(0\); factors are contiguous, but binomial equivalence uses scattered subsequences. All integers \(j\ge2\) are covered, with no finite-length cutoff. For a finite word \(w\), write \(\binom{w}{ab}\) for the number of pairs of positions \(r<s\) carrying the ordered letters \(a,b\). The first moments in the theorem are determined by the 2-binomial signature, since
\[
M_a(w)=\binom{N_a(w)}2+\sum_{b\ne a}\binom{w}{ba}.
\]
For \(n=2^j\), the previously known factor-complexity formula \(p_x(n)=p_t(n+1)=3n\), where \(t\) is the binary Thue–Morse word, is used as an upper bound. The proof below independently supplies \(3n\) distinct 2-binomial classes.

## Proof

**1. Binary transition realization and blocks.** Let \(t_i\in\{0,1\}\) be the parity of the number of ones in the binary expansion of \(i\). The standard transition encoding of \(x\) is
\[
x_i=\begin{cases}0,&(t_i,t_{i+1})=(0,1),\\2,&(t_i,t_{i+1})=(1,0),\\1,&t_i=t_{i+1}.
\end{cases}
\]
This encoding and its agreement with the above morphism are classical [3]. Fix \(n=2^j\), \(j\ge2\). For \(0\le k\le3\) and \(0\le r<n\), binary digit parity gives
\[
t_{kn+r}=t_k\oplus t_r,
\]
where \(\oplus\) is XOR. In particular, the internal equal-adjacency indicators within each binary block of length \(n\) coincide, independently of \(k\). Let \(h_j\) be the number of equal adjacent pairs among the first \(n\) bits \(t_0,\ldots,t_{n-1}\). Since \(t[0:2^j]\) is the concatenation of the preceding block and its complement,
\[
h_1=0,\qquad h_j=2h_{j-1}+\mathbf1_{j\text{ even}},
\]
so \(h_j=(n-1)/3\) for even \(j\), and \(h_j=(n-2)/3\) for odd \(j\).

Put \(W_i=x[i:i+n]\) and \(A_k=N_1(W_{kn})\) for \(k=0,1,2\). Across the three relevant binary block boundaries, \((t_k,t_{k+1})\) equals \((0,1),(1,1),(1,0)\), respectively. The last internal digit of any length-\(n\) binary block is \(t_k\oplus(j\bmod2)\). Consequently,
\[
A_0=A_2=\begin{cases}(n-1)/3,&j\text{ even},\\ (n+1)/3,&j\text{ odd},\end{cases}
\quad
A_1=\begin{cases}(n+2)/3,&j\text{ even},\\ (n-2)/3,&j\text{ odd}.\end{cases}
\]
Here \(A_0\) is odd and \(A_1\equiv2\pmod4\). For any \(r<n\), the 1-indicator word of \(W_{kn+r}\) is the cyclic rotation by \(r\) of the 1-indicator word of \(W_{kn}\): the first \(n-1\) transition indicators repeat across consecutive blocks, and the shifted window never includes the new block's terminal boundary. In particular,
\[
N_1(W_{kn+r})=A_k,
\qquad M_1(W_{kn+r})\equiv M_1(W_{kn})-rA_k\pmod n.\tag{1}
\]
(The congruence follows by moving each of the \(A_k\) occupied positions left by \(r\) modulo \(n\).)

**2. The first and third groups.** The group \(W_0,\ldots,W_{n-1}\) and group \(W_{2n},\ldots,W_{3n-1}\) have odd \(N_1\); the middle group has even \(N_1\), so the middle group is disjoint from both. For either outside group, \(A_0=A_2\) is odd and \(n\) is a power of two. Equation (1) therefore distinguishes all \(n\) offsets \(r\) within either outside group by \(M_1\pmod n\).

Because \(t_{2n+s}=1-t_s\) for \(0\le s<2n\), the word \(W_{2n+r}\) is obtained from \(W_r\) by interchanging letters \(0\) and \(2\), for every \(0\le r<n\). Thus their \(N_1\) and \(M_1\) coincide. By the telescoping identity for the transition encoding,
\[
N_0(W_r)-N_2(W_r)=t_{r+n}-t_r=1-2t_r\in\{-1,1\}.
\]
The interchange therefore changes \(N_0\). Hence no two factors from different outside groups have the same four-statistic fingerprint: (1) first forces their offsets to be equal, and then \(N_0\) separates them.

**3. The middle group.** Here \(A_1\equiv2\pmod4\), so \(\gcd(A_1,n)=2\). Equation (1) distinguishes the offsets in the middle group except for possible pairs \(r,r+n/2\), with \(0\le r<n/2\). The length-\(n\) blocks \(x[n:2n]\) and \(x[2n:3n]\) have identical first \(n-1\) letters, because \(t_1=t_2=1\) and their internal binary transition patterns agree. Thus each \(W_{n+r}\), \(r<n\), is a cyclic rotation by \(r\) of \(W_n\), and the two potentially conflicting factors are half-turn rotations of each other.

The telescoping identity now gives \(N_0(W_n)=N_2(W_n)\), since \(t_n=t_{2n}=1\). Therefore their common zero count is
\[
C=N_0(W_n)=(n-A_1)/2,
\]
which is odd because \(n\equiv0\pmod4\) and \(A_1\equiv2\pmod4\). For any word of length \(n\) with \(C\) zeros and \(Z\) zeros in its first half, rotating by \(n/2\) changes its zero-position sum by
\[
M_0(\operatorname{rot}_{n/2}w)-M_0(w)
=\tfrac n2(2Z-C)\ne0.\tag{2}
\]
Thus the possible middle-group collisions are separated by \(M_0\).

The three groups jointly provide \(3n\) pairwise distinct four-statistic fingerprints, and each fingerprint is recoverable from the 2-binomial signature. Hence \(b_{x,2}(n)\ge3n\). Finally the classical binary Thue–Morse complexity formula and transition-factor bijection give \(p_x(n)=p_t(n+1)=3n\) at \(n=2^j\), \(j\ge2\) [3]. Because \(b_{x,2}(n)\le p_x(n)\), equality follows. \(\square\)

## Verification

Run the standalone Python 3 file `verify.py` with `python3 verify.py`; it requires only the Python standard library. It independently compares the binary-transition and ternary-morphism constructions, computes full scattered-subsequence signatures of lengths one and two, checks the four-statistic distinguishing property, and verifies every stated group invariant for \(j=2,3,\ldots,10\) (dyadic lengths \(4\) through \(1024\)). The observed class totals are \(12,24,48,96,192,384,768,1536,3072\), ending with `VERIFY_OK`. These are diagnostics, not an infinite proof; the all-length conclusion is established by the three-part argument above together with the established ordinary factor-complexity theorem.

## Relationship to prior work

Rigo and Salimov [1] define binomial complexity and prove bounded binomial complexity for the *binary* Thue–Morse word; the ternary squarefree transition word is not their object. Shallit and Shur [3] identify the ternary transition encoding and establish the ordinary factor-complexity identity used above; their subject is contiguous factor complexity, rather than scattered-subsequence equivalence. Lejeune, Rigo and Rosenfeld [4] prove full 2-binomial/factor-complexity equality for the *Tribonacci* fixed point, whose generating morphism differs from \(\theta\). Golafshan, Rigo and Whiteland [5] study the *uniform* generalized Thue–Morse substitutions, not this nonuniform squarefree morphism. Rao, Rigo and Salimov [2] address avoidance of binomial powers, not exact binomial factor complexity in this word. None of these inspected primary sources states the claimed dyadic 2-binomial rigidity for \(x\); absence in the inspected literature is not a universal priority proof.

## Limitations

The formula is established at dyadic lengths \(n=2^j\) with \(j\ge2\); it does not classify \(b_{x,2}(n)\) at other lengths and does not imply full complexity equality there. The theorem distinguishes *literal factors*, not rotational classes, and concerns scattered subsequences of length at most two. Priority beyond the specific inspected sources remains subject to unindexed or inaccessible work. Independent mathematical validation has not been performed.

## References

1. M. Rigo and P. Salimov, *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words*, WORDS 2013, available since 27 May 2013, https://orbi.uliege.be/handle/2268/149313 (full author preprint and longer version inspected).
2. M. Rao, M. Rigo and P. Salimov, *Avoiding 2-binomial squares and cubes*, arXiv:1310.4743, https://arxiv.org/abs/1310.4743 (full accessible preprint inspected).
3. J. Shallit and A. Shur, *Subword complexity and power avoidance*, arXiv:1801.05376, https://arxiv.org/abs/1801.05376 (formula (2), Section 3.1 and the ternary transition coding inspected).
4. M. Lejeune, M. Rigo and M. Rosenfeld, *Templates for the k-binomial complexity of the Tribonacci word*, WORDS 2019, https://orbi.uliege.be/handle/2268/240049 (full author preprint inspected).
5. M. Golafshan, M. Rigo and M. A. Whiteland, *Computing the k-binomial complexity of generalized Thue–Morse words*, arXiv:2412.18425, https://arxiv.org/abs/2412.18425 (full preprint inspected for substitution and theorem scope).
