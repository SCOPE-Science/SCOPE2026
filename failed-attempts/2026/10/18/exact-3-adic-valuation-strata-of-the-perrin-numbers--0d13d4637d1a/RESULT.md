# Exact 3-adic valuation strata of the Perrin numbers

## Finding

Let \(R_0=3\), \(R_1=0\), \(R_2=2\), and \(R_{n+3}=R_{n+1}+R_n\) for all integers \(n\ge0\). Put \(\nu_3(0)=\infty\). There exist unique 3-adic integers \(\alpha_1,\alpha_3,\alpha_9\), with \(\alpha_1=0\), such that for every \(t\ge0\):

\[
\nu_3(R_{13t+a})=\begin{cases}
1+\nu_3(t-\alpha_a),&a\in\{1,3,9\},\\
1,&a=0,\\
0,&a\in\{2,4,5,6,7,8,10,11,12\}.
\end{cases}
\]

For \(a\in\{1,3,9\}\), each \(\alpha_a\) is uniquely specified as the 3-adic zero of \(t\mapsto R_{13t+a}/3\), interpreted by the binomial interpolation below. For every integer \(k\ge1\), its companion transition matrix has exact order \(13\cdot3^{k-1}\) modulo \(3^k\), giving a period of the scalar sequence. Over that period the number of zeros is exactly \(4\) for \(k=1\) and exactly \(3\) for every \(k\ge2\).

Consequently the exact natural density of indices of valuation \(0\) is \(9/13\), of valuation \(1\) is \(3/13\), and of each valuation \(k\ge2\) is \(6/(13\cdot3^k)\). These density statements concern nonnegative integers and are unaffected by the isolated zero term \(R_1=0\).

## Assumptions and scope

All indices are nonnegative integers. The valuation is normalized by \(\nu_3(3)=1\). A 3-adic root \(\alpha_a\) need not be an ordinary nonnegative integer; the identity uses the valuation on \(\mathbb Z_3\). In the root branch \(a=1,t=0\), both sides equal \(\infty\).

## Proof

Set
\[
M=\begin{pmatrix}0&1&0\\0&0&1\\1&1&0\end{pmatrix},\quad
v=\begin{pmatrix}3\\0\\2\end{pmatrix},\quad e=(1,0,0).
\]
Then \(R_n=eM^nv\). Exact integer multiplication gives
\[
M^{13}=\begin{pmatrix}7&12&9\\9&16&12\\12&21&16\end{pmatrix}
=I+3B,\quad
B=\begin{pmatrix}2&4&3\\3&5&4\\4&7&5\end{pmatrix}.
\]
The residues \((R_0,\ldots,R_{12})\pmod3\) are
\((0,0,2,0,2,2,2,1,1,0,2,1,2)\).
Since \(M^{13}\equiv I\pmod3\), these residues repeat with period \(13\), and the zero branches are precisely \(a\in\{0,1,3,9\}\).

For each such branch set \(w_a=M^av\), and define a continuous function on \(\mathbb Z_3\) by the uniformly convergent series
\[
F_a(t)=\frac{e(I+3B)^tw_a}{3}
=\frac{R_a}{3}+\sum_{j\ge1}3^{j-1}\binom tj eB^jw_a.
\]
For ordinary nonnegative \(t\) the series is finite and \(F_a(t)=R_{13t+a}/3\). All terms lie in \(\mathbb Z_3\). Write \(b_a=eBw_a\). Exact multiplication yields
\[
(b_0,b_1,b_3,b_9)=(12,17,29,158),\quad
(R_0,R_1,R_3,R_9)=(3,0,3,12).
\]
For \(j\ge2\), the scalar \(3^{j-1}/j!\) belongs to \(3\mathbb Z_3\), because \(\nu_3(j!)\le(j-1)/2\). The difference of the two integer polynomials \(t(t-1)\cdots(t-j+1)\) evaluated at \(t,s\) is divisible by \(t-s\) over \(\mathbb Z_3\). The corresponding series converges uniformly, even after division by \(3(t-s)\). Hence the terms with \(j\ge2\) form \(3H_a(t)\), where \(H_a:\mathbb Z_3\to\mathbb Z_3\) is 1-Lipschitz. In particular,
\[
F_a(t)=R_a/3+b_at+3H_a(t).
\]
When \(a=0\), \(R_a/3\equiv1\pmod3\) and \(b_0\equiv0\pmod3\); thus \(F_0(t)\equiv1\pmod3\) and \(\nu_3(R_{13t})=1\).

For \(a\in\{1,3,9\}\), one has \(b_a\equiv2\pmod3\) and therefore, for distinct \(s,t\in\mathbb Z_3\),
\[
\nu_3(F_a(t)-F_a(s))=\nu_3(t-s).
\]
Moreover \(F_a\pmod3\) is the affine bijection \(t\mapsto R_a/3+2t\). It follows inductively that \(F_a\) bijects each residue ring \(\mathbb Z/3^j\mathbb Z\) with itself and hence is a bijective 3-adic isometry. Let \(\alpha_a\) be its unique zero. Then
\(\nu_3(F_a(t))=\nu_3(t-\alpha_a)\), which proves the valuation formula. Because \(R_1=0\), \(\alpha_1=0\).

The matrix \(M\pmod3\) has order \(13\): its thirteenth power is the identity, but \(M\ne I\pmod3\) and \(13\) is prime. Also \(B\not\equiv0\pmod3\), and for every \(j\ge0\) the binomial identity gives
\[
(I+3B)^{3^j}\equiv I+3^{j+1}B\pmod{3^{j+2}}.
\]
Thus the exact order of \(M\) modulo \(3^k\) is \(13\cdot3^{k-1}\). Each of the three bijective branches contributes one zero modulo \(3^k\) per \(3^{k-1}\) choices of \(t\) for \(k\ge2\); the branch \(a=0\) contributes none. At \(k=1\), all four base zeros occur. The period counts follow.

Finally, the natural density of the class \(13t+a\) is \(1/13\). The branch \(a=0\) always has valuation \(1\). In each of the other three branches, an isometry gives the Haar probabilities \(\Pr(\nu_3(t-\alpha)=0)=2/3\) and \(\Pr(\nu_3(t-\alpha)=j)=2/3^{j+1}\) for \(j\ge1\). Hence the valuation-zero density is \(9/13\), the valuation-one density is \(1/13+3(2/3)/13=3/13\), and the valuation-\(k\) density for each \(k\ge2\) is \(3(2/3^k)/13=6/(13\cdot3^k)\).

## Verification

The standalone `verify_perrin3.py` uses exact integer matrix multiplication and the recurrence, checks \(M^{13}=I+3B\), all thirteen base residues, the four slope values, the number and branch types of zeros through modulus \(3^5\), the unique root in each specified branch through the fourth lifting stage, and independent recurrence/matrix agreement for the first 200 terms. Run `python3 verify_perrin3.py`; expected output begins `VERIFY_OK`. These finite checks support, but do not replace, the all-exponent proof above.

## Relationship to prior work

Perrin's sequence is classical; the OEIS A001608 entry records it and prior congruence and period questions. Rihane and Togbé (2021, Lemma 2.2) quote Irmak's complete **2-adic** valuation classification for Perrin numbers; that statement does not assert the 3-adic fibre count here. Antony and Barman (2024) study general p-adic valuation conjectures for third-order recurrences but their publicly accessible abstract does not state this explicit Perrin classification. The present result concerns the fully explicit 3-adic residue-stratum theorem and its natural-density law, not the general idea of 3-adic analytic interpolation.

## Limitations

This result describes only prime \(3\) for the Perrin sequence, not all primes or all third-order recurrences. It does not give conventional integer closed forms for the two nonzero 3-adic roots. The historic Adams--Shanks article and the full text of the later general third-order paper were not materially accessible for complete implication comparisons, so residual priority risk remains. Independent validation is not claimed.

## References

1. OEIS A001608, *Perrin sequence*, including dated sequence commentary and references, https://oeis.org/A001608 .
2. W. Adams and D. Shanks, *Strong primality tests that are not sufficient*, Mathematics of Computation 39 (1982), 255--300, DOI:10.1090/S0025-5718-1982-0658231-9.
3. S. E. Rihane and A. Togbé, *Repdigits as products of consecutive Padovan or Perrin numbers*, Arabian Journal of Mathematics 10 (2021), 469--480, https://doi.org/10.1007/s40065-021-00317-1 , especially Lemma 2.2.
4. D. Antony and R. Barman, *On the p-adic valuation of third order linear recurrence sequences*, arXiv:2402.18279 (2024), https://arxiv.org/abs/2402.18279 .
