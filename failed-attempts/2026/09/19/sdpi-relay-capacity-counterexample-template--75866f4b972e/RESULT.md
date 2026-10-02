# SDPI template for robust counterexamples to a proposed relay-capacity characterization

## Result

Consider two discrete memoryless channels
\[
W_1:\mathcal A\to\mathcal Y_r,\qquad
W_2:\mathcal X_r\to\mathcal Z
\]
with Shannon capacities \(C_1\) and \(C_2\), respectively. Let \(\mathcal B\) be a finite alphabet of size \(M\), and write
\[
D=\log_2 M.
\]
Form the relay channel with source input \(X_s=(A,B)\), relay input \(X_r\), relay output
\[
Y_r\sim W_1(\cdot\mid A),
\]
and destination output
\[
Y_d=(B,Z),\qquad Z\sim W_2(\cdot\mid X_r),
\]
where the two component channels are conditionally independent given the inputs.

Define the input-free post-processing contraction coefficient
\[
\eta_{\rm post}(W_1)
=
\sup \frac{I(A;U)}{I(Y_r;U)},
\]
where the supremum ranges over all input laws on \(A\), all post-processing channels
\(P_{U\mid Y_r}\), and all cases with \(I(Y_r;U)>0\), under the Markov chain
\(A\to Y_r\to U\) induced by \(W_1\). Put \(\eta=\eta_{\rm post}(W_1)\).

For this channel:

1. Its true capacity is exactly
   \[
   \boxed{C=D+\min\{C_1,C_2\}.}
   \]

2. Let \(R_{\rm prop}\) denote the maximum of the decode-forward, coordinated
   compress-forward, and uncoordinated compress-forward expressions in the
   capacity characterization proposed by Ponniah (arXiv:2609.15709), using the
   definitions reproduced and analyzed by Shiu (arXiv:2609.18727). Then
   \[
   \boxed{
   R_{\rm prop}\le
   \max\{C_1,\ D+\eta C_2\}.
   }
   \]

Consequently, every parameter choice satisfying
\[
D+\min\{C_1,C_2\}>
\max\{C_1,D+\eta C_2\}
\]
is a counterexample to the proposed characterization.

A particularly transparent sufficient condition is
\[
C_1\ge C_2>0,\qquad \eta<1,\qquad D>C_1-C_2.
\]
In that regime,
\[
C-R_{\rm prop}
\ge
\min\{D+C_2-C_1,\ (1-\eta)C_2\}>0.
\]
If moreover \(D\ge C_1\), then
\[
\boxed{
C-R_{\rm prop}\ge (1-\eta)C_2.
}
\]

Thus the failure identified by Shiu is not an isolated binary parameter choice:
it follows from a general tension between partial message decoding and strict
post-processing contraction.

## Proof

### Exact capacity

The \(B\)-component is observed noiselessly by the destination and supports
\(D=\log_2 M\) bits per channel use. Independently, a second sub-message can be
sent from the source through \(W_1\), decoded by the relay, and forwarded in the
next block through \(W_2\). Standard block-Markov pipelining therefore achieves
every rate below
\[
D+\min\{C_1,C_2\}.
\]

For the converse, the cut separating the source from the relay and destination
gives, for every joint input distribution,
\[
\begin{aligned}
I(A,B;Y_r,B,Z\mid X_r)
&=H(B\mid X_r)+I(A;Y_r\mid B,X_r)\\
&\le D+C_1.
\end{aligned}
\]
The second term is at most \(C_1\) after conditioning on each value of
\((B,X_r)\), because the conditional channel from \(A\) to \(Y_r\) is still
\(W_1\).

The cut separating source and relay from the destination gives
\[
\begin{aligned}
I(A,B,X_r;B,Z)
&=H(B)+I(X_r;Z\mid B)\\
&\le D+C_2.
\end{aligned}
\]
Hence the cutset bound is at most
\[
D+\min\{C_1,C_2\},
\]
which matches achievability.

### Decode-forward part of the proposed expression

For every input distribution,
\[
I(A,B;Y_r\mid X_r)=I(A;Y_r\mid X_r)\le C_1,
\]
so
\[
R_{\rm DF}\le C_1.
\]

### Compress-forward parts

Shiu showed that both compress-forward feasible sets from the proposed
characterization can be relaxed to distributions of the form
\[
p(a,b,x_r)\,
W_1(y_r\mid a)\,
W_2(z\mid x_r)\,
p(\hat y_r\mid y_r,x_r)
\]
subject to
\[
I(\hat Y_r;Y_r\mid X_r)
\le
I(\hat Y_r,X_r;B,Z).
\]
The same conditional-independence cancellation used in that proof gives
\[
I(\hat Y_r;Y_r\mid B,X_r)
\le
I(X_r;B,Z).
\]
The relaxed objective is
\[
H(B\mid X_r)+I(A;\hat Y_r\mid B,X_r).
\]

For each fixed \((B,X_r)=(b,x_r)\), the variables form
\[
A\to Y_r\to \hat Y_r
\]
through the same channel \(W_1\). By the definition of the input-free
post-processing contraction coefficient,
\[
I(A;\hat Y_r\mid B,X_r)
\le
\eta\,I(Y_r;\hat Y_r\mid B,X_r).
\]
Therefore
\[
\begin{aligned}
R_{\rm CF}
&\le H(B\mid X_r)+\eta I(X_r;B,Z)\\
&=H(B)-(1-\eta)I(B;X_r)+\eta I(X_r;Z\mid B)\\
&\le D+\eta C_2.
\end{aligned}
\]
This simultaneously upper-bounds the coordinated and uncoordinated
compress-forward terms. Combining with the decode-forward bound proves
\[
R_{\rm prop}\le\max\{C_1,D+\eta C_2\}.
\]

## Binary symmetric specialization

Take
\[
W_1=\operatorname{BSC}(p),\qquad
W_2=\operatorname{BSC}(q),\qquad
\mathcal B=\{0,1\}.
\]
For \(0\le p,q\le 1/2\),
\[
C_1=1-h_2(p),\qquad
C_2=1-h_2(q),
\]
and the BSC post-processing contraction coefficient used by Shiu is
\[
\eta=(1-2p)^2.
\]

Hence for every
\[
\boxed{0<p\le q<1/2}
\]
we have \(C_1\ge C_2>0\), and therefore
\[
\boxed{
C=2-h_2(q)
}
\]
while the proposed characterization obeys
\[
\boxed{
R_{\rm prop}
\le
1+(1-2p)^2\,[1-h_2(q)].
}
\]
The certified strict gap is
\[
\boxed{
C-R_{\rm prop}
\ge
4p(1-p)\,[1-h_2(q)].
}
\]

Shiu's published choice \(p=q=1/4\) is one point in this two-parameter
counterexample region. A clean larger-gap example is
\[
p=q=\frac18,
\]
for which
\[
C=1.456435556800\ldots,
\]
\[
R_{\rm prop}\le1.256745000700\ldots,
\]
and therefore
\[
\boxed{
C-R_{\rm prop}\ge0.199690556100\ldots\ \text{bits/use}.
}
\]
For comparison, the same bound at \(p=q=1/4\) is
\(0.141541406656\ldots\) bits/use.

## Context and originality boundary

Shiu's recent counterexample fixes both binary crossover probabilities at
\(1/4\), proves an achievable rate \(2-h_2(1/4)\), notes that the cutset bound
gives equality, and upper-bounds the proposed DF/C-CF/U-CF expression by using
the BSC post-processing strong data-processing inequality. The fixed
counterexample, the proposed characterization being refuted, the cutset bound,
block-Markov relaying, and the BSC SDPI are not new here.

The contribution claimed here is the abstraction of that mechanism to an
arbitrary pair of product component channels through the post-processing
contraction coefficient, together with the resulting open two-parameter BSC
counterexample region and an explicit stronger numerical witness. To the best
of our knowledge, targeted searches for the exact channel template, arbitrary
BSC crossover parameters, post-processing contraction formulations, and
equivalent relay-channel statements did not locate this general theorem.

Because the motivating counterexample is very recent and the abstraction is
short once its proof is recognized, folklore and near-simultaneous priority
risk are material.

## Limitations

The theorem concerns this split product relay architecture; it is not a new
capacity theorem for general relay channels. The upper bound is on the specific
DF/C-CF/U-CF characterization proposed in arXiv:2609.15709, not on all
compress-forward or partial-decode-forward variants in the literature. The
post-processing coefficient bound can be loose, so the stated sufficient
counterexample region need not describe every parameter for which the proposed
formula fails. No claim of sharpness of the certified gap is made.

## References

- C. H. M. Shiu, *Counterexample to a Proposed Capacity Characterization of the Relay Channel*, arXiv:2609.18727, submitted 16 September 2026. https://arxiv.org/abs/2609.18727
- J. Ponniah, *The Capacity of the Relay Channel*, arXiv:2609.15709, submitted 14 September 2026. https://arxiv.org/abs/2609.15709
- T. M. Cover and A. A. El Gamal, *Capacity Theorems for the Relay Channel*, IEEE Transactions on Information Theory 25(5), 1979.
