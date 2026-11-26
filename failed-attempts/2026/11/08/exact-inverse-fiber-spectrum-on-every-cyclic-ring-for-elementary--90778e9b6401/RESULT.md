# Exact inverse-fiber spectrum on every cyclic ring for elementary cellular automaton Rule 106

## Finding

For every integer \(n\ge1\), let \(F_n\) be the cyclic binary elementary cellular automaton Rule 106 and let \(C_j(n)\) be the number of *indexed* outputs of length \(n\) possessing precisely \(j\) indexed one-step predecessors. Its entire inverse-fiber spectrum is given by the following rational generating functions:

\[
A(z):=\sum_{n\ge1} C_0(n)z^n =
\frac{z+2z^3-z^4-z^5-2z^6}{(1-z^3)(1-z-2z^3)},
\qquad
T(z):=\sum_{n\ge1}C_3(n)z^n=\frac{z^3}{1-z^3},
\]

\[
\sum_{n\ge1}C_2(n)z^n=A(z)-2T(z),\qquad
\sum_{n\ge1}C_1(n)z^n=\frac{2z}{1-2z}-2A(z)+T(z),
\qquad C_j(n)=0\quad(j\ge4).
\]

In particular, exactly one target, \(1^n\), has three predecessors when \(3\mid n\); otherwise no target has three predecessors. The zero-preimage count satisfies
\[
C_0(n)=C_0(n-1)+3C_0(n-3)-C_0(n-4)-2C_0(n-6)\quad(n\ge7),
\]
with \(C_0(0)=0\) and \((C_0(1),\ldots,C_0(6))=(1,1,3,5,6,12)\). The number of uniquely invertible outputs is \(2^n-2C_0(n)+\mathbf 1_{3\mid n}\). The fraction of uniquely invertible outputs tends to one exponentially: the exceptional count is of order \(\lambda^n\), where \(\lambda\approx1.69562076956\) is the positive root of \(\lambda^3-\lambda^2-2=0\).

## Assumptions and scope

The configurations are labeled words \(x=(x_0,\ldots,x_{n-1})\in\{0,1\}^n\); shifts, complements, or rotations of words are **not** identified. Indices are in \(\mathbb Z/n\mathbb Z\), including the repeated-neighbor cases \(n=1,2\). The update is exactly
\[
(F_n(x))_i=x_{i+1}\oplus(x_{i-1}x_i),
\]
where multiplication and exclusive-or are in \(\mathbb F_2\). Predecessors are one-step solutions \(F_n(x)=y\), not preimages under multiple iterations.

## Proof

**1. Deterministic labeled pair transitions.** Encode the pair \((a,b)\in\{0,1\}^2\) as \(2a+b\in\{0,1,2,3\}\). For each output bit \(v\in\{0,1\}\), the right-permutive local rule forces the next pair to be
\[
g_v(a,b)=(b,v\oplus ab).
\]
Writing each map as the list of images of \(0,1,2,3\) yields
\[
g_0=(0,2,0,3),\qquad g_1=(1,3,1,2).
\]
For a prescribed cyclic output \(y\), the initial pair determines every subsequent pair. A predecessor exists precisely for an initial pair fixed by the product \(g_{y_{n-1}}\circ\cdots\circ g_{y_0}\). Thus its number of fixed points is exactly \(|F_n^{-1}(y)|\), including for rings of length one or two.

**2. Finite semigroup and multiplicity bound.** Close the identity map of the four pairs under left multiplication by \(g_0,g_1\). Breadth-first closure terminates at precisely \(41\) distinct functions. The generators are noninjective, so every nonempty composition is noninjective and cannot equal the identity map on four elements. The identity is the only transformation with four fixed points. Consequently no positive-length output has four or more predecessors. The stand-alone program `verify.py` constructs all \(41\) maps from the displayed generators, rather than reading a precomputed state list.

**3. Transfer identity and exact rational certificate.** Order the reachable maps with the identity first. Let \(H\) be their integer adjacency matrix: there is one edge for each multiplication by \(g_0\) and \(g_1\), counted with multiplicity if necessary. Let \(u\) select the identity, and \(p_j\) indicate the maps with exactly \(j\) fixed points. Then
\[
C_j(n)=u^\mathsf TH^np_j\qquad(n\ge1).
\]
The executable certificate computes this expression by integer arithmetic. Write
\[
Q_0(z)=1-z-3z^3+z^4+2z^6,
\quad P_0(z)=z+2z^3-z^4-z^5-2z^6,
\]
\[
Q_3(z)=1-z^3,\qquad P_3(z)=z^3.
\]
For \(j=0\) the program confirms the coefficient identity \(Q_0(z)\sum_{n\ge0}C_0(n)z^n=P_0(z)\) in degrees \(0\) through \(47\); for \(j=3\) it confirms \(Q_3(z)\sum_{n\ge0}C_3(n)z^n=P_3(z)\) in degrees \(0\) through \(44\). Here \(C_0(0)=C_3(0)=0\) by convention, and degree zero of the transfer matrix is not counted as an output.

These *finite* checks prove the infinite identities: for a degree-\(d\) polynomial \(Q\), all residual coefficients after degree \(d\) have the form \(u^\mathsf T H^m v\) for a single integer vector \(v\) depending on \(Q\) and \(p_j\). Since \(H\) has dimension \(41\), Cayley–Hamilton implies that this sequence obeys a recurrence of order at most \(41\). The verifier establishes \(41\) consecutive residual zeros, in degrees \(7,\ldots,47\) for \(Q_0\) and degrees \(4,\ldots,44\) for \(Q_3\); therefore *all* subsequent residual coefficients vanish. These are exact integer operations, not extrapolation from a finite prefix.

**4. Recovering every fiber size.** Each of the \(2^n\) inputs has exactly one output. Consequently
\[
C_0(n)+C_1(n)+C_2(n)+C_3(n)=2^n,\qquad
C_1(n)+2C_2(n)+3C_3(n)=2^n.
\]
Subtracting gives \(C_2(n)=C_0(n)-2C_3(n)\) and \(C_1(n)=2^n-2C_0(n)+C_3(n)\). For the target \(1^n\), the transformation \(g_1\) consists of a three-cycle and a transient point; its power has three fixed points exactly when \(3\mid n\). Because the coefficient of \(z^n\) in \(T(z)\) is then exactly one, this is the sole three-preimage target.

**5. Asymptotic statement.** The factor \(1-z-2z^3\) has a simple positive root \(\rho=1/\lambda\) strictly inside the unit circle. Its remaining roots have larger modulus (from its primitive nonnegative recurrence), and the other factor \(1-z^3\) has roots of modulus one. The numerator \(P_0(\rho)\) is nonzero. Thus standard simple-pole coefficient asymptotics give \(C_0(n)=\Theta(\lambda^n)\), with \(\lambda<2\). The displayed identities then show that the proportion of targets with other than one predecessor tends to zero exponentially.

## Verification

Run `python3 verify.py` from this package to reconstruct the full \(41\)-state transfer semigroup and certify the stated generating-function equalities by the \(41\)-step Cayley–Hamilton check. Run `python3 independent_check.py` for a separate direct enumeration of every cyclic binary configuration through length \(12\) and an independent four-state labeled-de-Bruijn matrix trace for every corresponding output. Both return success in the delivered package.

For \(n=1,\ldots,6\), the respective \((C_0,C_1,C_2,C_3)\) vectors are \((1,0,1,0)\), \((1,2,1,0)\), \((3,3,1,1)\), \((5,6,5,0)\), \((6,20,6,0)\), and \((12,41,10,1)\). The transfer-matrix certificate—not the direct enumeration—is the basis for the all-length conclusion.

## Relationship to prior work

Zhao, Chen, and Jin (2014) establish topological mixing and many chaotic invariant subsystems of Rule 106 on bi-infinite configurations; they do not count inverse fibers of *all* cyclic targets at every ring length. Powley and Stepney (2009) investigate automorphisms of finite transition graphs; their symmetry classification does not specify this fiber distribution. Powley and Stepney (2010) develop preimage counting for homogeneous outputs, a strictly smaller family than the \(2^n\) targets counted here. Mariot and coauthors (2017) study periodic preimages, including the labeled de Bruijn graph of Rule 106, but not this global inverse-fiber histogram or its rational generating functions.

The de Bruijn/semigroup method is standard; the concrete Rule 106 all-ring inverse-fiber spectrum and asymptotic density are the claim. Other elementary rules related by reversal or state-complement conjugacies may have equivalent fiber statistics; the result is not presented as independent of such equivalent formulations.

## Limitations

This result concerns one Wolfram rule, one temporal step, cyclic labeled binary rings, and exact inverse multiplicities; it does not count multistep ancestors, infer universality, or establish the complexity of finding individual predecessors. The finite verification is a dimension-bounded certificate coupled to Cayley–Hamilton, not a purported exhaustive enumeration of infinitely many rings. Historical-priority checks are based on inspected primary literature and research indexes; they do not constitute a proof that no earlier equivalent result exists. No independent scientific validation has been performed.

## References

- Gaocang Zhao, Fangyue Chen, Weifeng Jin, “Infinite Number of Disjoint Chaotic Subsystems of Cellular Automaton Rule 106,” *Applied Mathematics* 5 (2014), 3256–3263. First verified public date: 2014-11-20. https://www.scirp.org/journal/paperinformation?paperid=51585
- Edward J. Powley, Susan Stepney, “Automorphisms of Transition Graphs for Elementary Cellular Automata,” *Journal of Cellular Automata* 4 (2009), 125–136. https://www-users.york.ac.uk/~ss44/bib/ss/nonstd/jca08.pdf
- Edward J. Powley, Susan Stepney, “Counting preimages of homogeneous configurations in 1-dimensional cellular automata,” *Journal of Cellular Automata* 5 (2010), 353–381. https://www-users.york.ac.uk/~ss44/bib/ss/nonstd/jca11.pdf
- Luca Mariot, Alberto Leporati, Alberto Dennunzio, Enrico Formenti, “Computing the Periods of Preimages in Surjective Cellular Automata,” *Natural Computing* (2017). https://lucamariot.org/files/papers/mldf_naco_2017_postprint.pdf
