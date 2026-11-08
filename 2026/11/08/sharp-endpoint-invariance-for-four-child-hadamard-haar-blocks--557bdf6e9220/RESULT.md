# Sharp endpoint invariance for four-child Hadamard Haar blocks

## Finding
For every integer \(d\geq0\), let \(\Omega_d=(\mathbb F_2^2)^d\) have uniform probability and let \(\mathcal H_d\) be the real, complete, normalized four-child Haar system consisting of the constant function and the three nontrivial Walsh contrasts at every cylinder of lengths \(0,\ldots,d-1\). For every independent choice of signs \(\varepsilon_h\in\{-1,1\}\), let \(T_\varepsilon f=\sum_{h\in\mathcal H_d}\varepsilon_h\langle f,h\rangle h\). Then the sharp endpoint unconditionality constant is
\[
U_d:=\max_\varepsilon\|T_\varepsilon\|_{L^\infty(\Omega_d)\to L^\infty(\Omega_d)}
=\frac{4d}{3}+\frac59+\frac4{9\cdot4^d}.
\]
This is **exactly equal at every depth** to the sharp constant for the *binary*, standard Haar system through \(2d\) levels. The two signed multiplier families are nevertheless different: a four-child Walsh signed kernel can have its distinguished entry in a child outside the binary half of the evaluation point, whereas a signed two-stage binary Haar kernel cannot. All \(4^d\) evaluation rows can attain \(U_d\) for a suitable choice of coefficient signs. When the constant coefficient sign is fixed positive, an evaluation row has exactly \(4\) maximizing ancestral sign patterns for \(d=1\), and exactly \(16\cdot3^{d-2}\) for \(d\ge2\); signs at other nodes do not affect that row. Norming inputs are precisely the unit sup-norm functions agreeing, up to one global sign, with the sign of a corresponding kernel row at every nonzero kernel entry.

## Assumptions and scope
Write the four children as \(\mathbb F_2^2\). For each nonzero \(a\in\mathbb F_2^2\) put \(\chi_a(x)=(-1)^{a\cdot x}\). At a cylinder \(v\) of level \(j<d\), define \(h_{v,a}(z)=2^j\chi_a(z_{j+1})\) when \(z\) extends \(v\), and zero otherwise. Together with \(h_\emptyset=1\), these \(1+3\sum_{j=0}^{d-1}4^j=4^d\) functions form an orthonormal basis under uniform probability. The norm is the operator norm on real \(L^\infty\), not a weak-type or \(L^p\) norm. The constant coefficient is signed independently. The statement includes \(d=0\), where \(U_0=1\).

## Proof
**1. Kernel and the eight local possibilities.** The signed operator has kernel
\[
K_\varepsilon(x,y)=\varepsilon_\emptyset+
\sum_{j=0}^{d-1}\mathbf1_{\{x_{<j}=y_{<j}\}}4^j
\sum_{a\ne0}\varepsilon_{x_{<j},a}\chi_a(x_{j+1})\chi_a(y_{j+1}).
\]
A global reversal of signs permits \(\varepsilon_\emptyset=+1\). For any fixed evaluation child, the vector of four local kernel values, as its three contrast signs vary, runs through exactly the eight vectors
\[
\bigl\{\,s(3\mathbf1_{\{y=t\}}-\mathbf1_{\{y\ne t\}}):s\in\{-1,1\},\ t\in\mathbb F_2^2\,\bigr\}.
\]
Here the displayed expression equals \(3s\) at \(t\), and \(-s\) elsewhere. This follows by applying the four-by-four Walsh matrix: any signed sum of the three nonconstant rows has exactly one entry of absolute value \(3\) and three entries of absolute value \(1\). Thus there are precisely two cases after ignoring which of the three siblings is distinguished: the exceptional child is the evaluation child, or it is a sibling.

**2. Exact backward optimization.** Fix an evaluation leaf. Since a Haar function off its ancestral path vanishes there, only signs on its ancestors affect its kernel row. At a level with \(k\) generations remaining, suppose previous ancestors contribute the constant \(4^ju\) on the current cylinder. Let \(F_k(u)\) denote the largest *conditional* average of the absolute final kernel, divided by \(4^j\). The terminal condition is \(F_0(u)=|u|\). Partitioning the cylinder into the three completed siblings and the continuing child gives the exact recurrence
\[
F_k(u)=\max_{s=\pm1}\left\{
\frac34|u-s|+F_{k-1}\!\left(\frac{u+3s}{4}\right),
\quad
\frac{|u+3s|+2|u-s|}{4}+F_{k-1}\!\left(\frac{u-s}{4}\right)
\right\}.
\]
The first expression places the exceptional signed entry on the continuing child; the second places it on a sibling. This recurrence is exact, not a bound.

**3. An invariant affine Bellman window.** Only \(|u|\le1\) is needed: whenever \(|u|\le1\), all four successor arguments in the recurrence remain in \([-1,1]\). The recurrence is even in \(u\). Assume inductively that on this interval
\[
F_{k-1}(u)=A+B|u|,\qquad \frac13\le B\le1.
\]
For \(0\le u\le1\), maximizing separately over \(s\) gives the two affine branches
\[
\begin{aligned}
H(u)&=A+\frac{3(1+B)}4+\frac{3-B}{4}u,\\
S(u)&=A+\frac{5+B}4+\frac{1+B}4u.
\end{aligned}
\]
Their exact difference is
\[
S(u)-H(u)=\frac{(1-B)(1-u)}2\ge0.
\]
Hence the sibling-exception branch is globally optimal throughout the required interval and
\[
A_k=A_{k-1}+\frac{5+B_{k-1}}4,\qquad
B_k=\frac{1+B_{k-1}}4,
\quad A_0=0,\ B_0=1.
\]
These relations preserve \(1/3\le B_k\le1\) and solve to
\[
B_k=\frac13+\frac2{3\cdot4^k},\qquad
A_k=\frac{4k}3+\frac29\left(1-4^{-k}\right).
\]
At the root the normalized state is \(u=1\), so \(U_d=F_d(1)=A_d+B_d\), giving the asserted formula for all \(d\ge0\).

**4. Sharpness, row counts, and binary comparison.** Each maximizing local branch is realized by an actual triple of coefficient signs, and off-path signs are free. Therefore the Bellman value is an attained operator norm. For positive \(u<1\) and \(k\ge2\), \(B_{k-1}<1\), making the sibling-exception branch strictly better; the maximizing signed orientation is opposite the sign of \(u\). At the initial state \(u=1\), both exceptional-child placements tie and give four maximizing local choices, leaving continuation state of absolute value \(1/2\). Every intermediate stage with at least two levels remaining has exactly three maximizing sibling locations and keeps the continuation state strictly between zero and one. At the last stage the two placements tie again, giving four choices. The count follows. The same local symmetry works at every possible evaluation leaf. For any row with \(\ell^1\) norm \(U_d\), choosing the input signs of its kernel entries makes the row attain the operator norm; conversely equality in the rowwise triangle inequality forces those signs up to one common sign wherever the kernel is nonzero.

For completeness, the binary comparator is proved independently here rather than assumed. Let \(G_m(u)\) be the corresponding normalized conditional absolute row mass with \(m\) binary generations remaining. The signed binary local contrast has values \(s,-s\), so
\[
G_0(u)=|u|,\qquad
G_m(u)=\max_{s=\pm1}\left\{\frac12|u-s|+G_{m-1}\!\left(\frac{u+s}{2}\right)\right\}.
\]
As in the four-child proof, \(|u|\le1\) is an invariant window. If \(G_{m-1}(u)=C+D|u|\) there, then \(G_m(u)=C_m+D_m|u|\) with \(C_m=C+(1+D)/2\) and \(D_m=(1-D)/2\). Beginning with \(C_0=0,D_0=1\), induction gives \(D_m=1/3+(2/3)(-1/2)^m\) and \(C_m=2m/3+(2/9)(1-(-1/2)^m)\). Hence the binary sharp constant is \(G_m(1)=2m/3+5/9+(4/9)(-1/2)^m\), and substitution of \(m=2d\) yields exactly \(U_d\). This equality does not identify the operator families: for an evaluation leaf beginning with binary child \(00\), the four-child Walsh kernel can take its exceptional magnitude-three value at child \(10\), while the first two binary Haar levels give only magnitude-one contributions there.

## Verification
The standalone script `verify.py` checks all eight signed four-child contrast rows, independently maximizes exact rational kernel-row masses across all \(8^d\) ancestral sign assignments through depth five, checks the Bellman formula to depth six, tests the affine window on a rational grid, and constructs full Haar matrix rows for multiple sign configurations through depth three. These finite diagnostics do not replace the proof above; they check indexing, normalization, the recurrence, and small-dimensional boundaries. Running `python verify.py` requires only Python 3 standard-library modules.

## Relationship to prior work
The 2013 open-access paper by Osękowski treats restricted weak-type inequalities for ordinary Haar projections and martingale transforms, rather than the real finite-depth, four-child, independently signed Hadamard contrast basis here. Kazarian, Kazaryan and San-Antolín's October 2014 preprint treats weighted \(L^p\) unconditionality of higher-rank Haar wavelets, but its accessible abstract does not state a finite \(L^\infty\) formula; full-text priority comparison remains incomplete. The classical binary finite-depth constant supplies a *numerically equal comparator*, not an implication: the two signed local kernel classes differ. The contribution is the exact identity of the sharp norms in these distinct bases and the four-child optimizer count, not unconditionality of infinite Haar bases.

## Limitations
The theorem uses uniform four-child splitting, the three real Sylvester/Walsh contrasts, complete generations, and independent real coefficient signs. It does not claim the same constant under arbitrary orthogonal rotations of the contrasts, node-dependent measures, non-power-of-four branching, suppression-only multipliers, or nonendpoint \(L^p\) norms. An unindexed earlier calculation of the same four-child constant or a hidden implication of a general higher-rank endpoint theorem remains a priority risk. Independent verification of originality is not claimed.

## References
1. A. Osękowski, “Sharp Inequalities for the Haar System and Fourier Multipliers,” *Journal of Function Spaces and Applications* (2013), article 646012, DOI 10.1155/2013/646012; publicly available December 5, 2013.
2. K. S. Kazarian, S. S. Kazaryan and Á. San-Antolín, “Wavelets in weighted norm spaces,” arXiv:1410.4888 (first public version October 17, 2014), subsequently *Tohoku Mathematical Journal* 70 (2018), 567–605.
