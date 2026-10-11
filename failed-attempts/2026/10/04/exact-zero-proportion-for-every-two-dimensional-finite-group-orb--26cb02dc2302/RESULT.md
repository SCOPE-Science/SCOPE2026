# Exact zero proportion for every two-dimensional finite-group orbit
## Finding
Let \(G\) be a finite group and let \(\pi:G\to U(2)\) be a unitary representation. Define the projective kernel
\[
K=\{g\in G:\pi(g)\in\mathbb T I\},
\]
and put \(H=G/K\). For a nonzero window \(\eta\in\mathbb C^2\), write \([\eta]\in\mathbb{CP}^1\) for its ray and
\[
m(\eta)=|H\cdot[\eta]|.
\]
Using the zero-proportion invariant introduced by Führ and Oussa,
\[
p_0(\pi,\eta)=\max_{0\ne f\in\mathbb C^2}\left(1-\frac{|\operatorname{supp}(V_\eta f)|}{|G|}\right),
\qquad
V_\eta f(g)=\langle f,\pi(g)\eta\rangle,
\]
one has the exact identity
\[
p_0(\pi,\eta)=\frac1{m(\eta)}.
\]
Therefore
\[
p_0(\pi)=\min_{0\ne\eta}p_0(\pi,\eta)=\frac1{|H|}=\frac{|K|}{|G|}.
\]
The minimizing windows are exactly those whose projective stabilizer in \(H\) is trivial. For a fixed window, the sharp universal sampling threshold is \(|G|/m(\eta)\): every sample set \(A\subseteq G\) with \(|A|>|G|/m(\eta)\) gives an injective sampled coefficient map, while some set with exactly \(|G|/m(\eta)\) samples does not.

## Assumptions and scope
The group is finite, the representation is complex unitary of dimension exactly two, and no irreducibility or nilpotence hypothesis is needed. The statement concerns the support-zero invariant \(p_0\) and linear injectivity of sampled coefficient maps; it does not by itself assert phase retrieval from magnitudes.

The dimension-two hypothesis is essential to this proof mechanism: for every nonzero \(f\in\mathbb C^2\), the orthogonal complement \(f^\perp\) is a single projective ray. In higher dimensions it is a projective hyperplane and may meet an orbit in many points with nonuniform multiplicities.

## Proof
Fix \(0\ne\eta\in\mathbb C^2\), and consider the projective orbit map
\[
q_\eta:G\longrightarrow H\cdot[\eta],
\qquad
q_\eta(g)=[\pi(g)\eta].
\]
It factors through \(H=G/K\). By orbit--stabilizer, every fiber of the induced map \(H\to H\cdot[\eta]\) has cardinality
\[
|\operatorname{Stab}_H([\eta])|=\frac{|H|}{m(\eta)}.
\]
Each element of \(H\) has exactly \(|K|\) lifts to \(G\), so every fiber of \(q_\eta\) has cardinality
\[
|K|\frac{|H|}{m(\eta)}=\frac{|G|}{m(\eta)}.
\]

For \(0\ne f\in\mathbb C^2\), the coefficient \(V_\eta f(g)\) vanishes exactly when \(\pi(g)\eta\in f^\perp\). Since \(f^\perp\) is a one-dimensional complex subspace, it determines a single point \([f^\perp]\in\mathbb{CP}^1\). Hence the zero set of \(V_\eta f\) is either empty, if \([f^\perp]\notin H\cdot[\eta]\), or it is one complete fiber of \(q_\eta\), of cardinality \(|G|/m(\eta)\). As \(f\) varies over nonzero vectors, \([f^\perp]\) ranges over all of \(\mathbb{CP}^1\), so the latter case occurs. Thus the largest possible zero proportion is exactly \(1/m(\eta)\).

It remains to minimize over \(\eta\). The finite group \(H\) acts faithfully on \(\mathbb{CP}^1\) by projective unitaries. Every nonidentity element of \(H\) fixes at most two rays, namely its eigendirections. The union of these fixed-ray sets over the finitely many nonidentity elements of \(H\) is finite, whereas \(\mathbb{CP}^1\) is infinite. A ray outside that union has trivial stabilizer, hence projective orbit size \(|H|\). No orbit can be larger, so \(p_0(\pi)=1/|H|\), and equality for a given window occurs exactly for trivial stabilizer.

Finally, Führ--Oussa's sampling observation says that every set with cardinality strictly larger than \(p_0(\pi,\eta)|G|\) yields an injective sampled coefficient map. The exact formula gives the threshold \(|G|/m(\eta)\). Sharpness follows by choosing \(f\) whose orthogonal ray is any point of the projective orbit: its coefficient vanishes on a full fiber of exactly that size.

## Verification
The proof uses only orbit--stabilizer, the definition of projective kernel, and the fact that a nonzero linear functional on \(\mathbb C^2\) has a one-dimensional kernel. The boundary case \(|H|=1\) is included: every orbit has one ray and \(p_0(\pi,\eta)=1\). If \(m(\eta)=1\), the orbit lies in one ray, so a nonzero orthogonal vector produces an identically zero coefficient, again matching the formula.

The minimization step was checked separately: because the action of \(H\) is faithful on \(\mathbb{CP}^1\), a nonidentity projective unitary cannot fix every ray; its fixed set consists of its one or two eigendirections. A finite union of such sets cannot exhaust \(\mathbb{CP}^1\).

No finite experiment, numerical approximation, or unproved classification is used.

## Relationship to prior work
Führ and Oussa introduced \(p_0(\pi,\eta)\) as the maximal zero proportion of a nonzero matrix coefficient, observed its invariance under factoring projective-kernel subgroups, related it to uniform sampling, and developed estimates for it in their induction for finite \(p\)-groups. Their article gives general estimates rather than the exact two-dimensional orbit-stabilizer formula above. The first public version of their paper is arXiv:2201.08654, dated 2022-01-21, and the published article lists MSC 42C15 first.

The full-spark orbit literature studies the stronger requirement that every subfamily of the relevant size be linearly independent, often for particular groups or projective representations. That does not state the present formula for every window of every two-dimensional finite-group representation, including projective multiplicities. Cheng's later work on phase retrievability of irreducible finite-group representations is indexed under adjoint representations, cyclic vectors, maximal spanning vectors, and phase retrieval; its accessible metadata does not state an exact \(p_0\) formula. Its full text was not materially available in this check, so it remains a residual priority risk rather than evidence of coverage.

## Limitations
The result is specific to complex dimension two. It determines the exact support-zero invariant and the sharp worst-case sample-count guarantee, not a magnitude-only phase-retrieval criterion. It also does not optimize which particular sample sets work below the universal threshold.

A residual literature risk remains that an equivalent orbit-fiber statement may occur as an unindexed corollary in later representation-frame or full-spark work. The searches performed found no such statement.

## References
1. Hartmut Führ and Vignon Oussa, “Phase Retrieval for Nilpotent Groups,” arXiv:2201.08654 (first public version 2022-01-21); Journal of Fourier Analysis and Applications 29, 47 (2023), DOI 10.1007/s00041-023-10031-5.
2. Romanos Diogenes Malikiosis and Vignon Oussa, “Full Spark Frames in the Orbit of a Representation,” arXiv:1909.06223.
3. Chuangxun Cheng and Deguang Han, “On twisted group frames,” Linear Algebra and its Applications 569 (2019), 285–310, DOI 10.1016/j.laa.2018.11.034.
4. Chuangxun Cheng, “On the phase retrievability of irreducible representations of finite groups,” Linear Algebra and its Applications 714 (2025), DOI 10.1016/j.laa.2025.03.011.
