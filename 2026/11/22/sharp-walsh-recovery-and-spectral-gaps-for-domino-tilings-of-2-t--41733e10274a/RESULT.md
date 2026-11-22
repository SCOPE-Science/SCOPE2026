# Sharp Walsh recovery and spectral gaps for domino tilings of \(2\times n\) rectangles

## Finding
Let \(L_n=P_n\square K_2\) for every integer \(n\ge1\). Let \(E_n\) be its \(3n-2\) edges, and let \(f_n:\mathbb F_2^{E_n}\to\{0,1\}\) be the indicator of the edge-incidence vectors of all perfect matchings (domino tilings) of \(L_n\). Write \(T_ng=f_n*g\) for **unnormalized** counting convolution on the Boolean edge group and
\[
W_n(S)=\sum_{M\text{ perfect matching of }L_n}(-1)^{|M\cap S|}
\qquad (S\subseteq E_n).
\]
Set \(F_0=0,F_1=1,F_{j+1}=F_j+F_{j-1}\). Then the following statements hold simultaneously for every \(n\ge1\).

1. \(T_n\) is invertible if and only if \(n\not\equiv2\pmod3\).
2. Its largest absolute Walsh multiplier is \(F_{n+1}\). Its smallest **strictly positive** absolute Walsh multiplier is \(1\) if \(n\not\equiv2\pmod3\), and \(2\) if \(n\equiv2\pmod3\). Hence the sharp \(\ell^2\)-spectral condition number on the recoverable Fourier range is
\[
\kappa_n=\begin{cases}F_{n+1},&n\not\equiv2\pmod3,\\ F_{n+1}/2,&n\equiv2\pmod3.\end{cases}
\]
For invertible widths this is the ordinary condition number; for singular widths it is the condition number on \((\ker T_n)^\perp\).
3. If \(n=3k-1\) with integer \(k\ge1\), then
\[
\frac{\dim\ker T_n}{2^{3n-2}}\ge2^{-k}.
\]
In fact the exact nullity equals \(2^{2n-1}Z_n\), where \(Z_n\) counts sign strings \((\epsilon_2,\ldots,\epsilon_n)\in\{\pm1\}^{n-1}\) for which \(u_0=u_1=1\), \(u_j=u_{j-1}+\epsilon_j u_{j-2}\) satisfy \(u_n=0\). Thus \(Z_n\) is an explicitly computable integer-state return count, without a claimed closed form.

## Assumptions and scope
Graphs are simple, labelled by their two rows and \(n\) ordered columns; orientations of physical dominoes do not create additional tilings. A Fourier frequency assigns a bit to every edge, so top and bottom horizontal edges are distinct. All ranks and singular values concern the convolution operator on the complete \(2^{3n-2}\)-dimensional function space, not an edge-coordinate sampling matrix. The rank is over \(\mathbb R\) or \(\mathbb C\); both agree because the Walsh diagonalization is real. Nonzero spectral conditioning is defined only on the orthogonal complement of the nullspace.

## Proof
Denote the sign on the vertical rung of column \(j\) by \(a_j\in\{\pm1\}\). For \(2\le j\le n\), denote by \(b_j\in\{\pm1\}\) the product of the signs on the two horizontal edges joining columns \(j-1\) and \(j\). Let \(P_j\) be the signed tiling partition function of the first \(j\) columns, using the restricted edge signs. The final column is covered either by one vertical domino or by the two horizontal dominoes from the preceding column; hence
\[
P_0=1,\quad P_1=a_1,\quad P_j=a_jP_{j-1}+b_jP_{j-2}\quad(2\le j\le n).
\]
This recurrence is a decomposition of every tiling exactly once and gives \(W_n(S)=P_n\). Put \(A_j=\prod_{i=1}^j a_i\) and \(u_j=A_jP_j\), with \(A_0=1\). Because every \(a_j\) is a sign, \(u_0=u_1=1\) and
\[
u_j=u_{j-1}+\epsilon_j u_{j-2},\qquad \epsilon_j=b_ja_{j-1}a_j\in\{\pm1\}.
\]
Every sign string \((\epsilon_2,\ldots,\epsilon_n)\) is attainable: choose all \(a_j=1\) and choose one of the two horizontal edge signs for each \(b_j\) to equal \(\epsilon_j\). For fixed \(\epsilon\), exactly \(2^n\) choices of the rung signs and \(2^{n-1}\) choices of the individual horizontal-edge signs yield it; therefore each normalized sign string occurs at precisely \(2^{2n-1}\) Walsh frequencies. In particular \(\dim\ker T_n=2^{2n-1}Z_n\) for \(n\ge2\).

There are \(F_{n+1}\) tilings by the same two-case recursion with all signs equal to \(+1\), so \(|W_n(S)|\le F_{n+1}\) for every frequency, with equality at the empty frequency. For any frequency, \(W_n(S)\equiv F_{n+1}\pmod2\), since each summand is \(\pm1\). The Fibonacci recurrence modulo two has period three, with a zero precisely when the index is divisible by three. Hence for \(n\not\equiv2\pmod3\), all Fourier multipliers are odd and nonzero; in the other residue class they are all even.

Choose \(\epsilon_j=-1\) for every \(j\ge2\). The normalized sequence begins \(1,1,0,-1,-1,0,1,1,0,\ldots\), is period six, and has absolute value one whenever \(j\not\equiv2\pmod3\); at \(j\equiv2\pmod3\) it equals zero. The same sign construction is attainable at a Walsh frequency, proving both the converse singularity criterion and the sharp positive minimum one at every nonsingular width. If \(n\equiv2\pmod3\), change only the last \(\epsilon_n\) from \(-1\) to \(+1\). For the all-minus sequence \(u_{n-1}=u_{n-2}\in\{\pm1\}\) and \(u_n=0\), so the changed last step yields \(u_n=2u_{n-1}=\pm2\). Parity already excluded any smaller nonzero magnitude. Walsh diagonalization now proves both condition-number formulas.

Finally let \(n=3k-1\). Fix \(\epsilon_2=-1\), giving \((u_1,u_2)=(1,0)\). Whenever a state \((u_{m-1},u_m)=(c,0)\) with \(c\in\{\pm1\}\) has been reached, select \(\epsilon_{m+1}\) and \(\epsilon_{m+2}\) arbitrarily, and set \(\epsilon_{m+3}=-1\). The recurrence gives
\[
(u_{m+1},u_{m+2},u_{m+3})=(\epsilon_{m+1}c,\epsilon_{m+1}c,0).
\]
There are four independent choices in each of the \(k-1\) subsequent blocks of length three, so \(Z_n\ge4^{k-1}\). Multiplying by the fixed multiplicity \(2^{2n-1}\) and dividing by the group size \(2^{3n-2}\) gives \(2^{-k}\). This completes the proof for all stated lengths.

## Verification
Two independently organized exact-integer programs are included. `check_direct.py` generates all domino tilings as edge-incidence masks, evaluates their complete Walsh transform by an in-place butterfly, and independently calculates the weighted matching recurrence at every frequency for \(1\le n\le6\). `check_recurrence.py` enumerates all normalized signed-continuant states through \(n=15\), checking the zero criterion, extremal multiplier magnitudes, the constructive nullity bound, and exact initial null counts. Both programs were executed successfully with Python 3 and have no third-party dependencies.

The first resonant values of \(Z_n\) are \(Z_2=1\), \(Z_5=5\), \(Z_8=27\), \(Z_{11}=152\), and \(Z_{14}=879\). These are independent finite checks, not substitutes for the all-width proof.

## Relationship to prior work
The Fibonacci count of \(2\times n\) domino tilings is classical. Cohn, Kenyon and Propp (first public arXiv posting 2000-08-30) study dimer partition functions and general weighted tilings, but their variational and entropy results do not determine arbitrary edge-sign Walsh spectra of this ladder. Barkley and Liu (first posted 2019-11-19) study the two-adic divisibility of unsigned perfect-matching counts: their parity framework explains why widths with odd Fibonacci counts cannot have a Walsh zero but does not imply a signed zero witness, sharp nonzero spectral gap or quantitative family of null frequencies. Gross and Yamzon (first posted 2020-08-06) analyze tiling-flip connectivity and binomial ideals, not the Boolean edge-convolution spectrum. Aksenov and Kokhas (2014, Sections 2–5) relate signed vertical-domino statistics and a single specialization of a tiling polynomial to adjacency determinants. Their Theorems 3.5–3.6 consider the uniform vertical-count weighting, not independent signs on each physical edge or the complete Boolean Walsh spectrum. The new claim uses these standard prerequisites but concerns a different recovery invariant.

## Limitations
The theorem does not provide a closed-form expression for \(Z_n\) at every resonant width, nor a sharp endpoint \(\ell^1\) or \(\ell^\infty\) projection norm. The condition number is an exact \(\ell^2\) statement using the **unnormalized** Fourier multipliers; normalizing convolution by the group size scales all positive singular values equally and does not alter their ratio. Historical novelty remains conditional on bounded literature comparison; equivalent unindexed signed-continuant calculations may exist.

## References
1. H. Cohn, R. Kenyon, J. Propp, *A Variational Principle for Domino Tilings*, arXiv:math/0008220, first public 2000-08-30, https://arxiv.org/abs/math/0008220 (dimer and weighted-partition background).
2. G. T. Barkley, R. I. Liu, *Channels, Billiards, and Perfect Matching 2-Divisibility*, arXiv:1911.08102, first public 2019-11-19, https://arxiv.org/abs/1911.08102 (parity of matching counts).
3. E. Gross, N. Yamzon, *Binomial Ideals of Domino Tilings*, arXiv:2008.02896, first public 2020-08-06, https://arxiv.org/abs/2008.02896 (tiling-space and flip-connectivity context).
4. V. Aksenov, K. Kokhas, *Domino Tilings and Determinants*, Journal of Mathematical Sciences 200 (2014), 647–658, DOI:10.1007/s10958-014-1954-4 (determinants and the vertical-domino-statistic polynomial).
