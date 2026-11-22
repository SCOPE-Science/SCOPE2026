# Parity bifurcation at the first post-Apéry representation threshold for consecutive coin triples

## Finding
For each integer \(a\ge3\), put \(p=\lfloor a/2\rfloor+1\) and
\[
d_a(n)=\#\{(x,y,z)\in\mathbb Z_{\ge0}^3: ax+(a+1)y+(a+2)z=n\}.
\]
The complete finite set \(G_a=\{n\in\mathbb Z_{\ge0}:d_a(n)\le p\}\) has the following exact description:
\[
G_a=\begin{cases}
\{0,1,\ldots,a(a+1)-1\},&a\text{ odd},\\
\{0,1,\ldots,a(a+1)-1\}\ \cup\ \{a(a+1)+2j+1:0\le j<a/2\},&a\text{ even}.
\end{cases}
\]
Consequently the gap set is a single interval for odd \(a\), but for even \(a\) has that initial interval followed by exactly \(a/2\) isolated singleton components. The numbers of gaps are respectively \(a(a+1)\) and \(a(a+1)+a/2\). The maximum gap agrees with the previously known generalized Frobenius threshold; the complete topology and gap census at this first post-Apéry level are the present claim.

## Assumptions and scope
All indices and coin multiplicities are nonnegative integers; the triple is ordered by the three fixed denominations \(a,a+1,a+2\). The representation threshold is precisely \(p=\lfloor a/2\rfloor+1\), for every integer \(a\ge3\). A gap means an integer with at most \(p\) representations (including zero); this differs from an ordinary nonrepresentable semigroup gap. A component means a maximal nonempty interval of consecutive gaps.

## Proof
Write \(n=aq+s\) uniquely with \(q\ge0\) and \(0\le s<a\). A representation with \(k=x+y+z\) total coins has \(y+2z=n-ak\). For an integer \(u\), its number of solutions with exactly \(k\) coins is
\[
c_k(u)=\begin{cases}\lfloor u/2\rfloor-\max(0,u-k)+1,&0\le u\le2k,\\0,&\text{otherwise}.\end{cases}
\]
In particular \(d_a(aq+s)=\sum_{t=0}^q c_{q-t}(s+at)\). If \(q\le a+1\), every term with \(t\ge2\) vanishes, since \(s+2a>2(q-2)\); thus only \(t=0,1\) are possible.

First suppose \(q\le a\). If the \(t=1\) contribution vanishes, then \(d_a(aq+s)=c_q(s)\le\lfloor s/2\rfloor+1\le\lceil a/2\rceil\le p\). If that contribution is nonzero, the condition \(a+s\le2(q-1)\) implies \(s\le q\); moreover \(a+s\ge q-1\). Direct substitution gives
\[
d_a(aq+s)=\lfloor s/2\rfloor+1+q-\lceil(a+s)/2\rceil
=\begin{cases}q-m,&a=2m+1,\\q-m+1-(s\bmod2),&a=2m.\end{cases}
\]
Both quantities are at most \(p=m+1\) when \(q\le a\). This proves that every \(n<a(a+1)\) lies in \(G_a\).

Next put \(q=a+1\). Every remainder \(0\le s<a\) has both contributions nonzero, since \(a+s\le2a\) and \(s\le q\), so the same displayed identity applies. For odd \(a=2m+1\), it gives \(d_a(a(a+1)+s)=m+2>p\) for every remainder. For even \(a=2m\), it gives \(m+2\) at even remainders and \(m+1=p\) at odd remainders. Hence the claimed isolated gaps are exactly the odd-remainder positions in this block.

Finally all subsequent integers have more than \(p\) representations. For odd \(a\), appending an \(a\)-coin injects the representations of \(n\) into those of \(n+a\), so the preceding full above-threshold block propagates forever. For even \(a=2m\), examine the next block \(q=a+2\). If \(1\le s<a\), only \(t=0,1\) contribute, and their sum equals \(m+3-(s\bmod2)>p\). At \(s=0\), the contributions at \(t=0,1,2\) are respectively \(1,m+1,1\), so the total is \(m+3>p\). This full block lies above threshold and propagates to all later blocks by the same injection. There are no additional gaps. The disjoint component and cardinality statements follow immediately. \(\square\)

## Verification
The standalone standard-library program `verify.py` constructs all representation counts independently by a three-coin generating-function dynamic program for every \(3\le a\le160\), and checks the full predicted gap set beyond the last gap. It also cross-checks the dynamic program with direct coefficient-vector enumeration for \(3\le a\le21\), and prints `PASS` on success. This finite verification supplements but does not replace the quantified proof.

## Relationship to prior work
Komatsu and Ying [1, Theorem 1 and Section 3] determine explicit generalized Frobenius, genus and full Apéry data only for \(0\le p\le\lfloor a/2\rfloor\); their first successor is exactly the regime studied here and not supplied by their Apéry formula. A subsequent result [2] determines the largest \(p\)-gap through \(p=2a\), including the endpoint claimed here, but does not classify all \(p\)-gaps or their connected components. Subwattanachai [3, Theorem 1] concerns generalized Frobenius values under a divisibility assumption not satisfied by three successive generators; it does not give their post-threshold gap set. The novelty is the complete set and parity-dependent component structure, not the already known last-gap formula. Search and direct literature comparison cannot exclude an unindexed equivalent statement.

## Limitations
This theorem does not classify any other threshold \(p\) or an arbitrary arithmetic step. It does not assert originality of the Frobenius maximum, general counting formula, or known lower-level Apéry tables. It has not received an independent mathematical audit.

## References
[1] T. Komatsu and H. Ying, *The p-numerical semigroup of the triple of arithmetic progressions*, arXiv:2206.13052 (first public 2022-06-27), published in *Symmetry* 15 (2023), article 1328, https://www.mdpi.com/2073-8994/15/7/1328.

[2] *Three exact phases of generalized Frobenius numbers for three consecutive denominations*, published mathematical research record, https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-three-exact-phases-of-generalized-frobenius-numbers-for-three-co--6dc430dbb315/RESULT.md.

[3] K. Subwattanachai, *Generalized Frobenius Number of Three Variables*, arXiv:2309.09149 (first public 2023-09-17), https://arxiv.org/abs/2309.09149.
