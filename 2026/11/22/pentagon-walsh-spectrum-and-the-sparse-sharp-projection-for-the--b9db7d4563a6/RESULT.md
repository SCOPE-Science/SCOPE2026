# Pentagon Walsh spectrum and the sparse sharp projection for the Petersen graph

## Finding

Let \(P\) be the Petersen graph with fifteen edges and let \(G=\mathbb F_2^{E(P)}\). Write \(\mathcal C_5\) for its twelve simple five-edge cycles and \(k:G\to\{0,1\}\) for the indicator of their edge-incidence vectors. Convolution \((Tf)(x)=\sum_{y\in G}k(y)f(x+y)\) has this **complete signed Walsh spectrum**:

| Multiplier | Multiplicity |
|---:|---:|
| \(-12\) | 512 |
| \(-4\) | 7,680 |
| \(0\) | 16,384 |
| \(4\) | 7,680 |
| \(12\) | 512 |

Consequently its rank and nullity are both \(16,384\), its least nonzero singular value is \(4\), and the condition number on its range in the Euclidean norm is \(3\).

More structurally, let \(\mathcal C_6\) denote the ten simple six-edge cycles and let \(\mathcal F\) be the six distinct spanning two-factors, each the disjoint union of two five-edge cycles. Write \(\delta_z\) for the point mass at \(z\in G\). The unique translation-invariant projection onto \(\operatorname{ran}T\) is convolution by

\[
p=\frac12\delta_0+\frac18\sum_{C\in\mathcal C_6}\delta_{\mathbf 1_C}-\frac18\sum_{F\in\mathcal F}\delta_{\mathbf 1_F}.
\]

Among **all real or complex linear projections** \(Q\) onto this range, including projections without translation symmetry, the sharp endpoint constants are

\[
\min_Q\|Q\|_{\ell^1(G)\to\ell^1(G)}
=\min_Q\|Q\|_{\ell^\infty(G)\to\ell^\infty(G)}=\frac52.
\]

## Assumptions and scope

Indices below are modulo five. The vertex set is \(\{u_i,v_i:0\le i<5\}\); the fifteen undirected edges are exactly \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\) for \(0\le i<5\). The group operation is symmetric difference (XOR), not graph-edge union. The Fourier convention is unnormalized: \(\widehat k(s)=\sum_{x\in G}k(x)(-1)^{s\cdot x}\). All norms are for counting measure, which yields the same operator norm on each endpoint as any uniform rescaling of that measure. The result is specific to the twelve pentagons of this labelled graph; relabelling the edges only conjugates the operator.

## Proof

**1. Exhaustive identification of the edge sets.** Encode \(u_i=i\), \(v_i=i+5\), and order the edges as: the five outer rim edges \(u_i u_{i+1}\), the five spokes \(u_i v_i\), and the five inner-star edges \(v_i v_{i+2}\), with \(i=0,\ldots,4\) in each family. A subset of edges is encoded by the integer whose binary positions are its selected edge indices. Direct examination of all length-five closed simple paths, up to cyclic rotation and reversal, produces precisely these twelve masks:

`31, 1187, 2374, 4748, 5680, 8504, 9604, 10337, 16977, 19208, 20674, 31744`.

The computation is finite and exhaustive: every unrooted simple cycle has a unique vertex sequence beginning at its minimum-labelled vertex and with its second vertex smaller than its last; checking all such five-tuples enumerates each exactly once. This construction can be independently reproduced by `verify.py` without relying on the displayed list.

**2. Six-dimensional reduction.** The binary edge cycle space has dimension \(15-10+1=6\), because \(P\) is connected. The twelve masks span this whole space. One XOR basis, in descending-pivot elimination order, is

`16974, 8487, 4748, 2374, 1187, 31`.

Thus there are exactly \(64\) edge codewords and every assignment of signs to these six basis vectors is realized by exactly \(2^9=512\) characters of the original group. For a basis-coordinate word \(z=(z_0,\ldots,z_5)\), define \(c(z)\) as the XOR of basis masks whose corresponding bit is one, and define the compressed indicator \(a(z)=1\) precisely when \(c(z)\) is a pentagon mask. The sixty-four compressed Walsh sums are

\[
L(t)=\sum_{z\in\mathbb F_2^6}a(z)(-1)^{t\cdot z},\qquad t\in\mathbb F_2^6.
\]

An exact exhaustive evaluation of the sixty-four sums, in integer order \(t=0,\ldots,63\), yields the following eight successive rows, each containing eight values:

```text
12, 4, 4, 0, 4, 4, 0,-4
 4, 4, 4, 0, 0, 0,-4, 0
 4, 0, 4,-4, 4, 0, 0, 0
 0,-4, 0, 0,-4, 0, 0, 0
 4, 0, 0, 0, 0, 4, 0, 0
-4, 0, 0, 0,-4, 0,-4, 4
 0, 0, 4, 0,-4,-4,-4, 0
-4,-4, 0, 4,-12,-4,-4, 0
```

Every row is computable from the twelve masks and displayed basis with only bit parity and integer addition. This gives \(-12:1,-4:15,0:32,4:15,12:1\) on the compressed dual, each with the stated multiplicity factor \(512\) on \(G\). No estimated sampling or numerical tolerance is involved.

**3. The sparse orthogonal projector.** Fourier inversion of the Boolean function \(1_{L(t)\ne0}\), divided by \(64\), gives an element of the six-dimensional code. The exact inverse has coefficient \(1/2\) at zero, coefficient \(1/8\) at precisely the ten weight-six codewords, and coefficient \(-1/8\) at precisely the six weight-ten codewords, with zero at the other \(47\) codewords. The weight-six words are exactly the ten simple hexagons; the weight-ten words are the six unions of two disjoint pentagons. The code has weight enumerator \(1+12z^5+10z^6+15z^8+20z^9+6z^{10}\), independently confirmed by the six-generator span. Fourier inversion of \(1_{\widehat k\ne0}\) on the full group gives the same kernel, since the character support is constant on cosets of the cycle-space annihilator. This proves the asserted formula and \(p*p=p\).

**4. Sharp unrestricted optimality.** Let \(W=\operatorname{ran}T\), which is translation invariant, and let \(Q\) be any real or complex linear projection with range \(W\). Averaging \(\tau_g^{-1}Q\tau_g\) over \(g\in G\) yields a projection onto \(W\) of norm at most \(\|Q\|\) in either endpoint norm. Its Fourier multiplier must equal one on \(W\)'s active characters and zero on the other characters, so the averaged operator is uniquely the convolution projection by \(p\). A convolution operator on a finite group has \(\ell^1\)- and \(\ell^\infty\)-operator norm equal to the sum of absolute values of its kernel (apply it to a suitably signed point mass, respectively a suitably signed function). Hence

\[
\|p*\|=\frac12+10\cdot\frac18+6\cdot\frac18=\frac52,
\]

which is attained and is a lower bound for every competing projection. The largest surviving Fourier multiplier magnitude is \(12\) and the smallest is \(4\), proving condition number \(3\).

## Verification

Run `python3 verify.py` using Python 3.9 or later and only the standard library. The checker independently enumerates simple cycles from adjacency, calculates the six-dimensional cycle code and its complete weight census, performs the sixty-four exact compressed character sums, performs a separate \(2^{15}\)-point integer Walsh–Hadamard transform, inverts the spectral-support indicator, tests the explicit coefficient formula and pairwise cycle autocorrelation, and verifies singleton/pair zero counts. All arithmetic is integral; no probabilistic experiment is used. Its exact tests prove finite exhaustive claims; the accompanying translation-averaging argument proves the unrestricted norm optimum.

## Relationship to prior work

The Petersen graph and its twelve pentagons, six complementary perfect matchings, and binary \([15,6,5]\) cycle code are classical. DeVos–Mkrtchyan–Petrosyan study the special five-cycle two-factor property in their 2008 paper, not an edge-incidence Walsh convolution. The graph catalogue of A. E. Brouwer lists the weight distribution of the six-dimensional cycle code, and an exposition titled *The Petersen code* also lists its codewords by weight. A code weight enumerator describes the number of edge sets at each size; it does not by itself give the signed Walsh value at every character or the inverse support projector. A related publicly indexed coset-leader census examines minimum-distance syndrome corrections rather than these Fourier sums; studies of Petersen spanning-tree convolution concern a different incidence family. The novel assertion assessed here is the signed spectrum **together with** the unusually sparse signed projection kernel and its globally sharp endpoint norm, not the known graph or code enumerator.

## Limitations

The theorem is for the Petersen graph only. There is no generalization here to all cubic graphs, and no claim of an independently audited or formally machine-certified proof. Exact finite checking is essential for the displayed compressed sixty-four-value table; the analytical reduction proves why that table exhausts all original frequencies. An unindexed earlier signed weight-five code calculation could contain an equivalent statement, so a bounded literature comparison does not establish absolute historical priority.

## References

- M. DeVos, V. V. Mkrtchyan, S. S. Petrosyan, *5-cycles and the Petersen graph*, arXiv:0801.3714, first posted 2008-01-24, https://arxiv.org/abs/0801.3714 .
- A. E. Brouwer, *Petersen*, distance-regular graph catalogue, https://aeb.win.tue.nl/drg/graphs/Petersen.html .
- *The Petersen code*, mathematical exposition of the binary cycle-code weight distribution, https://minworks.co.uk/blog/petersen/index.html .
- D. A. Holton, J. Sheehan, *The Petersen Graph*, Cambridge University Press, 1993 (background reference; not relied on for the new spectral assertion).
