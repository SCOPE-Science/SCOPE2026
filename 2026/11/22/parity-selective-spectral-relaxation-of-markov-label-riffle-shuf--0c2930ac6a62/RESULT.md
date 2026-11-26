# Parity-selective spectral relaxation of Markov-label riffle shuffles

## Finding

Stably sort the positions of a symmetric binary Markov word of length \(n\), with a fair first bit, so that zeros precede ones. Write \(p\in[0,1]\) for the literal probability of retaining a bit and \(q=1-p\) for the probability of switching it. If \(\rho_n(p)\) is the expected sign of the resulting permutation, then, for \(n\ge1\),
\[
\rho_{n+4}=2p^2\rho_{n+2}-(2p-1)^2\rho_n,
\quad
(\rho_1,\rho_2,\rho_3,\rho_4)=(1,p,1-2(1-p)^2,2p^3-4p^2+4p-1).
\]
For each fixed \(m\ge1\), as \(q\downarrow 0\),
\[
\rho_{2m}(1-q)=1-mq+O_m(q^2),\qquad
\rho_{2m+1}(1-q)=1-m(m+1)q^2+O_m(q^3).
\]
After \(t\) independent shuffles, the expected sign (from the identity) is \(\rho_n(p)^t\). For fixed \(s>0\), this converges to \(e^{-ms}\) on an even deck at \(t=\lfloor s/q\rfloor\), and to \(e^{-m(m+1)s}\) on an odd deck at \(t=\lfloor s/q^2\rfloor\).

If \(n\to\infty\) and \(nq\to\xi\in[0,\infty)\), put \(a=1-1/\sqrt 2\), \(b=1+1/\sqrt 2\). The one-shuffle sign expectation converges along each parity to
\[
\begin{aligned}
\Phi_{\rm even}(\xi)&=\left(\tfrac12+\tfrac1{2\sqrt2}\right)e^{-a\xi}
+\left(\tfrac12-\tfrac1{2\sqrt2}\right)e^{-b\xi},\\
\Phi_{\rm odd}(\xi)&=\left(\tfrac12+\tfrac1{\sqrt2}\right)e^{-a\xi}
+\left(\tfrac12-\tfrac1{\sqrt2}\right)e^{-b\xi}.
\end{aligned}
\]
In particular the respective right derivatives at zero are \(-1/2\) and zero.

## Assumptions and scope

Start with a fair bit and draw independent Bernoulli(\(q\)) switches at all adjacent positions. Sort by bit only, preserving order within each bit value. The inverse permutation has the same sign. Regenerate the labels independently in successive rounds. The signs are relative to the original order. The recurrence includes both deterministic endpoints and the single-card initialization. If using the alternative adhesion parameter \(h\) for literal retention \((1+h)/2\), translate via \(h=2p-1\); its adhesion loss \(1-h\) is \(2q\), not \(q\).

## Proof

**Signed transfer.** The permutation sign is \((-1)^{I_n}\), where \(I_n\) counts pairs of positions \(i<j\) with bits \(1,0\). Track the last bit \(b\) and the parity \(z\) of all ones seen. Appending a one toggles \(z\), and appending a zero multiplies the sign by \((-1)^z\). The row transfer on \((0,0),(0,1),(1,0),(1,1)\) is
\[
M=\begin{pmatrix}p&0&0&q\\0&-p&q&0\\q&0&0&p\\0&-q&p&0\end{pmatrix},\qquad
\rho_n=(1/2,0,0,1/2)M^{n-1}\mathbf1 .
\]
Expansion of \(\det(\lambda I-M)\) gives \(\lambda^4-2p^2\lambda^2+(p^2-q^2)^2\), with \(p^2-q^2=2p-1\). The first four products give the displayed initial data; Cayley–Hamilton gives the recurrence without needing distinct roots.

**Rare switches.** No switches gives positive sign. With one switch after \(k\), the inversion count is zero for initial zero and \(k(n-k)\) for initial one. For \(n=2m\) exactly the \(m\) odd positions give odd inversion count in the latter case. Thus the odd-sign probability is \((m/2)q+O_m(q^2)\). For \(n=2m+1\) zero or one switch cannot produce odd sign. With two switches after \(k<\ell\), the inversion counts for initial zero and one are \((\ell-k)(n-\ell)\) and \(k(\ell-k)\), respectively. Both are odd exactly when \(k\) is odd and \(\ell\) is even. There are \(m(m+1)/2\) such switch pairs, so the odd-sign probability is \(m(m+1)q^2/2+O_m(q^3)\). The expansions follow since the mean sign is one minus twice the odd-sign probability.

**Time relaxation.** The sign is multiplicative under permutation composition and the increments are independent. Applying the logarithm to \(\rho_n(1-q)>0\) for small enough \(q\) gives the stated limits. Uniform measure on \(S_n\) has zero mean sign for \(n\ge2\), so the sign also gives the lower bound \(d_{\rm TV}(t)\ge |\rho_n|^t/2\) from the identity.

**Growing-deck limit.** For \(p<1\) sufficiently close to one, the two subsequence roots are
\[
r_\pm=p^2\pm(1-p)\sqrt{p^2+2p-1}.
\]
Writing \(c_+=2-\sqrt2\), \(c_-=2+\sqrt2\), we have \(r_\pm=1-c_\pm q+O(q^2)\). For either parity, start the subsequence at \(y_0=\rho_2\) or \(\rho_1\) and write \(y_j=A r_+^j+(y_0-A)r_-^j\), where \(A=(y_1-r_-y_0)/(r_+-r_-)\). At even parity \(y_1-y_0=-q+O(q^2)\); at odd parity it is \(O(q^2)\). As \(y_0\to1\), the limits of \(A\) are \((c_--1)/(c_--c_+)\) and \(c_-/(c_--c_+)\) respectively. Here \(j=\lfloor n/2\rfloor+O(1)\), so \(jq\to\xi/2\) and \(jq^2\to0\). The powers converge to \(e^{-a\xi}\) and \(e^{-b\xi}\). At \(q=0\) the word is constant and \(\rho_n=1\), consistent with either profile at \(\xi=0\).

## Relationship to prior work and limitations

Jonasson and Morris, §2 and Theorem 2.1, give this same stable-sort labeling rule for the inverse of their \(p\)-riffle and prove a full-chain mixing upper bound for fixed \(p\) as the deck grows. Jiang, Definition 2.4, uses the adhesion convention \(p=(1+h)/2\) in the present notation and gives full-chain fixed-deck mixing bounds near maximal adhesion. Palomares, Definitions 6–7 and §7, treats the same geometric model with a switch parameter and reports finite-deck spectral computations. Finite spectra can include a sign eigenvalue; the result here gives an exact sign law across sizes, together with both fixed-deck time scales and the growing-deck sign profiles. An inversion-count weak limit after normalization does not by itself give a parity expectation: the alternating signs oscillate on the scale of one inversion.

The sign is one Fourier coefficient of the shuffle law, not its full spectrum. Its faster relaxation on an even deck is compatible with slower full-deck mixing. No cutoff, sharp mixing estimate, or joint time-and-growing-deck mixing theorem is claimed.

## Verification

Run `python3 check.py` to compare literal-stay word enumeration and the signed transfer with the recurrence, check the rare-switch parity counts, and compare the limiting profiles numerically on a growing-size grid. These are finite checks; the all-size formulas and limits are proved above.

## References

1. Y. Jiang, *Adhesive riffle shuffles: one-parameter models and mixing bounds*, arXiv:2611.02092, https://arxiv.org/abs/2611.02092.
2. J. Jonasson and B. Morris, *Rapid mixing of dealer shuffles and clumpy shuffles*, Electronic Communications in Probability 20 (2015), no. 20, https://doi.org/10.1214/ECP.v20-3682.
3. M. Palomares, *Comparing the Mixing Rates of Neat Riffle Shuffles*, University of Michigan report, https://lsa.umich.edu/content/dam/math-assets/reu-su22/2025/REU_Report_Final_Mateo_Palomares.pdf.
