# A post-SDPI family of orthogonal relay-channel counterexamples

## Result

Let \(W_1:\{0,1\}\to\mathcal Y_r\) and \(W_2:\{0,1\}\to\mathcal Z\) be binary-input discrete memoryless channels with capacities \(C_1\) and \(C_2\), respectively. Define the input-free post-processing contraction coefficient
\[
\eta_{\rm post}(W_1)
:=\sup \frac{I(A;U)}{I(Y;U)},
\]
where the supremum is over all input laws \(P_A\) and all post-processing channels \(P_{U|Y}\) such that \(A\to Y\to U\), \(Y\sim W_1(\cdot|A)\), and \(I(Y;U)>0\). Write \(\eta=\eta_{\rm post}(W_1)\).

Consider the relay channel with source input \(X_s=(A,B)\in\{0,1\}^2\), relay input \(X_r\in\{0,1\}\), relay output \(Y_r\sim W_1(\cdot|A)\), and destination output
\[
Y_d=(B,Z),\qquad Z\sim W_2(\cdot|X_r),
\]
with transition law
\[
p(y_r,b',z|a,b,x_r)
=\mathbf 1\{b'=b\}W_1(y_r|a)W_2(z|x_r).
\]
Then:

1. The relay-channel capacity is exactly
   \[
   C=1+\min\{C_1,C_2\}.
   \]
2. For the three-rate expression proposed in Ponniah, arXiv:2609.15709, namely the maximum of its decode-forward, uncoordinated compress-forward, and coordinated compress-forward terms, denoted here by \(C_{\rm prop}\),
   \[
   C_{\rm prop}\le 1+\eta C_2.
   \]
3. Consequently, whenever
   \[
   \min\{C_1,C_2\}>\eta C_2,
   \]
   the proposed characterization is strictly below capacity, with certified gap
   \[
   C-C_{\rm prop}\ge \min\{C_1,C_2\}-\eta C_2>0.
   \]

This turns the isolated numerical counterexample of Shiu, arXiv:2609.18727, into a channel-family criterion: the same obstruction occurs whenever the source-to-relay channel contracts post-processed information sufficiently strongly relative to the relay-to-destination bottleneck.

## Proof

### Exact capacity

Achievability is by a standard partial-decode-forward/block-Markov pipeline. The source sends one bit per use directly through the noiseless \(B\) coordinate. Independently, it sends another sub-message through \(W_1\) at any rate below \(C_1\); the relay decodes that sub-message and forwards it through \(W_2\) in the next block at any rate below \(C_2\). Pipelining makes the initialization and termination overhead vanish. Hence every rate below
\[
1+\min\{C_1,C_2\}
\]
is achievable.

For the cutset bound, for every joint input law \(P_{A,B,X_r}\), the source-side cut satisfies
\[
\begin{aligned}
I(A,B;Y_r,B,Z\mid X_r)
&=I(A,B;Y_r,B\mid X_r)\\
&=H(B\mid X_r)+I(A;Y_r\mid B,X_r)\\
&\le 1+C_1.
\end{aligned}
\]
The last inequality holds because for every conditioning value \((b,x_r)\), the induced input law on \(A\) is merely some input distribution for \(W_1\), and its mutual information is at most the channel capacity \(C_1\).

The destination-side cut satisfies
\[
\begin{aligned}
I(A,B,X_r;B,Z)
&=H(B)+I(X_r;Z\mid B)\\
&\le 1+C_2,
\end{aligned}
\]
because \(Z\) is conditionally independent of \(A\) given \(X_r\), and each conditional input law on \(X_r\) yields mutual information at most \(C_2\). Therefore
\[
C\le 1+\min\{C_1,C_2\},
\]
which matches achievability. This channel is a particularly simple member of the relay channels with orthogonal sender components whose capacity was characterized by El Gamal and Zahedi (2005).

### Decode-forward term

The decode-forward expression contains the source-to-relay term
\[
I(A,B;Y_r\mid X_r)=I(A;Y_r\mid X_r)\le C_1.
\]
Therefore
\[
R_{\rm DF}\le C_1\le 1.
\]

### Both compress-forward terms

Shiu's counterexample proof upper-bounds both proposed compress-forward terms by enlarging their feasible sets to a common optimization. The same reduction uses only the factorization of the relay channel and therefore applies verbatim with \(W_{1/4}\) replaced by \(W_1\) and \(W_2\). For any distribution in that relaxed feasible set, the objective is
\[
J=H(B\mid X_r)+I(A;\widehat Y_r\mid B,X_r),
\]
while feasibility implies
\[
I(\widehat Y_r;Y_r\mid B,X_r)
\le I(X_r;B,Z).
\]
Conditioned on any \((B,X_r)=(b,x_r)\) of positive probability,
\[
A\to Y_r\to\widehat Y_r
\]
is a Markov chain whose first channel is \(W_1\). By the definition of \(\eta\), averaging the conditional post-SDPI gives
\[
I(A;\widehat Y_r\mid B,X_r)
\le \eta I(Y_r;\widehat Y_r\mid B,X_r).
\]
Hence
\[
\begin{aligned}
J
&\le H(B\mid X_r)+\eta I(X_r;B,Z)\\
&=H(B)-(1-\eta)I(B;X_r)+\eta I(X_r;Z\mid B)\\
&\le 1+\eta C_2.
\end{aligned}
\]
Thus both proposed compress-forward terms are at most \(1+\eta C_2\). Since \(C_1\le1\) for a binary-input channel and \(1+\eta C_2\ge1\), the maximum of the three proposed rates obeys
\[
C_{\rm prop}\le1+\eta C_2.
\]
This proves the criterion.

## Binary-symmetric continuum

Take
\[
W_i=\operatorname{BSC}(\delta_i),\qquad 0\le\delta_i\le\tfrac12.
\]
Then
\[
C_i=1-h_2(\delta_i),
\qquad
\eta=(1-2\delta_1)^2,
\]
where the post-processing coefficient is the BSC value used in Shiu's proof.

Therefore
\[
C=1+\min\{1-h_2(\delta_1),1-h_2(\delta_2)\},
\]
and
\[
C_{\rm prop}
\le
1+(1-2\delta_1)^2\bigl(1-h_2(\delta_2)\bigr).
\]
In particular, throughout the entire wedge
\[
0<\delta_1\le\delta_2<\tfrac12,
\]
we have \(C_2\le C_1\), so
\[
\boxed{
C-C_{\rm prop}
\ge
4\delta_1(1-\delta_1)\bigl(1-h_2(\delta_2)\bigr)>0.
}
\]
Thus every nondegenerate symmetric choice
\[
\delta_1=\delta_2=\delta\in(0,\tfrac12)
\]
is a counterexample, not only \(\delta=1/4\).

For \(\delta=1/4\), this recovers Shiu's values
\[
C=1.1887218755\ldots,
\qquad
C_{\rm prop}\le1.0471804689\ldots,
\]
with gap at least \(0.1415414067\ldots\) bits/use. A simple alternative point, \(\delta=1/8\), gives
\[
C=1.4564355568\ldots,
\qquad
C_{\rm prop}\le1.2567450007\ldots,
\]
and hence the larger certified gap
\[
C-C_{\rm prop}\ge0.1996905561\ldots
\]
bits/use.

## Significance

The main point is structural rather than numerical. The exact capacity of this orthogonal relay family is controlled by the smaller point-to-point capacity \(\min(C_1,C_2)\), because the relay can decode and forward only the part of the message routed through \(A\). The proposed compress-forward characterization, after Shiu's relaxation, can exploit the source-to-relay observation only through a post-processed auxiliary; the post-SDPI coefficient contracts that contribution by \(\eta\). Whenever
\[
\min(C_1,C_2)>\eta C_2,
\]
this contraction forces a strict separation. The failure is therefore not tied to the special crossover probability \(1/4\), but persists on an open family of channels and, for BSC links, on an explicit two-parameter region.

## Verification

`artifacts/verify_bsc_family.py` evaluates the closed-form BSC capacity and proposed-rate upper bound at representative points and verifies the wedge identity and strict inequality on a finite grid. `artifacts/verification.txt` records its output. These computations are sanity checks only; the general theorem is proved above.

## Limitations

The theorem concerns the particular three-rate capacity expression proposed in arXiv:2609.15709 and upper-bounded by the relaxation used in arXiv:2609.18727. It does not claim that compress-forward in general is bounded by \(1+\eta C_2\), nor does it characterize all relay channels on which the proposed expression fails. The condition \(\min(C_1,C_2)>\eta C_2\) is sufficient, not asserted necessary.

The exact capacity formula itself is not claimed as new: it is a direct specialization of known orthogonal-sender relay-channel capacity results and also follows from the elementary cutset argument above. The novelty claim is restricted to the post-SDPI family criterion, its propagation through the proposed three-rate expression, and the resulting continuum of explicit counterexamples.

Originality is asserted only to the best of our knowledge. The motivating counterexample preprint is very recent, so a near-simultaneous note or subsequent revision may independently contain the same generalization.

## References

1. C. H. M. Shiu, "Counterexample to a Proposed Capacity Characterization of the Relay Channel," arXiv:2609.18727, 2026. https://arxiv.org/abs/2609.18727
2. J. Ponniah, "The Capacity of the Relay Channel," arXiv:2609.15709, 2026. https://arxiv.org/abs/2609.15709
3. A. El Gamal and S. Zahedi, "Capacity of a Class of Relay Channels With Orthogonal Components," IEEE Transactions on Information Theory 51(5), 1815--1817, 2005. https://doi.org/10.1109/TIT.2005.846438
4. Y. Polyanskiy and Y. Wu, *Information Theory: From Coding to Learning*, Cambridge University Press, 2025. The post-processing SDPI and BSC coefficient are used through the formulation cited by Shiu.
