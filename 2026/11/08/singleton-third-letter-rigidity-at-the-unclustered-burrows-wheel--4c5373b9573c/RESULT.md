# Singleton-third-letter rigidity at the unclustered Burrows–Wheeler boundary

## Finding

Fix the ordered alphabet \(0<1<2\). For each integer \(m\ge 2\), put \(n=2m+1\) and let \(\mathcal B_m\) consist of all length-\(n\) words \(L\) satisfying all four conditions:

1. \(L\) has exactly \(m\) copies of \(0\), \(m\) copies of \(1\), and one copy of \(2\);
2. consecutive letters of \(L\) are unequal;
3. its stable sorting permutation \(\pi_L\) is an \(n\)-cycle;
4. \(d_{\mathrm H}(L,0^m1^m2)=m+1\).

**Theorem.** For every integer \(m\ge2\),
\[
|\mathcal B_m|=
\begin{cases}
1,&\text{if }p=2m+1\text{ is prime and }2\text{ is a primitive root modulo }p,\\
0,&\text{otherwise.}
\end{cases}
\]
In the nonempty case its **unique** member is
\[
L=(10)^{m-1}120.
\]
In particular, the number is zero for every odd \(m\). The stated prime-root condition automatically entails \(p\equiv5\pmod8\).

A stronger rigidity statement holds before imposing either the distance condition or the one-cycle condition: for every \(m\ge2\), among *all* unclustered words with the specified content, exactly two have a stable sorting permutation without fixed points, namely
\[
A_m=(10)^{m-1}120,\qquad B_m=(10)^{m-2}10201.
\]
Their exact distances from \(0^m1^m2\) are respectively \(m+1\) and \(m+2\) if \(m\) is even, and \(m+2\) and \(m+3\) if \(m\) is odd.

Via the standard one-cycle criterion and the cyclic input-run identity for the Burrows–Wheeler transform, this gives a necessary-and-sufficient solution to the sharp unclustered input-run problem for the entire infinite family of fixed Parikh vectors \((m,m,1)\).

## Assumptions and scope

All indices are zero-based. The stable sorting permutation of a word \(L\) maps its \(i\)-th occurrence of letter \(a\) to the position of the same occurrence in the sorted word \(F=0^m1^m2\). Thus, writing \(c_a(i)\) for the number of occurrences of \(a\) strictly before index \(i\),
\[
\pi_L(i)=\begin{cases}
c_0(i),&L_i=0,\\
m+c_1(i),&L_i=1,\\
2m,&L_i=2.
\end{cases}
\]
A word is *unclustered* if its consecutive letters are all unequal (the comparison is linear, not cyclic). If \(\pi_L\) is a single cycle, \(L\) is the Burrows–Wheeler last column of a unique primitive necklace. In that case the necklace's cyclic input-run number equals \(d_{\mathrm H}(L,F)\); these standard identities are recalled in the cited primary literature.

No assumption about an unproved infinitude of Artin-type primes is used.

## Proof

**Step 1: fixed points.** If \(L_0=0\), then \(\pi_L(0)=0\). If \(L_{2m}=2\), then \(\pi_L(2m)=2m\). For a position \(i\) holding a \(1\), the formula above gives
\[
\pi_L(i)=i\quad\Longleftrightarrow\quad
\#\{j<i:L_j\in\{0,2\}\}=m.
\]
There are exactly \(m+1\) letters in \(\{0,2\}\). Since consecutive \(1\)'s are forbidden, this fixed point occurs precisely when a \(1\) separates the last two occurrences of letters in \(\{0,2\}\). Consequently a fixed-point-free unclustered word must start with \(1\) or \(2\), must not end in \(2\), and must have its last two non-\(1\) letters adjacent.

**Step 2: exhaustive symbolic classification.** Suppose first that \(L\) starts with \(2\). The remaining letters form an alternating binary word, because the sole \(2\) has been used. For \(m\ge2\), the last two zeros are separated by a \(1\), giving the fixed point from Step 1. Thus \(L\) must start in \(1\).

Remove the sole \(2\) to obtain a binary word \(D\) of length \(2m\), with \(m\) zeros and \(m\) ones. There is at most one equal-adjacent pair in \(D\), namely the pair exposed at the deleted \(2\).

If \(L\) ends in \(0\), then \(D\) starts in \(1\) and ends in \(0\). The number of equal-adjacent pairs in \(D\) is even, so it must be zero. Therefore \(D=(10)^m\). The last two zeros of this alternating word are separated by a \(1\). Making the last two letters from \(\{0,2\}\) adjacent while keeping \(2\) away from the final position forces insertion of \(2\) immediately before the final zero. Hence \(L=A_m\).

If \(L\) ends in \(1\), then \(D\) starts and ends in \(1\). There must be exactly one equal-adjacent pair. The prescribed equal counts make it a \(00\) pair (a single \(11\) pair instead creates \(m+1\) ones). The \(2\) must split this pair. To avoid the fixed point in Step 1, the split pair must be the last two zeros of \(D\), followed by its final \(1\). Therefore \(D=(10)^{m-2}1001\), and \(L=B_m\).

Both displayed words are unclustered, have the required content and have fixed-point-free stable permutations. This proves the two-word rigidity without assuming any particular length bound or computational enumeration.

**Step 3: exact distance.** Counting the agreements with \(F=0^m1^m2\) separately on the first \(m\) and next \(m\) positions gives
\[
\begin{array}{c|cc}
& m\text{ even}&m\text{ odd}\\\hline
 d_{\mathrm H}(A_m,F)&m+1&m+2\\
 d_{\mathrm H}(B_m,F)&m+2&m+3.
\end{array}
\]
The final position never matches the unique final \(2\). Thus a word satisfying the four conditions of the theorem must have even \(m\) and be exactly \(A_m\).

**Step 4: cycle criterion for arbitrary odd modulus.** Put \(p=2m+1\) (not yet assumed prime), and \(a=m+1\), so \(2a\equiv1\pmod p\). For \(A_m\), the stable permutation is explicitly
\[
\pi(2r)=m+r\quad(0\le r<m),\qquad
\pi(2r+1)=r\quad(0\le r<m-1),
\]
with \(\pi(2m-1)=2m\) and \(\pi(2m)=m-1\). Conjugate by \(\theta(i)=i+1\pmod p\). The resulting permutation of \(\mathbb Z/p\mathbb Z\) is
\[
T(y)=\begin{cases}
0,&y=-1,\\
m,&y=0,\\
ay\pmod p,&y\notin\{-1,0\}.
\end{cases}
\]
It is precisely multiplication by the invertible residue \(a\), with the edge \(-1\mapsto m\) replaced by \(-1\mapsto0\mapsto m\). Consequently \(T\) is one cycle on all \(p\) residues exactly when multiplication by \(a\) is one cycle on the \(p-1\) nonzero residues. This is possible only if all nonzero residues are units, hence if \(p\) is prime; then it is equivalent to \(a\), or equivalently \(2\), having multiplicative order \(p-1\). This supplies both necessity and sufficiency. Combining Steps 1–4 proves the theorem. \(\square\)

## Verification

The included self-contained `verify.py` reconstructs each stable permutation and checks both explicit candidate words and their distances for \(2\le m\le100\). It enumerates **all** words of the specified content with unequal consecutive letters for \(2\le m\le10\), independently comparing them with a decomposition obtained by deleting the unique \(2\). It checks the exact two-word fixed-point-free set for every parameter in both ranges, verifies the modular conjugacy at every position through \(m=100\), compares the cycle criterion to elementary primality and multiplicative-order tests, and reconstructs sorted cyclic rotations in four independent nontrivial one-cycle examples. A successful replay prints `BWT_SINGLETON_RIGIDITY_VERIFY_OK`.

The exhaustive checks are finite corroboration, not the reason the theorem holds for every \(m\). The proof of the unbounded statement is Steps 1–4 above.

## Relationship to prior work

Kumallagov, *An extremal problem for completely unclustered Burrows–Wheeler images* (arXiv:2606.01267v1), supplies the run/Hamming identity, a general Parikh-parity obstruction, the sufficient arithmetic construction \(A_m\), and explicitly asks in Problem 10.1 which fixed Parikh vectors admit sharp unclustered necklaces. Its Proposition 8.1 proves existence under the specified prime-root hypothesis, but does not establish necessity or uniqueness among all last columns of content \((m,m,1)\). The theorem here adds the complete two-word fixed-point-free classification and shows that the existing arithmetic hypothesis is both necessary and sufficient for sharpness **at this fixed content**. It does not assert necessity for other Parikh vectors or for unrestricted ternary lengths.

Fici, Gabory, Romana and Sciortino, *Unclustered BWTs of any Length over Non-Binary Alphabets* (arXiv:2508.20879v1), prove unrestricted ternary existence and primitive-root criteria for alternating BWT words; neither implies that every sharp balanced-singleton ternary image belongs to one explicit word. Prior finite sharpness/count profiles across bounded lengths do not establish this all-parameter fixed-content theorem.

## Limitations

The classification concerns the exactly balanced singleton content \((m,m,1)\) over the **ordered** ternary alphabet, with a linear unclustered last column and sharp cyclic input run number. Other contents can realize sharpness even when this particular content does not. The statement does not resolve the unrestricted all-length sharpness conjecture or show that qualifying primes occur infinitely often. Its priority assessment is subject to undiscovered equivalent results in the string-transformation literature; no independent validation is claimed.

## References

1. David Kumallagov, *An extremal problem for completely unclustered Burrows–Wheeler images*, arXiv:2606.01267v1 (first public submission 2026-05-31), especially Propositions 4.3, 8.1, 9.2 and Problem 10.1. https://arxiv.org/html/2606.01267v1
2. Gabriele Fici, Estéban Gabory, Giuseppe Romana, and Marinella Sciortino, *Unclustered BWTs of any Length over Non-Binary Alphabets*, arXiv:2508.20879v1 (first public submission 2025-08-28), especially the standard-cycle criterion and Theorem 19. https://arxiv.org/html/2508.20879v1
