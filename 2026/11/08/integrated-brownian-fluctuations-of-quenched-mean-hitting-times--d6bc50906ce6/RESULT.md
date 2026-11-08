# Integrated-Brownian fluctuations of quenched mean hitting times in Bernoulli recursive comb trees

## Finding
Let the Bernoulli recursive tree be defined below with fixed \(0<p<1\), \(q=1-p\), and let \(\sigma_0=0<\sigma_1<\cdots\) be the birth indices along its unique infinite ray. For simple random walk on the realized infinite tree, started at \(v_0\), write
\[
\mathcal H_m=\mathbf E^{T}_{v_0}\!\left[\inf\{t\ge0:X_t=v_{\sigma_m}\}\right],\qquad m\ge1.
\]
Here \(\mathbf E^T\) averages only the walk, with the tree fixed. Under the tree law, as \(m\to\infty\),
\[
\left(\frac{\mathcal H_{\lfloor mt\rfloor}-(1+q)m^2t^2}{m^{3/2}}\right)_{0\le t\le1}
\Longrightarrow\left(2\sqrt{pq}\int_0^t B(s)\,ds\right)_{0\le t\le1}
\]
in \(D([0,1])\) with the Skorokhod topology, where \(B\) is standard Brownian motion. In particular,
\[
\frac{\mathcal H_m-(1+q)m^2}{m^{3/2}}\Longrightarrow N\!\left(0,\frac{4pq}{3}\right),\qquad
\frac{\mathcal H_m}{m^2}\longrightarrow1+q\quad\text{almost surely}.
\]
The Gaussian limit describes randomness of the **quenched mean**, not the additional fluctuations of individual random-walk hitting times.

## Assumptions and scope
The initial tree has vertices \(v_0,v_1\) joined by an edge. Fix independent Bernoulli variables \(b_j\), \(j\ge1\), with \(\Pr(b_j=1)=p\), and put \(b_0=1\). For \(j\ge1\), add \(v_{j+1}\) with parent \(v_j\) if \(b_j=1\), or parent \(v_{j-1}\) if \(b_j=0\). The infinite union is locally finite. As \(p>0\), successes occur infinitely often, and the tree is almost surely one-ended. All statements concern fixed \(p\in(0,1)\) and the tree-environment law; no uniformity at \(p=0\) is claimed. The infinite ray is well defined and its successive vertices are enumerated by increasing birth index.

## Proof
**1. Exact regenerative geometry.** Enumerate the success indices \(0=j_0<j_1<j_2<\cdots\) at which \(b_j=1\). The gaps \(K_r=j_{r+1}-j_r-1\) are independent, with \(\Pr(K_r=k)=p q^k\), \(k\ge0\). Between successive success indices, all parent edges after the first split jump backward by two birth labels; there are precisely two parity chains. The one reaching \(v_{j_{r+1}}\) is the unique continuing ray; the other is a finite tooth rooted at \(v_{j_r}\). The continuing ray advances
\[
H_r=\lfloor K_r/2\rfloor+1
\]
edges, and the tooth has
\[
A_r=\lceil K_r/2\rceil
\]
edges. Every other ray vertex within the block has zero tooth length. Consequently these pairs \((H_r,A_r)\) are i.i.d. This is an exact joint description, not an independence assumption on successive tooth lengths. For any \(m\ge0\), let \(L_i\) denote the full number of tooth edges attached to ray vertex \(v_{\sigma_i}\) and define \(C_m=\sum_{i=0}^{m-1}L_i\), \(C_0=0\). The process \(C_m\) is the renewal reward with block length \(H_r\), block reward \(A_r\) placed at the first site of the block.

**2. Exact centered reward variance.** Put \(z=q^2\). Geometric-series identities give
\[
\mathbf E H_r=\frac1{p(1+q)},\qquad
\mathbf E A_r=\frac q{p(1+q)},\qquad
\mathbf E(A_r-qH_r)=0.
\]
When \(K_r=2\ell\), the centered reward \(D_r=A_r-qH_r\) equals \(p\ell-q\); when \(K_r=2\ell+1\), it equals \(p(\ell+1)\). Inserting \(\sum_{\ell\ge0}z^\ell=(1-z)^{-1}\), \(\sum \ell z^\ell=z(1-z)^{-2}\) and \(\sum \ell^2z^\ell=z(1+z)(1-z)^{-3}\) yields
\[
\mathbf E D_r^2=\frac q{1+q},\qquad
\frac{\mathbf E D_r^2}{\mathbf E H_r}=pq.
\]
Both block length and reward have exponential tails. Donsker's theorem for the i.i.d. \(D_r\), the renewal law \(\max\{r:\sum_{i<r}H_i\le mt\}/m\to t/\mathbf E H_r\) uniformly on compact time intervals, and the random-time-change theorem imply
\[
\left(\frac{C_{\lfloor mt\rfloor}-q\lfloor mt\rfloor}{\sqrt m}\right)_{0\le t\le1}
\Longrightarrow \bigl(\sqrt{pq}\,B(t)\bigr)_{0\le t\le1}.
\]
Indeed, a partial block contributes at most \(A_r+qH_r\); the maximum over the \(O(m)\) blocks encountered by time \(m\) is \(O_{\Pr}(\log m)=o_{\Pr}(\sqrt m)\). The renewal-reward strong law also gives \(C_m/m\to q\) almost surely.

**3. Exact walk hitting-time identity.** Cut the ray edge from ray vertex \(i\) to \(i+1\). Its root-side component has exactly \(i+\sum_{j=0}^iL_j\) edges. By elementary first-step equations for simple walk on a finite tree, the mean duration to cross this edge from its root-side endpoint is twice that number plus one. Adding successive crossings gives, identically for every realization and every \(m\ge1\),
\[
\mathcal H_m=m^2+2\sum_{j=0}^{m-1}(m-j)L_j=m^2+2\sum_{h=1}^m C_h.
\]
For completeness, the edge-crossing identity follows by induction on the finite root-side component: an excursion into a neighboring subtree of \(e\) edges has mean duration \(2e+2\) including return, and the geometric number of such excursions before the desired edge is taken gives \(2e_{\rm left}+1\).

**4. Functional limit and almost-sure normalization.** For \(k=\lfloor mt\rfloor\), substitute \(C_h=qh+(C_h-qh)\) into the last display:
\[
\mathcal H_k=(1+q)k^2+qk+2\sum_{h=1}^k(C_h-qh).
\]
After division by \(m^{3/2}\), the \(qk\) term and replacing \(k^2\) by \(m^2t^2\) vanish uniformly. The previous functional central limit theorem and continuity of time integration give the asserted integrated-Brownian limit. At \(t=1\), \(\operatorname{Var}(\int_0^1B(s)\,ds)=1/3\). Cesàro summation of the strong law for \(C_h\) gives \(\mathcal H_m/m^2\to1+q\) almost surely.

## Verification
The accompanying standard-library script `verification.py` exhaustively enumerates small birth-bit patterns, constructs the resulting finite trees, checks each completed regenerative block, solves rational first-step hitting-time systems and compares with the exact edge-cut formula. It also verifies the closed rational reward-variance identity and runs a seeded finite simulation as a diagnostic. Execute `python3 verification.py`. These finite checks do not establish the functional limit; the preceding proof does.

## Relationship to prior work
Tang, Wang and Wu (2026) introduced the Bernoulli last-or-second-last recursive tree and proved its one-endedness and infinite-collision property; their question is qualitative recurrence/collision. Georgakopoulos and Wagner give general tree hitting-time identities. Janson provides a central limit theorem for general regenerative-increment processes. Gantert and Klenke examine a different random spanning-tree comb and a quenched invariance principle for the **walk**. The result here concerns a different object: the random-environment fluctuations of the **conditional mean** hitting time along the Bernoulli tree's infinite ray. The necessary joint block-length/tooth-reward decomposition and its simplified variance coefficient are supplied explicitly; the standard general facts alone do not identify that coefficient for this model.

## Limitations
The theorem is not a limit theorem for the random hitting time itself, for total-variation mixing, or for the finite-volume Kemeny constant. It does not describe a parameter regime where \(p\) varies with \(m\). The numerical checker is finite and is not an exhaustive verification of any infinite limit. The result is subject to historical-priority and independent mathematical review.

## References
- J.-s. Tang, F. Wang, X.-Y. Wu, *Infinite collisions of simple random walks on random recursive trees generated by Bernoulli sequences*, arXiv:2607.02916v1, 2026-07-03, https://arxiv.org/html/2607.02916.
- A. Georgakopoulos and S. Wagner, *Hitting Times, Cover Cost, and the Wiener Index of a Tree*, arXiv:1302.3212, 2013, https://arxiv.org/abs/1302.3212.
- S. Janson, *On a central limit theorem in renewal theory*, arXiv:2305.13229, 2023, https://arxiv.org/abs/2305.13229.
- N. Gantert and A. Klenke, *Biased Random Walk on Spanning Trees of the Ladder Graph*, Journal of Statistical Physics 190, 83 (2023), https://doi.org/10.1007/s10955-023-03091-w.
