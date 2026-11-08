# Exact uncertainty law and variance cancellation for rooted cascade opinions

## Finding

In a single Friedkin–Johnsen-on-cascades (FJC) exposure on an arbitrary finite rooted arborescence, terminal opinions are deterministic affine responses multiplied by correlated path-activation indicators. Consequently, the **full moment-generating function of every weighted aggregate opinion change** has an exact linear-size tree recursion. The same recursion yields an exact **sum-of-squares variance decomposition** and a necessary-and-sufficient condition for a nonconstant collection of random individual opinions to produce a deterministic aggregate.

Specifically, with the notation below, put
\[
M_v=a_v+\theta_v\sum_{c\in\operatorname{ch}(v)}M_c,
\qquad
\delta_v=\prod_{u\in\operatorname{Anc}(v)}\theta_u.
\]
Then, for the aggregate opinion change \(Y\),
\[
\boxed{\operatorname{Var}(Y)=
\sum_{v\in V}\delta_v\theta_v(1-\theta_v)
\left(\sum_{c\in\operatorname{ch}(v)}M_c\right)^2.}
\]
Therefore \(Y\) is almost surely constant **if and only if** every vertex with \(\delta_v\theta_v(1-\theta_v)>0\) has \(\sum_{c}M_c=0\). Mean, variance, and the moment-generating function at any fixed argument can each be computed in \(O(|V|)\) arithmetic operations.

## Assumptions and scope

Let \(T=(V,E)\) be any finite rooted, outward-directed tree with root \(r\), with vertices ordered after their parents. Write \(p(v)\) for the unique parent of a nonroot vertex, \(\operatorname{ch}(v)\) for its children, and \(\operatorname{Anc}(v)\) for its strict ancestors. A single post begins at \(r\), which always reshares; set \(\theta_r=1\). Every other vertex \(v\), conditional on receiving the post, independently chooses whether to reshare to **all** its children with probability \(\theta_v\in[0,1]\). Coin flips at different vertices are independent and independent of initial opinions. A vertex updates once, when first exposed; unexposed vertices retain their opinions. There are no extra exposure arcs and no concurrent posts.

Initial opinions \(\xi_v\in[-1,1]\) and innate opinions \(u_v\in[-1,1]\) are deterministic. For nonroot \(v\), an exposure from \(p(v)\) produces the asynchronous FJC-style update
\[
X_v=h_v\big[(1-\gamma_v)\xi_v+\gamma_vX_{p(v)}\big]+(1-h_v)u_v,
\qquad h_v,\gamma_v\in[0,1].
\]
The parent is already updated when \(v\) receives the post. This is the single-predecessor specialization of the update in Biondi et al., arXiv:2610.19867, Eq. (6); admissible calibrated FJC coefficients form a subset of the displayed coefficient ranges. The root is not updated, so \(X_r=\xi_r\). Fix arbitrary real aggregate weights \(w_v\), and set
\[
Y=\sum_{v\in V}w_v(X_v-\xi_v).
\]
The theorem concerns one cascade conditional on a deterministic input state, not a closed law for an arbitrary graph with multiple predecessors or for joint trajectories over many dependent posts.

Define deterministic *conditional-on-exposure* values by \(z_r=\xi_r\) and
\[
z_v=h_v\big[(1-\gamma_v)\xi_v+\gamma_vz_{p(v)}\big]+(1-h_v)u_v,
\qquad a_v=w_v(z_v-\xi_v),\quad a_r=0.
\]
The product over an empty set is one, and all formulas include zero or deterministic resharing probabilities.

## Proof

**1. Deterministic conditional opinions.** Pre-sample independent Bernoulli indicators \(B_v\) of parameters \(\theta_v\), with \(B_r=1\). A nonroot vertex \(v\) is exposed exactly on the event
\[
I_v=\prod_{u\in\operatorname{Anc}(v)}B_u=1;
\qquad I_r=1.
\]
Induction by tree depth shows that, whenever \(I_v=1\), all ancestors have already been updated and \(X_v=z_v\). When \(I_v=0\), \(X_v=\xi_v\). Thus the **path-activation representation** is exactly
\[
X_v=\xi_v+(z_v-\xi_v)I_v,
\qquad Y=\sum_{v\in V}a_vI_v.
\]
This reduction is valid despite correlations among the \(I_v\): sibling exposures share their parent's single broadcast coin.

**2. Exact all-order law.** For a vertex \(v\) conditioned on its exposure, define \(Z_v\) as the weighted opinion change contributed by its descendant subtree, including itself. The children are all exposed if \(B_v=1\), and none are exposed if \(B_v=0\). Since disjoint descendant subtrees use disjoint resharing coins, their conditional contributions \(Z_c\) are mutually independent and are independent of \(B_v\). Hence
\[
Z_v\ \overset{d}{=}\ a_v+B_v\sum_{c\in\operatorname{ch}(v)}Z_c.
\]
For every real \(t\), its moment-generating function \(G_v(t)=\mathbb E[e^{tZ_v}]\) therefore satisfies
\[
\boxed{G_v(t)=e^{t a_v}\left(1-\theta_v+\theta_v\prod_{c\in\operatorname{ch}(v)}G_c(t)\right).}
\]
The root is exposed, so \(G_r(t)=\mathbb E[e^{tY}]\). The leaf formula is \(G_v(t)=e^{t a_v}\). Thus the identity gives the complete finite-support law and all moments, without a diffusion–opinion independence approximation.

**3. Exact variance.** Let \(M_v=\mathbb E Z_v\), \(V_v=\operatorname{Var}(Z_v)\), and \(S_v=\sum_{c\in\operatorname{ch}(v)}M_c\). Total expectation and variance applied to the preceding distributional identity give
\[
M_v=a_v+\theta_v S_v,
\qquad
V_v=\theta_v\sum_{c\in\operatorname{ch}(v)}V_c+
\theta_v(1-\theta_v)S_v^2.
\]
Expanding the second identity from the root through all descendants multiplies the local variance contribution at \(v\) by the product of broadcast probabilities of its strict ancestors, namely \(\delta_v\). This is precisely the displayed nonnegative sum-of-squares identity. Every term is nonnegative, so the asserted zero-variance criterion is both necessary and sufficient. No assumption about the signs of the weights or the induced opinion changes is needed.

**4. Pairwise covariance.** For any vertices \(i,j\), set
\[
\delta_{ij}=\prod_{v\in\operatorname{Anc}(i)\cup\operatorname{Anc}(j)}\theta_v,
\qquad d_i=z_i-\xi_i.
\]
Then \(\mathbb E I_i=\delta_i\), \(\mathbb E(I_iI_j)=\delta_{ij}\), and
\[
\boxed{\operatorname{Cov}(X_i,X_j)=d_id_j(\delta_{ij}-\delta_i\delta_j).}
\]
The bracket is nonnegative, because each probability factor in \([0,1]\) shared by the two ancestor sets appears once in \(\delta_{ij}\) but twice in \(\delta_i\delta_j\). Consequently, if the bracket is positive, the sign of terminal-opinion covariance is exactly the sign of the product of the two deterministic opinion changes. Positive activation association can therefore generate **negative** opinion covariance. This proves the complete claim.

## Verification

The accompanying standalone `verify.py` implements two genuinely separate finite-state calculations: exhaustive enumeration of every Bernoulli resharing pattern followed by sequential FJC opinion updates, and a bottom-up tree-law convolution with independent moment messages. Using exact rational arithmetic it checks the complete aggregate distribution, mean, variance, gatewise sum of squares, every individual mean, and every pairwise covariance for 360 independently generated rooted trees of sizes two through nine (including zero-reshare parameters). It separately checks a cancellation example. Run `python3 verify.py` in a standard Python 3 installation; no external packages are required. The verifier returns `PASS` with no mismatches. The enumerations are finite stress tests, **not** a substitute for the universal proof above.

For a concrete cancellation instance, take four vertices \(r\to v\to\{a,b\}\), with \(\xi_r=\xi_v=0\), \(\xi_a=u_a=-1\), \(\xi_b=u_b=1\), and \(u_v=0\). Let \(h_v=h_a=h_b=1/2\), \(\gamma_v=\gamma_a=\gamma_b=1\), and \(\theta_v=1/2\). With equal positive weights on the two leaves and zero weights elsewhere, both terminal leaf opinions remain random, each having variance \(1/16\), while their covariance is \(-1/16\); their aggregate opinion change is identically zero. An approximation that makes their exposure events independent would miss this exact cancellation.

## Relationship to prior work

Biondi, Boldrini, Passarella, and Conti (2026), arXiv:2610.19867, specify the FJC node update, stochastic tree exposure, conditional layer recursion and a mean-field approximation for expected opinions; they also describe computational tree reductions. The result here is restricted to a **genuine unique-parent arborescence**, rather than the general layered graph where nodes may have multiple exposure predecessors. The new contribution is the exact path-activation reduction for FJC terminal opinions, its weighted full-law recursion, and its explicit necessary-and-sufficient variance-cancellation criterion. These statements are not the general no-closure claim and are not inferred from an approximation. The earlier FJC model description, arXiv:2506.16302, principally reports simulated opinion patterns.

Standard independent-cascade and branching-tree theory already has Bernoulli reachability recursions, and ordinary probability theory supplies the conditional variance identity. Those underlying tools are **not** asserted to be novel. The relevant new mathematical identification is that the *coupled, sequential opinion updates* become deterministic conditional path responses on a true arborescence, permitting an exact law for signed aggregate opinion changes and the associated cancellation classification. Results on reachability totals alone do not specify those opinion-response coefficients. A broader already-published weighted-tree theorem or an uninspected supplementary calculation could still subsume the result; an absence of search matches does not rule that out.

## Limitations

The unique-parent and single-cascade assumptions are essential for the simple factorization. Multiple exposure parents, cycles, multiple simultaneous posts, adaptive resharing probabilities, and random or correlated starting opinions are outside the unconditional theorem. When the previous opinion state is random, the formulas hold conditionally on that state, but the stated unconditional moment-generating function need not follow by replacing initial values with their means. Zero variance of one weighted aggregate need not mean that any individual's terminal opinion is deterministic. The result does not claim that tree-percolation generating functions or laws of total variance are new, nor that it is independently validated.

## References

1. E. Biondi, C. Boldrini, A. Passarella, and M. Conti, *From Content Sharing to Opinion Shaping: A Theoretical Framework for Cascade-Driven Opinion Dynamics*, arXiv:2610.19867v1, first public October 14, 2026. https://arxiv.org/abs/2610.19867
2. E. Biondi, C. Boldrini, A. Passarella, and M. Conti, *Cascade-driven opinion dynamics on social networks*, arXiv:2506.16302v1, first public June 19, 2025. https://arxiv.org/abs/2506.16302
3. E. Abbe, S. Kulkarni, and E. J. Lee, *Nonbacktracking Bounds on the Influence in Independent Cascade Models*, arXiv:1706.05295, 2017. https://arxiv.org/abs/1706.05295
