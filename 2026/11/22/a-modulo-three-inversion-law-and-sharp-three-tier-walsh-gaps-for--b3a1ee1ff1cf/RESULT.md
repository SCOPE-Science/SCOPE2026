# A modulo-three inversion law and sharp three-tier Walsh gaps for prism dimers

## Finding

Let \(G_n=C_n\square K_2\) be the simple prism graph with \(n\ge3\), having \(3n\) labelled edges. Let \(p_n\) indicate the edge-incidence vectors of its perfect matchings on \(H_n=(\mathbb Z/2\mathbb Z)^{E(G_n)}\). The unnormalized counting-convolution operator \(T_n h=p_n*h\) satisfies

\[
T_n\text{ is invertible}\quad\Longleftrightarrow\quad 3\nmid n.
\]

Write \(\sigma_{\min}^{+}(T_n)\) for its least strictly positive singular value on \(\ell^2(H_n)\), with counting-measure convention. Then

\[
\sigma_{\min}^{+}(T_n)=
\begin{cases}
1,&3\nmid n,\\
2,&n\equiv3\pmod6,\\
4,&n\equiv0\pmod6.
\end{cases}
\]

Writing \(L_0=2\), \(L_1=1\), and \(L_j=L_{j-1}+L_{j-2}\) for Lucas numbers, the largest singular value equals \(L_n+2\mathbf1_{2\mid n}\). Thus the sharp \(\ell^2\) condition number on the nonzero Fourier subspace is \((L_n+2\mathbf1_{2\mid n})/\sigma_{\min}^{+}(T_n)\). Every Fourier multiplier is given explicitly below, without any spectral multiplicity assertion.

## Assumptions and scope

Index columns cyclically by \(i\in\mathbb Z/n\mathbb Z\). Label each vertical edge \(r_i\), each upper horizontal edge \(a_i\), and each lower horizontal edge \(b_i\), with horizontal edges joining columns \(i\) and \(i+1\). For a Walsh character, let \(x_i,u_i,v_i\in\{-1,1\}\) denote its signs on these three edge types. The multiplier is \(W_n(x,u,v)=\sum_{M\text{ perfect matching}}\prod_{e\in M}\varepsilon_e\). These are the eigenvalues of \(T_n\); their absolute values are its singular values. No normalization by the size of the group or by the number of matchings is applied.

## Proof

**1. Exact weighted decomposition.** Every perfect matching containing a vertical edge is encoded uniquely by a set of pairwise nonadjacent edges of the column cycle. Selecting a cycle edge \(i\) uses both horizontal edges \(a_i,b_i\), and every uncovered column uses its vertical edge. The same description includes the two horizontal tilings with a common alternating offset when \(n\) is even. If \(n\) is even, there are exactly two additional matchings: the two rows are covered by horizontal edges with opposite alternating offsets. No such matchings exist at odd \(n\). This classification can also be obtained by following the boundary of a block between consecutive vertical edges.

Define \(y_i=u_iv_ix_ix_{i+1}\) and \(B(t)=\begin{pmatrix}1&t\\1&0\end{pmatrix}\). The signed cycle matching polynomial is \(\operatorname{tr}(B(y_1)\cdots B(y_n))\): the trace counts circular binary choices with no adjacent chosen edges and weight \(\prod_{i\text{ chosen}}y_i\). Therefore the **exact multiplier formula** is

\[
W_n=(\prod_{i=1}^n x_i)\operatorname{tr}\left(\prod_{i=1}^nB(y_i)\right)+\mathbf1_{2\mid n}(U+V),
\]

where, for even \(n\),
\[
U=\prod_{i\text{ even}}u_i\prod_{i\text{ odd}}v_i,
\qquad V=\prod_{i\text{ odd}}u_i\prod_{i\text{ even}}v_i.
\]

The identities \(UV=\prod_i y_i\) and \(U,V\in\{-1,1\}\) imply \(U+V=0\) if \(\prod_i y_i=-1\), while \(U+V\in\{-2,2\}\) otherwise.

**2. Parity obstruction and explicit zero.** Evaluating all signs at \(+1\), the number of matchings is \(N_n=L_n+2\mathbf1_{2\mid n}\). Lucas numbers satisfy \(L_n\equiv0\pmod2\) exactly when \(3\mid n\), by the recurrence and its three-period reduction modulo two. If \(3\nmid n\), \(N_n\) is odd; since every signed Walsh sum is congruent to \(N_n\) modulo two, none can vanish.

If \(n=3k\), take \(x_i=u_i=1\) for every \(i\), take \(v_3=1\), and take \(v_i=-1\) for every \(i\ne3\). Then \(y_1=y_2=-1\), \(y_3=1\), and all remaining \(y_i=-1\). Direct multiplication yields \(B(-1)^3=-I\) and \(\operatorname{tr}(B(-1)^2B(1))=0\). Thus the first term of the multiplier vanishes for every multiple of three. If \(n\) is even, \(\prod_i y_i=-1\), so also \(U+V=0\). This is an explicit zero frequency for every \(3\mid n\).

**3. Sharp nonzero gap away from multiples of three.** The oddness in Step 2 bounds the least nonzero absolute multiplier below by one. Set \(x_i=1\) and \(y_i=-1\) for all columns. The matrix \(B(-1)\) has eigenvalues \(e^{\pm i\pi/3}\); consequently \(\operatorname{tr}(B(-1)^n)=2\cos(n\pi/3)\). For odd \(n\) with \(3\nmid n\), this is \(\pm1\). For even \(n\) with \(3\nmid n\), it equals \(-1\), and the upper/lower signs can be chosen with \(u_iv_i=-1\) and \(U=V=1\). This produces multiplier \(+1\), attaining the bound.

**4. Sharp gap when \(n\equiv3\pmod6\).** The total matching count is even, so all multipliers are even. At the all-vertical-positive, all-\(y_i=-1\) frequency the trace is \(2\cos(n\pi/3)=-2\) and there are no extra horizontal matchings. Hence two is attained.

**5. Sharp gap when \(n\equiv0\pmod6\).** The total matching count is divisible by four: in fact \(B(1)^6\equiv I\pmod4\), so \(L_n=\operatorname{tr}(B(1)^n)\equiv2\pmod4\), giving \(N_n=L_n+2\equiv0\pmod4\). Let \(F_0=0\), \(F_1=1\), \(F_j=F_{j-1}+F_{j-2}\). The number of perfect matchings using any fixed vertical edge is \(F_n\), and the number using any fixed horizontal edge is \(F_{n-1}+1\): the second summand counts the unique mixed-offset matching containing that edge. Since \(F_n\) is even and \(F_{n-1}\) is odd whenever \(3\mid n\), every edge belongs to an even number of matchings. For any frequency support \(S\), the parity of the number of matchings with odd \(|M\cap S|\) is thus zero. From \(W_n(S)=N_n-2\#\{M:|M\cap S|\text{ odd}\}\) it follows that \(4\mid W_n(S)\). To attain four, choose \(x_i=1\), \(y_i=-1\) for every \(i\) and select the separate upper/lower signs with \(U=V=1\). Here \(\operatorname{tr}(B(-1)^n)=2\), giving \(W_n=4\).

**6. Largest singular value.** Every signed sum has magnitude at most \(N_n\), by the triangle inequality; equality holds at the trivial character. Combining with Steps 2–5 proves all assertions.

## Verification

The accompanying standalone `prism_verifier.py` constructs perfect matchings independently by recursive vertex pairing. Its exact integer Walsh–Hadamard transform checks every multiplier through \(n=7\) (all frequency signs for \(n=3,4,5\), and 2000 deterministic/random frequency checks for \(n=6,7\)). It checks the asserted zero/nonzero boundary, least positive multiplier and maximal multiplier for each of \(n=3,\ldots,7\); the count, kernel dimension and gap output is independently obtained by complete Walsh transform. In addition, integer transfer identities and explicit vanishing witnesses were checked for every \(3\le n\le300\). These are finite corroborations, not a substitute for Steps 1–6.

## Relationship to prior work

Multivariate matching polynomials and their cyclic recurrences are classical; in particular McSorley–Feinsilver give explicit general cyclic matching-polynomial identities, so the cycle transfer calculation itself is not a novelty claim. Hwang–Lei–Yeh–Zhang give a full prism-perfect-matching decomposition by cyclic choices and two exceptional matchings at even orders. The result here concerns a distinct question not answered by those enumerations: **simultaneous sign choices on all \(3n\) individual edges**, the precise convolution invertibility boundary, and the *sharp* positive singular-value residue classes \(1,2,4\). The known Lucas matching counts are credited rather than claimed anew. Transfer-matrix work for cyclic ladder lattice models also motivated examining signs around the seam.

## Limitations

This result gives an exact formula for each Fourier coefficient but **does not** give a closed multiplicity census or the nullity at lengths divisible by three. The lower bounds for singular values refer only to nonzero multipliers. It does not prove a statement about nonlinear inverse problems, arbitrary cylindrical graphs, or independent validation. Although the cited full texts have been compared, an equivalent unindexed evaluation of a prism dimer partition function at all edge signs cannot be excluded conclusively.

## References

- J. P. McSorley and P. Feinsilver, *Multivariate matching polynomials of cyclically labelled graphs*, Discrete Mathematics 309 (2009), 3205–3218, DOI 10.1016/j.disc.2008.09.020; openly reproduced at https://www.academia.edu/58240900/Multivariate_matching_polynomials_of_cyclically_labelled_graphs, sections 1 and 5.
- H.-K. Hwang, H. Lei, Y.-N. Yeh and H. Zhang, *Distribution of forcing and anti-forcing numbers of random perfect matchings on hexagonal chains and crowns*, https://algo.stat.sinica.edu.tw/hk/files/2015/01/distribution_of_the_forcing_and_anti-forcing_numbers.pdf, appendix, Lemmas 4.3–4.4 (pp. 20–21).
- S.-C. Chang and R. Shrock, *Exact Partition Functions for the q-State Potts Model with a Generalized Magnetic Field on Lattice Strip Graphs*, arXiv:1506.07392, first posted 2015-06-24, https://arxiv.org/abs/1506.07392 (related cyclic-strip transfer framework; not a prism-dimer Fourier result).
- Y. Wang, *Di-Forcing Polynomials for Cyclic Ladder Graphs*, Mathematics 11 (2023), 3598, https://doi.org/10.3390/math11163598, section 3 (unsigned forcing enumerators, not the signed Fourier multipliers).
