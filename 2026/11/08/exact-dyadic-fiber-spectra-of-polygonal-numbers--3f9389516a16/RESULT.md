# Exact dyadic fiber spectra of polygonal numbers

## Finding

For an integer polygonal order \(s\ge3\), a positive integer \(k\), and \(m=2^k\), put
\[
P_s(n)=\frac{(s-2)n^2-(s-4)n}{2},\qquad
M_{s,k}(t)=\#\{0\le n<m:P_s(n)\equiv t\pmod m\}
\]
for \(0\le t<m\). The entire fiber law is as follows.

**Even orders \(s\equiv2\pmod4\).** Every fiber has size one:
\[
M_{s,k}(t)=1\qquad(0\le t<m).
\]

**Even orders \(s\equiv0\pmod4\).** Put \(u=(s-2)/2\), \(b=-(s-4)/4\), and \(\alpha\equiv bu^{-1}\pmod m\). Since \(u\) is odd,
\[
M_{s,k}(t)=N_k(u^{-1}t+\alpha^2),
\]
where arguments of \(N_k\) are reduced modulo \(m\), and \(N_k(w)\) counts square roots of \(w\) modulo \(m\). The following valuation formula makes this pointwise explicit. For \(w\equiv0\pmod m\),
\[
N_k(w)=2^{\lfloor k/2\rfloor}.
\]
Otherwise, take \(0\le v=\nu_2(w)<k\). If \(v\) is odd then \(N_k(w)=0\). If \(v=2j\), set \(h=k-2j\) and let \(z\equiv w/2^{2j}\pmod{2^h}\) be odd. Then
\[
N_k(w)=\begin{cases}
2^j,&h=1,\\
2^{j+1},&h=2\text{ and }z\equiv1\pmod4,\\
2^{j+2},&h\ge3\text{ and }z\equiv1\pmod8,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, the number of distinct polygonal residues is independent of the order within this class:
\[
\#\operatorname{Im}(P_s\mid_{[0,m)})
=Q_k=\begin{cases}
(2^{k-1}+4)/3,&k\text{ even},\\
(2^{k-1}+5)/3,&k\text{ odd}.
\end{cases}
\]

**Odd orders.** Let \(r\) be the unique odd integer with \(1\le r<m\) and \((s-2)r\equiv1\pmod m\). Put
\[
d=\min\{r-1,m+1-r\},\qquad c=2m+1-2r.
\]
The fiber sizes are only \(0,1,2\), with **exactly** \(d\) empty fibers, \(m-2d\) singleton fibers, and \(d\) double fibers. The complete collisions are the disjoint pairs
\[
\{n,c-n\}\quad\text{with}\quad0\le n<c-n<m;
\]
no other distinct inputs in \([0,m)\) collide. Consequently the image has exactly \(m-d\) residues.

Thus for \(k\ge2\), the map is a permutation precisely when \(s\equiv2\pmod4\) or \(s\) is odd and \(s\equiv3\pmod{2^k}\); for \(k=1\) every order gives a permutation. For odd \(s\) and \(k\ge2\), all nonempty fibers have size two precisely when \(s\equiv3+2^{k-1}\pmod{2^k}\).

## Assumptions and scope

Every order is an integer \(s\ge3\); \(k\ge1\). The index interval is exactly \(0\le n<2^k\), not an assumed period. This matters for odd orders: the natural congruence period may be \(2^{k+1}\). All counts refer to ordinary residue classes \(t\pmod{2^k}\), including zero. The inverse \(r\) in the odd case is defined modulo \(2^k\); no inverse modulo a larger modulus is needed to calculate the spectrum.

## Proof

Write \(a=s-2\) and \(b=s-4=a-2\). For all integers \(x,y\), the exact integer identity is
\[
2(P_s(x)-P_s(y))=(x-y)(a(x+y)-b).\tag{1}
\]

If \(s\equiv2\pmod4\), then \(P_s(n)=un^2+vn\) for even \(u=(s-2)/2\) and odd \(v=-(s-4)/2\). Hence
\[
P_s(x)-P_s(y)=(x-y)(u(x+y)+v),
\]
and the second factor is always odd. Therefore equal values modulo \(2^k\) imply \(x\equiv y\pmod{2^k}\), which proves bijectivity.

If \(s\equiv0\pmod4\), then \(u=(s-2)/2\) is odd and \(P_s(n)=un^2+2bn\), with \(b=-(s-4)/4\). Completing the square modulo \(2^k\) gives
\[
P_s(n)\equiv u(n+\alpha)^2-u\alpha^2\pmod{2^k},
\]
where \(\alpha\equiv bu^{-1}\). Translation of \(n\) and scaling of the output by the odd unit \(u\) prove the pointwise root formula. For \(w\not\equiv0\), a square root forces \(v=\nu_2(w)=2j\). Writing \(x=2^j y\) reduces the condition to \(y^2\equiv z\pmod{2^{k-2j}}\), with \(2^j\) lifts of each such odd root. Odd squares have one root modulo two, two roots modulo four if \(z\equiv1\pmod4\), and four roots modulo \(2^h\) for \(h\ge3\) exactly when \(z\equiv1\pmod8\). For \(w=0\), the condition is \(2^{\lceil k/2\rceil}\mid x\), yielding \(2^{\lfloor k/2\rfloor}\) roots. The number \(Q_k\) of distinct square residues has \(Q_1=Q_2=2\) and, for \(k\ge3\),
\[
Q_k=2^{k-3}+Q_{k-2},
\]
because the odd squares are exactly the \(2^{k-3}\) classes \(1\pmod8\), and the even squares correspond bijectively to the squares modulo \(2^{k-2}\) after division by four. Solving this recurrence gives the displayed image-size formula.

Suppose \(s\) is odd. In (1), for distinct \(x,y\in[0,m)\) of the **same parity**, \(a(x+y)-b\) is odd. Thus
\[
\nu_2(P_s(x)-P_s(y))=\nu_2(x-y)-1<k,
\]
so same-parity collisions are impossible. If \(x,y\) have opposite parities, then \(x-y\) is odd; (1) gives
\[
P_s(x)\equiv P_s(y)\pmod m
\iff a(x+y)\equiv b\pmod{2m}.\tag{2}
\]
Since \(a\) is odd and \(b=a-2\), the unique sum residue is \(c\equiv1-2a^{-1}\pmod{2m}\). Taking \(r\equiv a^{-1}\pmod m\) with \(1\le r<m\) gives the unique odd representative \(c=2m+1-2r\in[1,2m-1]\). Because \(0\le x+y\le2m-2\), congruence (2) is equivalent to the **integer equation** \(x+y=c\). Such a pair always has opposite parities because \(c\) is odd, and each input can have at most one distinct partner.

When \(c\le m-1\), there are \(c+1\) inputs with a partner, hence \((c+1)/2=m+1-r\) unordered pairs. When \(c\ge m-1\), there are \(2m-1-c\) such inputs and \((2m-1-c)/2=r-1\) unordered pairs. In both cases the pair count is \(d=\min(r-1,m+1-r)\). Every pair accounts for one double fiber and one missing output class relative to injectivity; all remaining \(m-2d\) input values yield singleton fibers, proving the spectrum.

For odd \(s\), \(d=0\) is equivalent to \(r=1\), or \(s-2\equiv1\pmod m\), hence \(s\equiv3\pmod m\). For \(k\ge2\), the maximum \(d=m/2\) occurs exactly when \(r=m/2+1\). This odd integer is its own inverse modulo \(m\), so the condition is \(s\equiv3+m/2\pmod m\). In the square-map class, \(Q_1=m=2\) but \(Q_k<m\) for all \(k\ge2\); these observations prove the remaining permutation and two-to-one characterizations.

## Verification

The standalone script `check_polygonal.py` enumerates all inputs, constructs independent residue multiplicities, compares every even-order fiber with the square-root formula, and checks odd-order predicted pairings and exact multiplicity histograms. It tested every \(3\le s\le140\) and \(1\le k\le9\), together with eleven additional order cases at \(k=12\): \(1253\) parameter pairs and \(186092\) inputs. It reported:

`VERIFY_OK parameter_pairs= 1253 input_residues= 186092 odd_pairing=exact even_square_fibers=exact permutation_and_double_cover=checked`

Finite checks are not a proof for unbounded \(s,k\); the proof above is algebraic.

## Relationship to prior work

Ulness (2022) studies triangular residues modulo arbitrary moduli and proves saturation one at powers of two. The triangular order \(s=3\) is the permutation special case here. The present claim of a new classification lies in the order-dependent odd-polygonal collision law and the uniform three-case spectrum, not in the already known triangular permutation case.

Dehnavi, Mirzaee Shamsabad, and Mahmoodi Rishakani (2019) classify root counts of general integral quadratic congruences modulo powers of two. Their square-root cases supply the classical local ingredient in the even-order part of this result and their quadratic solver can analyze any individual target. They do not state the simultaneous over-all-target spectrum for a half-period of an integer-valued polygonal polynomial; for odd \(s\) the equation after multiplication by two lives modulo \(2^{k+1}\), whereas this theorem selects only the first \(2^k\) inputs and counts its cross-parity collisions globally. The inverse-parameter formula for \(d\) and exact extreme-covering criterion require that additional comparison.

Bandyopadhyay and Baruah (2024) study representation counts for *sums* of generalized polygonal numbers, not individual dyadic residue fibers. The present theorem concerns a distinct distributional invariant; no additive Waring-type assertion follows.

## Limitations

The result concerns only prime-power moduli \(2^k\), one polygonal polynomial at a time, and the specified first block of indices. It does not classify all composite-modulus spectra, simultaneous distributions of several shapes, or additive representations by polygonal numbers. The square-root counts and conventional polynomial-permutation tests are classical; originality is claimed for the uniform order-wise fiber spectrum and the odd-order half-period pairing/census, not those ingredients. An unindexed equivalent theorem could remain unknown.

## References

1. D. J. Ulness, "Structure of Triangular Numbers Modulo m," *AppliedMath* 2 (2022), 326–358. DOI: 10.3390/appliedmath2030020. Public version dated 1 July 2022.
2. S. M. Dehnavi, M. R. Mirzaee Shamsabad, A. Mahmoodi Rishakani, "Complete solving the quadratic equation mod \(2^n\)," *Notes on Number Theory and Discrete Mathematics* 25 (2019), 75–83. DOI: 10.7546/nntdm.2019.25.1.75-83.
3. S. Bandyopadhyay, N. D. Baruah, "A Note on the Number of Representations of \(n\) as a Sum of Generalized Polygonal Numbers," arXiv:2409.02023v1 (3 September 2024).
4. R. L. Rivest, "Permutation Polynomials Modulo \(2^w\)," *Finite Fields and Their Applications* 7 (2001), 287–292. DOI: 10.1006/ffta.2000.0282.
