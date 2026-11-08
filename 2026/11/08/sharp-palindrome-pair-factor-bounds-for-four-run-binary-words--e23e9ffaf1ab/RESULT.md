# Sharp palindrome-pair factor bounds for four-run binary words

## Finding
A *palindrome pair* is a word of the form \(PQ\), where \(P,Q\) are palindromes and either may be empty. A *factor* is a contiguous subword, including the empty factor. Write \(F(w)\) for the number of **distinct** factors of a binary word \(w\) that are palindrome pairs; positions are not counted with multiplicity.

**Theorem.** For every integer \(n\ge1\), every binary length-\(n\) word with at most four maximal constant-symbol runs satisfies
\[
F(w)\le H(n):=1+\left\lfloor\frac{(n+1)^2}{3}\right\rfloor
=\left\lceil\frac{n^2+2n+3}{3}\right\rceil.
\]
For every \(n\) this bound is attained by a word with at most three runs. In contrast, among words having **exactly four** runs, the sharp maximum is
\[
M_4(n)=\begin{cases}8,12,16,21&\text{respectively for }n=4,5,6,7,\\
\left\lfloor(n^2+n+10)/3\right\rfloor&n\ge8.
\end{cases}
\]
In particular no four-run word is a global maximizer of the displayed bound. For every \(n\ge8\), all four-run maximizers, up to swapping the two alphabet symbols, are precisely
\[
0^a1^b0^c1^d,\quad a,b,c,d\in\mathbb Z_{>0},\quad a+b+c+d=n,
\]
with \(a<c\), \(b>d\), at least one of \(a,d\) equal to \(1\), and the three integers \(a+d+2,b,c\) differing pairwise by at most one.

## Assumptions and scope
Words are linear and binary; each run has positive integer length. Distinct factors include the empty word. Reversal, bit-complement and positional occurrence are not quotiented in \(F\). A binary word with four runs can be written uniquely after a possible bit-complement as \(0^a1^b0^c1^d\). The result imposes a run bound; it does not assert the corresponding bound for arbitrary binary words with five or more runs.

## Proof
We give an explicit count followed by a complete four-case optimization. The elementary identity
\[
\max_{x+y+z=t\atop x,y,z\in\mathbb Z_{>0}}(xy+xz+yz)=\left\lfloor t^2/3\right\rfloor
\]
follows by replacing any two positive entries differing by at least two by their nearest pair, preserving their sum and strictly increasing the sum of products. Equality is attained exactly when the entries differ by at most one.

A factor of a binary word having at most three runs is always a palindrome pair: a one-run factor is a palindrome, a two-run factor is the product of its one-run palindromes, and a three-run factor of shape \(0^i1^j0^k\) splits as \(0^{i-k}(0^k1^j0^k)\) when \(i\ge k\), or symmetrically at the other end when \(k>i\). For a three-run host \(0^a1^b0^c\), reverse it if necessary to suppose \(a\ge c\). Its distinct factors consist of the empty word, \(a\) zero-only words, \(b\) one-only words, \(ab+bc\) distinct two-run words, and \(ac\) distinct three-run words. Hence
\[
F(0^a1^b0^c)=1+a+b+ab+bc+ac
=1+XY+XZ+YZ
\]
where \(X=a\), \(Y=b\), \(Z=c+1\), summing to \(n+1\). Thus \(F\le H(n)\). Balancing \(X,Y,Z\) with \(X\ge Z-1\) yields equality for every \(n\ge3\); for \(n=1,2\) a one- or two-run word attains \(H(n)\). A two-run host has \(F=1+n+ab\le1+n+\lfloor n^2/4\rfloor\le H(n)\), as the real-valued difference between \((n+1)^2/3\) and \(n+n^2/4\) is \((n-2)^2/12\). The one-run case is immediate.

Now put \(w=0^a1^b0^c1^d\). The number of distinct zero-only factors is \(\max(a,c)\) and of one-only factors \(\max(b,d)\). The counts of two-run factors of shape \(01\) and \(10\) are respectively \(ab+cd-\min(a,c)\min(b,d)\) and \(bc\). The counts of three-run factors of shape \(010\) and \(101\) are \(ac\) and \(bd\). A four-run factor is \(0^i1^b0^c1^j\) with \(1\le i\le a\) and \(1\le j\le d\). Since a palindrome can span at most three runs, such a factor is a palindrome pair if and only if the first three runs form a palindrome (\(i=c\)) or the last three form a palindrome (\(j=b\)). The number of these is
\[
q=d\mathbf1_{c\le a}+a\mathbf1_{b\le d}
-\mathbf1_{c\le a,\,b\le d}.
\]
Therefore the **exact** factor count is
\[
\begin{split}
F(w)= {}&1+\max(a,c)+\max(b,d)+ab+cd-\min(a,c)\min(b,d)\\
&+bc+ac+bd+q. \tag{1}
\end{split}
\]

We partition all positive quadruples into four disjoint cases. If \(a\ge c,b>d\) (case I), direct simplification of (1) gives
\[
F=ab+ac+a+bc+bd+b+d+1.
\]
For \(d>1\), replace \((a,d)\) by \((a+1,d-1)\); the case inequalities persist, and \(F\) increases by exactly \(c\). So an upper bound is obtained at \(d=1\). Then set \((X,Y,Z)=(a,c+1,b-1)\), which has sum \(n-1\), and expand to obtain
\[
F=\frac{n^2+5-(X^2+Y^2+Z^2)}2\le\frac{n^2+n+7}{3},
\]
using \(X^2+Y^2+Z^2\ge(n-1)^2/3\). Here \(Z\ge1\) because \(b>d=1\).

If \(a\ge c,b\le d\) (case II), (1) reduces to \(F=(a+d)(b+c+2)\). With \(x=a+d\), this is \(x(n-x+2)\le(n+2)^2/4\le(n^2+n+7)/3\), the last inequality being \((n-4)^2\ge0\) after multiplying by 12. If \(a<c,b\le d\) (case IV), reverse the word and interchange symbols: this maps to case I (with tuple \((d,c,b,a)\)), preserving \(F\), so the case-I upper bound applies.

Finally if \(a<c,b>d\) (case III), set \(X=a+d+2,Y=b,Z=c\), all positive, with \(X+Y+Z=n+2\). Expanding (1) gives the exact identity
\[
F=XY+XZ+YZ-n+2-(a-1)(d-1). \tag{2}
\]
Thus
\[
F\le\left\lfloor(n+2)^2/3\right\rfloor-n+2
=\left\lfloor(n^2+n+10)/3\right\rfloor.
\]
Equality holds **exactly** when \((a-1)(d-1)=0\) and \(X,Y,Z\) are balanced. Cases I, II and IV cannot attain it, because their integer upper bound is \(\lfloor(n^2+n+7)/3\rfloor\), one lower. For each \(n\ge8\), choose \(a=1\), \(X=\lceil(n+2)/3\rceil\), \(d=X-3\), and take \(b,c\) as the two remaining balanced parts of \(n+2\); all strict inequalities \(a<c,b>d\) hold. This proves sharpness and every equality case for \(n\ge8\). For \(n=4,5,6,7\), substituting every positive four-composition into (1) yields respectively \(8,12,16,21\); the accompanying verifier performs this finite enumeration. Each is below \(H(n)\); for \(n\ge8\), the displayed formulas likewise give \(M_4(n)<H(n)\). QED.

## Verification
The standalone file `verify.py` directly constructs distinct palindrome-pair factors for all binary run compositions with at most four runs and lengths 1 through 14, independently checks (1), verifies the global bound and its attainability, then exhaustively checks the formula and complete equality classification for all 395010 four-run compositions of lengths 4 through 57. Running `python verify.py` produces `VERIFY_OK direct_words=1470 run_quadruples=395010 extremizers=223 range_n=1..57`. The unrestricted quantifiers rest on the algebraic proof, not on finite checks.

## Relationship to prior work
Borchert and Rampersad formulated the unrestricted binary maximum \(\lceil(n^2+2n+3)/3\rceil\) as a conjecture, gave candidate examples, and noted that every binary word with at most three runs is itself a palindrome pair [1]. The present theorem establishes that proposed factor bound throughout the bounded-run class and solves the exact **four-run** optimization and all its extremizers; it does not settle the unrestricted conjecture. Guo, Shallit and Shur treat characterization and enumeration of palindrome-pair words rather than maximizing the number of distinct palindrome-pair factors inside an ambient host word [2].

## Limitations
The statement is restricted to binary linear words with at most four constant-letter runs. Nothing is claimed for unrestricted or circular words, other alphabets, or factors counted with positional multiplicity. A specialist publication not located by the searches may contain an equivalent result; the proof establishes correctness but cannot establish historical priority. Computational checks are finite, while infinite validity follows from the explicit identities and inequality argument.

## References
[1] J. Borchert and N. Rampersad, *Words with many palindrome pair factors*, arXiv:1509.05396, initial public version September 17, 2015, https://arxiv.org/abs/1509.05396 .

[2] C. Guo, J. Shallit and A. Shur, *On the combinatorics of palindromic pairs*, arXiv:1503.09112, first submitted March 31, 2015, https://arxiv.org/abs/1503.09112 .
