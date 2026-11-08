# Sparse-cut overhand shuffles: a total-variation and chi-square separation

## Finding
For a fixed \(c>0\) consider \(n\) cards, \(n>c\), and cut each of the \(n-1\) gaps independently with probability \(p_n=c/n\). Reverse each resulting contiguous packet in place. Let \(K_n\) be the Markov transition matrix of the position of one distinguished card, and \(U_n\) the uniform law on \(\{1,\ldots,n\}\). Set \(q_n=1-c/n\) and \(\delta_n=cq_n^{n-1}\).

**Theorem.** For all integers \(n>c\), all positions \(i,j\), and all integer \(t\ge0\),
\[
 K_n(i,j)\ge\frac{\delta_n}{n},\qquad
 \sup_i\|K_n^t(i,\cdot)-U_n\|_{\rm TV}\le(1-\delta_n)^t,\qquad
 \inf_i\|K_n^t(i,\cdot)-U_n\|_{\rm TV}\ge q_n^{(n-1)t}-\frac1n.
\]
For every fixed \(C>0\), as \(n\to\infty\),
\[
\sup_{\substack{t\in\mathbb Z_{\ge0}\\|t-(\log n)/(2c)|\le C}}
\sup_{1\le i\le n}
\left|\chi^2(K_n^t(i,\cdot)\|U_n)-n e^{-2ct}\right|\longrightarrow0.
\]
In particular, for each \(\varepsilon\in(0,1)\) the tagged-card total-variation mixing times stay bounded as \(n\to\infty\), while for every \(\eta>0\) the worst-start \(\chi^2\)-mixing time equals \((\log n)/(2c)+O_{c,\eta}(1)\). The limiting \(\chi^2\) window is discrete; no convergence under arbitrary floor centering is asserted.

## Assumptions and scope
The packet-reversal convention reverses cards *inside* each packet and does not reorder packets. Initial position is deterministic and arbitrary. Time is measured in complete independent shuffle passes. For probability measures \(\nu\) and \(\pi\) on the positions,
\[
\|\nu-\pi\|_{\rm TV}=\tfrac12\sum_j|\nu(j)-\pi(j)|,\qquad
\chi^2(\nu\|\pi)=\sum_j\frac{(\nu(j)-\pi(j))^2}{\pi(j)}.
\]
The theorem is about the one-card marginal, not the permutation-valued full-deck chain. The limit holds for each fixed positive \(c\); its constants are not uniform in \(c\).

## Proof
**1. Exact minorization.** At position \(i\), let \(L\) and \(R\) be the numbers of positions to the left and right, respectively, inside the card's packet. Since gaps are independently cut,
\[
 L\overset d=\min(G_L,i-1),\quad R\overset d=\min(G_R,n-i),\quad
 \Pr(G_L=r)=\Pr(G_R=r)=p_n q_n^r,
\]
with independent geometric variables, and the new position is \(i+R-L\). For prescribed \(i,j\), choose \(L=\min(i-1,n-j)\) and \(R=j-i+L\). These are nonnegative and within their permitted ranges; either \(L=i-1\) or \(R=n-i\), so at least one of the two corresponding geometric probabilities is the endpoint mass \(q_n^r\) rather than \(p_nq_n^r\). Their product is at least \(p_nq_n^{L+R}\ge p_nq_n^{n-1}\). Every packet reversal is an involution, so \(K_n\) is symmetric and \(U_n\) is invariant. The entrywise bound gives \(K_n\ge\delta_n\Pi_n\), where \(\Pi_n\) is the uniform-row kernel, yielding the stated Doeblin total-variation bound by iteration. If all \(n-1\) gaps are uncut during each of \(t\) passes, the card is at the deterministic full-reversal image of its original position; this event has probability \(q_n^{(n-1)t}\). A single-atom test yields the lower bound. In particular, \(\delta_n\to ce^{-c}>0\).

**2. An exact spectral representation.** The finite-deck diagonalization in Jiang, Proposition 3.2, gives the complete cosine basis
\[
 f_{n,k}(i)=\cos\left(\frac{k\pi(i-1/2)}{n}\right),\quad
 \ell_{n,k}=2\left(1-\cos\frac{k\pi}{n}\right),\quad
 \lambda_{n,k}=\frac{p_n^2+(-1)^kq_n^{n+1}\ell_{n,k}}{p_n^2+q_n\ell_{n,k}}
\]
for \(0\le k<n\). The constant mode has eigenvalue one; nonconstant cosine modes are orthogonal in \(L^2(U_n)\) and have squared norm \(1/2\). By reversibility and Parseval, for any \(t\ge0\),
\[
 \chi^2(K_n^t(i,\cdot)\|U_n)
 =2\sum_{k=1}^{n-1}f_{n,k}(i)^2\lambda_{n,k}^{2t},\qquad
 2\sum_{k=1}^{n-1}f_{n,k}(i)^2=n-1.
\]
The eigenvalues and orthogonality are prior inputs, not asserted to be newly discovered.

**3. Uniform separation of the low modes.** Write \(a_n=q_n^{n+1}\to e^{-c}\). For all large \(n\), \(q_n>a_n\), and
\[
 |\lambda_{n,k}|\le\frac{p_n^2+a_n\ell_{n,k}}{p_n^2+q_n\ell_{n,k}}.
\]
The right side decreases in \(\ell_{n,k}\). Since \(n^2p_n^2=c^2\) and \(n^2\ell_{n,1}\to\pi^2\), its maximum converges to
\[
 r_*(c)=\frac{c^2+e^{-c}\pi^2}{c^2+\pi^2}<1.
\]
Choose a fixed \(r\in(r_*(c),1)\), then for large \(n\) all nonconstant modes satisfy \(|\lambda_{n,k}|\le r\). Choose \(\alpha\in(0,1)\) with \(\alpha<-\log r/c\). If \(t=(\log n)/(2c)+O(1)\), the combined contribution of \(k\le n^\alpha\) to the above Parseval sum is at most \(2n^\alpha r^{2t}=o(1)\), uniformly in the starting position.

**4. A common bulk decay and the window.** For \(k>n^\alpha\), the inequality \(\ell_{n,k}=4\sin^2(k\pi/(2n))\ge4k^2/n^2\), together with the exact eigenvalue expression, gives
\[
 \lambda_{n,k}-(-1)^k a_n
 =\frac{p_n^2(1-(-1)^ka_n)}{p_n^2+q_n\ell_{n,k}}
 =O_c(k^{-2}).
\]
Since \(a_n\to e^{-c}>0\), it follows uniformly in these modes that
\[
 \lambda_{n,k}^{2t}=a_n^{2t}\left[1+O_c\left(\frac{\log n}{n^{2\alpha}}\right)\right].
\]
The error remains \(o(1)\) when summed against the cosine weights because \(n a_n^{2t}=O_c(1)\). The omitted cosine weights total at most \(2n^\alpha\), and hence the full sum is \(n a_n^{2t}+o(1)\), uniformly in \(i,t\) in the stated window. Finally \(\log a_n=-c+O_c(n^{-1})\), so \(na_n^{2t}=ne^{-2ct}+o(1)\). This proves the window formula. Monotonicity of \(\chi^2\) under a Markov transition and the window profile place its fixed-threshold mixing time within a bounded distance of \((\log n)/(2c)\).

## Verification
A standalone program \(\texttt{verify.py}\) independently builds the tagged-card kernel from truncated geometric packet lengths for several finite decks, compares each cosine mode to the exact transition action, checks entrywise minorization and stochasticity, and evaluates the \(\chi^2\) spectral formula at increasing sizes. It checks finite identities and illustrative convergence only. The proof above, including the uniform low/bulk decomposition, establishes the infinite limit.

## Relationship to prior work
Jiang, *Cutoff for the Overhand Shuffle*, arXiv:2610.00137v1 (2026), studies the entire permutation-valued chain at a **fixed** cut probability and proves full-deck total-variation and entropy cutoff on the diffusive scale. Proposition 3.2 supplies the exact one-card eigenvalues for arbitrary finite decks. The new result uses that formula as an input and studies a different singular regime \(p_n=c/n\), distinguishing the one-card total-variation and \(\chi^2\) scales. Jonasson (2006) and Pemantle (1989) address fixed-parameter full-deck mixing, not this joint vanishing-cut, growing-deck marginal asymptotic. The exact spectral formula does imply each finite-deck \(\chi^2\) value; what is established here beyond that input is the uniform time-window asymptotic and the contrasting Doeblin bound.

## Limitations
The result makes no assertion about full-deck mixing, optimal constants for the tagged-card total-variation mixing time, relative-entropy asymptotics, or regimes in which \(c\) varies with \(n\). The discrete-time \(\chi^2\) profile has lattice effects, so centering by an integer floor need not produce a single limit as \(n\) ranges over all integers. Historical priority for equivalent spectral-limit formulations is not independently certified.

## References
1. Y. Jiang, *Cutoff for the Overhand Shuffle*, arXiv:2610.00137v1, first public version September 10, 2026, Section 3.2, Proposition 3.2. https://arxiv.org/html/2610.00137v1
2. J. Jonasson, *The overhand shuffle mixes in* \(\Theta(n^2\log n)\) *steps*, Ann. Appl. Probab. **16** (2006), 231–243, DOI 10.1214/105051605000000692. https://arxiv.org/abs/math/0501401
3. R. Pemantle, *Randomization time for the overhand shuffle*, J. Theoret. Probab. **2** (1989), 37–49. DOI 10.1007/BF01048267.
