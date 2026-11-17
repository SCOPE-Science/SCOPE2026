# Almost-sure stabilization of receptive edges in adaptive-confidence Deffuant–Weisbuch dynamics

## Finding

**Theorem (finite-time stabilization of the effective graph).** On any finite, fixed, undirected simple graph with at least one edge, run the asynchronous adaptive-dyadic-confidence Deffuant–Weisbuch process defined below. With probability one, there is a finite random time \(T\) such that the effective graph \(G_{\mathrm{eff}}(t)\) equals \(G_{\mathrm{eff}}(T)\) for all integer times \(t\ge T\). For every original edge \(e\), almost surely,

\[
 e\in E_{\mathrm{eff}}(T)\quad\Longleftrightarrow\quad \lim_{t\to\infty}c_e(t)=1,
 \qquad e\notin E_{\mathrm{eff}}(T)\quad\Longleftrightarrow\quad\lim_{t\to\infty}c_e(t)=0.
\]

Moreover, both endpoints of every edge retained in the eventual effective graph have the same limiting opinion. Endpoints with the same limiting opinion are **not** asserted to retain their edge. The conclusion includes the parameter boundaries \(\gamma=1\), \(\delta=0\), and \(\mu=1/2\).

## Assumptions and scope

Fix a finite simple undirected graph \(G=(V,E)\) with \(m=|E|\ge1\), arbitrary initial opinions \(x_i(0)\in[0,1]\), and equal initial dyadic confidences \(c_e(0)=c_0\in(0,1)\). Fix \(\mu\in(0,1/2]\), \(\gamma\in(0,1]\), and \(\delta\in[0,1)\). At the beginning of each discrete time \(t\ge0\), select one edge \(J_t\) independently and uniformly from \(E\). Write \(J_t=\{i,j\}\). Define its *preselection* receptive indicator as

\[
 A_e(t)=\mathbf 1\big\{|x_i(t)-x_j(t)|<c_e(t)\big\},\qquad
 E_{\mathrm{eff}}(t)=\{e\in E:A_e(t)=1\}.
\]

For the selected pair, if \(A_{J_t}(t)=1\), set

\[
 x_i(t+1)=(1-\mu)x_i(t)+\mu x_j(t),\quad
 x_j(t+1)=\mu x_i(t)+(1-\mu)x_j(t),\quad
 c_{J_t}(t+1)=c_{J_t}(t)+\gamma(1-c_{J_t}(t)).
\]

Otherwise leave their opinions unchanged and set \(c_{J_t}(t+1)=\delta c_{J_t}(t)\). All other opinions and confidences remain unchanged. Receptiveness is checked **before** the random selection at that time, so \(A_e(t)\) is measurable with respect to the past and independent of \(J_t\). Every statement is almost sure with respect to edge selections, conditional on any fixed initial opinion profile. Isolated vertices are allowed.

We use two established facts from Li–Luo–Porter's adaptive-confidence model (Theorem 3.8 and the subsequent effective-graph theorem in the 2025 article; Theorems 5 and 6 in arXiv v3): (i) every opinion has a limit and each \(c_e(t)\) converges almost surely to a member of \(\{0,1\}\); (ii) if an edge's endpoint opinion limits differ, its confidence limit is zero. These prior results are **not** claimed here as new.

## Proof

**Step 1: predictable-opportunity sampling lemma.** Let \(J_t\) be independent uniform draws from a finite set \(E\) of size \(m\), and let \(A_e(t)\in\{0,1\}\) be any indicator measurable before the draw at time \(t\). Then

\[
 \Pr\big(A_e(t)=1\text{ infinitely often but }J_t=e,\ A_e(t)=1
 \text{ only finitely often}\big)=0.
\]

To establish it, fix a deterministic integer \(s\ge0\) and list, if they exist, the first \(k\) receptive opportunities for \(e\) at or after \(s\) as \(\tau_1<\cdots<\tau_k\). Each \(\tau_j\) is a predictable selection opportunity: \(A_e(\tau_j)\) has been decided from the history before drawing \(J_{\tau_j}\). Conditioned on that history, the probability of missing \(e\) is exactly \(1-1/m\). Inductively,

\[
 \Pr\big(\tau_k<\infty,\ J_{\tau_j}\ne e\text{ for all }1\le j\le k\big)
 \le (1-1/m)^k.
\]

Indeed, the event of an unsuccessful first \(k\) opportunities is contained in the event of an unsuccessful first \(k-1\) opportunities, and conditioning at the last opportunity contributes exactly the factor \(1-1/m\). Sending \(k\to\infty\) proves that the probability of infinitely many receptive opportunities after \(s\) with no receptive selection after \(s\) is zero. If there are infinitely many receptive times but only finitely many receptive selections, there is some deterministic integer \(s\) after the last such selection. A countable union over \(s\) gives the lemma. This is the conditional Borel–Cantelli principle in a form that explicitly permits the receptive status to depend on all earlier selections.

**Step 2: edges with zero confidence limit disappear permanently.** Work on the probability-one event on which all edge confidence limits exist and belong to \(\{0,1\}\) and the sampling lemma holds for all finitely many edges. Fix \(e\in E\) with \(c_e(t)\to0\). Choose a finite time \(t_0\) after which \(c_e(t)<\gamma/2\). If \(J_t=e\) and \(A_e(t)=1\) at any \(t\ge t_0\), its confidence update would satisfy

\[
 c_e(t+1)=c_e(t)+\gamma(1-c_e(t))\ge\gamma,
\]

contradicting \(c_e(t+1)<\gamma/2\). Thus there are no receptive selections after \(t_0\). By Step 1, the set of times \(t\) with \(A_e(t)=1\) must be finite. Hence \(A_e(t)=0\) at all sufficiently large times.

**Step 3: edges with unit confidence limit remain permanently.** Fix \(e=\{i,j\}\) with \(c_e(t)\to1\). The cited prior theorems show that the opinion limits exist and, because different endpoint opinion limits would imply \(c_e(t)\to0\), they must be equal. Therefore \(|x_i(t)-x_j(t)|\to0\). For all sufficiently large \(t\), \(c_e(t)>1/2\) and \(|x_i(t)-x_j(t)|<1/2\), so \(A_e(t)=1\).

**Step 4: a simultaneous finite stabilization time.** Each of the finitely many edges belongs to exactly one of the cases in Steps 2 and 3 almost surely. Let \(T\) be the maximum of their finite stabilization times. For every \(t\ge T\), the receptive set is exactly the set of edges whose confidence limit equals one; this proves all assertions. \(\square\)

## Verification

The crucial probabilistic step is conditioned on the pre-draw information. The explicit \((1-1/m)^k\) bound remains valid even if receptiveness switches arbitrarily as a function of earlier edge selections. The proof uses no enumeration, numerical approximation, stationarity assumption, or claim that an edge is always receptive merely because both endpoints have the same limit. The contradiction for zero confidence works even at \(\gamma=1\), \(\delta=0\), and \(m=1\). Since \(\gamma>0\) is necessary for a positive upward jump, no assertion is made about \(\gamma=0\) under these arguments. Since the cited zero–one confidence theorem assumes \(\delta<1\), the case \(\delta=1\) is likewise not claimed.

For a direct checker of the finite-step update and the exact sampling bound, see the accompanying standalone \(\texttt{verify.py}\). These finite checks do not certify almost-sure behavior; the proof above does.

## Relationship to prior work

Li, Luo, and Porter introduced the adaptive-dyadic-confidence model and proved almost-sure convergence of opinions and confidence bounds, as well as eventual exclusion of effective edges across different limiting opinion clusters. The arXiv v3 discussion in Section 6.2 and Appendix A.2, and the 2025 journal article's corresponding appendix, explicitly leave eventual constancy of the asynchronous model's effective graph unresolved, because an edge can become receptive between two of its selection times. The present theorem resolves that precise stochastic stabilization question by applying a predictable-opportunity sampling argument to the already-established zero–one confidence limits. Their synchronous HK effective-graph theorem and baseline fixed-confidence DW theorem concern different dynamics and do not themselves state the asynchronous adaptive-confidence conclusion.

Thompsky and collaborators' 2026 model adapts *interaction probabilities* while holding the confidence threshold fixed, rather than adapting the dyadic confidence threshold under uniform selection, so its effective-graph arguments do not cover this claim. Collins and collaborators' 2023 report uses opinion-dependent *per-agent* confidence functions and potentially asymmetric updates, not the per-edge updating rule studied here. These distinctions matter to both the theorem statement and the proof.

## Limitations

The result asserts almost-sure eventual constancy, not a deterministic bound, moment bound, or computable tail for the stabilization time. It does not identify the distribution of the retained graph or show that all edges joining equal-limit opinion vertices survive. Its correctness relies on the cited, previously proved opinion/conﬁdence convergence results for this exact model; an independent proof of those results is not reproduced. The conditional sampling step depends on the selected edge retaining a strictly positive probability at each receptive opportunity and on receptiveness being determined before selection. Results for rewired graphs, adaptive edge-selection probabilities without a uniform positive lower bound, infinite networks, or the parameter boundaries excluded above are outside scope.

## References

1. G. J. Li, J. Luo, and M. A. Porter, *Bounded-Confidence Models of Opinion Dynamics with Adaptive Confidence Bounds*, arXiv:2303.07563 (first public version 2023-03-14; HTML v3 2024-07-27), https://arxiv.org/html/2303.07563v3 ; *SIAM Journal on Applied Dynamical Systems* 24 (2025), 994–1041, https://doi.org/10.1137/23M1558951 . In particular, Theorems 3.8 and 3.11 and the later effective-graph discussion in the published version, corresponding to arXiv-v3 Theorems 5–6 and Appendix A.2.
2. L. Thompsky and collaborators, *A Bounded-Confidence Model of Opinion Dynamics with Adaptive Interaction Probabilities*, arXiv:2605.20418 (2026), https://arxiv.org/abs/2605.20418 .
3. M. Collins, Z. Gong, A. Ogranovich, and N. White, *A Deffuant–Weisbuch Model of Opinion Dynamics with Adaptive Confidence Bounds*, 2023 technical report, https://ww3.math.ucla.edu/wp-content/uploads/2023/10/CAMREU2023-FinalReport-1.pdf .
