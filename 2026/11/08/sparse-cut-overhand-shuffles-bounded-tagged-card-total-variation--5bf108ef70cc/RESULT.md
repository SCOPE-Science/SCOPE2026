# Sparse-cut overhand shuffles: a total-variation and chi-square separation

## Finding

Fix \(c>0\). For each integer \(n>c\), cut each of the \(n-1\) gaps of an \(n\)-card deck independently with probability \(p_n=c/n\), and reverse the cards inside each resulting contiguous packet, leaving the packet order unchanged. Let \(K_n\) be the transition matrix of one distinguished card's position, \(U_n\) uniform on \(\{1,\ldots,n\}\), \(q_n=1-c/n\), and \(\delta_n=cq_n^{n-1}\).

**Theorem.** For every such \(n\), every pair of positions \(i,j\), and integer \(t\ge0\),
\[
K_n(i,j)\ge\frac{\delta_n}{n},\qquad
\sup_i\|K_n^t(i,\cdot)-U_n\|_{\rm TV}\le(1-\delta_n)^t,\qquad
\inf_i\|K_n^t(i,\cdot)-U_n\|_{\rm TV}\ge q_n^{(n-1)t}-\frac1n.
\]
For each fixed \(C>0\), as \(n\to\infty\),
\[
\sup_{\substack{t\in\mathbb Z_{\ge0}\\|t-(\log n)/(2c)|\le C}}
\sup_{1\le i\le n}
\left|\chi^2(K_n^t(i,\cdot)\|U_n)-n e^{-2ct}\right|\to0.
\]
Consequently, at every fixed total-variation accuracy the one-card mixing time stays bounded as \(n\to\infty\), whereas its worst-start fixed-accuracy chi-square mixing time is \((\log n)/(2c)+O_{c,\eta}(1)\). The chi-square window is at integer times; it does not have an unrestricted floor-centered pointwise limit.

## Assumptions and definitions

Each shuffle pass resamples all cuts independently. The result is for the *one-card marginal*, not the full permutation-valued shuffle. Time counts complete passes. For measures on \(\{1,\ldots,n\}\),
\[
\|\nu-\pi\|_{\rm TV}=\frac12\sum_j|\nu(j)-\pi(j)|,
\qquad \chi^2(\nu\|\pi)=\sum_j\frac{(\nu(j)-\pi(j))^2}{\pi(j)}.
\]
Constants in the limit can depend on the fixed \(c\); no uniform assertion for varying \(c\) is made.

## Proof

**1. Kernel, stationarity and minorization.** Suppose the card starts at \(i\). The numbers of additional cards in its packet to the left and right are independent truncated-geometric variables \(L\in\{0,\ldots,i-1\}\) and \(R\in\{0,\ldots,n-i\}\), with probabilities \(p_nq_n^r\) below their respective terminal values and terminal probabilities \(q_n^{i-1}\) and \(q_n^{n-i}\). After reversal its position is \(i+R-L\). For prescribed \(j\), take \(L=\min(i-1,n-j)\) and \(R=j-i+L\); then both are admissible and at least one is terminal. Their joint probability is at least \(p_n q_n^{L+R}\ge p_nq_n^{n-1}\). This proves the entrywise bound. Every fixed cut pattern produces an involutive permutation; hence \(K_n\) is symmetric and \(U_n\) is stationary. Since \(K_n(i,j)\ge\delta_n/n\), the Doeblin decomposition \(K_n=\delta_n\Pi_n+(1-\delta_n)R_n\), with \(\Pi_n\) the uniform-row kernel, proves the upper total-variation estimate. If all gaps remain uncut for \(t\) passes, an event of probability \(q_n^{(n-1)t}\), the card reaches a deterministic position (the initial position or its full-deck reflection); testing this atom proves the lower bound. Note \(\delta_n\to ce^{-c}>0\).

**2. Exact finite-deck spectrum (prior input).** Jiang's finite-deck diagonalization (Proposition 3.2) gives the cosine modes
\[
f_{n,k}(i)=\cos\bigl(k\pi(i-1/2)/n\bigr),\qquad
\ell_{n,k}=2(1-\cos(k\pi/n)),
\]
and eigenvalues
\[
\lambda_{n,k}=\frac{p_n^2+(-1)^kq_n^{n+1}\ell_{n,k}}{p_n^2+q_n\ell_{n,k}},
\qquad 0\le k<n.
\]
The constant mode is one; the other modes are orthogonal in \(L^2(U_n)\) with squared norms \(1/2\). Thus Parseval yields, for every starting position \(i\),
\[
\chi^2(K_n^t(i,\cdot)\|U_n)=2\sum_{k=1}^{n-1}f_{n,k}(i)^2\lambda_{n,k}^{2t},
\qquad 2\sum_{k=1}^{n-1}f_{n,k}(i)^2=n-1.
\]
The finite spectral representation is credited, not claimed as a new discovery.

**3. Uniform control of the low frequencies.** Put \(a_n=q_n^{n+1}\to e^{-c}\). For large \(n\), \(q_n>a_n\), and
\[
|\lambda_{n,k}|\le\frac{p_n^2+a_n\ell_{n,k}}{p_n^2+q_n\ell_{n,k}}.
\]
This upper bound decreases with \(\ell_{n,k}\). Since \(n^2p_n^2=c^2\) and \(n^2\ell_{n,1}\to\pi^2\), its largest value converges to
\[
r_*(c)=\frac{c^2+e^{-c}\pi^2}{c^2+\pi^2}<1.
\]
Choose any \(r\in(r_*(c),1)\), and then \(\alpha\in(0,1)\) satisfying \(\alpha<-\log(r)/c\). For all large \(n\), every nonconstant mode has \(|\lambda_{n,k}|\le r\), and for \(t=(\log n)/(2c)+O(1)\), uniformly in the starting position,
\[
2\sum_{1\le k\le n^\alpha}f_{n,k}(i)^2\lambda_{n,k}^{2t}\le2n^\alpha r^{2t}=o(1).
\]

**4. Correct bulk eigenvalue normalization and uniform chi-square window.** Define \(b_n=q_n^n\), *not* \(q_n^{n+1}\). The exact eigenvalue formula in Step 2 gives the following **exact algebraic identity**:
\[
\boxed{\lambda_{n,k}-(-1)^kb_n
=\frac{p_n^2\bigl(1-(-1)^kb_n\bigr)}{p_n^2+q_n\ell_{n,k}}.}
\]
Indeed \(q_n^{n+1}=q_nb_n\), so the two \(q_n\ell_{n,k}\) terms cancel on subtraction. For \(k>n^\alpha\), \(\ell_{n,k}=4\sin^2(k\pi/(2n))\ge4k^2/n^2\), making the right-hand side \(O_c(k^{-2})\), uniformly in this range. Since \(b_n\to e^{-c}>0\), for integers \(t=(\log n)/(2c)+O(1)\),
\[
\lambda_{n,k}^{2t}=b_n^{2t}\left(1+O_c\left(\frac{\log n}{n^{2\alpha}}\right)\right)
\quad(k>n^\alpha),
\]
uniformly in \(k\) and \(t\). Meanwhile \(nb_n^{2t}=O_c(1)\) and the total weight of the removed low modes is at most \(2n^\alpha\); their missing contribution to the putative bulk main term is therefore \(O(n^{\alpha-1})=o(1)\). The Parseval sum from Step 2 is consequently
\[
\chi^2(K_n^t(i,\cdot)\|U_n)=nb_n^{2t}+o(1)
\]
uniformly in \(i\) and in the displayed integer window. Finally, \(\log b_n=n\log(1-c/n)=-c+O_c(n^{-1})\), and \(ne^{-2ct}=O_c(1)\) in that window; hence \(nb_n^{2t}=ne^{-2ct}+o(1)\). This proves the asserted uniform limit. Markov contraction of chi-square in time and its uniform window profile give the fixed-accuracy \((\log n)/(2c)+O(1)\) mixing-time estimate.

## Verification and scope of evidence

The companion `verify.py` independently constructs finite tagged-card matrices, checks symmetry, stationarity and the entrywise lower bound, compares every cosine eigenmode to the direct matrix action, and evaluates finite chi-square sums. These are numerical and finite checks, not a proof of the limiting assertion. The proof uses the exact finite spectrum, the low-frequency bound, and the uniform bulk calculation above. The bulk normalization \(b_n=q_n^n\) is required for the boxed exact identity; replacing it by \(q_n^{n+1}\) would make that identity false, although the two choices have the same fixed-\(c\) leading asymptotic.

## Relationship to prior work

Jiang, *Cutoff for the Overhand Shuffle*, arXiv:2610.00137v1 (2026), studies the full permutation-valued deck with a **fixed** gap-cut probability and proves full-deck total-variation and entropy cutoff. Proposition 3.2 provides the finite one-card spectral representation used in this proof. The present result concerns the singular sparse-cut scaling \(p_n=c/n\) and contrasting one-card total-variation versus chi-square mixing times. Jonasson (2006) and Pemantle (1989) concern fixed-parameter full-deck shuffling and do not state this joint limiting one-card result in the identified material. An unlocated equivalent asymptotic formulation remains a priority risk.

## Limitations

This is not a full-deck mixing theorem, a sharp total-variation mixing-time constant, an entropy asymptotic, or a result uniform when \(c\) varies with \(n\). Finite numerical verification alone cannot establish an infinite-domain window. The discrete-time window admits lattice effects.

## References

1. Y. Jiang, *Cutoff for the Overhand Shuffle*, arXiv:2610.00137v1 (2026), Section 3.2, Proposition 3.2. https://arxiv.org/abs/2610.00137
2. J. Jonasson, *The overhand shuffle mixes in* \(\Theta(n^2\log n)\) *steps*, Ann. Appl. Probab. **16** (2006), 231–243, DOI 10.1214/105051605000000692. https://arxiv.org/abs/math/0501401
3. R. Pemantle, *Randomization time for the overhand shuffle*, J. Theoret. Probab. **2** (1989), 37–49, DOI 10.1007/BF01048267.
