# Odd-power Smith factors of a relative Hasse–Witt map in a Hermitian Artin–Schreier deformation

## Finding
For every odd prime \(p\), let \(S=\mathbb F_p[a]\), \(g=p(p-1)/2\), \(J=\lfloor(p+1)/4\rfloor\), and \(m_j=p+2-4j\) for \(1\le j\le J\). The smooth projective family with affine equation
\[
y^p-y=x^{p+1}+a x^2
\]
has a relative Hasse–Witt map \(F^*R^1\pi_*\mathcal O\longrightarrow R^1\pi_*\mathcal O\) whose Smith matrix over \(S\), in free bases, is
\[
\operatorname{diag}\left(aI_{m_1},a^3I_{m_2},\dots,a^{2J-1}I_{m_J},0_{g-R}\right),\qquad R=\frac{p^2-1}{8}.
\]
In particular,
\[
\operatorname{coker}(H)\simeq S^{g-R}\oplus\bigoplus_{j=1}^J\left(S/(a^{2j-1})\right)^{m_j}.
\]
If \(\nu_t\) is the sum of the \(t\) smallest elements of the multiset \(\{(2j-1)^{[m_j]}:1\le j\le J\}\), then every size-\(t\) minor ideal of \(H\) is \((a^{\nu_t})\) for \(1\le t\le R\); the higher minor ideals are zero. This is a scheme-theoretic determinantal statement on the *specified coefficient affine line*, not a claim about the coarse moduli quotient. For example, in characteristic seven the nonzero factors are five \(a\)'s and one \(a^3\), making the maximal nonzero minor ideal \((a^8)\).

## Assumptions and scope
The relative base is the affine coefficient scheme \(\operatorname{Spec} S\); all fibres are smooth, since \(\partial(y^p-y-x^{p+1}-ax^2)/\partial y=-1\) on the affine chart, and the unique point over infinity is smooth in the smooth projective model of the one-pole Artin–Schreier cover. The pole order \(p+1\) is prime to \(p\), so Riemann–Hurwitz gives genus \(g=p(p-1)/2\). The family is smooth proper after taking these standard projective models, and the Hodge bundles are locally free of constant rank \(g\). The claimed matrix is the **linearized relative Hasse–Witt** map, not a semilinear matrix treated incorrectly as an ordinary \(S\)-linear map. It is defined over the prime-field coefficient ring \(S\), and its Smith form persists after extension of constants.

## Proof
**1. An integral Hodge basis and Cartier formula.** Write \(f=x^{p+1}+ax^2\). The differential \(dx\) has divisor \((p(p-1)-2)P_\infty\), while \(x\) and \(y\) have pole orders \(p\) and \(p+1\), respectively. Consequently the \(g\) sections
\[
\omega_{i,j}=x^i y^j\,dx,\quad i,j\ge0,\quad i+j\le p-2
\]
form an \(S\)-basis of relative regular differentials. Indeed they are regular in all fibres, have pairwise distinct pole orders (since \(0\le j<p\)), and their number is the genus; relative base change makes them a basis.

For the Cartier operator, expand \(y^j=(y^p-f)^j\), and expand \(f^t\) by choosing \(s\) occurrences of \(ax^2\) and \(t-s\) of \(x^{p+1}\). The \(x\)-exponent is
\[
i+(p+1)(t-s)+2s=p(t-s)+(i+t+s).
\]
Since \(i+t+s\le 2p-4\), the Cartier residue condition is precisely \(i+t+s=p-1\). Thus, interpreting each coefficient after the appropriate \(p\)-th root as required for the Cartier-semilinear action,
\[
\mathcal C(\omega_{i,j})=
\sum_{\substack{0\le s\le t\le j\\i+t+s=p-1}}
\left((-1)^t\binom jt\binom ts\right)^{1/p}a^{s/p}x^{t-s}y^{j-t}\,dx.
\]
Dualizing and applying Frobenius to the coefficients produces the relative \(S\)-linear Hasse–Witt matrix, whose entries are the corresponding elements \((-1)^t\binom jt\binom ts a^s\). A transpose does not alter Smith factors.

**2. Constant direct-sum block decomposition.** If an input basis vector \(\omega_{i,j}\) contributes to output \(\omega_{r,h}\), then \(r=t-s\), \(h=j-t\), so
\[
i+2j=p-1+(r+2h).
\]
For each \(v=0,1,\ldots,p-3\), list the output rows by \(h=0,\ldots,\lfloor v/2\rfloor\), \(r=v-2h\), and the input columns by \(c=0,\ldots,M-\lceil v/2\rceil-1\), \(j=v+1+c\), \(i=p-3-v-2c\), where \(M=(p-1)/2\). All other input columns contribute zero. The \(v\)-block has \(R_v=\lfloor v/2\rfloor+1\) rows and \(C_v=M-\lceil v/2\rceil\) columns. The unique relevant pair of expansion indices is \(t=j-h\), \(s=1+h+c\), and its matrix entry is
\[
(-1)^{j-h}\frac{j!}{h!(v-2h)!(1+h+c)!}\,a^{1+h+c}.
\]
All factorials occurring in these fractions are less than \(p\), hence units in \(S\). Invertible constant row and column rescalings reduce the block to
\[
B_v(h,c)=\frac{a^{1+h+c}}{(1+h+c)!}.
\]

**3. Complete determinantal computation within each block.** Put \(k_v=\min(R_v,C_v)\). For any size-\(t\) minor, \(1\le t\le k_v\), its determinant contains the factor \(a^{t+\sum h_i+\sum c_i}\); distinct nonnegative row and column indices force \(\sum h_i+\sum c_i\ge t(t-1)\). Thus every such minor belongs to \((a^{t^2})\). The upper-left \(t\)-square minor has exactly this power, times the nonzero scalar
\[
\det\left[\frac1{(1+i+j)!}\right]_{0\le i,j<t}
=(-1)^{t(t-1)/2}\frac{\prod_{i=0}^{t-1}i!}{\prod_{i=0}^{t-1}(i+t)!}\ne0\pmod p.
\]
For completeness, multiply row \(i\) by \((i+t)!\). Its entry in column \(j\) becomes the falling-factorial polynomial \((i+t)!/(i+j+1)!\) of degree \(t-j-1\) in \(i\), with leading coefficient \(1\); reversing the columns gives a Vandermonde determinant on \(i=0,\ldots,t-1\), establishing the formula. Since \(2t-1<p\), no displayed factorial vanishes modulo \(p\). The order of the size-\(t\) determinantal ideal is therefore exactly \(t^2\), and the successive Smith valuations in this block are \(1,3,5,\ldots,2k_v-1\).

**4. Counting factors and reassembling.** The condition \(k_v\ge j\) is equivalent to \(2j-2\le v\le p-1-2j\), giving exactly \(p+2-4j\) blocks. Thus the exponent \(2j-1\) occurs \(m_j=p+2-4j\) times across all blocks. Every unit in the local Smith computations is an element of \(\mathbb F_p^\times\), so the splitting works over \(\mathbb F_p[a]\), not merely over its localization. The total nonzero rank is \(\sum_j m_j=(p^2-1)/8\). The asserted diagonal and minor ideals follow from the direct sum and Smith invariant-factor theorem for the PID \(S\). This proves the claim for every odd prime.

## Verification
The independently executable standard-library Python file `verify_hasse_witt.py` reconstructs all Cartier coefficients directly from the binomial expansion rather than hard-coding the predicted blocks. For primes \(3,5,7,11,13,17,19,23\), it compares the exact entries in every block, verifies nonvanishing leading Hankel determinants and their factorial formula, checks exponent multiplicities, and for the smaller primes computes specialized matrix ranks. Its last line is `VERIFY_OK`. These finite checks are corroboration only; the proof above is the universal argument. Running `python3 verify_hasse_witt.py` needs no additional packages.

## Relationship to prior work
Farnell–Pries (2012 preprint) study constant Cartier ranks under a pole-order congruence that does not apply to a pole of order \(p+1\). Pries–Weir (2013 preprint) determine Ekedahl–Oort information for the special Hermitian fibre, but not the coefficient-line Fitting orders. Bouw–Ho–Malmskog–Scheidler–Srinivasan–Vincent (2014 preprint) examine zeta functions and large automorphism groups of the broader \(y^p-y=xR(x)\) family. Most directly, Almeida Filho–Tafazolian–Vieira (2026 preprint), Corollary 8.5 and Theorem 8.4, prove the already-known generic rank \((p^2-1)/8\), vanishing rank at \(a=0\), and associated Cartier nilpotency; their Section 8 contains matrix block arguments. **Those pointwise ranks and the change in a-number are not claimed as new here.** The additional statement here is the exact order of *every* determinantal ideal, equivalently the entire \(S\)-torsion profile of the relative Frobenius cokernel. Pointwise ranks alone cannot distinguish \((a)\) from \((a^3)\), and therefore do not imply the displayed Smith classification. The most relevant 2026 full-text sections were examined; no Fitting/Smith-order classification was located there.

## Limitations
The Smith profile is specific to the displayed affine coefficient coordinate and does not assert an intrinsic multiplicity on the coarse moduli space, nor a classification for all additive polynomials \(R\). The result does not determine the full Ekedahl–Oort type of every fibre. The 2026 rank paper proves a substantial part of the surrounding story and is a close originality comparator; an equivalent unlocated calculation in its proofs or specialized literature remains a residual risk. A computational verification at finitely many primes cannot establish the universal theorem without the independent symbolic argument given above.

## References
1. S. Farnell and R. Pries, *Families of Artin–Schreier curves with Cartier–Manin matrix of constant rank* (first public preprint 2012-02-19), arXiv:1202.4183.
2. R. Pries and C. Weir, *The Ekedahl–Oort type of Jacobians of Hermitian curves* (first public preprint 2013-02-25), arXiv:1302.6261.
3. I. Bouw, W. Ho, B. Malmskog, R. Scheidler, P. Srinivasan and C. Vincent, *Zeta functions of a class of Artin–Schreier curves with many automorphisms* (first public preprint 2014-10-26), arXiv:1410.7031.
4. G. B. Almeida Filho, S. Tafazolian and S. C. Vieira, *a-Numbers, higher Cartier ranks and maximality of van der Geer–van der Vlugt curves* (first public preprint 2026-10-12), arXiv:2610.17476, especially Theorem 8.4 and Corollary 8.5.

