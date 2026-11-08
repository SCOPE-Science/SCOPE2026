# Complete bispecial factors and exact antidictionaries of binary four-run cycles

## Finding

Fix positive integers \(a,b,c,d\) and let \(X=(0^a1^b0^c1^d)^\omega\) be the infinite periodic word over the **binary** alphabet \(\{0,1\}\). A factor is a contiguous finite word, and a *minimal forbidden factor* (also called a minimal absent word) is absent from \(X\) although each of its proper contiguous factors occurs. Put
\[
A=\max(a,c),\quad B=\max(b,d),\quad u=\min(a,c),\quad v=\min(b,d),
\quad\delta_0=[a\ne c],\quad\delta_1=[b\ne d].
\]
Then the following three statements hold, **including all cases where run lengths coincide**.

1. The set of *bispecial factors* (factors having both symbols as left extensions and both as right extensions) is exactly the empty word, the words \(0^j\) for \(1\le j<A\), the words \(1^j\) for \(1\le j<B\), and the following additional mixed factors:
   - if \(a\ne c\) and \(b\ne d\): \(0^u1^v\) and \(1^v0^u\);
   - if \(a=c\) and \(b\ne d\): \(1^v0^a1^v\);
   - if \(a\ne c\) and \(b=d\): \(0^u1^b0^u\);
   - if \(a=c\) and \(b=d\): none.
2. The exact number of distinct minimal forbidden factors is
\[
\boxed{\#\operatorname{MAW}(X)=A+B+\delta_0+\delta_1.}
\]
3. Their maximum length \(\Lambda\) is
\[
\boxed{\Lambda=\begin{cases}
\max\{A+1,B+1,u+v+2\},&a\ne c,\ b\ne d,\\
\max\{A+1,B+1,a+2v+2\},&a=c,\ b\ne d,\\
\max\{A+1,B+1,2u+b+2\},&a\ne c,\ b=d,\\
\max\{A+1,B+1\},&a=c,\ b=d.
\end{cases}}
\]
All bounds are achieved by actual minimal forbidden factors. For instance, parameters \((a,b,c,d)=(2,3,4,5)\) give exactly \(11\) minimal forbidden factors with maximum length \(7\), whereas the repeated two-run cycle \((2,3,2,3)\) has exactly \(5\) and maximum length \(4\).

## Assumptions and scope

All run lengths are arbitrary positive integers; factors may cross period boundaries arbitrarily many times. The language is the set of all contiguous factors of the one-sided infinite periodic word (equivalently of all powers of its finite period). It is **not** the language of scattered subsequences, nor the factor language of only one finite copy. The alphabet is exactly binary, so there are no length-one absent symbols. The formulas depend on the specified four-run representation even when it has a smaller primitive period; the equal-pair case handles that situation without double counting.

## Proof

**Step 1: complete bispecial census.** A nonempty constant factor \(0^j\) is bispecial precisely when \(j<A\). If \(j<A\), the longer zero run provides extensions \(0\) on both sides, and zero-run boundaries provide extensions \(1\) on both sides. If \(j=A\), neither side permits another zero, and if \(j>A\) the factor is absent. The same argument gives \(1^j\) exactly when \(1\le j<B\). The empty word is bispecial because both letters occur.

Consider a factor with exactly one change of symbol. For \(0^i1^j\), a left extension \(1\) is possible only when \(i\) is an entire zero run, while a left extension \(0\) requires a strictly longer zero run at the same zero-to-one boundary. Thus both left extensions occur exactly when \(a\ne c\) and \(i=u\). Similarly both right extensions occur exactly when \(b\ne d\) and \(j=v\). The reversed factor \(1^j0^i\) satisfies the analogous conditions using the other two cyclic boundaries. Therefore the one-change bispecial factors, when they exist, are exactly the two words stated above.

A factor with exactly two changes has form \(0^i1^j0^h\) or \(1^i0^j1^h\). Its middle run is necessarily a complete run in the cycle. If the two available middle runs of that symbol have different lengths, an occurrence can use only one of them, fixing both extensions and precluding bispeciality. If the two middle-run lengths agree, the two occurrences have the same complete middle run but opposite order of the neighboring outer-run lengths. Both left and right extensions can vary simultaneously precisely when the two outer lengths differ and \(i=h\) equals their minimum. This gives \(0^u1^b0^u\) when \(a\ne c,b=d\), or \(1^v0^a1^v\) when \(a=c,b\ne d\).

Finally, a factor with three or more changes contains two successive *complete* internal runs. If \((a,b)\ne(c,d)\), their ordered symbols and lengths determine uniquely which of the four run slots they occupy, so all occurrences have the same immediate left and right symbols; it is not bispecial. If \((a,b)=(c,d)\), the word has the smaller two-run period \(0^a1^b\); already one complete interior run in a factor with two or more changes fixes all extensions. This proves the claimed exhaustive list.

**Step 2: counting missing extensions.** Write \(p_n\) for the number of distinct length-\(n\) factors, with \(p_0=1,p_1=2\). For each length-\(n\) factor \(w\), let \(L(w)\), \(R(w)\) be its sets of preceding and following letters, and let \(E(w)\) be the set of observed ordered pairs of letters surrounding \(w\). Every minimal forbidden factor of length \(n+2\) is uniquely \(xwy\) with \(x\in L(w)\), \(y\in R(w)\), and \((x,y)\notin E(w)\). Counting all such words gives
\[
M_{n+2}=\sum_{|w|=n}\bigl(|L(w)|\,|R(w)|-|E(w)|\bigr)
=2p_{n+1}-p_n-p_{n+2}+b_n,
\]
where \(b_n\) counts bispecial factors of length \(n\). The second equality uses \(|L|,|R|\in\{1,2\}\), hence \(|L||R|=|L|+|R|-1+[|L|=|R|=2]\), and the identities \(\sum|L|=\sum|R|=p_{n+1}\), \(\sum|E|=p_{n+2}\).

Because a periodic factor complexity eventually stabilizes, summing over all \(n\ge0\) telescopes to
\[
\sum_{n\ge0}M_{n+2}=p_1-p_0+\sum_{n\ge0}b_n
=1+\sum_{n\ge0}b_n.
\]
There are no length-one minimal forbidden factors. The census in Step 1 has \(1+(A-1)+(B-1)+\delta_0+\delta_1\) bispecial factors. The asserted count follows.

**Step 3: maximum length.** Every minimal forbidden factor of length at least two has a bispecial middle factor (delete its first and last symbols). Conversely, each listed mixed bispecial factor has exactly two distinct surrounding letter pairs, from the two relevant boundaries, leaving two missing pairs; it therefore gives minimal forbidden factors of length exactly its own length plus two. The unary patterns \(0^{A+1}\) and \(1^{B+1}\) are always minimal forbidden factors, giving lengths \(A+1\) and \(B+1\), even if \(A=1\) or \(B=1\). The exhaustive middle-factor census therefore makes the maximum equal to the largest of these lengths and the applicable mixed-core length plus two. This is exactly the displayed four-case formula.

## Verification

The standalone `verify.py` uses two independent finite constructions: it explicitly records surrounding letter pairs of cyclic factors to enumerate bispecial factors; separately, it builds actual circular factor sets and tests all one-symbol extensions of observed factors for minimal absence. It compares both independently constructed sets and statistics with the theorem. The checker passed all \(6^4=1296\) profiles with run lengths between one and six (including all \(36\) repeated two-run profiles), and a further \(200\) deterministic pseudorandom profiles with lengths up to forty. Run with `python3 verify.py`. These are finite reproducibility tests; the unbounded theorem is established by the proof above.

## Relationship to prior work

Fici, Restivo and Rizzo study minimal forbidden factors of circular words and prove general finiteness, automaton and upper-bound results; their full publicly available preprint focuses its explicit classifications on circular Fibonacci words, not the four-run binary family. Akagi et al. analyze minimal absent words of *finite* run-length-encoded inputs and provide general enumeration methods, rather than this closed-form cyclic four-run census. Charalampopoulos, Crochemore and Pissis connect finite-word absent factors with extended bispecial factors and give length-specific algorithms, but no four-run periodic formula was found in their inspected manuscript. The missing-extension counting identity is a standard type of factor-complexity argument; the contribution claimed here is the complete explicit bispecial census and its exact cardinality and longest-length consequences for this four-parameter family, not the existence of a general enumeration algorithm.

## Limitations

The result concerns only binary periodic words having at most two runs of each symbol in a period. No analogous formula is established for more run pairs, nonperiodic words, scattered subsequences, or finite unclosed factors. The literature comparison does not prove uniqueness of publication: differently phrased or unindexed equivalent formulas may exist. The included finite checks do not establish the infinite parameter claim on their own. No independent scientific audit has been conducted.

## References

- G. Fici, A. Restivo and L. Rizzo, *Minimal Forbidden Factors of Circular Words*, arXiv:1707.04450 (first posted 2017-07-14), https://arxiv.org/abs/1707.04450 .
- T. Akagi, K. Okabe, T. Mieno, Y. Nakashima and S. Inenaga, *Minimal Absent Words on Run-Length Encoded Strings*, arXiv:2202.13591 (first posted 2022-02-28), https://arxiv.org/abs/2202.13591 .
- P. Charalampopoulos, M. Crochemore and S. P. Pissis, *On Extended Special Factors of a Word*, SPIRE 2018, https://doi.org/10.1007/978-3-030-00479-8_11 .
