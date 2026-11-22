# Dyadic isometric doubling of every fixed binomial column

## Finding
Write \(B_m(x)=\binom{x}{m}=m!^{-1}\prod_{j=0}^{m-1}(x-j)\) for the integer-valued polynomial on \(\mathbb Z_2\). For **every** integer \(m\ge1\), put \(L=1+\lfloor\log_2m\rfloor\). For **each** \(\epsilon\in\{0,1\}\), there exists a bijective isometry \(\Phi_{m,\epsilon}:\mathbb Z_2\longrightarrow\mathbb Z_2\) such that
\[
\Phi_{m,\epsilon}(x)\equiv x\pmod{2^L},\qquad
\boxed{B_{2m}(2x+\epsilon)=B_m(\Phi_{m,\epsilon}(x))\quad(x\in\mathbb Z_2).}
\]
The isometries are constructed, rather than merely asserted, in the proof below.

In particular, if \(\mu\) is normalized additive Haar measure on \(\mathbb Z_2\), the two restrictions \(x\mapsto B_{2m}(2x)\) and \(x\mapsto B_{2m}(2x+1)\) have exactly the same pushforward \(2\)-adic measure as \(B_m\). Consequently the pushforward distribution of \(B_m\) depends only on the **odd part of \(m\)**: columns indexed by \(u,2u,4u,8u,\ldots\), for fixed odd \(u\), have identical complete \(2\)-adic output laws.

The assertion is stronger than an equality of valuation histograms. For every integer \(k\ge1\), every residue \(r\pmod{2^L}\), and every output \(y\pmod{2^k}\), the following three **exact** counts are equal:
\[
\begin{aligned}
&\#\{0\le t<2^k:B_m(r+2^Lt)\equiv y\pmod{2^k}\},\\
&\#\{0\le t<2^k:B_{2m}(2r+2^{L+1}t)\equiv y\pmod{2^k}\},\\
&\#\{0\le t<2^k:B_{2m}(2r+1+2^{L+1}t)\equiv y\pmod{2^k}\}.
\end{aligned}
\]
Thus the coincidence persists **within every prescribed input class** \(r\pmod{2^L}\), not merely after summing classes.

For illustration, the already known fifth-column law transfers verbatim to the tenth column: for \(k\ge3\), among \(0\le n<2^{k+4}\) the exact number with \(\binom n{10}\equiv y\pmod{2^k}\) is \(8+8\mathbf1_{2\mid y}+32\mathbf1_{8\mid y}\). This is the twice-as-long normalization of the same dyadic measure \(\tfrac12+\tfrac12\mathbf1_{2\mid y}+2\mathbf1_{8\mid y}\), not a separate novelty claim.

## Assumptions and scope
All integer column indices satisfy \(m\ge1\); all congruence exponents satisfy \(k\ge1\). The top variable ranges over \(\mathbb Z_2\), with its ordinary \(2\)-adic valuation \(\nu_2\) and the convention \(\nu_2(0)=+\infty\). For nonnegative top indices below the lower index, the binomial coefficient is zero. Integer-valued polynomials extend continuously to \(\mathbb Z_2\) because the nonnegative integers are dense and the polynomial is continuous into \(\mathbb Q_2\). The equality of distributions refers to Haar pushforwards, or equivalently all finite output residue counts; it is not a pointwise identity without a reparametrization. No analogous assertion for odd primes is made: for example, modulo nine the images of \(\binom n2\) and \(\binom n6\) are respectively \(\{0,1,3,6\}\) and \(\{0,1,3,6,7\}\), as can be checked exhaustively over a period of length 81.

## Proof
**1. A unique closest integral root in each binary input class.** Set \(a=\lfloor\log_2m\rfloor\) and \(L=a+1\), so \(2^a\le m<2^{a+1}\). Fix \(0\le r<2^L\). Among the roots \(0,1,\ldots,m-1\), at least one root is congruent to \(r\pmod{2^a}\), because the first \(2^a\) integers occur. At most two such roots occur, and if there are two, they differ by \(2^a\); exactly one is congruent to \(r\pmod{2^{a+1}}\). It follows that there is a unique index \(j_*\in\{0,\ldots,m-1\}\) maximizing \(\nu_2(r-j)\). Put \(e=\nu_2(r-j_*)\), allowing \(e=+\infty\) if \(r=j_*\). Then \(e\ge a\), and for every other root \(i\ne j_*\),
\[
\nu_2(r-i)<\min(e,L).
\]
Indeed, if \(e=a\), no other root can agree with \(r\) modulo \(2^a\); if \(e\ge a+1\), the other roots agree with \(r\) at most modulo \(2^a\).

**2. Every input class is a scaled isometric branch.** Define
\[
S_r=\sum_{\substack{0\le i<m\\i\ne j_*}}\nu_2(r-i),\qquad
d_r=L+S_r-\nu_2(m!).
\]
For distinct \(t,s\in\mathbb Z_2\), set \(x=r+2^Lt\) and \(z=r+2^Ls\). Consider the exact polynomial telescoping identity
\[
\frac{\prod_{i=0}^{m-1}(x-i)-\prod_{i=0}^{m-1}(z-i)}{x-z}
=\sum_{j=0}^{m-1}
\Bigl(\prod_{i<j}(x-i)\Bigr)
\Bigl(\prod_{i>j}(z-i)\Bigr).
\]
The summand at \(j=j_*\) has valuation exactly \(S_r\), since all its factors have valuation \(\nu_2(r-i)\) for \(i\ne j_*\), which are strictly less than \(L\). Every other summand contains the nearest-root factor \(x-j_*\) or \(z-j_*\), whose valuation is at least \(\min(e,L)\), instead of one factor associated with a root \(j\ne j_*\) whose valuation is strictly smaller. Such summands have valuation at least \(S_r+1\). Therefore the whole sum has valuation exactly \(S_r\), with no possible cancellation of its uniquely lowest-valuation term. Dividing by \(m!\) gives the exact identity
\[
\boxed{\nu_2(B_m(r+2^Lt)-B_m(r+2^Ls))=d_r+\nu_2(t-s).}
\]
Because the polynomial takes integral values on integers, this identity with \(s=0,t=1\) implies \(d_r\ge0\). After subtracting \(B_m(r)\) and dividing by \(2^{d_r}\), the map is an isometry \(\mathbb Z_2\to\mathbb Z_2\). Its reduction modulo every power of two is injective and therefore bijective; by completeness it is surjective. Thus the exact branch image is
\[
B_m(r+2^L\mathbb Z_2)=B_m(r)+2^{d_r}\mathbb Z_2,
\]
with a bijective scaled-isometry parameterization.

**3. The two doubled branches have the same scale.** For a fixed \(\epsilon\in\{0,1\}\), use lower index \(2m\), center \(r'=2r+\epsilon\), and input step \(2^{L+1}\). Its unique closest root is \(j'_* =2j_*+\epsilon\). There are \(m-1\) other roots of the same parity as \(\epsilon\), whose valuation contributions sum to \((m-1)+S_r\); the \(m\) opposite-parity roots contribute zero. Since \(\nu_2((2m)!)=m+\nu_2(m!)\), the depth of the doubled branch, by step 2, is
\[
(L+1)+(m-1+S_r)-\nu_2((2m)!)=d_r.
\]
Hence both doubled branches are bijective scaled isometries onto balls of radius \(2^{-d_r}\), centered respectively at \(B_{2m}(2r+\epsilon)\).

**4. The three image balls have the same center modulo their radius.** If \(r<m\), all three center values vanish: \(B_m(r)=B_{2m}(2r)=B_{2m}(2r+1)=0\). If \(r\ge m\), elementary factorial valuation gives
\[
\nu_2\!\left(B_{2m}(2r+\epsilon)\right)=\nu_2(B_m(r)),
\]
using \(\nu_2((2n+\epsilon)!)=n+\nu_2(n!)\) for \(\epsilon=0,1\). Meanwhile,
\[
\nu_2(B_m(r))=e+S_r-\nu_2(m!)=d_r+e-L\ge d_r-1.
\]
If this valuation is at least \(d_r\), every center is zero modulo \(2^{d_r}\). Otherwise it is exactly \(d_r-1\), in which case every center is congruent to \(2^{d_r-1}\pmod{2^{d_r}}\) because its unit factor is odd. Therefore
\[
B_m(r)+2^{d_r}\mathbb Z_2
=B_{2m}(2r)+2^{d_r}\mathbb Z_2
=B_{2m}(2r+1)+2^{d_r}\mathbb Z_2.
\]

**5. Construct the global isometries and deduce all exact counts.** On each input ball \(r+2^L\mathbb Z_2\), the maps
\[
t\mapsto B_m(r+2^Lt),\qquad
 t\mapsto B_{2m}(2r+\epsilon+2^{L+1}t)
\]
are bijective scaled isometries onto the **same** output ball, by steps 2–4. Invert the first map on that output ball and compose it with the second, obtaining a bijective isometry \(\psi_{r,\epsilon}:\mathbb Z_2\to\mathbb Z_2\). Define
\[
\Phi_{m,\epsilon}(r+2^Lt)=r+2^L\psi_{r,\epsilon}(t).
\]
Within an input ball this preserves every \(2\)-adic distance, and between different input balls the fixed residues \(r\pmod{2^L}\) preserve all distances as well. The resulting map is a global bijective isometry, preserves each prescribed input class, and satisfies the asserted polynomial identity. Isometries of \(\mathbb Z_2\) preserve normalized Haar measure, so the pushforward measures coincide. Reducing the maps modulo \(2^{L+k}\) shows that each of the three sequences in the finding has exactly the same finite multiset of output residues modulo \(2^k\) for every \(r\), because each \(\psi_{r,\epsilon}\) induces a permutation modulo \(2^k\). Iteration establishes dependence only on the odd part of \(m\).

## Verification
Run `python3 verify.py`. It uses exact integer arithmetic, not floating-point approximation, to test unique closest factors, depth separation, image-center congruences, and pairwise branch-distance identities for every \(m\) from 1 through 32. It exhaustively compares the three output histograms on every input residue ball for every \(1\le m\le24\), every \(1\le k\le6\), and tests the explicit fifth/tenth-column consequence through \(k=9\). Its 30,890 assertions are finite corroboration; the algebraic argument above proves the result for every positive \(m\) and \(k\).

## Relationship to prior work
Sun and Zhang's *Binomial coefficients and the ring of p-adic integers* (2008 arXiv posting; published 2011) studies complete prime-power residue images and proves density for many fixed lower columns, particularly the dyadic universal-image property. Those results do not assert equality of output-fiber distributions between **different** columns, nor the stronger input-class-preserving isometries here. Barat and Grabner's *Distribution of binomial coefficients and digital functions* (2001) analyzes joint row-and-column residue distributions across Pascal's triangle, not a fixed-column doubling conjugacy. Classical Lucas congruences control binomial coefficients modulo two and Kummer's theorem gives their valuations, but equality of valuations alone does not determine full unit residues modulo \(2^k\). A published exact fifth-column dyadic fiber formula and a sixth-column ternary image formula provide relevant special-case context without subsuming the universal binary doubling theorem. The new claim is the all-column isometric reparametrization and its all-depth, residue-classwise distribution identity; known surjectivity and valuation formulas are not claimed as new.

## Limitations
The theorem concerns the dyadic field and fixed binomial columns, not arbitrary primes or the joint **paired** distribution of \(B_m(x)\) and \(B_{2m}(2x+\epsilon)\) under the *same* input without reparametrization. It does not evaluate the common output-density formula for every odd lower index; it reduces those evaluations to the odd-index cases. The comparison with indexed and accessible published literature cannot exclude an unindexed implicit equivalent in general polynomial-image theory. Mathematical review of the proof is not an independent audit.

## References
- Z.-W. Sun and W. Zhang, *Binomial coefficients and the ring of p-adic integers*, arXiv:0812.3089 (initial public posting 2008-12-16), *Proc. Amer. Math. Soc.* **139** (2011), 1569–1577. https://arxiv.org/abs/0812.3089 ; full PDF https://arxiv.org/pdf/0812.3089 .
- G. Barat and P. J. Grabner, *Distribution of binomial coefficients and digital functions*, *J. London Math. Soc.* **64** (2001), 523–547. https://doi.org/10.1112/S0024610701002630 ; author-hosted PDF https://www.math.tugraz.at/~grabner/Publications/Binomial.pdf .
- *Exact three-level 2-adic fibers of the fifth binomial column*, published mathematical result: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-three-level-2-adic-fibers-of-the-fifth-binomial-column--68ab08bc975b .
- *Exact ternary residue images of the sixth binomial polynomial*, published mathematical result: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-ternary-residue-images-of-the-sixth-binomial-polynomial--2c5deda1b9d1 .
