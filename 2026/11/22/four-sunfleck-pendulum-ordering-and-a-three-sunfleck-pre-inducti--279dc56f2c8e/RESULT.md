# Four-sunfleck pendulum ordering and a three-sunfleck pre-induction switch

## Finding

**Exact finite-fleck ordering theorem.** Consider the first-order saturating-induction model specified below. Given any three distinct, strictly positive illumination durations, write their activation increments as \(0<a<b<c<1\) and set \(q=e^{-\beta h}\in(0,1)\). If the initial induction fraction is \(s\in[0,1]\), the carbon-maximizing temporal orders of the three lightflecks, expressed as their increments, are exactly:

- \((a,c,b)\) and \((b,c,a)\) if \(s=0\);
- \((b,c,a)\) alone if \(0<s<qa\);
- \((b,c,a)\) and \((c,b,a)\) if \(s=qa\);
- \((c,b,a)\) alone if \(qa<s\le1\).

For **four** distinct, strictly positive lightfleck durations, with increments \(0<a<b<c<d<1\) and initial induction \(s=0\), the **only** globally optimal orders are \((a,c,d,b)\) and its reversal \((b,d,c,a)\), for every \(q\in(0,1)\). These are the two pendulum arrangements: the two shortest lightflecks are at the ends and the two longest are adjacent in the middle. The order is independent of the durations' values and of the relative time scales of light induction and dark relaxation. These are global comparisons over all six or twenty-four permutations, including all equality cases stated here.

## Assumptions and scope

One leaf has a scalar induction state \(x\in[0,1]\). During an illuminated interval of duration \(\ell>0\), its state evolves by \(\dot x=\alpha(1-x)\), with \(\alpha>0\), and its instantaneous modeled carbon-assimilation rate is \(P x\), with \(P>0\). All lightflecks have the same saturating illumination intensity. Between consecutive lightflecks are dark intervals of exactly the same duration \(h>0\), in which \(\dot x=-\beta x\), with \(\beta>0\); carbon gain in darkness is taken to be zero. No terminal carbon reward or post-illumination fixation is included. Light durations are fixed as a multiset; only their temporal order can be changed. There is no pre-fleck dark interval unless already reflected in the specified initial state \(s\).

Define \(u(\ell)=1-e^{-\alpha\ell}\in(0,1)\), \(q=e^{-\beta h}\in(0,1)\), and let the dimensionless activation increment of the \(i\)-th ordered lightfleck be \(u_i\). If \(x_i\) is the induction immediately before that lightfleck, then

\[
\int_{\text{lightfleck }i}P x(t)\,dt=P\left[\ell_i-\frac{(1-x_i)u_i}{\alpha}\right],\qquad
x_{i+1}=q\bigl(u_i+(1-u_i)x_i\bigr),\quad x_1=s.
\]

Consequently, with \(C(\pi)\) the accumulated light-phase carbon gain of an ordering \(\pi\), maximizing \(C(\pi)\) is exactly equivalent to minimizing \(H(\pi)=\sum_i(1-x_i)u_i\). In the proof we use the score \(S(\pi)=-H(\pi)\), which differs from \(\alpha C(\pi)/P\) by the permutation-independent sum \(-\alpha\sum_i\ell_i\).

## Proof

**Three lightflecks.** Direct substitution in the two affine state-update equations gives, for any \(u,v,w\in(0,1)\), the following exact exchange identities:

\[
S(u,v,w)-S(v,u,w)=(1-q)(u-v)(s-qw),
\]
\[
S(u,v,w)-S(u,w,v)=q(1-q)(v-w)[u+(1-u)s],
\]
\[
S(u,v,w)-S(w,v,u)=s(1-q)(u-w)[1+q(1-v)].
\]

The second difference is strictly positive precisely when \(v>w\), so every maximizer puts a larger increment second than third. For three distinct increments \(a<b<c\), only \((a,c,b)\), \((b,c,a)\), and \((c,b,a)\) can maximize. The third identity shows that for \(s>0\), \((b,c,a)\) strictly beats \((a,c,b)\), while those two tie for \(s=0\). The first identity comparing \((b,c,a)\) and \((c,b,a)\) has sign \((1-q)(b-c)(s-qa)\). This gives every regime and the listed strict inequalities and ties. At \(s=0\) the first identity makes \((b,c,a)\) strictly preferable to \((c,b,a)\); at \(s>0\) exactly one or both survive the comparison. No other permutation can tie because the rejected last-pair swaps are strict.

**Four lightflecks from zero induction.** Write the ordered increments as \((A,B,C,D)\), all in \((0,1)\). Expanding the recurrence for the deficits \(1-x_i\) gives

\[
H=A+B+C+D-Q(A,B,C,D),
\]
\[
\begin{aligned}
Q(A,B,C,D)={}&q(AB+BC+CD)\\
&+q^2\bigl[A(1-B)C+B(1-C)D\bigr]\\
&+q^3 A(1-B)(1-C)D.
\end{aligned}
\]

Thus carbon is maximized exactly when \(Q\) is maximized. The polynomial is invariant under reversal. Five exact transposition differences are

\[
\begin{aligned}
Q(A,B,C,D)-Q(B,A,C,D)&=q(1-q)(B-A)[C+qD(1-C)],\\
Q(A,B,C,D)-Q(A,B,D,C)&=q(1-q)(C-D)[B+qA(1-B)],\\
Q(A,B,C,D)-Q(C,B,A,D)&=q(1-q)D(C-A)[1+q(1-B)],\\
Q(A,B,C,D)-Q(A,D,C,B)&=q(1-q)A(B-D)[1+q(1-C)],\\
Q(A,B,C,D)-Q(A,C,B,D)&=q(1-q)(A-D)(B-C).
\end{aligned}
\]

Every bracket in the first four expressions is positive. Thus every global maximizer (which exists among the twenty-four permutations) must satisfy \(A<B\), \(C>D\), \(A<C\), and \(B>D\). In particular \(A,D\) are the two *smallest* increments and \(B,C\) are the two *largest*. The final transposition identity forces \((A-D)(B-C)>0\): if \(A<D\), then \(B<C\), giving \((a,c,d,b)\); if \(A>D\), then \(B>C\), giving its reversal \((b,d,c,a)\). Reversal symmetry makes their scores equal. Every excluded permutation has a strictly improving transposition, establishing uniqueness of the two global maxima.

**Exact witness and comparison.** Let \(q=1/2\) and use the four increments \(a=1/5\), \(b=1/4\), \(c=1/2\), and \(d=3/4\). These correspond, at \(\alpha=1\), to durations \(\log(5/4)\), \(\log(4/3)\), \(\log2\), and \(\log4\). The optimal pendulum order \((a,c,d,b)\) has \(Q=459/1280\), whereas the monotone increasing order \((a,b,c,d)\) has \(Q=83/256\). The exact excess dimensionless carbon gain is \(11/320\). For the three increments \((1/5,1/2,3/4)\) at the same \(q\), the exact pre-induction switch occurs at \(s=1/10\).

## Verification

The standalone `verify.py` enumerates every permutation of three and four exact rational increments, evaluates carbon directly from the exact affine recurrence, and checks the optimizer classes and the three three-lightfleck exchange identities. It also checks the four-lightfleck \(Q\)-identity and the explicit rational example. Run from a folder containing this file and the checker using `python3 verify.py`. A full execution produced `PASS: 124005 exact rational assertions`. The exhaustive permutation enumeration is only for each sampled rational parameter tuple; it is **not** an exhaustive verification of continuous parameter space. The algebraic exchange proofs above establish the theorem for all admissible real parameters.

## Relationship to prior work

Photosynthetic induction, its loss in shade, and the practical dependence of carbon gain on fluctuating irradiance are longstanding established phenomena (Jackson, Woodrow and Mott 1991; Pons, Pearcy and Seemann 1992; Retkute and colleagues 2015). Durand and colleagues (2022) report light-use dynamics in sunflecks and model photosynthetic performance as durations and frequencies vary; Burgess, Retkute and Murchie (2023) use an exponential light-history memory to model entrainment. Those works provide substantially richer biological models and do not, in the material examined, give the present exact permutation rankings under a fixed multiset of unequal light durations and equal shade gaps. The integer-sequence record OEIS A101986 documents pendulum maximization of *adjacent-pair products*; that is a related limiting comparison when \(q\) tends to zero, whereas the present four-fleck objective also contains nonadjacent, attenuation-weighted products at every \(q>0\). It does not follow as a stated corollary of the adjacent-only result without the full transposition argument.

The theorem is deliberately restricted to a scalar, one-rate induction mechanism; it does not claim novelty of induction kinetics, fading memory, or generic rearrangement methods. Older relevant empirical papers were available only in abstract or partial text, so the historical priority comparison is qualified rather than a claim that they have been fully ruled out.

## Limitations

The model omits multiple induction timescales, stomatal dynamics, photodamage, post-illumination fixation, shade photosynthesis, changing illumination intensity, and variable shade gaps. It assumes known fixed durations and no feedback from other environmental variables. No statement is proved here for five or more lightflecks, for a nonzero initial induction state in the four-lightfleck case, or for unequal shade gaps. The theorem is a mathematical benchmark and is **not** a validated rule for greenhouse operation or crop productivity. Self-review does not imply independent scientific validation or complete historical-priority assurance.

## References

1. Jackson, R. B., Woodrow, I. E. and Mott, K. A. (1991). *Nonsteady-State Photosynthesis following an Increase in Photon Flux Density: Effects of Magnitude and Duration of Initial PFD.* Plant Physiology 95(2), 498–503. Published 1991-02-01. https://doi.org/10.1104/pp.95.2.498
2. Pons, T. L., Pearcy, R. W. and Seemann, J. R. (1992). *Photosynthesis in flashing light in soybean leaves grown in different conditions. I. Photosynthetic induction state.* Plant, Cell & Environment 15, 569–576. https://doi.org/10.1111/j.1365-3040.1992.tb01490.x
3. Pons, T. L. and Pearcy, R. W. (1992). *Photosynthesis in flashing light in soybean leaves grown in different conditions. II. Lightfleck utilization efficiency.* Plant, Cell & Environment 15, 577–584. https://doi.org/10.1111/j.1365-3040.1992.tb01491.x
4. Retkute, R. et al. (2015). *Exploiting heterogeneous environments: does photosynthetic acclimation optimize carbon gain in fluctuating light?* Journal of Experimental Botany 66, 2437–2447. Published online 2015-03-18. https://doi.org/10.1093/jxb/erv055
5. Durand, M. et al. (2022). *Sunflecks in the upper canopy: dynamics of light-use efficiency in sun and shade leaves of Fagus sylvatica.* New Phytologist 235, 1365–1378. https://doi.org/10.1111/nph.18222
6. Burgess, A. J., Retkute, R. and Murchie, E. H. (2023). *Photoacclimation and entrainment of photosynthesis by fluctuating light varies according to genotype in Arabidopsis thaliana.* Frontiers in Plant Science 14, 1116367. https://doi.org/10.3389/fpls.2023.1116367
7. OEIS Foundation. *A101986: Maximum sum of products of successive pairs in a permutation of order n+1.* https://oeis.org/A101986
